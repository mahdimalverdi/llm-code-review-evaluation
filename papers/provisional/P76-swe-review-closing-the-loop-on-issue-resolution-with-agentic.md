# P76 — SWE-Review: Closing the Loop on Issue Resolution with Agentic Code Review

## 1. Identification

- Project ID: `P76` (provisional)
- Citation key: `p76_wang2026_swe_review_closing_the_loop_on`
- Full reference: Ruoyu Wang; Jierun Chen; Shaowei Wang; Chaofan Tao; Sidi Yang; Yuxin Jiang; Kim-Hui Yap; Lifeng Shang; Xiaohui Li; Haoli Bai. “SWE-Review: Closing the Loop on Issue Resolution with Agentic Code Review.” arXiv:2607.06065v1, 2026.
- DOI/URL: `https://arxiv.org/abs/2607.06065v1`
- Review date: 2026-08-04
- Source/database: arXiv full-text screening
- Selection stage: included for reconciliation; canonical corpus integration pending
- Duplicate or companion publication: Not reported; verify final metadata.

## 2. Screening

- Decision: `Include`
- Relevance: `High`
- Decision rationale: Directly evaluates agentic review decisions and structured diagnoses as part of a generate–review–revise loop for AI-generated pull requests.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: taxonomy / annotation protocol / mitigation design / trade-off framework
- Exact inclusion criterion: Core inclusion: LLM-based code review and end-to-end usefulness evaluation.

## 3. Study overview

- Purpose: Close the open loop between AI-generated PRs and issue resolution through repository-grounded review and revision.
- Research questions: The study evaluates review correctness, revision usefulness, trajectory training, transfer to issue resolution, and test-time scaling.
- Method: SWE-Review framework and SWE-Review-Bench evaluation; agentic reviewer explores repository, makes approve/request-changes decision, and gives structured revision diagnosis.
- Evaluated system/artifact: Reviewer agents and open reviewers trained from trajectories; experiments use models including Claude Opus 4.6, Qwen3 variants, and GLM-5.
- Dataset/benchmark: SWE-Review-Bench contains 1,384 candidate PRs from 500 SWE-bench Verified issues and three PR-generator quality splits; SWE-Review-Traj contains 8,914 agentic review trajectories.
- Input context: Repository checkout, issue, candidate PR/diff, executable tests and hidden outcome signals; reviewer may browse files, search code, inspect dependencies, and execute commands.
- Main findings: Generate–review–revise raises resolve rates (e.g., Qwen3-30B-A3B 27.5%→56.9%; Qwen3-Coder 50.9%→68.8%; GLM-5 72.2%→75.4%). Agentic review beats fixed-context review in decision accuracy and post-revision resolve rate.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Completion Rate (parseable review), Decision Accuracy, and Resolve Rate after Revision evaluate review quality in an executable issue-resolution setting. | Reported | Sections 2–3 |
| RQ2 | Diagnosis quality is scored for factual accuracy, suggested-fix correctness, and repository grounding; judge means exceed 3.0/5. | Reported | Section 3.3, Table 1 |
| RQ3 | Agentic review is an intervention in a generate–review–revise loop; review trajectories also support SFT and reviewer-gated test-time scaling. | Reported | Sections 3–4 |
| RQ4 | Review improves downstream resolve rate, while review trajectories improve reviewer completion and decision accuracy. | Reported | Sections 3.3–4 |
| RQ5 | Benchmark tasks preserve repository, issue, PR, commit, and hidden-test context; 8,914 trajectories provide training data. | Reported | Sections 2–3 |
| RQ6 | The paper reframes review usefulness as revision and issue resolution, rather than comment similarity alone. | Inferred | Sections 2–5 |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Incorrect merge decision | Reviewer approves an unresolved PR or requests changes on a resolved PR. | Operational category | Section 2 |
| Ungrounded diagnosis | Feedback lacks factual accuracy, correct fix, or repository evidence. | Operational category | Section 3.3 |
| Non-parseable review | Reviewer fails to produce a valid structured report. | Operational category | Section 2 |
| Open-loop revision failure | Review feedback does not help the coding agent improve the patch outcome. | Operational category | Sections 2–4 |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Completion | Parseable final review report. | SFT raises Qwen3-8B completion from about 4% to 71–84%. | Sections 2, 3.3 |
| Decision accuracy | Correct approve/request-changes decision. | SFT yields 67–72% DA for Qwen3-8B; agentic beats fixed-context. | Sections 2, 3.3 |
| Revision usefulness | Resolve Rate after Revision (RRR). | Closed loop raises resolve rate substantially across generators. | Sections 2–4 |
| Diagnosis quality | 1–5 ratings for factual accuracy, fix correctness, and repository grounding. | Mean scores exceed 3.0; reviewer quality is not perfect. | Section 3.3, Table 1 |
| Test-time scaling | Resolve rate under sampling, reviewer gating, and review-guided resampling. | Review enables effective and efficient scaling. | Section 4.3 |

