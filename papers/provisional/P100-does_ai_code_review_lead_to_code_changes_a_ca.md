# P100 — Does AI Code Review Lead to Code Changes? A Case Study of GitHub Actions

> **Provisional intake record.** This is not a canonical paper note.

| Field | Value |
|---|---|
| Project ID | `P100` (provisional) |
| Citation key | `p100_sun2025_does_ai_code_review_lead_to_co` |
| Authors | Kexin Sun; Hongyu Kuang; Sebastian Baltes; Xin Zhou; He Zhang; Xiaoxing Ma; Guoping Rong; Dong Shao; Christoph Treude |
| Year | 2025 |
| Source | arXiv |
| arXiv | `2508.18771v2` |
| Screening tier | `core` |
| Reconciliation status | New candidate after initial local matching |
| Metadata status | local_arxiv_metadata |
| Evidence status | Full-text eligibility recorded; extraction not yet completed |

## 1. Identification

- Duplicate or companion publication: No publisher venue or DOI is reported; verify before final integration.

## 2. Screening
- Decision: `Include`; Relevance: `High`
- Decision rationale: Large-scale empirical study of AI review adoption, comment addressing, human comparison, and interpretable predictors in GitHub Actions.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: actionability / workflow impact / trade-off framework

## 3. Study overview
- Purpose: Measure whether AI-generated review comments lead to code changes and identify tool/comment factors associated with developer response.
- Research questions: Adoption/configuration (RQ1), AI versus human comment addressing (RQ2), and predictors of addressing (RQ3).
- Method: Mine GitHub Actions and pull requests, classify comment validity/addressing with a two-stage LLM framework, manually annotate a sample, then model predictors with Random Forest and SHAP.
- Evaluated system/artifact: 16 popular AI code-review GitHub Actions grouped into PR-, file-, and hunk-level tools.
- Dataset/benchmark: 718 matched repositories, 178 mature repositories, 22,326 AI comments; addressing dataset contains 5,652 comments (3,604 file-level AI, 882 hunk-level AI, 1,166 human) from 51 repositories.
- Input context: Review comment, original diff/hunk and line metadata, subsequent file changes to merge, repository/project features, trigger mode, model, author history, and comment text features.
- Main findings: 37.1% of matched repositories generated comments. In manual labels, addressed rates were 26% file-level AI, 36% hunk-level AI, and 80% human. Full-dataset estimates were 4.2%/19.2%/60.0% respectively for file-level AI, hunk-level AI, and human comments.

## 4. Evidence mapped to review questions
| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | AI review adoption is concentrated in a few tools; 178 repositories produced 22,326 comments, but many configured repositories showed no generated comments. | Reported | Section IV-A |
| RQ2 | Human comments are addressed more often than AI comments; hunk-level AI comments outperform file-level comments. | Reported | Section IV-B, Tables VI–IX |
| RQ3 | Addressing is associated with source/tool, trigger mode, comment conciseness, code snippets, and review granularity. | Reported | Section IV-C, Tables X–XI |
| RQ4 | A two-stage LLM classifier can scale addressing analysis, but human annotation remains necessary for validity calibration. | Inferred | Sections IV-B–C |
| RQ5 | Exact-line/file-change resolution is a behavioral proxy and can miss discussion, architectural, or non-code outcomes. | Limitation | Sections IV, VI |
| RQ6 | Tool evaluation should report adoption, comment validity, addressing, granularity, content specificity, and reviewer context jointly. | Inferred | Sections V–VI |

## 5. Failure and problematic-comment categories
| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Invalid/no-suggestion comment | Praise, summary, or comment with no actionable issue. | Annotation category | Section IV-B |
| General suggestion | Vague advice such as “test thoroughly” without concrete guidance. | Annotation category | Section IV-B |
| Valid but unaddressed | Specific issue/suggestion exists but no relevant later change occurs. | Outcome category | Section IV-B |
| Partially addressed | Some, but not all, identified issues are changed. | Outcome category | Section IV-B |
| Low-specificity/file-level feedback | Broad comments spanning files are less likely to trigger changes than hunk-level inline feedback. | Reported association | Sections IV-B, V |

