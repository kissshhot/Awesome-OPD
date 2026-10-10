# Recent Literature Search — 2026-10-10

Cutoff and access date: **2026-10-10 (UTC)**. Priority window: **2026-08-10 through 2026-10-10**. Working catalog before this update: **5d575fc**, with 73 unique papers; original classification baseline: **70fe1f2**.

This curated update adds **41** independently identified papers and technical reports: **35** first submitted within the priority window and **6** earlier, directly relevant omissions. The catalog now contains **114** entries. Additions comprise 34 Methods entries and 7 OPD Mechanism Analysis entries. Eleven are system or infrastructure reports that actually use OPD; DiffusionOPSD is a separate method technical report. Every new entry has abstract/metadata and named method or analysis sections checked (**M**). No experiments, code, or weights were reproduced.

## Search Scope and Selection

Parallel discovery covered recent arXiv records, official institutional reports, and author project releases. Queries included `"on-policy distillation"` and `"on-policy self-distillation"` with August, September, October, 2026, technical-report, and author/project terms. Institution-focused queries covered Xiaomi, AMD, NVIDIA, DeepSeek, Meta, AI Singapore, SenseTime, Kuaishou, Reflection, Google/Gemma, Qwen, GLM and Kimi. The arXiv search was also opened directly with exact phrase, all fields, and descending announcement date.

