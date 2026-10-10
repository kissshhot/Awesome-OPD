# Contributing

Contributions should make this reading list easier to navigate and more reliable. Prefer a precise correction or a clearly relevant paper over increasing the paper count.

## Scope

Use the [README scope criteria](README.md#scope-and-terminology) to identify who generates the training trajectories and where teacher feedback is applied. Distinguish current-student sampling from fixed offline data, privileged-teacher trajectories, and teacher-free self-training. If a paper contains multiple regimes, describe the relevant branch explicitly.

Preserve the existing classification: Surveys, Direction Overview, Methods, and Related Work with its six named subtopics. Keep section names, heading levels, section order, existing paper placement, per-paper direction labels, and existing entry order unchanged when editing the catalog. Append verified additions to the most relevant existing section and use the existing direction vocabulary. Do not create a second row for the same arXiv identifier.

When an original direction label has a conceptual boundary, explain the actual sampling process and feedback in both summaries without moving or relabeling the paper. For example, SSD retains its original Methods placement and Black-Box OPD label, while its summary states that it is teacher-free and does not meet the strict teacher-feedback criterion. A factual clarification does not authorize a taxonomy change.

## Sources and Evidence

1. Read the original paper or official author source. Confirm the identifier, current title, and first submission date from the source record.
2. Record the exact reviewed version and its revision date in [SOURCE_AUDIT.md](docs/SOURCE_AUDIT.md). An arXiv identifier's month can differ from the first submission month.
3. Use **A** when the description is supported by the abstract and metadata. Use **M** only after reading and citing the relevant method sections as well. A working link alone is not a content check.
4. Explain sampling, teacher access, and the training signal in the summary. If those details are ambiguous, inspect the method before asserting strict OPD membership; otherwise mark the uncertainty in both summaries while retaining the original classification.
5. For any experimental number, include the model, benchmark/version, metric, comparison, and the table or section supporting it. Distinguish percentage points from relative percentages. Do not mix versions or repeat a historical leaderboard claim as a current ranking.

These statuses describe source inspection, not experimental reproduction. If a source cannot be read, state the limitation rather than claiming verification. A proposed unverified addition should remain in the contribution discussion until its identity and scope can be established.

For recent-literature updates, state a search cutoff and priority window, record queries and excluded or unverified candidates, and verify author credits as well as dates. Use the latest version available by the cutoff, not a later revision. Record revisions under the existing identifier. For technical reports, read the actual OPD section and distinguish a new distillation method from a system that uses OPD; a citation to OPD alone is not enough. The [2026-10-10 search record](docs/RECENT_SEARCH_2026-10-10.md) shows the evidence trail for the current additions.

## Language and Entry Format

Keep headings, navigation, tags, metadata, and repository guidance in English. Provide parallel **English and Chinese paper summaries** in the same row. Both summaries must include the same method, scope qualifications, and any retained results; neither language should add a stronger claim.

Keep summaries concise, usually one or two sentences. Preserve the canonical paper link and existing method name as the display label; put the complete current title in the audit. Show the verified first submission date without reordering existing entries.

Use the six-column README format below. Replace every placeholder and add a corresponding audit row with a unique `paper-YYMM-NNNNN` anchor.

```markdown
| Paper and original direction | First submitted | English | Chinese summary | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **Method name**<br>Original direction labels | YYYY-MM-DD | Mechanism and scope in English. | Matching Chinese translation. | [arXiv YYMM.NNNNN](https://arxiv.org/abs/YYMM.NNNNN) | [A · v1](docs/SOURCE_AUDIT.md#paper-YYMM-NNNNN) |
```

Keep the existing Chinese-summary column header when editing the actual catalog. Escape a literal pipe as `\|` inside a table cell, and use `<br>` to separate a method name from its original direction labels. Omit the line break and direction text for entries that had no direction label. Preserve the existing section headings and anchors.

## Local Validation

This is a documentation repository. The structural validator uses Python 3's standard library; no package installation or application build is required.

```sh
python3 scripts/validate_catalog.py
git diff --check
```

For the current authorized additions, verify preservation of the original inventory and classification plus the explicit addition manifest:

```sh
python3 scripts/validate_catalog.py --baseline 70fe1f2 --additions docs/ADDITIONS_2026-10-10.json --as-of 2026-10-10
```

Baseline mode compares section names, heading levels, section order, the direction overview, every original paper's section and direction labels, and relative entry order, as well as paper identifiers and canonical links. Without `--additions`, it still requires the exact original inventory. With `--additions`, it accepts only the manifest's exact additional identifiers, display names, directions, and existing section paths; it still rejects a moved or missing original entry, a new category, or an unlisted addition. Extend the reviewed manifest explicitly for a future authorized addition rather than resetting the baseline or weakening preservation checks. Update the displayed total only when the inventory changes.

The validator also checks table shapes, duplicate papers, valid dates no later than the cutoff (today UTC by default), audit versions/statuses, summary language presence, numeric parity, relative file links, and local anchors. It does not check scientific truth, translation meaning, or remote availability. Read both summaries side by side and open every changed external link, recording access limitations separately from broken links.

Before submitting a contribution, preview the Markdown tables, review the diff for unrelated edits, and describe what changed with the precise source evidence. Preserve existing valid paper links; a title change or a new revision is not a new paper.
