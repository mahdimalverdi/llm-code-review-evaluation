# P98 — Fine-Tuning LLMs to Analyze Multiple Dimensions of Code Review: A Maximum Entropy Regulated Long Chain-of-Thought Approach

> **Provisional intake record.** This is not a canonical paper note.

| Field | Value |
|---|---|
| Project ID | `P98` (provisional) |
| Citation key | `p98_yu2025_fine_tuning_llms_to_analyze_mu` |
| Authors | Yongda Yu; Guohao Shi; Xianwei Wu; Haochuan He; XueMing Gu; Qianqian Zhao; Kui Liu; Qiushi Wang; Zhao Tian; Haifeng Shen; Guoping Rong |
| Year | 2025 |
| Source | arXiv |
| arXiv | `2509.21170v1` |
| Screening tier | `core` |
| Reconciliation status | New candidate after initial local matching |
| Metadata status | local_arxiv_metadata |
| Evidence status | Full-text eligibility recorded; extraction not yet completed |

## 1. Identification

- Duplicate or companion publication: The extracted PDF contains inconsistent JACM 2018 placeholder metadata while the arXiv record is 2025; publisher/version status requires verification.

## 2. Screening
- Decision: `Include`; Relevance: `High`
- Decision rationale: Directly evaluates a fine-tuned LLM for issue localization, review-comment accuracy, hallucination/factual validity, and human agreement.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: evaluation dimensions / context quality / mitigation design

## 3. Study overview
- Purpose: Improve automated code review by training models to reason over multiple review dimensions rather than mapping diffs directly to comments.
- Research questions: MelcotCR performance in issue localization and description (RQ1) and the effects of maximum-entropy fine-tuning/reasoning steps (RQ2).
- Method: Curate MelcotCR from open-source review history, augment comments with long chain-of-thought, regulate fine-tuning with maximum-entropy modeling (MEFT), and evaluate a Qwen2.5-14B model.
- Evaluated system/artifact: MelcotCR (14B) compared with Carllm 14B, Qwen2.5-72B, QWQ-32B, and DeepSeek-R1 671B.
- Dataset/benchmark: 12,152,191 raw comments filtered to 6,735,961 comments from 11,324 projects, then to 211,868 valid entries and a 12,881-instance MelcotCR dataset. Evaluation uses 1,000 in-distribution MelcotCR items and 1,000 CodeReviewer items.
- Input context: Historical code submissions, diffs, review comments, code flows, summaries, issue checks, and proposed solutions; the method explicitly expands beyond isolated diff fragments.
- Main findings: MelcotCR Qwen2.5-14B achieves IoU 27.16, Hit Rate 25.4, Human Hit 29.72, and Human Valuable 81.67 on MelcotCR. On CodeReviewer it achieves Hit Rate 36.56, Human Hit 39.17, and Human Valuable 92.00.

## 4. Evidence mapped to review questions
| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | MelcotCR improves localization and comment accuracy over the compared fine-tuned/general baselines, especially on in-distribution data. | Reported | Sections 4.2.1–4.2.2, Table 5 |
| RQ2 | MEFT and long COT jointly improve performance; removing diff analysis or key code flows causes the largest degradation. | Reported | Sections 4.2.3, Tables 6–7 |
| RQ3 | Human Valuable measures whether comments identify genuine issues even when they differ from the reference, addressing hallucination/factual validity. | Reported | Section 4.1.4 |
| RQ4 | Long reasoning improves context integration but increases data, prompt, and training complexity. | Inferred | Sections 3–4 |
| RQ5 | Code flow and historical context can improve localization, but the benchmark remains largely derived from curated review comments. | Reported / limitation | Sections 3–4 |
| RQ6 | Evaluation should separate localization, reference agreement, factual validity, and human judgment rather than rely on lexical overlap. | Inferred | Sections 4–5 |

## 5. Failure and problematic-comment categories
| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Mislocalized issue | Predicted problematic lines do not overlap the ground-truth issue span. | Evaluated failure | Section 4.1.3 |
| Hallucinated issue | Comment claims a problem that does not genuinely exist in the code. | Evaluated failure | Section 4.1.4 |
| Missing contextual flow | Removing key-code-flow reasoning reduces comment accuracy. | Ablation failure | Table 7 |
| Shallow diff-only reasoning | Isolated patches omit historical or repository context. | Motivation/limitation | Sections 1, 3 |
| Judge self-preference | QWQ-32B reportedly overestimates its own responses in LLM judging. | Reported evaluator failure | Section 4.2.2 |

