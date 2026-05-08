# Paper Analysis Template

> [!NOTE]
> Use this template for every paper. The goal is not only to summarize the paper, but to extract evidence for our own research argument about LLM-based code review evaluation, context quality, problematic comments, and trade-off-aware evaluation.

## Completion Checklist

Before marking this paper as completed, make sure every item below is checked.

- [ ] All bibliographic fields are filled.
- [ ] The one-sentence summary is written in a precise and non-generic way.
- [ ] The paper’s main goal is separated from our interpretation of its contribution.
- [ ] All reported research questions are listed, or `Not reported` is written explicitly.
- [ ] Dataset details are filled as much as the paper allows.
- [ ] Missing dataset details are marked as `Not reported`, not left blank.
- [ ] Evaluation methods and metrics are described.
- [ ] Human annotation protocol is documented, if any.
- [ ] Evaluation dimensions are checked and explained.
- [ ] Problematic comment types are extracted or inferred carefully.
- [ ] Every inferred point is marked as `Inferred`.
- [ ] Limitations from the paper are separated from our own critique.
- [ ] Relevance to our research is explicitly explained.
- [ ] Evidence for our argument is extracted into Section 15.
- [ ] Open questions for follow-up reading are listed.
- [ ] No `TODO` remains unless it is intentionally listed in the follow-up checklist.

## Status

- Paper ID: `PXX`
- Analysis status: `Not started | In progress | First pass completed | Verified | Ready to cite`
- Priority: `High | Medium | Low`
- Reading depth: `Skimmed | Read once | Deep read | Verified with notes`
- Last updated: `YYYY-MM-DD`

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

---

# PXX — Paper Title

## 1. Bibliographic Information

| Field | Value |
|---|---|
| Title |  |
| Authors |  |
| Year |  |
| Venue / Source |  |
| Publication type | `Journal | Conference | Workshop | Preprint | Industrial report | Benchmark paper | Case study | Survey` |
| Link |  |
| DOI / arXiv |  |
| Code / artifact | `Reported | Not reported` |

### Citation Note

- [ ] This paper should be cited in the final report.
- [ ] Citation format has been checked.
- [ ] BibTeX entry has been collected.

```bibtex
% Paste BibTeX here if available.
```

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
- [ ] Industrial deployment
- [ ] Benchmark construction
- [ ] Cost / latency / operational trade-off
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

## 5. Dataset and Study Context

| Field | Value |
|---|---|
| Dataset name |  |
| Dataset source |  |
| Dataset size |  |
| Number of repositories / projects |  |
| Programming languages |  |
| Repository type | `Open-source | Enterprise/proprietary | Mixed | Synthetic | Not reported` |
| Input context available |  |
| Output being evaluated |  |
| Time period |  |
| Data availability | `Public | Private | Partially public | Not reported` |

### Dataset Validity Notes

- [ ] The dataset is realistic for code review.
- [ ] The dataset has human review feedback.
- [ ] The dataset includes actual pull requests / merge requests.
- [ ] The dataset includes generated LLM comments.
- [ ] The dataset includes developer reactions or production signals.
- [ ] The dataset may have incomplete ground truth.
- [ ] Dataset details need a second verification pass.

### Important Notes About the Dataset



## 6. Methods, Models, or Systems Studied

| Field | Value |
|---|---|
| Models / systems |  |
| Prompting strategy |  |
| Retrieval or context selection |  |
| Post-generation verification |  |
| Static analysis or rule-based checks |  |
| Human-in-the-loop component |  |
| Other mechanisms |  |

### Method Checklist

- [ ] The paper evaluates generated review comments.
- [ ] The paper evaluates a judge/filter/gate.
- [ ] The paper compares multiple LLMs.
- [ ] The paper compares multiple prompts or context settings.
- [ ] The paper uses retrieval or context augmentation.
- [ ] The paper includes a post-generation quality check.
- [ ] The paper includes a human evaluation component.

## 7. Evaluation Method

| Field | Value |
|---|---|
| Automatic metrics |  |
| Human evaluation |  |
| Qualitative analysis |  |
| Statistical analysis |  |
| Cost-related evaluation |  |
| Reproducibility materials |  |

### Evaluation Validity Checklist

