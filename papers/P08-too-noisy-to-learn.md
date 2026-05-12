# P08 — Too Noisy To Learn: Enhancing Data Quality for Code Review Comment Generation

> [!NOTE]
> This note follows the v2 framework-coding template. P08 is central for our data-quality and problematic-comment taxonomy because it studies noisy code review comments such as vague and non-actionable feedback and shows that cleaning training data can improve generated review-comment quality.

## Completion Checklist

- [x] Bibliographic fields are filled.
- [x] Dataset/study details are filled as far as the paper allows in first pass.
- [x] Evaluation methods and metrics are described.
- [x] Human annotation / validation protocol is documented.
- [x] Evaluation dimensions are separated from problematic comment types.
- [x] Context-quality evidence is extracted.
- [x] Trade-offs are explicitly identified.
- [x] Mapping to our RQs is included.
- [x] Open questions and follow-up TODOs are listed.

## Status

- Paper ID: `P08`
- Analysis status: `First pass completed; needs PDF-level verification`
- Priority: `High`
- Reading depth: `Read once from metadata/public abstract + source row + public excerpts`
- Last updated: `2026-05-08`
- Confidence in extraction: `Medium`

## Our Research Questions

| RQ | Question | Relevance of this paper |
|---|---|---|
| RQ1 | What types of problematic comments appear in LLM-generated code review? | Strong evidence for noisy, vague, non-actionable, low-value, and unclear comments as harmful training/evaluation samples. |
| RQ2 | How is context quality defined, used, or ignored? | Uses code diff + natural-language comment context to classify valid/noisy comments; supports semantic context-aware cleaning. |
| RQ3 | Which evaluation dimensions are covered or missing? | Strong on relevance, clarity, constructiveness, actionability, informativeness; weaker on live workflow impact and reviewer overhead. |
| RQ4 | What trade-offs arise from filtering/gating/evaluation? | Cleaning removes noise but reduces training data size and may remove borderline useful comments. |
| RQ5 | What should our framework include? | Supports explicit data-quality layer and useful-feedback preservation when filtering noisy comments. |

---

## 1. Bibliographic Information

| Field | Value |
|---|---|
| Title | Too Noisy To Learn: Enhancing Data Quality for Code Review Comment Generation |
| Authors | Chunhua Liu, Hong Yi Lin, Patanamon Thongtanunam |
| Year | 2025 |
| Venue / Source | MSR 2025 / arXiv |
| Publication type | Empirical study + data-quality improvement + dataset cleaning |
| Link | arXiv / MSR 2025 |
| DOI / arXiv | DOI: 10.1109/MSR66628.2025.00043; arXiv:2502.02757 |
| Code / artifact | Not verified in this pass |

### Citation Note

- [x] This paper should be cited in the final report.
- [ ] Citation format has been checked.
- [ ] BibTeX entry has been collected.

```bibtex
% TODO: Paste BibTeX here after checking IEEE/arXiv BibTeX.
```

## 2. One-Sentence Summary

> This paper studies noisy comments in code review comment generation datasets and shows that LLM-based semantic data cleaning can identify valid review comments and improve the informativeness and relevance of generated comments after fine-tuning on cleaned data.

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
- [ ] Benchmark construction
- [x] Cost / latency / operational trade-off
- [x] Filtering / gating / aggregation

### Goal

The paper investigates how noisy review comments in training datasets affect review comment generation and proposes an LLM-based semantic cleaning approach to identify valid comments and remove noisy ones.

### Notes

This paper is highly relevant because it treats data quality as a first-order cause of low-quality generated comments. It also provides concrete definitions for valid and noisy comments, which can feed directly into our taxonomy and evaluation framework.

## 4. Research Questions of the Paper

| RQ | Text | Status |
|---|---|---|
| RQ1 | Can LLMs effectively identify valid and noisy comments in code review datasets? | `Reported / Inferred` |
| RQ2 | How does semantic data cleaning affect the performance of review comment generation models? | `Reported` |
| RQ3 | Does semantic data cleaning improve the quality of generated review comments? | `Reported` |
| RQ4 | What trade-off exists between retaining valid comments and reducing dataset size? | `Inferred from paper motivation` |

## 5. Dataset / Study Context

