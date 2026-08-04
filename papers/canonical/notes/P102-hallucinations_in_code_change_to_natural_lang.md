# P102 — Hallucinations in Code Change to Natural Language Generation: Prevalence and Evaluation of Detection Metrics

> **Provisional intake record.** This is not a canonical paper note.

| Field | Value |
|---|---|
| Project ID | `P102` (provisional) |
| Citation key | `p102_liu2025_hallucinations_in_code_change_` |
| Authors | Chunhua Liu; Hong Yi Lin; Patanamon Thongtanunam |
| Year | 2025 |
| Source | arXiv |
| arXiv | `2508.08661v1` |
| Screening tier | `core` |
| Reconciliation status | New candidate after initial local matching |
| Metadata status | local_arxiv_metadata |
| Evidence status | Full-text eligibility recorded; extraction not yet completed |

## 1. Identification

- Duplicate or companion publication: No publisher venue or DOI is reported; verify before final integration.

## 2. Screening
- Decision: `Include`; Relevance: `High`
- Decision rationale: Directly measures hallucination prevalence in generated code-review comments and evaluates automatic detection metrics.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: problematic-comment taxonomy / evaluator validity / mitigation design

## 3. Study overview
- Purpose: Characterize hallucinations in code-change-to-natural-language generation and test whether metric-based signals can detect them.
- Research questions: Hallucination prevalence/types in code review and commit messages (RQ1) and effectiveness of reference-based/reference-free detection metrics (RQ2).
- Method: Generate outputs with three selected models, manually annotate hallucinations using a CodeChange2NL workflow, and evaluate individual/multi-metric logistic-regression detectors with ROC-AUC.
- Evaluated system/artifact: Fine-tuned CCT5, Llama3.1, and Qwen2.5 models on CodeReviewer and CommitBench tasks.
- Dataset/benchmark: 264 samples × 3 models for CodeReviewer comments and 268 × 3 for CommitBench messages; 1,596 outputs annotated in total.
- Input context: Code changes/diffs and task-specific prompts; code review outputs must identify issues and suggest improvements, while commit messages describe changes.
- Main findings: Hallucination rates are approximately 42.8–47.0% for code review and 14.2–21.6% for commit messages. Individual metrics are weak (ROC-AUC about .538–.566 on CodeReviewer); combining metrics reaches .69 on CodeReviewer and .75 on CommitBench.

## 4. Evidence mapped to review questions
| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Hallucinations are common in code-review generation, with input inconsistency dominant and logic/intent errors also present. | Reported | Sections 4.1–4.2, Table 3 |
| RQ2 | Individual reference/reference-free metrics are near chance, while complementary uncertainty and attribution features substantially improve detection. | Reported | Section 5, Tables 4–6 |
| RQ3 | Specialized and general models exhibit different hallucination profiles: CCT5 has more logic inconsistency; larger general models show more intent deviation. | Reported | Section 4.2 |
| RQ4 | Model confidence can be informative but may be overconfident; attribution signals reveal whether generation attends to changed code. | Inferred | Section 5.2 |
| RQ5 | BLEU/reference agreement does not ensure factual alignment with the code change. | Reported / inferred | Sections 4–5 |
| RQ6 | Hallucination evaluation should combine model-internal uncertainty, source attribution, reference similarity, and human labels. | Inferred | Sections 3–6 |

## 5. Failure and problematic-comment categories
| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Input inconsistency | Generated text contradicts or fabricates information relative to the code change. | Taxonomy/reported | Sections 3.2, 4.2 |
| Logic inconsistency | Internal reasoning or explanation is contradictory. | Taxonomy/reported | Sections 3.2, 4.2 |
| Intention violation | Output performs the wrong task, such as a summary instead of a review comment. | Taxonomy/reported | Sections 3.2, 4.2 |
| Input repetition | Output repeats input tokens without meaningful interpretation. | Taxonomy | Section 3.2 |
| Reference mismatch | Strong lexical/reference score masks unsupported or wrong content. | Evaluator failure | Sections 4–5 |

