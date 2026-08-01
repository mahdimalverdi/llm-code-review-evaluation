# P62 — DeputyDev: AI-Powered Developer Assistant

## Screening and proposal alignment

- **Decision:** Include
- **Group:** Core
- **Relevance:** High
- **Method:** Double-controlled A/B experiment with more than 200 engineers; telemetry-based PR review-time evaluation.
- **Citation key:** `p62_khare2025_deputydev`

## Proposal RQ mapping

- **RQ1:** Addresses inconsistent and low-quality review feedback.
- **RQ2:** Contextual AI is central to review generation.
- **RQ3:** Uses per-PR and per-line review duration and productivity outcomes.
- **RQ4:** Directly measures automation versus review-time and productivity trade-offs.
- **RQ5:** Provides organizational telemetry and contextual validity evidence.
- **RQ6:** Supports production evaluation and workflow-cost design.

## Synthesis-ready summary

DeputyDev reports substantial baseline PR delays at TATA 1mg and a statistically significant reduction in review times after deployment of contextual AI review, with safeguards for outliers. It is strong workflow evidence, but time reduction does not establish correctness or useful-feedback preservation.

**Provisional quality score: 21/24.** Verify exact effect sizes, study design, and confounder handling from the full PDF.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p62_khare2025_deputydev`; Core; Include; High relevance.
- Study overview: Contextual AI review assistant evaluated with telemetry and a double-controlled A/B experiment involving more than 200 engineers.
- RQ1: Inconsistent, low-quality, and delayed review feedback (Reported/Our perspective).
- RQ2: Contextual PR information and organizational workflow (Reported).
- RQ3: Per-PR and per-line review duration, productivity, and rollout outcomes (Reported).
- RQ4: Review-time reduction versus deployment, outliers, trust, and productivity effects (Reported).
- RQ5: Industrial telemetry, experiment validity, and confounding (Reported/Our perspective).
- RQ6: Strong production and operational-cost support.
- Failure taxonomy: inconsistent; delayed; low-quality; context-insufficient feedback.
- Metrics: review duration per PR/line, PR cycle, statistical A/B effects, rollout telemetry.
- Mitigation/trade-off: contextual automation with safeguards; faster review may not imply better review quality.
- Validity: exact experimental controls/confounders require full-text verification.
- Quality: 21/24 provisional; strong workflow evidence.
- Synthesis conclusion: operational cost and time should be measured alongside quality and coverage.

### 1. Identification
- P62; `p62_khare2025_deputydev`; local full PDF extracted and reviewed; authoritative record.
### 2. Screening and proposal alignment
- Include as Core. `p62_khare2025_deputydev`; Core; Include; High relevance.
### 3. Study overview
Contextual AI review assistant evaluated with telemetry and a double-controlled A/B experiment involving more than 200 engineers.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Inconsistent, low-quality, and delayed review feedback (Reported/Our perspective). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Contextual PR information and organizational workflow (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Per-PR and per-line review duration, productivity, and rollout outcomes (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Review-time reduction versus deployment, outliers, trust, and productivity effects (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Industrial telemetry, experiment validity, and confounding (Reported/Our perspective). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Strong production and operational-cost support. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| inconsistent | Reported/Inferred | Full PDF |
| delayed | Reported/Inferred | Full PDF |
| low-quality | Reported/Inferred | Full PDF |
| context-insufficient feedback. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| review duration per PR/line | Transfer/deployment limits remain | Full PDF |
| PR cycle | Transfer/deployment limits remain | Full PDF |
| statistical A/B effects | Transfer/deployment limits remain | Full PDF |
| rollout telemetry. | Transfer/deployment limits remain | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: contextual automation with safeguards; faster review may not imply better review quality.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: task-specific; retained useful-issue coverage is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- exact experimental controls/confounders require full-text verification.
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
- Contribution: Contextual AI review assistant evaluated with telemetry and a double-controlled A/B experiment involving more than 200 engineers.
- Boundary: operational cost and time should be measured alongside quality and coverage.
