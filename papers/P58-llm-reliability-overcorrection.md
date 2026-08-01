# P58 — Are LLMs Reliable Code Reviewers? Systematic Overcorrection

## Screening and proposal alignment

- **Decision:** Include
- **Group:** Core
- **Relevance:** High
- **Evidence basis:** Full local PDF, abstract and first-pass review
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

## Quality appraisal

**Provisional score: 21/24.** Strong direct evidence for overcorrection and verification; full-text extraction is needed for exact datasets, metrics, and validity checks.
