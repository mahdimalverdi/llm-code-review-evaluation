# P89 — Understanding Dominant Themes in Reviewing Agentic AI-authored Code

## 1. Identification

- Project ID: `P89` (provisional)
- Citation key: `p89_haider2026_understanding_dominant_themes_`
- Full reference: Md. Asif Haider; Thomas Zimmermann. “Understanding Dominant Themes in Reviewing Agentic AI-authored Code.” MSR 2026; arXiv:2601.19287v1.
- DOI/URL: `https://doi.org/10.1145/3793302.3793566`; `https://arxiv.org/abs/2601.19287v1`
- Review date: 2026-08-04
- Source/database: arXiv/full-text screening
- Selection stage: included for reconciliation; canonical corpus integration pending
- Duplicate or companion publication: Publisher metadata available; reconcile final record.

## 2. Screening

- Decision: `Include`
- Relevance: `High`
- Decision rationale: Large-scale empirical taxonomy of developer review themes on agent-authored PRs, with human-validated LLM annotation and accepted/rejected PR analysis.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: taxonomy / annotation protocol / mitigation design / trade-off framework
- Exact inclusion criterion: Core inclusion: real-world agentic PR review themes and outcome-linked failure patterns.

## 3. Study overview

- Purpose: Understand what reviewers focus on when reviewing AI-authored PRs and how themes differ by PR outcome.
- Research questions: RQ1 LLM theme annotation accuracy; RQ2 prevalent themes; RQ3 dominant themes in successful vs. rejected PRs.
- Method: Topic modeling plus LLM-assisted semantic clustering produced 12 categories; Gemma 3:12B zero-shot annotation was compared with human labels.
- Evaluated system/artifact: Review comments on agent-authored PRs from OpenAI Codex, Devin, GitHub Copilot, Cursor, and Claude Code.
- Dataset/benchmark: AIDev curated subset of 33,596 PRs; study analyzes 19,450 inline comments across 3,177 PRs, with outcome subset 12,191 comments across 2,035 PRs and 483 rejected/2,035 accepted PRs.
- Input context: Inline review comment text, PR/repository metadata, diffs, review events, and merge/close timestamps.
- Main findings: LLM annotation achieves exact match 78.63%, macro F1 0.7756, κ=0.7348; PR-level dominant-theme Top-1 accuracy 78% and Jaccard 0.76. Functional correctness dominates; documentation, styling, refactoring, testing, and security are recurring themes.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Gemma annotation aligns substantially with human themes at comment and PR levels. | Reported | Section 3 |
| RQ2 | Functional/logic concerns dominate; documentation, style/formatting, refactoring, testing, and security follow. | Reported | Section 4 |
| RQ3 | Security and build themes are more prevalent in rejected PRs; documentation is more prevalent in accepted PRs; undo/revert comments trend toward rejection. | Reported | Section 5 |
| RQ4 | Theme distribution identifies likely review bottlenecks and targeted training opportunities, but causal effects are not established. | Inferred | Sections 4–6 |
| RQ5 | Human annotation validation and AIDev metadata provide ecological evidence, with one-primary-annotator and timestamp limits. | Reported limitation | Sections 3, 6 |
| RQ6 | Supports outcome-aware taxonomy and targeted mitigation for agent-generated code. | Inferred | Sections 5–6 |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Functional/logic defect | Review targets correctness, behavior, or logic changes. | Dominant theme | Section 4 |
| Documentation gap | Missing/inadequate documentation or comments. | Theme/outcome signal | Sections 4–5 |
| Style/formatting | Readability, consistency, or formatting issue. | Theme | Section 4 |
| Testing/security/build concern | Missing tests, vulnerability/safety, configuration/CI/build problem. | Outcome-linked theme | Section 5 |
| Unnecessary undo/revert | Agent changes are reverted or rejected as unnecessary. | Rejection signal | Section 5 |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Theme annotation | Exact match, macro precision/recall/F1, Cohen’s kappa. | Exact 78.63%, macro F1 0.7756, κ=0.7348. | Section 3 |
| PR dominant theme | Top-1 accuracy and Jaccard over top-3 tags. | 78% Top-1, Jaccard 0.76/0.8819 reported at PR-level analyses. | Section 3 |
| Theme prevalence | Share of comments/PRs by 12 categories. | Functional dominates; style/documentation/refactor follow. | Section 4 |
| Outcome association | Theme frequencies in accepted vs. rejected PRs; chi-square tests. | Security 5.59% rejected vs. 3.05% accepted; build/undo patterns differ. | Section 5 |

