# P07 — Impact of LLM-based Review Comment Generation in Practice: A Mixed Open-/Closed-source User Study

> [!NOTE]
> This note uses the repository paper-analysis template. This paper is important because it evaluates LLM-generated review comments in live review environments at Mozilla and Ubisoft, measuring reviewer acceptance, perceived value, and time overhead.

## Completion Checklist

- [x] All bibliographic fields are filled.
- [x] The one-sentence summary is written in a precise and non-generic way.
- [x] The paper’s main goal is separated from our interpretation of its contribution.
- [x] All reported research questions are listed, or `Not reported` is written explicitly.
- [x] Dataset/study details are filled as much as the paper allows.
- [x] Missing details are marked as `Not reported`, not left blank.
- [x] Evaluation methods and metrics are described.
- [x] Human/user-study protocol is documented as far as available in the first pass.
- [x] Evaluation dimensions are checked and explained.
- [x] Problematic comment types are extracted or inferred carefully.
- [x] Every inferred point is marked as `Inferred`.
- [x] Limitations from the paper are separated from our own critique.
- [x] Relevance to our research is explicitly explained.
- [x] Evidence for our argument is extracted into Section 15.
- [x] Open questions for follow-up reading are listed.
- [x] No `TODO` remains unless it is intentionally listed in the follow-up checklist.

## Status

- Paper ID: `P07`
- Analysis status: `First pass completed; public abstract/details verified once`
- Priority: `High`
- Reading depth: `Read once from metadata/abstract/public page; needs PDF-level verification`
- Last updated: `2026-05-08`

## Notation Rules

| Label | Meaning |
|---|---|
| `Reported` | Explicitly stated in the paper, abstract, or verified public metadata. |
| `Inferred` | Reconstructed from examples, tables, results, or implications. |
| `Our perspective` | Our own critique, interpretation, or research positioning. |
| `Not reported` | The paper does not provide this information in the material checked so far. |
| `Not applicable` | The field does not fit this paper. |
| `Partially` | The paper touches the dimension but does not operationalize it clearly. |

> [!IMPORTANT]
> This paper is one of the best sources for evaluating real reviewer behavior. It directly helps us separate “model can generate comments” from “reviewers accept, value, inspect, edit, and act on those comments.”

---

## 1. Bibliographic Information

| Field | Value |
|---|---|
| Title | Impact of LLM-based Review Comment Generation in Practice: A Mixed Open-/Closed-source User Study |
| Authors | Doriane Olewicki, Leuson Da Silva, Suhaib Mujahid, Arezou Amini, Benjamin Mah, Marco Castelluccio, Sarra Habchi, Foutse Khomh, Bram Adams |
| Year | 2024 arXiv preprint; Mozilla research page published 2026 |
| Venue / Source | arXiv / Mozilla research |
| Publication type | Live user study + mixed open-/closed-source empirical study |
| Link | arXiv / Mozilla Research Library |
| DOI / arXiv | DOI: 10.48550/arXiv.2411.07091; arXiv:2411.07091 |
| Code / artifact | Not fully verified in this pass |

### Citation Note

- [x] This paper should be cited in the final report.
- [ ] Citation format has been checked.
- [ ] BibTeX entry has been collected.

```bibtex
% TODO: Paste BibTeX here after checking the final arXiv/BibTeX source.
```

## 2. One-Sentence Summary

> This paper evaluates RevMate, an LLM-based review assistant using RAG and LLM-as-a-Judge, in live review environments at Mozilla and Ubisoft, showing that generated comments have modest direct acceptance but meaningful perceived value and reasonable reviewer time overhead.

## 3. Main Goal of the Paper

### Focus Area

- [x] LLM-based code review generation
- [x] Code review comment evaluation
- [ ] Hallucination / unsupported claims
- [x] Context quality / context selection
- [x] LLM-as-a-judge
- [x] Human annotation / human evaluation
- [x] Industrial / live deployment
- [ ] Benchmark construction
- [x] Cost / latency / operational trade-off
- [x] Other: reviewer acceptance, perceived value, review-time overhead

### Goal

The paper aims to evaluate the practical impact of LLM-generated review comments inside normal review workflows, comparing open-source and closed-source settings and measuring whether reviewers accept, value, inspect, edit, or act on the generated comments.

### Notes

