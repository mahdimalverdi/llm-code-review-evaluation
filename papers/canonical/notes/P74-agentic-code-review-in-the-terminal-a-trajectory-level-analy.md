# P74 — Agentic Code Review in the Terminal: A Trajectory-Level Analysis of Behavior, Cost, and Human-Alignment

## 1. Identification

- Project ID: `P74` (provisional)
- Citation key: `p74_charoenwet2026_agentic_code_review_in_the_ter`
- Full reference: Wachiraphan Charoenwet; Kla Tantithamthavorn; Patanamon Thongtanunam; Hong Yi Lin; Minwoo Jeong; Ming Wu. “Agentic Code Review in the Terminal: A Trajectory-Level Analysis of Behavior, Cost, and Human-Alignment.” arXiv:2607.16740v1, 2026.
- DOI/URL: `https://arxiv.org/abs/2607.16740v1`
- Review date: 2026-08-02
- Source/database: arXiv amendment, full-text screening
- Search string used, if applicable: Recorded in `method/search-run-log.csv`.
- Selection stage: included for reconciliation; canonical corpus integration pending
- Duplicate or companion publication: Not reported; verify before final inclusion.

## 2. Screening

- Decision: `Include`
- Relevance: `High`
- Decision rationale: Empirically evaluates terminal-based agentic reviewers using a human-verified review dataset, review precision, repository-grounded trajectories, human alignment, and operational cost.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: taxonomy / annotation protocol / mitigation design / trade-off framework
- Exact inclusion criterion: Core inclusion: LLM-based code review and trade-off-aware evaluation.

## 3. Study overview

- Purpose: Agentic Code Review in the Terminal: A Trajectory-Level Analysis of Behavior, Cost, and Human-Alignment
- Research questions: RQ1 trajectory effort allocation; RQ2 command-line tool use; RQ3 computational cost; RQ4 differences between successful and unsuccessful trajectories.
- Method: Reconstructed benchmark evaluation in Harbor, comparing four terminal agents with five static LLM reviewers and analyzing phase-level trajectories.
- Evaluated system/artifact: Gemini CLI, Claude Code, Rovo Dev, CodeRabbit; static GPT-5.4, GPT-5.2, Claude Sonnet 4.6/4.5, and Gemini 2.5 Pro. Temperature was set to zero.
- Dataset/benchmark: AgenticCR-Verified: 68K discussions from 99 repositories were filtered to 30K candidates, 1,078 resolvable/matching tasks, then 421 stratified tasks; manual verification yielded 362 terminal-based tasks.
- Input context: Repository, commit hash, diff hunks, linked issue and PR context. Agentic systems could inspect the repository through terminal tools; static reviewers received fixed diff/PR inputs.
- Main findings: Rovo Dev and Claude Code had the highest overall comment performance (5.81% and 5.60%). Agents improved localization over static reviewers but incurred exploration/validation overhead; planning was low yet associated with success, while excessive validation correlated with failure.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Exploration and validation dominate agent effort; planning remains below 10% across agents. | Reported | Sections 3.2.3–3.2.4, 4 RQ1. |
| RQ2 | Rovo Dev relies heavily on shell commands; Claude Code mixes shell and structured tools; Gemini CLI uses fewer specialized tools. | Reported | Section 4 RQ2. |
| RQ3 | Rovo Dev had highest reported cost ($0.75 validation, $0.44 exploration); Claude Code cost $0.10 for comparable exploration; Gemini CLI was ≤$0.007 per phase. | Reported | Section 4 RQ3. |
| RQ4 | Successful trajectories showed stronger planning and less downstream validation; excessive validation correlated with unaccomplished reviews. | Reported | Section 4 RQ4. |
| RQ5 | Localization is within ±5 lines of a human comment; human alignment is relevance judged with an LLM-as-a-Judge framework. | Reported | Section 3.2.5. |
| RQ6 | The benchmark exposes a precision–cost–trajectory trade-off, but strict ground truth may penalize valid novel issues. | Inferred | Sections 3.1, 3.2.5, 5.2. |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Localization failure | Generated comment falls outside ±5 lines of a human comment. | Operational category | Section 3.2.5. |
| Human-alignment failure | Generated comment does not identify a relevant issue according to the LLM-as-a-Judge evaluation. | Operational category | Section 3.2.5. |
| Over-validation | Repeated downstream verification/refinement is associated with unaccomplished reviews and high cost. | Reported association | Sections 4 RQ3–RQ4. |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Localization | Comment within ±5 lines of a human comment. | Agentic: 7.22–22.39%; static: 7.26–9.15%. | Table 1, Section 3.2.5. |
| Human alignment | Relevant issue identified by LLM-as-a-Judge. | Agentic: 8.54–15.10%; static: 12.68–21.44%. | Table 1. |
| Overall performance | Comment satisfies both localization and human-alignment criteria. | Rovo Dev 5.81%, Claude Code 5.60%; static maximum 2.61%. | Table 1. |
| Trajectory effort/cost | Steps, tool calls, input/output tokens, and estimated token cost by phase. | Exploration/validation dominate; cost varies substantially by agent. | Sections 3.2.3–3.2.4, 4. |

