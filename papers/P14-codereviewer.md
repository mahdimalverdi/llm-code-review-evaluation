# P14 — CodeReviewer: Automating Code Review Activities by Large-Scale Pre-training

> [!NOTE]
> This note follows the v2 framework-coding template. P14 is foundational for our paper because CodeReviewer is the baseline/dataset/model that many later LLM-based code review papers compare against. It also introduces a large multilingual code-review dataset, diff-hunk-level tasks, BLEU-based evaluation, and a human evaluation that explicitly recognizes BLEU as insufficient for review-comment generation.

## Completion Checklist

- [x] Bibliographic fields are filled.
- [x] Dataset/study details are filled from the PDF.
- [x] Evaluation methods and metrics are described.
- [x] Human annotation / validation protocol is documented as far as the paper reports.
- [x] Evaluation dimensions are separated from problematic comment types.
- [x] Context-quality evidence is extracted.
- [x] Trade-offs are explicitly identified.
- [x] Mapping to our RQs is included.
- [x] Open questions and follow-up TODOs are listed.

## Status

- Paper ID: `P14`
- Analysis status: `First pass completed from PDF; needs citation/BibTeX cleanup`
- Priority: `High`
- Reading depth: `Read once from PDF`
- Last updated: `2026-05-12`
- Confidence in extraction: `High`

## Our Research Questions

| RQ | Question | Relevance of this paper |
|---|---|---|
| RQ1 | What types of problematic comments appear in LLM-generated code review? | Moderate: gives examples of generic, irrelevant, low-information, and low-relevance comments, but does not define a full harmful-comment taxonomy. |
| RQ2 | How is context quality defined, used, or ignored? | Strong foundational evidence: uses diff hunks and special diff tags as the main context representation, but omits broader PR/project context. |
| RQ3 | Which evaluation dimensions are covered or missing? | Strong for early evaluation practice: BLEU, information, relevance, quality estimation F1, and code-refinement EM; weak on correctness/actionability/harm. |
| RQ4 | What trade-offs arise from filtering/gating/evaluation? | Strong for benchmark construction trade-offs: hunk-level simplification, single earliest comment, noisy human-comment ground truth, and BLEU-vs-human-eval mismatch. |
| RQ5 | What should our framework include? | Supports baseline/history section, metric-validity critique, data-quality layer, and context-granularity discussion. |

---

## 1. Bibliographic Information

| Field | Value |
|---|---|
| Title | Automating Code Review Activities by Large-Scale Pre-training |
| Authors | Zhiyu Li, Shuai Lu, Daya Guo, Nan Duan, Shailesh Jannu, Grant Jenks, Deep Majumder, Jared Green, Alexey Svyatkovskiy, Shengyu Fu, Neel Sundaresan |
| Year | 2022 |
| Venue / Source | ESEC/FSE 2022 |
| Publication type | Foundational model + dataset + benchmark paper |
| Link | arXiv / ACM |
| DOI / arXiv | DOI: 10.1145/3540250.3549081; arXiv:2203.09095 |
| Code / artifact | Code/model/data released under Microsoft CodeBERT/CodeReviewer repository |

### Citation Note

- [x] This paper should be cited in the final report.
- [ ] Citation format has been checked.
- [ ] BibTeX entry has been collected.

```bibtex
% TODO: Paste BibTeX here after checking ACM BibTeX.
```

## 2. One-Sentence Summary

> This paper introduces CodeReviewer, a code-review-specific encoder-decoder pre-trained model and multilingual dataset for code change quality estimation, review comment generation, and code refinement, establishing a major baseline and benchmark for later automated code review research.

## 3. Main Goal of the Paper

### Focus Area

- [x] LLM/pre-trained-model-based code review generation
- [x] Code review comment evaluation
- [ ] Hallucination / unsupported claims
- [x] Context quality / context selection
- [ ] LLM-as-a-judge
- [x] Human annotation / human evaluation
- [ ] User study / reviewer behavior
- [ ] Industrial deployment
- [x] Benchmark construction
- [x] Cost / latency / operational trade-off
- [ ] Filtering / gating / aggregation

### Goal

