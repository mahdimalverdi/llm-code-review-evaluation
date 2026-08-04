# P73 — Evaluating the Impact of Explainable AI on Trust in AI-Assisted Code Review

## 1. Identification

- Project ID: `P73` (provisional)
- Citation key: `p73_gao2026_evaluating_the_impact_of_expla`
- Full reference: Zhenhan Gao; Marvin Muñoz Barón; Umm-e Habiba; Daniel Graziotin; Stefan Wagner. “Evaluating the Impact of Explainable AI on Trust in AI-Assisted Code Review.” Proceedings of the ACM on Software Engineering, ISSTA093, 2026; arXiv:2607.24601v1.
- DOI/URL: `https://doi.org/10.1145/3832184`; `https://arxiv.org/abs/2607.24601v1` (publisher metadata in the PDF gives October 2026; verify the final bibliographic record).
- Review date: 2026-08-02
- Source/database: arXiv amendment, full-text screening
- Search string used, if applicable: Recorded in `method/search-run-log.csv`.
- Selection stage: included for reconciliation; canonical corpus integration pending
- Duplicate or companion publication: Not reported; verify before final inclusion.

## 2. Screening

- Decision: `Include`
- Relevance: `High`
- Decision rationale: Within-subject user study directly evaluates explanation level, trust, agreement with AI review recommendations, and review time for AI-assisted code review.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: taxonomy / annotation protocol / mitigation design / trade-off framework
- Exact inclusion criterion: Core inclusion: AI-assisted code review and reviewer trust/usefulness evaluation.

## 3. Study overview

- Purpose: Evaluating the Impact of Explainable AI on Trust in AI-Assisted Code Review
- Research questions: RQ1 asks how XAI affects trust; RQ2 how explanation level affects agreement with AI recommendations; RQ3 how XAI affects review-task time; and RQ4 which reasons participants give for accepting or rejecting the change.
- Method: Controlled within-subject online user study with 34 Prolific participants, preceded by a five-person pilot; repeated-measures ANOVA and paired post-hoc tests for trust, agreement, and time, plus qualitative coding of decision reasons.
- Evaluated system/artifact: A two-phase GPT-4o code-review pipeline. Phase 1 generates feedback and an accept/reject recommendation; Phase 2 explains feedback and highlights supporting diff regions. Temperature was set to zero.
- Dataset/benchmark: Nine manually selected real-world pull requests from TheAlgorithms/Python, spanning three difficulty levels and nine final decisions; each participant reviewed all nine tasks, three per condition.
- Input context: Raw Python diffs, under 55 changed lines, selected for non-trivial but self-contained changes; conditions exposed (A) recommendation + feedback + inline detailed explanations, (B) recommendation + feedback, or (C) recommendation only.
- Main findings: Full explanations produced the highest perceived trust (M=3.99/5), while moderate explanations produced the highest agreement with the AI recommendation (89.22%, 91/102). Explanation condition significantly affected trust and agreement but not completion time; readability and correctness were the most common decision reasons.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Trust means were A=3.99, B=3.77, C=3.41; repeated-measures ANOVA found a condition effect, F(2,66)=8.2497, p=0.0006. After Bonferroni correction, A–C remained significant, whereas A–B and B–C did not. | Reported | Abstract; Sections 3.2.3, 4.1. |
| RQ2 | Agreement was highest in B (89.22%, 91/102), followed by A (77.45%) and C. The condition effect was significant, F(2,66)=9.1042, p=0.0003; only B–C remained significant after correction. | Reported | Abstract; Section 4.2. |
| RQ3 | Mean task times were A=196.31 s, B=166.42 s, C=164.18 s; the difference was not significant, F(2,66)=0.5704, p=0.5681. | Reported | Abstract; Section 4.3. |
| RQ4 | Participants most often cited code readability and correctness. Agreement with the AI was mentioned only in explanation conditions and never in C; qualitative coding of 306 multi-label responses yielded Krippendorff’s α=0.7564. | Reported | Sections 3.3, 4.4, 5. |
| RQ5 | The study uses 34 participants and nine controlled PR tasks, TXAI trust items, decision agreement, task time, and coded reasons; the authors note a shuffling imbalance and single-session trust measurement. | Reported | Sections 3.2–3.3, 4.7. |
| RQ6 | Direct evidence links explanation format to trust/agreement trade-offs, but recommendation correctness was held constant and comment-level usefulness or error detection was not measured. | Inferred | Sections 4.2, 4.7, 5. |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Explanation-induced overtrust or scrutiny | Full explanations increased perceived trust but also led to more rejection of AI recommendations; more agreement is not treated as equivalent to better judgment. | Reported/interpretive | Sections 4.2, 4.7, 5. |
| Recommendation correctness not varied | The study manually verified review accuracy and held recommendation quality constant, so it does not directly test detection of incorrect AI recommendations. | Reported limitation | Section 5. |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Perceived trust | Seven-item revised TXAI questionnaire, averaged per participant and condition on a 1–5 scale. | A=3.99, B=3.77, C=3.41; ANOVA significant. | Sections 3.2.3, 4.1. |
| Behavioral agreement | Proportion of three decisions per condition matching the AI recommendation. | B=89.22%, A=77.45%; condition effect significant. | Section 3.3, 4.2. |
| Review time | Page-load to next-page duration per task, averaged over three tasks per condition. | No significant condition effect. | Section 3.3, 4.3. |
| Decision reasoning | Mandatory free-text justification, multi-label coded by three coders. | α=0.7564; readability and correctness most frequent. | Sections 3.2.3, 3.3, 4.4. |

