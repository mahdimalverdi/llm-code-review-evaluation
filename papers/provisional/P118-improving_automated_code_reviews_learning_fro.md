# P118 — Improving Automated Code Reviews: Learning from Experience

## 1. Identification

| Field | Value |
|---|---|
| Project ID | `P118` |
| Citation key | `p118_lin2024_improving_automated_code_revie` |
| Authors | Hong Yi Lin; Patanamon Thongtanunam; Christoph Treude; Wachiraphan Charoenwet |
| Year | 2024 |
| Source | arXiv preprint, `2402.03777v1` |
| Study type | Experience-aware training-data reweighting and human evaluation |

## 2. Screening

- **Scope decision:** Include as core evidence for reviewer-experience signals, training-data quality, and actionable comment evaluation.
- **Task:** Generate code-review comments from code changes using CodeReviewer with experience-aware oversampling.
- **Evidence boundary:** Reviewer experience is inferred from repository ownership metrics; the study does not directly observe expertise or downstream developer outcomes.
- **Metadata caveat:** Publisher/duplicate status and the provisional BibTeX record require verification.

## 3. Study overview

The study fine-tunes CodeReviewer after oversampling examples associated with experienced reviewers and authors. Experience is approximated using Authoring Code Ownership (ACO) and Review-Specific Ownership (RSO). The dataset is derived from GitHub pull requests, with 150,406 original training comments and final processed sets of 141,259 training, 12,406 validation, and 12,369 test comments. Three oversampling groups are compared: major reviewers/major authors (MRMA), major reviewers (MR), and major authors (MA), each upsampled by 400%. Evaluation combines BLEU-4, semantic equivalence, applicability, feedback type, explanation, and comment category on 100 samples.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Oversampling models generate more semantically equivalent comments than the original model, despite slightly lower BLEU. | Reported | Table 4 |
| RQ2 | Oversampling increases applicable comments and explanation, while reducing confused questions and changing suggestion/concern balance. | Reported | Table 5; RQ2 |
| RQ3 | Models produce more functional, validation, logical, resource, and maintenance-related comments, with differences by experience group. | Reported | Figure 2; RQ3 |
| RQ4 | Reviewer familiarity is represented through repository-level authoring and reviewing ownership metrics. | Reported | Section 3.2 |
| RQ5 | Experience-aware oversampling improves comment quality without new data, but 400% ratios are arbitrary and may trade coverage for reviewer-style bias. | Reported/limitation | Sections 3–5 |
| RQ6 | Manual review of 100 samples and Cohen’s kappa ranges provide human validity, although agreement is low for some dimensions. | Reported/limitation | Section 3.5 |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Confused question | Comment indicates lack of understanding rather than a useful concern or solution. | Human category | Table 5 |
| Unapplicable comment | Comment does not raise a valid concern or suggestion for the pull request. | Human category | Table 5 |
| Missing explanation | Comment identifies an issue but does not explain rationale or remediation. | Human category | Table 5 |
| Underrepresented critical issue | Baseline underproduces logic, validation, resource, or functional feedback. | Category analysis | Figure 2 |
| Ownership-proxy error | Repository activity inaccurately labels reviewer experience because of deletions, aliases, or missing accounts. | Threat | Section 5 |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Lexical similarity | BLEU-4 on full test set | Original 7.27; oversampling models are slightly lower, despite better semantic results. | Table 4 |
| Semantic correctness | Manual equivalence to the ground-truth intention | Original 15/100; oversampling reaches 16–21/100, with MA highest. | Table 4 |
| Applicability | Valid suggestion/concern in PR context | Original 40/100; MRMA/MR 43/100; MA 45/100. | Table 5 |
| Informational value | Suggestion, concern, or confused-question type | Oversampling increases suggestions and reduces confusion. | Table 5 |
| Explanation | Presence of rationale or explanation | Original 4/40 applicable comments; oversampling 9–16/approximately 40. | Table 5 |
| Issue coverage | 18-category comment taxonomy | Experience-aware models produce more critical logic, validation, resource, and maintenance comments. | Figure 2 |
| Annotation reliability | Cohen’s kappa ranges by task | Semantic equivalence .28–.45; applicability .12–.35; feedback type .52–1; explanation .46–.63; category .17–.33. | Section 3.5 |