- [ ] The evaluation goes beyond BLEU/ROUGE/text similarity.
- [ ] The evaluation checks semantic correctness.
- [ ] The evaluation checks usefulness or developer value.
- [ ] The evaluation checks actionability.
- [ ] The evaluation checks hallucination or unsupported claims.
- [ ] The evaluation measures false positives.
- [ ] The evaluation measures false negatives.
- [ ] The evaluation measures cost or latency.
- [ ] The evaluation includes real developer feedback.
- [ ] The evaluation includes production/workflow signals.

## 8. Evaluation Dimensions Covered

Use `Yes`, `No`, `Partially`, `Not reported`, or `Not applicable`.

| Dimension | Coverage | Notes |
|---|---|---|
| Technical correctness |  |  |
| Relevance to code change |  |  |
| Usefulness |  |  |
| Actionability |  |  |
| Specificity |  |  |
| Novelty / non-triviality |  |  |
| Hallucination / unsupported claim |  |  |
| False positive rate |  |  |
| False negative rate |  |  |
| Preservation of useful comments |  |  |
| Wrong removal of useful comments |  |  |
| Review coverage |  |  |
| Human escalation rate |  |  |
| Human annotation cost |  |  |
| Computational cost |  |  |
| Latency |  |  |
| Operational complexity |  |  |
| Trade-off analysis |  |  |
| Developer trust |  |  |
| Workflow impact |  |  |

### Notes on Evaluation Dimensions



## 9. Problematic Comment Types / Error Taxonomy

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

### Does the Paper Separate Correctness, Usefulness, and Actionability?

- Answer: `Yes | No | Partially | Not reported`
- Explanation:



## 10. Human Annotation Protocol

| Field | Value |
|---|---|
| Human annotators | `Yes | No | Not reported` |
| Number of annotators |  |
| Annotator expertise |  |
| Annotation guideline provided |  |
| Pilot annotation phase |  |
| Inter-rater agreement reported |  |
| Agreement metric used |  |
| Conflict resolution method |  |

### Annotation Quality Checklist

- [ ] Independent annotation is used.
- [ ] At least two annotators are used.
- [ ] Annotators have software engineering expertise.
- [ ] Annotation guideline is described.
- [ ] Inter-rater agreement is reported.
- [ ] Conflict resolution is described.
- [ ] Threats to annotation validity are discussed.

### Main Concerns About Annotation Validity



## 11. Key Findings of the Paper

| Finding | Summary | Evidence / Metric | Importance for us |
|---|---|---|---|
| Finding 1 |  |  |  |
| Finding 2 |  |  |  |
| Finding 3 |  |  |  |
| Finding 4 |  |  |  |
| Finding 5 |  |  |  |

## 12. Limitations from the Paper’s Own Perspective

- 

## 13. Limitations from Our Perspective

> [!WARNING]
> This section is our critique. Do not present it as a claim made by the paper.

### Possible Issues

- 

### Detailed Notes



## 14. Relevance to Our Paper

### Useful For

- [ ] Related work
- [ ] Motivation / research gap
- [ ] Evaluation framework
- [ ] Taxonomy of problematic comments
- [ ] Context-quality argument
- [ ] Hallucination / unsupported-claim discussion
- [ ] Human annotation protocol
- [ ] Cost / latency / operational trade-off
- [ ] Industrial validation
- [ ] Benchmark selection
- [ ] Methodology design
- [ ] Discussion / threats to validity

### Explanation



## 15. Extracted Evidence for Our Argument

| Argument Need | Evidence from this paper | Label |
|---|---|---|
| Limitations of current evaluations |  | `Reported | Inferred | Our perspective` |
| Missing cost analysis |  | `Reported | Inferred | Our perspective` |
| Missing actionability/usefulness distinction |  | `Reported | Inferred | Our perspective` |
| Need for taxonomy |  | `Reported | Inferred | Our perspective` |
| Need for human annotation quality control |  | `Reported | Inferred | Our perspective` |
| Need for context-quality evaluation |  | `Reported | Inferred | Our perspective` |
| Need for trade-off-aware evaluation |  | `Reported | Inferred | Our perspective` |

## 16. Final Assessment

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
- [ ] Verify dataset size and composition.
- [ ] Verify model list and prompting setup.
- [ ] Verify exact metrics and results.
- [ ] Extract 1–3 short cite-worthy statements.
- [ ] Add BibTeX.
- [ ] Update `matrices/cross-paper-synthesis.md`.
- [ ] Update relevant synthesis files.

<details>
<summary>Scratchpad</summary>

Use this section for rough notes while reading. Clean it before marking the paper as `Verified`.

- 

</details>
