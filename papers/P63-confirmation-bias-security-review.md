# P63 — Measuring and Exploiting Confirmation Bias in LLM-Assisted Security Code Review

## Screening and proposal alignment

- **Decision:** Include as supporting
- **Group:** Supporting/Core
- **Relevance:** High
- **Citation key:** `p63_mitropoulos2026_confirmation_bias`

## Proposal RQ mapping

- **RQ1:** Supports security false positives, confirmation bias, and context-induced misjudgment.
- **RQ2:** Directly studies contextual bias in security review.
- **RQ3:** Adds bias, robustness, and security-review dimensions.
- **RQ4:** Supports correctness/robustness versus mitigation cost trade-offs.
- **RQ5:** Strong evaluator-validity and context-consistency evidence.
- **RQ6:** Supports bias-audit and specialized security sublayer design.

## Synthesis-ready summary

P63 is relevant for evaluator and security-review failure modes, especially confirmation bias. Its results should remain in a specialized security/evaluator layer rather than being generalized to all code-review comments.

**Provisional quality score: 18/24.** Verify benchmark, attack construction, and reliability measures.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p63_mitropoulos2026_confirmation_bias`; Supporting/Core; Include; High relevance.
- Study overview: Measurement and exploitation of confirmation/contextual bias in LLM-assisted security code review.
- RQ1: Confirmation bias, security false positives/negatives, and context-induced misjudgment (Reported).
- RQ2: Security context and contextual bias (Reported).
- RQ3: Bias, robustness, and security-review evaluation dimensions (Reported).
- RQ4: Detection reliability versus adversarial/contextual bias and defense cost (Reported).
- RQ5: Strong evaluator-validity and annotation concerns.
- RQ6: Supports bias-audit and specialized security sublayer design.
- Failure taxonomy: confirmation bias; contextual bias; false positive; false negative; security misjudgment.
- Metrics: bias effect, detection performance, robustness, and attack/defense outcomes.
- Mitigation/trade-off: bias measurement/exploitation and defenses; robustness adds evaluation cost.
- Validity: security-specific setting and benchmark construction require verification.
- Quality: 18/24 provisional; specialized supporting evidence.
- Synthesis conclusion: evaluator/context bias must be explicit in security review evaluation.

### 1. Identification
- P63; `p63_mitropoulos2026_confirmation_bias`; local full PDF extracted and reviewed; authoritative record.
### 2. Screening and proposal alignment
- Include as supporting. `p63_mitropoulos2026_confirmation_bias`; Supporting/Core; Include; High relevance.
### 3. Study overview
Measurement and exploitation of confirmation/contextual bias in LLM-assisted security code review.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Confirmation bias, security false positives/negatives, and context-induced misjudgment (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Security context and contextual bias (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Bias, robustness, and security-review evaluation dimensions (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Detection reliability versus adversarial/contextual bias and defense cost (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Strong evaluator-validity and annotation concerns. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Supports bias-audit and specialized security sublayer design. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| confirmation bias | Reported/Inferred | Full PDF |
| contextual bias | Reported/Inferred | Full PDF |
| false positive | Reported/Inferred | Full PDF |
| false negative | Reported/Inferred | Full PDF |
| security misjudgment. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| bias effect | Transfer/deployment limits remain | Full PDF |
| detection performance | Transfer/deployment limits remain | Full PDF |
| robustness | Transfer/deployment limits remain | Full PDF |
| and attack/defense outcomes. | Transfer/deployment limits remain | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: bias measurement/exploitation and defenses; robustness adds evaluation cost.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: task-specific; retained useful-issue coverage is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- security-specific setting and benchmark construction require verification.
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
| Q12 | 1 | SLR support at scored depth. |
- Total: 18/24; calibrated reporting-quality score.
### 10. Review-process reliability and bias
- Missing preservation/escalation evidence, transfer limits, and selection/publication bias remain explicit; independent second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: Measurement and exploitation of confirmation/contextual bias in LLM-assisted security code review.
- Boundary: evaluator/context bias must be explicit in security review evaluation.
