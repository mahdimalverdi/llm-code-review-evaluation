# P65 — QASecClaw: Multi-Agent False-Positive Reduction in SAST

## Screening and proposal alignment

- **Decision:** Include as supporting
- **Group:** Supporting/Core
- **Relevance:** High
- **Citation key:** `p65_ameen2026_qasecclaw`

## Proposal RQ mapping

- **RQ1:** Focuses on false-positive security findings.
- **RQ2:** Uses source-code context and validation evidence.
- **RQ3:** Evaluates multi-agent filtering and security validation.
- **RQ4:** Directly addresses false-positive reduction versus agent complexity and cost.
- **RQ5:** Supports annotation and security-grounding validity.
- **RQ6:** Supports hybrid static-analysis/LLM mitigation design.

## Synthesis-ready summary

QASecClaw combines SAST findings with specialized LLM agents, testing, and validation to reduce false positives. It is useful as a specialized hybrid-mitigation case, but its security-warning setting should not be generalized to ordinary review comments.

**Provisional quality score: 19/24.** Verify datasets, baselines, and cost/latency reporting.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p65_ameen2026_qasecclaw`; Supporting/Core; Include; High relevance.
- Study overview: Multi-agent LLM approach for reducing SAST false positives using source context, testing, and validation.
- RQ1: False-positive security warnings and hidden true vulnerabilities (Reported).
- RQ2: Source-code context, SAST evidence, tests, and security validation (Reported).
- RQ3: Multi-agent filtering and security-review dimensions (Reported).
- RQ4: False-positive reduction versus agent complexity, latency, and cost (Reported/Our perspective).
- RQ5: Security-label and validation reliability (Reported/Our perspective).
- RQ6: Strong hybrid mitigation support.
- Failure taxonomy: false positive; ignored true positive; insufficient evidence; validation failure.
- Metrics: false-positive reduction, detection/validation performance, and agent comparison.
- Mitigation/trade-off: SAST plus LLM filter/test/validation agents; more agents add cost and latency.
- Validity: security-warning setting and baseline/tool choices require verification.
- Quality: 19/24 provisional; specialized core-supporting evidence.
- Synthesis conclusion: supports hybrid verification and false-positive-cost analysis.

### 1. Identification
- P65; `p65_ameen2026_qasecclaw`; local full PDF extracted and reviewed; authoritative record.
### 2. Screening and proposal alignment
- Include as supporting. `p65_ameen2026_qasecclaw`; Supporting/Core; Include; High relevance.
### 3. Study overview
Multi-agent LLM approach for reducing SAST false positives using source context, testing, and validation.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | False-positive security warnings and hidden true vulnerabilities (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Source-code context, SAST evidence, tests, and security validation (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Multi-agent filtering and security-review dimensions (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | False-positive reduction versus agent complexity, latency, and cost (Reported/Our perspective). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Security-label and validation reliability (Reported/Our perspective). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Strong hybrid mitigation support. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| false positive | Reported/Inferred | Full PDF |
| ignored true positive | Reported/Inferred | Full PDF |
| insufficient evidence | Reported/Inferred | Full PDF |
| validation failure. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| false-positive reduction | Transfer/deployment limits remain | Full PDF |
| detection/validation performance | Transfer/deployment limits remain | Full PDF |
| and agent comparison. | Transfer/deployment limits remain | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: SAST plus LLM filter/test/validation agents; more agents add cost and latency.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: task-specific; retained useful-issue coverage is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- security-warning setting and baseline/tool choices require verification.
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
| Q9 | 2 | intervention at scored depth. |
| Q10 | 1 | trade-offs at scored depth. |
| Q11 | 1 | threats at scored depth. |
| Q12 | 1 | SLR support at scored depth. |
- Total: 19/24; calibrated reporting-quality score.
### 10. Review-process reliability and bias
- Missing preservation/escalation evidence, transfer limits, and selection/publication bias remain explicit; independent second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: Multi-agent LLM approach for reducing SAST false positives using source context, testing, and validation.
- Boundary: supports hybrid verification and false-positive-cost analysis.
