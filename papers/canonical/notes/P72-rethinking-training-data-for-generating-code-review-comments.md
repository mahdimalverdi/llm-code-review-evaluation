# P72 — Rethinking Training Data for Generating Code Review Comments

## 1. Identification

- Project ID: `P72` (provisional)
- Citation key: `p72_centellas_claros2026_rethinking_training_data_for_g`
- Full reference: Leonardo Centellas-Claros, Estefania Pakarati-Cofre, Juan Pablo Sandoval Alcocer, and Diego Elias Costa. “Rethinking Training Data for Generating Code Review Comments.” arXiv, 2026.
- DOI/URL: `https://arxiv.org/abs/2607.25851v1`
- Review date: 2026-08-02
- Source/database: arXiv amendment, full-text screening
- Search string used, if applicable: Recorded in `method/search-run-log.csv`.
- Selection stage: included for reconciliation; canonical corpus integration pending
- Duplicate or companion publication: No publisher version identified in the current record; verify before final inclusion.

## 2. Screening

- Decision: `Include`
- Relevance: `High`
- Decision rationale: Empirically analyses diff-comment training pairs for automated review-comment generation and derives a taxonomy covering semantic ambiguity, lack of actionability, and context dependence.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: taxonomy / annotation protocol / mitigation design / trade-off framework
- Exact inclusion criterion: Core inclusion: generated review comments and dataset/context validity.

## 3. Study overview

- Purpose: Rethinking Training Data for Generating Code Review Comments
- Research questions: Not reported as a separate list.
- Method: Four-step empirical study: select a public dataset, randomly sample 383 pairs, independently screen them with two reviewers, and construct a taxonomy through open card sorting. Reported.
- Evaluated system/artifact: Diff-comment training pairs and taxonomy-guided LLM filtering.
- Dataset/benchmark: Training split of 117,739 diff-comment pairs; 383 sampled pairs; 184 identified as misaligned. A second 270-pair dataset from Liu et al. is used for filtering comparison.
- Input context: Localized code diff paired with a human review comment; the study tests the limitation of diff-only/localized input.
- Main findings: Misalignment categories are semantic ambiguity (25/184), lack of actionability (98/184), and context dependence (61/184). Taxonomy-guided prompting improves filtering only marginally and inconsistently.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Reports semantic ambiguity, lack of actionability, and context dependence in training pairs. | Reported | Abstract; Sections III–IV; Table I |
| RQ2 | Uses actionability/suitability classification and precision, recall, and F1 for LLM filtering. | Reported | Section IV; Table II |
| RQ3 | Taxonomy-guided prompting is an after-generation dataset-filtering intervention. | Reported | Section IV |
| RQ4 | Filtering captures signal beyond chance but taxonomy-guided gains are marginal and inconsistent; preservation/coverage cost is not measured. | Reported/Our perspective | Section IV |
| RQ5 | Shows that localized diff input can omit review intent, surrounding code, previous comments, or external artifacts. | Reported | Sections II–III; Table I |
| RQ6 | Directly supports failure taxonomy, annotation protocol, context-quality model, and trade-off framing. | Reported/Our perspective | Sections III–V |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Semantic ambiguity | Comment intent is unclear or under-specified. | Reported | Section III; Table I |
| Lack of actionability | Inquiry, comment, chit-chat, and remark do not provide a concrete modification path. | Reported | Section III; Table I |
| Context dependence | Comment depends on another change, another line, a previous comment, or a broken URL. | Reported | Section III; Table I |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Suitability/actionability | Two-reviewer binary assessment of whether a pair is suitable training feedback. | Reported | Section III |
| Filtering performance | Precision, recall, and F1 for Valid/Noisy classification. | Reported | Section IV; Table II |
| Inter-rater reliability | Cohen’s kappa κ = 0.758 for the initial screening. | Reported | Section III-A |

## 7. Mitigation and trade-offs

- Mitigation family: Taxonomy-guided LLM dataset filtering.
- Intervention point: after generation.
- What it reduces: Misaligned training pairs, imperfectly; filtering remains difficult.
- Useful feedback potentially lost: Valid comments may be classified as unsuitable; preservation is not measured.
- Coverage effect: Class-level recall is reported, but review-issue coverage is not.
- Human escalation effect: Human labels establish ground truth; deployment escalation is not evaluated.
- Computational/operational cost: Not reported.
- New failure modes: Over-filtering, model-dependent class imbalance, and taxonomy-guidance brittleness.

## 8. Annotation and evaluator validity

- Judge/annotator: Two postgraduate software-engineering reviewers; GPT-3.5-turbo and GPT-4o-mini for filtering.
- Rubric: Actionable/suitable versus misaligned/unsuitable, with taxonomy categories.
- Agreement/reliability: Cohen’s κ = 0.758; disagreements were discussed to consensus.
- Validity checks: LLM predictions compared with manually annotated datasets using precision, recall, and F1.
- Possible bias: Reviewer judgments and prompt definitions determine the boundary between valid interaction and unsuitable generation target.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Artifact and misalignment taxonomy are clearly reported. |
| Q2 | 2 | Diff-only input and missing-context dependencies are described. |
| Q3 | 2 | Dataset sizes and sampling are reported. |
| Q4 | 2 | Actionability, suitability, precision, recall, and F1 are reported. |
| Q5 | 2 | Two reviewers and LLM filtering configurations are identified. |
| Q6 | 2 | Cohen’s kappa and consensus procedure are reported. |
| Q7 | 2 | Screening and card-sorting procedures are described. |
| Q8 | 2 | Manual labels provide a validity reference. |
| Q9 | 1 | Taxonomy-guided filtering is evaluated, but deployment mitigation is not. |
| Q10 | 0 | Computational/operational cost is not reported. |
| Q11 | 1 | Dataset/task-formulation limitations are discussed. |
| Q12 | 2 | Direct support for taxonomy, context, and annotation design. |

- Total: `20/24`
- Quality interpretation: Strong direct evidence for taxonomy and annotation validity; preservation and operational-cost evidence are absent.

## 10. Review-process reliability and bias

- Missing data: Operational cost, preservation, and review-coverage effects are not reported.
- Publication-bias concern: Results rely on one primary dataset and sampled pairs.
- Selection uncertainty: Included by full-text screening; publisher/version check pending.
- Extraction uncertainty: Low for reported methods and taxonomy; medium for transfer implications.
- Second-reviewer agreement: Not available.
- Duplicate-publication handling: Pending.

## 11. Synthesis-ready conclusion

- Contribution to the SLR: Direct evidence that dataset misalignment is heterogeneous and that localized input can make valid review interactions unsuitable generation targets.
- What the paper does not establish: It does not establish production filtering performance, useful-feedback preservation, review coverage, or operational cost.
- Research gap supported: Dataset cleaning and taxonomy-guided filtering do not by themselves solve context and task-formulation validity.
- Candidate synthesis claims: LLM code-review evaluation should distinguish dataset noise from context-dependent or structurally misaligned feedback.
- Follow-up verification needed: Verify publisher metadata and reconcile the provisional project ID before final citation.