## 6. Evaluation dimensions and metrics
| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Hallucination prevalence | Manual taxonomy labels and total hallucination percentage. | Code review 42.8–47.0%; commit messages 14.2–21.6%. | Table 3 |
| Individual detection | ROC-AUC for BLEU, entailment, similarity, uncertainty, and attribution metrics. | Generator-agnostic CodeReviewer .538–.566; CommitBench .562–.617. | Section 5.1 |
| Combined detection | Logistic regression using multiple metrics; accuracy and ROC-AUC. | Combined ROC-AUC .69 CodeReviewer and .75 CommitBench. | Section 5.2 |
| Annotation reliability | Cohen’s kappa across pilot/final annotation. | Final κ=.98 CodeReviewer and .96 CommitBench; pilot agreement lower. | Section 4.2 |
| Model/task variation | Compare CCT5, Llama3.1, Qwen2.5 and two CodeChange2NL tasks. | Detection effectiveness varies by generator and dataset. | Sections 4–5 |
| Cost/operations | Inference-time confidence/attribution signals. | Potential detection without references; runtime/cost is not reported. | Section 5.2 |

## 7. Mitigation and trade-offs
- Mitigation family: Multi-metric inference-time detection using uncertainty and feature attribution, optionally with reference signals.
- Intervention point: Post-generation monitoring and output acceptance/filtering.
- What it reduces: Unsupported code claims, inconsistent reasoning, and task-intent deviations.
- Useful feedback potentially lost: Aggressive hallucination filters may suppress unusual but valid review comments, especially when confidence is low.
- Coverage effect: Reference-free metrics enable deployment without human references, but model/dataset-specific calibration is required.
- Human escalation effect: Detection scores can route suspicious comments to human review; workflow escalation is not tested.
- Computational/operational cost: Attribution and multiple metric calculations add inference overhead; no latency/cost measurements are reported.
- New failure modes: Confidence overconfidence, attribution instability, metric multicollinearity, and detector dependence on generator/dataset.

## 8. Annotation and evaluator validity
- Judge/annotator: Two authors with 5+ years’ experience annotate all outputs; two pilot rounds refine the taxonomy/guidelines.
- Rubric: Input inconsistency, logic inconsistency, intention violation, input repetition, and other hallucination types, with task-specific output validity.
- Agreement/reliability: Final κ=.98/.96 after discussion; pilot κ=.36/.30 then .56/.38.
- Validity checks: Large multi-model sample, pilots, cross-examination, reference-based and reference-free metrics, and generator-specific analysis.
- Possible bias: Authors annotate their own model outputs, selected fine-tuned models, limited datasets, and possible dependence on generated reference quality.

## 9. Quality appraisal
| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Tasks, hallucination concept, and questions explicit. |
| Q2 | 2 | Datasets, models, and 1,596 outputs reported. |
| Q3 | 2 | Annotation workflow and metric families described. |
| Q4 | 2 | Prevalence, ROC-AUC, logistic regression, and kappa reported. |
| Q5 | 2 | Hallucination taxonomy defined. |
| Q6 | 2 | Pilot/final agreement and adjudication reported. |
| Q7 | 2 | Multiple generators, tasks, and metric combinations evaluated. |
| Q8 | 1 | Limited tasks/models and author annotation constrain validity. |
| Q9 | 2 | Multi-metric detection is empirically evaluated. |
| Q10 | 1 | Inference-time signals discussed but cost unmeasured. |
| Q11 | 2 | Generator, dataset, and metric limitations discussed. |
| Q12 | 2 | Direct code-review hallucination evidence. |
- Total: `22/24` provisional
- Quality interpretation: Strong taxonomy and evaluator-validity evidence, with limited operational and external-validity data.

## 10. Review-process reliability and bias
- Missing data: Developer impact, detector latency/cost, independent annotation, and production false-positive burden.
- Publication-bias concern: Model selection and annotations are author-controlled; code/data release is promised upon acceptance.
- Selection uncertainty: Full text available; final publisher metadata unverified.
- Extraction uncertainty: Moderate; some metric values are figure/table based.
- Second-reviewer agreement: Not available for this note.
- Duplicate-publication handling: Check for a later venue/version before final bibliography integration.

## 11. Synthesis-ready conclusion
- Contribution to the SLR: Establishes that hallucination is prevalent in LLM-generated review comments and that lexical/reference metrics alone are weak detectors.
- What the paper does not establish: It does not establish developer acceptance, production detector reliability, or robustness beyond the studied models/tasks.
- Research gap supported: Review systems need factual-alignment labels and calibrated, reference-free hallucination monitoring alongside quality/actionability evaluation.
- Candidate synthesis claims: Combining uncertainty and source-attribution signals can detect hallucinations better than individual metrics, but calibration is generator- and dataset-dependent.
- Follow-up verification needed: Inspect the promised code/data release, reproduce annotation agreement, and evaluate detector precision/recall under deployment conditions.
