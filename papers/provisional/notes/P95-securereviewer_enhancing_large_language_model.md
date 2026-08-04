# P95 — SecureReviewer: Enhancing Large Language Models for Secure Code Review through Secure-aware Fine-tuning

> **Provisional intake record.** This is not a canonical paper note.

| Field | Value |
|---|---|
| Project ID | `P95` (provisional) |
| Citation key | `p95_liu2025_securereviewer_enhancing_large` |
| Authors | Fang Liu; Simiao Liu; Yinghao Zhu; Xiaoli Lian; Li Zhang |
| Year | 2025 |
| Source | arXiv |
| arXiv | `2510.26457v1` |
| Screening tier | `core` |
| Reconciliation status | New candidate after initial local matching |
| Metadata status | local_arxiv_metadata |
| Evidence status | Full-text eligibility recorded; extraction not yet completed |

## 1. Identification

- Project ID: `P95` (provisional)
- Citation key: `p95_liu2025_securereviewer_enhancing_large`
- Full reference: Fang Liu; Simiao Liu; Yinghao Zhu; Xiaoli Lian; Li Zhang. “SecureReviewer: Enhancing Large Language Models for Secure Code Review through Secure-aware Fine-tuning.” arXiv:2510.26457v1, 2025; ICSE 2026 DOI: `10.1145/3744916.3773191`.
- DOI/URL: `https://doi.org/10.1145/3744916.3773191`; `https://arxiv.org/abs/2510.26457v1`
- Review date: 2026-08-04
- Source/database: arXiv/full-text screening
- Selection stage: included for reconciliation; canonical corpus integration pending
- Duplicate or companion publication: The manuscript reports an ICSE ’26 publication and DOI; publisher metadata should be checked before final integration.

## 2. Screening

- Decision: `Include`
- Relevance: `High`
- Decision rationale: Directly evaluates LLM-generated security code-review comments, security-issue detection, actionable advice, human ratings, and a security-aware evaluation metric.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: evaluation dimensions / problematic-comment taxonomy / mitigation design
- Exact inclusion criterion: Generated review comments are evaluated for issue detection and comment quality on code changes.

## 3. Study overview

- Purpose: Adapt automated code review to security issues, where general review models may produce inaccurate or generic feedback.
- Research questions: Overall detection/comment performance (RQ1), component ablations (RQ2), and performance across security types plus human quality analysis (RQ3).
- Method: Build a security-review dataset; fine-tune 7B models with a security-aware loss that upweights vulnerability-related tokens; optionally use BM25 retrieval-augmented review generation (RARG); evaluate against specialized and general LLM baselines.
- Evaluated system/artifact: SecureReviewer variants based on CodeLlama-7B, DeepSeek-Coder-6.7B, and Qwen2.5-Coder-7B. Comments follow four fields: security type, description, impact, and advice.
- Dataset/benchmark: Derived from CodeReviewer. Keyword/embedding matching plus GPT-4o judging/refinement produced 4,674 entries: seven security types and 585 Non-Issue examples. Train/validation/test sizes are 4,074/300/300; the test contains 262 security-issue samples used for expert quality control/evaluation.
- Input context: Code diffs and review comments; RARG retrieves a similar security-comment template using BM25. The isolated-diff setting does not provide full repository or inter-procedural context.
- Main findings: Best SecureReviewer variant (CodeLlama backbone) reports F1 71.98, accuracy 71.91, BLEU 11.34, and SecureBLEU 29.31. The best baseline is LlamaReviewer with F1 61.46, accuracy 61.20, BLEU 9.20, and SecureBLEU 24.56. Human ratings average 3.93 clarity, 4.06 relevance, 3.98 comprehensiveness, and 3.90 actionability on a 1–5 scale.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Secure-aware fine-tuning variants outperform listed baselines on security-issue detection and SecureBLEU; the CodeLlama variant is strongest overall in Table 2. | Reported | Sections 3.2–4.1, Table 2 |
| RQ2 | Domain fine-tuning provides the largest gain; the reweighted loss adds further detection/SecureBLEU gains, while RARG has limited incremental value for already fine-tuned models. | Reported | Section 4.2, Table 3 |
| RQ3 | Performance varies by security type; concurrency, state management, and resource management remain difficult. Human ratings are positive, but errors include superficial pattern matching and limited context awareness. | Reported | Sections 4.3, 5.1 |
| RQ4 | SecureBLEU correlates more strongly with human ratings than BLEU (r=.7533 vs .4026), supporting security-aware evaluation while remaining dependent on reference comments and extracted keywords. | Reported / limitation | Sections 3.1, 5.1–5.2 |
| RQ5 | Security specialization improves issue classification and comment utility, but the isolated-diff setting bounds context coverage. | Inferred | Sections 2–5 |
| RQ6 | The study supports separating detection accuracy, security content, human actionability, context coverage, and operational cost in review evaluation. | Inferred | Sections 3–5 |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Superficial pattern matching | Overreacting to keywords such as `map` or mutex operations and assigning the wrong security issue. | Reported failure | Section 5.1 |
| Limited contextual awareness | Missing initialization, execution flow, or inter-procedural dependencies, such as out-of-bounds vulnerabilities. | Reported failure | Section 5.1 |
| Generic or inaccurate security advice | General-purpose generation may lack security-specific descriptions and actionable remediation. | Motivation/target failure | Sections 1–2 |
| Security-type confusion | Incorrect eight-way classification propagates into comment generation. | Evaluation target / inferred failure | Sections 2.1, 3.4 |
| Linguistic mismatch | Security-relevant comments can differ from references and receive lower BLEU despite higher practical utility. | Reported limitation | Section 4.1.2 |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Issue detection | Precision, recall, F1, accuracy over eight classes. | Best variant: 73.28/71.48/71.98/71.91. | Table 2 |
| Comment quality | BLEU-4 and SecureBLEU, combining field-level BLEU with security-keyword coverage. | Best variant: BLEU 11.34, SecureBLEU 29.31. | Sections 3.1, 4.1 |
| Human quality | Two experts rate clarity, relevance, comprehensiveness, and actionability from 1–5. | Means: 3.93, 4.06, 3.98, 3.90; Cohen’s kappa=.66. | Section 5.1 |
| Metric validity | Pearson correlation with human aggregate scores. | SecureBLEU r=.7533; BLEU r=.4026. | Section 5.1 |
| Robustness by issue type | Per-type detection and comment scores. | Concurrency, state, and resource-management cases remain harder. | Section 4.3 |
| Efficiency/cost | Dataset construction tokens, API cost, and expert hours. | Approx. $46 GPT-4o cost; 98 and 87.3 person-hours reported. Inference latency is not reported. | Section 3.4 |

