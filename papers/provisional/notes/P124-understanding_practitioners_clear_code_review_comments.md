# P124 — Understanding Practitioners' Expectations on Clear Code Review Comments

## 1. Identification

| Field | Value |
|---|---|
| Project ID | `P124` |
| Citation key | `p124_chen2025_clear_code_review_comments` |
| Authors | Junkai Chen; Zhenhao Li; Qiheng Mao; Xing Hu; Kui Liu; Xin Xia |
| Year | 2025 |
| Source | Proceedings of the ACM on Software Engineering 2 (ISSTA) |
| DOI | 10.1145/3728931 |

## 2. Screening

- **Scope decision:** Include as supporting evidence for human-centred clarity and usefulness evaluation.
- **Evidence boundary:** Full text was acquired locally; exact results and page locations require detailed extraction.

## 3. Study overview

The study investigates practitioners' expectations for clear code-review comments and introduces the RIE clarity attributes and ClearCRC evaluation context. It informs rubric design for generated comments, but does not by itself establish model performance.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Clarity is treated as a human-centred quality property of review feedback. | Reported | Abstract; full text |
| RQ2 | The attributes provide candidate rubric dimensions for comment evaluation. | Reported/inferred | Full text |
| RQ3 | Practitioner expectations constrain what counts as useful feedback. | Reported | Full text |

## 5. Evaluation dimensions and metrics

Exact operational definitions, quantitative results, and section/page locations remain to be verified from the PDF before synthesis citation.

## 6. Validity threats and quality appraisal

Assess sampling, participant representativeness, annotation agreement, and transfer from human-written to LLM-generated comments during final extraction.

## 7. Failure and problematic-comment categories

Clarity failures and insufficiently specific or actionable comments are the relevant provisional categories; exact definitions require full-text extraction.

## 8. Mitigation and trade-offs

- **Useful feedback potentially lost:** A narrow clarity rubric may miss domain-specific or technically subtle usefulness.
- **Coverage:** Practitioner expectations may not cover all repositories, languages, or review cultures.
- **Human escalation:** Human judgement remains necessary for ambiguous or context-dependent comments.
- **Cost:** Eliciting and applying richer clarity attributes increases annotation and evaluation effort.

## 9. Annotation and evaluator validity

Record participant sampling, annotation protocol, agreement, and evaluator calibration from the full text before final synthesis.

## 10. Review-process reliability and bias

Potential risks include sampling bias in practitioner expectations and hindsight or social-desirability effects in reported preferences.

## 11. Synthesis-ready conclusion

Clarity should be evaluated as a practitioner-facing, multidimensional property rather than inferred from lexical similarity alone. This bounded claim remains provisional until exact evidence locations are recorded.

## 12. Canonical research-question coverage

| RQ | Evidence status |
|---|---|
| RQ1 | Human-centred clarity construct is relevant. |
| RQ2 | Rubric dimensions require verification. |
| RQ3 | Practitioner expectations inform usefulness. |
| RQ4 | Context dependence remains to be extracted. |
| RQ5 | Actionability relation remains to be extracted. |
| RQ6 | Evaluator validity requires verification. |

## 13. Quality evidence

| Criterion | Evidence |
|---|---|
| Q1–Q12 | Full-text extraction pending; no exact score assigned. |
| Q1 | Study purpose and clarity construct identified. |
| Q2 | Dataset and participant sampling require verification. |
| Q3 | Annotation protocol requires verification. |
| Q4 | Evaluator validity requires verification. |
| Q5 | Metrics require exact extraction. |
| Q6 | Context coverage requires assessment. |
| Q7 | Failure categories require exact extraction. |
| Q8 | Mitigation evidence requires verification. |
| Q9 | Trade-offs require bounded interpretation. |
| Q10 | Reliability and bias require assessment. |
| Q11 | Reproducibility details require verification. |
| Q12 | Synthesis transfer remains provisional. |

## 14. Provisional synthesis claim

Clarity should be evaluated as a practitioner-facing, multidimensional property rather than inferred from lexical similarity alone. This bounded claim remains provisional until exact evidence locations are recorded.
