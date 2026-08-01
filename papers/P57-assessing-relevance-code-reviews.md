# P57 — On Assessing the Relevance of Code Reviews Authored by Generative Models

## Screening and proposal alignment

- **Decision:** Include
- **Group:** Core
- **Relevance:** High
- **Evidence basis:** Full local PDF, abstract and first-pass review
- **Citation key:** `p57_heumuller2025_relevance_reviews`
- **Contribution:** Multi-subjective ranking of 280 self-contained CodeReview StackExchange requests and ChatGPT comments against human responses.

## Proposal RQ mapping

- **RQ1:** Challenges single-ground-truth assumptions and subjective usefulness ambiguity.
- **RQ2:** Treats relevance as a distinct evaluation dimension.
- **RQ3:** Proposes multi-subjective ranking beyond lexical matching.
- **RQ4:** Supports evaluator-validity and unchecked-integration risk analysis.
- **RQ5:** Directly addresses ground-truth and judge-validity concerns.
- **RQ6:** Supports annotation and evaluation-framework design.

## Synthesis-ready summary

The study argues that one human response is an inadequate exclusive ground truth because multiple valid review comments may exist. Its multi-subjective ranking places ChatGPT comments above sampled human responses in the reported setting, but this result should be interpreted cautiously because relevance ranking is not equivalent to factual correctness or production usefulness.

## Legacy quality appraisal (superseded by the canonical record)

**Provisional score: 20/24.** Strong evaluation-method contribution; judge protocol, inter-rater reliability, and external validity require full-text extraction.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p57_heumuller2025_relevance_reviews`; Core; Include; High relevance.
- Study overview: Multi-subjective ranking of 280 code-review requests and generated/human comments.
- RQ1: Ground-truth ambiguity and potentially irrelevant or unsafe comments (Reported/Our perspective).
- RQ2: Relevance and multi-subjective quality judgment (Reported).
- RQ3: Ranking beyond single-reference lexical similarity (Reported).
- RQ4: Evaluator validity versus ranking cost and unchecked integration risk (Reported).
- RQ5: Direct ground-truth and judge-validity support.
- RQ6: Strong annotation and evaluation-framework support.
- Failure taxonomy: irrelevant; unsafe; ground-truth mismatch; single-reference evaluation failure.
- Metrics: multi-subjective ranking and human-judge comparison.
- Mitigation/trade-off: multi-judge ranking; improves validity but adds annotation cost and does not prove correctness.
- Validity: StackExchange/self-contained tasks differ from PR workflows.
- Quality: 20/24 provisional; strong core evaluation evidence.
- Synthesis conclusion: single ground truth should not be treated as exclusive correctness.

### 1. Identification
- P57; `p57_heumuller2025_relevance_reviews`; local full PDF extracted and reviewed; authoritative record.
### 2. Screening and proposal alignment
- Include as Core. `p57_heumuller2025_relevance_reviews`; Core; Include; High relevance.
### 3. Study overview
Multi-subjective ranking of 280 code-review requests and generated/human comments.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Ground-truth ambiguity and potentially irrelevant or unsafe comments (Reported/Our perspective). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Relevance and multi-subjective quality judgment (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Ranking beyond single-reference lexical similarity (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Evaluator validity versus ranking cost and unchecked integration risk (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Direct ground-truth and judge-validity support. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Strong annotation and evaluation-framework support. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| irrelevant | Reported/Inferred | Full PDF |
| unsafe | Reported/Inferred | Full PDF |
| ground-truth mismatch | Reported/Inferred | Full PDF |
| single-reference evaluation failure. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| multi-subjective ranking and human-judge comparison. | Does not alone establish deployment value | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: multi-judge ranking; improves validity but adds annotation cost and does not prove correctness.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: task-specific; retained useful-issue coverage is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- StackExchange/self-contained tasks differ from PR workflows.
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
- Contribution: Multi-subjective ranking of 280 code-review requests and generated/human comments.
- Boundary: single ground truth should not be treated as exclusive correctness.
