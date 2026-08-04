# P123 — Example Driven Code Review Explanation

## 1. Identification

| Field | Value |
|---|---|
| Project ID | `P123` |
| Citation key | `p123_rahman2022_example_driven_code_review_exp` |
| Authors | Shadikur Rahman; Umme Ayman Koana; Maleknaz Nayebi |
| Year | 2022 |
| Source | arXiv preprint, `2207.11627v1` |
| Study type | Industrial case study and example-retrieval prototype |

## 2. Screening

- **Scope decision:** Include as core evidence for explanation quality, ambiguity detection, retrieval context, and actionable review feedback.
- **Task:** Identify unclear review comments and retrieve similar historical examples to explain them.
- **Evidence boundary:** EDRE evaluates classification strongly but only preliminarily evaluates whether retrieved examples are useful to developers.
- **Metadata caveat:** Publisher/duplicate status and the provisional BibTeX record require verification.

## 3. Study overview

Example Driven Review Explanation (EDRE) addresses short or ambiguous review comments that require follow-up communication. The system first classifies review clarity using text embeddings and classifiers, then retrieves five similar historical reviews as analogical examples. The study analyzes 3,722 labeled reviews from three projects of an industrial partner and compares TF-IDF, SentenceBERT, and USE embeddings with Naive Bayes, SVM, Random Forest, logistic regression, and GBRT. A prototype GitHub bot is evaluated on 744 held-out reviews, with 2,978 reviews used for training.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | The task is to identify reviews needing explanation using a four-point clarity label; TF-IDF with SVM performs best. | Reported | RQ1; Table 2 |
| RQ2 | EDRE retrieves five similar historical reviews using cosine similarity to provide context-specific examples. | Reported | RQ2 |
| RQ3 | The motivating failure is short, unclear, or unactionable feedback that increases communication overhead. | Reported | Introduction |
| RQ4 | Historical reviews across projects serve as analogical context for interpreting a new review. | Reported | EDRE design |
| RQ5 | Example retrieval is proposed as a lightweight explanation aid rather than a prescriptive replacement for reviewer judgment. | Proposed | RQ2/conclusion |
| RQ6 | Industrial data, classifier metrics, held-out prototype testing, and qualitative usefulness judgments provide evidence; full developer usefulness evaluation remains pending. | Reported/limitation | Sections 4–6 |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Unclear review | Review needs additional explanation according to the four-point clarity label. | Annotated classification target | RQ1 |
| Short/unactionable feedback | Comment lacks enough context for a developer to understand or act. | Motivation | Introduction |
| Example irrelevance | Retrieved historical comment is textually similar but does not explain the target review. | Retrieval risk | RQ2 |
| Cross-project mismatch | Example reflects another project/team’s conventions and may mislead. | Validity risk | Limitations |
| Non-prescriptive ambiguity | Example offers analogy without guaranteeing that the same fix or interpretation applies. | Design caveat | RQ2 |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Clarity classification | Precision, recall, F-score, and accuracy across embeddings/classifiers | TF-IDF+SVM reaches approximately 92% F-score and 90% accuracy. | Table 2 |
| Explanation retrieval | Cosine similarity and ranked top-five historical examples | Retrieves examples for reviews classified as needing explanation. | RQ2 |
| Example usefulness | Human/industrial preliminary judgment of top-five examples as useful or somewhat useful | Positive preliminary result; full usefulness study remains future work. | Section 5.2 |
| Context coverage | Three projects and cross-project historical review corpus | Industrial context supports realism, but cross-team generalization is limited. | Dataset |
| Workflow integration | GitHub bot prototype | Demonstrates delivery path, not adoption or productivity impact. | Figure 6 |

## 7. Mitigation and trade-offs

- **Mitigation family:** Ambiguity classification, historical example retrieval, TF-IDF similarity, and GitHub integration.
- **Intervention point:** Explanation/context delivery after review generation.
- **What it reduces:** Follow-up communication and interpretation burden for unclear comments.
- **Useful feedback potentially lost:** Retrieval may favor lexical similarity and omit a novel but better explanatory example.
- **Coverage:** Historical examples provide organizational context, but sparse or inconsistent review history limits coverage.
- **Human escalation:** Examples are explicitly non-prescriptive; developers still interpret the review and choose whether advice applies.
- **Cost:** TF-IDF/SVM and cosine retrieval are lightweight, but maintaining searchable review history and privacy controls adds operational work.
- **New failure modes:** Misleading analogies, cross-project convention transfer, stale examples, and explanation overconfidence.

## 8. Annotation and evaluator validity

- **Dataset:** 3,722 reviews from three projects and eight developers at an industrial partner.
- **Labeling:** Reviews are labeled on a four-point clarity scale; the extracted evidence does not report a formal inter-rater statistic.
- **Classifier evaluation:** Multiple embeddings/classifiers reduce dependence on one model choice.
- **Prototype evaluation:** One-fifth of the data (744 reviews) is held out for preliminary retrieval evaluation.
- **Limitations:** Small organizational sample, text-similarity retrieval, preliminary usefulness judgments, and no controlled developer task study.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Two research questions and EDRE objective are explicit. |
| Q2 | 2 | Industrial projects, reviewers, and 3,722-review corpus are described. |
| Q3 | 2 | Preprocessing, embeddings, classifiers, retrieval, and bot are detailed. |
| Q4 | 2 | Classification metrics and retrieval/usefulness evaluation are reported. |
| Q5 | 1 | Clarity labels are described, but annotation rubric/agreement is limited. |
| Q6 | 0 | No formal inter-rater agreement reported. |
| Q7 | 2 | Three embeddings and five classifiers are compared. |
| Q8 | 1 | Industrial setting, but three projects and one partner. |
| Q9 | 2 | Example-based explanation directly addresses ambiguity. |
| Q10 | 2 | Lightweight retrieval/classification design supports practical deployment. |
| Q11 | 1 | Retrieval limitations are discussed, but failure analysis is preliminary. |
| Q12 | 2 | Directly targets comprehensibility and actionability of review feedback. |

**Total: 19/24 — moderate-high confidence for explanation/classification evidence; limited proof of developer usefulness.**

## 10. Review-process reliability and bias

- **Label bias:** Four-point clarity judgments may reflect local communication norms and reviewer expectations.
- **Retrieval bias:** Cosine similarity and TF-IDF favor lexical overlap rather than issue equivalence or code-context compatibility.
- **Organizational bias:** Three projects and eight developers may not represent other teams, languages, or review cultures.
- **Usefulness uncertainty:** Preliminary top-five judgments do not establish improved comprehension, reduced communication, or better fixes.
- **Privacy/maintenance:** Historical reviews may contain sensitive project information and become stale as conventions change.
- **Missing outcomes:** No controlled user study, acceptance measure, review time, or downstream code-quality effect is reported.

## 11. Synthesis-ready conclusion

- P123 supports example-based explanation as a lightweight way to make ambiguous code-review comments more understandable.
- TF-IDF+SVM identifies reviews needing explanation well in the studied industrial corpus, while retrieval provides contextual analogies.
- The key trade-off is low-cost contextual support versus the risk that lexical similarity produces misleading or stale examples.
- Retrieved examples should remain non-prescriptive and be evaluated for developer comprehension and downstream action.
- Use as core evidence for explanation quality, context delivery, and actionability—not as evidence of autonomous review correctness.

