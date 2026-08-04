# P85 — RepoReviewer: A Local-First Multi-Agent Architecture for Repository-Level Code Review

## 1. Identification

- Project ID: `P85` (provisional)
- Citation key: `p85_zhang2026_reporeviewer_a_local_first_multi_agent`
- Full reference: Peng Zhang. “RepoReviewer: A Local-First Multi-Agent Architecture for Repository-Level Code Review.” arXiv:2603.16107v1, 2026.
- DOI/URL: `https://arxiv.org/abs/2603.16107v1`
- Review date: 2026-08-04
- Source/database: arXiv full-text screening
- Selection stage: included for reconciliation; canonical corpus integration pending
- Duplicate or companion publication: Not reported; verify final metadata.

## 2. Screening

- Decision: `Include`
- Relevance: `High`
- Decision rationale: Presents a repository-level multi-agent review workflow with explicit context, prioritization, deduplication, artifacts, and planned human evaluation.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: taxonomy / annotation protocol / mitigation design / trade-off framework
- Exact inclusion criterion: Core inclusion: repository-level review architecture and evaluation infrastructure.

## 3. Study overview

- Purpose: Provide a practical local-first architecture for repository-level automated review rather than claim benchmark superiority.
- Research questions: The report describes architecture, implementation trade-offs, practical failure modes, and future evaluation rather than completed empirical RQs.
- Method: Systems design and operational demonstration using Python CLI, FastAPI API, LangGraph orchestration, LiteLLM, PyGithub, and Next.js UI.
- Evaluated system/artifact: RepoReviewer stages repository acquisition, context synthesis, file review, prioritization, and summary generation.
- Dataset/benchmark: No completed benchmark; a minimal repository demonstration and evaluation templates are provided.
- Input context: Public GitHub repository or PR; repository structure, README, key file previews, selected diffs, and branch synchronization.
- Main findings: The full pipeline is operational, but precision, recall, usefulness, cost, and latency require future human-annotated evaluation.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Structured findings contain file, line, severity, issue, suggestion, and snippet, but no validated quality results are reported. | Reported | Sections 2–4 |
| RQ2 | ContextAgent synthesizes repository structure and key files; larger/sparse repositories create context-breadth trade-offs. | Reported | Sections 3, 5 |
| RQ3 | Multi-agent decomposition and deterministic filtering are proposed to reduce shallow review, duplication, and weak prioritization. | Design claim | Sections 3–4 |
| RQ4 | Prioritization and deduplication target human inspection burden; no user study quantifies improvement. | Design claim/limitation | Sections 3, 5 |
| RQ5 | Evaluation runner, annotation sheets, and aggregation artifacts are implemented, but results are deferred. | Reported | Section 5 |
| RQ6 | Architecture makes context, prioritization, and artifacts inspectable, supporting future trade-off evaluation. | Inferred | Sections 3–6 |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Context overflow | Repository content exceeds model context limits or requires selective file inclusion. | Reported failure mode | Section 2 |
| Shallow file review | Single-pass review lacks project-wide structure/dependencies. | Motivation/design target | Sections 1, 3 |
| Duplicate findings | Multiple file agents produce overlapping comments. | Design target | Sections 1, 3 |
| Weak prioritization | Important findings are buried among low-priority output. | Design target | Sections 1, 3 |
| Provider quota/rate limit | Large evaluations are disrupted by provider limits. | Reported limitation | Section 5 |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Structured review | JSON/Markdown findings with file, line, severity, issue, suggestion, snippet. | Implemented, not benchmarked. | Sections 2–4 |
| Human usefulness | Planned precision, recall, usefulness, and severity agreement. | Requires human annotation; no result. | Section 5 |
| Efficiency | Planned latency, token usage, and cost. | Not reported empirically. | Section 5 |
| Reproducibility | Per-run artifacts, annotation sheets, CSV/JSON/LaTeX exports. | Infrastructure implemented. | Sections 4–5 |

## 7. Mitigation and trade-offs

- Mitigation family: Multi-agent decomposition, local context synthesis, prioritization, deduplication, and human-auditable artifacts.
- Intervention point: Repository acquisition and review orchestration before final report presentation.
- What it reduces: Context blindness, duplicated findings, weak ranking, and opaque monolithic prompts.
- Useful feedback potentially lost: File selection and context truncation may omit relevant evidence; prioritization may suppress lower-severity valid findings.
- Coverage effect: Intended to improve repository coverage, but no measured recall.
- Human escalation effect: Artifacts and annotation sheets support later human review; workflow is not evaluated.
- Computational/operational cost: Multiple agents and context synthesis increase calls/tokens; provider quota/rate limits are acknowledged.
- New failure modes: Context-selection errors, cross-agent inconsistency, deduplication mistakes, and summary loss.

## 8. Annotation and evaluator validity

- Judge/annotator: No completed judge; the system includes annotation sheets and aggregation tools for future human evaluation.
- Rubric: Planned precision, recall, usefulness, severity agreement, cost, and latency.
- Agreement/reliability: Not reported.
- Validity checks: Minimal operational demonstration, comparative/ablation modes, and exportable per-run artifacts; no completed benchmark.
- Possible bias: Architecture paper without empirical comparison; demonstrations may not represent difficult repositories.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Architecture and workflow are clearly specified. |
| Q2 | 0 | No completed benchmark or dataset evaluation. |
| Q3 | 2 | Components, interfaces, and modes are described. |
| Q4 | 0 | No empirical quality metrics/results. |
| Q5 | 1 | Planned rubric exists but is not applied. |
| Q6 | 0 | No reliability evidence. |
| Q7 | 1 | Demonstration and ablation infrastructure exist. |
| Q8 | 1 | Operational demo supports feasibility, not external validity. |
| Q9 | 2 | Multi-agent/context/prioritization interventions are explicit. |
| Q10 | 1 | Cost/latency are acknowledged but unmeasured. |
| Q11 | 2 | Practical failure modes and deferred evaluation are candidly discussed. |
| Q12 | 2 | Direct repository-level review relevance. |

- Total: `14/24` provisional
- Quality interpretation: Useful systems contribution and evaluation scaffold, not evidence of comparative review quality.

## 10. Review-process reliability and bias

- Missing data: Completed benchmark, human labels, correctness/usefulness, recall, cost, latency, and user impact.
- Publication-bias concern: Architecture paper explicitly defers performance claims; no comparative evidence.
- Selection uncertainty: Included as core architecture evidence; final metadata should be reconciled.
- Extraction uncertainty: Low for implementation claims, high for effectiveness claims because they are absent.
- Second-reviewer agreement: Not available for this note.
- Duplicate-publication handling: Pending version reconciliation.

## 11. Synthesis-ready conclusion

- Contribution to the SLR: Offers a concrete decomposition and audit-friendly infrastructure for repository-level review, while explicitly separating implementation from validation.
- What the paper does not establish: It does not establish precision, recall, usefulness, human acceptance, or cost superiority.
- Research gap supported: Repository review systems need reproducible, human-annotated evaluation of context selection, prioritization, deduplication, and operational cost.
- Candidate synthesis claims: Multi-agent decomposition is a plausible architecture-level mitigation for repository context and output management, but it remains an unvalidated design hypothesis here.
- Follow-up verification needed: Run the supplied evaluation harness on human-annotated repositories and inspect ablation artifacts.
