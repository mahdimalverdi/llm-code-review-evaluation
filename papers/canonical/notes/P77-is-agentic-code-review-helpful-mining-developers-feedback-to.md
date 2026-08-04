# P77 — Is Agentic Code Review Helpful? Mining Developers' Feedback to CodeRabbit Reviews in the Wild

## 1. Identification

- Project ID: `P77` (provisional)
- Citation key: `p77_lin2026_is_agentic_code_review_helpful`
- Full reference: Hong Yi Lin; Mingzhao Liang; Patanamon Thongtanunam; Kla Tantithamthavorn. “Is Agentic Code Review Helpful? Mining Developers' Feedback to CodeRabbit Reviews in the Wild.” arXiv:2607.03316v2, 2026.
- DOI/URL: `https://arxiv.org/abs/2607.03316v2`
- Review date: 2026-08-04
- Source/database: arXiv full-text screening
- Selection stage: included for reconciliation; canonical corpus integration pending
- Duplicate or companion publication: Publisher metadata remains provisional.

## 2. Screening

- Decision: `Include`
- Relevance: `High`
- Decision rationale: Large-scale empirical study of real CodeRabbit comments and subsequent developer feedback, including rejection reasons and an early quality-gate model.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: taxonomy / annotation protocol / mitigation design / trade-off framework
- Exact inclusion criterion: Core inclusion: real-world AI review usefulness and problematic-comment evaluation.

## 3. Study overview

- Purpose: Measure whether agentic reviews help developers in practice and identify causes of rejection.
- Research questions: RQ1 developer feedback; RQ2 relationship between concern types and feedback; RQ3 prediction of developer feedback.
- Method: Mining 31,073 CodeRabbit review–feedback pairs, manual open coding of a stratified 10% sample, LLM annotation of the remainder, and rejection prediction with prompted/fine-tuned models.
- Evaluated system/artifact: CodeRabbit agentic inline review comments on GitHub pull requests.
- Dataset/benchmark: 10,191 PRs across 239 repositories and ten languages; 31,073 initial CodeRabbit reviews with developer replies.
- Input context: CodeRabbit inline review, code diff, PR context, and subsequent human feedback. The study selects the initial review in each discussion thread.
- Main findings: 36.4% accepted, 7.3% triggered discussion, and 56.3% rejected. Rejections involve invalid false positives, redundant/out-of-scope suggestions, and misalignment with developer intent or coding practices; prediction reaches up to 76% F1.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Accepted reviews lead to code changes/issues; discussion indicates possible usefulness requiring confirmation; rejected reviews are non-helpful or misaligned. | Reported | Sections 1, 4 |
| RQ2 | Functional concerns form 43.3% of reviews and have 35.8% invalid rejection; evolvability concerns are often rejected for coding-practice misalignment (31.6%). | Reported | Sections 1, 4–5 |
| RQ3 | Lightweight learning-based methods predict rejection with up to 76% F1; fine-tuned models reach up to 68%. | Reported | Sections 1, 5 |
| RQ4 | The study exposes a usefulness–noise trade-off: CodeRabbit feedback is actionable in a minority of cases and imposes validation overhead when rejected. | Inferred | Sections 1, 4–6 |
| RQ5 | Developer replies are used as real-world outcome evidence, with manual labels and LLM annotation validated against a sample. | Reported | Section 3 |
| RQ6 | Directly supports a feedback-grounded quality gate for agentic review. | Inferred | Sections 5–6 |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Invalid suggestion | False-positive issue or technically incorrect review. | Reported taxonomy | Sections 1, 3–4 |
| Redundant suggestion | Suggestion already implemented or otherwise unnecessary. | Reported taxonomy | Sections 1, 3–4 |
| Out of scope | Recommendation beyond the PR objective. | Reported taxonomy | Section 3 |
| Developer preference/practice misalignment | Suggestion conflicts with intended design or local coding practices. | Reported taxonomy | Sections 1, 3–4 |
| Insufficient context | Feedback requires further discussion or confirmation before action. | Reported category | Section 4 |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Practical usefulness | Accepted suggestion, triggered discussion, or rejected suggestion based on developer reply. | 36.4% / 7.3% / 56.3%. | Section 4, Table 2 |
| Concern distribution | Functional vs. evolvability concern type and rejection reason. | Functional concerns 43.3%; 35.8% invalid rejection. | Sections 4–5 |
| Quality-gate prediction | F1 for early rejection prediction. | Up to 76% for lightweight learning-based methods. | Section 5 |
| Annotation reliability | Manual labels compared with LLM labels using Cohen’s kappa. | κ=0.74, substantial agreement. | Section 3 |
| Temporal trend | Monthly feedback distribution. | Accepted reviews increase over time; reported increase 12.5% since release. | Section 4 |

