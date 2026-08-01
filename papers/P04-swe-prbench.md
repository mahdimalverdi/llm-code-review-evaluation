# P04 — SWE-PRBench: Benchmarking AI Code Review Quality Against Pull Request Feedback

> [!NOTE]
> This note follows the v2 framework-coding template. This paper is central to our context-quality argument because it reports that adding more context can degrade LLM-based code review performance.

## Completion Checklist

- [x] Bibliographic fields are filled.
- [x] Dataset/study details are filled as far as the paper allows.
- [x] Evaluation methods and metrics are described.
- [x] Human/LLM-judge validation protocol is documented as far as available.
- [x] Evaluation dimensions are separated from problematic comment types.
- [x] Context-quality evidence is extracted.
- [x] Trade-offs are explicitly identified.
- [x] Mapping to our RQs is included.

## Status

- Paper ID: `P04`
- Analysis status: `First pass completed; migrated to v2 template; needs PDF-level verification`
- Priority: `High`
- Reading depth: `Read once + metadata verified`
- Last updated: `2026-05-08`
- Confidence in extraction: `Medium`

## Proposal RQ Mapping

| Proposal RQ | Relevance and evidence |
|---|---|---|
| RQ1 | **High.** Reports missed human issues, fabricated issues, unmatched plausible issues, and context-induced failures. |
| RQ2 | **High.** Compares diff-only, diff-plus-file, and fuller-context conditions; context expansion can degrade performance. |
| RQ3 | **High.** Focuses on issue detection/coverage and judge comparison; usefulness, actionability, workflow impact, and cost are limited. |
| RQ4 | **High but partial.** Supports context-richness versus noise/attention trade-offs; does not measure useful-feedback preservation or escalation. |
| RQ5 | **High.** Directly treats context amount/type and benchmark validity, but annotation difficulty needs further verification. |
| RQ6 | **High.** Supports PR-centric benchmark design, context-quality dimensions, and evaluator-validity analysis. |

---

## 1. Bibliographic Information

| Field | Value |
|---|---|
| Title | SWE-PRBench: Benchmarking AI Code Review Quality Against Pull Request Feedback |
| Authors | Deepak Kumar |
| Year | 2026 |
| Venue / Source | arXiv preprint / benchmark paper |
| Publication type | Benchmark + empirical evaluation |
| Link | arXiv / Hugging Face paper page |
| DOI / arXiv | arXiv:2603.26130 |
| Code / artifact | Reported: dataset, contexts, annotations, and evaluation harness are public |

### Citation Note

- [x] This paper should be cited in the final report.
- [x] Citation key checked against `references/references.bib`.
- [x] Canonical BibTeX entry exists in `references/references.bib`.

```bibtex
```

## 2. One-Sentence Summary

> SWE-PRBench introduces a 350-PR benchmark for evaluating whether AI code review systems detect human-flagged review issues and reports that frontier models detect only a minority of issues while performance degrades as more context is added.

## 3. Main Goal of the Paper

### Focus Area

- [x] LLM-based code review generation
- [x] Code review comment evaluation
- [ ] Hallucination / unsupported claims
- [x] Context quality / context selection
- [x] LLM-as-a-judge
- [x] Human annotation / human evaluation
- [ ] User study / reviewer behavior
- [ ] Industrial deployment
- [x] Benchmark construction
- [ ] Cost / latency / operational trade-off
- [ ] Filtering / gating / aggregation

### Goal

The paper builds a PR-level benchmark to test whether AI reviewers can detect issues that human reviewers flagged, under different context configurations.

### Notes

This paper is critical because it challenges the naive assumption that more context improves review quality. It supports our claim that context must be evaluated by quality, not just size.

## 4. Research Questions of the Paper

| RQ | Text | Status |
|---|---|---|
| RQ1 | How well do AI models identify issues human reviewers flagged in PR feedback? | `Reported / Inferred` |
| RQ2 | How do frontier models perform on PR-level review quality? | `Reported / Inferred` |
| RQ3 | How does context amount/type affect AI code review performance? | `Reported` |
| RQ4 | Can LLM-as-Judge compare generated comments against human PR feedback? | `Reported` |

## 5. Dataset / Study Context