## 7. Mitigation and trade-offs

- Mitigation family: Repository-grounded agentic exploration and trajectory-aware evaluation.
- Intervention point: Before and during comment generation, through terminal inspection, planning, and validation.
- What it reduces: Missing repository context and poor localization relative to static review.
- Useful feedback potentially lost: Valid novel issues not present in the human ground truth may be scored as failures.
- Coverage effect: Agentic reviewers achieved higher localization/overall precision, but recall or issue coverage is not measured.
- Human escalation effect: Not measured; human comments provide ground truth rather than an escalation workflow.
- Computational/operational cost: Explicitly measured via tokens, tool calls, steps, and estimated cost; exploration and validation are the main cost drivers.
- New failure modes: Inefficient navigation, unnecessary context retrieval, excessive validation, and heuristic trajectory-phase misclassification.

## 8. Annotation and evaluator validity

- Judge/annotator: Human-written review comments are ground truth; human verification removes bots, non-substantive remarks, untied discussions, and extreme commits. Relevance is assessed with an LLM-as-a-Judge framework.
- Rubric: Localization ±5 lines plus relevant-issue alignment; task success requires at least one comment satisfying both.
- Agreement/reliability: No inter-annotator statistic is reported; trajectory labels use keyword heuristics and are manually validated.
- Validity checks: Commit/diff token matching, repository resolvability, manual comment verification, and a released replication package.
- Possible bias: Strict ground truth may undercount valid novel issues; LLM judging and keyword labels introduce noise; repository and tool/model versions limit generalization.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Agent systems, trajectory representation, and phase metrics are clearly specified. |
| Q2 | 2 | Repository-level task definition, filtering, and final 362-task dataset are reported. |
| Q3 | 2 | Models/tools, static-vs-agentic setup, and Harbor harness are described. |
| Q4 | 2 | Localization, alignment, task success, trajectory, and cost metrics are explicit. |
| Q5 | 2 | Human comments, issue/PR/diff context, and judge criteria are defined. |
| Q6 | 0 | No inter-annotator reliability statistic is reported. |
| Q7 | 2 | Dataset filters, evaluation rules, and trajectory annotation procedure are described. |
| Q8 | 1 | Manual validation and replication release exist, but LLM judging/heuristic labels remain risks. |
| Q9 | 2 | Repository exploration is the evaluated intervention relative to static review. |
| Q10 | 2 | Token, tool-call, step, and dollar-cost proxies are measured. |
| Q11 | 2 | Threats to validity explicitly discuss ground truth, judge, heuristics, and generalization. |
| Q12 | 2 | Directly evaluates quality–trajectory–cost trade-offs in terminal code review. |

- Total: `21/24` provisional
- Quality interpretation: Strong benchmark and trajectory evidence, with important validity limits around strict ground truth and automated judging.

## 10. Review-process reliability and bias

- Missing data: Recall/coverage, comment usefulness beyond alignment, and human escalation are not evaluated.
- Publication-bias concern: Not assessed; results may depend on selected repositories and current tool versions.
- Selection uncertainty: Included by full-text screening; arXiv version and replication artifact should be reconciled.
- Extraction uncertainty: Moderate because phase labels are heuristic and judge reliability is not reported.
- Second-reviewer agreement: Not available.
- Duplicate-publication handling: Pending.

## 11. Synthesis-ready conclusion

- Contribution to the SLR: Shows that repository-grounded agents can improve localization and combined precision relative to static reviewers while incurring substantial exploration and validation costs.
- What the paper does not establish: It does not establish recall, usefulness coverage, factual correctness of every comment, or whether lower-cost trajectories are preferable to human reviewers.
- Research gap supported: Evaluation should include trajectory behavior and cost alongside comment-level quality, with stronger human-verified alignment and coverage measures.
- Candidate synthesis claims: Agentic context retrieval can improve review precision, but exploration and validation overhead create a measurable operational trade-off; planning and validation patterns may be more diagnostic than raw output volume.
- Follow-up verification needed: Reconcile the arXiv metadata and inspect the released AgenticCR-Verified artifact before corpus integration.