The paper aims to automate three code review activities through large-scale pre-training on code review data: detecting code changes that need review, generating review comments, and refining code according to review comments.

### Notes

P14 is not a modern LLM evaluation paper, but it is necessary for our related-work baseline because many later papers use CodeReviewer, its dataset, or its evaluation setup.

## 4. Research Questions of the Paper

| RQ | Text | Status |
|---|---|---|
| RQ1 | How does CodeReviewer perform on code change quality estimation? | `Reported` |
| RQ2 | How does CodeReviewer perform on review generation? | `Reported` |
| RQ3 | How does CodeReviewer perform on code refinement? | `Reported` |
| RQ4 | What role does each pre-training task play in CodeReviewer? | `Reported` |
| RQ5 | Can multilingual dataset benefit model performance on understanding a single programming language? | `Reported` |

## 5. Dataset / Study Context

| Field | Value |
|---|---|
| Dataset / study name | CodeReview / CodeReviewer dataset |
| Dataset / study source | GitHub pull requests from high-quality open-source projects |
| Dataset / study size | Pre-training: 1,161 projects, ~7.933M PRs, 463.2GB metadata/data, ~4.311M code changes without comments, ~2.481M code changes with comments; benchmark: quality estimation ~266k train / ~31k valid / ~31k test; review generation ~118k train / ~10k valid / ~10k test; code refinement ~150k train / ~13k valid / ~13k test |
| Number of repositories / projects | 1,161 projects in pre-training dataset |
| Programming languages | Python, Java, Go, C++, JavaScript, C, C#, PHP, Ruby |
| Repository type | Popular GitHub open-source repositories with permissive redistribution licenses and large PR volume |
| Input context available | Diff hunks with special diff tags; code refinement uses source code plus review comment |
| Output being evaluated | Quality-estimation label, generated review comment, refined code |
| Time period | Not extracted in first pass |
| Data availability | Released with code/model according to paper |

### Dataset / Study Validity Notes

- [x] Large multilingual GitHub dataset.
- [x] Project-level split to reduce leakage.
- [x] Diff-hunk-level representation.
- [x] Separate benchmark datasets for three tasks.
- [x] Human evaluation for review generation.
- [x] Explicitly acknowledges dataset quality variation and filters low-quality comments.
- [ ] Open-source-only dataset may not generalize to industrial projects.
- [ ] Only earliest comment per diff hunk is retained when multiple comments exist.
- [ ] Single-comment modeling loses multi-reviewer and multi-perspective context.
- [ ] Commented code changes are treated as suspicious/positive labels; this may be noisy.

### Important Notes

This paper is important for our critique of “human comments as ground truth.” It uses human comments as reference data, but also recognizes that review comments are diverse, non-unique, and sometimes not well captured by BLEU.

## 6. Methods, Models, or Systems Studied

| Field | Value |
|---|---|
| Models / systems | CodeReviewer; Transformer baseline; T5 for code review; CodeT5; qualitative Codex/Copilot comparison |
| Prompting strategy | Not a prompting paper |
| Retrieval or context selection | Not a RAG paper; uses diff hunk as core context unit |
| Post-generation verification | No explicit post-generation judge/filter |
| Static analysis or rule-based checks | No static-analysis integration; relies on learned diff/comment patterns |
| Human-in-the-loop component | 6 professional programmers score generated comments on information and relevance |
| Filtering / gating / aggregation mechanism | Dataset filtering/cleaning; no deployment-time gate |
| Other mechanisms | Four pre-training tasks: Diff Tag Prediction, Denoising Code Diff, Denoising Review Comment, Review Comment Generation |

### Method Checklist

- [x] Evaluates generated review comments.
- [ ] Evaluates a deployment-time judge/filter/gate.
- [ ] Evaluates aggregation.
- [x] Compares model variants and baselines.
- [x] Uses code-review-specific pre-training.
- [x] Includes diff-aware input representation.
- [x] Includes human evaluation.
- [ ] Includes production/workflow evidence.

## 7. Evaluation Method