| Field | Value |
|---|---|
| Dataset / study name | SWE-PRBench |
| Dataset / study source | Pull requests from active open-source repositories with human review feedback |
| Dataset / study size | 350 pull requests, filtered from 700 candidates using Repository Quality Score |
| Number of repositories / projects | Not fully verified |
| Programming languages | Not fully verified |
| Repository type | Open-source / PR-based repositories |
| Input context available | `config_A`: diff only; `config_B`: diff + file content; `config_C`: full context |
| Output being evaluated | Generated review comments or issue detections matched against human PR feedback |
| Time period | Not reported in this pass |
| Data availability | Public dataset, contexts, annotations, and evaluation harness |

### Dataset / Study Validity Notes

- [x] Realistic PR-level benchmark.
- [x] Has human review feedback.
- [x] Includes actual PRs.
- [x] Ground truth may be incomplete.
- [x] Context configurations are explicitly controlled.
- [ ] Needs PDF-level verification.

### Important Notes

Human PR feedback is realistic but incomplete. A model comment that does not match human feedback may still be useful, and a human comment may be subjective or stylistic.

## 6. Methods, Models, or Systems Studied

| Field | Value |
|---|---|
| Models / systems | Eight frontier models; exact list needs verification |
| Prompting strategy | Evaluation under three frozen context configurations |
| Retrieval or context selection | Central variable: diff-only, diff+file, full context; structured semantic context such as AST/function and import graph reported |
| Post-generation verification | LLM-as-Judge matching against human PR feedback |
| Static analysis or rule-based checks | Context construction uses structured extraction, but not main evaluation target |
| Human-in-the-loop component | Human review feedback used as reference; no live human-in-loop deployment |
| Filtering / gating / aggregation mechanism | Judge-based matching, not deployment-time gate |
| Other mechanisms | Repository quality filtering, issue-type analysis, context ablations |

### Method Checklist

- [x] Evaluates generated review comments/issue detections.
- [x] Evaluates LLM-as-Judge matching.
- [ ] Evaluates aggregation.
- [x] Compares multiple LLMs.
- [x] Compares context settings.
- [x] Uses structured context configurations.
- [ ] Includes production/workflow evidence.

## 7. Evaluation Method

| Field | Value |
|---|---|
| Automatic metrics | Issue detection / recall-like measures, composite score, judge labels |
| Human evaluation / user study | Human PR feedback as benchmark reference; judge validation with human agreement |
| Qualitative analysis | Discusses context-induced degradation and Type2_Contextual collapse |
| Statistical analysis | Reports top model tiers and mean score ranges |
| Cost / latency / time evaluation | Limited; context cost not deeply quantified |
| Reproducibility materials | Publicly released benchmark/evaluation harness |

### Evaluation Validity Checklist

- [x] Beyond BLEU/ROUGE.
- [x] Checks semantic correspondence to human feedback.
- [ ] Separately checks grounding/context alignment.
- [x] Indirectly checks usefulness via human-flagged issues.
- [x] Partially checks actionability.
- [x] Partially checks fabricated/hallucinated issues.
- [x] Measures missed issues.
- [ ] Measures useful-feedback preservation.
- [ ] Measures cost/latency in detail.
- [ ] Includes live workflow signals.

## 8. Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Technical correctness | `Partially` | Matching human issues approximates correctness. |
| Relevance to code change | `Yes` | PR-level review target. |
| Grounding / context alignment | `Partially` | Judge matching and context configurations, but not claim grounding. |
| Usefulness | `Partially` | Human feedback as proxy. |
| Actionability | `Partially` | Part of judge scoring, not fully isolated. |
| Specificity | `Partially` | Concrete PR feedback encourages specificity. |
| Novelty / non-triviality | `Partially` | Human-flagged issues are meaningful targets. |
| Hallucination / unsupported claim | `Partially` | Fabricated/unmatched issues. |
| False positive rate | `Partially` | Extra/unmatched comments may be false positives, but ground truth incomplete. |
| False negative rate | `Yes` | Missed human-flagged issues central. |
| Preservation of useful comments | `No / Partially` | Not a filtering paper. |
| Wrong removal of useful comments | `No` | Not evaluated. |
| Review coverage / issue coverage | `Yes` | Core benchmark objective. |
| Human escalation rate | `No` | Not evaluated. |
| Human annotation cost | `Not reported` | Not central. |
| Computational cost | `Not central` | Not central. |
| Latency | `Not central` | Not central. |
| Reviewer time overhead | `No` | Not live user study. |
| Operational complexity | `No` | Not deployment paper. |
| Trade-off analysis | `Partially` | Context expansion vs performance degradation. |
| Developer trust | `No` | Not studied. |
| Workflow impact | `No` | Not production study. |