## 7. Mitigation and trade-offs

- **Mitigation family:** Experience-aware data selection and oversampling during fine-tuning.
- **Intervention point:** Training-data distribution rather than model architecture or inference prompting.
- **What it reduces:** Underuse of high-quality reviewer examples, confused questions, and weak explanations.
- **Useful feedback potentially lost:** Oversampling experienced reviewers may reduce diversity and overfit to dominant ownership/review styles.
- **Coverage:** Targeting experienced examples improves critical issue types, but may underrepresent novice perspectives or less common repositories.
- **Human escalation:** Generated comments still require human judgment; experience metadata does not guarantee correctness.
- **Cost:** Oversampling increases effective training exposure without collecting data, but training and ownership mining require substantial compute/API work.
- **New failure modes:** Proxy-based experience misclassification, arbitrary sampling ratios, and bias toward repository insiders.

## 8. Annotation and evaluator validity

- **Human sample:** Two evaluators manually assess 100 test comments for semantic equivalence, applicability, feedback type, explanation, and issue category.
- **Process:** The first and fourth authors independently evaluate 25 samples, then one reviews the remaining classifications.
- **Agreement:** Cohen’s kappa is strongest for feedback type but low for semantic equivalence, applicability, and category.
- **Rubric:** Applicability is context-based rather than reference-equivalence-based, which is a useful validity distinction.
- **Threats:** Co-author evaluation, low agreement for key dimensions, ownership heuristics, and incomplete GitHub metadata.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Three research questions and experience-aware objective are explicit. |
| Q2 | 2 | Large GitHub dataset and processed counts are described. |
| Q3 | 2 | Ownership metrics, sampling groups, model, and training settings are detailed. |
| Q4 | 2 | BLEU, semantic, applicability, explanation, and category outcomes are reported. |
| Q5 | 2 | Human rubric distinguishes semantic correctness and practical applicability. |
| Q6 | 1 | Kappa is reported, but low for several dimensions. |
| Q7 | 2 | Original, MRMA, MR, and MA models are compared. |
| Q8 | 1 | Large open-source sample, but reviewer demographic and repository bias remain. |
| Q9 | 2 | Experience-aware oversampling is directly evaluated. |
| Q10 | 1 | Resource-efficient motivation, but no deployment cost/latency. |
| Q11 | 2 | Comment categories, confusion, explanation, and ownership risks are analyzed. |
| Q12 | 2 | Directly targets actionable generated review comments. |

**Total: 21/24 — high confidence for experience-aware training evidence, with annotation and proxy limitations.**

## 10. Review-process reliability and bias

- **Experience-proxy bias:** ACO/RSO may undercount expertise when accounts, repositories, or historical data are missing.
- **Sampling bias:** Upsampling major reviewers/authors may encode local ownership norms rather than universally useful review practice.
- **Annotation uncertainty:** Low kappa for applicability and semantic equivalence weakens fine-grained conclusions.
- **Metric divergence:** BLEU decreases while semantic/applicability measures improve, demonstrating reference-metric limitations.
- **External validity:** GitHub data and ownership patterns may not represent industrial review teams or private repositories.
- **Missing outcomes:** No accepted-fix rate, developer trust, reviewer workload, or longitudinal model effect is measured.

## 11. Synthesis-ready conclusion

- P118 shows that training datasets contain underused quality variation associated with reviewer experience.
- Oversampling experienced reviewer examples can improve semantic correctness, applicability, explanation, and coverage of critical issue types without new data.
- The results also show why BLEU alone is inadequate: lexical scores can decline while human-relevant quality improves.
- Experience-aware training introduces a coverage/fairness trade-off and depends on imperfect ownership proxies and low-agreement human labels.
- Use as core evidence for supervision quality, reviewer-experience signals, and multi-dimensional evaluation of generated comments.

