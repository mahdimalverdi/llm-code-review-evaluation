# Paper Analysis Template

> [!NOTE]
> Use this template for every paper. The goal is not to summarize papers for their own sake. The goal is to extract coded evidence for a focused evidence synthesis that produces:
>
> 1. a taxonomy of problematic LLM-generated code review comments,
> 2. an evaluation framework for generated review comments,
> 3. a context-quality model,
> 4. and a trade-off matrix for filtering/gating/aggregation decisions.

## Completion Checklist

Before marking this paper as completed, make sure every item below is checked.

- [ ] All bibliographic fields are filled.
- [ ] Citation key is added and matches `references/references.bib`.
- [ ] The one-sentence summary is written in a precise and non-generic way.
- [ ] The paper’s main goal is separated from our interpretation of its contribution.
- [ ] All reported research questions are listed, or `Not reported` is written explicitly.
- [ ] Dataset/study details are filled as much as the paper allows.
- [ ] Missing details are marked as `Not reported`, not left blank.
- [ ] Evaluation methods and metrics are described.
- [ ] Human annotation, user-study, or production-feedback protocol is documented, if any.
- [ ] Evaluation dimensions are checked and explained.
- [ ] Problematic comment types are extracted separately from evaluation dimensions.
- [ ] Context-quality dimensions are extracted, if relevant.
- [ ] Trade-offs are explicitly identified, not only mentioned.
- [ ] Every inferred point is marked as `Inferred`.
- [ ] Limitations from the paper are separated from our own critique.
- [ ] Relevance to our research questions is explicitly explained.
- [ ] Evidence for our argument is extracted into Section 17.
- [ ] Open questions for follow-up reading are listed.
- [ ] No `TODO` remains unless it is intentionally listed in the follow-up checklist.

## Status

- Paper ID: `PXX`
- Analysis status: `Not started | In progress | First pass completed | Verified | Ready to cite`
- Priority: `High | Medium | Low`
- Reading depth: `Skimmed | Read once | Deep read | Verified with notes`
- Last updated: `YYYY-MM-DD`
- Confidence in extraction: `High | Medium | Low`

## Notation Rules

Use these labels consistently.

| Label | Meaning |
|---|---|
| `Reported` | Explicitly stated in the paper. |
| `Inferred` | Reconstructed from examples, tables, results, or implications. |
| `Our perspective` | Our own critique, interpretation, or research positioning. |
| `Not reported` | The paper does not provide this information. |
| `Not applicable` | The field does not fit this paper. |
| `Partially` | The paper touches the dimension but does not operationalize it clearly. |

> [!IMPORTANT]
> Do not leave important fields empty. If the paper does not say something, write `Not reported`. Empty fields make cross-paper synthesis unreliable.

## Citation Rule

All BibTeX entries must live in:

```text
references/references.bib
```

Paper notes should contain only the citation key. Do not paste local BibTeX blocks into individual paper notes, because duplicated BibTeX becomes stale.

Citation-key convention:

```text
pXX_firstauthorYYYY_shortslug
```

Example:

```text
p40_ram2018_reviewability
```

## Our Research Questions

Use these as the coding lens while reading each paper.

| RQ | Question | What to extract from each paper |
|---|---|---|
| RQ1 | What types of problematic comments appear in LLM-generated code review? | Error types, failure examples, hallucinations, low-value comments, missed issues. |
| RQ2 | How is context quality defined, used, or ignored in LLM-based code review evaluation? | Context sources, context-selection strategy, context failures, context-size effects. |
| RQ3 | Which evaluation dimensions are covered or missing in current studies? | Correctness, grounding, usefulness, actionability, specificity, coverage, cost, workflow impact. |
| RQ4 | What trade-offs appear when filtering, gating, aggregating, or enriching generated review comments? | Error reduction vs useful feedback preservation, context size vs noise/cost, automation vs reviewer overhead. |
| RQ5 | What should a trade-off-aware evaluation framework include? | Taxonomy categories, metrics, annotation protocol, context-quality dimensions, decision matrix. |

---

# PXX — Paper Title

## 1. Bibliographic Information

| Field | Value |
|---|---|
| Title |  |
| Authors |  |
| Year |  |
| Venue / Source |  |
| Publication type | `Journal | Conference | Workshop | Preprint | Industrial report | Benchmark paper | Case study | User study | Survey` |
| Link |  |
| DOI / arXiv |  |
| Citation key | `pXX_firstauthorYYYY_shortslug` |
| Code / artifact | `Reported | Not reported | Partially reported` |

