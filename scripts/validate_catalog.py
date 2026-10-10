#!/usr/bin/env python3
"""Validate this catalog's structure offline with the Python standard library."""

import argparse
import datetime as dt
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ID = r"\d{4}\.\d{4,5}"
CJK = re.compile(r"[\u3400-\u9fff]")
LINK = re.compile(r"\[[^\]]*\]\(([^\s)]+)\)")
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def body_lines(text):
    """Ignore fenced examples when validating actual Markdown content."""
    fence = None
    for number, line in enumerate(text.splitlines(), 1):
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            continue
        if fence is None:
            yield number, line
    check(fence is None, "Unclosed Markdown fence")


def cells(line):
    return [cell.strip() for cell in re.split(r"(?<!\\)\|", line.strip().strip("|"))]


def anchors(text):
    found = set()
    counts = Counter()
    for _, line in body_lines(text):
        for explicit in re.findall(r'<a\s+(?:id|name)="([^"]+)"', line):
            check(explicit not in found, f"Duplicate explicit anchor: {explicit}")
            found.add(explicit)
        if re.match(r"^#{1,6} ", line):
            heading = re.sub(r"^#+\s+", "", line).strip()
            heading = re.sub(r"<[^>]+>", "", heading)
            key = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
            suffix = f"-{counts[key]}" if counts[key] else ""
            counts[key] += 1
            found.add(key + suffix)
    return found


def paper_ids(text):
    return set(re.findall(r"https://arxiv\.org/abs/(" + ID + r")(?!\d)", text))


