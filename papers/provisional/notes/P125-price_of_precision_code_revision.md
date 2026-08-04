# P125 — The Price of Precision: The Cost of Preprocessing for Automated Code Revision in Code Review

## 1. Identification

| Field | Value |
|---|---|
| Project ID | `P125` |
| Citation key | `p125_pirouzkhah2026_price_precision` |
| Authors | Shirin Pirouzkhah; Pooja Rani; Francesco Sovrano; Vincent Hellendoorn; Alberto Bacchelli |
| Year | 2026 |
| Source | Empirical Software Engineering 31, Article 47 |
| DOI | 10.1007/s10664-025-10781-4 |

## 2. Screening

- **Scope decision:** Include as core evidence for evaluation validity and preprocessing cost/benefit trade-offs in code-review automation.
- **Evidence boundary:** Full text was acquired and verified locally; exact results and page locations require detailed extraction.

## 3. Study overview

The study examines how preprocessing choices affect automated code-revision evaluation and the associated performance cost. It is relevant to the framework because metric validity and computational cost can move in opposite directions.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Preprocessing is treated as an evaluation design choice rather than a neutral implementation detail. | Reported | Abstract; full text |
| RQ2 | Precision and computational/model-scale costs must be reported jointly. | Reported/inferred | Full text |
| RQ3 | Automated code-review pipelines can trade evaluation validity against throughput or cost. | Reported/inferred | Full text |

## 5. Evaluation dimensions and metrics

Exact preprocessing variants, metrics, effect sizes, and section/page locations remain to be verified from the PDF before synthesis citation.

## 6. Validity threats and quality appraisal

Assess benchmark representativeness, sensitivity to preprocessing configuration, reproducibility of cost measurements, and transfer from code revision to generated review comments.

## 7. Failure and problematic-comment categories

Preprocessing-induced measurement distortion and incomplete evaluation context are the relevant provisional categories; exact categories require full-text extraction.

## 8. Mitigation and trade-offs

- **Useful feedback potentially lost:** Aggressive normalization may remove information needed to assess a review or revision.
- **Coverage:** Results may depend on the selected code-revision tasks and preprocessing configurations.
- **Human escalation:** Human review is needed when automated preprocessing changes the meaning of an artifact.
- **Cost:** More precise preprocessing can increase runtime, engineering complexity, and reproducibility burden.

## 9. Annotation and evaluator validity

Record datasets, preprocessing variants, metrics, baselines, and cost-measurement protocol from the full text before final synthesis.

## 10. Review-process reliability and bias

Potential risks include benchmark-selection bias, metric sensitivity to normalization, and conflation of revision quality with review-comment quality.

## 11. Synthesis-ready conclusion

Evaluation pipelines should report preprocessing choices and their cost because apparent precision gains may carry computational or validity trade-offs. This claim remains provisional pending exact evidence extraction.

## 12. Canonical research-question coverage

| RQ | Evidence status |
|---|---|
| RQ1 | Evaluation validity is directly relevant. |
| RQ2 | Preprocessing context requires verification. |
| RQ3 | Metric trade-offs require exact extraction. |
| RQ4 | Applicability to generated comments requires bounded interpretation. |
| RQ5 | Cost reporting is relevant. |
| RQ6 | Human alignment remains to be assessed. |

## 13. Quality evidence

| Criterion | Evidence |
|---|---|
| Q1–Q12 | Full-text extraction pending; no exact score assigned. |
| Q1 | Study purpose and evaluation setting identified. |
| Q2 | Dataset and task sampling require verification. |
| Q3 | Preprocessing protocol requires exact extraction. |
| Q4 | Metric validity requires assessment. |
| Q5 | Cost measurement requires exact extraction. |
| Q6 | Benchmark coverage requires assessment. |
| Q7 | Failure categories require exact extraction. |
| Q8 | Mitigation evidence requires verification. |
| Q9 | Precision-cost trade-off requires bounded interpretation. |
| Q10 | Reliability and bias require assessment. |
| Q11 | Reproducibility details require verification. |
| Q12 | Transfer to generated comments remains provisional. |

## 14. Provisional synthesis claim

Evaluation pipelines should report preprocessing choices and their cost because apparent precision gains may carry computational or validity trade-offs. This claim remains provisional pending exact evidence extraction.
