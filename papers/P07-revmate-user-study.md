# P07 — Impact of LLM-based Review Comment Generation in Practice: A Mixed Open-/Closed-source User Study

> [!NOTE]
> This note follows the v2 framework-coding template. P07 is central for the human-centered part of our framework because it evaluates generated review comments in live Mozilla and Ubisoft review workflows.

## Completion Checklist

- [x] Bibliographic fields are filled.
- [x] Dataset/study details are filled as far as the paper allows.
- [x] Evaluation methods and live-study metrics are described.
- [x] User-study protocol is documented as far as available.
- [x] Evaluation dimensions are separated from problematic comment types.
- [x] Context-quality evidence is extracted.
- [x] Trade-offs are explicitly identified.
- [x] Mapping to our RQs is included.

## Status

- Paper ID: `P07`
- Analysis status: `First pass completed; migrated to v2 template; needs PDF-level verification`
- Priority: `High`
- Reading depth: `Read once from metadata/abstract/public page`
- Last updated: `2026-05-08`
- Confidence in extraction: `Medium`

## Our Research Questions

| RQ | Question | Relevance of this paper |
|---|---|---|
| RQ1 | What types of problematic comments appear in LLM-generated code review? | Provides rejected comments, valuable-but-not-accepted comments, filtered irrelevant comments, and poor value-to-time cases. |
| RQ2 | How is context quality defined, used, or ignored? | RevMate uses RAG and LLM-as-a-Judge filtering; context strategy affects reviewer exposure and value. |
| RQ3 | Which evaluation dimensions are covered or missing? | Strong on acceptance, perceived value, reviewer overhead, and downstream revision; weaker on independent correctness labels. |
| RQ4 | What trade-offs arise from filtering/gating/evaluation? | Strong usefulness-vs-time-overhead and filtering-before-exposure trade-off. |
| RQ5 | What should our framework include? | Supports separating acceptance, usefulness, actionability, downstream impact, and reviewer overhead. |

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

> This paper evaluates RevMate, an LLM-based review assistant using RAG and LLM-as-a-Judge filtering, in live Mozilla and Ubisoft review workflows, showing modest direct acceptance but meaningful perceived value, downstream revisions, and measurable reviewer time overhead.

## 3. Main Goal of the Paper

### Focus Area

- [x] LLM-based code review generation
- [x] Code review comment evaluation
- [ ] Hallucination / unsupported claims
- [x] Context quality / context selection
- [x] LLM-as-a-judge
- [x] Human annotation / human evaluation
- [x] User study / reviewer behavior
- [x] Industrial or live deployment
- [ ] Benchmark construction
- [x] Cost / latency / operational trade-off
- [x] Filtering / gating / aggregation

### Goal

The paper evaluates practical impact of generated review comments inside normal review workflows, comparing Mozilla and Ubisoft and measuring acceptance, value, inspection/editing time, and downstream revisions.

### Notes

P07 is essential because it separates “accepted” from “valuable.” It gives concrete evidence that usefulness is not equivalent to direct acceptance.

## 4. Research Questions of the Paper

| RQ | Text | Status |
|---|---|---|
| RQ1 | What is the acceptance rate of generated comments in live workflows? | `Reported / Inferred` |
| RQ2 | How valuable are generated comments even when not directly accepted? | `Reported / Inferred` |
| RQ3 | What reviewer time overhead is introduced? | `Reported / Inferred` |
| RQ4 | Do accepted generated comments lead to patch revisions like human comments? | `Reported / Inferred` |
| RQ5 | How do open-source and closed-source settings differ? | `Reported / Inferred` |

## 5. Dataset / Study Context

| Field | Value |
|---|---|
| Dataset / study name | RevMate live user study |
| Dataset / study source | Mozilla and Ubisoft review environments |
| Dataset / study size | 6 weeks; 59 reviewers; 587 patch reviews; about 1.6K generated comments; 37/59 survey responses |
| Number of repositories / projects | Not fully verified |
| Programming languages | Not fully verified |
| Repository type | Mixed open-source and closed-source industrial settings |
| Input context available | RAG-provided code/review context; LLM-as-a-Judge filtering of irrelevant comments |
| Output being evaluated | Generated comments suggested to reviewers in normal review environment |
| Time period | 6 weeks |
| Data availability | Raw organization-level data likely private |

### Dataset / Study Validity Notes

- [x] Realistic live review setting.
- [x] Includes live reviewer behavior.
- [x] Includes generated LLM comments.
- [x] Includes open-source and closed-source settings.
- [x] Includes acceptance/value/time signals.
- [x] Needs PDF-level verification.