| Field | Value |
|---|---|
| Automatic metrics | Quality estimation: precision, recall, F1, accuracy; review generation: BLEU-4; code refinement: BLEU and exact match |
| Human evaluation / user study | 6 professional programmers score 100 selected Java/Python samples on information and relevance using 1–5 scale |
| Qualitative analysis | Examples comparing T5, CodeT5, Codex/Copilot, and CodeReviewer comments |
| Statistical analysis | Not emphasized in first pass |
| Cost / latency / time evaluation | Training cost implied: pre-training with 2 DGX-2 servers, 32 V100-32G GPUs total, 250k steps; no deployment cost/latency metric |
| Reproducibility materials | Dataset/code/model released according to paper |

### Evaluation Validity Checklist

- [x] Uses automatic metrics.
- [x] Uses human evaluation for review generation.
- [x] Evaluates information.
- [x] Evaluates relevance.
- [x] Discusses BLEU unsuitability for review generation.
- [x] Uses exact match for code refinement.
- [x] Uses project-level split.
- [ ] Measures correctness separately for comments.
- [ ] Measures actionability separately.
- [ ] Measures hallucination/unsupported claims.
- [ ] Measures live acceptance/adoption.
- [ ] Measures false-positive/false-negative consequences of generated comments.

## 8. Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Technical correctness | `Partially` | Quality estimation and code refinement evaluate correctness indirectly; comment correctness not separately labeled. |
| Relevance to code change | `Yes` | Human evaluation includes relevance. |
| Grounding / context alignment | `Partially` | Diff-aware input and special tags support grounding in changed lines, but no claim-level grounding. |
| Usefulness | `Partially / Yes` | Information score measures how informative comments are for revision. |
| Actionability | `Partially` | Information score partially captures whether a comment helps the contributor revise code. |
| Specificity | `Partially` | Diff-hunk focus gives some specificity; no explicit specificity metric. |
| Novelty / non-triviality | `No / Partially` | Not central. |
| Hallucination / unsupported claim | `No / Partially` | Codex examples show unmeaningful comments, but hallucination is not framed as a metric. |
| False positive rate | `Partially` | Quality-estimation precision/recall covers whether a diff needs review, but not generated-comment false positives. |
| False negative rate | `Partially` | Quality-estimation recall covers missed comment-needing diffs. |
| Preservation of useful comments | `No` | Not a filtering/gating paper. |
| Wrong removal of useful comments | `No` | Not applicable. |
| Review coverage / issue coverage | `Partially` | Diff-hunk-level design and quality estimation, but no issue-level coverage. |
| Human escalation rate | `No` | Not a production system. |
| Human annotation cost | `Partially` | 6 programmers evaluate 100 samples; cost not quantified. |
| Computational cost | `Yes / Partially` | Pre-training infrastructure is substantial. |
| Latency | `No` | Not reported. |
| Reviewer time overhead | `No / Partially` | Motivation discusses reducing reviewer burden, but no live time-saving metric. |
| Operational complexity | `Yes / Partially` | Dataset collection, cleaning, pre-training, and multilingual modeling are complex. |
| Trade-off analysis | `Yes / Partially` | Hunk-level simplification, BLEU limits, dataset noise, training cost, multilingual benefits. |
| Developer trust | `No` | Not measured directly. |
| Workflow impact | `No` | Not live deployment. |

## 9. Problematic Comment Types / Error Taxonomy

### Explicitly Defined Error Types

The paper does not define a formal problematic-comment taxonomy, but it gives signals for several weak comment types:

- `Low-information comment`: e.g., comments like “why do we need this?” are less informative than direct suggestions like “declare this variable as private.”
- `Low-relevance comment`: comments unrelated to the code change or disobeying the code-change logic get low relevance scores.
- `Generic meaningless comment`: Codex/Copilot can copy examples or generate generic comments such as “I think this is a good idea.”
- `Reference-mismatch under BLEU`: predicted comment can convey similar intent to ground truth but receive low BLEU due to wording differences.
- `Incorrect refinement`: generated code can be lexically similar but fail exact match, potentially causing compile/execution problems.

### Inferred Error Types

- `Inferred`: Comment that focuses on unchanged context rather than changed lines.
- `Inferred`: Comment that is plausible but not tied to the actual diff.
- `Inferred`: Human reference incompleteness due to retaining only earliest comment.
- `Inferred`: Multi-reviewer perspective loss.
- `Inferred`: Noisy positive/negative labels in quality estimation.

