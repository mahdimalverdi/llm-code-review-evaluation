# P68 — CoTDeceptor: Adversarial Code Obfuscation Against LLM Code Agents

## Screening and proposal alignment

- **Decision:** Include as supporting
- **Group:** Supporting/Core
- **Relevance:** Medium–High
- **Citation key:** `p68_li2025_cotdeceptor`

## Proposal RQ mapping

- **RQ1:** Adds obfuscation-induced and supply-chain security failures.
- **RQ2:** Tests code representation and context sensitivity.
- **RQ3:** Evaluates CoT-enhanced agent detection.
- **RQ4:** Supports robustness versus obfuscation/defense cost trade-offs.
- **RQ5–RQ6:** Supports adversarial validity and specialized mitigation design.

## Synthesis-ready summary

P68 studies adversarial code obfuscation against CoT-enhanced LLM agents. It is relevant for robustness and evaluator-failure taxonomy, but its findings should remain in a security/adversarial sublayer.

**Provisional quality score: 17/24.** Verify benchmark, attack protocol, and defense evaluation.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p68_li2025_cotdeceptor`; Supporting; Include; Medium–High relevance.
- Study overview: Adversarial code obfuscation against chain-of-thought-enhanced LLM code agents.
- RQ1: Obfuscation-induced vulnerability misses and misleading reasoning (Reported).
- RQ2: Code representation, reasoning context, and supply-chain context (Reported).
- RQ3: CoT-agent security detection and robustness (Reported).
- RQ4: Robustness versus obfuscation/defense cost and false alarms (Reported).
- RQ5: Adversarial benchmark and evaluator validity (Reported).
- RQ6: Supports adversarial/security mitigation design.
- Failure taxonomy: obfuscation miss; hidden backdoor; reasoning deception; supply-chain context failure.
- Metrics: detection, attack success, robustness, and defense performance.
- Mitigation/trade-off: adversarial testing/defense; more robust checks add cost and may affect useful context.
- Validity: specialized security setting and transfer boundary.
- Quality: 17/24 provisional; supporting security evidence.
- Synthesis conclusion: use for robustness taxonomy, not general review-comment prevalence.

### 1. Identification
- P68; `p68_li2025_cotdeceptor`; local full PDF extracted and reviewed; authoritative record.
### 2. Screening and proposal alignment
- Include as supporting. `p68_li2025_cotdeceptor`; Supporting; Include; Medium–High relevance.
### 3. Study overview
Adversarial code obfuscation against chain-of-thought-enhanced LLM code agents.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Obfuscation-induced vulnerability misses and misleading reasoning (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Code representation, reasoning context, and supply-chain context (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | CoT-agent security detection and robustness (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Robustness versus obfuscation/defense cost and false alarms (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Adversarial benchmark and evaluator validity (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Supports adversarial/security mitigation design. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| obfuscation miss | Reported/Inferred | Full PDF |
| hidden backdoor | Reported/Inferred | Full PDF |
| reasoning deception | Reported/Inferred | Full PDF |
| supply-chain context failure. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| detection | Transfer/deployment limits remain | Full PDF |
| attack success | Transfer/deployment limits remain | Full PDF |
| robustness | Transfer/deployment limits remain | Full PDF |
| and defense performance. | Transfer/deployment limits remain | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: adversarial testing/defense; more robust checks add cost and may affect useful context.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: task-specific; retained useful-issue coverage is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- specialized security setting and transfer boundary.
- Q7–Q8 encode judging and reliability depth.
### 9. Quality appraisal
| Criterion | Score | Evidence note |
|---|---:|---|
| Q1 | 2 | goal at scored depth. |
| Q2 | 2 | artifact at scored depth. |
| Q3 | 2 | dataset/context at scored depth. |
| Q4 | 1 | procedure at scored depth. |
| Q5 | 2 | metrics at scored depth. |
| Q6 | 1 | failures at scored depth. |
| Q7 | 2 | judging at scored depth. |
| Q8 | 1 | reliability at scored depth. |
| Q9 | 0 | intervention at scored depth. |
| Q10 | 1 | trade-offs at scored depth. |
| Q11 | 1 | threats at scored depth. |
| Q12 | 2 | SLR support at scored depth. |
- Total: 17/24; calibrated reporting-quality score.
### 10. Review-process reliability and bias
- Missing preservation/escalation evidence, transfer limits, and selection/publication bias remain explicit; independent second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: Adversarial code obfuscation against chain-of-thought-enhanced LLM code agents.
- Boundary: use for robustness taxonomy, not general review-comment prevalence.