### Citation Note

- [ ] This paper should be cited in the final report.
- [ ] Citation key exists in `references/references.bib`.
- [ ] Citation format has been checked against official publisher metadata.

## 2. One-Sentence Summary

Write one precise sentence.

> 

## 3. Main Goal of the Paper

### Focus Area

- [ ] LLM-based code review generation
- [ ] Code review comment evaluation
- [ ] Hallucination / unsupported claims
- [ ] Context quality / context selection
- [ ] LLM-as-a-judge
- [ ] Human annotation / human evaluation
- [ ] User study / reviewer behavior
- [ ] Industrial deployment
- [ ] Benchmark construction
- [ ] Cost / latency / operational trade-off
- [ ] Filtering / gating / aggregation
- [ ] Other: 

### Goal



### Notes



## 4. Research Questions of the Paper

| RQ | Text | Status |
|---|---|---|
| RQ1 |  | `Reported | Inferred | Not reported` |
| RQ2 |  | `Reported | Inferred | Not reported` |
| RQ3 |  | `Reported | Inferred | Not reported` |
| RQ4 |  | `Reported | Inferred | Not applicable` |
| RQ5 |  | `Reported | Inferred | Not applicable` |

## 5. Dataset / Study Context

| Field | Value |
|---|---|
| Dataset / study name |  |
| Dataset / study source |  |
| Dataset / study size |  |
| Number of repositories / projects |  |
| Programming languages |  |
| Repository type | `Open-source | Enterprise/proprietary | Mixed | Synthetic | Not reported` |
| Input context available |  |
| Output being evaluated |  |
| Time period |  |
| Data availability | `Public | Private | Partially public | Not reported` |

### Dataset / Study Validity Notes

- [ ] The dataset/study is realistic for code review.
- [ ] The dataset/study has human review feedback.
- [ ] The dataset/study includes actual pull requests / merge requests.
- [ ] The dataset/study includes generated LLM comments.
- [ ] The dataset/study includes developer reactions, acceptance, or production signals.
- [ ] The dataset/study may have incomplete ground truth.
- [ ] Dataset/study details need a second verification pass.

### Important Notes About the Dataset / Study



## 6. Methods, Models, or Systems Studied

| Field | Value |
|---|---|
| Models / systems |  |
| Prompting strategy |  |
| Retrieval or context selection |  |
| Post-generation verification |  |
| Static analysis or rule-based checks |  |
| Human-in-the-loop component |  |
| Filtering / gating / aggregation mechanism |  |
| Other mechanisms |  |

### Method Checklist

- [ ] The paper evaluates generated review comments.
- [ ] The paper evaluates a judge/filter/gate.
- [ ] The paper evaluates aggregation or multi-review synthesis.
- [ ] The paper compares multiple LLMs.
- [ ] The paper compares multiple prompts or context settings.
- [ ] The paper uses retrieval or context augmentation.
- [ ] The paper includes a post-generation quality check.
- [ ] The paper includes a human/user-study component.
- [ ] The paper includes production or workflow evidence.

## 7. Evaluation Method

| Field | Value |
|---|---|
| Automatic metrics |  |
| Human evaluation / user study |  |
| Qualitative analysis |  |
| Statistical analysis |  |
| Cost / latency / time evaluation |  |
| Reproducibility materials |  |

### Evaluation Validity Checklist

- [ ] The evaluation goes beyond BLEU/ROUGE/text similarity.
- [ ] The evaluation checks semantic correctness.
- [ ] The evaluation checks grounding / context alignment.
- [ ] The evaluation checks usefulness or developer value.
- [ ] The evaluation checks actionability.
- [ ] The evaluation checks hallucination or unsupported claims.
- [ ] The evaluation measures false positives.
- [ ] The evaluation measures false negatives.
- [ ] The evaluation measures preservation of useful feedback.
- [ ] The evaluation measures cost, latency, or reviewer time.
- [ ] The evaluation includes real developer feedback.
- [ ] The evaluation includes production/workflow signals.

## 8. Evaluation Dimensions Covered

Use `Yes`, `No`, `Partially`, `Not reported`, or `Not applicable`.

