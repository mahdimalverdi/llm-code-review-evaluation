# P67 — Trust Me, I Know This Function: Familiar Pattern Attacks

## Screening and proposal alignment

- **Decision:** Include as supporting
- **Group:** Supporting/Core
- **Relevance:** Medium–High
- **Citation key:** `p67_bernstein2025_trust_me_function`

## Proposal RQ mapping

- **RQ1:** Adds abstraction-bias and missed-small-bug failure categories.
- **RQ2:** Shows code context can induce misleading familiar-pattern interpretations.
- **RQ3:** Evaluates vulnerability detection across models/languages.
- **RQ4:** Supports adversarial robustness and defense-cost trade-offs.
- **RQ5:** Strong context-validity and evaluator-robustness evidence.
- **RQ6:** Supports adversarial and security sublayer design.

## Synthesis-ready summary

The paper introduces Familiar Pattern Attacks that exploit abstraction bias in LLM static analysis and cause models to overlook small meaningful bugs. It supports robustness testing, but remains a security/static-analysis study rather than general review-comment evaluation.

**Provisional quality score: 18/24.** Verify attack success, transferability, and defense results.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p67_bernstein2025_trust_me_function`; Supporting; Include; Medium–High relevance.
- Study overview: Familiar Pattern Attack hijacks LLM static analysis through abstraction bias and minimal code edits.
- RQ1: Missed small bugs and familiar-pattern misclassification (Reported).
- RQ2: Code representation and semantic context bias (Reported).
- RQ3: Security detection, transferability, and adversarial robustness (Reported).
- RQ4: Detection robustness versus attack/defense cost (Reported).
- RQ5: Security evaluator validity and adversarial testing (Reported).
- RQ6: Supports security/adversarial sublayer design.
- Failure taxonomy: abstraction bias; familiar-pattern miss; hijacked interpretation; small-bug omission.
- Metrics: attack success, detection degradation, transferability, language/model robustness.
- Mitigation/trade-off: warnings/defenses and adversarial testing; robustness increases evaluation complexity.
- Validity: static-analysis/security setting limits generalization.
- Quality: 18/24 provisional; specialized supporting evidence.
- Synthesis conclusion: adversarial robustness is a distinct evaluator/context dimension.

### 1. Identification
- P67; `p67_bernstein2025_trust_me_function`; local full PDF extracted and reviewed; authoritative record.
### 2. Screening and proposal alignment
- Include as supporting. `p67_bernstein2025_trust_me_function`; Supporting; Include; Medium–High relevance.
### 3. Study overview
Familiar Pattern Attack hijacks LLM static analysis through abstraction bias and minimal code edits.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Missed small bugs and familiar-pattern misclassification (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Code representation and semantic context bias (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Security detection, transferability, and adversarial robustness (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Detection robustness versus attack/defense cost (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Security evaluator validity and adversarial testing (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Supports security/adversarial sublayer design. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| abstraction bias | Reported/Inferred | Full PDF |
| familiar-pattern miss | Reported/Inferred | Full PDF |
| hijacked interpretation | Reported/Inferred | Full PDF |
| small-bug omission. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| attack success | Transfer/deployment limits remain | Full PDF |
| detection degradation | Transfer/deployment limits remain | Full PDF |
| transferability | Transfer/deployment limits remain | Full PDF |
| language/model robustness. | Transfer/deployment limits remain | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: warnings/defenses and adversarial testing; robustness increases evaluation complexity.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: task-specific; retained useful-issue coverage is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- static-analysis/security setting limits generalization.
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
- Contribution: Familiar Pattern Attack hijacks LLM static analysis through abstraction bias and minimal code edits.
- Boundary: adversarial robustness is a distinct evaluator/context dimension.
