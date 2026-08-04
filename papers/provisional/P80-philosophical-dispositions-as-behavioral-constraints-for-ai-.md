# P80 — Philosophical Dispositions as Behavioral Constraints for AI-Assisted Code Review

## 1. Identification

- Project ID: `P80` (provisional)
- Citation key: `p80_bansal2026_philosophical_dispositions_as_behavioral`
- Full reference: Kaushal Bansal. “Philosophical Dispositions as Behavioral Constraints for AI-Assisted Code Review: An Empirical Study.” arXiv:2605.23108v1, 2026.
- DOI/URL: `https://arxiv.org/abs/2605.23108v1`
- Review date: 2026-08-04
- Source/database: arXiv full-text screening
- Selection stage: included for reconciliation; canonical corpus integration pending
- Duplicate or companion publication: Not reported; verify final metadata.

## 2. Screening

- Decision: `Include`
- Relevance: `High`
- Decision rationale: Empirically evaluates a multi-lens prompting/orchestration framework for generating structurally different code-review findings.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: taxonomy / annotation protocol / mitigation design / trade-off framework
- Exact inclusion criterion: Core inclusion: AI review behavior, finding diversity, and human-alignment evaluation.

## 3. Study overview

- Purpose: Constrain reviewer behavior through ten philosophy-grounded dispositions and eight role protocols rather than a generic expert prompt.
- Research questions: The retrospective study compares disposition reviews with human reviews and generic prompting, examines finding profiles/misses, and performs preliminary cross-model validation.
- Method: Blind retrospective review of 50 merged PRs across 7 repositories, 5 languages, 5 organizations, and two temporal eras; generic baseline on 34 PRs; cross-model check on 3 PRs.
- Evaluated system/artifact: Four reviewer dispositions are orchestrated for code review (Cynic, Skeptic, Nyāya, Confucian); each uses apophatic refusals and a named hamartia self-check.
- Dataset/benchmark: 50 merged PRs, 601 disposition findings, and 311 human findings; 29 internal/21 public PRs, with enterprise repositories intended to reduce training contamination.
- Input context: Diffs from feature, refactor, bug-fix, and infrastructure changes; disposition reviews are blind to human comments.
- Main findings: 46% convergence with human findings, 75% disposition-only findings, 0 author-judged false positives, and 51% of findings absent from generic prompting. Dispositions miss 50.2% of human findings, including many convention/style cases by design.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Disposition findings are compared with human comments using convergence, unique findings, misses, and false-positive categories. | Reported | Sections III–VII |
| RQ2 | 51% of disposition findings are not produced by generic prompting; unique findings target structural, operational, and logical issues. | Reported | Section V |
| RQ3 | Cross-model runs show 100% framework-structure adherence and 39% finding-level agreement on three PRs. | Reported | Section VI |
| RQ4 | Framework adds differentiated signal but does not replace human review: 50.2% of human findings are missed. | Reported | Section V |
| RQ5 | Human comments are a practical reference, but a single author performs comparison and false-positive judgment. | Reported limitation | Sections III, VII |
| RQ6 | A multi-lens design creates a coverage–noise–review-burden trade-off. | Inferred | Sections V–VII |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Human-finding miss | Human concern not matched by any disposition finding. | Reported | Table VI |
| Framework-convention miss | Style, convention, or typo concern intentionally outside disposition scope. | Reported | Table VI |
| Overextension/hamartia | Disposition’s characteristic failure mode, such as excessive subtraction or skepticism. | Design category | Section III |
| Generic-perspective blind spot | Structural/logical/operational concern absent from generic review. | Reported | Section V |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Human convergence | Disposition finding matches a human concern. | 46%. | Section V |
| Unique findings | Disposition finding not mentioned by human reviewers. | 75%; does not imply objective novelty. | Section V |
| False positives | Finding judged factually incorrect by author. | 0/601, single-rater result. | Section V, VII |
| Baseline differentiation | Disposition finding absent from generic review. | 51% on 34 PRs. | Section V |
| Misses | Human findings not caught by dispositions. | 50.2%; 52% of misses are convention/style/typo by design. | Section V |
| Cross-model adherence | Same disposition structure followed across models. | 100% structural adherence; 39% finding-level agreement, N=3. | Section VI |