## 7. Mitigation and trade-offs

- Mitigation family: Explainability and code-grounded rationale presentation.
- Intervention point: During review presentation: Phase 2 links each feedback item to highlighted diff regions and exposes a localized explanation on hover.
- What it reduces: Opacity and uncertainty about why the model generated feedback; the study does not establish reductions in false or unhelpful comments.
- Useful feedback potentially lost: Not measured; the paper warns that detailed explanations may increase critical scrutiny rather than compliance.
- Coverage effect: Not measured.
- Human escalation effect: Not measured.
- Computational/operational cost: GPT-4o is used for both phases, but generation latency or monetary cost is not evaluated; detailed explanations increased task time descriptively but not significantly.
- New failure modes: Post-hoc rationalization and overtrust remain concerns; the authors explicitly note that explanation faithfulness is not guaranteed.

## 8. Annotation and evaluator validity

- Judge/annotator: 34 human participants for trust/decisions; three coders (two PhD students and one master’s student) for free-text reasons.
- Rubric: Seven-item revised TXAI scale; binary accept/reject decision; mandatory written reason; AI agreement is exact match to the recommendation.
- Agreement/reliability: Krippendorff’s α=0.7564 on 306 multi-label reasoning responses, described as tentative/acceptable but below 0.80.
- Validity checks: Five-person pilot led to a mandatory reasoning field and a recommendation-only control. Prompt outputs were manually checked for requested elements and accuracy; sample decisions came from PR merge outcomes.
- Possible bias: Prolific sample, self-reported programming/AI experience, curated single-repository tasks, one-session trust measurement, and a task-to-condition shuffling imbalance limit generalizability.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Two-phase GPT-4o review/explanation system and controlled conditions are clearly described. |
| Q2 | 2 | Nine Python PRs, selection criteria, difficulty strata, and condition assignment are reported. |
| Q3 | 2 | 34 participants, recruitment, power analysis, and participant characteristics are reported. |
| Q4 | 2 | Trust, agreement, time, and coded decision-reason metrics are operationalized with results. |
| Q5 | 2 | TXAI, behavioral agreement, timing, and mandatory reasoning protocols are specified. |
| Q6 | 1 | Coder agreement is reported, but it is tentative and below the 0.80 robustness threshold. |
| Q7 | 2 | Pilot, prompt validation, randomization, and repeated-measures analysis are described. |
| Q8 | 1 | Construct-validity limits, single-session measurement, and shuffle imbalance are acknowledged. |
| Q9 | 2 | Inline, code-grounded explanations are the explicit intervention. |
| Q10 | 1 | Time is measured, but generation/operational cost is not. |
| Q11 | 2 | Sampling, task assignment, measurement, and generalizability limitations are discussed. |
| Q12 | 2 | Directly tests a trust/agreement/time trade-off in AI-assisted code review. |

- Total: `21/24` provisional
- Quality interpretation: Strong study-method evidence for trust/agreement trade-offs, but limited for comment correctness, usefulness, coverage, and operational cost.

## 10. Review-process reliability and bias

- Missing data: No comment-level correctness/usefulness taxonomy, coverage, escalation behavior, or generation cost is reported.
- Publication-bias concern: Single-repository, curated tasks and a Prolific sample may limit external validity; publication bias is not assessed.
- Selection uncertainty: Included by full-text screening; arXiv/publisher version should be reconciled before corpus integration.
- Extraction uncertainty: Moderate; the paper reports a task-condition shuffling imbalance and tentative coder reliability.
- Second-reviewer agreement: Not available for this note.
- Duplicate-publication handling: Publisher DOI/version reconciliation pending.

## 11. Synthesis-ready conclusion

- Contribution to the SLR: Provides direct evidence that explanation detail can improve perceived trust without increasing agreement, exposing a trust–critical-engagement trade-off in AI-assisted review.
- What the paper does not establish: It does not show that explanations improve review-comment correctness, usefulness, coverage, or detection of flawed recommendations; recommendation quality was held constant.
- Research gap supported: Explanation formats should be evaluated jointly with recommendation correctness and behavioral calibration, not with trust or agreement alone.
- Candidate synthesis claims: Code-grounded explanations can increase perceived trust, while moderate explanations may yield more agreement; agreement should not be used as a standalone proxy for review quality.
- Follow-up verification needed: Reconcile the arXiv and publisher records, inspect the replication package if available, and compare with P72/P74 evidence on comment-level quality.