## 7. Mitigation and trade-offs

- Mitigation family: Theme-aware review oversight, targeted fine-tuning, and reduction of unnecessary agent changes.
- Intervention point: Model training/review prioritization and human oversight after agent PR generation.
- What it reduces: Review fatigue from unnecessary changes and blind spots around security, testing, and build concerns.
- Useful feedback potentially lost: Theme-based prioritization may deprioritize constructive documentation/style feedback; no intervention experiment measures this.
- Coverage effect: Taxonomy exposes 12 categories; coverage of latent/unstated defects is not measured.
- Human escalation effect: Findings recommend targeted oversight; escalation behavior is not measured.
- Computational/operational cost: LLM annotation at scale is used; cost/latency is not reported.
- New failure modes: Topic-label ambiguity, LLM annotation confusion, outcome timestamp artifacts, and multiple-testing risks.

## 8. Annotation and evaluator validity

- Judge/annotator: One author primarily annotates a validation set; Gemma 3:12B annotates the corpus; topic modeling and LLM clustering derive taxonomy.
- Rubric: 12 thematic categories, up to three dominant PR tags, exact/macro metrics, kappa, and Jaccard.
- Agreement/reliability: Comment-level κ=0.7348; validation set is small and primarily annotated by one author.
- Validity checks: Topic modeling, LLM semantic consolidation, random 100-PR validation sample (571 comments), comment- and PR-level evaluation, and chi-square outcome analysis.
- Possible bias: AIDev-only dataset, popular repositories, one annotator, timestamp-based accepted/rejected definition, and no multiple-comparison correction for individual themes.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Dataset, themes, and RQs are explicit. |
| Q2 | 2 | 19,450 comments/3,177 PRs and outcome subsets reported. |
| Q3 | 2 | Taxonomy construction and Gemma annotation are described. |
| Q4 | 2 | Annotation and prevalence/outcome metrics are explicit. |
| Q5 | 2 | 12-category taxonomy and PR top-theme rubric specified. |
| Q6 | 2 | Cohen’s kappa and human comparison reported. |
| Q7 | 2 | Topic modeling, sampling, and multi-level validation included. |
| Q8 | 1 | Small/one-annotator validation and timestamp limitations. |
| Q9 | 1 | Targeted oversight is proposed, not experimentally tested. |
| Q10 | 1 | Scale is reported, cost is not. |
| Q11 | 2 | Dataset, annotation, outcome, and multiple-testing limits discussed. |
| Q12 | 2 | Direct real-world agentic review taxonomy and outcome analysis. |

- Total: `21/24` provisional
- Quality interpretation: Strong large-scale taxonomy and annotation evidence, with observational and validation-sample limits.

## 10. Review-process reliability and bias

- Missing data: Developer usefulness, review time, causal rejection mechanisms, and intervention efficacy are not measured.
- Publication-bias concern: Not assessed; AIDev and popular-repository selection may shape theme distribution.
- Selection uncertainty: Included by full-text screening; final MSR metadata should be reconciled.
- Extraction uncertainty: Moderate because accepted/rejected status uses timestamps and archival effects may confound outcomes.
- Second-reviewer agreement: Kappa reported for study labels; SLR agreement not available.
- Duplicate-publication handling: Pending final-version reconciliation.

## 11. Synthesis-ready conclusion

- Contribution to the SLR: Provides a validated taxonomy of themes in real agent-authored PR reviews and identifies security/build/revert patterns associated with rejection.
- What the paper does not establish: It does not establish that a theme causes rejection, that comments are useful, or that targeted training improves review quality.
- Research gap supported: Agentic review evaluation should connect thematic coverage to human usefulness, rejection reasons, and model-training interventions.
- Candidate synthesis claims: Functional correctness dominates review attention, but security, testing, build, and unnecessary-change themes may be more consequential for rejected agent PRs.
- Follow-up verification needed: Inspect released taxonomy/annotations and reproduce outcome association with multiple annotators and corrected statistical testing.