### Example Problematic Comments

| Type | Example / Paraphrase | Source | Label |
|---|---|---|---|
| Generic meaningless comment | Codex output: “I think this is a good idea.” | Figure 5 | `Reported / Short quote` |
| Low-information comment | “Why do we need this?” is given as less informative than a direct fix suggestion. | Evaluation metrics discussion | `Reported / Paraphrased` |
| Generic T5 output | T5 generates broad comments such as “I don’t think this change is needed.” | Figure 5 | `Reported / Paraphrased` |
| Contextually useful despite BLEU mismatch | CodeReviewer generates a comment with similar intent to ground truth but different wording, lowering BLEU. | RQ2 discussion / Figure 5 | `Reported / Paraphrased` |

### Taxonomy Checklist

- [x] Hallucinated or unsupported claim
- [x] Context-misaligned comment
- [x] Factually incorrect comment
- [ ] Wrong API/type assumption
- [ ] Wrong-location comment
- [x] Irrelevant comment
- [x] Out-of-scope comment
- [x] Vague or generic comment
- [x] Non-actionable comment
- [ ] Redundant comment
- [x] Low-value nitpick
- [x] Style-only comment with poor practical value
- [x] Comment that misses the actual issue
- [x] Comment that depends on missing project context
- [x] Technically plausible but unsupported comment
- [x] Comment with poor value-to-time ratio

### Does the Paper Separate Correctness, Usefulness, and Actionability?

- Answer: `Partially`
- Explanation: P14 separates information and relevance for generated comments, but does not separately label correctness, usefulness, actionability, hallucination, or harmfulness. Its evaluation is an important early step but incomplete for our framework.

## 10. Context-Quality Extraction

| Context Dimension | Coverage | Evidence / Notes |
|---|---|---|
| Relevance | `Yes / Partially` | Diff hunk focuses model on changed lines and avoids reviewing unchanged context. |
| Completeness | `Partially` | Hunk-level context includes surrounding unchanged lines but omits broader PR/project context. |
| Specificity / focus | `Yes` | Special [ADD], [DEL], [KEEP] tags help distinguish changed and unchanged lines. |
| Consistency | `Partially` | Project-level split helps evaluation consistency; no output consistency metric. |
| Groundability | `Partially` | Diff format ties comments to changed code, but no formal claim-to-line grounding. |
| Locality | `Yes` | Hunk-level modeling is local by design. |
| Freshness | `Not central` | Not central. |
| Attention load | `Partially` | Hunk-level representation reduces input length and avoids full-file complexity. |
| Cost / token budget | `Yes / Partially` | Hunk-level design reduces large-file processing; training cost is high. |
| Context availability vs usability | `Yes` | Diff-aware representation is more usable than raw before/after code for review tasks. |

### Context Failure Types

- [x] Missing project context
- [x] Missing language/framework/version context
- [x] Missing surrounding code
- [x] Missing cross-file dependency
- [ ] Irrelevant retrieved context
- [x] Excessive context / attention dilution
- [x] Generated/comment claim not grounded in code diff
- [x] Unsupported inference from partial context
- [x] Ambiguous relationship between diff and comment

## 11. Trade-off Extraction

| Strategy / Mechanism | Benefit | Risk / Cost | Missing Metric |
|---|---|---|---|
| Diff-hunk-level modeling | Keeps input focused and tractable; aligns with review comments on changed code. | Loses PR-level, file-level, cross-hunk, and project context. | Needed-context coverage and cross-hunk dependency coverage. |
| Keeping earliest comment per hunk | Simplifies one-input/one-output modeling. | Removes multiple perspectives and later clarifications. | Multi-comment coverage / lost useful feedback. |
| Human comment as reference | Realistic source of review signal. | Human comments are diverse, incomplete, and noisy. | Reference completeness and alternate-valid-comment rate. |
| BLEU evaluation | Scalable automatic metric. | Not suitable for diverse/non-unique review comments; penalizes semantically valid rewrites. | Human correlation and semantic issue coverage. |
| Human information/relevance scoring | Captures more useful dimensions than BLEU. | Small sample and limited dimensions. | Correctness, actionability, severity, and inter-rater agreement. |
| Large-scale pre-training | Improves downstream code-review tasks. | High compute/data cost; not always feasible for projects. | Quality-per-compute and project-specific transfer. |
| Multilingual training | Improves monolingual performance and broad applicability. | May still miss project-specific conventions. | Language/project-specific generalization. |