| Field | Value |
|---|---|
| Dataset / study name | CodeReviewer benchmark dataset; manually labeled test subsets; Tufano et al. labeled subset |
| Dataset / study source | Large-scale open-source code review dataset used for review comment generation |
| Dataset / study size | Public excerpts report a manually labeled sample of 371 comments plus a 355-comment Tufano subset, combined into 726 samples with 452 valid and 274 noisy comments; training set size and full cleaning pipeline need PDF verification |
| Number of repositories / projects | Not verified in first pass |
| Programming languages | Not verified in first pass |
| Repository type | Open-source code review data |
| Input context available | Code diff and corresponding human review comment |
| Output being evaluated | Valid/noisy label for review comments; generated comments from models trained on original vs cleaned datasets |
| Time period | Not reported in first pass |
| Data availability | Dataset source is public/benchmark-based; exact released artifacts need verification |

### Dataset / Study Validity Notes

- [x] Realistic code review dataset.
- [x] Includes human-written review comments.
- [x] Includes code diff + comment context.
- [x] Includes manual labels for valid/noisy comments.
- [ ] Includes live developer reactions.
- [x] Ground truth may be subjective because validity/actionability can be ambiguous.
- [x] Needs PDF-level verification.

### Important Notes

The paper’s core contribution is not just better generation; it shows that many training examples are semantically noisy, and that quality of training data affects generated review-comment quality. This directly supports our argument that evaluation must include data quality and not only model output quality.

## 6. Methods, Models, or Systems Studied

| Field | Value |
|---|---|
| Models / systems | CodeReviewer and CodeT5 variants trained on original and cleaned datasets; LLMs used for noisy/valid classification, including GPT-3.5 and Llama 3 in public excerpts |
| Prompting strategy | LLM prompt classifies comments as valid or noisy using code diff + review comment and criteria such as relevance, clarity, constructiveness, and focus on improvement |
| Retrieval or context selection | Not a retrieval paper; uses diff/comment pair as classification context |
| Post-generation verification | Generated comments evaluated automatically and manually for informativeness and relevance |
| Static analysis or rule-based checks | Prior heuristic/ML cleaning is discussed as insufficient; proposed cleaning is semantic/LLM-based |
| Human-in-the-loop component | Manual labeling and manual quality evaluation of generated comments |
| Filtering / gating / aggregation mechanism | Dataset-level filter retaining predicted valid comments for training cleaned models |
| Other mechanisms | Fine-tuning generation models on cleaned vs original datasets |

### Method Checklist

- [x] Evaluates generated review comments.
- [x] Evaluates a judge/filter/gate at dataset-cleaning level.
- [ ] Evaluates aggregation.
- [x] Compares model variants trained on original vs cleaned data.
- [x] Uses context-aware semantic classification.
- [x] Includes post-generation quality evaluation.
- [x] Includes human annotation/evaluation.
- [ ] Includes production/workflow evidence.

## 7. Evaluation Method

| Field | Value |
|---|---|
| Automatic metrics | Precision for detecting valid comments; BLEU and similarity to valid human-written comments; model comparison before/after cleaning |
| Human evaluation / user study | Manual labeling of valid/noisy comments; manual evaluation of 300 generated comments for informativeness and relevance |
| Qualitative analysis | Valid/noisy definitions and examples; quality comparison between original and cleaned models |
| Statistical analysis | Wilcoxon signed-rank tests reported in public excerpts; Cohen’s Kappa for annotation agreement |
| Cost / latency / time evaluation | Not central; cleaning reduces data size and uses LLM calls, but operational cost is not the main focus |
| Reproducibility materials | Needs PDF/artifact verification |

### Evaluation Validity Checklist

- [x] Beyond BLEU/ROUGE alone.
- [x] Checks semantic validity of review comments.
- [x] Checks relevance to code change.
- [x] Checks clarity/constructiveness/actionability.
- [ ] Explicitly checks hallucination/unsupported claims.
- [x] Measures false positives/precision for valid-comment detection.
- [x] Partially measures false negatives through valid/noisy labels, but first-pass details need verification.
- [x] Measures effect of filtering on generation quality.
- [ ] Measures useful-feedback preservation in full detail.
- [ ] Measures deployment cost/latency.
- [ ] Includes live workflow signals.