### Important Notes

This study has strong ecological validity. It is not a clean correctness benchmark; it measures how reviewers interact with generated suggestions in practice.

## 6. Methods, Models, or Systems Studied

| Field | Value |
|---|---|
| Models / systems | RevMate; public text reports GPT-4o as underlying model |
| Prompting strategy | Not fully verified |
| Retrieval or context selection | RAG provides code/review context; variants include code context and related comment examples |
| Post-generation verification | LLM-as-a-Judge filters irrelevant generated comments |
| Static analysis or rule-based checks | Not main mechanism in first pass |
| Human-in-the-loop component | Reviewers inspect, accept, edit, mark value, or reject comments |
| Filtering / gating / aggregation mechanism | LLM-as-a-Judge relevance filtering before reviewer exposure |
| Other mechanisms | Post-study survey; comparison with human comments for downstream revisions |

### Method Checklist

- [x] Evaluates generated review comments.
- [x] Evaluates judge/filter behavior.
- [ ] Evaluates aggregation.
- [ ] Compares multiple LLMs.
- [x] Compares context variants.
- [x] Uses RAG/context augmentation.
- [x] Includes post-generation filtering.
- [x] Includes live human evaluation.
- [x] Includes workflow evidence.

## 7. Evaluation Method

| Field | Value |
|---|---|
| Automatic metrics | Acceptance rate, value marking, inspection/editing time, patch revision after accepted comments, comparison with human-written comment outcomes |
| Human evaluation / user study | Live reviewer interaction and survey feedback |
| Qualitative analysis | Survey/reviewer perspectives collected; exact thematic analysis needs PDF verification |
| Statistical analysis | Not fully verified |
| Cost / latency / time evaluation | Reviewer time overhead; median 43 seconds per patch |
| Reproducibility materials | Not fully verified; live data likely private |

### Evaluation Validity Checklist

- [x] Beyond text similarity.
- [ ] Independently checks semantic correctness for every comment.
- [x] Partially checks relevance via filtering/acceptance.
- [x] Checks usefulness/developer value.
- [x] Checks actionability indirectly via acceptance/revision.
- [ ] Systematically checks hallucination.
- [x] Partially measures false positives via rejected/non-valued comments.
- [ ] Measures missed issues.
- [x] Partially measures useful-feedback preservation/value.
- [x] Measures reviewer time overhead.
- [x] Includes live workflow signals.

## 8. Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Technical correctness | `Partially` | Accepted comments and revisions imply value, but correctness not independently labeled. |
| Relevance to code change | `Yes / Partially` | LLM-as-Judge filters irrelevant cases; acceptance/value indicate relevance. |
| Grounding / context alignment | `Partially` | RAG and judge filtering, but no full claim-grounding analysis. |
| Usefulness | `Yes` | Acceptance and value-marking. |
| Actionability | `Partially / Yes` | Accepted comments and patch revisions. |
| Specificity | `Partially` | Not fully verified. |
| Novelty / non-triviality | `Partially` | Refactoring vs functional acceptance differences. |
| Hallucination / unsupported claim | `Partially` | Filtering irrelevant cases, not hallucination-specific. |
| False positive rate | `Partially` | Rejected/non-valued comments may indicate false positives. |
| False negative rate | `No / Partially` | Missed review issues not central. |
| Preservation of useful comments | `Partially` | Valuable-but-not-accepted signal helps; filter wrong removals not measured. |
| Wrong removal of useful comments | `Not reported` | Pre-exposure filtering may hide wrong removals. |
| Review coverage / issue coverage | `Partially` | Usage coverage, not issue coverage. |
| Human escalation rate | `Not applicable / No` | Humans always in loop. |
| Human annotation cost | `Partially` | Reviewer time overhead. |
| Computational cost | `Not reported` | Not central. |
| Latency | `Partially` | Reviewer overhead measured, not model latency. |
| Reviewer time overhead | `Yes` | Median 43 seconds per patch. |
| Operational complexity | `Partially` | Live integration at two organizations. |
| Trade-off analysis | `Partially / Yes` | Acceptance/value vs time overhead. |
| Developer trust | `Partially / Yes` | Survey/behavior signals. |
| Workflow impact | `Yes` | Live setup and downstream revisions. |

## 9. Problematic Comment Types / Error Taxonomy

### Explicitly Defined Error Types

First-pass public material does not expose a detailed bad-comment taxonomy, but it distinguishes:

- accepted comments;
- valuable tips;
- filtered irrelevant cases;
- edited accepted comments;
- rejected comments.

### Inferred Error Types

- `Inferred`: Irrelevant generated comment filtered by judge.
- `Inferred`: Comment inspected but not accepted.
- `Inferred`: Valuable but not directly accepted comment.
- `Inferred`: Comment requiring editing before acceptance.
- `Inferred`: Comment with poor value-to-time ratio.
- `Inferred`: Functional comment with lower acceptance than refactoring comment.

### Example Problematic Comments

| Type | Example / Paraphrase | Source | Label |
|---|---|---|---|
| Rejected generated comment | Reviewer sees comment but does not accept it. | Live interaction signal | `Reported / Inferred` |
| Valuable but not accepted | Reviewer marks comment valuable but does not post it. | Reported value signal | `Reported` |
| Edited accepted comment | Reviewer edits generated comment before accepting. | Interaction pattern | `Reported` |
| Irrelevant filtered comment | LLM-as-Judge discards irrelevant comment before reviewer exposure. | RevMate mechanism | `Reported` |

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
- Explanation: It separates acceptance, perceived value, reviewer time, and downstream revision, but does not independently label correctness for each comment.

## 10. Context-Quality Extraction

| Context Dimension | Coverage | Evidence / Notes |
|---|---|---|
| Relevance | `Yes / Partially` | LLM-as-Judge filters irrelevant comments. |
| Completeness | `Partially` | RAG adds code/review context. |
| Specificity / focus | `Partially` | Context variants should be checked in PDF. |
| Consistency | `Not reported` | Not central in first pass. |
| Groundability | `Partially` | Filtering, but not full claim grounding. |
| Locality | `Partially` | Patch review context, exact locality not verified. |
| Freshness | `Not reported` | Not central. |
| Attention load | `Not reported` | Not central. |
| Cost / token budget | `Not reported` | Compute cost not central. |
| Context availability vs usability | `Yes / Partially` | RAG context affects practical usefulness/acceptance. |

### Context Failure Types

- [x] Missing project context
- [ ] Missing language/framework/version context
- [x] Missing surrounding code
- [ ] Missing cross-file dependency
- [x] Irrelevant retrieved/generated context
- [ ] Excessive context / attention dilution
- [ ] Contradictory PR metadata and diff
- [x] Unsupported inference from partial context

## 11. Trade-off Extraction

| Strategy / Mechanism | Benefit | Risk / Cost | Missing Metric |
|---|---|---|---|
| RAG context | Adds code/review context for better suggestions. | Irrelevant or low-value suggestions may still occur. | Context relevance/quality score. |
| LLM-as-Judge filtering | Reduces irrelevant comments before reviewer exposure. | Wrongly removed useful comments are hidden. | Wrong-removal / useful-comment preservation rate. |
| Live reviewer inspection | Preserves human control and captures real value. | Adds reviewer time overhead. | Value-to-time ratio by comment type. |
| Direct acceptance metric | Simple practical signal. | Underestimates useful-but-not-accepted comments. | Valuable-but-not-accepted rate. |
| Editing before acceptance | Improves usability of generated comments. | Attribution becomes harder. | Edit effort and edit distance. |

### Trade-off Notes

P07 is the strongest evidence that usefulness must be evaluated separately from acceptance. It also shows why reviewer overhead belongs in our framework.

## 12. Human Annotation / User Study / Production Protocol

| Field | Value |
|---|---|
| Human annotators / participants | 59 reviewers across Mozilla and Ubisoft |
| Number of annotators / participants | 59 reviewers; 37 survey responses |
| Expertise | Professional reviewers/developers |
| Guideline or study protocol provided | Not fully verified |
| Pilot phase | Not reported in first-pass material |
| Inter-rater agreement / validation reported | Not applicable as annotation study |
| Agreement metric used | Not applicable / not reported |
| Conflict resolution method | Not applicable / not reported |
| Production/workflow signal | Acceptance, value, time overhead, downstream patch revision |

### Protocol Quality Checklist

- [x] Real users involved.
- [x] Professional developers/reviewers.
- [x] Live review environment.
- [x] Open-source and closed-source settings.
- [x] Interaction metrics collected.
- [x] Survey feedback collected.
- [ ] Controlled inter-rater agreement.
- [x] Live workflow signal included.

### Main Concerns About Validity

Acceptance does not equal correctness. Rejection can reflect timing, style, redundancy, or priority. Pre-exposure filtering means wrong removals may be invisible.

## 13. Key Findings