### Trade-off Notes

P14 gives us a foundation for arguing that code-review evaluation has long been aware of metric limitations, but later work still often inherits BLEU-style evaluation and single-reference benchmark assumptions. It also shows why hunk-level benchmarks are useful but incomplete.

## 12. Human Annotation / User Study / Production Protocol

| Field | Value |
|---|---|
| Human annotators / participants | Yes |
| Number of annotators / participants | 6 professional sophisticated programmers |
| Expertise | Professional programmers |
| Guideline or study protocol provided | Partially; information and relevance metrics described; detailed appendix not extracted in first pass |
| Pilot phase | Not reported in first pass |
| Inter-rater agreement / validation reported | Not extracted in first pass |
| Agreement metric used | Not extracted in first pass |
| Conflict resolution method | Not extracted in first pass |
| Production/workflow signal | No live production signal |

### Protocol Quality Checklist

- [x] Human evaluation is used.
- [x] Professional programmers are involved.
- [x] Information and relevance are defined.
- [ ] Correctness is separately annotated.
- [ ] Actionability is separately annotated.
- [ ] Inter-rater agreement is reported in extracted text.
- [ ] Live workflow signal included.

### Main Concerns About Validity

The human evaluation improves over BLEU, but it is still limited to information and relevance on 100 selected Java/Python samples. It does not fully answer whether comments are correct, actionable, harmful, or accepted by developers in workflow.

## 13. Key Findings

| Finding | Summary | Evidence / Metric | Importance for us |
|---|---|---|---|
| F1 | CodeReviewer pre-training dataset covers 1,161 projects and ~7.933M PRs across 9 languages. | Table 2. | Foundational dataset scale. |
| F2 | Review generation benchmark has ~118k train, ~10k validation, ~10k test samples. | Table 3. | Baseline benchmark source. |
| F3 | CodeReviewer improves quality estimation over Transformer, T5, and CodeT5. | F1 71.53, accuracy 73.89 in Table 4. | Early review-quality prediction evidence. |
| F4 | CodeReviewer achieves BLEU 5.32 on review generation, outperforming baselines but still below 10. | Table 5 / RQ2. | Shows task difficulty and BLEU limits. |
| F5 | Human information/relevance scores improve over baselines: information 3.60, relevance 3.20. | Table 5. | Human-eval dimensions. |
| F6 | CodeReviewer achieves code-refinement BLEU 82.61 and EM 30.32. | Table 6. | Review-to-fix connection. |
| F7 | Diff Tag Prediction and Denoising Code Diff are important for code change understanding. | Table 7. | Context/diff representation evidence. |
| F8 | Multilingual dataset improves monolingual performance on Java/C#/Ruby. | Table 8. | Data scale/language transfer. |
| F9 | The paper states BLEU is not suitable for review generation and therefore adds human evaluation. | Threats to validity / metric section. | Direct support for our metric-validity argument. |

## 14. Limitations from the Paper’s Own Perspective

- More hyperparameter tuning could improve results.
- Dataset is collected from GitHub open-source projects, not industrial projects.
- Code review often involves multiple reviewers and perspectives, but the dataset retains only a single comment for a code change.
- BLEU is not suitable for review generation because comments are diverse and non-unique.

## 15. Limitations from Our Perspective

- Human comments are treated as reference ground truth despite incompleteness and noise.
- Retaining only earliest comment loses dialogue and multi-perspective feedback.
- Hunk-level representation misses PR-level intent, cross-file dependencies, and project-specific context.
- Human evaluation lacks correctness, actionability, harmfulness, and downstream acceptance labels.
- Large-scale pre-training cost is high and may not transfer to organization-specific rules.
- The quality-estimation label assumption—commented means suspicious, uncommented means correct—is noisy.

## 16. Relevance to Our Paper

