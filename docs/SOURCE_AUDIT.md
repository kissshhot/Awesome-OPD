# Source Audit

Review date: **2026-10-10**. Inventory baseline: **70fe1f235f59c77650ce535b856d5bdf22de4e9e**.

The baseline README contained **73 unique arXiv papers**: 1 survey, 46 method entries, and 26 related-work entries. Its badge reported 70. All 73 paper identifiers and canonical source URLs are retained; no papers were added. Decorative badges with stale counts were replaced by an auditable total. Original section anchors are retained as compatibility aliases.

The organizational reference was inspected at **ecbf5d7**, including its numbered sections, tabular summaries, date/source fields, and verification column. Its topic labels, claims, and blanket confirmation marks were not used as evidence for OPD papers.

## Review Method and Limits

Every entry was checked against its arXiv abstract page for identity, current title, first submission date, revision, and the mechanism summarized in the README. **A** denotes that scope. **M** additionally denotes inspection of the method sections linked below. Category placement is an editorial interpretation of the documented sampling process and feedback, not an author-issued certification. Experiments, code, and model weights were not reproduced or audited.

The source links resolve to the current arXiv entry. The reviewed version and its date are recorded explicitly so that a later revision is not silently treated as already reviewed. Titles below are canonical titles at review time; README labels retain familiar method names. For v1 entries, the revision date repeats the first submission date.

## Material Corrections

| Entry | Evidence and resulting change |
| --- | --- |
| SSD | The v2 abstract explicitly describes learning from raw model outputs without a teacher or verifier. Moved from black-box OPD to adjacent teacher-free self-training. |
| NPO / NPD | The v2 abstract distinguishes off-policy transfer of verified future-self trajectories (NPO) from on-policy token feedback on learner trajectories (NPD). The row covers both without assigning NPO itself to strict OPD. |
| Negative RL | Submission history gives 2025-06-02, replacing 2026.06 in the baseline. |
| TrOPD | Submission history gives 2026-05-31 despite the 2606 identifier. Its summary also retains both on-policy supervision and off-policy prefix guidance. |
| DDT / On-Policy SFT | Sections 3.1–3.2 describe loss reweighting and hinted dataset rewriting. Kept as distribution-aware SFT rather than a continually refreshed OPD loop. |
| Lightning OPD | Section 3.2 samples from the SFT checkpoint once and reuses cached teacher probabilities. Labeled an offline approximation, preserving the authors' method name. |
| HDPO | Sections 3.2–3.3 define the JSD training set using correct privileged-teacher trajectories. The distillation branch is not sampled from the unprivileged student. |
| SCoRe | Sections 4.1–4.3 use prompted textual teacher corrections, SFT, and later short-horizon RL. Removed the white-box label and the implication that only one intervention is possible per trajectory. |
| OpenClaw-RL | Sections 3.1–3.2 use a hint-conditioned self-teacher's probabilities and top-K overlap. Replaced the black-box label on the distillation branch with white-box self-distillation. |
| GLM-5 | Section 3.5 places cross-stage OPD at the final stage and replaces the advantage with the teacher-student log-probability gap. Described this specific stage rather than implying joint outcome-reward training throughout. |
| PBSD | Section 3.2 uses Bayesian evidence for turn-level advantage calibration, preserving reward direction. Distinguished this from directly copying privileged actions. |
| HAT / TaoLive | Section 3.4 identifies the pre-HSA-SFT base model as the General OPD teacher on student-sampled Tulu instructions. Preserved the distinction between that stage and subsequent harness-augmented RL. |
| Survey, OVD, OPRD, and other revised papers | Summaries follow the versions recorded below. Updated the survey axes, OVD's retention/replacement mechanism and inference-feedback caveat, and OPRD's representation/bridge scope. Removed unsupported rankings, unqualified universals, and detailed numeric claims not needed for a concise method description. |

## Per-Paper Evidence

All rows were checked on the review date above. Method links identify the additional evidence used for **M** rows. For **A** rows, the abstract and submission history are the evidence; no full-paper review is implied.