## 8. Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Technical correctness | `Partially` | Valid comments should improve code, but correctness is not the only focus. |
| Relevance to code change | `Yes` | Explicit criterion for valid/noisy classification. |
| Grounding / context alignment | `Partially / Yes` | Classification uses diff + comment context; not full claim grounding. |
| Usefulness | `Yes / Partially` | Valid comments should contribute to code improvement. |
| Actionability | `Yes` | Valid comments require direct and applicable action. |
| Specificity | `Partially` | Valid comments should explicitly express issues/actions; specificity should be verified. |
| Novelty / non-triviality | `Partially` | Noisy comments include low-value/vague feedback; novelty not central. |
| Hallucination / unsupported claim | `Partially` | Noisy comments may be factually poor, but hallucination is not central. |
| False positive rate | `Partially / Yes` | Precision of valid-comment detection. |
| False negative rate | `Partially` | Needs verification; missing valid comments is possible. |
| Preservation of useful comments | `Partially` | Cleaning retains predicted valid comments; risk of discarding useful comments exists but needs deeper analysis. |
| Wrong removal of useful comments | `Partially` | Implied by data-cleaning trade-off, not fully central. |
| Review coverage / issue coverage | `No / Partially` | Not a PR issue-coverage benchmark. |
| Human escalation rate | `No` | Not evaluated. |
| Human annotation cost | `Partially` | Manual labeling discussed; exact cost not central. |
| Computational cost | `Partially` | LLM cleaning calls imply cost; not central. |
| Latency | `Not central` | Not central. |
| Reviewer time overhead | `No` | Not live reviewer study. |
| Operational complexity | `Partially` | Dataset cleaning pipeline, not deployment workflow. |
| Trade-off analysis | `Partially` | Cleaning improves quality but reduces training data size. |
| Developer trust | `No` | Not studied. |
| Workflow impact | `No` | Not production study. |

## 9. Problematic Comment Types / Error Taxonomy

### Explicitly Defined Error Types

The paper distinguishes valid comments from noisy comments.

Valid comments should:

- request direct and explicit code changes;
- aim to improve source code;
- explicitly express issues;
- clearly outline necessary actions;
- be relevant to the submitted code diff.

Noisy comments are comments that do not request direct and applicable actions to refine the code.

### Inferred Error Types

- `Inferred`: Vague comment.
- `Inferred`: Non-actionable comment.
- `Inferred`: Low-value nitpick.
- `Inferred`: Comment without clear improvement target.
- `Inferred`: Comment not grounded in the code diff.
- `Inferred`: Ambiguous natural-language review comment.
- `Inferred`: Noisy training sample that causes low-quality generation.

### Example Problematic Comments

| Type | Example / Paraphrase | Source | Label |
|---|---|---|---|
| Vague/non-actionable | Comment gives unclear feedback without direct applicable action. | Paper definition | `Reported / Paraphrased` |
| Low-value nitpick | Comment asks for trivial formatting with limited practical value. | Related examples / paper framing | `Reported / Inferred` |
| Ambiguous comment | Comment requires semantic understanding of code and language to classify. | Paper motivation | `Reported / Paraphrased` |
| Noisy training sample | Human-written review comment remains noisy after heuristic cleaning. | Paper motivation | `Reported` |

### Taxonomy Checklist

- [ ] Hallucinated or unsupported claim
- [x] Context-misaligned comment
- [ ] Factually incorrect comment
- [ ] Wrong API/type assumption
- [ ] Wrong-location comment
- [x] Irrelevant comment
- [x] Out-of-scope comment
- [x] Vague or generic comment
- [x] Non-actionable comment
- [x] Redundant comment
- [x] Low-value nitpick
- [x] Style-only comment with poor practical value
- [x] Comment that misses the actual issue
- [x] Comment that depends on missing project context
- [x] Technically plausible but unsupported comment
- [x] Comment with poor value-to-time ratio

### Does the Paper Separate Correctness, Usefulness, and Actionability?

- Answer: `Partially`
- Explanation: The paper strongly separates actionability and relevance through valid/noisy definitions. However, correctness, usefulness, and actionability are partly bundled into the valid-comment concept.

## 10. Context-Quality Extraction