## 7. Mitigation and trade-offs

- Mitigation family: Multi-perspective behavioral prompting with explicit failure-mode checks.
- Intervention point: Review generation/orchestration before synthesis.
- What it reduces: Homogeneous generic-review behavior and blind spots for structural, operational, and relational concerns.
- Useful feedback potentially lost: High miss rate for conventions, style, typos, and domain-context findings; candidate volume may increase reviewer burden.
- Coverage effect: Adds unique findings but does not cover half of human findings.
- Human escalation effect: Framework is explicitly complementary to human review; escalation is not measured.
- Computational/operational cost: Multiple disposition passes increase inference/output volume; monetary cost is not reported.
- New failure modes: Philosophy-specific overreach, inconsistent disposition overlap, and false-positive claims based on one rater.

## 8. Annotation and evaluator validity

- Judge/annotator: First author compares disposition findings with human comments and judges factual false positives; a generic same-model baseline is used.
- Rubric: Convergence, unique, miss, false positive, and qualitative finding-type categories.
- Agreement/reliability: Inter-rater agreement was not assessed; this is an explicit limitation. Cross-model finding agreement averages 39% on N=3.
- Validity checks: Stratified PR selection, blind review, baseline comparison, power analysis for 50 PRs, and cross-model pilot.
- Possible bias: Single-rater judgments, retrospective selection, small cross-model sample, and internal/private repositories limit validity.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Architecture and dispositions are clearly specified. |
| Q2 | 2 | 50 PRs across languages, organizations, and eras are described. |
| Q3 | 2 | Baseline and cross-model setups are reported. |
| Q4 | 2 | Convergence, uniqueness, misses, and false positives are explicit. |
| Q5 | 1 | Rubric is defined but manually applied by one rater. |
| Q6 | 0 | Inter-rater reliability is absent. |
| Q7 | 2 | Blind comparison, stratification, and power analysis are reported. |
| Q8 | 1 | Cross-model validation is small and descriptive. |
| Q9 | 2 | Multi-disposition orchestration is explicit intervention. |
| Q10 | 1 | Output burden is discussed, cost is not measured. |
| Q11 | 2 | Misses, confounding, rater bias, and non-replacement of humans are acknowledged. |
| Q12 | 2 | Directly studies review-finding diversity and human alignment. |

- Total: `19/24` provisional
- Quality interpretation: Promising exploratory evidence for differentiated review lenses, weakened by single-rater assessment and small cross-model validation.

## 10. Review-process reliability and bias

- Missing data: Independent false-positive judgments, developer usefulness, review time, and cost are not reported.
- Publication-bias concern: Author-developed framework and positive claims require independent replication.
- Selection uncertainty: Included by full-text screening; final metadata should be reconciled.
- Extraction uncertainty: Moderate/high for uniqueness and false-positive interpretations.
- Second-reviewer agreement: Not available for this note.
- Duplicate-publication handling: Pending version reconciliation.

## 11. Synthesis-ready conclusion

- Contribution to the SLR: Suggests that explicit analytical lenses can produce findings missed by generic prompting, while functioning as a complement rather than replacement for human review.
- What the paper does not establish: It does not establish lower false-positive rates, general human usefulness, or superiority over independently designed reviewer prompts.
- Research gap supported: Multi-lens review needs independent annotation, calibrated quality judgments, and cost/coverage evaluation.
- Candidate synthesis claims: Behavioral constraints may diversify review attention, but unique findings and zero false positives require independent validation before being treated as quality improvements.
- Follow-up verification needed: Replicate comparisons with multiple raters and larger cross-model samples.