| Source | Canonical title | First submitted | Reviewed revision | Evidence |
| --- | --- | --- | --- | --- |
| <a id="paper-2210-10760"></a>[2210.10760](https://arxiv.org/abs/2210.10760) | Scaling Laws for Reward Model Overoptimization | 2022-10-19 | v1 · 2022-10-19 | A — abstract and submission history |
| <a id="paper-2504-07164"></a>[2504.07164](https://arxiv.org/abs/2504.07164) | R2E-Gym: Procedural Environments and Hybrid Verifiers for Scaling Open-Weights SWE Agents | 2025-04-09 | v1 · 2025-04-09 | A — abstract and submission history |
| <a id="paper-2504-21798"></a>[2504.21798](https://arxiv.org/abs/2504.21798) | SWE-smith: Scaling Data for Software Engineering Agents | 2025-04-30 | v2 · 2025-05-21 | A — abstract and submission history |
| <a id="paper-2505-10978"></a>[2505.10978](https://arxiv.org/abs/2505.10978) | Group-in-Group Policy Optimization for LLM Agent Training | 2025-05-16 | v3 · 2025-10-28 | A — abstract and submission history |
| <a id="paper-2505-20732"></a>[2505.20732](https://arxiv.org/abs/2505.20732) | SPA-RL: Reinforcing LLM Agents via Stepwise Progress Attribution | 2025-05-27 | v1 · 2025-05-27 | A — abstract and submission history |
| <a id="paper-2506-01347"></a>[2506.01347](https://arxiv.org/abs/2506.01347) | The Surprising Effectiveness of Negative Reinforcement in LLM Reasoning | 2025-06-02 | v2 · 2025-10-25 | A — abstract and submission history |
| <a id="paper-2506-02208"></a>[2506.02208](https://arxiv.org/abs/2506.02208) | KDRL: Post-Training Reasoning LLMs via Unified Knowledge Distillation and Reinforcement Learning | 2025-06-02 | v1 · 2025-06-02 | A — abstract and submission history |
| <a id="paper-2506-10954"></a>[2506.10954](https://arxiv.org/abs/2506.10954) | SWE-Factory: Your Automated Factory for Issue Resolution Training Data and Evaluation Benchmarks | 2025-06-12 | v3 · 2026-01-05 | A — abstract and submission history |
| <a id="paper-2508-13167"></a>[2508.13167](https://arxiv.org/abs/2508.13167) | Chain-of-Agents: End-to-End Agent Foundation Models via Multi-Agent Distillation and Agentic RL | 2025-08-06 | v1 · 2025-08-06 | A — abstract and submission history |
| <a id="paper-2509-08755"></a>[2509.08755](https://arxiv.org/abs/2509.08755) | AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning | 2025-09-10 | v1 · 2025-09-10 | A — abstract and submission history |
| <a id="paper-2509-14257"></a>[2509.14257](https://arxiv.org/abs/2509.14257) | Student-Centered Distillation Narrows the Agentic Gap Between Small and Large LLMs | 2025-09-12 | v3 · 2026-07-23 | M — abstract/history + [Sections 4.1–4.3](https://arxiv.org/html/2509.14257v3) |
| <a id="paper-2510-04206"></a>[2510.04206](https://arxiv.org/abs/2510.04206) | AgentRL: Scaling Agentic Reinforcement Learning with a Multi-Turn, Multi-Task Framework | 2025-10-05 | v1 · 2025-10-05 | A — abstract and submission history |
| <a id="paper-2510-16907"></a>[2510.16907](https://arxiv.org/abs/2510.16907) | VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents | 2025-10-19 | v1 · 2025-10-19 | A — abstract and submission history |
| <a id="paper-2511-16108"></a>[2511.16108](https://arxiv.org/abs/2511.16108) | SkyRL-Agent: Efficient RL Training for Multi-turn LLM Agent | 2025-11-20 | v1 · 2025-11-20 | A — abstract and submission history |
| <a id="paper-2511-17579"></a>[2511.17579](https://arxiv.org/abs/2511.17579) | Multi-Value Alignment for LLMs via Value Decorrelation and Extrapolation | 2025-11-15 | v1 · 2025-11-15 | A — abstract and submission history |
| <a id="paper-2601-02780"></a>[2601.02780](https://arxiv.org/abs/2601.02780) | MiMo-V2-Flash Technical Report | 2026-01-06 | v2 · 2026-01-08 | A — abstract and submission history |
| <a id="paper-2601-05242"></a>[2601.05242](https://arxiv.org/abs/2601.05242) | GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization | 2026-01-08 | v1 · 2026-01-08 | A — abstract and submission history |
| <a id="paper-2601-16206"></a>[2601.16206](https://arxiv.org/abs/2601.16206) | Computer Environments Elicit General Agentic Intelligence in LLMs | 2026-01-22 | v3 · 2026-04-08 | A — abstract and submission history |
| <a id="paper-2601-20802"></a>[2601.20802](https://arxiv.org/abs/2601.20802) | Reinforcement Learning via Self-Distillation | 2026-01-28 | v2 · 2026-02-16 | A — abstract and submission history |
| <a id="paper-2601-21968"></a>[2601.21968](https://arxiv.org/abs/2601.21968) | OVD: On-policy Verbal Distillation | 2026-01-29 | v2 · 2026-09-28 | A — abstract and submission history |
| <a id="paper-2602-04942"></a>[2602.04942](https://arxiv.org/abs/2602.04942) | Privileged Information Distillation for Language Models | 2026-02-04 | v3 · 2026-02-16 | A — abstract and submission history |
| <a id="paper-2602-08234"></a>[2602.08234](https://arxiv.org/abs/2602.08234) | SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning | 2026-02-09 | v2 · 2026-10-07 | A — abstract and submission history |
| <a id="paper-2602-12125"></a>[2602.12125](https://arxiv.org/abs/2602.12125) | Learning beyond Teacher: Generalized On-Policy Distillation with Reward Extrapolation | 2026-02-12 | v2 · 2026-02-26 | A — abstract and submission history |
| <a id="paper-2602-12222"></a>[2602.12222](https://arxiv.org/abs/2602.12222) | Towards On-Policy SFT: Distribution Discriminant Theory and its Applications in LLM Training | 2026-02-12 | v2 · 2026-03-14 | M — abstract/history + [Sections 3.1–3.2](https://arxiv.org/html/2602.12222v2) |
| <a id="paper-2602-15763"></a>[2602.15763](https://arxiv.org/abs/2602.15763) | GLM-5: from Vibe Coding to Agentic Engineering | 2026-02-17 | v2 · 2026-02-24 | M — abstract/history + [Section 3.5, Equation 2](https://arxiv.org/html/2602.15763v2) |
| <a id="paper-2602-22495"></a>[2602.22495](https://arxiv.org/abs/2602.22495) | Reinforcement-aware Knowledge Distillation for LLM Reasoning | 2026-02-26 | v3 · 2026-06-17 | A — abstract and submission history |
| <a id="paper-2603-07079"></a>[2603.07079](https://arxiv.org/abs/2603.07079) | Entropy-Aware On-Policy Distillation of Language Models | 2026-03-07 | v3 · 2026-06-12 | A — abstract and submission history |
| <a id="paper-2603-10165"></a>[2603.10165](https://arxiv.org/abs/2603.10165) | OpenClaw-RL: Train Any Agent Simply by Talking | 2026-03-10 | v2 · 2026-05-11 | M — abstract/history + [Sections 3.1–3.2, Equation 1](https://arxiv.org/html/2603.10165v2) |
| <a id="paper-2603-11137"></a>[2603.11137](https://arxiv.org/abs/2603.11137) | Scaling Reasoning Efficiently via Relaxed On-Policy Distillation | 2026-03-11 | v1 · 2026-03-11 | A — abstract and submission history |
| <a id="paper-2603-19220"></a>[2603.19220](https://arxiv.org/abs/2603.19220) | Nemotron-Cascade 2: Post-Training LLMs with Cascade RL and Multi-Domain On-Policy Distillation | 2026-03-19 | v2 · 2026-03-22 | A — abstract and submission history |
| <a id="paper-2603-22446"></a>[2603.22446](https://arxiv.org/abs/2603.22446) | Sparse but Critical: A Token-Level Analysis of Distributional Shifts in RLVR Fine-Tuning of LLMs | 2026-03-23 | v1 · 2026-03-23 | A — abstract and submission history |
| <a id="paper-2603-23871"></a>[2603.23871](https://arxiv.org/abs/2603.23871) | HDPO: Hybrid Distillation Policy Optimization via Privileged Self-Distillation | 2026-03-25 | v1 · 2026-03-25 | M — abstract/history + [Sections 3.2–3.3, Algorithm 1](https://arxiv.org/html/2603.23871v1) |
| <a id="paper-2603-25562"></a>[2603.25562](https://arxiv.org/abs/2603.25562) | Revisiting On-Policy Distillation: Empirical Failure Modes and Simple Fixes | 2026-03-26 | v2 · 2026-04-27 | A — abstract and submission history |
| <a id="paper-2604-00626"></a>[2604.00626](https://arxiv.org/abs/2604.00626) | A Survey of On-Policy Distillation for Large Language Models | 2026-04-01 | v4 · 2026-06-18 | A — abstract and submission history |
| <a id="paper-2604-01193"></a>[2604.01193](https://arxiv.org/abs/2604.01193) | Embarrassingly Simple Self-Distillation Improves Code Generation | 2026-04-01 | v2 · 2026-06-24 | A — abstract and submission history |
| <a id="paper-2604-02288"></a>[2604.02288](https://arxiv.org/abs/2604.02288) | Unifying Group-Relative and Self-Distillation Policy Optimization via Sample Routing | 2026-04-02 | v1 · 2026-04-02 | A — abstract and submission history |
| <a id="paper-2604-03128"></a>[2604.03128](https://arxiv.org/abs/2604.03128) | Self-Distilled RLVR | 2026-04-03 | v2 · 2026-04-08 | A — abstract and submission history |
| <a id="paper-2604-08527"></a>[2604.08527](https://arxiv.org/abs/2604.08527) | Demystifying OPD: Length Inflation and Stabilization Strategies for Large Language Models | 2026-04-09 | v1 · 2026-04-09 | A — abstract and submission history |
| <a id="paper-2604-10674"></a>[2604.10674](https://arxiv.org/abs/2604.10674) | Skill-SD: Skill-Conditioned Self-Distillation for Multi-turn LLM Agents | 2026-04-12 | v1 · 2026-04-12 | A — abstract and submission history |
| <a id="paper-2604-10688"></a>[2604.10688](https://arxiv.org/abs/2604.10688) | SCOPE: Signal-Calibrated On-Policy Distillation Enhancement with Dual-Path Adaptive Weighting | 2026-04-12 | v2 · 2026-05-30 | A — abstract and submission history |
| <a id="paper-2604-13010"></a>[2604.13010](https://arxiv.org/abs/2604.13010) | Lightning OPD: Efficient Post-Training for Large Reasoning Models with Offline On-Policy Distillation | 2026-04-14 | v3 · 2026-09-26 | M — abstract/history + [Section 3.2](https://arxiv.org/html/2604.13010v3) |
| <a id="paper-2604-13016"></a>[2604.13016](https://arxiv.org/abs/2604.13016) | Rethinking On-Policy Distillation of Large Language Models: Phenomenology, Mechanism, and Recipe | 2026-04-14 | v2 · 2026-04-15 | A — abstract and submission history |
| <a id="paper-2604-20733"></a>[2604.20733](https://arxiv.org/abs/2604.20733) | Learning from the Near Future: Temporal Self-Distillation for RLVR | 2026-04-22 | v2 · 2026-10-01 | A — abstract and submission history |
| <a id="paper-2604-24005"></a>[2604.24005](https://arxiv.org/abs/2604.24005) | TCOD: Exploring Temporal Curriculum in On-Policy Distillation for Multi-turn Autonomous Agents | 2026-04-27 | v3 · 2026-04-29 | A — abstract and submission history |
| <a id="paper-2605-01347"></a>[2605.01347](https://arxiv.org/abs/2605.01347) | MAD-OPD: Breaking the Ceiling in On-Policy Distillation via Multi-Agent Debate | 2026-05-02 | v1 · 2026-05-02 | A — abstract and submission history |
| <a id="paper-2605-03677"></a>[2605.03677](https://arxiv.org/abs/2605.03677) | Uni-OPD: Unifying On-Policy Distillation with a Dual-Perspective Recipe | 2026-05-05 | v2 · 2026-07-06 | A — abstract and submission history |
| <a id="paper-2605-05750"></a>[2605.05750](https://arxiv.org/abs/2605.05750) | RVPO: Risk-Sensitive Alignment via Variance Regularization | 2026-05-07 | v1 · 2026-05-07 | A — abstract and submission history |
| <a id="paper-2605-07725"></a>[2605.07725](https://arxiv.org/abs/2605.07725) | SOD: Step-wise On-policy Distillation for Small Language Model Agents | 2026-05-08 | v3 · 2026-08-18 | A — abstract and submission history |
| <a id="paper-2605-07865"></a>[2605.07865](https://arxiv.org/abs/2605.07865) | KL for a KL: On-Policy Distillation with Control Variate Baseline | 2026-05-08 | v1 · 2026-05-08 | A — abstract and submission history |
| <a id="paper-2605-08142"></a>[2605.08142](https://arxiv.org/abs/2605.08142) | Reasoning emerges from constrained inference manifolds in large language models | 2026-05-02 | v1 · 2026-05-02 | A — abstract and submission history |
| <a id="paper-2605-11739"></a>[2605.11739](https://arxiv.org/abs/2605.11739) | Learning to Foresee: Unveiling the Unlocking Efficiency of On-Policy Distillation | 2026-05-12 | v3 · 2026-05-21 | A — abstract and submission history |
| <a id="paper-2605-13641"></a>[2605.13641](https://arxiv.org/abs/2605.13641) | Multi-Objective and Mixed-Reward Reinforcement Learning via Reward-Decorrelated Policy Optimization | 2026-05-13 | v1 · 2026-05-13 | A — abstract and submission history |
| <a id="paper-2605-15155"></a>[2605.15155](https://arxiv.org/abs/2605.15155) | Self-Distilled Agentic Reinforcement Learning | 2026-05-14 | v1 · 2026-05-14 | A — abstract and submission history |
| <a id="paper-2605-21468"></a>[2605.21468](https://arxiv.org/abs/2605.21468) | You Only Need Minimal RLVR Training: Extrapolating LLMs via Rank-1 Trajectories | 2026-05-20 | v1 · 2026-05-20 | A — abstract and submission history |
| <a id="paper-2605-25582"></a>[2605.25582](https://arxiv.org/abs/2605.25582) | Extreme Region Policy Distillation | 2026-05-25 | v2 · 2026-06-04 | A — abstract and submission history |
| <a id="paper-2605-27354"></a>[2605.27354](https://arxiv.org/abs/2605.27354) | Guiding LLM Post-training Data Engineering with Model Internals from Sparse Autoencoders | 2026-05-26 | v1 · 2026-05-26 | A — abstract and submission history |
| <a id="paper-2606-01249"></a>[2606.01249](https://arxiv.org/abs/2606.01249) | Trust Region On-Policy Distillation | 2026-05-31 | v3 · 2026-06-17 | A — abstract and submission history |
| <a id="paper-2606-04036"></a>[2606.04036](https://arxiv.org/abs/2606.04036) | Self-Distilled Policy Gradient | 2026-06-02 | v1 · 2026-06-02 | A — abstract and submission history |
| <a id="paper-2606-06021"></a>[2606.06021](https://arxiv.org/abs/2606.06021) | OPRD: On-Policy Representation Distillation | 2026-06-04 | v4 · 2026-06-20 | A — abstract and submission history |
| <a id="paper-2606-07082"></a>[2606.07082](https://arxiv.org/abs/2606.07082) | On the Geometry of On-Policy Distillation | 2026-06-05 | v3 · 2026-06-14 | A — abstract and submission history |
| <a id="paper-2606-09348"></a>[2606.09348](https://arxiv.org/abs/2606.09348) | PBSD: Privileged Bayesian Self-Distillation for Long-Horizon Credit Assignment | 2026-06-08 | v2 · 2026-07-06 | M — abstract/history + [Section 3.2](https://arxiv.org/html/2606.09348v2) |
| <a id="paper-2606-09821"></a>[2606.09821](https://arxiv.org/abs/2606.09821) | Rethinking the Divergence Regularization in LLM RL | 2026-06-08 | v1 · 2026-06-08 | A — abstract and submission history |
| <a id="paper-2606-11709"></a>[2606.11709](https://arxiv.org/abs/2606.11709) | RLCSD: Reinforcement Learning with Contrastive On-Policy Self-Distillation | 2026-06-10 | v2 · 2026-09-14 | A — abstract and submission history |
| <a id="paper-2606-13657"></a>[2606.13657](https://arxiv.org/abs/2606.13657) | Dense Supervision, Sparse Updates: On the Sparsity and Geometry of On-Policy Distillation | 2026-06-11 | v3 · 2026-07-30 | A — abstract and submission history |
| <a id="paper-2606-17199"></a>[2606.17199](https://arxiv.org/abs/2606.17199) | PowerOPD: Stabilizing On-Policy Distillation with Bounded Power Transformation | 2026-06-15 | v1 · 2026-06-15 | A — abstract and submission history |
| <a id="paper-2606-22600"></a>[2606.22600](https://arxiv.org/abs/2606.22600) | On the Position Bias of On-Policy Distillation | 2026-06-21 | v3 · 2026-06-26 | A — abstract and submission history |
| <a id="paper-2606-22830"></a>[2606.22830](https://arxiv.org/abs/2606.22830) | Finding the Evidence: Discovering Decision-Supporting Tokens for On-Policy Reasoning Distillation | 2026-06-22 | v1 · 2026-06-22 | A — abstract and submission history |
| <a id="paper-2606-26790"></a>[2606.26790](https://arxiv.org/abs/2606.26790) | OPID: On-Policy Skill Distillation for Agentic Reinforcement Learning | 2026-06-25 | v1 · 2026-06-25 | A — abstract and submission history |
| <a id="paper-2606-27377"></a>[2606.27377](https://arxiv.org/abs/2606.27377) | DanceOPD: On-Policy Generative Field Distillation | 2026-06-25 | v3 · 2026-08-15 | A — abstract and submission history |
| <a id="paper-2606-27814"></a>[2606.27814](https://arxiv.org/abs/2606.27814) | ATOD: Annealed Turn-Aware On-Policy Distillation for Multi-Turn Agentic Tasks | 2026-06-26 | v6 · 2026-08-10 | A — abstract and submission history |
| <a id="paper-2606-30406"></a>[2606.30406](https://arxiv.org/abs/2606.30406) | MOPD: Multi-Teacher On-Policy Distillation for Capability Integration in LLM Post-Training | 2026-06-29 | v1 · 2026-06-29 | A — abstract and submission history |
| <a id="paper-2607-14777"></a>[2607.14777](https://arxiv.org/abs/2607.14777) | SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning | 2026-07-16 | v1 · 2026-07-16 | A — abstract and submission history |
| <a id="paper-2608-15763"></a>[2608.15763](https://arxiv.org/abs/2608.15763) | Training Agents to Evolve with Their Harness: TaoLive Digital Avatar Agent Technical Report | 2026-08-16 | v5 · 2026-10-04 | M — abstract/history + [Section 3.4, Stage 2](https://arxiv.org/html/2608.15763v5) |

## Maintenance

When a source changes, inspect the new version, update both summaries together, and change the revision and evidence scope in this table. Do not infer strict OPD membership from a paper title or from the presence of an RL objective alone. Preserve the existing source identifier when updating a renamed paper.

See [CONTRIBUTING.md](../CONTRIBUTING.md) for validation steps and [README.md](../README.md) for the catalog.