| Context Dimension | Coverage | Evidence / Notes |
|---|---|---|
| Relevance | `Yes` | Valid comments must be relevant to the code diff. |
| Completeness | `Partially` | Uses diff/comment context, not full project context. |
| Specificity / focus | `Yes / Partially` | Valid comments should express issues and actions clearly. |
| Consistency | `Partially` | Comment should align with submitted code change. |
| Groundability | `Partially` | Comment validity judged with code diff; not full claim grounding. |
| Locality | `Partially` | Diff-level context, not line-level verification. |
| Freshness | `Not reported` | Not central. |
| Attention load | `Not reported` | Not central. |
| Cost / token budget | `Partially` | LLM cleaning cost implied, not central. |
| Context availability vs usability | `Yes / Partially` | Semantic understanding of code diff + natural language comment required. |

### Context Failure Types

- [ ] Missing project context
- [ ] Missing language/framework/version context
- [ ] Missing surrounding code
- [ ] Missing cross-file dependency
- [ ] Irrelevant retrieved context
- [ ] Excessive context / attention dilution
- [x] Generated/comment claim not grounded in code diff
- [x] Unsupported inference from partial context
- [x] Ambiguous relationship between diff and comment

## 11. Trade-off Extraction

| Strategy / Mechanism | Benefit | Risk / Cost | Missing Metric |
|---|---|---|---|
| LLM-based data cleaning | Removes noisy training comments and improves generated-comment quality. | LLM misclassification; API cost; possible bias. | Recall of valid-comment preservation. |
| Retaining only predicted valid comments | Higher training-data quality. | Smaller training set; potential loss of useful borderline comments. | Useful-comment preservation rate. |
| Heuristic cleaning | Cheap and simple. | Misses semantic noise. | Residual noise rate. |
| Manual labeling | Higher-quality labels. | Expensive and hard to scale. | Annotation cost and inter-rater reliability. |
| Fine-tuning on cleaned data | More informative/relevant generated comments. | May reduce diversity or coverage. | Coverage/diversity after cleaning. |

### Trade-off Notes

P08 is strong evidence that filtering can improve quality, but it also makes the preservation problem concrete: removing noisy comments can accidentally remove useful comments and reduce training coverage.

## 12. Human Annotation / User Study / Production Protocol

| Field | Value |
|---|---|
| Human annotators / participants | Yes |
| Number of annotators / participants | Two annotators for labeled samples and generated-comment quality evaluation; exact roles need PDF verification |
| Expertise | Not fully verified; likely researchers/authors |
| Guideline or study protocol provided | Valid/noisy definitions and evaluation criteria are provided |
| Pilot phase | Not fully verified |
| Inter-rater agreement / validation reported | Yes |
| Agreement metric used | Public excerpts report Cohen’s Kappa: 0.71 for informativeness, 0.42 then 0.60 for relevance after discussion/second round |
| Conflict resolution method | Disagreements discussed to reach consensus |
| Production/workflow signal | No live production signal |

### Protocol Quality Checklist

- [x] Manual annotation is used.
- [x] At least two annotators are involved in parts of evaluation.
- [ ] Annotator expertise fully verified.
- [x] Guideline/protocol is described.
- [x] Inter-rater agreement reported.
- [x] Conflict resolution discussed.
- [ ] Live workflow signal included.

### Main Concerns About Validity

Valid/noisy labels require semantic judgment and may be subjective. Kappa for relevance was initially moderate, showing that relevance/usefulness can be difficult to label consistently.

## 13. Key Findings

| Finding | Summary | Evidence / Metric | Importance for us |
|---|---|---|---|
| F1 | Noisy review comments persist in cleaned datasets. | Public abstract and motivation. | Data-quality gap. |
| F2 | LLM-based cleaning detects valid comments. | 66–85% precision. | Supports LLM-as-data-quality gate. |
| F3 | Training on predicted valid comments improves similarity to valid references. | 13.0%–12.4% improvement. | Shows data quality affects generation. |
| F4 | Cleaned models generate more informative and relevant comments. | Manual quality evaluation. | Supports usefulness/actionability dimensions. |
| F5 | Cleaning creates a size/quality trade-off. | Retaining only valid comments reduces training size. | Supports trade-off-aware filtering. |

