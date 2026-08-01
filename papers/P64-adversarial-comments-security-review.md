# P64 — Adversarial Comments and AI Security Reviewers

## Screening and proposal alignment

- **Decision:** Include as supporting
- **Group:** Supporting/Core
- **Relevance:** High
- **Citation key:** `p64_thornton2026_adversarial_comments`

## Proposal RQ mapping

- **RQ1:** Addresses adversarial, authority-spoofing, attention-dilution, and technical-deception comments.
- **RQ2:** Tests comment context as a possible attack surface.
- **RQ3:** Evaluates detection accuracy and automated defenses.
- **RQ4:** Directly measures adversarial robustness versus defense effects; comment stripping can remove helpful context.
- **RQ5:** Supports context-consistency and evaluator-validity analysis.
- **RQ6:** Supports adversarial testing and mitigation-family design.

## Synthesis-ready summary

The 100-sample, multi-language benchmark reports small non-significant effects from adversarial comments across tested models, while SAST cross-referencing improves detection and comment stripping can degrade weaker models by removing helpful context. This is strong evidence that a mitigation may create context-loss trade-offs.

**Provisional quality score: 21/24.** Verify paired analysis, benchmark construction, and defense evaluation details.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p64_thornton2026_adversarial_comments`; Supporting/Core; Include; High relevance.
- Study overview: 100-sample, three-language benchmark testing adversarial code comments against eight AI security reviewers and four defenses.
- RQ1: Authority spoofing, attention dilution, technical deception, and adversarial-comment failures (Reported).
- RQ2: Comment context as an attack surface; SAST evidence as verification context (Reported).
- RQ3: Security detection accuracy and defense evaluation (Reported).
- RQ4: Adversarial robustness versus defense effects; stripping comments can remove helpful context (Reported).
- RQ5: Paired benchmark validity and statistical testing (Reported).
- RQ6: Strong adversarial testing and mitigation support.
- Failure taxonomy: authority spoofing; attention dilution; technical deception; comment-based manipulation.
- Metrics: detection accuracy, McNemar tests, confidence intervals, attack effects, recovery, and SAST cross-reference.
- Mitigation/trade-off: comment stripping and SAST cross-reference; stripping can degrade weaker models, while static evidence improves detection.
- Validity: security benchmark and model-class differences limit generalization.
- Quality: 21/24 provisional; strong specialized evidence.
- Synthesis conclusion: mitigation can remove both attack and useful context; preservation must be measured.

### 1. Identification
- P64; `p64_thornton2026_adversarial_comments`; local full PDF extracted and reviewed; authoritative record.
### 2. Screening and proposal alignment
- Include as supporting. `p64_thornton2026_adversarial_comments`; Supporting/Core; Include; High relevance.
### 3. Study overview
100-sample, three-language benchmark testing adversarial code comments against eight AI security reviewers and four defenses.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Authority spoofing, attention dilution, technical deception, and adversarial-comment failures (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Comment context as an attack surface; SAST evidence as verification context (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Security detection accuracy and defense evaluation (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Adversarial robustness versus defense effects; stripping comments can remove helpful context (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Paired benchmark validity and statistical testing (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Strong adversarial testing and mitigation support. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| authority spoofing | Reported/Inferred | Full PDF |
| attention dilution | Reported/Inferred | Full PDF |
| technical deception | Reported/Inferred | Full PDF |
| comment-based manipulation. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| detection accuracy | Transfer/deployment limits remain | Full PDF |
| McNemar tests | Transfer/deployment limits remain | Full PDF |
| confidence intervals | Transfer/deployment limits remain | Full PDF |
| attack effects | Transfer/deployment limits remain | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: comment stripping and SAST cross-reference; stripping can degrade weaker models, while static evidence improves detection.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: task-specific; retained useful-issue coverage is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- security benchmark and model-class differences limit generalization.
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
- Contribution: 100-sample, three-language benchmark testing adversarial code comments against eight AI security reviewers and four defenses.
- Boundary: mitigation can remove both attack and useful context; preservation must be measured.