| Dimension | Coverage | Notes |
|---|---|---|
| Technical correctness |  |  |
| Relevance to code change |  |  |
| Grounding / context alignment |  |  |
| Usefulness |  |  |
| Actionability |  |  |
| Specificity |  |  |
| Novelty / non-triviality |  |  |
| Hallucination / unsupported claim |  |  |
| False positive rate |  |  |
| False negative rate |  |  |
| Preservation of useful comments |  |  |
| Wrong removal of useful comments |  |  |
| Review coverage / issue coverage |  |  |
| Human escalation rate |  |  |
| Human annotation cost |  |  |
| Computational cost |  |  |
| Latency |  |  |
| Reviewer time overhead |  |  |
| Operational complexity |  |  |
| Trade-off analysis |  |  |
| Developer trust |  |  |
| Workflow impact |  |  |

### Notes on Evaluation Dimensions



## 9. Problematic Comment Types / Error Taxonomy

> [!IMPORTANT]
> Keep this section separate from evaluation dimensions. For example, `actionability` is an evaluation dimension, while `non-actionable comment` is a problematic comment type.

### Explicitly Defined Error Types

- 

### Inferred Error Types

Mark inferred items explicitly.

- `Inferred`: 

### Example Problematic Comments

> [!CAUTION]
> Keep examples short. Prefer paraphrase unless a short direct quote is necessary.

| Type | Example / Paraphrase | Source in paper | Label |
|---|---|---|---|
|  |  |  | `Reported | Inferred` |

### Taxonomy Checklist

- [ ] Hallucinated or unsupported claim
- [ ] Context-misaligned comment
- [ ] Factually incorrect comment
- [ ] Wrong API/type assumption
- [ ] Wrong-location comment
- [ ] Irrelevant comment
- [ ] Out-of-scope comment
- [ ] Vague or generic comment
- [ ] Non-actionable comment
- [ ] Redundant comment
- [ ] Low-value nitpick
- [ ] Style-only comment with poor practical value
- [ ] Comment that misses the actual issue
- [ ] Comment that depends on missing project context
- [ ] Technically plausible but unsupported comment
- [ ] Comment with poor value-to-time ratio
- [ ] Stale-context-based comment
- [ ] Documentation-code inconsistency
- [ ] Unsupported rationale
- [ ] Invalid repair suggestion
- [ ] Security false alarm
- [ ] Unsupported efficiency claim

### Does the Paper Separate Correctness, Usefulness, and Actionability?

- Answer: `Yes | No | Partially | Not reported`
- Explanation:



## 10. Context-Quality Extraction

> [!NOTE]
> Fill this even when the paper does not explicitly use the phrase “context quality.” We need to know whether the study assumes, measures, improves, or ignores context quality.

| Context Dimension | Coverage | Evidence / Notes |
|---|---|---|
| Relevance |  |  |
| Completeness |  |  |
| Specificity / focus |  |  |
| Consistency |  |  |
| Groundability |  |  |
| Locality |  |  |
| Freshness |  |  |
| Reviewability |  |  |
| Provenance |  |  |
| Behavioral evidence |  |  |
| Attention load |  |  |
| Cost / token budget |  |  |
| Context availability vs context usability |  |  |

### Context Failure Types

- [ ] Missing project context
- [ ] Missing language/framework/version context
- [ ] Missing surrounding code
- [ ] Missing cross-file dependency
- [ ] Irrelevant retrieved context
- [ ] Excessive context / attention dilution
- [ ] Contradictory PR metadata and diff
- [ ] Stale documentation or examples
- [ ] Documentation-code behavior mismatch
- [ ] Unsupported inference from partial context
- [ ] Generated claim not grounded in provided context
- [ ] Tool/static-analysis output misinterpreted
- [ ] AI-generated context without provenance or verification

## 11. Trade-off Extraction

> [!IMPORTANT]
> Do not only say “there is a trade-off.” Specify the strategy, benefit, risk, and missing metric.

| Strategy / Mechanism | Benefit | Risk / Cost | Missing Metric |
|---|---|---|---|
| More context |  |  |  |
| RAG / retrieval |  |  |  |
| Hallucination gate |  |  |  |
| Actionability gate |  |  |  |
| Reviewability gate |  |  |  |
| Context-consistency check |  |  |  |
| LLM-as-a-Judge |  |  |  |
| Human escalation |  |  |  |
| Multi-review aggregation |  |  |  |
| Live reviewer inspection |  |  |  |

### Trade-off Notes



## 12. Human Annotation / User Study / Production Protocol

| Field | Value |
|---|---|
| Human annotators / participants | `Yes | No | Not reported` |
| Number of annotators / participants |  |
| Expertise |  |
| Guideline or study protocol provided |  |
| Pilot phase |  |
| Inter-rater agreement / validation reported |  |
| Agreement metric used |  |
| Conflict resolution method |  |
| Production/workflow signal |  |