## 9. Problematic Comment Types / Error Taxonomy

### Explicitly Defined Error Types

- Type1 direct issues visible in diff.
- Type2 contextual issues requiring same-file context.
- Type3 latent/cross-file issues.
- Confirmed issues.
- Plausible but unmatched issues.
- Fabricated/hallucinated issues.

### Inferred Error Types

- `Inferred`: Missed human-flagged issue.
- `Inferred`: Context-induced failure.
- `Inferred`: Over-contextualized review output.
- `Inferred`: Generic/low-signal feedback.
- `Inferred`: False positive due to incomplete ground truth.
- `Inferred`: Attention-dilution failure.

### Example Problematic Comments

| Type | Example / Paraphrase | Source | Label |
|---|---|---|---|
| Missed issue | Model fails to identify a human-flagged issue. | Benchmark objective/results | `Reported` |
| Context-induced failure | Model performs worse when file/full context is added. | Context ablation | `Reported` |
| Fabricated issue | Model produces a fabricated review concern. | Judge label scheme | `Reported` |
| Plausible unmatched issue | Model produces a plausible issue outside human ground truth. | Judge labels | `Reported` |

### Taxonomy Checklist

- [x] Hallucinated or unsupported claim
- [x] Context-misaligned comment
- [x] Factually incorrect comment
- [ ] Wrong API/type assumption
- [ ] Wrong-location comment
- [x] Irrelevant comment
- [x] Out-of-scope comment
- [x] Vague or generic comment
- [ ] Non-actionable comment
- [ ] Redundant comment
- [ ] Low-value nitpick
- [ ] Style-only comment with poor practical value
- [x] Comment that misses the actual issue
- [x] Comment that depends on missing project context
- [x] Technically plausible but unsupported comment
- [ ] Comment with poor value-to-time ratio

### Does the Paper Separate Correctness, Usefulness, and Actionability?

- Answer: `Partially`
- Explanation: Quality is mostly operationalized through match to human PR feedback and judge scoring; constructs are partly collapsed.

## 10. Context-Quality Extraction

| Context Dimension | Coverage | Evidence / Notes |
|---|---|---|
| Relevance | `Partially` | Configs vary context amount/type; relevance not separately scored. |
| Completeness | `Yes / Partially` | Richer configs intended to provide more evidence. |
| Specificity / focus | `Yes` | Diff-only vs richer context explicitly tests focus. |
| Consistency | `Not reported` | Not central. |
| Groundability | `Partially` | Judge labels, but not evidence-span grounding. |
| Locality | `Yes / Partially` | Type2 contextual issues require same-file context. |
| Freshness | `Not reported` | Not central. |
| Attention load | `Yes` | Degradation with richer context supports attention/noise concern. |
| Cost / token budget | `Partially` | Context expansion implies cost, not deeply measured. |
| Context availability vs usability | `Yes` | More context available but less usable by models. |

### Context Failure Types

- [x] Missing surrounding code
- [x] Missing cross-file dependency
- [ ] Missing language/framework/version context
- [ ] Irrelevant retrieved context
- [x] Excessive context / attention dilution
- [ ] Contradictory PR metadata and diff
- [x] Unsupported inference from partial context
- [x] Generated claim not grounded in provided context

## 11. Trade-off Extraction

| Strategy / Mechanism | Benefit | Risk / Cost | Missing Metric |
|---|---|---|---|
| More context | More evidence for contextual/cross-file issues. | Performance degradation, attention dilution, cost. | Marginal value of added context. |
| Diff-only context | Focused and cheaper. | Misses contextual issues. | Context sufficiency score. |
| Full context | Realistic and information-rich. | Noise and lower performance. | Useful-context ratio. |
| LLM-as-Judge | Scales semantic matching. | Judge bias and matching errors. | Judge calibration by issue type. |
| Human PR feedback ground truth | Realistic reference. | Incomplete and subjective. | Ground-truth completeness estimate. |

### Trade-off Notes

P04 is one of the strongest empirical supports for our claim that context quality is not the same as context quantity.

## 12. Human Annotation / User Study / Production Protocol