The author-maintained [OPD survey resource](https://github.com/nick7nlp/Awesome-LLM-On-Policy-Distillation) and the [public OPD index](https://github.com/chrisliu298/awesome-on-policy-distillation) supplied discovery leads only. Each included title, author credit, first submission, latest reviewed revision, and mechanism was checked against the original arXiv record and paper. Official release posts were cross-checks, including [AMD Instella-MoE](https://rocm.blogs.amd.com/artificial-intelligence/instella-moe/README.html) and [NVIDIA Nemotron 3 Ultra](https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra-powers-faster-more-efficient-reasoning-for-long-running-agents/).

General search returned unrelated results, and different arXiv search variants exposed differently dated cached snapshots. Search-result counts and snippets were not treated as coverage or metadata guarantees. This is a focused, source-verified update, not a claim to enumerate every paper published in the window. Bare citations to OPD, generic distillation work, and release names without a reviewed OPD mechanism were not sufficient for inclusion.

All original section names, levels, ordering, direction overview, paper placements, names, direction labels, relative order and navigation remain fixed. Additions are appended to an existing table; no new category is introduced. The [exact addition manifest](ADDITIONS_2026-10-10.json) preserves this constraint in validation.

## Added Papers and Reports

Paper links below are canonical primary sources. Exact author credits, version dates, and method-section links are in the [source audit](SOURCE_AUDIT.md). Full English/Chinese introductions are in the [catalog](../README.md).

| Entry | First submitted | Window | Type and inclusion reason | Existing section |
| --- | --- | --- | --- | --- |
| [SGUID](https://arxiv.org/abs/2610.12367) | 2026-10-08 | Priority | Direct on-policy self-distillation: skills are teacher-only privileged context and both policies score student rollouts; contribution is selecting persistently useful skills. | Methods |
| [MetaOPD](https://arxiv.org/abs/2610.11989) | 2026-10-08 | Priority | Direct OPD method with meta-learned token allocation. Reference solutions train the outer weighting objective, not a direct SFT term in the actual student update. | Methods |
| [MiMo-V2.6](https://arxiv.org/abs/2610.11959) | 2026-10-08 | Priority | System report with OPD extension: System report using MOPD2 after mixed RL to combine specialized teachers. | Methods |
| [DIAL-OPD](https://arxiv.org/abs/2610.11659) | 2026-10-08 | Priority | Direct OPD token-selection method; masks supervision, not context or the signed reward itself, and refreshes current-student rollouts. | Methods |
| [ReTeach](https://arxiv.org/abs/2610.11529) | 2026-10-08 | Priority | Direct OPSD. The privileged context is generated attempt history and final reflection; corrected retries are not directly imitated. Method uses token JSD and an EMA teacher. | Methods |
| [Residual Advantage / Co-RA](https://arxiv.org/abs/2610.11519) | 2026-10-08 | Priority | Directly relevant teacher-guided RLVR hybrid: dense teacher signals evaluated on student trajectories; the verifier retains the response-mean advantage. Does not claim a standard KL-distillation objective. | Methods |
| [SAIL](https://arxiv.org/abs/2610.11451) | 2026-10-08 | Priority | System report using OPD: Scientific-agent system report using specialist training followed by multi-teacher OPD. | Methods |
| [PAMA](https://arxiv.org/abs/2610.11423) | 2026-10-08 | Priority | OPD-specific mechanism and membership-auditing analysis. Suitable for the existing OPD Mechanism Analysis subsection, not a direct OPD training method. | OPD Mechanism Analysis |
| [ReCal](https://arxiv.org/abs/2610.11332) | 2026-10-08 | Priority | A preparation method explicitly designed and evaluated for OPD recovery of pruned reasoning models. Inclusion should retain the caveat that its contribution is pre-pruning calibration, not a new OPD loss. | Methods |
| [OPD Skills vs. Knowledge](https://arxiv.org/abs/2610.09639) | 2026-10-07 | Priority | Directly tests which capability changes arise from student rollouts versus divergence choice; addresses OPD mechanism rather than generic knowledge distillation. | OPD Mechanism Analysis |
| [Cross-Tokenizer Supervision Reliability](https://arxiv.org/abs/2610.08448) | 2026-10-06 | Priority | Direct empirical and gradient analysis of student-prefix supervision when teacher/student tokenizers differ; improves the catalogue’s treatment of alignment reliability. | OPD Mechanism Analysis |
| [NP-OPD](https://arxiv.org/abs/2610.07874) | 2026-10-06 | Priority | Direct extension of OPD that changes rollout sources; distinct from existing NPO/NPD and Negative RL. | Methods |
| [SCOUT](https://arxiv.org/abs/2609.38360) | 2026-09-29 | Priority | Direct OPD co-training method that addresses unreliable teacher feedback on student-visited contexts. | Methods |
| [Dr. OPD](https://arxiv.org/abs/2609.38025) | 2026-09-29 | Priority | Direct OPD method that uses task rewards to determine which teacher signals to emphasize. | Methods |
| [RIDE](https://arxiv.org/abs/2609.36484) | 2026-09-29 | Priority | Direct representation-level OPD extension that uses the RL teacher's change from its base to form supervision. | Methods |
| [RetireOPD](https://arxiv.org/abs/2609.20784) | 2026-09-17 | Priority | Direct student-rollout OPD for multi-turn agents, with trained privileged teacher and adaptive withdrawal. | Methods |
| [When EOS Tokens Disagree](https://arxiv.org/abs/2609.20511) | 2026-09-17 | Priority | Direct diagnosis and correction of an OPD failure mechanism. | OPD Mechanism Analysis |
| [SEA-LION-v4.8](https://arxiv.org/abs/2609.18310) | 2026-09-16 | Priority | System report using OPD: Regional-language system report jointly training with SFT examples and online student trajectories. | Methods |
| [GammaOPD](https://arxiv.org/abs/2609.16937) | 2026-09-15 | Priority | New temporal-credit OPD objective with an explicit verifier-reward hybrid. | Methods |
| [DF-OPD](https://arxiv.org/abs/2609.14193) | 2026-09-12 | Priority | Direct OPD recipe replacing external prompts with teacher-generated questions. | Methods |
| [SenseNova-U1.5](https://arxiv.org/abs/2609.11929) | 2026-09-10 | Priority | Visual system report using OPD: Unified visual-model report consolidating four task experts through on-policy velocity-field distillation. | Methods |
| [KuaiRP](https://arxiv.org/abs/2609.11127) | 2026-09-10 | Priority | System report with OPD extension: Role-playing report distilling an SFT-and-RL adapted checkpoint back into its original base model. | Methods |
| [CompassOPD](https://arxiv.org/abs/2609.10154) | 2026-09-09 | Priority | Direct cross-family OPD signal construction and reference regularization. | Methods |
| [Miles v0.1](https://arxiv.org/abs/2609.08368) | 2026-09-08 | Priority | Infrastructure report implementing OPD: Post-training infrastructure report implementing OPD by subtracting a scaled sampled-token student–teacher log-probability gap from token advantages. | Methods |
| [TV-OPD](https://arxiv.org/abs/2609.08341) | 2026-09-08 | Priority | Direct OPD advantage transformation aimed at training stability. | Methods |
| [NeoHorse-1](https://arxiv.org/abs/2609.08183) | 2026-09-08 | Priority | System report with OPD extension: Agent system report scheduling recorded starting contexts by routing-estimated capability demand. | Methods |
| [OPD Data Efficiency and Selection](https://arxiv.org/abs/2609.05198) | 2026-09-04 | Priority | OPD-specific empirical study of data selection, rollout length and supervision. | OPD Mechanism Analysis |
| [One Training Example](https://arxiv.org/abs/2609.04172) | 2026-09-03 | Priority | OPD-specific empirical mechanism analysis of data sufficiency and optimization. | OPD Mechanism Analysis |
| [OPD-then-RL](https://arxiv.org/abs/2609.04108) | 2026-09-03 | Priority | Direct sequential recipe combining OPD and RLVR, with analysis of their interaction. | Methods |
| [TGOPD](https://arxiv.org/abs/2609.02998) | 2026-09-02 | Priority | Direct reliability-gated OPD and RLVR routing method. | Methods |
| [Instella-MoE](https://arxiv.org/abs/2609.00791) | 2026-09-01 | Priority | System report using OPD: AMD system report that merges instruction-following RL gains into a DPO-initialized student. | Methods |
| [DiffusionOPSD](https://arxiv.org/abs/2608.24646) | 2026-08-25 | Priority | Directly studies refreshed learner-state self-distillation for diffusion post-training, adjacent to the catalog's existing DanceOPD entry; not merely a system using OPD. | Methods |
| [S²VOPD](https://arxiv.org/abs/2608.14144) | 2026-08-14 | Priority | Student-prefix distribution matching with an EMA teacher; visual augmentation creates teacher–student asymmetry without an external stronger teacher. | Methods |
| [LOPD](https://arxiv.org/abs/2608.13040) | 2026-08-13 | Priority | Makes training-only teacher context learnable and applies logit-level supervision on current student trajectories, extending the existing skill/context OPD thread. | Methods |
| [SR-OPSD](https://arxiv.org/abs/2608.09745) | 2026-08-10 | Priority | Directly changes teacher target construction and divergence on student rollouts; latest September revision reviewed rather than its older August formulation. | Methods |
| [u-OPSD](https://arxiv.org/abs/2608.06296) | 2026-08-06 | Earlier omission | Constructs privileged context from on-policy samples and matches teacher distributions on student-generated disagreeing trajectories; nearby omission just before the priority window. | Methods |
| [Demystifying OPD](https://arxiv.org/abs/2607.13399) | 2026-07-15 | Earlier omission | Analyzes the same teacher log-ratio guidance used in catalogued OPD methods and adds concrete in-loop regulation; July omission adjacent to existing SEED rather than unrelated RL. | OPD Mechanism Analysis |
| [GR2](https://arxiv.org/abs/2606.31984) | 2026-06-30 | Earlier omission | Recommendation system report using OPD; earlier omission: Industrial recommendation report transferring a frozen teacher's reasoning into a student reranker. | Methods |
| [Nemotron 3 Ultra](https://arxiv.org/abs/2606.15007) | 2026-06-12 | Earlier omission | System report using OPD; earlier omission: NVIDIA system report consolidating domain specialists through asynchronous multi-teacher OPD on student-generated rollouts. | Methods |
| [DeepSeek-V4](https://arxiv.org/abs/2606.19348) | 2026-04-26 | Earlier omission | System report using OPD; earlier omission: System report merging domain experts trained by specialized SFT and RL through multi-teacher OPD. | Methods |
| [Self-Distilled Reasoner / OPSD](https://arxiv.org/abs/2601.18734) | 2026-01-26 | Earlier omission | Foundational privileged-context OPSD mechanism used by already-listed papers; an earlier direct omission. | Methods |

The earlier omissions are Self-Distilled Reasoner / OPSD (the privileged-context mechanism used by already-listed papers), DeepSeek-V4, Nemotron 3 Ultra and GR2 (documented industrial OPD stages alongside the catalog's existing reports), Demystifying OPD (a July mechanism study adjacent to the existing SEED timeframe), and u-OPSD (four days before the priority window). They are recorded with their real first-submission dates, not presented as new October releases.

## Existing Revisions Rechecked

These recent revisions already matched the local catalog, so no second entry or unnecessary replacement was made:

| Existing entry | Primary source | Reviewed version | Revision date | Outcome |
| --- | --- | --- | --- | --- |
| NPO / NPD | [2604.20733](https://arxiv.org/abs/2604.20733) | v2 | 2026-10-01 | Retained the existing distinction between off-policy NPO and on-policy NPD. |
| OVD | [2601.21968](https://arxiv.org/abs/2601.21968) | v2 | 2026-09-28 | Already current. |
| SkillRL | [2602.08234](https://arxiv.org/abs/2602.08234) | v2 | 2026-10-07 | Already current. |
| HAT / TaoLive | [2608.15763](https://arxiv.org/abs/2608.15763) | v5 | 2026-10-04 | Already current; the report's general OPD stage remains distinct from subsequent RL. |

All 73 existing entries retain the review already completed on this same cutoff date. This follow-up specifically refreshed the four records above; it does not claim a second full read of all 73 papers.

## Scope and Metadata Decisions

- NP-OPD is a new identifier, distinct from the existing temporal NPO/NPD and Negative RL papers. Its mixture may include pre-generated negative-policy trajectories, and its all-negative setting is off-policy for the student.
- ReCal changes pruning calibration before SFT and OPD recovery. It is not described as a new OPD loss. Residual Advantage is a verifier-reward hybrid, and OPD-then-RL is sequential rather than simultaneous objective mixing.
- RIDE assumes compatible representation spaces and a shared initialization. Cross-tokenizer supervision findings are limited to the studied alignment losses. The skills/knowledge study finds divergence-dependent factual transfer; its title is not repeated as a universal impossibility claim.
- System reports are identified as such inside both summaries. SAIL specifies a general masked divergence, SenseNova-U1.5 matches flow velocities, and Miles implements OPD infrastructure. MiMo-V2.6's separate Qwen release uses teacher-data SFT and is not conflated with its main MOPD2 stage.
- DiffusionOPSD constructs reward-adjusted self-targets rather than relying on an external teacher. Its original PDF was read after the web reader rejected the large file. First submission is August 25 despite an August 26 cover date. The paper-linked repository labels itself an external implementation, so no official-code claim is made.
- DeepSeek-V4's arXiv record gives **2026-04-26** despite its `2606` identifier; this date was independently rechecked. NeoHorse-1's current abstract record gives **2026-09-08**, overriding the September 7 date in a cached search page. RetireOPD uses the latest v2 author list, not an older secondary-index list. DF-OPD uses the latest v4 title and October 7 revision.

## Excluded or Unverified Candidates

| Candidate | Evidence inspected | Decision |
| --- | --- | --- |
| Gemma 4 Technical Report | [Original report v2](https://arxiv.org/html/2607.02770v2) | No OPD mechanism established from the inspected report; a third-party index is insufficient. Not added. |
| LongCat-DeepResearch Technical Report | [Original report v1](https://arxiv.org/html/2609.36071v1), Section 3.2 | Teacher-harness trajectory construction is described, but no OPD objective or student-rollout feedback mechanism was established. Not selected for this OPD-focused update. |
| Reflection Beam | [Official October 5 preview](https://reflection.ai/blog/introducing-beam) | MOPD is named, but a detailed technical report was promised later in October. No independently reviewed rollout/objective specification; pending, not a fabricated paper entry. |
| MiMo-V2.5-Pro release | Official launch inspected in the report search | No separately verified report in this pass; the detailed MiMo-V2.6 report is included. No duplicate release-only entry. |
| GLM-5.3, Qwen3.8 and Kimi K3 release leads | Targeted official-source searches | No reviewed original OPD method section established in this pass; no entry inferred from release names. This is not a claim that no report exists. |
| Draft-OPD, 2605.29343 | [Author repository](https://github.com/Simplified-Reasoning/Draft-OPD) | May paper surfaced through a September repository update. Exact paper metadata and methods were not audited in this pass; deferred outside the priority window. |

Other discovery-only search hits were not promoted to verified catalog entries. Pending candidates do not change the source status of included items.

## Validation and Limits

Run the structural check from the repository root:

```sh
python3 scripts/validate_catalog.py --baseline 70fe1f2 --additions docs/ADDITIONS_2026-10-10.json --as-of 2026-10-10
git diff --check
```

The check requires all 73 original entries plus exactly the 41 manifest additions. It checks the original taxonomy and ordering, existing-category placement for additions, unique identifiers, paired summaries, numeric parity, valid dates no later than the cutoff, audit/version agreement, table shapes, local files and anchors. Primary-source access and bilingual meaning were checked separately. Remote retrieval demonstrates access at review time, not permanent availability or experimental validity.

This update is local only. No push, pull request, merge, deployment, or publication is part of the review.
