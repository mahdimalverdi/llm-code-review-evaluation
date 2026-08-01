# P69 — Deep Assessment of Code Review Generation Approaches

## Screening and proposal alignment

- **Decision:** Include
- **Group:** Core
- **Relevance:** High
- **Citation key:** `p69_jiang2025_deep_assessment_crg`

## Proposal RQ mapping

- **RQ1:** Addresses inaccurate assessment caused by reference and lexical-metric limitations.
- **RQ2:** Evaluates semantic similarity and explicit quality criteria.
- **RQ3:** Proposes GradedReviews and semantic/LLM-based assessment.
- **RQ4:** Supports metric validity versus complexity/cost trade-offs.
- **RQ5:** Supports human scoring and benchmark validity.
- **RQ6:** Strong direct support for evaluation-framework design.

## Synthesis-ready summary

P69 introduces GradedReviews and compares lexical metrics with semantic vector similarity and ChatGPT-based scoring. The reported correlation with human scores improves from 0.22 to 0.47. This supports evaluation beyond BLEU, while correlation improvements should not be treated as proof of deployment usefulness.

**Provisional quality score: 21/24.** Verify manual-assessment protocol, agreement, and benchmark construction.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p69_jiang2025_deep_assessment_crg`; Core; Include; High relevance.
- Study overview: GradedReviews benchmark and semantic/LLM-based assessment beyond lexical similarity.
- RQ1: Reference mismatch and underestimation of semantically valid reviews (Reported).
- RQ2: Semantic similarity and explicit quality criteria (Reported).
- RQ3: Cosine semantic scoring and ChatGPT rubric scoring compared with BLEU-like metrics (Reported).
- RQ4: Metric validity and assessment complexity/cost (Reported/Our perspective).
- RQ5: Manual quality assessment and benchmark validity (Reported).
- RQ6: Strong direct evaluation-framework support.
- Failure taxonomy: lexical-metric false negative; reference mismatch; semantically valid but dissimilar review.
- Metrics: correlation with human scores, semantic vector cosine, LLM rubric score; reported improvement from 0.22 to 0.47.
- Mitigation/trade-off: semantic/LLM assessment; improves validity but adds model and annotation cost.
- Validity: human rubric and benchmark construction require verification.
- Quality: 21/24 provisional; high-value core evidence.
- Synthesis conclusion: supports semantic, rubric-based evaluation beyond lexical overlap.

### 1. Identification
- P69; `p69_jiang2025_deep_assessment_crg`; local full PDF extracted and reviewed; authoritative record.
### 2. Screening and proposal alignment
- Include as Core. `p69_jiang2025_deep_assessment_crg`; Core; Include; High relevance.
### 3. Study overview
GradedReviews benchmark and semantic/LLM-based assessment beyond lexical similarity.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Reference mismatch and underestimation of semantically valid reviews (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Semantic similarity and explicit quality criteria (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Cosine semantic scoring and ChatGPT rubric scoring compared with BLEU-like metrics (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Metric validity and assessment complexity/cost (Reported/Our perspective). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Manual quality assessment and benchmark validity (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Strong direct evaluation-framework support. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| lexical-metric false negative | Reported/Inferred | Full PDF |
| reference mismatch | Reported/Inferred | Full PDF |
| semantically valid but dissimilar review. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| correlation with human scores | Transfer/deployment limits remain | Full PDF |
| semantic vector cosine | Transfer/deployment limits remain | Full PDF |
| LLM rubric score | Transfer/deployment limits remain | Full PDF |
| reported improvement from 0.22 to 0.47. | Transfer/deployment limits remain | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: semantic/LLM assessment; improves validity but adds model and annotation cost.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: task-specific; retained useful-issue coverage is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- human rubric and benchmark construction require verification.
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
| Q9 | 2 | intervention at scored depth. |
| Q10 | 1 | trade-offs at scored depth. |
| Q11 | 1 | threats at scored depth. |
| Q12 | 2 | SLR support at scored depth. |
- Total: 21/24; calibrated reporting-quality score.
### 10. Review-process reliability and bias
- Missing preservation/escalation evidence, transfer limits, and selection/publication bias remain explicit; independent second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: GradedReviews benchmark and semantic/LLM-based assessment beyond lexical similarity.
- Boundary: supports semantic, rubric-based evaluation beyond lexical overlap.