## 6. Evaluation dimensions and metrics
| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Adoption | Configured repositories, mature repositories, generated comments, configuration changes. | 178 mature repos; 22,326 AI comments; 37.1% of matched repos generated comments. | Section IV-A |
| Human validity | None/General/Valid classification. | 150 comments manually annotated; validity separated from addressing. | Section IV-B |
| Addressing outcome | Valid-Uncertain, Unaddressed, Partially, Fully based on subsequent file changes. | Human 80% addressed in manual sample; hunk AI 36%; file AI 26%. | Table VI |
| LLM classification | OA and Macro-F1 for two-stage six-class labeling. | Best setup OA 86.1%, Macro-F1 74.6%; addressed-vs-other OA 91.5%, Macro-F1 89.8%. | Table VII |
| Agreement | Cohen’s kappa for human labels. | File κ=.674, hunk κ=.734, human κ=.764. | Section IV-B |
| Predictors | Random Forest, 5-fold CV, SHAP, binned addressing rates. | Comment source, manual trigger, conciseness, snippets, and hunk-level granularity are influential. | Section IV-C |

## 7. Mitigation and trade-offs
- Mitigation family: Concise, code-specific, manually triggered, hunk-level inline review design.
- Intervention point: Tool granularity, trigger policy, prompt/output format, and comment content.
- What it reduces: Broad low-specificity feedback, reviewer mapping effort, and low-actionability output.
- Useful feedback potentially lost: Optimizing for immediate code changes may suppress valuable design, explanation, or discussion feedback that does not alter the exact file/line.
- Coverage effect: Hunk-level comments improve localization/actionability but may miss cross-file or PR-level concerns.
- Human escalation effect: Findings support AI as a complement to human review; unresolved comments and ambiguous outcomes need human interpretation.
- Computational/operational cost: Large-scale GitHub mining, API reconstruction, LLM labeling, and five-run model evaluation are required; monetary cost is not reported.
- New failure modes: Language filtering, file-change proxy bias, tool/source confounding, and misclassification of general or multi-issue comments.

## 8. Annotation and evaluator validity
- Judge/annotator: Two authors and an external graduate student manually label comments; LLMs classify validity/addressing at scale.
- Rubric: Six-class annotation scheme distinguishing invalid/general/uncertain/unaddressed/partial/full addressing.
- Agreement/reliability: κ=.674 file-level, .734 hunk-level, .764 human; LLM model selection uses annotated samples and five repeated runs.
- Validity checks: Consensus guide on nine comments, 150-comment independent sample, third-author adjudication, best-model selection, and SHAP cross-validation.
- Possible bias: English-only filtering, exact-file-change proxy, GitHub Actions/tool selection, repository maturity, and source/model confounding.

## 9. Quality appraisal
| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | RQs and mining scope explicit. |
| Q2 | 2 | Repositories/comments and filtered samples reported. |
| Q3 | 2 | Two-stage labeling and predictor modeling described. |
| Q4 | 2 | Adoption, addressing, agreement, OA/Macro-F1, and SHAP reported. |
| Q5 | 2 | Validity/addressing rubric clearly defined. |
| Q6 | 2 | Human agreement and adjudication reported. |
| Q7 | 2 | AI sources, human comparison, repeated model runs, and CV included. |
| Q8 | 1 | Observational design and proxy outcome limit causal validity. |
| Q9 | 2 | Tool design factors are analyzed, though not experimentally manipulated. |
| Q10 | 1 | Operational data collection described; monetary cost absent. |
| Q11 | 2 | Filtering, proxy, selection, and generalization threats discussed. |
| Q12 | 2 | Direct evidence concerns real generated review comments and changes. |
- Total: `22/24` provisional
- Quality interpretation: Strong large-scale behavioral evidence, with observational and measurement-proxy limitations.

## 10. Review-process reliability and bias
- Missing data: Developer intent, acceptance rationale, time-to-resolution, comment dismissal, and monetary/API cost.
- Publication-bias concern: Tool/repository selection and GitHub-visible activity may overrepresent mature or successful projects.
- Selection uncertainty: Full text available; final publisher metadata unverified.
- Extraction uncertainty: Moderate because some predictor details and full distributions are table/figure dependent.
- Second-reviewer agreement: Not available for this note.
- Duplicate-publication handling: Check for a later venue/version before final bibliography integration.

## 11. Synthesis-ready conclusion
- Contribution to the SLR: Provides rare large-scale evidence linking AI review comment characteristics to subsequent code changes in real repositories.
- What the paper does not establish: It does not establish causal effects, comment correctness beyond sampled labels, or usefulness without code modification.
- Research gap supported: Actionability evaluation should distinguish validity, partial/full addressing, discussion value, source/tool effects, and exact-change proxies.
- Candidate synthesis claims: Concise, code-specific hunk-level comments are more likely to trigger changes, while human feedback remains more frequently addressed; this is an association, not a causal guarantee.
- Follow-up verification needed: Inspect released mining/annotation scripts, verify tool coverage, and examine how non-code outcomes and multi-file comments are treated.