## 7. Mitigation and trade-offs

- Mitigation family: Security-specialized data curation, token-weighted fine-tuning, and optional retrieval grounding.
- Intervention point: Training data, loss function, prompt/context construction, and evaluation metric.
- What it reduces: Security-type misses, generic comments, and omission of security-specific impact/advice.
- Useful feedback potentially lost: Keyword-focused scoring and template retrieval may favor canonical vulnerability language and under-reward novel explanations.
- Coverage effect: Eight categories improve comparability, but the CodeReviewer-derived dataset does not establish broad repository-level coverage.
- Human escalation effect: Human evaluation is offline; workflow escalation is not measured.
- Computational/operational cost: GPT-4o judging/refinement and 185.3 reported expert hours are substantial; RARG adds retrieval/prompt complexity.
- New failure modes: Surface-pattern errors, context omission, retrieval/template mismatch, and metric sensitivity to keyword/reference design.

## 8. Annotation and evaluator validity

- Judge/annotator: GPT-4o performs candidate judging and data refinement; two security-experienced software engineers validate samples and the test set.
- Rubric: Four structured fields—security type, description, impact, advice—plus human ratings of clarity, relevance, comprehensiveness, and actionability.
- Agreement/reliability: Initial sample kappa=.74; human evaluation kappa=.66. The full training set is not manually validated.
- Validity checks: Random 351-entry sample, expert review of all 262 security test samples, component ablations, multiple baselines, and correlation with human ratings.
- Possible bias: GPT-4o curation, keyword/CWE filtering, CodeReviewer source distribution, reference-based metrics, and exclusion of Non-Issue cases from human evaluation.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Task, system, and security-review objective are explicit. |
| Q2 | 2 | Dataset construction, categories, and split are reported. |
| Q3 | 2 | Fine-tuning, loss weighting, RARG, and baselines are described. |
| Q4 | 2 | Detection, text, human, correlation, and cost measures are reported. |
| Q5 | 2 | Security categories and four-field rubric are defined. |
| Q6 | 2 | Two expert validation stages and kappa values are reported. |
| Q7 | 2 | Baseline, ablation, per-category, and human analyses are included. |
| Q8 | 1 | LLM curation, source bias, and limited context constrain validity. |
| Q9 | 2 | Interventions are explicit and separately ablated. |
| Q10 | 1 | Data-construction cost is reported, but inference/runtime cost is absent. |
| Q11 | 2 | Surface matching, context limits, and dataset threats are discussed. |
| Q12 | 2 | Direct evidence concerns generated security-review comments. |

- Total: `22/24` provisional
- Quality interpretation: Strong direct evidence for security-focused review evaluation, with limitations in data provenance, repository context, and runtime-cost reporting.

## 10. Review-process reliability and bias

- Missing data: Developer acceptance, false-positive burden, repository-level context, and production/runtime cost.
- Publication-bias concern: Results are reported by the proposing authors; independent replication is not assessed.
- Selection uncertainty: Full text is available and the DOI/preprint relationship is stated, but final publisher metadata needs verification.
- Extraction uncertainty: Moderate; several per-type results are figure-based rather than tabulated.
- Second-reviewer agreement: Not available for this note.
- Duplicate-publication handling: Treat arXiv and ICSE records as one study after publisher metadata confirmation.

## 11. Synthesis-ready conclusion

- Contribution to the SLR: Provides direct evidence that security-aware fine-tuning and structured evaluation can improve detection and perceived usefulness of LLM-generated secure code-review comments.
- What the paper does not establish: It does not establish repository-level effectiveness, lower developer workload, or generalization beyond its CodeReviewer-derived security dataset.
- Research gap supported: Secure review evaluation should combine issue detection, security-specific content, human actionability, context coverage, and operational cost.
- Candidate synthesis claims: Security specialization can improve issue classification and comment utility, but keyword/template grounding may introduce surface-pattern errors and context-boundary failures.
- Follow-up verification needed: Confirm final ICSE metadata, inspect released code/data, and verify independent reproducibility.
