# P106 — Automated Code Review Using Large Language Models with Symbolic Reasoning

## 1. Identification

| Field | Value |
|---|---|
| Project ID | `P106` |
| Citation key | `p106_icoz2025_automated_code_review_using_la` |
| Authors | Busra Icoz; Goksel Biricik |
| Year | 2025 |
| Source | arXiv preprint, `2507.18476v1` |
| Study type | Controlled empirical comparison of code-defect classifiers |

## 2. Screening

- **Scope decision:** Include as supporting evidence for hybrid, trade-off-aware evaluation of automated code review.
- **Population/task:** Python code-defect detection framed as automated review.
- **Evidence boundary:** The extracted preprint reports model metrics, but does not evaluate the usefulness, correctness, or acceptance of natural-language review comments by human reviewers.
- **Metadata caveat:** Publisher/duplicate status and the provisional BibTeX record still require verification before submission.

## 3. Study overview

The study combines fine-tuned CodeT5, CodeBERT, and GraphCodeBERT with few-shot prompting and a knowledge map containing 20 Python bug patterns and best practices. The knowledge map is presented as a symbolic-reasoning aid, although the paper does not provide a formal symbolic inference procedure or an independently validated knowledge-base construction protocol. Experiments use the Python defect-detection portion of CodeXGLUE, with clean/buggy labels, and compare a base condition, few-shot prompting, fine-tuning, and the proposed hybrid condition. Reported metrics are precision, recall, F1, and accuracy.

## 4. Evidence mapped to review questions

| Review question | Extracted evidence | Interpretation / boundary |
|---|---|---|
| RQ1 | Binary Python code-defect detection using CodeT5, CodeBERT, and GraphCodeBERT. | Reported | CodeXGLUE evaluation |
| RQ2 | Precision, recall, F1-score, and accuracy across three models and four configurations. | Reported | Tables I–IV |
| RQ3 | Hallucinations, semantic limitations, false positives, and missed defects are motivated, but no categorized output-level analysis is reported. | Limitation | Introduction; evaluation |
| RQ4 | Fine-tuning, few-shot labeled examples, and a knowledge map of Python bug patterns/best practices provide task context. | Reported | Sections III–IV |
| RQ5 | Hybrid prompting and knowledge-map integration improve reported classification results; effects vary by model. | Reported/inferred | Tables I–IV |
| RQ6 | Fixed benchmark and standard metrics are used; no human evaluation, agreement, external-project validation, or robustness test is reported. | Limitation | Evaluation design |

## 5. Failure and problematic-comment categories

| Category | Evidence in study | Relevance |
|---|---|---|
| False-positive defect reports | Precision is explicitly used to represent the ability to avoid flagging clean code. | Directly relevant to review noise and trust. |
| Missed defects | Recall is used to measure detection of buggy examples. | Directly relevant to omission risk. |
| Semantic/logical weakness | The introduction motivates symbolic support because LLMs may not understand deeper code semantics. | Relevant motivation, but not a measured error category. |
| Hallucinated findings | Hallucinations are identified as a limitation of automated review systems. | Relevant risk, without comment-level prevalence estimates. |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization | Result pattern |
|---|---|---|
| Detection precision | Proportion of predicted buggy samples that are buggy | GraphCodeBERT reaches 0.485 in the fine-tuned and hybrid conditions. |
| Detection recall | Proportion of buggy samples detected | CodeT5 and CodeBERT report 0.534 in the hybrid condition; GraphCodeBERT reports 0.532. |
| Balanced classification performance | F1-score | GraphCodeBERT reports 0.381 in the hybrid condition. |
| Overall classification accuracy | Correct predictions over clean and buggy samples | Hybrid accuracy is 0.621 for CodeT5, 0.598 for CodeBERT, and 0.687 for GraphCodeBERT. |
| Efficiency | The abstract claims improved efficiency, but the extracted experiments do not report runtime, token, or human-time measurements. | Efficiency remains insufficiently operationalized. |

## 7. Mitigation and trade-offs

