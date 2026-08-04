# P105 — Automated Code Review Using Large Language Models at Ericsson: An Experience Report

> **Provisional intake record.** This is not a canonical paper note.

| Field | Value |
|---|---|
| Project ID | `P105` (provisional) |
| Citation key | `p105_ramesh2025_automated_code_review_using_la` |
| Authors | Shweta Ramesh; Joy Bose; Hamender Singh; A K Raghavan; Sujoy Roychowdhury; Giriprasad Sridhara; Nishrith Saini; Ricardo Britto |
| Year | 2025 |
| Source | arXiv |
| arXiv | `2507.19115v2` |
| Screening tier | `core` |
| Reconciliation status | New candidate after initial local matching |
| Metadata status | local_arxiv_metadata |
| Evidence status | Full-text eligibility recorded; extraction not yet completed |

## 1. Identification

- Duplicate or companion publication: No publisher venue or DOI is reported; verify before final integration.

## 2. Screening
- Decision: `Include`; Relevance: `High`
- Decision rationale: Industrial experience report describing an LLM/static-analysis code-review tool, expert evaluation, model comparison, and workflow adoption at Ericsson.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: context quality / workflow impact / efficiency trade-off

## 3. Study overview
- Purpose: Reduce senior-developer review burden using a lightweight, secure, workflow-integrated LLM review assistant.
- Research questions: Review quality (RQ1), best model among smaller open LMs (RQ2), and practical tool effectiveness/adoption (RQ3).
- Method: Retrieve Java diffs from Gerrit, extract enclosing methods with static analysis, prompt open LLMs, post-process/summarize reviews, and collect expert surveys and usage feedback.
- Evaluated system/artifact: Ericsson web/plugin tool using Llama-family models and static program analysis; compared Llama 2 13B, Code Llama 13B, Llama 2 7B, and Code Llama 7B.
- Dataset/benchmark: Java changes from Ericsson code repositories; RQ1 uses 10 review examples, RQ2 uses 36 pairwise evaluations by nine experts, and RQ3 surveys nine developers. Five change IDs are used for targeted behavior/time checks.
- Input context: Modified Java lines plus the enclosing method/function; prompts target concise, relevant, human-like comments without generated code.
- Main findings: Experts found positive, neutral, and negative quality signals; Code Llama 13B appeared strongest in pairwise comparison. Four of nine developers said the tool saved time; generation took roughly 5–6 seconds for short snippets and about 6 seconds on average.

## 4. Evidence mapped to review questions
| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Expert feedback suggests contextual prompts improve relevance, but comments can still be verbose, irrelevant, or factually incorrect. | Reported | Section VI-A |
| RQ2 | Code Llama 13B was preferred in the small pairwise comparison over other 7B/13B models. | Reported | Section VI-B, Table II |
| RQ3 | Tool adoption is preliminary: four of nine reported time savings, two used it regularly, and five sometimes. | Reported | Section VI-C |
| RQ4 | Enclosing-method context and static analysis provide a lightweight mitigation for diff-only hallucination. | Inferred | Sections II, V |
| RQ5 | Small expert samples and self-reported usage do not establish production correctness or causal productivity benefit. | Limitation | Section VII |
| RQ6 | Industrial evaluation should combine contextual grounding, expert correctness/relevance, adoption, and latency. | Inferred | Sections V–VII |

## 5. Failure and problematic-comment categories
| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Irrelevant feedback | Comment focuses on areas unrelated to changed code or task. | Reported feedback | Section VI-C |
| Factual incorrectness | Generated review contains claims experts identify as wrong. | Reported feedback | Section VI-C |
| Verbosity | Review is too long or insufficiently concise for workflow use. | Reported feedback | Section VI-A |
| Random context hallucination | Naive prompting invents function names/objects or drifts from enclosing method. | Motivation/target failure | Sections I–II |
| Missed changed-line focus | Tool does not remain tied to modified code lines. | Target validation | Section VII |

