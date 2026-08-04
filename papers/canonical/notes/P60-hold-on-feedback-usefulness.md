# P60 — Hold On! Is My Feedback Useful?

## Screening and proposal alignment

- **Decision:** Include
- **Group:** Core
- **Relevance:** High
- **Evidence basis:** Full local PDF, abstract and first-pass review
- **Citation key:** `p60_ahmed2025_feedback_useful`
- **Contribution:** Predictive evaluation of code-review-comment usefulness across open-source and commercial datasets.

## Proposal RQ mapping

- **RQ1:** Directly addresses useful versus non-useful comments.
- **RQ2:** Tests textual, jargon, voice, code, and domain features as context/quality signals.
- **RQ3:** Compares feature-based, bag-of-words, transfer-learning, and GPT-4o approaches.
- **RQ4:** Supports usefulness-prediction versus model/resource trade-offs.
- **RQ5:** Compares domains, projects, datasets, and feature validity.
- **RQ6:** Supports usefulness annotation and evaluation-schema design.

## Synthesis-ready summary

The study predicts code-review-comment usefulness using multiple datasets and feature/model families, reporting improved performance over baselines and strong results for GPT-4o and TF-IDF bag-of-words in the tested setting. Usefulness prediction is valuable for the SLR, but predicted usefulness is not identical to correctness, actionability, or acceptance.

## Legacy quality appraisal (superseded by the canonical record)

**Provisional score: 20/24.** Strong relevance to usefulness and dataset comparison; full-text extraction is needed for label construction, agreement, and cross-project validity.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p60_ahmed2025_feedback_useful`; Core; Include; High relevance.
- Study overview: Prediction of code-review-comment usefulness across open-source and commercial datasets using feature-based, TF-IDF, transfer-learning, and GPT-4o approaches.
- RQ1: Useful versus non-useful comments and usefulness-related failure categories (Reported).
- RQ2: Jargon, voice, code, domain, and textual features as usefulness signals (Reported).
- RQ3: Usefulness classification and cross-domain/model evaluation (Reported).
- RQ4: Prediction accuracy versus model/resource and annotation cost (Reported/Our perspective).
- RQ5: Dataset/domain/project differences and usefulness-label validity (Reported).
- RQ6: Strong usefulness annotation and evaluation-schema support.
- Failure taxonomy: non-useful; redundant; vague; non-constructive; domain-mismatched feedback.
- Metrics: usefulness classification performance, feature ablations, cross-dataset/model comparison.
- Mitigation/trade-off: usefulness prediction/prioritization; false classification may suppress useful feedback.
- Validity: usefulness is not correctness, actionability, or acceptance; label construction requires verification.
- Quality: 20/24 provisional; strong core usefulness evidence.
- Synthesis conclusion: usefulness must be measured separately and linked to preservation under filtering.

### 1. Identification
- P60; `p60_ahmed2025_feedback_useful`; local full PDF extracted and reviewed; authoritative record.
### 2. Screening and proposal alignment
- Include as Core. `p60_ahmed2025_feedback_useful`; Core; Include; High relevance.
### 3. Study overview
Prediction of code-review-comment usefulness across open-source and commercial datasets using feature-based, TF-IDF, transfer-learning, and GPT-4o approaches.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Useful versus non-useful comments and usefulness-related failure categories (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Jargon, voice, code, domain, and textual features as usefulness signals (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Usefulness classification and cross-domain/model evaluation (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Prediction accuracy versus model/resource and annotation cost (Reported/Our perspective). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Dataset/domain/project differences and usefulness-label validity (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Strong usefulness annotation and evaluation-schema support. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| non-useful | Reported/Inferred | Full PDF |
| redundant | Reported/Inferred | Full PDF |
| vague | Reported/Inferred | Full PDF |
| non-constructive | Reported/Inferred | Full PDF |
| domain-mismatched feedback. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| usefulness classification performance | Does not alone establish deployment value | Full PDF |
| feature ablations | Does not alone establish deployment value | Full PDF |
| cross-dataset/model comparison. | Does not alone establish deployment value | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: usefulness prediction/prioritization; false classification may suppress useful feedback.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: task-specific; retained useful-issue coverage is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- usefulness is not correctness, actionability, or acceptance; label construction requires verification.
- Q7–Q8 encode judging and reliability depth.
### 9. Quality appraisal
| Criterion | Score | Evidence note |
|---|---:|---|
| Q1 | 2 | goal at scored depth. |
| Q2 | 2 | artifact at scored depth. |
| Q3 | 2 | dataset/context at scored depth. |
| Q4 | 2 | procedure at scored depth. |
| Q5 | 2 | metrics at scored depth. |
| Q6 | 2 | failures at scored depth. |
| Q7 | 2 | judging at scored depth. |
| Q8 | 1 | reliability at scored depth. |
| Q9 | 1 | intervention at scored depth. |
| Q10 | 1 | trade-offs at scored depth. |
| Q11 | 1 | threats at scored depth. |
| Q12 | 2 | SLR support at scored depth. |
- Total: 20/24; calibrated reporting-quality score.
### 10. Review-process reliability and bias
- Missing preservation/escalation evidence and selection/publication bias remain explicit; independent second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: Prediction of code-review-comment usefulness across open-source and commercial datasets using feature-based, TF-IDF, transfer-learning, and GPT-4o approaches.
- Boundary: usefulness must be measured separately and linked to preservation under filtering.