- Fine-tuning, few-shot examples, and the knowledge map are combined as a hybrid intervention.
- GraphCodeBERT benefits most in the reported comparison, while CodeBERT shows smaller gains; therefore, the intervention is model-dependent.
- Precision and recall are not interchangeable: increasing defect sensitivity can increase review noise, so a single accuracy score is inadequate for deployment decisions.
- The knowledge map improves reported classification metrics, but its coverage, maintenance cost, and effect on out-of-distribution defects are not evaluated.
- Useful feedback potentially lost: a binary defect label does not represent nuanced review guidance or cross-cutting concerns.
- Coverage: the Python benchmark and 20-pattern map may omit repository-specific and inter-procedural defects.
- Human escalation: no escalation protocol or human confirmation step is evaluated.
- Cost: training and knowledge-map maintenance costs are not reported; runtime efficiency is claimed but not measured.

## 8. Annotation and evaluator validity

- Labels are inherited from the CodeXGLUE Python defect-detection task; the extraction does not describe new annotation or inter-rater agreement.
- The evaluation uses automated metrics rather than expert assessment of review comments.
- The paper does not report calibration, threshold analysis, confidence intervals, statistical significance, or tests on repositories outside CodeXGLUE.
- Consequently, metric improvements should be treated as benchmark-level evidence rather than evidence of improved reviewer outcomes.

## 9. Quality appraisal

| Criterion | Score (0–2) | Rationale |
|---|---:|---|
| Clear objective | 2 | The hybrid code-review objective is explicit. |
| Relevant population/task | 2 | Python defect detection is relevant to automated review. |
| Dataset described | 2 | CodeXGLUE and the Python subset are identified. |
| Model/configuration described | 2 | Models, fine-tuning, prompting, and knowledge-map conditions are described. |
| Baseline comparison | 2 | Base, few-shot, fine-tuned, and hybrid conditions are compared. |
| Metrics appropriate | 2 | Precision, recall, F1, and accuracy fit binary defect detection. |
| Error analysis | 0 | No systematic manual or per-category error analysis is reported. |
| Human validation | 0 | No reviewer or expert validation is reported. |
| External validity | 0 | Evaluation is limited to a CodeXGLUE Python benchmark. |
| Reproducibility | 1 | Training details are partly reported, but the knowledge map and full implementation are not sufficiently specified. |
| Statistical support | 0 | No uncertainty or significance analysis is reported. |
| Outcome alignment | 1 | Defect detection aligns with review support, but natural-language comment quality is not measured. |

| Q1 | 2 | Objective and hybrid intervention are explicit. |
| Q2 | 2 | CodeXGLUE and its Python defect task are identified. |
| Q3 | 2 | Models, training settings, prompting, and knowledge-map design are described. |
| Q4 | 2 | Standard classification metrics are reported. |
| Q5 | 1 | No human comment-quality rubric is used. |
| Q6 | 0 | No inter-rater agreement or uncertainty analysis. |
| Q7 | 1 | Multiple models and configurations are compared. |
| Q8 | 0 | No external validity study beyond the benchmark. |
| Q9 | 2 | Fine-tuning, few-shot prompting, and knowledge-map mitigation are specified. |
| Q10 | 0 | Runtime/cost efficiency is not quantitatively reported. |
| Q11 | 1 | Precision/recall trade-offs are discussed but not threshold-analyzed. |
| Q12 | 1 | Relevant defect-detection evidence, but no end-to-end review outcome. |

**Total: 14/24 — moderate-low confidence for synthesis; useful primarily as benchmark-level supporting evidence.**

## 10. Review-process reliability and bias

- The benchmark and binary labels may not represent the diversity of defects, repositories, or review practices encountered in production.
- Reported gains may reflect dataset-specific adaptation and class-balancing choices, including random oversampling.
- The hybrid intervention bundles multiple changes, limiting causal attribution to symbolic reasoning alone.
- The paper’s claims about improved efficiency and reliability exceed the directly reported validation of classification metrics; these claims should be narrowed in synthesis.

## 11. Synthesis-ready conclusion

- P106 supports the proposition that structured defect knowledge, few-shot examples, and fine-tuning can improve benchmark-level code-defect classification.
- Its strongest contribution for this review is to make the precision–recall trade-off explicit when automated findings are used to support code review.
- It does not establish that the resulting natural-language comments are correct, actionable, understandable, or beneficial to human reviewers.
- Use as supporting evidence for context-aware detection and hybrid mitigation, with a clear external-validity and human-evaluation caveat.