| Field | Value |
|---|---|
| Human annotators / participants | Human PR reviewers provide original feedback; judge validated against human agreement |
| Number of annotators / participants | Benchmark has 350 human-annotated PRs; exact annotator count not verified |
| Expertise | Original software reviewers/developers; validation annotators need verification |
| Guideline or study protocol provided | Judge rubric/labels should be checked in PDF |
| Pilot phase | Not verified |
| Inter-rater agreement / validation reported | Yes |
| Agreement metric used | Kappa = 0.75 for judge validation |
| Conflict resolution method | Not verified |
| Production/workflow signal | No live production signal |

### Protocol Quality Checklist

- [ ] Independent annotation verified.
- [ ] At least two annotators verified.
- [x] SE expertise through PR review context.
- [x] Judge rubric partially described.
- [x] Agreement reported.
- [ ] Conflict resolution verified.
- [ ] Live workflow signal included.

### Main Concerns About Validity

Human PR feedback is realistic but incomplete; judge matching can hide semantic or construct-validity errors.

## 13. Key Findings

| Finding | Summary | Evidence / Metric | Importance for us |
|---|---|---|---|
| F1 | Provides PR-level benchmark. | 350 human-annotated PRs. | Benchmark realism. |
| F2 | Frontier models detect only minority of issues. | 15–31% in diff-only config. | Caution on model capability. |
| F3 | More context degrades performance. | All eight models degrade across richer contexts. | Core context-quality evidence. |
| F4 | Type2 contextual detection collapses with expansion. | Reported issue-type drop. | Attention/noise hypothesis. |
| F5 | LLM-as-Judge supports scalable evaluation. | Kappa = 0.75. | Methodology evidence. |

## 14. Limitations from the Paper’s Own Perspective

- Human PR feedback is realistic but incomplete/subjective.
- Judge-based evaluation may not perfectly capture usefulness.
- Results depend on repositories, PRs, models, prompts, and context configs.
- Benchmark performance may not translate to workflow impact.

## 15. Limitations from Our Perspective

- Human comments as ground truth may miss valid AI comments.
- Focuses on recall/matching more than full taxonomy.
- Does not separate correctness, usefulness, actionability, and preference.
- Cost/latency/human verification effort underdeveloped.
- Shows extra context can hurt but does not provide full context-quality model.

## 16. Relevance to Our Paper

### Useful For

- [x] Related work
- [x] Motivation / research gap
- [x] Evaluation framework
- [x] Taxonomy of problematic comments
- [x] Context-quality argument
- [x] Hallucination / unsupported-claim discussion
- [x] Human annotation / user-study protocol
- [x] Cost / latency / operational trade-off
- [ ] Industrial or live validation
- [x] Benchmark selection
- [x] Methodology design
- [x] Discussion / threats to validity

### Mapping to Our RQs

| Our RQ | Relevance | Evidence |
|---|---|---|
| RQ1 — problematic comments | `Medium` | Missed issues, fabricated issues, plausible unmatched issues. |
| RQ2 — context quality | `High` | More context worsens performance; config comparison. |
| RQ3 — evaluation dimensions | `High` | Issue coverage and judge labels. |
| RQ4 — trade-offs | `High` | Context richness vs attention/noise/performance. |
| RQ5 — framework design | `High` | Context-quality dimension must be explicit. |

### Explanation

SWE-PRBench is direct evidence that context expansion must be evaluated, not assumed beneficial.

## 17. Extracted Evidence for Our Argument

| Argument Need | Evidence | Label |
|---|---|---|
| Limitations of current evaluations | Need for PR-level human-feedback benchmark. | `Reported` |
| Missing cost/latency/reviewer-overhead analysis | Quality/context effects measured, cost not deeply quantified. | `Our perspective` |
| Missing actionability/usefulness distinction | Human-feedback matching collapses correctness/usefulness/actionability. | `Our perspective` |
| Need for problematic-comment taxonomy | Missed, fabricated, unmatched, context-induced failures. | `Inferred` |
| Need for human annotation / user-study quality control | Human feedback and judge matching require validation. | `Reported / Our perspective` |
| Need for context-quality evaluation | Richer context degrades performance. | `Reported` |
| Need for trade-off-aware evaluation | Context expansion adds evidence but can reduce quality. | `Reported / Our perspective` |
| Need for useful-feedback preservation metric | Not measured. | `Our perspective` |

