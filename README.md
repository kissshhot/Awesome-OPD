# Awesome On-Policy Distillation (OPD)

A curated reading list on **on-policy distillation**, **on-policy self-distillation**, and related post-training research. OPD learns from teacher feedback on student-generated trajectories to reduce the training–inference distribution mismatch of offline imitation.

**73 papers** · **Source review: 2026-10-10** · **English and Chinese paper summaries**

[Browse by topic](#topic-navigation) · [Scope and terminology](#scope-and-terminology) · [Source audit](docs/SOURCE_AUDIT.md) · [Contributing](CONTRIBUTING.md)

## Scope and Terminology

For this catalog, strict online OPD requires both:

1. **Student sampling:** training trajectories or states are refreshed from the current student policy (or a recently synchronized rollout policy).
2. **Teacher feedback:** a teacher supplies learning signals on those student trajectories or states.

White-box methods access teacher probabilities or internal representations. Black-box methods use textual scores, corrections, or other outputs without teacher probabilities. In privileged-information (PI) self-distillation, a teacher branch receives training-only context such as answers, feedback, or skills. A self-teacher may share parameters with the student; temporal self-distillation instead uses another checkpoint. A historical checkpoint is a teacher choice, not itself privileged input.

Categories describe each paper's main emphasis and are not mutually exclusive technical labels. Each paper appears once; tags expose overlapping directions. Sections 2–5 cover OPD and related hybrids, Section 6 marks extensions beyond token distributions, and Section 7 makes departures from strict online OPD explicit. An RL hybrid may use teacher feedback to reweight advantages rather than directly match distributions.

## Reading the Entries

- **First submitted** is the date on the arXiv submission record, not an inferred date from the identifier, an acceptance date, or the latest revision date.
- **Source** preserves the original arXiv link. **Checked** records the reviewed version and links to the audit. Later revisions may change a paper's title, method, or results.
- **A** means the primary-source abstract and metadata were checked. **M** additionally means the cited method sections were checked. Neither status means the experiments were reproduced or every claim in the paper was verified.
- English and Chinese summaries convey the same mechanism and scope. This list emphasizes methods; it does not compare scores from incompatible evaluations or present unverified superlatives as facts.

<a id="direction-overview"></a>

## Topic Navigation

| Topic | Papers | Focus |
| --- | ---: | --- |
| [1. Surveys](#1-surveys) | 1 | Start with the field overview and its current taxonomy. |
| [2. Objectives and Training Stability](#2-objectives-and-training-stability) | 11 | Divergence design, signal reliability, token selection, and efficient optimization on student rollouts. |
| [3. Self-Distillation and RL Connections](#3-self-distillation-and-rl-connections) | 10 | Teacher-guided policy optimization, privileged-context self-teachers, temporal teachers, and reward modulation. Mixed regimes are identified in the summaries. |
| [4. Agentic and Verbal Feedback](#4-agentic-and-verbal-feedback) | 10 | Multi-turn interaction, tool use, black-box verbal feedback, and skill-conditioned supervision. Feedback access is specified per entry. |
| [5. Multi-Teacher and Industrial Recipes](#5-multi-teacher-and-industrial-recipes) | 7 | Capability integration and OPD stages in larger post-training pipelines. A report can contain OPD alongside separate SFT and RL stages. |
| [6. Representation and Generative-Field Extensions](#6-representation-and-generative-field-extensions) | 2 | Extensions of student-state supervision beyond next-token probability matching: hidden representations and image-generation velocity fields. |
| [7. Adjacent Distillation and Self-Training Regimes](#7-adjacent-distillation-and-self-training-regimes) | 5 | Teacher-free learning, fixed-data approximations, staged correction, and teacher-generated trajectories. These are retained for comparison and are not counted as strict online OPD methods. |
| [8. Related Work on Agent Environments and Training](#8-related-work-on-agent-environments-and-training) | 12 | Environment construction, data synthesis, infrastructure, and credit assignment that can inform agentic OPD research. |
| [9. Related Work on Data Engineering](#9-related-work-on-data-engineering) | 1 | Data selection and curriculum methods for RL post-training. |
| [10. Related Work on Multiple Rewards](#10-related-work-on-multiple-rewards) | 4 | Reward normalization, decorrelation, and aggregation for competing objectives. |
| [11. Mechanism and Geometry Analyses](#11-mechanism-and-geometry-analyses) | 9 | Empirical and theoretical analyses are grouped by the learning process they study. |
| [12. Related Work on Two-Stage Policy Distillation](#12-related-work-on-two-stage-policy-distillation) | 1 | Policy optimization and distillation separated into distinct stages. |

<a id="surveys"></a>

## 1. Surveys

Start with the field overview and its current taxonomy.

| Paper and tags | First submitted | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **A Survey of On-Policy Distillation for LLMs**<br>Survey | 2026-04-01 | Surveys OPD through objective design, supervision sources, and training stabilization. The reviewed revision connects student-sampled distillation to KL-constrained RL and discusses success conditions, failure modes, and open problems. | 从优化目标、监督来源和训练稳定性三个方面梳理 OPD。所核验版本将学生采样蒸馏与 KL 约束强化学习联系起来，并讨论成功条件、失效模式和开放问题。 | [arXiv 2604.00626](https://arxiv.org/abs/2604.00626) | [A · v4](docs/SOURCE_AUDIT.md#paper-2604-00626) |

<a id="methods"></a>

## 2. Objectives and Training Stability

Divergence design, signal reliability, token selection, and efficient optimization on student rollouts.

| Paper and tags | First submitted | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **DEAR**<br>White-box; Token selection | 2026-06-22 | Selects high-entropy decision tokens and discovers supporting evidence through hidden-state similarity and teacher-student divergence. Focuses reasoning distillation on both branch choices and the intermediate knowledge supporting them. | 选择高熵决策词元，并通过隐藏状态相似度和教师与学生散度发现支持证据。让推理蒸馏同时关注分支选择及支撑这些选择的中间知识。 | [arXiv 2606.22830](https://arxiv.org/abs/2606.22830) | [A · v1](docs/SOURCE_AUDIT.md#paper-2606-22830) |
| **IW-OPD**<br>White-box; Position weighting | 2026-06-21 | Finds that teacher supervision degrades as student trajectories drift at later positions. Weights tokens using accumulated teacher-student discrepancy to emphasize reliable supervision earlier in the rollout. | 发现随着学生轨迹在靠后位置逐渐偏移，教师监督质量会下降。依据累积的教师与学生分布差异对词元加权，强化轨迹较早部分的可靠监督。 | [arXiv 2606.22600](https://arxiv.org/abs/2606.22600) | [A · v3](docs/SOURCE_AUDIT.md#paper-2606-22600) |
| **PowerOPD**<br>White-box; Bounded rewards | 2026-06-15 | Attributes sampled OPD instability to the unbounded teacher-student log-ratio reward. Replaces it with a family of bounded, sign-consistent power transformations to control gradient variance and generation behavior. | 将采样式 OPD 的不稳定归因于无界的教师与学生对数比奖励。以一族有界、符号一致的幂变换替代该奖励，控制梯度方差与生成行为。 | [arXiv 2606.17199](https://arxiv.org/abs/2606.17199) | [A · v1](docs/SOURCE_AUDIT.md#paper-2606-17199) |
| **TrOPD**<br>White-box; Trust region; Mixed guidance | 2026-05-31 | Restricts reverse-KL OPD to regions with reliable teacher guidance and evaluates alternative treatment of outliers. Adds generation from teacher prefixes with forward-KL guidance, explicitly combining on-policy and off-policy components. | 将反向 KL OPD 限于教师指导可靠的区域，并评估异常位置的不同处理方式。加入从教师前缀开始的生成与前向 KL 指导，明确结合在策略和离策略成分。 | [arXiv 2606.01249](https://arxiv.org/abs/2606.01249) | [A · v3](docs/SOURCE_AUDIT.md#paper-2606-01249) |
| **EffOPD**<br>White-box; Training efficiency | 2026-05-12 | Studies how OPD allocates parameter updates and settles into stable low-rank directions early. EffOPD accelerates training by selecting an extrapolation step along the current update direction. | 研究 OPD 如何分配参数更新，以及如何在训练早期形成稳定的低秩方向。EffOPD 沿当前更新方向选择外推步长，以加速训练。 | [arXiv 2605.11739](https://arxiv.org/abs/2605.11739) | [A · v3](docs/SOURCE_AUDIT.md#paper-2605-11739) |
| **vOPD**<br>White-box; Variance reduction | 2026-05-08 | Subtracts a detached control-variate baseline from the sampled OPD estimator. Derives the baseline from per-token negative reverse KL, avoiding a separate critic, and studies a cheaper top-K approximation. | 从采样式 OPD 估计器中减去停止梯度的控制变量基线。由逐词元负反向 KL 推导基线，无需单独的评价网络，并研究成本更低的 top-K 近似。 | [arXiv 2605.07865](https://arxiv.org/abs/2605.07865) | [A · v1](docs/SOURCE_AUDIT.md#paper-2605-07865) |
| **SCOPE**<br>White-box; Sample routing | 2026-04-12 | Routes incorrect student rollouts to teacher-perplexity-weighted KL distillation and correct rollouts to student-perplexity-weighted maximum likelihood. Group normalization calibrates the two signals across prompts of different difficulty. | 将错误的学生轨迹送入按教师困惑度加权的 KL 蒸馏，将正确轨迹送入按学生困惑度加权的最大似然训练。组内归一化校准不同难度提示上的两类信号。 | [arXiv 2604.10688](https://arxiv.org/abs/2604.10688) | [A · v2](docs/SOURCE_AUDIT.md#paper-2604-10688) |
| **StableOPD**<br>White-box; Stability | 2026-04-09 | Diagnoses length inflation and repetition that cause truncated rollouts to dominate OPD training. Combines a reference-based divergence constraint with rollout mixture distillation to stabilize optimization. | 分析长度膨胀和重复生成导致截断轨迹主导 OPD 训练的问题。结合基于参考模型的散度约束与混合轨迹蒸馏，提高优化稳定性。 | [arXiv 2604.08527](https://arxiv.org/abs/2604.08527) | [A · v1](docs/SOURCE_AUDIT.md#paper-2604-08527) |
| **OPD Fixes**<br>White-box; Local support | 2026-03-26 | Examines imbalanced supervision, unreliable teacher feedback on student prefixes, and tokenizer or special-token mismatch. Matches teacher and student distributions over teacher top-K support at student prefixes, with rollout sampling and masking fixes. | 研究监督不均衡、学生前缀上的教师反馈不可靠，以及分词器或特殊词元不匹配等问题。在学生前缀处的教师 top-K 支持集上匹配双方分布，并改进采样与掩码。 | [arXiv 2603.25562](https://arxiv.org/abs/2603.25562) | [A · v2](docs/SOURCE_AUDIT.md#paper-2603-25562) |
| **REOPOLD**<br>White-box; Stability | 2026-03-11 | Interprets the teacher-student log-likelihood ratio as a token reward. Relaxes imitation with mixture-based reward clipping, entropy-based token selection, and an exploration-to-refinement schedule. | 将教师与学生的对数似然比解释为词元奖励。通过基于混合分布的奖励裁剪、基于熵的词元选择，以及从探索到精修的调度，放宽模仿约束。 | [arXiv 2603.11137](https://arxiv.org/abs/2603.11137) | [A · v1](docs/SOURCE_AUDIT.md#paper-2603-11137) |
| **EOPD**<br>White-box; Teacher uncertainty | 2026-03-07 | Augments reverse-KL distillation with forward KL where teacher entropy is high. The objective aims to preserve plausible alternatives and reduce unstable supervision while retaining precise imitation in confident regions. | 在教师熵较高的位置，为反向 KL 蒸馏加入前向 KL。该目标旨在保留合理的备选输出、减少不稳定监督，同时在高置信区域维持精确模仿。 | [arXiv 2603.07079](https://arxiv.org/abs/2603.07079) | [A · v3](docs/SOURCE_AUDIT.md#paper-2603-07079) |

## 3. Self-Distillation and RL Connections

Teacher-guided policy optimization, privileged-context self-teachers, temporal teachers, and reward modulation. Mixed regimes are identified in the summaries.

| Paper and tags | First submitted | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **RLCSD**<br>White-box; PI self-distillation; RL hybrid | 2026-06-10 | Contrasts teacher-student gaps under correct and incorrect hints to suppress style changes caused by privileged context. The resulting self-distillation signal concentrates more on task-relevant tokens during RL. | 对比正确提示与错误提示下的教师与学生差异，抑制特权上下文引起的风格变化。得到的自蒸馏信号在 RL 中更集中于任务相关词元。 | [arXiv 2606.11709](https://arxiv.org/abs/2606.11709) | [A · v2](docs/SOURCE_AUDIT.md#paper-2606-11709) |
| **SDPG**<br>White-box; PI self-distillation; RL hybrid | 2026-06-02 | Combines group-relative verifier advantages, full-vocabulary reverse-KL self-distillation on student generations, and reference-policy regularization. Privileged context supplies dense auxiliary guidance alongside the verifier signal. | 结合组相对验证器优势、学生生成轨迹上的全词表反向 KL 自蒸馏，以及参考策略正则化。特权上下文在验证器信号之外提供稠密的辅助指导。 | [arXiv 2606.04036](https://arxiv.org/abs/2606.04036) | [A · v1](docs/SOURCE_AUDIT.md#paper-2606-04036) |
| **NPO / NPD**<br>Temporal self-distillation; Multimodal; Mixed regimes | 2026-04-22 | Uses later checkpoints as temporal teachers. In the reviewed version, NPO transfers verified future-self trajectories off-policy, while NPD supplies token-level feedback on learner-generated trajectories; AutoNPO adaptively schedules temporal guidance and rollback. | 使用后续检查点作为时间教师。在所核验版本中，NPO 以离策略方式迁移经验证的未来自身轨迹，NPD 则在学习者生成的轨迹上提供词元级反馈；AutoNPO 自适应安排时间指导与回滚。 | [arXiv 2604.20733](https://arxiv.org/abs/2604.20733) | [A · v2](docs/SOURCE_AUDIT.md#paper-2604-20733) |
| **RLSD**<br>White-box; PI self-distillation; Advantage modulation | 2026-04-03 | Uses environmental rewards to determine update direction and self-teacher/student policy differences to modulate token-level update magnitude. The method addresses information leakage and instability from relying only on privileged-teacher guidance. | 由环境奖励决定更新方向，并用自教师与学生的策略差异调节词元级更新幅度。该方法针对仅依赖特权教师指导时的信息泄漏和不稳定问题。 | [arXiv 2604.03128](https://arxiv.org/abs/2604.03128) | [A · v2](docs/SOURCE_AUDIT.md#paper-2604-03128) |
| **SRPO**<br>White-box; PI self-distillation; RL hybrid | 2026-04-02 | Applies GRPO to correct rollouts and SDPO to failed rollouts. Entropy-aware weighting reduces the influence of uncertain self-teacher predictions to balance rapid improvement and longer-term stability. | 对正确轨迹应用 GRPO，对失败轨迹应用 SDPO。基于熵的加权降低不确定自教师预测的影响，以平衡快速提升与较长期的训练稳定性。 | [arXiv 2604.02288](https://arxiv.org/abs/2604.02288) | [A · v1](docs/SOURCE_AUDIT.md#paper-2604-02288) |
| **RLAD**<br>White-box; RL hybrid | 2026-02-26 | Uses Trust Region Ratio Distillation to anchor PPO/GRPO updates to a mixture of teacher and old-policy likelihoods. Teacher imitation becomes advantage-aware and bounded by the trust region on student rollouts. | 通过信赖域比率蒸馏，将 PPO/GRPO 更新锚定到教师与旧策略似然的混合分布。在学生轨迹上，使教师模仿感知优势信号，并受信赖域约束。 | [arXiv 2602.22495](https://arxiv.org/abs/2602.22495) | [A · v3](docs/SOURCE_AUDIT.md#paper-2602-22495) |
| **G-OPD / ExOPD**<br>White-box; RL connection; Multi-teacher | 2026-02-12 | Generalizes OPD as dense KL-constrained RL with a configurable reference and reward scale. ExOPD extrapolates the teacher-derived reward; the paper also studies multi-expert integration and reward correction using a teacher's pre-RL model. | 将 OPD 推广为可配置参考模型与奖励尺度的稠密 KL 约束 RL。ExOPD 对教师导出的奖励进行外推；论文还研究多专家整合，以及利用教师的 RL 前模型校正奖励。 | [arXiv 2602.12125](https://arxiv.org/abs/2602.12125) | [A · v2](docs/SOURCE_AUDIT.md#paper-2602-12125) |
| **PID**<br>White-box; PI self-distillation; Agent | 2026-02-04 | Transfers training-only privileged information to an unprivileged policy. Introduces joint teacher-student training with pi-Distill and an OPSD variant combining RL with a reverse-KL penalty to a privileged teacher; their learning procedures differ. | 将仅在训练时可用的特权信息转移给无特权信息的策略。提出教师与学生联合训练的 pi-Distill，以及将 RL 与特权教师反向 KL 惩罚结合的 OPSD 变体；两者学习流程不同。 | [arXiv 2602.04942](https://arxiv.org/abs/2602.04942) | [A · v3](docs/SOURCE_AUDIT.md#paper-2602-04942) |
| **SDPO**<br>White-box; PI self-distillation | 2026-01-28 | Conditions the current model on rich feedback to form a self-teacher, then distills its token predictions into the policy. Successful rollouts can supply feedback when an environment returns only scalar rewards. | 以丰富反馈作为当前模型的条件，构造自教师，再将其词元预测蒸馏回策略。当环境仅提供标量奖励时，可用成功轨迹作为反馈。 | [arXiv 2601.20802](https://arxiv.org/abs/2601.20802) | [A · v2](docs/SOURCE_AUDIT.md#paper-2601-20802) |
| **KDRL**<br>White-box; RL hybrid | 2025-06-02 | Jointly optimizes reverse-KL teacher matching and rule-based rewards through a unified GRPO and distillation objective. Studies KL estimators, coefficient choices, and reward-guided distillation for reasoning. | 通过统一的 GRPO 与蒸馏目标，联合优化对教师的反向 KL 匹配和规则奖励。研究 KL 估计方式、系数设置及奖励引导的推理蒸馏。 | [arXiv 2506.02208](https://arxiv.org/abs/2506.02208) | [A · v1](docs/SOURCE_AUDIT.md#paper-2506-02208) |

## 4. Agentic and Verbal Feedback

Multi-turn interaction, tool use, black-box verbal feedback, and skill-conditioned supervision. Feedback access is specified per entry.

| Paper and tags | First submitted | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **SEED**<br>White-box; PI self-distillation; RL hybrid | 2026-07-16 | Trains the policy to act and analyze its completed trajectories into evolving hindsight skills. Re-scores actions under ordinary and skill-augmented contexts to produce an auxiliary distillation signal alongside outcome-based RL. | 训练策略既执行任务，也将自身完成的轨迹分析为持续演化的事后技能。在普通与技能增强上下文中对动作重新评分，为基于结果的 RL 提供辅助蒸馏信号。 | [arXiv 2607.14777](https://arxiv.org/abs/2607.14777) | [A · v1](docs/SOURCE_AUDIT.md#paper-2607-14777) |
| **ATOD**<br>White-box; Agent; RL hybrid | 2026-06-26 | Anneals training from OPD-dominated imitation toward stronger RL optimization. Turn-level disagreement and uncertainty reweight teacher guidance in long agent trajectories. | 将训练从以 OPD 模仿为主逐步调度到更强的 RL 优化。依据轮次级分歧与不确定性，对较长智能体轨迹中的教师指导重新加权。 | [arXiv 2606.27814](https://arxiv.org/abs/2606.27814) | [A · v6](docs/SOURCE_AUDIT.md#paper-2606-27814) |
| **OPID**<br>White-box; PI self-distillation; RL hybrid | 2026-06-25 | Extracts episode- and step-level hindsight skills from completed student trajectories. Re-scores sampled actions with and without the selected skill, combining the resulting token-level advantage with outcome-based RL. | 从已完成的学生轨迹中提取回合级和步骤级事后技能。分别在有无所选技能的条件下对采样动作重新评分，将得到的词元级优势与基于结果的 RL 结合。 | [arXiv 2606.26790](https://arxiv.org/abs/2606.26790) | [A · v1](docs/SOURCE_AUDIT.md#paper-2606-26790) |
| **PBSD**<br>White-box; PI self-distillation; Credit assignment | 2026-06-08 | Compares ordinary and answer-conditioned likelihoods on agent rollouts to derive turn-level Bayesian evidence. Uses that evidence to reweight outcome advantages, preserving their direction instead of directly imitating privileged actions. | 比较智能体轨迹在普通条件与答案条件下的似然，得到轮次级贝叶斯证据。用该证据重新加权结果优势并保留其方向，而不是直接模仿特权动作。 | [arXiv 2606.09348](https://arxiv.org/abs/2606.09348) | [M · v2](docs/SOURCE_AUDIT.md#paper-2606-09348) |
| **SDAR**<br>White-box; PI self-distillation; RL hybrid | 2026-05-14 | Keeps RL as the main objective and gates auxiliary self-distillation with detached token-level teacher-student gaps. An asymmetric sigmoid gate strengthens positive guidance while attenuating unreliable rejections from a skill-conditioned teacher. | 保留 RL 作为主目标，利用停止梯度的词元级教师与学生差异，对辅助自蒸馏进行门控。非对称 sigmoid 门增强正向指导，并减弱技能条件教师可能不可靠的否定信号。 | [arXiv 2605.15155](https://arxiv.org/abs/2605.15155) | [A · v1](docs/SOURCE_AUDIT.md#paper-2605-15155) |
| **SOD**<br>White-box; Agent; Tool use | 2026-05-08 | Reweights distillation at each tool-integrated reasoning step according to teacher-student divergence. Attenuates guidance where erroneous tool calls have driven the student away from reliable teacher support. | 根据教师与学生的散度，对工具集成推理中每一步的蒸馏重新加权。当错误工具调用使学生偏离可靠的教师支持范围时，减弱指导信号。 | [arXiv 2605.07725](https://arxiv.org/abs/2605.07725) | [A · v3](docs/SOURCE_AUDIT.md#paper-2605-07725) |
| **TCOD**<br>White-box; Agent; Curriculum | 2026-04-27 | Diagnoses increasing trajectory-level KL under compounding multi-turn errors. Gradually expands the trajectory depth exposed to the student, using a temporal curriculum to stabilize teacher guidance on longer interactions. | 分析多轮错误累积时轨迹级 KL 上升的问题。通过时间课程逐步增加学生接触的轨迹深度，使较长交互中的教师指导更稳定。 | [arXiv 2604.24005](https://arxiv.org/abs/2604.24005) | [A · v3](docs/SOURCE_AUDIT.md#paper-2604-24005) |
| **Skill-SD**<br>White-box; PI self-distillation; Agent | 2026-04-12 | Summarizes completed agent trajectories into skills that condition only the teacher. Uses importance-weighted reverse KL and teacher synchronization to internalize this dynamic guidance while the student acts without skill prompts. | 将已完成的智能体轨迹总结为技能，仅用于教师条件。采用重要性加权反向 KL 和教师同步，使学生在不接收技能提示的情况下内化动态指导。 | [arXiv 2604.10674](https://arxiv.org/abs/2604.10674) | [A · v1](docs/SOURCE_AUDIT.md#paper-2604-10674) |
| **OpenClaw-RL**<br>White-box; PI self-distillation; RL hybrid | 2026-03-10 | Extracts evaluative rewards and directive hints from interaction next states. Combines RL with log-probability supervision from a hint-conditioned self-teacher, using overlap-guided hint selection and clipping; textual hints do not make the distillation branch black-box. | 从交互的下一状态提取评价奖励与指导提示。将 RL 和提示条件自教师的对数概率监督结合，并使用重叠度引导的提示选择与裁剪；文本提示并不意味着蒸馏分支是黑盒。 | [arXiv 2603.10165](https://arxiv.org/abs/2603.10165) | [M · v2](docs/SOURCE_AUDIT.md#paper-2603-10165) |
| **OVD**<br>Black-box; Verbal; Agent | 2026-01-29 | Uses black-box teacher scores to rank student sub-trajectories, retaining stronger segments and replacing weaker ones with teacher continuations. The reviewed version separates Web Q&A with inference-time teacher feedback from training-time reasoning experiments. | 利用黑盒教师评分对学生子轨迹排序，保留较好片段，并用教师续写替换较弱片段。所核验版本区分了推理时使用教师反馈的 Web 问答与训练阶段的推理实验。 | [arXiv 2601.21968](https://arxiv.org/abs/2601.21968) | [A · v2](docs/SOURCE_AUDIT.md#paper-2601-21968) |

## 5. Multi-Teacher and Industrial Recipes

Capability integration and OPD stages in larger post-training pipelines. A report can contain OPD alongside separate SFT and RL stages.

| Paper and tags | First submitted | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **HAT / TaoLive**<br>White-box; Agent; Industrial | 2026-08-16 | Places general-domain OPD between harness-augmented SFT and RL. The pre-SFT base model supervises student-sampled general instructions to recover capabilities while later RL trains adaptation to changing harness configurations. | 在执行框架增强的 SFT 与 RL 之间加入通用领域 OPD。由 SFT 前的基础模型监督学生在通用指令上的采样输出，以恢复能力；后续 RL 训练对变化的执行框架配置的适应性。 | [arXiv 2608.15763](https://arxiv.org/abs/2608.15763) | [M · v5](docs/SOURCE_AUDIT.md#paper-2608-15763) |
| **MOPD**<br>White-box; Multi-teacher; Industrial | 2026-06-29 | Trains domain experts independently with RL, then distills their capabilities into one student on its own rollouts. Studies capability integration and reports use of this recipe in MiMo-V2-Flash post-training. | 先用 RL 独立训练各领域专家，再在单个学生自身的采样轨迹上蒸馏并整合能力。研究能力整合，并报告该方案在 MiMo-V2-Flash 后训练中的应用。 | [arXiv 2606.30406](https://arxiv.org/abs/2606.30406) | [A · v1](docs/SOURCE_AUDIT.md#paper-2606-30406) |
| **Uni-OPD**<br>White-box; Multi-teacher; Multimodal | 2026-05-05 | Balances training data to improve exploration of informative student states, then calibrates teacher guidance against outcome rewards. Evaluates this dual-perspective recipe in language, multimodal, and single- or multi-teacher settings. | 通过平衡训练数据，促进对有信息量的学生状态的探索，再依据结果奖励校准教师指导。在语言、多模态以及单教师和多教师设置中评估这一双视角方案。 | [arXiv 2605.03677](https://arxiv.org/abs/2605.03677) | [A · v2](docs/SOURCE_AUDIT.md#paper-2605-03677) |
| **MAD-OPD**<br>White-box; Multi-teacher; Agent | 2026-05-02 | Lets teachers debate over student-visited states and weights their token-level guidance by post-debate confidence. Adds step-level agent sampling and studies task-dependent choices between JSD and reverse KL. | 让多位教师围绕学生访问的状态辩论，并按辩论后的置信度加权词元级指导。加入智能体步级采样，并研究不同任务中 JSD 与反向 KL 的选择。 | [arXiv 2605.01347](https://arxiv.org/abs/2605.01347) | [A · v1](docs/SOURCE_AUDIT.md#paper-2605-01347) |
| **Nemotron-Cascade 2**<br>White-box; Multi-teacher; Industrial | 2026-03-19 | Combines Cascade RL across reasoning and agentic domains with multi-domain OPD from strong intermediate checkpoints. Distillation recovers domain regressions that arise across successive RL stages. | 将在推理和智能体领域开展的级联 RL，与来自较强中间检查点的多领域 OPD 相结合。蒸馏用于恢复连续 RL 阶段中出现的领域能力退化。 | [arXiv 2603.19220](https://arxiv.org/abs/2603.19220) | [A · v2](docs/SOURCE_AUDIT.md#paper-2603-19220) |
| **GLM-5**<br>White-box; Multi-teacher; Industrial | 2026-02-17 | Uses checkpoints from preceding SFT and RL stages as teachers in a final cross-stage OPD phase. Teacher-student log-probability gaps replace the advantage signal to recover capabilities degraded by sequential post-training. | 在最终的跨阶段 OPD 阶段，以先前 SFT 和 RL 阶段的检查点作为教师。用教师与学生的对数概率差替代优势信号，恢复顺序后训练中退化的能力。 | [arXiv 2602.15763](https://arxiv.org/abs/2602.15763) | [M · v2](docs/SOURCE_AUDIT.md#paper-2602-15763) |
| **MiMo-V2-Flash**<br>White-box; Multi-teacher; Industrial | 2026-01-06 | Introduces multi-teacher on-policy distillation in an industrial MoE training pipeline. Domain-specialized teachers supply dense token-level rewards so one student can integrate separately developed capabilities. | 在工业级 MoE 训练流程中引入多教师在策略蒸馏。各领域专用教师提供稠密的词元级奖励，使单个学生整合分别训练得到的能力。 | [arXiv 2601.02780](https://arxiv.org/abs/2601.02780) | [A · v2](docs/SOURCE_AUDIT.md#paper-2601-02780) |

## 6. Representation and Generative-Field Extensions

Extensions of student-state supervision beyond next-token probability matching: hidden representations and image-generation velocity fields.

| Paper and tags | First submitted | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **DanceOPD**<br>Generative fields; Multi-capability | 2026-06-25 | Extends student-state supervision to flow-matching image models. Routes each sample to a capability field, queries a low-noise student-induced state, and learns through velocity MSE to combine generation and editing capabilities. | 将学生状态上的监督扩展到流匹配图像模型。把每个样本路由到一个能力场，在学生产生的低噪声状态上查询，并通过速度 MSE 学习，整合生成与编辑能力。 | [arXiv 2606.27377](https://arxiv.org/abs/2606.27377) | [A · v3](docs/SOURCE_AUDIT.md#paper-2606-27377) |
| **OPRD**<br>White-box; Representations | 2026-06-04 | Aligns teacher and student hidden representations on the student's own rollouts, bypassing output-distribution matching. The reviewed revision includes OPRD-Bridge, which uses frozen projectors to handle differing architectures and tokenizers. | 在学生自身采样轨迹上对齐教师与学生的隐藏表征，绕过输出分布匹配。所核验版本包含 OPRD-Bridge，使用冻结投影器处理架构与分词器差异。 | [arXiv 2606.06021](https://arxiv.org/abs/2606.06021) | [A · v4](docs/SOURCE_AUDIT.md#paper-2606-06021) |

<a id="related-work"></a>

## 7. Adjacent Distillation and Self-Training Regimes

Teacher-free learning, fixed-data approximations, staged correction, and teacher-generated trajectories. These are retained for comparison and are not counted as strict online OPD methods.

| Paper and tags | First submitted | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **Lightning OPD**<br>White-box; Offline approximation | 2026-04-14 | Precomputes teacher log-probabilities on rollouts from an SFT-initialized student and reuses a fixed dataset. Its teacher-consistency condition supports an offline approximation to OPD, without refreshing rollouts from the evolving student during optimization. | 在 SFT 初始化学生的采样轨迹上预计算教师对数概率，并复用固定数据集。其教师一致性条件支持对 OPD 的离线近似，但优化期间不从持续变化的学生重新采样轨迹。 | [arXiv 2604.13010](https://arxiv.org/abs/2604.13010) | [M · v3](docs/SOURCE_AUDIT.md#paper-2604-13010) |
| **SSD**<br>Teacher-free self-training | 2026-04-01 | Samples code solutions from the model with chosen temperature and truncation settings, then applies standard SFT to those outputs. SSD needs no teacher, verifier, or RL, so it does not satisfy this catalog's teacher-feedback criterion for strict OPD. | 按选定的温度和截断设置从模型采样代码解答，再对这些输出进行标准 SFT。SSD 不需要教师、验证器或 RL，因此不满足本目录对严格 OPD 的教师反馈条件。 | [arXiv 2604.01193](https://arxiv.org/abs/2604.01193) | [A · v2](docs/SOURCE_AUDIT.md#paper-2604-01193) |
| **HDPO**<br>White-box; Privileged trajectories; RL hybrid | 2026-03-25 | Targets prompts where all ordinary rollouts fail by generating and filtering answer-conditioned teacher trajectories, then applying token-level JSD. The distillation trajectories come from the privileged teacher, so this branch differs from strict student-rollout OPD. | 针对普通采样全部失败的提示，生成并筛选以答案为条件的教师轨迹，再应用词元级 JSD。蒸馏轨迹来自特权教师，因此该分支不同于严格的学生采样 OPD。 | [arXiv 2603.23871](https://arxiv.org/abs/2603.23871) | [M · v1](docs/SOURCE_AUDIT.md#paper-2603-23871) |
| **DDT / On-Policy SFT**<br>Distribution-aware SFT | 2026-02-12 | Uses Distribution Discriminant Theory to assess how well training data fit the model distribution. Combines In-Distribution Finetuning with Hinted Decoding to rewrite data and reduce distribution mismatch; the pipeline is not a continually refreshed student-rollout OPD loop. | 利用分布判别理论评估训练数据与模型分布的匹配程度。结合分布内微调与提示解码，重写数据并减小分布偏移；该流程并非持续更新学生采样轨迹的 OPD 循环。 | [arXiv 2602.12222](https://arxiv.org/abs/2602.12222) | [M · v2](docs/SOURCE_AUDIT.md#paper-2602-12222) |
| **SCoRe**<br>Correction-based; Agent; Staged | 2025-09-12 | Collects student trajectories with teacher corrections at the earliest error, then applies SFT and short-horizon RL from verified prefixes. This staged correction pipeline uses textual interventions rather than requiring teacher logits. | 收集学生轨迹，由教师纠正最早的错误，再进行 SFT，并从已验证前缀开展短时域 RL。这是分阶段的纠错流程，使用文本干预，而非要求教师 logits。 | [arXiv 2509.14257](https://arxiv.org/abs/2509.14257) | [M · v3](docs/SOURCE_AUDIT.md#paper-2509-14257) |

<a id="related-work-agentic-rl-environments"></a>

## 8. Related Work on Agent Environments and Training

Environment construction, data synthesis, infrastructure, and credit assignment that can inform agentic OPD research.

| Paper and tags | First submitted | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **SkillRL**<br>Related; Skill memory | 2026-02-09 | Builds and retrieves a hierarchical skill library from agent experience, with the library evolving alongside RL training. Provides context for skill-based guidance, distinct from token-level OPD into model weights. | 从智能体经验构建并检索分层技能库，使技能库随 RL 训练共同演化。为技能引导提供参考，与将指导通过词元级 OPD 内化到模型权重的做法有所区别。 | [arXiv 2602.08234](https://arxiv.org/abs/2602.08234) | [A · v2](docs/SOURCE_AUDIT.md#paper-2602-08234) |
| **LLM-in-Sandbox**<br>Related; Sandbox | 2026-01-22 | Studies how a minimal computer sandbox enables resource access, file management, and code execution for general tasks. Also trains weaker models through RL in the sandbox using non-agentic data. | 研究最小计算机沙箱如何通过资源访问、文件管理和代码执行支持通用任务。还使用非智能体数据，在沙箱内通过 RL 训练较弱模型。 | [arXiv 2601.16206](https://arxiv.org/abs/2601.16206) | [A · v3](docs/SOURCE_AUDIT.md#paper-2601-16206) |
| **SkyRL-Agent**<br>Related; RL infrastructure | 2025-11-20 | Optimizes asynchronous dispatch and tool integration for multi-turn agent training. Its software-engineering recipe uses code-search tools and RL, providing infrastructure context for long-horizon learning. | 优化多轮智能体训练中的异步调度和工具集成。其软件工程训练方案使用代码搜索工具与 RL，为长时域学习提供基础设施参考。 | [arXiv 2511.16108](https://arxiv.org/abs/2511.16108) | [A · v1](docs/SOURCE_AUDIT.md#paper-2511-16108) |
| **VAGEN**<br>Related; Multimodal agents | 2025-10-19 | Trains vision-language agents to reason explicitly about current states and future transitions. Combines world-model rewards with turn-aware advantage estimation for partially observable environments. | 训练视觉语言智能体显式推理当前状态与后续转移。结合世界模型奖励与轮次感知的优势估计，处理部分可观测环境。 | [arXiv 2510.16907](https://arxiv.org/abs/2510.16907) | [A · v1](docs/SOURCE_AUDIT.md#paper-2510-16907) |
| **AgentRL**<br>Related; RL infrastructure | 2025-10-05 | Provides asynchronous multi-turn, multi-task RL with a shared function-call interface and containerized environments. Uses cross-policy sampling for exploration and task-level advantage normalization for stability. | 通过共享函数调用接口与容器化环境，支持异步多轮、多任务 RL。采用跨策略采样促进探索，并用任务级优势归一化提升稳定性。 | [arXiv 2510.04206](https://arxiv.org/abs/2510.04206) | [A · v1](docs/SOURCE_AUDIT.md#paper-2510-04206) |
| **AgentGym-RL**<br>Related; RL curriculum | 2025-09-10 | Provides a modular framework for agent RL across interactive environments. ScalingInter-RL starts with shorter interaction horizons and gradually expands them to balance exploitation, exploration, and training stability. | 提供面向交互环境的模块化智能体 RL 框架。ScalingInter-RL 从较短交互时域开始，再逐步扩展，以平衡利用、探索和训练稳定性。 | [arXiv 2509.08755](https://arxiv.org/abs/2509.08755) | [A · v1](docs/SOURCE_AUDIT.md#paper-2509-08755) |
| **Chain-of-Agents**<br>Related; Offline agent distillation | 2025-08-06 | Distills multi-agent systems into supervised chain-of-agents trajectories for a single model, then applies agentic RL. This staged SFT-to-RL recipe supplies a comparison for on-policy agent distillation. | 将多智能体系统蒸馏为单个模型使用的智能体链监督轨迹，再进行智能体 RL。该分阶段 SFT 到 RL 方案可作为在策略智能体蒸馏的对照。 | [arXiv 2508.13167](https://arxiv.org/abs/2508.13167) | [A · v1](docs/SOURCE_AUDIT.md#paper-2508-13167) |
| **SWE-Factory**<br>Related; SWE environments | 2025-06-12 | Automates issue-resolution data construction through binary-test recovery, multi-agent environment setup, and exit-code-based fail-to-pass validation. Supports both training data and evaluation benchmark construction. | 通过恢复二进制测试文件、多智能体环境搭建，以及基于退出码的失败到通过验证，自动构建问题修复数据。支持训练数据与评测基准的构建。 | [arXiv 2506.10954](https://arxiv.org/abs/2506.10954) | [A · v3](docs/SOURCE_AUDIT.md#paper-2506-10954) |
| **SPA-RL**<br>Related; Credit assignment | 2025-05-27 | Learns a progress estimator to redistribute terminal rewards into stepwise contributions. Combines these contributions with action-grounding signals to improve credit assignment in multi-step agent RL. | 学习进度估计器，将终局奖励重新分配为逐步贡献。结合这些贡献与动作落地信号，改进多步智能体 RL 中的信用分配。 | [arXiv 2505.20732](https://arxiv.org/abs/2505.20732) | [A · v1](docs/SOURCE_AUDIT.md#paper-2505-20732) |
| **GiGPO**<br>Related; Credit assignment | 2025-05-16 | Combines episode-level relative advantages with step-level groups built from repeated environment states. Supplies finer agent credit assignment without an auxiliary critic or additional rollouts. | 将回合级相对优势与依据重复环境状态构建的步骤级分组相结合。在无需辅助评价网络或额外采样轨迹的情况下，提供更细粒度的智能体信用分配。 | [arXiv 2505.10978](https://arxiv.org/abs/2505.10978) | [A · v3](docs/SOURCE_AUDIT.md#paper-2505-10978) |
| **SWE-Smith**<br>Related; SWE data | 2025-04-30 | Constructs execution environments from Python repositories and synthesizes task instances that break existing tests. Provides scalable training data for software-engineering agents rather than an OPD objective. | 从 Python 仓库构建执行环境，并合成使现有测试失败的任务实例。为软件工程智能体提供可扩展训练数据，而非 OPD 优化目标。 | [arXiv 2504.21798](https://arxiv.org/abs/2504.21798) | [A · v2](docs/SOURCE_AUDIT.md#paper-2504-21798) |
| **R2E-Gym**<br>Related; SWE environments | 2025-04-09 | Builds executable software-engineering tasks through test generation and commit back-translation. Combines execution-based and execution-free verifiers for test-time selection; useful environment and verification context for agent training. | 通过测试生成和提交反向转换构建可执行的软件工程任务。结合执行型与非执行型验证器进行测试时选择，为智能体训练提供环境与验证方面的参考。 | [arXiv 2504.07164](https://arxiv.org/abs/2504.07164) | [A · v1](docs/SOURCE_AUDIT.md#paper-2504-07164) |

<a id="related-work-rl-post-training-data-engineering"></a>

## 9. Related Work on Data Engineering

Data selection and curriculum methods for RL post-training.

| Paper and tags | First submitted | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **SAERL**<br>Related; Data engineering | 2026-05-26 | Uses sparse-autoencoder features to estimate data diversity, difficulty, and quality. These signals drive batch mixing, curriculum ordering, and filtering for RL post-training. | 利用稀疏自编码器特征估计数据多样性、难度和质量。以这些信号指导 RL 后训练中的批次混合、课程排序和数据过滤。 | [arXiv 2605.27354](https://arxiv.org/abs/2605.27354) | [A · v1](docs/SOURCE_AUDIT.md#paper-2605-27354) |

<a id="related-work-multi-reward-rl"></a>

## 10. Related Work on Multiple Rewards

Reward normalization, decorrelation, and aggregation for competing objectives.

| Paper and tags | First submitted | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **RDPO**<br>Related; Reward decorrelation | 2026-05-13 | Applies magnitude-aware quantile normalization to heterogeneous rewards, then Mahalanobis whitening to reduce correlation redundancy. Targets more stable scalar advantages in multi-objective post-training. | 对异质奖励应用幅度感知的分位数归一化，再通过马氏白化减少相关冗余。旨在为多目标后训练构造更稳定的标量优势。 | [arXiv 2605.13641](https://arxiv.org/abs/2605.13641) | [A · v1](docs/SOURCE_AUDIT.md#paper-2605-13641) |
| **RVPO**<br>Related; Reward aggregation | 2026-05-07 | Uses a SoftMin-style aggregation that penalizes variation across reward dimensions. Encourages improvement of weak constraints instead of allowing strong rewards to mask failures elsewhere. | 使用 SoftMin 式聚合，惩罚奖励维度之间的差异。鼓励改善较弱约束，避免较高奖励掩盖其他维度的失败。 | [arXiv 2605.05750](https://arxiv.org/abs/2605.05750) | [A · v1](docs/SOURCE_AUDIT.md#paper-2605-05750) |
| **GDPO**<br>Related; Reward normalization | 2026-01-08 | Normalizes reward dimensions separately before aggregation to retain distinctions lost by aggregate-first group normalization. Studies stable multi-reward optimization for tool use, math, and coding. | 先分别归一化各奖励维度，再进行聚合，保留先聚合后组归一化可能丢失的差异。研究工具使用、数学和编码中的稳定多奖励优化。 | [arXiv 2601.05242](https://arxiv.org/abs/2601.05242) | [A · v1](docs/SOURCE_AUDIT.md#paper-2601-05242) |
| **MVA**<br>Related; Multi-value alignment | 2025-11-15 | Reduces interference between value dimensions through decorrelation and explores trade-offs through value extrapolation. Provides a neighboring approach to integrating competing training objectives. | 通过去相关减少价值维度间的干扰，并利用价值外推探索权衡。为整合相互竞争的训练目标提供相邻领域的方法参考。 | [arXiv 2511.17579](https://arxiv.org/abs/2511.17579) | [A · v1](docs/SOURCE_AUDIT.md#paper-2511-17579) |

## 11. Mechanism and Geometry Analyses

Empirical and theoretical analyses are grouped by the learning process they study.

<a id="related-work-rlvr-mechanism-analysis"></a>

### 11.1. RL and Representation Analyses

Reward overoptimization, token-level changes, trust regions, and inference or parameter geometry.

| Paper and tags | First submitted | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **DRPO**<br>Related; RL optimization | 2026-06-08 | Replaces hard trust-region masking with a smooth, advantage-weighted quadratic penalty on policy probability shifts. Keeps corrective gradients beyond the boundary and studies stability across model and precision settings. | 以策略概率变化上的平滑、优势加权二次惩罚替代硬信赖域掩码。保留边界外的纠正梯度，并研究不同模型和精度设置下的稳定性。 | [arXiv 2606.09821](https://arxiv.org/abs/2606.09821) | [A · v1](docs/SOURCE_AUDIT.md#paper-2606-09821) |
| **RELEX**<br>Related; RLVR efficiency | 2026-05-20 | Models early RLVR parameter changes with a low-rank trajectory and extrapolates later checkpoints. Studies when short training observations can predict useful updates and reduce total optimization cost. | 用低秩轨迹建模早期 RLVR 参数变化，并外推后续检查点。研究何时能根据较短训练观测预测有效更新，从而降低总优化成本。 | [arXiv 2605.21468](https://arxiv.org/abs/2605.21468) | [A · v1](docs/SOURCE_AUDIT.md#paper-2605-21468) |
| **Inference Manifold**<br>Related; Representation analysis | 2026-05-02 | Examines low-dimensional structure in inference-time representations. Proposes a label-free diagnostic combining expressivity, manifold compression, and retained information, offering a complementary view of reasoning quality. | 考察推理时表征中的低维结构。提出结合表达能力、流形压缩和信息保留的无标签诊断，为评估推理质量提供补充视角。 | [arXiv 2605.08142](https://arxiv.org/abs/2605.08142) | [A · v1](docs/SOURCE_AUDIT.md#paper-2605-08142) |
| **Sparse but Critical**<br>Related; RLVR analysis | 2026-03-23 | Uses token-distribution diagnostics and cross-sampling interventions to study RLVR. Finds that sparse changes at consequential token positions can explain much of the observed reasoning improvement. | 通过词元分布诊断与交叉采样干预研究 RLVR。发现关键词元位置上的稀疏变化可以解释相当一部分观测到的推理提升。 | [arXiv 2603.22446](https://arxiv.org/abs/2603.22446) | [A · v1](docs/SOURCE_AUDIT.md#paper-2603-22446) |
| **Negative RL**<br>Related; RLVR analysis | 2025-06-02 | Separates reinforcement of correct answers from penalties on incorrect answers. Studies how negative-sample reinforcement preserves alternative solutions and proposes an objective that emphasizes this signal; first submitted in June 2025. | 将对正确答案的强化与对错误答案的惩罚分开。研究负样本强化如何保留其他解法，并提出更重视该信号的目标；首次提交于 2025 年六月。 | [arXiv 2506.01347](https://arxiv.org/abs/2506.01347) | [A · v2](docs/SOURCE_AUDIT.md#paper-2506-01347) |
| **RM Overoptimization Scaling Laws**<br>Related; RLHF analysis | 2022-10-19 | Measures how optimizing a proxy reward can eventually reduce a separate gold-model score. Studies scaling trends under RL and best-of-n sampling, providing context for reward overoptimization rather than an OPD method. | 衡量优化代理奖励如何最终降低独立金标准模型的评分。研究 RL 与 best-of-n 采样下的尺度规律，为奖励过度优化提供分析参考，而非提出 OPD 方法。 | [arXiv 2210.10760](https://arxiv.org/abs/2210.10760) | [A · v1](docs/SOURCE_AUDIT.md#paper-2210-10760) |

<a id="related-work-opd-mechanism-analysis"></a>

### 11.2. OPD Analyses

Teacher compatibility and the geometry of OPD updates.

| Paper and tags | First submitted | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **Dense Supervision Sparse Updates**<br>OPD analysis | 2026-06-11 | Characterizes OPD updates as coordinate-sparse at checkpoint precision and spectrally concentrated, yet numerically full-rank. Examines where these updates occur and whether masked training can recover full-training performance. | 将 OPD 更新刻画为在检查点精度下坐标稀疏、谱集中，但在数值上仍为满秩。研究更新发生的位置，以及掩码训练能否恢复完整训练的性能。 | [arXiv 2606.13657](https://arxiv.org/abs/2606.13657) | [A · v3](docs/SOURCE_AUDIT.md#paper-2606-13657) |
| **OPD Geometry**<br>OPD analysis | 2026-06-05 | Compares OPD parameter-update geometry with SFT and RLVR. Finds early concentration into a narrow update subspace and tests whether restricting training to that subspace preserves performance. | 比较 OPD 与 SFT、RLVR 的参数更新几何。发现更新在早期集中到较窄子空间，并测试限制训练在该子空间内是否仍能保持性能。 | [arXiv 2606.07082](https://arxiv.org/abs/2606.07082) | [A · v3](docs/SOURCE_AUDIT.md#paper-2606-07082) |
| **OPD Recipe**<br>OPD analysis | 2026-04-14 | Studies when teacher guidance transfers effectively: compatible reasoning patterns and useful new teacher capabilities both matter. Analyzes token-level alignment and proposes off-policy initialization and teacher-aligned prompt selection for failing OPD runs. | 研究教师指导有效迁移的条件：推理模式兼容性与教师提供的新能力均有影响。分析词元级对齐，并针对失效的 OPD 训练提出离策略初始化和教师匹配的提示选择。 | [arXiv 2604.13016](https://arxiv.org/abs/2604.13016) | [A · v2](docs/SOURCE_AUDIT.md#paper-2604-13016) |

<a id="related-work-two-stage-policy-decoupling"></a>

## 12. Related Work on Two-Stage Policy Distillation

Policy optimization and distillation separated into distinct stages.

| Paper and tags | First submitted | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **ERPD**<br>Related; Two-stage distillation | 2026-05-25 | First performs weakly constrained off-policy optimization on fixed data, then distills the resulting token-level signals into a base policy under trust-region constraints. Separates signal extraction from controlling harmful policy drift. | 先在固定数据上进行弱约束的离策略优化，再将所得词元级信号在信赖域约束下蒸馏回基础策略。将训练信号提取与有害策略偏移控制分开。 | [arXiv 2605.25582](https://arxiv.org/abs/2605.25582) | [A · v2](docs/SOURCE_AUDIT.md#paper-2605-25582) |

## Contributing

See the [contribution guide](CONTRIBUTING.md) for scope decisions, the bilingual entry template, source evidence, and local validation commands. Corrections with precise primary-source evidence are welcome.

## Organization Reference

The numbered topics, consistent tables, dates, source links, and explicit verification status are inspired by the organization of [awesome-environment](https://github.com/possibleme2026-lang/awesome-environment/blob/ecbf5d7/readme.en.md). This catalog uses OPD-specific categories and independently checked paper descriptions.