## 7. Mitigation and trade-offs

- Mitigation family: Repository-grounded diagnosis and iterative review-guided patch revision.
- Intervention point: After candidate PR generation and before final merge/issue-resolution judgment.
- What it reduces: Unresolved or incorrect candidate patches by tracing issue context, code, and execution evidence.
- Useful feedback potentially lost: The benchmark focuses on SWE-style correctness and revision, not style, maintainability, or human communication quality.
- Coverage effect: Review improves resolve rate, but issue coverage and recall of all valid defects are not separately measured.
- Human escalation effect: Not measured; review is an autonomous agent step.
- Computational/operational cost: Test-time scaling and multi-turn repository exploration add inference/tool cost; detailed monetary accounting is not reported.
- New failure modes: Reviewer diagnosis can be inaccurate or ungrounded; structured output failure and error propagation through revision remain possible.

## 8. Annotation and evaluator validity

- Judge/annotator: SWE-bench hidden tests and known issue outcomes evaluate resolution; two judge settings assess diagnosis quality; agentic review trajectories are generated by teacher reviewers.
- Rubric: Completion, binary decision correctness, resolve after revision, and 1–5 diagnosis ratings for factual accuracy, suggested fix, and repository grounding.
- Agreement/reliability: The paper reports judge scores but no inter-rater reliability statistic for diagnosis assessment.
- Validity checks: Executable tests, golden patches, oracle revision condition, comparison with fixed-context baselines, and multiple PR-generator quality splits.
- Possible bias: SWE-bench Verified tasks and model/scaffold choices limit generalizability; diagnosis scores and hidden tests may not capture style or broader human usefulness.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Framework, benchmark, and agent roles are clearly specified. |
| Q2 | 2 | 1,384 PRs from 500 issues and task construction are reported. |
| Q3 | 2 | Reviewer models, generators, and trajectory corpus are described. |
| Q4 | 2 | Completion, decision, diagnosis, and revision outcomes are explicit. |
| Q5 | 2 | Repository/issue/PR/test context and revision protocol are specified. |
| Q6 | 1 | Multiple judges are used, but reliability statistics are absent. |
| Q7 | 2 | Baselines, oracle revision, and split comparisons are included. |
| Q8 | 2 | Hidden tests, golden patches, and executable validation support construct validity. |
| Q9 | 2 | Repository-grounded review and review-guided revision are explicit interventions. |
| Q10 | 1 | Scaling efficiency is studied, but full monetary/tool cost is not reported. |
| Q11 | 2 | Scope limits around SWE correctness, style, models, and scaffolds are discussed. |
| Q12 | 2 | Directly evaluates review quality as downstream issue-resolution usefulness. |

- Total: `22/24` provisional
- Quality interpretation: Strong end-to-end evidence for review-guided issue resolution, with limited evidence for human-facing comment quality and operational cost.

## 10. Review-process reliability and bias

- Missing data: Human reviewer usefulness, comment style, defect-recall coverage, and detailed inference cost are not evaluated.
- Publication-bias concern: Not assessed; results may depend on SWE-bench task selection and chosen agents.
- Selection uncertainty: Included by full-text screening; final metadata and released benchmark should be reconciled.
- Extraction uncertainty: Moderate because diagnosis judging and agentic trajectories may vary by scaffold/model.
- Second-reviewer agreement: Not available for this note.
- Duplicate-publication handling: Pending version reconciliation.

## 11. Synthesis-ready conclusion

- Contribution to the SLR: Establishes an end-to-end evaluation where agentic review is useful when it helps revise candidate patches and resolve issues, not merely when its comments resemble references.
- What the paper does not establish: It does not establish human usefulness, style quality, comprehensive defect coverage, or low operational cost.
- Research gap supported: Code-review evaluation should connect diagnosis correctness to downstream patch revision while separately measuring communication quality and cost.
- Candidate synthesis claims: Repository-grounded agentic review can substantially improve issue-resolution outcomes, but its value depends on structured, grounded diagnoses and incurs additional inference complexity.
- Follow-up verification needed: Reconcile metadata and inspect the released SWE-Review-Bench/Traj artifacts and exact judge prompts.