### Protocol Quality Checklist

- [ ] Independent annotation is used.
- [ ] At least two annotators are used.
- [ ] Annotators/participants have software engineering expertise.
- [ ] Annotation guideline or study protocol is described.
- [ ] Inter-rater agreement or validation is reported.
- [ ] Conflict resolution is described.
- [ ] Threats to annotation/user-study validity are discussed.
- [ ] Live workflow or production signal is included.

### Main Concerns About Validity



## 13. LLM-as-a-Judge / Evaluator Validity

Fill this section when the paper uses or studies LLM-as-a-Judge.

| Check | Value / Notes |
|---|---|
| Judge model(s) |  |
| Evaluation type | `pointwise | pairwise | listwise | rubric scoring | classification | other` |
| Judge rubric |  |
| Answer rate / parseability |  |
| Repeated-run consistency |  |
| A/B order sensitivity |  |
| Prompt perturbation check |  |
| Judge-choice sensitivity |  |
| Source-model sensitivity |  |
| Human agreement / calibration |  |
| Known limitations |  |

## 14. Key Findings of the Paper

| Finding | Summary | Evidence / Metric | Importance for us |
|---|---|---|---|
| Finding 1 |  |  |  |
| Finding 2 |  |  |  |
| Finding 3 |  |  |  |
| Finding 4 |  |  |  |
| Finding 5 |  |  |  |

## 15. Limitations from the Paper’s Own Perspective

- 

## 16. Limitations from Our Perspective

> [!WARNING]
> This section is our critique. Do not present it as a claim made by the paper.

### Possible Issues

- 

### Detailed Notes



## 17. Relevance to Our Paper

### Useful For

- [ ] Related work
- [ ] Motivation / research gap
- [ ] Evaluation framework
- [ ] Taxonomy of problematic comments
- [ ] Context-quality argument
- [ ] Hallucination / unsupported-claim discussion
- [ ] Human annotation / user-study protocol
- [ ] Cost / latency / operational trade-off
- [ ] Industrial or live validation
- [ ] Benchmark selection
- [ ] Methodology design
- [ ] Discussion / threats to validity

### Mapping to Our RQs

| Our RQ | Relevance | Evidence |
|---|---|---|
| RQ1 — problematic comments |  |  |
| RQ2 — context quality |  |  |
| RQ3 — evaluation dimensions |  |  |
| RQ4 — trade-offs |  |  |
| RQ5 — framework design |  |  |

### Explanation



## 18. Extracted Evidence for Our Argument

| Argument Need | Evidence from this paper | Label |
|---|---|---|
| Limitations of current evaluations |  | `Reported | Inferred | Our perspective` |
| Missing cost/latency/reviewer-overhead analysis |  | `Reported | Inferred | Our perspective` |
| Missing actionability/usefulness distinction |  | `Reported | Inferred | Our perspective` |
| Need for problematic-comment taxonomy |  | `Reported | Inferred | Our perspective` |
| Need for human annotation / user-study quality control |  | `Reported | Inferred | Our perspective` |
| Need for context-quality evaluation |  | `Reported | Inferred | Our perspective` |
| Need for trade-off-aware evaluation |  | `Reported | Inferred | Our perspective` |
| Need for useful-feedback preservation metric |  | `Reported | Inferred | Our perspective` |
| Need for evaluator-validity checks |  | `Reported | Inferred | Our perspective` |

## 19. Final Assessment

| Field | Value |
|---|---|
| Overall relevance to our study | `High | Medium | Low` |
| Should we cite this paper? | `Yes | No | Maybe` |
| Priority for deep reading | `High | Medium | Low` |
| Confidence in this analysis | `High | Medium | Low` |

### Short Justification



## Open Questions for Follow-up Reading

- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 

## Follow-up TODOs

- [ ] Verify bibliographic metadata.
- [ ] Verify citation key exists in `references/references.bib`.
- [ ] Verify dataset/study size and composition.
- [ ] Verify model list and prompting setup.
- [ ] Verify exact metrics and results.
- [ ] Extract 1–3 short cite-worthy statements.
- [ ] Update `matrices/cross-paper-synthesis.md`.
- [ ] Update `synthesis/evaluation-dimensions.md`.
- [ ] Update `synthesis/problematic-comment-taxonomy.md`.
- [ ] Update `synthesis/context-quality.md`.
- [ ] Update `synthesis/trade-off-framework.md`.

<details>
<summary>Scratchpad</summary>

Use this section for rough notes while reading. Clean it before marking the paper as `Verified`.

- 

</details>