## 6. Evaluation dimensions and metrics
| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Expert quality | Qualitative relevance, accuracy, and usability judgments on 10 reviews. | Mixed positive/neutral/negative feedback; exact aggregate unavailable. | Section VI-A |
| Model preference | Pairwise expert comparison across four models. | 9 experts × 4 comparisons = 36 evaluations; Code Llama 13B appeared best. | Section VI-B |
| Adoption/usefulness | Developer survey on time saved, effectiveness, deficiencies, frequency. | 4/9 time saved; 2 regular, 5 sometimes; 4 reported factual errors, 3 irrelevance. | Section VI-C |
| Context adherence | Manual check over five change IDs for comments focused on changed lines. | Procedure reported; aggregate result not clearly tabulated. | Section VII |
| Latency | Generation time per change/snippet. | Approximately 5–6 seconds; short snippets similar. | Section VII |
| Cost/operations | Lightweight open-source models and local workflow integration. | Avoids external API/fine-tuning costs; exact infrastructure cost absent. | Sections I, VII |

## 7. Mitigation and trade-offs
- Mitigation family: Static-analysis enclosing-method extraction, prompt engineering, review summarization/ranking, and human feedback recalibration.
- Intervention point: Input context, prompt/output constraints, post-processing, and workflow integration.
- What it reduces: Diff-only context errors, irrelevant/random comments, verbosity, and cognitive burden.
- Useful feedback potentially lost: Restricting comments to changed lines or concise outputs can omit cross-method/system-level concerns.
- Coverage effect: Enclosing-method context improves local semantics but does not provide full repository/inter-procedural context.
- Human escalation effect: Tool is positioned as developer assistance; experts remain the oracle and adoption is optional.
- Computational/operational cost: Lightweight models and 5–6 second generation support low latency; maintenance/prompt calibration cost is not measured.
- New failure modes: Model-specific variability, prompt brittleness, context truncation, and unvalidated comments reaching developers.

## 8. Annotation and evaluator validity
- Judge/annotator: Experienced Ericsson developers and experts evaluate quality, pairwise preference, and practical usefulness.
- Rubric: Relevance, accuracy, usability, time saved, effectiveness, missing qualities, usage frequency, and line adherence.
- Agreement/reliability: No formal inter-rater agreement is reported; pairwise/sample sizes are small.
- Validity checks: Multiple prompts, models, expert comparisons, workflow integration, and targeted line-adherence/time checks.
- Possible bias: Single-company Java context, self-reported adoption, small convenience samples, and author-developed tool/prompts.

## 9. Quality appraisal
| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | System and practical questions explicit. |
| Q2 | 1 | Industrial context described, but dataset size/details limited. |
| Q3 | 2 | Pipeline, context extraction, prompts, and models described. |
| Q4 | 1 | Qualitative/survey and latency results; aggregate quality metrics limited. |
| Q5 | 1 | Human rubric informal and incompletely quantified. |
| Q6 | 0 | No formal agreement statistic. |
| Q7 | 1 | Small model comparison and prompt variants. |
| Q8 | 1 | Single-company, small samples, self-report bias. |
| Q9 | 2 | Context/prompt/post-processing interventions described. |
| Q10 | 2 | Latency and lightweight deployment considerations reported. |
| Q11 | 2 | Accuracy, relevance, adoption, and context risks discussed. |
| Q12 | 2 | Direct industrial generated-review evidence. |
- Total: `17/24` provisional
- Quality interpretation: Useful experience evidence for lightweight context grounding, but preliminary and weakly quantified.

## 10. Review-process reliability and bias
- Missing data: Exact dataset/PR counts, aggregate ratings, correctness agreement, usage telemetry, and cost.
- Publication-bias concern: Positive experience report from the tool’s developers and organization.
- Selection uncertainty: Full text available; publisher metadata unverified.
- Extraction uncertainty: High-to-moderate because many results are qualitative and sample sizes are small.
- Second-reviewer agreement: Not available for this note.
- Duplicate-publication handling: Check for later venue/version before final bibliography integration.

## 11. Synthesis-ready conclusion
- Contribution to the SLR: Provides an industrial case showing that enclosing-method context and lightweight prompt engineering can yield fast, usable review assistance without expensive fine-tuning.
- What the paper does not establish: It does not establish reliable correctness, broad adoption, or replacement of expert review.
- Research gap supported: Experience reports need reproducible datasets, formal human agreement, comment-level correctness, and longitudinal adoption metrics.
- Candidate synthesis claims: Local context grounding can improve practical relevance at low latency, but small expert studies reveal persistent irrelevance and factual-error risks.
- Follow-up verification needed: Obtain exact prompt/model configurations, anonymized evaluation data, aggregate ratings, and longer-term usage outcomes.