This paper is important because it studies actual reviewer interaction rather than only offline benchmark performance. It helps us argue that acceptance, usefulness, reviewer overhead, and downstream revisions are separate evaluation dimensions that cannot be reduced to text similarity or model correctness alone.

## 4. Research Questions of the Paper

| RQ | Text | Status |
|---|---|---|
| RQ1 | What is the acceptance rate of LLM-generated review comments in live review workflows? | `Reported / Inferred` |
| RQ2 | How valuable do reviewers find generated comments even when they do not directly accept them? | `Reported / Inferred` |
| RQ3 | What time overhead do reviewers incur when inspecting or editing generated comments? | `Reported / Inferred` |
| RQ4 | Do accepted generated comments lead to patch revisions at rates comparable to human-written comments? | `Reported / Inferred` |
| RQ5 | How do results differ between open-source and closed-source organizational settings? | `Reported / Inferred` |

## 5. Dataset and Study Context

| Field | Value |
|---|---|
| Study system | RevMate |
| Study source | Live review environments at Mozilla and Ubisoft |
| Study size | 6-week user study; 59 reviewers; 587 patch reviews; about 1.6k generated comments; post-study survey completed by 37/59 participants |
| Organizations | Mozilla, with open-source codebase; Ubisoft, fully closed-source setting |
| Repository type | Mixed open-source and closed-source industrial settings |
| Input context available | Extra code and review context through RAG, plus LLM-as-a-Judge filtering of irrelevant generated comments |
| Output being evaluated | LLM-generated review comments suggested to reviewers inside their normal review environment |
| Time period | 6 weeks |
| Data availability | Not fully public; study results are reported, but organization-level raw review data is likely not public |

### Dataset / Study Validity Notes

- [x] The study is realistic for code review.
- [x] The study includes live reviewer behavior.
- [x] The study includes generated LLM comments.
- [x] The study includes open-source and closed-source settings.
- [x] The study includes reviewer acceptance and perceived value signals.
- [x] The study includes time-overhead measurement.
- [x] Study details need a second PDF-level verification pass.

### Important Notes About the Study

This is one of the strongest papers for practical impact. It does not only ask whether the generated comments are correct; it asks whether reviewers accept them, mark them as valuable, spend reasonable time inspecting them, and whether accepted generated comments lead to later patch revisions similarly to human-written comments.

## 6. Methods, Models, or Systems Studied

| Field | Value |
|---|---|
| Models / systems | RevMate, an LLM-based assistive tool for generating review comments; public text reports GPT-4o as the underlying model |
| Prompting strategy | Not fully verified in this pass |
| Retrieval or context selection | RAG provides extra code and review context; RevMate has a code-context variant and an example/comment retrieval variant |
| Post-generation verification | LLM-as-a-Judge is used to auto-evaluate generated comments and discard irrelevant cases |
| Static analysis or rule-based checks | Not reported as the main mechanism in first-pass material |
| Human-in-the-loop component | Yes; reviewers inspect, accept, edit, or mark generated comments as valuable within their normal review environment |
| Other mechanisms | Comparison across open-source and closed-source organizations; post-study survey; comparison with human-written comments for downstream revisions |

### Method Checklist

- [x] The paper evaluates generated review comments.
- [x] The paper evaluates a judge/filter/gate through LLM-as-a-Judge filtering.
- [ ] The paper compares multiple LLMs.
- [x] The paper compares contextualization variants, at least code context vs related comment examples.
- [x] The paper uses retrieval or context augmentation.
- [x] The paper includes a post-generation quality check.
- [x] The paper includes a live human evaluation component.

## 7. Evaluation Method

| Field | Value |
|---|---|
| Automatic metrics | Acceptance rate, value-marking rate, time spent inspecting/editing generated comments, patch revision after accepted comments, comparison with human-written comment outcomes |
| Human evaluation | Live reviewer interaction and survey feedback from 37/59 participants |
| Qualitative analysis | Partially; survey and reviewer perspectives are collected, but exact thematic analysis should be checked in the PDF |
| Statistical analysis | Not fully verified in this pass |
| Cost-related evaluation | Yes, through reviewer time overhead; median extra time is reported as 43 seconds per patch |
| Reproducibility materials | Not fully verified; live organization data is likely not fully reproducible |

### Evaluation Validity Checklist