## 18. Legacy Quality Appraisal (superseded by the canonical record)

| Criterion | Score | Evidence note |
|---|---:|---|
| Q1 goal/questions clear | 2 | Benchmark and context questions are stated. |
| Q2 artifact specified | 2 | Benchmark, models, contexts, and judging setup are identified. |
| Q3 dataset/context described | 2 | PR sample and context conditions are reported. |
| Q4 procedure understandable | 2 | Issue matching and context comparisons are described. |
| Q5 dimensions/metrics defined | 2 | Issue detection and judge metrics are reported. |
| Q6 failure categories reported | 2 | Missed, fabricated, unmatched, and context-induced failures are reported. |
| Q7 judging protocol described | 1 | Human-reference and judge validation are present but need PDF-level detail. |
| Q8 reliability/validity checks | 1 | Kappa/judge validation is reported in the existing extraction; exact protocol needs verification. |
| Q9 mitigation evaluated | 1 | Context conditions are compared, but no deployment mitigation is evaluated. |
| Q10 trade-offs measured | 1 | Context-performance trade-off is measured; cost and preservation are not. |
| Q11 limitations/threats | 1 | Some benchmark/judge limitations are discussed. |
| Q12 direct SLR support | 2 | Strong direct support for RQ1, RQ2, RQ4, RQ5, and RQ6. |
| **Total** | **19/24** | **High-quality core evidence with protocol details to verify.** |

### Evidence boundary correction

P04 supports issue-coverage and context-condition analysis. It should not be cited as evidence for production usefulness, human escalation, computational cost, or preservation of useful comments.

## 19. Final Assessment

| Field | Value |
|---|---|
| Overall relevance to our study | `High` |
| Should we cite this paper? | `Yes` |
| Priority for deep reading | `High` |
| Confidence in this analysis | `Medium` |

### Short Justification

This paper is crucial because it empirically challenges naive context expansion and supports context-quality as a first-class evaluation object.

## Open Questions for Follow-up Reading

- [ ] What is the exact model list?
- [ ] What is the exact performance drop by config/model?
- [ ] How is LLM-as-Judge validated?
- [ ] What are exact issue labels and definitions?
- [ ] How does judge handle semantically related but differently phrased comments?

## Follow-up TODOs

- [ ] Verify arXiv PDF/BibTeX.
- [ ] Verify model list and context configs.
- [ ] Extract cite-worthy statements.
- [ ] Add BibTeX.
- [ ] Update synthesis if deep reading changes coding.

<details>
<summary>Scratchpad</summary>

- Strongest use: more context can hurt.
- Important contrast with P05/P06: full/enriched context may be needed, but quality/filtering matters.

</details>
## Canonical citation record

Use citation key `p04_kumar2026_swe_prbench` from `references/references.bib`; do not duplicate its BibTeX entry in this note.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative for synthesis and quality scoring. Earlier compact/legacy appraisal material is retained only for provenance.

### 1. Identification

- Project ID: P04; citation key: `p04_kumar2026_swe_prbench`.
- Source: local full PDF; included after full-text screening; no local duplicate identified.

### 2. Screening and proposal alignment

- Decision: Include; Core; High relevance.
- Rationale: PR-level benchmark with explicit context configurations, issue taxonomy, judge validation, detection, and false-positive measurement.
- Deliverables: evaluation framework, context-quality model, and trade-off analysis.

### 3. Study overview

SWE-PRBench contains 350 PRs selected from 700 candidates. It defines repository-quality and review-value filters, three context configurations, a difficulty taxonomy, and an LLM-judge protocol for matching generated findings to human review issues (Sections 3–6).

### 4. Evidence mapped to proposal RQ1–RQ6

| RQ | Evidence and interpretation | Type | Location |
|---|---|---|---|
| RQ1 | Missed human issues, fabricated findings, plausible unmatched findings, and context-induced errors are reported. | Reported | Sections 5.2, 6.4 |
| RQ2 | Detection rate, FPR, issue matching, difficulty categories, and judge agreement operationalize correctness/coverage. | Reported | Sections 5.2–5.5, 6 |
| RQ3 | Context configuration is a before-generation intervention; benchmark/judge design is post-generation evaluation. | Reported/Inferred | Sections 4–5 |
| RQ4 | All evaluated models degrade as context expands from configuration A to C, showing a context-versus-noise/attention trade-off. | Reported | Sections 6.3–6.5; Figure 2 |
| RQ5 | PR selection, contamination mitigation, incomplete human ground truth, and judge validation are treated explicitly. | Reported | Sections 3.1–3.6, 5.4–5.5 |
| RQ6 | Direct benchmark and context-quality evidence; limited workflow/usefulness evidence. | Our perspective | Sections 3–6 |

