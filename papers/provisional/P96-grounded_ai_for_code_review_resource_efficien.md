# P96 — Grounded AI for Code Review: Resource-Efficient Large-Model Serving in Enterprise Pipelines

> **Provisional intake record.** This is not a canonical paper note.

| Field | Value |
|---|---|
| Project ID | `P96` (provisional) |
| Citation key | `p96_mandal2025_grounded_ai_for_code_review_re` |
| Authors | Sayan Mandal; Hua Jiang |
| Year | 2025 |
| Source | arXiv |
| arXiv | `2510.10290v1` |
| Screening tier | `core` |
| Reconciliation status | New candidate after initial local matching |
| Metadata status | local_arxiv_metadata |
| Evidence status | Full-text eligibility recorded; extraction not yet completed |

## 1. Identification

- Duplicate or companion publication: No publisher venue or DOI is reported; verify before final integration.

## 2. Screening
- Decision: `Include`; Relevance: `High`
- Decision rationale: Directly evaluates grounded PR-native AI review comments, static-analysis anchoring, violation outcomes, latency, resources, and developer perceptions.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: trade-off framework / context quality / operational evaluation

## 3. Study overview
- Purpose: Reduce hallucination, weak rationale, and serving cost in compliance-heavy review pipelines.
- Research questions: Effects of grounding on violation reduction; competitiveness of on-prem quantized models; and resource-efficient serving.
- Method: Pair static-analysis findings with AST/call-graph-guided context, generate structured evidence-backed comments, and serve a quantized open-weight model with one GPU, caching, and on-demand loading.
- Evaluated system/artifact: PR-native pipeline with analyzer, context extractor, prompt generator, LLM backend, policy handling, provenance logging, and threaded comments.
- Dataset/benchmark: 100 synthetic-but-replayable PR scenarios expanded to 314 atomic hunks across 10 C/C++ codebases and roughly 600K lines.
- Input context: Diff hunks, rule IDs/severity, file/line spans, rationale, and AST-guided code. Offline evaluation applies candidate patches automatically; deployment suggests changes for human acceptance.
- Main findings: Grounded Qwen2.5-Coder-23B reports WtdRPx=.493, NetRed=.276, and p50 first-feedback=59.79s. Grounded GPT-4o reports WtdRPx=.576 and NetRed=.285. Survey signals: clarity 4/5, grounding 3.38/5, adapt-or-accept ≈56%.

## 4. Evidence mapped to review questions
| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Grounding and structured context improve violation-reduction proxies over ungrounded settings. | Reported | Sections 4.1–5.1, Table 1 |
| RQ2 | Quantized on-prem serving provides sub-minute first feedback, but effectiveness is reported through recall proxies rather than precision. | Reported / limitation | Sections 4.3, 5.2–5.5 |
| RQ3 | Context trimming reduces tokens but harms recall proxies more than it improves latency. | Reported | Section 4.4 |
| RQ4 | PR-native delivery, provenance, policies, and caching support adoption; n=8 survey is directional only. | Reported / limitation | Sections 4.5, 5.6–5.7 |
| RQ5 | Grounding constrains comments to verifiable findings but leaves defects outside analyzer coverage unaddressed. | Inferred | Sections 2–5 |
| RQ6 | Evaluation should jointly report effectiveness, regressions, coverage, latency, cost, auditability, and acceptance. | Inferred | Sections 3.5–5.7 |

## 5. Failure and problematic-comment categories
| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Analyzer-bound blind spot | Defects outside the analyzer rule surface are not surfaced. | Limitation | Section 5.7 |
| Context omission | Token budgets or multi-file/macro-heavy cases omit semantics. | Limitation | Sections 4.4, 5.7 |
| Regression introduction | Generated fixes increase or introduce violations. | Evaluated failure | Sections 3.5, 4.1 |
| Weak rationale / hallucination | Ungrounded generation produces unsupported explanations. | Motivation | Sections 1–2 |
| Unmeasured false positive | Offline evaluation cannot observe dismissed comments or precision. | Measurement gap | Section 3.5 |