## 7. Mitigation and trade-offs

- Mitigation family: Early rejection prediction as a quality gate before developer exposure.
- Intervention point: After CodeRabbit generates a review and before it reaches/engages the developer.
- What it reduces: Likely rejected, invalid, redundant, or misaligned comments and associated validation burden.
- Useful feedback potentially lost: False negatives could suppress useful comments; this trade-off is not evaluated operationally.
- Coverage effect: Prediction concerns acceptance/rejection, not defect recall or issue coverage.
- Human escalation effect: Discussion is treated as a separate outcome, but escalation workflow is not measured.
- Computational/operational cost: Lightweight models are proposed to reduce workflow overhead; training/inference cost is not reported.
- New failure modes: A learned gate may reproduce annotation bias, miss rare useful comments, or treat preference-based rejection as technical invalidity.

## 8. Annotation and evaluator validity

- Judge/annotator: Two authors manually analyze a stratified 10% sample; LLM labels the remaining 30,776 reviews.
- Rubric: Three feedback classes (accepted, triggered discussion, rejected) and rejection-reason categories including intended design, preference, invalid, redundant, and out of scope.
- Agreement/reliability: LLM vs. manual labels achieve Cohen’s κ=0.74; the manual coding process includes disagreement review.
- Validity checks: Stratified sampling across repositories/languages, open coding, second-author review, manually derived labels, and agreement check before scaling annotation.
- Possible bias: Reply visibility, explicitness of developer feedback, CodeRabbit-only case study, and LLM annotation may bias observed helpfulness.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Tool, task, and real-world feedback target are explicit. |
| Q2 | 2 | 31,073 pairs from 10,191 PRs and 239 repositories are reported. |
| Q3 | 2 | Sampling, manual coding, and predictive model setups are described. |
| Q4 | 2 | Outcome categories, rejection taxonomy, trends, and F1 are explicit. |
| Q5 | 2 | Developer-feedback rubric and concern categories are specified. |
| Q6 | 2 | Cohen’s kappa is reported for scaled LLM annotation. |
| Q7 | 2 | Open coding, second-author review, and stratified sampling are described. |
| Q8 | 1 | Agreement check supports validity, but only one tool and reply-visible cases are studied. |
| Q9 | 2 | Rejection-prediction quality gate is explicit. |
| Q10 | 1 | Lightweight models are motivated, but cost is not quantified. |
| Q11 | 2 | Tool, feedback, annotation, and generalizability limitations are discussed. |
| Q12 | 2 | Direct real-world evidence of usefulness and problematic feedback. |

- Total: `22/24` provisional
- Quality interpretation: Strong ecological evidence for acceptance/rejection and failure categories, with tool-specific and reply-selection limitations.

## 10. Review-process reliability and bias

- Missing data: Human time, downstream code quality, defect recall, false-negative gate effects, and model cost are not evaluated.
- Publication-bias concern: Not assessed; only reviews receiving developer replies are included.
- Selection uncertainty: Included by full-text screening; publisher metadata should be reconciled.
- Extraction uncertainty: Moderate due to LLM annotation of most instances and observational feedback labels.
- Second-reviewer agreement: Manual/LLM agreement reported; independent SLR reviewer agreement not available.
- Duplicate-publication handling: Pending final-version reconciliation.

## 11. Synthesis-ready conclusion

- Contribution to the SLR: Provides large-scale real-world evidence that most observed CodeRabbit comments are rejected and identifies actionable failure categories.
- What the paper does not establish: It does not establish causal helpfulness, comment correctness independent of replies, comprehensive coverage, or safe suppression by a quality gate.
- Research gap supported: Agentic review evaluation should incorporate developer responses and rejection reasons, not only offline comment similarity.
- Candidate synthesis claims: Developer feedback reveals substantial noise from false positives, redundancy, scope mismatch, and practice misalignment; lightweight rejection prediction is promising but must account for suppressing useful feedback.
- Follow-up verification needed: Reconcile metadata and inspect released data/code if available, especially label definitions and temporal-trend calculation.