### Useful For

- [x] Related work
- [x] Motivation / research gap
- [x] Evaluation framework
- [x] Taxonomy of problematic comments
- [x] Context-quality argument
- [ ] Hallucination / unsupported-claim discussion
- [x] Human annotation / user-study protocol
- [x] Cost / latency / operational trade-off
- [ ] Industrial or live validation
- [x] Benchmark selection
- [x] Methodology design
- [x] Discussion / threats to validity

### Mapping to Our RQs

| Our RQ | Relevance | Evidence |
|---|---|---|
| RQ1 — problematic comments | `Medium` | Low-information, low-relevance, generic, and meaningless comments. |
| RQ2 — context quality | `High` | Diff-hunk representation and diff tags are an early context-quality design. |
| RQ3 — evaluation dimensions | `High` | BLEU, information, relevance, precision/recall/F1, EM. |
| RQ4 — trade-offs | `High` | Hunk-level simplification, BLEU limits, dataset noise, compute cost, single-reference assumptions. |
| RQ5 — framework design | `High` | Provides baseline/history and motivates richer evaluation. |

### Explanation

P14 should be cited as the foundational CodeReviewer paper and as an early source that already recognized BLEU’s weakness for review comment generation. It also helps us explain why later work built on incomplete benchmark assumptions.

## 17. Extracted Evidence for Our Argument

| Argument Need | Evidence | Label |
|---|---|---|
| Need for metric-validity analysis | The paper explicitly says BLEU is not suitable for review generation and adds human evaluation. | `Reported` |
| Need for context-quality evaluation | CodeReviewer uses diff hunks and special diff tags to focus on changed lines. | `Reported` |
| Need for data-quality layer | The paper acknowledges dataset quality varies and filters low-quality comments. | `Reported` |
| Need for reference-ground-truth caution | Multiple comments on a hunk are collapsed to the earliest one, losing perspectives. | `Reported / Our perspective` |
| Need for human-centered dimensions | Information and relevance are evaluated by professional programmers. | `Reported` |
| Need for cost-aware evaluation | Large-scale pre-training uses substantial GPU resources. | `Reported` |
| Need for PR/project context | Hunk-level modeling simplifies review but loses broader context. | `Our perspective` |

## 18. Final Assessment

| Field | Value |
|---|---|
| Overall relevance to our study | `High` |
| Should we cite this paper? | `Yes` |
| Priority for deep reading | `High for background; Medium for framework novelty` |
| Confidence in this analysis | `High` |

### Short Justification

P14 is foundational rather than directly aligned with our final contribution. It is necessary for the related-work baseline, benchmark-history discussion, and critique of BLEU/single-reference evaluation in code review comment generation.

## Open Questions for Follow-up Reading

- [ ] Does the supplementary appendix define information/relevance rubrics in detail?
- [ ] Are inter-rater agreement statistics available for the human evaluation?
- [ ] What exact filtering rules were used to remove low-quality comments?
- [ ] How many comments were discarded by data cleaning?
- [ ] How often does retaining only the earliest comment lose useful alternatives?
- [ ] Can the CodeReviewer dataset be reused to illustrate our taxonomy categories?

## Follow-up TODOs

- [ ] Verify ACM BibTeX.
- [ ] Add exact CodeReviewer artifact link.
- [ ] Update `synthesis/evaluation-dimensions.md` with information/relevance and BLEU criticism.
- [ ] Update `synthesis/context-quality.md` with diff-hunk-level representation and special diff tags.
- [ ] Update `synthesis/problematic-comment-taxonomy.md` with low-information and low-relevance comments.
- [ ] Update `synthesis/trade-off-framework.md` with hunk-level simplification, single-reference ground truth, and compute-cost trade-offs.
- [ ] Update `matrices/cross-paper-synthesis.md` with P14 evidence.

<details>
<summary>Scratchpad</summary>

- Strongest use: baseline/history and metric-validity.
- Good bridge from P13: P13 uses CodeReviewer dataset and baseline; P14 explains where that baseline/dataset comes from.
- Important caution: CodeReviewer is foundational, but its evaluation assumptions are exactly what our paper should critique and extend.

</details>