### 5. Failure and problematic-comment categories

| Category | Definition/example | Type | Location |
|---|---|---|---|
| Missed issue | Model fails to recover a human-identified review issue. | Reported | Section 6 |
| Fabricated issue | Generated finding is unsupported by the PR. | Reported | Section 6.4 |
| Plausible unmatched issue | Potentially valid finding lacks human-reference support. | Reported | Judge rubric, Section 5.2 |
| Context-induced failure | Additional context reduces detection or increases confusion. | Reported | Sections 6.3–6.5 |

### 6. Evaluation dimensions and metrics

| Dimension | Operationalization | Result/limitation | Location |
|---|---|---|---|
| Issue detection/coverage | Match against human review issues | Human ground truth may be incomplete | Sections 5.2–5.3 |
| False positives | FPR for unsupported findings | Judge-dependent classification | Sections 5.2, 6 |
| Context sensitivity | Performance across A/B/C configurations | More context consistently degrades models | Sections 4, 6.3 |
| Judge validity | Rubric κ=0.75 and cross-judge validation | Substantial, not perfect agreement | Sections 5.4–5.5 |

### 7. Mitigation and trade-offs

- Mitigation: controlled context selection before generation and rubric-based evaluation after generation.
- Reduces: irrelevant context exposure and unstructured issue matching.
- Useful feedback potentially lost: narrower contexts may omit cross-file evidence; not directly measured.
- Coverage: detection rate reported; human escalation: not reported.
- Cost: repository context and judging increase tokens/compute; full cost accounting not reported.
- New failures: context overload and judge disagreement.

### 8. Annotation and evaluator validity

- Judge/annotator: human PR feedback as reference plus validated LLM judge.
- Rubric: issue-match classifications and scoring formula.
- Reliability: κ=0.75 and cross-judge validation reported.
- Bias: incomplete human issue set, repository selection, and judge dependence.

### 9. Quality appraisal

| Criterion | Score | Evidence note |
|---|---:|---|
| Q1 | 2 | Benchmark goals and evaluation questions are explicit. |
| Q2 | 2 | Benchmark, agents, and judge artifact are specified. |
| Q3 | 2 | PR selection, taxonomy, and configurations are detailed. |
| Q4 | 2 | Reproducibility section and protocol are provided. |
| Q5 | 2 | Detection, FPR, scoring, and context comparisons are defined. |
| Q6 | 2 | Miss/fabrication/context failures are reported. |
| Q7 | 2 | Section 5.2 specifies the fixed judge, three-label rubric, matching constraints, thresholds, and released rubric. |
| Q8 | 2 | Section 5.4 reports κ=0.75 on a blind stratified sample; Section 5.5 reports 78.7% cross-judge agreement and κ=0.616. |
| Q9 | 2 | Three controlled context configurations are evaluated as a before-generation intervention. |
| Q10 | 2 | The A>B>C context degradation and associated detection/FPR behavior directly measure a context-versus-noise trade-off, although preservation and deployment cost remain absent. |
| Q11 | 1 | Threats are discussed with residual benchmark limitations. |
| Q12 | 2 | Direct support for RQ1, RQ2, RQ4–RQ6. |

- Total: 23/24; high-quality core benchmark evidence with incomplete human-reference ground truth.

### 10. Review-process reliability and bias

- Missing data: developer usefulness, escalation, end-to-end cost, and complete alternative-issue validation.
- Publication bias: benchmark/model selection may favor accessible agents.
- Selection uncertainty: low; extraction uncertainty: medium for ground-truth completeness.
- Second reviewer unavailable; no duplicate identified.

### 11. Synthesis-ready conclusion

- Contribution: direct evidence that context quantity is not equivalent to context quality.
- Does not establish: production usefulness or useful-feedback preservation.
- Candidate claim: context interventions should report both issue coverage and false-positive behavior under controlled configurations.
- Follow-up: verify final metadata and benchmark release details.