- [x] The evaluation goes beyond BLEU/ROUGE/text similarity.
- [x] The evaluation checks practical reviewer value.
- [x] The evaluation checks acceptance.
- [x] The evaluation checks actionability indirectly through accepted comments and patch revisions.
- [x] The evaluation uses post-generation filtering.
- [x] The evaluation measures cost/time overhead.
- [x] The evaluation includes real developer feedback.
- [x] The evaluation includes live workflow signals.
- [ ] The evaluation fully separates correctness, usefulness, and actionability.
- [ ] The evaluation systematically measures hallucination or unsupported claims.

## 8. Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Technical correctness | `Partially` | Accepted comments and downstream revisions imply usefulness/correctness, but correctness is not necessarily independently labeled for every generated comment. |
| Relevance to code change | `Yes / Partially` | LLM-as-a-Judge filters irrelevant cases; reviewer acceptance/value also indicates relevance. |
| Usefulness | `Yes` | Core dimension: reviewers accept comments or mark them valuable as review/development tips. |
| Actionability | `Partially / Yes` | Accepted comments can be used in review and may lead to patch revisions. |
| Specificity | `Partially` | Not fully verified as a standalone metric. |
| Novelty / non-triviality | `Partially` | Refactoring comments have higher acceptance than functional comments; exact novelty dimension not isolated. |
| Hallucination / unsupported claim | `Partially` | LLM-as-a-Judge discards irrelevant cases, but hallucination-specific evaluation is not central in first-pass material. |
| False positive rate | `Partially` | Rejected or non-valued comments may indicate false positives, but rejection can also reflect low priority or preference. |
| False negative rate | `No / Partially` | Study does not primarily measure missed review issues. |
| Preservation of useful comments | `Partially` | LLM-as-a-Judge discards irrelevant cases, but useful-comment loss due to filtering is not fully measured in first pass. |
| Wrong removal of useful comments | `Not reported` | Not fully analyzed in first-pass material. |
| Review coverage | `Partially` | 587 patch reviews and 1.6k comments provide usage coverage, but issue coverage is not central. |
| Human escalation rate | `Not applicable / No` | Human reviewers are always in the loop; no separate escalation metric. |
| Human annotation cost | `Partially` | Reviewer time overhead is measured. |
| Computational cost | `Not reported / limited` | Not central in first-pass material. |
| Latency | `Partially` | Reviewer overhead is measured; model latency is not central in first-pass material. |
| Operational complexity | `Partially` | Integration into two real review environments demonstrates practical complexity, but details need PDF checking. |
| Trade-off analysis | `Partially` | Measures acceptance/value against reviewer time overhead; does not fully model filtering thresholds or useful-comment preservation. |
| Developer trust | `Partially / Yes` | Survey and reviewer behavior capture trust-related signals, but trust should be checked in the full paper. |
| Workflow impact | `Yes` | Live setup, review-time overhead, acceptance, value, and patch revisions are workflow signals. |

### Notes on Evaluation Dimensions

P07 is especially strong for the usefulness-vs-cost side of evaluation. It shows that even low direct acceptance rates can coexist with additional perceived value, reasonable overhead, and patch revisions comparable to human-written comments.

## 9. Problematic Comment Types / Error Taxonomy

### Explicitly Defined Error Types

First-pass public material does not expose a detailed taxonomy of bad comments. However, it distinguishes accepted comments, valuable tips, and filtered irrelevant cases.

### Inferred Error Types

- `Inferred`: Irrelevant generated comment filtered by LLM-as-a-Judge.
- `Inferred`: Generated comment that reviewers inspect but do not accept.
- `Inferred`: Generated comment that is valuable as a tip but not directly accepted.
- `Inferred`: Functional comment with lower acceptance than refactoring comment.
- `Inferred`: Comment requiring editing before acceptance.
- `Inferred`: Comment that imposes reviewer overhead without enough value.

### Example Problematic Comments

> [!CAUTION]
> Detailed examples should be extracted from the PDF in a second pass. The examples below are conceptual categories, not direct quotes.