def classification(text):
    """Read the original and enhanced table layouts into the same structure."""
    auxiliary = {
        "Table of Contents", "Scope and Terminology", "Reading the Entries",
        "Contributing", "Organization Reference",
    }
    headings, directions, entries = [], [], []
    path = {}
    current = None
    for _, line in body_lines(text):
        heading = re.match(r"^(#{2,3}) (.+)$", line)
        if heading:
            level, title = len(heading[1]), heading[2]
            current = title
            path = {depth: name for depth, name in path.items() if depth < level}
            path[level] = title
            if title not in auxiliary:
                headings.append((level, title))
        if not line.startswith("|"):
            continue
        row = cells(line)
        if current == "Direction Overview" and row[0] != "Direction" and not row[0].startswith("-"):
            directions.append(row[0])
        if line.startswith("| **") and "https://arxiv.org/abs/" in line:
            aid = re.search(r"arxiv\.org/abs/(" + ID + ")", line)[1]
            name = re.search(r"\*\*(.*?)\*\*", row[0])[1]
            if "<br>" in row[0]:
                direction = row[0].split("<br>", 1)[1]
            elif current == "Methods" and len(row) == 4:
                direction = row[1]  # Original baseline has a separate Direction column.
            else:
                direction = ""
            entries.append((aid, tuple(path.values()), name, direction))
    return headings, directions, entries


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", help="Require identical paper inventory, classification, directions, and order to this Git ref")
    args = parser.parse_args()
    documents = {path: path.read_text(encoding="utf-8") for path in ROOT.rglob("*.md") if ".git" not in path.parts}
    anchor_map = {path: anchors(text) for path, text in documents.items()}
    for path, text in documents.items():
        previous_width = None
        for number, line in body_lines(text):
            if line.startswith("|"):
                width = len(cells(line))
                check(previous_width is None or width == previous_width, f"{path.name}:{number}: inconsistent table width")
                previous_width = width
            else:
                previous_width = None
            for target in LINK.findall(line):
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc:
                    check(parsed.scheme == "https", f"Non-HTTPS link: {target}")
                    continue
                dest = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
                check(dest.is_file(), f"Missing local file: {target} in {path.name}:{number}")
                if parsed.fragment and dest in anchor_map:
                    check(unquote(parsed.fragment) in anchor_map[dest], f"Missing anchor: {target} in {path.name}:{number}")

    readme = documents[ROOT / "README.md"]
    audit = documents[ROOT / "docs/SOURCE_AUDIT.md"]
    audited = {}
    for number, line in body_lines(audit):
        if line.startswith('| <a id="paper-'):
            row = cells(line)
            if len(row) != 5:
                continue
            match = re.search(r"arxiv\.org/abs/(" + ID + ")", row[0])
            check(match is not None, f"Audit:{number}: missing paper source")
            if not match:
                continue
            aid = match.group(1)
            check(aid not in audited, f"Duplicate audit identifier: {aid}")
            revision = re.fullmatch(r"(v\d+) · (\d{4}-\d{2}-\d{2})", row[3])
            check(revision is not None, f"Invalid audit revision: {aid}")
            if revision:
                audited[aid] = (row[2], revision[1], row[4][:1])
                try:
                    first, revised = dt.date.fromisoformat(row[2]), dt.date.fromisoformat(revision[2])
                    check(first <= revised, f"Revision precedes submission: {aid}")
                except ValueError:
                    check(False, f"Invalid audit date: {aid}")
            check(row[4].startswith(("A —", "M —")), f"Invalid evidence scope: {aid}")
            check(row[4][:1] != "M" or "https://arxiv.org/html/" in row[4], f"M evidence has no method link: {aid}")

    papers = []
    for number, line in body_lines(readme):
        if line.startswith("| **") and "https://arxiv.org/abs/" in line:
            row = cells(line)
            check(len(row) == 6, f"README:{number}: expected six paper columns")
            if len(row) != 6:
                continue
            match = re.search(r"arxiv\.org/abs/(" + ID + r")\)", row[4])
            check(match is not None, f"README:{number}: invalid canonical source link")
            if not match:
                continue
            aid = match[1]
            papers.append(aid)
            try:
                dt.date.fromisoformat(row[1])
            except ValueError:
                check(False, f"Invalid first submission date: {aid}")
            check(bool(re.search(r"[A-Za-z]", row[2])) and not CJK.search(row[2]), f"Missing English summary: {aid}")
            check(bool(CJK.search(row[3])), f"Missing Chinese summary: {aid}")
            check(not CJK.search(' '.join(row[:3] + row[4:])), f"Chinese outside summary cell: {aid}")
            # Numeric agreement is a useful guard, not a semantic translation test.
            nums = lambda s: re.findall(r"\d+(?:\.\d+)?", s)
            check(nums(row[2]) == nums(row[3]), f"Summary numeric mismatch: {aid}")
            status = re.search(r"\[([AM]) · (v\d+)\]", row[5])
            check(status is not None, f"Missing checked status/version: {aid}")
            check(aid in audited, f"Missing audit record: {aid}")
            if status and aid in audited:
                check((row[1], status[2], status[1]) == audited[aid], f"README/audit mismatch: {aid}")
        elif CJK.search(line):
            check(line == "| Paper and original direction | First submitted | English | 中文 | Source | Checked |", f"README:{number}: Chinese outside paper summaries")

    check(len(papers) == len(set(papers)), "Duplicate paper entries")
    check(set(papers) == set(audited), "README and audit inventories differ")
    total = re.search(r"\*\*(\d+) papers\*\*", readme)
    check(total is not None and int(total[1]) == len(papers), "Displayed paper count is stale")
    headings, directions, entries = classification(readme)
    groups = Counter(entry[1] for entry in entries)
    check(not CJK.search(audit), "Audit should be in English")

    if args.baseline:
        base = subprocess.run(["git", "show", f"{args.baseline}:README.md"], cwd=ROOT, text=True, capture_output=True)
        check(base.returncode == 0, f"Cannot read baseline: {args.baseline}")
        if base.returncode == 0:
            check(paper_ids(base.stdout) == set(papers), "Paper inventory differs from baseline")
            for aid in paper_ids(base.stdout):
                check(f"https://arxiv.org/abs/{aid})" in readme, f"Original paper URL lost: {aid}")
            base_headings, base_directions, base_entries = classification(base.stdout)
            check(headings == base_headings, "Original section names, hierarchy, or order changed")
            check(directions == base_directions, "Direction Overview names or order changed")
            check([e[0] for e in entries] == [e[0] for e in base_entries], "Original paper order changed")
            expected = {entry[0]: entry[1:] for entry in base_entries}
            for aid, path, name, direction in entries:
                check((path, name, direction) == expected.get(aid), f"Original paper placement, name, or direction changed: {aid}")
            def toc(text):
                return text.split("## Table of Contents\n", 1)[1].split("\n## ", 1)[0].split("\n---", 1)[0].strip()
            check("## Table of Contents\n" in readme, "Missing original Table of Contents")
            if "## Table of Contents\n" in readme:
                check(toc(readme) == toc(base.stdout), "Original table-of-contents structure changed")

    if errors:
        print('\n'.join(f"FAIL: {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"PASS: {len(papers)} unique bilingual entries, {len(audited)} audit records, {len(groups)} original paper groups")
    print(f"PASS: {len(documents)} Markdown files; tables, dates, versions, total count, local links and anchors")
    if args.baseline:
        print(f"PASS: all paper identifiers and canonical source URLs preserved from {args.baseline}")
        print(f"PASS: original classification unchanged from {args.baseline}: section names, hierarchy, order, direction overview, paper placement, names, direction labels, entry order, and navigation")
    print("Manual review still required: source truth, bilingual meaning, and external link access.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