| Finding | Summary | Evidence / Metric | Importance for us |
|---|---|---|---|
| F1 | Direct acceptance is modest. | 8.1% Mozilla, 7.2% Ubisoft. | Generation alone is not enough. |
| F2 | Non-accepted comments can still be valuable. | 14.6% and 20.5% valuable tips. | Separates usefulness from acceptance. |
| F3 | Refactoring comments accepted more than functional comments. | 18.2/18.6% vs 4.8/5.2%. | Issue-type evaluation. |
| F4 | Reviewer overhead is reasonable. | Median 43 seconds per patch. | Cost/time trade-off. |
| F5 | Accepted generated comments lead to revisions like human comments. | 74% vs 73% at chunk level. | Workflow-impact evidence. |

## 14. Limitations from the Paper’s Own Perspective

- Not fully verified in this pass.
- Likely limitations: RevMate-specific design, organization-specific workflows, study duration, reviewer self-selection, attribution of revisions.

## 15. Limitations from Our Perspective

- Acceptance is not correctness/usefulness/actionability.
- Value-marking is subjective and culture/workload-dependent.
- Wrong removals by LLM-as-Judge are hidden from reviewers.
- Reviewer time measured, compute cost/model latency not fully measured.
- Edited vs accepted vs tip-only usage needs careful interpretation.

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
- [x] Industrial or live validation
- [ ] Benchmark selection
- [x] Methodology design
- [x] Discussion / threats to validity

### Mapping to Our RQs

| Our RQ | Relevance | Evidence |
|---|---|---|
| RQ1 — problematic comments | `Medium` | Rejected, filtered, edited, valuable-but-not-accepted, poor value-to-time comments. |
| RQ2 — context quality | `Medium / High` | RAG context and judge filtering in live workflow. |
| RQ3 — evaluation dimensions | `High` | Acceptance, value, overhead, downstream revision. |
| RQ4 — trade-offs | `High` | Usefulness vs acceptance vs reviewer time; hidden wrong removals. |
| RQ5 — framework design | `High` | Human-centered evaluation layer. |

### Explanation

RevMate provides real-world evidence that generated review comments need human-centered evaluation dimensions beyond offline correctness.

## 17. Extracted Evidence for Our Argument

| Argument Need | Evidence | Label |
|---|---|---|
| Limitations of current evaluations | Live acceptance/value differ from offline quality. | `Reported / Our perspective` |
| Missing cost/latency/reviewer-overhead analysis | Reviewer time overhead measured, compute/latency not fully covered. | `Reported / Our perspective` |
| Missing actionability/usefulness distinction | Acceptance, value, and downstream revision are distinct. | `Reported` |
| Need for problematic-comment taxonomy | Refactoring vs functional acceptance patterns; rejected/filtered comments. | `Reported / Inferred` |
| Need for human annotation / user-study quality control | Live reviewers and surveys provide ecological validity. | `Reported` |
| Need for context-quality evaluation | RAG context and LLM-as-Judge filtering affect relevance/exposure. | `Reported / Inferred` |
| Need for trade-off-aware evaluation | Filtering/reviewer overhead/value preservation are central. | `Our perspective` |
| Need for useful-feedback preservation metric | Valuable-but-not-accepted comments show usefulness can be hidden by acceptance-only metric. | `Reported / Our perspective` |

## 18. Final Assessment

| Field | Value |
|---|---|
| Overall relevance to our study | `High` |
| Should we cite this paper? | `Yes` |
| Priority for deep reading | `High` |
| Confidence in this analysis | `Medium` |

### Short Justification

This is high-priority because it provides live evidence for separating acceptance, usefulness, reviewer overhead, and downstream impact.

## Open Questions for Follow-up Reading

- [ ] What exact study protocol did reviewers follow?
- [ ] How are accepted, valuable, edited, and rejected comments defined?
- [ ] What was discarded by LLM-as-Judge before exposure?
- [ ] How did context variants affect acceptance/value?
- [ ] Are trust/annoyance/interruption measured beyond time overhead?

## Follow-up TODOs

- [ ] Verify arXiv PDF/BibTeX.
- [ ] Verify RevMate model/prompt details.
- [ ] Verify definitions of acceptance/value/editing.
- [ ] Extract cite-worthy statements.
- [ ] Add BibTeX.
- [ ] Update synthesis if deep reading changes coding.

<details>
<summary>Scratchpad</summary>

- Strongest use: usefulness is not acceptance.
- Strong trade-off evidence: reviewer overhead vs value.
- Gate issue: hidden wrong removals before reviewer sees comments.

</details>