| Type | Example / Paraphrase | Source in paper | Label |
|---|---|---|---|
| Rejected generated comment | Reviewer sees a generated comment but does not accept it. | Live interaction signal | `Reported / Inferred` |
| Valuable but not accepted | Reviewer marks a generated comment as valuable for review/development but does not directly post it. | Reported value signal | `Reported` |
| Edited accepted comment | Reviewer accepts a generated comment after editing. | Reported interaction pattern | `Reported` |
| Irrelevant filtered comment | LLM-as-a-Judge discards irrelevant generated cases before reviewer exposure. | RevMate mechanism | `Reported` |

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
- [ ] Redundant comment
- [x] Low-value nitpick
- [ ] Style-only comment with poor practical value
- [ ] Comment that misses the actual issue
- [x] Comment that depends on missing project context
- [x] Comment with poor value-to-time ratio

### Does the Paper Separate Correctness, Usefulness, and Actionability?

- Answer: `Partially`
- Explanation: The paper separates acceptance, perceived value, reviewer time, and downstream patch revision. This is stronger than many benchmark papers, but it does not necessarily isolate technical correctness for each generated comment.

## 10. Human/User Study Protocol

| Field | Value |
|---|---|
| Human participants | Yes; 59 reviewers across Mozilla and Ubisoft |
| Number of participants | 59 reviewers; 37/59 completed the post-study survey |
| Participant expertise | Professional reviewers/developers in Mozilla and Ubisoft review workflows |
| Study guideline provided | Not fully verified in this pass |
| Pilot phase | Not reported in first-pass material |
| Agreement reported | Not applicable in the same way as annotation studies; interaction metrics and survey are used |
| Agreement metric used | Not applicable / not reported |
| Conflict resolution method | Not applicable / not reported |

### Annotation / Study Quality Checklist

- [x] Real users are involved.
- [x] Professional developers/reviewers are involved.
- [x] The study is conducted in live review environments.
- [x] Both open-source and closed-source settings are included.
- [x] Interaction metrics are collected.
- [x] Survey feedback is collected.
- [ ] Controlled inter-rater agreement is reported.
- [x] Threats to ecological validity are reduced by live setup.

### Main Concerns About Study Validity

The live setup gives strong ecological validity, but acceptance does not equal correctness. Reviewers may reject correct comments because of timing, style, redundancy, or priority. They may accept comments after editing, which complicates attribution. The study also uses RevMate’s filtering before reviewers see comments, so the effect of discarded comments and possible wrong removals needs deeper reading.

## 11. Key Findings of the Paper

| Finding | Summary | Evidence / Metric | Importance for us |
|---|---|---|---|
| Finding 1 | Direct acceptance of generated comments is modest. | 8.1% at Mozilla and 7.2% at Ubisoft accepted. | Shows that generation alone is not enough. |
| Finding 2 | Some non-accepted comments are still valuable. | 14.6% and 20.5% marked valuable as review/development tips. | Supports separating acceptance from usefulness. |
| Finding 3 | Refactoring comments are more accepted than functional comments. | 18.2% and 18.6% vs 4.8% and 5.2%. | Supports issue-type-specific evaluation. |
| Finding 4 | Reviewer time overhead is reasonable. | Overall median of 43 seconds per patch; accepted edited comments include 36/119 cases. | Useful for cost/time trade-off. |
| Finding 5 | Accepted generated comments lead to future revisions similarly to human comments. | 74% vs 73% at chunk level. | Strong workflow-impact evidence. |

## 12. Limitations from the Paper’s Own Perspective

- Not fully verified in this pass.
- Likely limitations include dependence on RevMate design, organization-specific workflows, limited study duration, reviewer self-selection, and the challenge of attributing downstream patch revisions to generated comments.
- Full limitations section should be checked directly in the PDF.

## 13. Limitations from Our Perspective

> [!WARNING]
> This section is our critique. Do not present it as a claim made by the paper.

### Possible Issues

- Acceptance is not the same as correctness, usefulness, or actionability.
- Value-marking is subjective and may depend on reviewer style, team culture, and review workload.
- LLM-as-a-Judge filtering happens before reviewer exposure, so wrong removal of useful comments may be hidden.
- The study measures reviewer time overhead, but not full compute cost or system latency.
- The distinction between generated comments used directly, edited comments, and comments used only as tips needs careful interpretation.

### Detailed Notes

This paper should be central for the human-centered evaluation side of our work. It provides evidence that a generated comment can be valuable even if it is not directly accepted. This helps us argue that evaluation should include multiple outcomes: direct acceptance, perceived value, downstream revision, reviewer overhead, and filtering side effects.

