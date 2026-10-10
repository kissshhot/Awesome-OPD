# Contributing

Contributions should make this reading list easier to navigate and more reliable. Prefer a precise correction or a clearly relevant paper over increasing the paper count.

## Scope

Use the [README scope criteria](README.md#scope-and-terminology) to identify who generates the training trajectories and where teacher feedback is applied. Distinguish current-student sampling from fixed offline data, privileged-teacher trajectories, and teacher-free self-training. If a paper contains multiple regimes, describe the relevant branch explicitly.

Assign each paper to one primary topic. Use the existing English tags to describe overlapping directions such as white-box access, privileged-information self-distillation, agents, multiple teachers, or an RL hybrid. Do not create a second row for the same arXiv identifier or classify a method solely from its title.

## Sources and Evidence

1. Read the original paper or official author source. Confirm the identifier, current title, and first submission date from the source record.
2. Record the exact reviewed version and its revision date in [SOURCE_AUDIT.md](docs/SOURCE_AUDIT.md). An arXiv identifier's month can differ from the first submission month.
3. Use **A** when the description is supported by the abstract and metadata. Use **M** only after reading and citing the relevant method sections as well. A working link alone is not a content check.
4. Explain sampling, teacher access, and the training signal in the summary. If those details are ambiguous, inspect the method before asserting strict OPD membership; otherwise mark the uncertainty and place the paper with adjacent work.
5. For any experimental number, include the model, benchmark/version, metric, comparison, and the table or section supporting it. Distinguish percentage points from relative percentages. Do not mix versions or repeat a historical leaderboard claim as a current ranking.

These statuses describe source inspection, not experimental reproduction. If a source cannot be read, state the limitation rather than claiming verification. A proposed unverified addition should remain in the contribution discussion until its identity and scope can be established.

## Language and Entry Format

Keep headings, navigation, tags, metadata, and repository guidance in English. Provide parallel **English and Chinese paper summaries** in the same row. Both summaries must include the same method, scope qualifications, and any retained results; neither language should add a stronger claim.

Keep summaries concise, usually one or two sentences. Preserve the canonical paper link and use a familiar method name as the display label; put the complete current title in the audit. Sort each topic by first submission date, newest first, then by identifier, descending, for ties.

Use the six-column README format below. Replace every placeholder and add a corresponding audit row with a unique `paper-YYMM-NNNNN` anchor.

```markdown
| Paper and tags | First submitted | English | Chinese summary | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **Method name**<br>White-box; RL hybrid | YYYY-MM-DD | Mechanism and scope in English. | Matching Chinese translation. | [arXiv YYMM.NNNNN](https://arxiv.org/abs/YYMM.NNNNN) | [A · v1](docs/SOURCE_AUDIT.md#paper-YYMM-NNNNN) |
```

Keep the existing Chinese-summary column header when editing the actual catalog. Escape a literal pipe as `\|` inside a table cell, and use `<br>` only for compact line breaks. Keep old section anchors when reorganizing topics so existing links continue to work.

## Local Validation

This is a documentation repository. The structural validator uses Python 3's standard library; no package installation or application build is required.

```sh
python3 scripts/validate_catalog.py
git diff --check
```

When reorganizing without changing the paper inventory, compare against the pre-edit commit:

```sh
python3 scripts/validate_catalog.py --baseline 70fe1f2
```

Use the appropriate pre-edit commit for later work. Baseline mode checks exact paper-identifier and canonical paper-link preservation. Do not use it to reject an intentional, reviewed addition. Update the displayed total and topic counts whenever the inventory changes.

The validator checks table shapes, duplicate papers, dates, audit versions/statuses, summary language presence, numeric parity, topic counts, sorting, relative file links, and local anchors. It does not check scientific truth, translation meaning, or remote availability. Read both summaries side by side and open every changed external link, recording access limitations separately from broken links.

Before submitting a contribution, preview the Markdown tables, review the diff for unrelated edits, and describe what changed with the precise source evidence. Preserve existing valid paper links; a title change or a new revision is not a new paper.
