# P89 — Understanding Dominant Themes in Reviewing Agentic AI-authored Code

## 1. Identification

- Project ID: `P89`
- Citation key: `p89_haider2026_understanding_dominant_themes_`
- Full reference: Haider, M. A., and Zimmermann, T. “Understanding Dominant Themes in Reviewing Agentic AI-authored Code.” 2026, arXiv:2601.19287.
- DOI/URL: `10.1145/3793302.3793566`; `https://arxiv.org/abs/2601.19287v1`
- Review date: 2026-08-04
- Source/database: arXiv amendment, full-text candidate ARXIV-0103
- Selection stage: included
- Duplicate or companion publication: Publisher DOI match recorded; final version equivalence requires verification.

## 2. Screening

- Decision: `Include`
- Relevance: `High`
- Decision rationale: Directly analyzes review comments on agent-authored pull requests and evaluates comment-theme annotation against human labels.
- Protocol deviation or amendment: None.
- Inclusion group: `Core`
- Proposal deliverable supported: taxonomy / annotation protocol / trade-off framework
- Exact criterion: Direct study of LLM/agent-authored code review feedback and its evaluation.

## 3. Study overview

- Purpose: Identify dominant themes in reviews of agent-authored pull requests.
- Research questions: Not reported as a separate RQ list; the study analyzes review-comment themes and annotation quality.
- Method: Empirical analysis of review comments with LLM-assisted thematic annotation and human comparison. Reported; details from Sections 1–6 and Tables 1–8.
- Evaluated artifact: Human review comments on agent-authored pull requests.
- Dataset/benchmark: 19,450 comments from 3,177 agent-authored pull requests.
- Input context: Pull-request review discussions and associated agent-authored changes; exact context fields require verification.
- Main findings: Twelve dominant themes are reported; LLM-assisted annotation is compared with human labels. Reported.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | The twelve themes provide an empirical taxonomy of review concerns for agent-authored changes. | Reported | Sections 1–6; Tables 1–8 |
| RQ2 | Theme annotation and human comparison support evaluation of comment categories and annotation validity. | Reported | Sections 3–6 |
| RQ3 | LLM-assisted annotation is a post-generation analysis/intervention layer, not a comment-generation mitigation. | Inferred | Sections 3–6 |
| RQ4 | Annotation automation may reduce coding effort, but preservation of useful feedback and workflow cost are not established. | Our perspective | Sections 4–6 |
| RQ5 | The large PR-level corpus supports ecological validity; annotation agreement and label ambiguity remain central risks. | Reported/Our perspective | Sections 2–6 |
| RQ6 | Directly supports taxonomy construction and annotation-protocol design. | Reported | Sections 1–6 |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Theme-level review concern | One of the twelve empirically derived themes in reviews of agent-authored changes. | Reported | Tables 1–8 |
| Annotation disagreement | Human and LLM-assisted theme labels do not always coincide. | Reported | Sections 4–6 |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Theme classification | Human/LLM label comparison | Supports annotation validity analysis; exact agreement metrics require verification. | Sections 4–6 |
| Comment distribution | Counts across 19,450 comments and 12 themes | Provides corpus-level prevalence, not comment correctness or usefulness. | Tables 1–8 |
| Annotation validity | Comparison with human labels | Reliability protocol and adjudication details require verification. | Sections 4–6 |

## 7. Mitigation and trade-offs

- Mitigation family: LLM-assisted annotation / post-generation analysis.
- Intervention point: after generation.
- What it reduces: Manual coding effort, potentially; reported evidence is bounded to annotation.
- Useful feedback potentially lost: Not reported.
- Coverage effect: Theme coverage is reported; useful-comment preservation is not.
- Human escalation effect: Human labels remain a reference/check, but operational escalation is not evaluated.
- Computational/operational cost: Not reported sufficiently for deployment comparison.
- New failure modes: Annotation bias, theme omission, and disagreement between human and LLM labels.

## 8. Annotation and evaluator validity

- Judge/annotator: Human annotators and LLM-assisted annotation.
- Rubric: Twelve-theme coding scheme; full rubric details require verification.
- Agreement/reliability: Comparison is reported; exact agreement statistic is not recorded here.
- Validity checks: Human comparison is reported.
- Possible bias: LLM label priors and theme-boundary ambiguity may bias prevalence estimates.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 1 | Artifact and corpus are identifiable; details require verification. |
| Q2 | 1 | Input context is only partly reported in the current extraction. |
| Q3 | 1 | Dataset size and PR setting are reported. |
| Q4 | 1 | Theme and annotation dimensions are reported. |
| Q5 | 1 | Human/LLM judging is identified. |
| Q6 | 1 | Reliability details require verification. |
| Q7 | 1 | Annotation procedure is described at a high level. |
| Q8 | 1 | Human comparison provides a validity check. |
| Q9 | 1 | LLM-assisted annotation is the evaluated intervention. |
| Q10 | 1 | Operational cost is not fully reported. |
| Q11 | 1 | Dataset and selection limitations require verification. |
| Q12 | 1 | Direct support for taxonomy and annotation validity. |

- Total: `12/24` provisional
- Quality interpretation: Direct and relevant, but the canonical score must be recalculated after checking the full methods and reliability details.

## 10. Review-process reliability and bias

- Missing data: Exact annotation sampling, adjudication, and agreement details require verification.
- Publication-bias concern: Agent-authored PRs may not represent all code-review settings.
- Selection uncertainty: Candidate passed full-text screening; version equivalence remains open.
- Extraction uncertainty: Medium until tables and methods are checked line by line.
- Second-reviewer agreement: Not available.
- Duplicate-publication handling: DOI/preprint relationship recorded as a companion check.

## 11. Synthesis-ready conclusion

- Contribution to the SLR: Strong evidence for taxonomy and annotation-validity design in agentic code review.
- What the paper does not establish: It does not establish generated-comment correctness, usefulness preservation, mitigation effectiveness, or deployment cost.
- Research gap supported: Theme classification and evaluator validity are not equivalent to trade-off-aware comment evaluation.
- Candidate synthesis claims: Large-scale agent-authored review corpora can reveal recurring themes, but automated annotation requires human validity checks.
- Follow-up verification needed: Confirm official publication metadata, exact agreement statistics, rubric, and annotation sampling.