## 6. Evaluation dimensions and metrics
| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Localization | Intersection over Union (IoU) of predicted and labeled issue lines. | MelcotCR 27.16 vs Carllm 24.12 on MelcotCR. | Table 5 |
| Reference issue agreement | Hit Rate and Human Hit. | MelcotCR Hit 25.4, Human Hit 29.72; CodeReviewer 36.56 and 39.17. | Table 5 |
| Factual usefulness | Human Valuable: genuine code problem, regardless of exact reference match. | MelcotCR 81.67 in-distribution and 92.00 on CodeReviewer. | Table 5 |
| Human reliability | Two evaluators, overlap, Cohen’s kappa. | Human–human κ=.8426; LLM judge–human κ=.5281. | Section 4.1.4 |
| Reasoning ablation | Remove summary, key flows, diff analysis, or issue check. | Removing diff analysis drops IoU 6.55% and Hit Rate 6.58%; key flows reduce Hit 8.23%. | Table 7 |
| Cost/scale | Training hardware and reasoning length. | Training uses 8× NVIDIA H800 80GB; inference/training monetary cost is not reported. | Section 3.3 |

## 7. Mitigation and trade-offs
- Mitigation family: Long-COT data augmentation, maximum-entropy regulated fine-tuning, and multi-step review reasoning.
- Intervention point: Dataset construction, training objective, context assembly, and inference prompts.
- What it reduces: Mislocalization, shallow explanations, and hallucinated/non-grounded comments.
- Useful feedback potentially lost: Strong reference alignment may favor issues represented in historical comments and can miss novel valid concerns.
- Coverage effect: Code flows and historical context improve semantic coverage, but data selection excludes some languages/comments and remains review-history dependent.
- Human escalation effect: Human evaluation validates factual usefulness offline; developer workflow impact is not measured.
- Computational/operational cost: Long COT generation and 8-GPU fine-tuning increase compute and prompt length; cost is unreported.
- New failure modes: Reasoning-path artifacts, context overload, judge self-preference, and dependence on generated training rationales.

## 8. Annotation and evaluator validity
- Judge/annotator: QWQ-32B generates enhanced training data; two senior software-engineering students conduct human evaluation; an LLM judge provides automated assessment.
- Rubric: Localization overlap, issue-description agreement, and factual/value judgment; 540 entries sampled with 60 overlaps.
- Agreement/reliability: Human κ=.8426; human versus LLM judge κ=.5281.
- Validity checks: In-distribution/out-of-distribution evaluation, human sampling at 95% confidence, ablations, and cross-validation of human/LLM judgments.
- Possible bias: LLM-generated reasoning/data, curated review history, language filtering, unavailable GPT-family baselines, and inconsistent placeholder publication metadata.

## 9. Quality appraisal
| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Tasks and MelcotCR intervention explicit. |
| Q2 | 2 | Dataset construction and evaluation samples reported. |
| Q3 | 2 | MEFT, long COT, context, and baselines described. |
| Q4 | 2 | IoU, Hit, Human Hit, Human Valuable, and kappa reported. |
| Q5 | 2 | Localization and factual-value rubrics defined. |
| Q6 | 2 | Human and judge agreement reported. |
| Q7 | 2 | Baselines, OOD set, and ablations included. |
| Q8 | 1 | Curated/LLM-generated data and limited baseline access constrain validity. |
| Q9 | 2 | MEFT and reasoning intervention are explicitly ablated. |
| Q10 | 1 | Hardware reported; monetary/runtime cost absent. |
| Q11 | 2 | Context, judge, and generalization risks are discussed. |
| Q12 | 2 | Direct evidence concerns generated review comments. |
- Total: `22/24` provisional
- Quality interpretation: Strong multi-dimensional evaluation evidence, with concerns about data generation, reproducibility, and metadata reliability.

## 10. Review-process reliability and bias
- Missing data: Monetary cost, detailed per-language breakdown, developer acceptance, and independent replication.
- Publication-bias concern: Author-reported comparisons and restricted access to some stronger baselines.
- Selection uncertainty: Full text available, but PDF contains contradictory JACM 2018 placeholder metadata.
- Extraction uncertainty: Moderate; some claims rely on table/figure interpretation and generated data.
- Second-reviewer agreement: Not available for this note.
- Duplicate-publication handling: Verify whether the PDF is a corrupted/placeholder publisher version or only the arXiv preprint.

## 11. Synthesis-ready conclusion
- Contribution to the SLR: Shows that structured long-chain reasoning and maximum-entropy fine-tuning can improve localization, issue description, and factual usefulness of automated review comments.
- What the paper does not establish: It does not establish production developer benefit, broad cross-language generalization, or superiority under matched compute/cost.
- Research gap supported: Review evaluation should distinguish localization, reference agreement, factual validity, and human usefulness, while reporting reasoning and data-generation cost.
- Candidate synthesis claims: Richer reasoning context can improve review quality, but it introduces substantial training/data complexity and may inherit biases from generated rationales and historical review data.
- Follow-up verification needed: Verify the publication metadata, inspect release artifacts, and reproduce the human/LLM judge comparison.