## 14. Limitations from the Paper’s Own Perspective

- Not fully verified in this pass.
- Likely limitations include dependence on selected dataset, LLM classifier errors, validity of automatic metrics, and generalizability to other review settings.

## 15. Limitations from Our Perspective

- Focuses on training-data quality, not deployment-time comment filtering.
- Valid/noisy may collapse usefulness, actionability, relevance, and correctness.
- Does not fully evaluate downstream workflow impact or reviewer trust.
- Cleaning may discard useful but unconventional or high-level comments.
- Compute/API cost of LLM-based cleaning is not central.

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
| RQ1 — problematic comments | `High` | Vague, non-actionable, noisy, low-value comments. |
| RQ2 — context quality | `Medium / High` | Diff + comment semantic relationship is needed for cleaning. |
| RQ3 — evaluation dimensions | `High` | Relevance, clarity, constructiveness, actionability, informativeness. |
| RQ4 — trade-offs | `High` | Noise removal vs training-size/useful-comment preservation. |
| RQ5 — framework design | `High` | Adds data-quality layer before generation/evaluation. |

### Explanation

P08 is the strongest source so far for treating data quality as part of code review evaluation. It also provides concrete categories that should appear in our problematic-comment taxonomy.

## 17. Extracted Evidence for Our Argument

| Argument Need | Evidence | Label |
|---|---|---|
| Limitations of current evaluations | Existing datasets still contain noisy, vague, non-actionable comments after heuristic/ML cleaning. | `Reported` |
| Missing cost/latency/reviewer-overhead analysis | LLM cleaning cost and deployment cost not central. | `Our perspective` |
| Missing actionability/usefulness distinction | Valid/noisy definitions emphasize actionability but bundle several constructs. | `Our perspective` |
| Need for problematic-comment taxonomy | Noisy comments include vague and non-actionable feedback. | `Reported` |
| Need for human annotation / user-study quality control | Manual labels and kappa show semantic labels are difficult but necessary. | `Reported` |
| Need for context-quality evaluation | Valid/noisy classification requires understanding both code diff and natural-language comment. | `Reported` |
| Need for trade-off-aware evaluation | Cleaning improves quality but reduces training size and may remove useful comments. | `Reported / Our perspective` |
| Need for useful-feedback preservation metric | Predicted-valid filtering needs recall/preservation metric, not precision alone. | `Our perspective` |

## 18. Final Assessment

| Field | Value |
|---|---|
| Overall relevance to our study | `High` |
| Should we cite this paper? | `Yes` |
| Priority for deep reading | `High` |
| Confidence in this analysis | `Medium` |

### Short Justification

P08 is high-priority because it connects noisy code review data to generated-comment quality and provides concrete evidence for vague/non-actionable comments as a data-quality and evaluation problem.

## Open Questions for Follow-up Reading

- [ ] What exact dataset size is cleaned in training?
- [ ] What are the exact LLM prompts and criteria?
- [ ] What are valid/noisy label distributions across train/test?
- [ ] What is recall for valid-comment detection, not only precision?
- [ ] How much training data is removed by cleaning?
- [ ] What examples of noisy comments are listed in the paper?
- [ ] Does the paper report cost of LLM cleaning?

## Follow-up TODOs

- [ ] Verify MSR/IEEE metadata and BibTeX.
- [ ] Verify full dataset statistics.
- [ ] Verify prompt and criteria wording.
- [ ] Extract cite-worthy statements.
- [ ] Add BibTeX.
- [ ] Update `matrices/cross-paper-synthesis.md` with data-quality/noise layer.
- [ ] Update `synthesis/problematic-comment-taxonomy.md` with noisy/vague/non-actionable comments.
- [ ] Update `synthesis/evaluation-dimensions.md` with valid/noisy classification dimensions.
- [ ] Update `synthesis/trade-off-framework.md` with cleaning-quality vs data-size trade-off.

<details>
<summary>Scratchpad</summary>

- Strongest use: data quality matters before model evaluation.
- Good bridge from P01: benchmark reference comments may be bad; P08 shows training data contains noisy comments.
- Important trade-off: precision-only cleaning is not enough; need useful-feedback preservation/recall.

</details>