## 14. Relevance to Our Paper

### Useful For

- [x] Related work
- [x] Motivation / research gap
- [x] Evaluation framework
- [x] Taxonomy of problematic comments
- [x] Context-quality argument
- [ ] Hallucination / unsupported-claim discussion
- [x] Human annotation/user-study protocol
- [x] Cost / latency / operational trade-off
- [x] Industrial/live validation
- [ ] Benchmark selection
- [x] Methodology design
- [x] Discussion / threats to validity

### Explanation

P07 gives us real-world evidence that LLM-generated review comments should be evaluated through reviewer behavior, not only offline correctness. Its strongest contribution for our paper is the distinction between accepted comments, comments marked valuable as tips, reviewer time overhead, and downstream patch revisions. This directly supports a trade-off-aware and human-centered evaluation framework.

## 15. Extracted Evidence for Our Argument

| Argument Need | Evidence from this paper | Label |
|---|---|---|
| Limitations of current evaluations | Live reviewer acceptance and value differ from offline comment quality; generated comments need workflow-level evaluation. | `Reported / Our perspective` |
| Missing cost analysis | The paper measures reviewer time overhead, but not full compute cost, latency, or cost of wrong filtering. | `Reported / Our perspective` |
| Missing actionability/usefulness distinction | Acceptance, perceived value, and downstream revisions are distinct signals; usefulness is not identical to acceptance. | `Reported` |
| Need for taxonomy | Refactoring and functional comments have different acceptance patterns, suggesting issue-type-specific evaluation is needed. | `Reported` |
| Need for human annotation/user-study quality control | The study uses live reviewers and survey feedback, supporting ecological evaluation beyond offline annotation. | `Reported` |
| Need for context-quality evaluation | RevMate uses RAG to provide extra code/review context; context strategy likely affects comment relevance and acceptance. | `Reported / Inferred` |
| Need for trade-off-aware evaluation | LLM-as-a-Judge filters irrelevant cases, but the evaluation should also consider wrong removals, reviewer overhead, and value preservation. | `Our perspective` |

## 16. Final Assessment

| Field | Value |
|---|---|
| Overall relevance to our study | `High` |
| Should we cite this paper? | `Yes` |
| Priority for deep reading | `High` |
| Confidence in this analysis | `Medium` |

### Short Justification

This is a high-priority paper because it evaluates LLM-generated review comments in live open-source and closed-source review environments. It provides strong evidence for human-centered evaluation dimensions such as acceptance, perceived value, reviewer overhead, and downstream patch revisions.

## Open Questions for Follow-up Reading

- [ ] What exact study protocol did Mozilla and Ubisoft reviewers follow?
- [ ] How are accepted, valuable, edited, and rejected comments defined?
- [ ] What kinds of comments were discarded by LLM-as-a-Judge before reviewer exposure?
- [ ] How much did code-context retrieval vs example/comment retrieval affect acceptance?
- [ ] What survey questions were asked, and what were the qualitative themes?
- [ ] How do acceptance/value rates differ by reviewer role, project, or comment category?
- [ ] Are there measures of trust, annoyance, or review interruption beyond median time overhead?

## Follow-up TODOs

- [ ] Verify bibliographic metadata against arXiv PDF and BibTeX.
- [ ] Verify RevMate model/prompt details.
- [ ] Verify exact definitions of acceptance and value.
- [ ] Extract 1–3 short cite-worthy statements.
- [ ] Add BibTeX.
- [ ] Update `matrices/cross-paper-synthesis.md` with RevMate.
- [ ] Update `synthesis/evaluation-dimensions.md` with acceptance, value, reviewer overhead, and downstream revision.
- [ ] Update `synthesis/trade-off-framework.md` with usefulness vs time-overhead trade-off.
- [ ] Update `synthesis/context-quality.md` with RAG code/review context and LLM-as-a-Judge filtering.

<details>
<summary>Scratchpad</summary>

- Strongest use: acceptance is low, but value can still exist.
- Important for trade-off: reviewer overhead is measurable and not huge in this study.
- Important for taxonomy: refactoring vs functional comments have different acceptance patterns.
- Important for gates: LLM-as-a-Judge filters comments before humans see them, but wrong removals are not obvious.
- Good phrase for paper: “usefulness is not equivalent to direct acceptance.”

</details>
