# P58 — Are LLMs Reliable Code Reviewers? Systematic Overcorrection

## Screening and proposal alignment

- **Decision:** Include
- **Group:** Core
- **Relevance:** High
- **Evidence basis:** Full local PDF, abstract and first-pass review
- **Citation key:** `p58_jin2026_reliable_code_reviewers`
- **Contribution:** Evidence of overcorrection in requirement-conformance judgments and a fix-guided verification filter.

## Proposal RQ mapping

- **RQ1:** False defect and overcorrection comments are central failure types.
- **RQ2:** Studies requirement/code context and rationale-required judgments.
- **RQ3:** Evaluates prompts, explanations, proposed fixes, and verification.
- **RQ4:** Directly studies prompt detail versus misjudgment and verification cost/benefit.
- **RQ5:** Supports context consistency and evaluator-validity analysis.
- **RQ6:** Strong support for verification-gate design.

## Synthesis-ready summary

More detailed prompts requiring explanations and corrections can increase misjudgment, including classifying correct implementations as non-compliant. The proposed fix-guided verification filter uses executable tests and specification-constrained tests as counterfactual evidence. This is relevant to false-positive reduction, but the requirements-verification setting is narrower than general review comments.

## Legacy quality appraisal (superseded by the canonical record)

**Provisional score: 21/24.** Strong direct evidence for overcorrection and verification; full-text extraction is needed for exact datasets, metrics, and validity checks.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p58_jin2026_reliable_code_reviewers`; Core; Include; High relevance.
- Study overview: Study of systematic overcorrection in requirement-conformance judgment and a fix-guided verification filter.
- RQ1: False defect and overcorrection comments (Reported).
- RQ2: Requirement/code context and rationale-required judgment (Reported).
- RQ3: Prompt, explanation, fix suggestion, and verification dimensions (Reported).
- RQ4: Detailed prompts can increase misjudgment; executable verification adds cost but may reduce false positives (Reported).
- RQ5: Context consistency and evaluator validity (Reported).
- RQ6: Strong verification-gate support.
- Failure taxonomy: overcorrection; false defect; non-compliance misclassification; unsupported fix.
- Metrics: conformance classification, misjudgment rate, rationale reliability, and verification outcomes.
- Mitigation/trade-off: fix-guided verification with tests; adds execution cost but can reduce false positives.
- Validity: requirement-conformance setting is narrower than general review comments.
- Quality: 21/24 provisional; strong core evidence pending full result extraction.
- Synthesis conclusion: richer reasoning prompts are not automatically safer; verification must be evaluated.

### 1. Identification
- P58; `p58_jin2026_reliable_code_reviewers`; local full PDF extracted and reviewed; authoritative record.
### 2. Screening and proposal alignment
- Include as Core. `p58_jin2026_reliable_code_reviewers`; Core; Include; High relevance.
### 3. Study overview
Study of systematic overcorrection in requirement-conformance judgment and a fix-guided verification filter.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | False defect and overcorrection comments (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Requirement/code context and rationale-required judgment (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Prompt, explanation, fix suggestion, and verification dimensions (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Detailed prompts can increase misjudgment; executable verification adds cost but may reduce false positives (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Context consistency and evaluator validity (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Strong verification-gate support. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| overcorrection | Reported/Inferred | Full PDF |
| false defect | Reported/Inferred | Full PDF |
| non-compliance misclassification | Reported/Inferred | Full PDF |
| unsupported fix. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| conformance classification | Does not alone establish deployment value | Full PDF |
| misjudgment rate | Does not alone establish deployment value | Full PDF |
| rationale reliability | Does not alone establish deployment value | Full PDF |
| and verification outcomes. | Does not alone establish deployment value | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: fix-guided verification with tests; adds execution cost but can reduce false positives.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: task-specific; retained useful-issue coverage is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- requirement-conformance setting is narrower than general review comments.
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
- Missing preservation/escalation evidence and selection/publication bias remain explicit; independent second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: Study of systematic overcorrection in requirement-conformance judgment and a fix-guided verification filter.
- Boundary: richer reasoning prompts are not automatically safer; verification must be evaluated.
