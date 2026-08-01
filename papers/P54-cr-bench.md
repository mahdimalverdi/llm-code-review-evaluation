# P54 — CR-Bench: Evaluating the Real-World Utility of AI Code Review Agents

## Screening and proposal alignment

- **Decision:** Include
- **Group:** Core
- **Relevance:** High
- **Evidence basis:** Full local PDF, first-pass abstract and introduction review
- **Citation key:** `p54_pereira2026_crbench`
- **Contribution:** CR-Bench dataset and CR-Evaluator pipeline for granular evaluation of issue resolution versus spurious findings.

## Proposal RQ mapping

- **RQ1:** Spurious findings and low signal-to-noise outputs are reported.
- **RQ2:** Evaluates issue correctness and utility beyond coarse resolution metrics.
- **RQ3:** Introduces benchmark and fine-grained evaluator for code-review agents.
- **RQ4:** Directly studies issue resolution versus false/spurious findings.
- **RQ5:** Supports benchmark validity and granular annotation concerns.
- **RQ6:** Strong support for benchmark, evaluator, and trade-off framework design.

## Synthesis-ready summary

CR-Bench is directly relevant because it frames code-review-agent evaluation as a frontier between resolving real issues and generating spurious findings. Resolution rate alone can obscure signal-to-noise and developer productivity. The paper should be used for RQ4, while preserving the distinction between benchmark utility and production adoption.

## Legacy quality appraisal (superseded by the canonical record)

**Provisional score: 19/24.** Core evidence is strong for artifact, benchmark, issue coverage, and trade-offs; detailed annotation reliability, cost, and limitations require full-text extraction.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p54_pereira2026_crbench`; Core; Include; High relevance.
- Study overview: CR-Bench dataset and CR-Evaluator pipeline for real-world code-review agents.
- RQ1: Spurious findings and low signal-to-noise outputs (Reported).
- RQ2: Issue correctness, utility, and granular evaluator dimensions (Reported).
- RQ3: Benchmark and fine-grained evaluation pipeline (Reported).
- RQ4: Real issue resolution versus spurious findings, with a frontier between coverage and signal quality (Reported).
- RQ5: Benchmark construction and granular annotation validity (Reported/Our perspective).
- RQ6: Strong benchmark, evaluator, and trade-off support.
- Failure taxonomy: spurious finding; low-signal comment; hidden-issue miss; resolution-only measurement failure.
- Metrics: issue resolution, spurious-finding rate, signal-to-noise, and agent comparison.
- Mitigation/trade-off: CR-Evaluator and agent design; improving issue coverage can increase spurious findings.
- Validity: first-pass full-text extraction; detailed annotation/reliability requires final verification.
- Quality: 19/24 provisional; high-value core evidence pending protocol verification.
- Synthesis conclusion: resolution rate must be paired with spurious-finding and signal-to-noise measures.

### 1. Identification
- P54; `p54_pereira2026_crbench`; local full PDF extracted and reviewed; authoritative record.
### 2. Screening and proposal alignment
- Include as Core. `p54_pereira2026_crbench`; Core; Include; High relevance.
### 3. Study overview
CR-Bench dataset and CR-Evaluator pipeline for real-world code-review agents.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Spurious findings and low signal-to-noise outputs (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Issue correctness, utility, and granular evaluator dimensions (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Benchmark and fine-grained evaluation pipeline (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Real issue resolution versus spurious findings, with a frontier between coverage and signal quality (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Benchmark construction and granular annotation validity (Reported/Our perspective). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Strong benchmark, evaluator, and trade-off support. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| spurious finding | Reported/Inferred | Full PDF |
| low-signal comment | Reported/Inferred | Full PDF |
| hidden-issue miss | Reported/Inferred | Full PDF |
| resolution-only measurement failure. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| issue resolution | Does not alone establish deployment value | Full PDF |
| spurious-finding rate | Does not alone establish deployment value | Full PDF |
| signal-to-noise | Does not alone establish deployment value | Full PDF |
| and agent comparison. | Does not alone establish deployment value | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: CR-Evaluator and agent design; improving issue coverage can increase spurious findings.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: task-specific; retained useful-issue coverage is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- first-pass full-text extraction; detailed annotation/reliability requires final verification.
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
| Q7 | 1 | judging at scored depth. |
| Q8 | 1 | reliability at scored depth. |
| Q9 | 1 | intervention at scored depth. |
| Q10 | 1 | trade-offs at scored depth. |
| Q11 | 1 | threats at scored depth. |
| Q12 | 2 | SLR support at scored depth. |
- Total: 19/24; calibrated reporting-quality score.
### 10. Review-process reliability and bias
- Missing preservation/escalation evidence and selection/publication bias remain explicit; independent second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: CR-Bench dataset and CR-Evaluator pipeline for real-world code-review agents.
- Boundary: resolution rate must be paired with spurious-finding and signal-to-noise measures.