## 6. Evaluation dimensions and metrics
| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Violation reduction | Reduction, NetRed, severity-normalized reductions. | Grounded Qwen NetRed=.276; grounded GPT-4o NetRed=.285. | Table 1 |
| Coverage proxy | WtdRPx, MacRPx, CovFrac. | Qwen WtdRPx=.493/CovFrac=.772; GPT-4o=.576/.882. | Table 1 |
| Regression risk | IntroFrac and post-analysis increases. | Qwen=.596; GPT-4o=.603; precision unmeasured. | Table 1 |
| Latency | p50 total and first-feedback per hunk. | Qwen 59.81s total, 59.79s first feedback. | Table 1 |
| Human/workflow signal | Survey of eight participants. | Clarity 4/5, grounding 3.38/5, adapt-or-accept ≈56%; directional. | Section 4.5 |
| Resource efficiency | Quantization, one-GPU serving, caching. | Cache hits, GPU-hours, and energy not measured. | Sections 2.3, 5.3, 5.7 |

## 7. Mitigation and trade-offs
- Mitigation family: Evidence grounding, AST-guided context selection, and resource-aware serving.
- Intervention point: Context, prompts, deployment, caching, and audit logging.
- What it reduces: Unsupported rationale, hallucination, prompt bloat, and external data exposure.
- Useful feedback potentially lost: Analyzer-bound grounding suppresses novel issues; trimming can remove dependencies.
- Coverage effect: Better rule-local context, but no evidence for dynamic languages or analyzer-external defects.
- Human escalation effect: Suggestions are non-destructive, but acceptance/dismissal is not objectively instrumented.
- Computational/operational cost: Requires GPU, analyzer licenses, builds/re-analysis, and orchestration; cache benefits are unquantified.
- New failure modes: Analyzer coupling, patch regressions, omitted context, cache artifacts, and semantic regressions.

## 8. Annotation and evaluator validity
- Judge/annotator: Automated static analysis and build/re-analysis produce pre/post violation deltas; an internal survey provides perception signals.
- Rubric: Rule IDs, severity, violation counts, coverage, introductions, latency, and structured comments with provenance.
- Agreement/reliability: No inter-rater agreement; survey n=8 is explicitly directional.
- Validity checks: Pinned commits, replayable transformations, snapshot hashing, two-pass aggregation, and open/internal repository balance.
- Possible bias: Synthetic benchmark, MISRA/C/C++ concentration, analyzer coverage, offline patch application, and small internal survey.

## 9. Quality appraisal
| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | System goal and architecture explicit. |
| Q2 | 2 | Benchmark scale and codebases reported. |
| Q3 | 2 | Grounding, context, serving, and caching described. |
| Q4 | 2 | Reduction, coverage, regression, latency, and survey measures reported. |
| Q5 | 1 | Rule rubric clear; precision/comment correctness absent. |
| Q6 | 1 | Small survey; no agreement measure. |
| Q7 | 2 | Model/context configurations and ablations included. |
| Q8 | 1 | Offline synthetic benchmark and analyzer dependence limit validity. |
| Q9 | 2 | Grounding and serving interventions explicit. |
| Q10 | 2 | Latency and operational architecture measured. |
| Q11 | 2 | Threats and unmeasured failure modes discussed. |
| Q12 | 2 | Direct evidence concerns generated review comments. |
- Total: `21/24` provisional
- Quality interpretation: Strong systems-level trade-off evidence, with gaps in precision, acceptance, and independent production validation.

## 10. Review-process reliability and bias
- Missing data: Comment precision, dismissal rates, cache/GPU/energy cost, and longitudinal drift.
- Publication-bias concern: Purpose-built benchmark and author-reported results; independent replication not assessed.
- Selection uncertainty: Full text available; publisher relationship and final metadata unverified.
- Extraction uncertainty: Moderate because some outcomes are figure-based and offline patching differs from deployment.
- Second-reviewer agreement: Not available.
- Duplicate-publication handling: Check for a later venue/version before bibliography integration.

## 11. Synthesis-ready conclusion
- Contribution to the SLR: Shows how static-analysis grounding and resource-efficient serving can make PR-native LLM review more auditable and operationally feasible.
- What the paper does not establish: Comment precision, developer acceptance, broad language coverage, or semantic correctness beyond static-analysis deltas.
- Research gap supported: Evaluation needs regression risk, analyzer coverage, context loss, latency, resource cost, and human acceptance.
- Candidate synthesis claims: Grounding improves evidence alignment and recall proxies, but transfers analyzer blind spots and trades context richness against latency/cost.
- Follow-up verification needed: Verify artifact release, final publication metadata, and comment-level acceptance/precision data.
