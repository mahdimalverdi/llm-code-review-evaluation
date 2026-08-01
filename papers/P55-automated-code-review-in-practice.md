# P55 — Automated Code Review in Practice

## Screening and proposal alignment

- **Decision:** Include
- **Group:** Core
- **Relevance:** High
- **Evidence basis:** Full local PDF, abstract and first-pass review
- **Citation key:** `p55_cihan2025_acr_practice`
- **Contribution:** Industrial evaluation of an LLM-based automated-review tool across 4,335 pull requests and 238 practitioners.

## Proposal RQ mapping

- **RQ1:** Reports faulty reviews, unnecessary corrections, and irrelevant comments.
- **RQ2:** Provides industrial context and practitioner-perceived quality evidence.
- **RQ3:** Uses resolution, PR closure duration, surveys, and perceived code-quality improvement.
- **RQ4:** Shows usefulness/resolution versus longer PR closure time and correction burden.
- **RQ5:** Supports ecological validity and practitioner-annotation considerations.
- **RQ6:** Strong support for workflow-aware and cost/burden dimensions.

## Synthesis-ready summary

The study reports that 73.8% of automated comments were labeled resolved, while average PR closure duration increased from 5h52m to 8h20m. It also reports faulty, unnecessary, and irrelevant comments. The results support treating resolution and perceived usefulness separately from workflow cost and delay; resolution should not be interpreted as unqualified benefit.

## Legacy quality appraisal (superseded by the canonical record)

**Provisional score: 21/24.** Strong industrial and workflow evidence; detailed sampling, confounding controls, and annotation reliability require full-text extraction.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p55_cihan2025_acr_practice`; Core; Include; High relevance.
- Study overview: Industrial study of an LLM-based automated review tool across 4,335 PRs, 238 practitioners, and ten projects.
- RQ1: Faulty reviews, unnecessary corrections, and irrelevant comments (Reported).
- RQ2: Industrial PR context and practitioner experience (Reported).
- RQ3: Resolution, PR closure duration, surveys, and perceived quality (Reported).
- RQ4: 73.8% resolved comments versus increased average PR closure duration; usefulness versus delay/burden (Reported).
- RQ5: Industrial sampling, survey, and practitioner validity (Reported/Our perspective).
- RQ6: Strong workflow and cost/burden support.
- Failure taxonomy: faulty; unnecessary; irrelevant; low-value; correction-inducing comment.
- Metrics: resolution labels, PR closure time, survey perceptions, and code-quality awareness.
- Mitigation/trade-off: deployed automated review; resolution gains may coexist with longer closure and correction burden.
- Validity: project confounding and survey response bias require verification.
- Quality: 21/24 provisional; strong industrial evidence.
- Synthesis conclusion: operational benefit must be evaluated jointly with time and correction costs.

### 1. Identification
- P55; `p55_cihan2025_acr_practice`; local full PDF extracted and reviewed; authoritative record.
### 2. Screening and proposal alignment
- Include as Core. `p55_cihan2025_acr_practice`; Core; Include; High relevance.
### 3. Study overview
Industrial study of an LLM-based automated review tool across 4,335 PRs, 238 practitioners, and ten projects.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Faulty reviews, unnecessary corrections, and irrelevant comments (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Industrial PR context and practitioner experience (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Resolution, PR closure duration, surveys, and perceived quality (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | 73.8% resolved comments versus increased average PR closure duration; usefulness versus delay/burden (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Industrial sampling, survey, and practitioner validity (Reported/Our perspective). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Strong workflow and cost/burden support. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| faulty | Reported/Inferred | Full PDF |
| unnecessary | Reported/Inferred | Full PDF |
| irrelevant | Reported/Inferred | Full PDF |
| low-value | Reported/Inferred | Full PDF |
| correction-inducing comment. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| resolution labels | Does not alone establish deployment value | Full PDF |
| PR closure time | Does not alone establish deployment value | Full PDF |
| survey perceptions | Does not alone establish deployment value | Full PDF |
| and code-quality awareness. | Does not alone establish deployment value | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: deployed automated review; resolution gains may coexist with longer closure and correction burden.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: task-specific; retained useful-issue coverage is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- project confounding and survey response bias require verification.
- Q7–Q8 encode judging and reliability depth.
### 9. Quality appraisal
| Criterion | Score | Evidence note |
|---|---:|---|
| Q1 | 2 | goal at scored depth. |
| Q2 | 2 | artifact at scored depth. |
| Q3 | 2 | dataset/context at scored depth. |
| Q4 | 2 | procedure at scored depth. |
| Q5 | 2 | metrics at scored depth. |
| Q6 | 1 | failures at scored depth. |
| Q7 | 1 | judging at scored depth. |
| Q8 | 1 | reliability at scored depth. |
| Q9 | 2 | intervention at scored depth. |
| Q10 | 2 | trade-offs at scored depth. |
| Q11 | 1 | threats at scored depth. |
| Q12 | 2 | SLR support at scored depth. |
- Total: 20/24; calibrated reporting-quality score.
### 10. Review-process reliability and bias
- Missing preservation/escalation evidence and selection/publication bias remain explicit; independent second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: Industrial study of an LLM-based automated review tool across 4,335 PRs, 238 practitioners, and ten projects.
- Boundary: operational benefit must be evaluated jointly with time and correction costs.
