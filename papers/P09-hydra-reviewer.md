# P09 — Hydra-Reviewer: A Holistic Multi-Agent System for Automatic Code Review Comment Generation

> [!NOTE]
> This note follows the v2 framework-coding template. P09 is central for our mitigation, multi-perspective review, and trade-off analysis because it frames automated code review failures as lack of comprehensiveness, incorrectness, and vagueness, then proposes a multi-agent LLM system with qualitative, user-study, ablation, and cost evidence.

## Completion Checklist

- [x] Bibliographic fields are filled.
- [x] Dataset/study details are filled as far as the public page allows in first pass.
- [x] Evaluation methods and metrics are described.
- [x] Human annotation / validation protocol is documented as far as public sources allow.
- [x] Evaluation dimensions are separated from problematic comment types.
- [x] Context-quality evidence is extracted.
- [x] Trade-offs are explicitly identified.
- [x] Mapping to our RQs is included.
- [x] Open questions and follow-up TODOs are listed.

## Status

- Paper ID: `P09`
- Analysis status: `First pass completed; needs PDF-level verification`
- Priority: `High`
- Reading depth: `Read once from Paper Pool row + FSE 2026 public page + public metadata pages`
- Last updated: `2026-05-12`
- Confidence in extraction: `Medium`

## Proposal RQ Mapping

| Proposal RQ | Relevance and evidence |
|---|---|---|
| RQ1 | **High.** Reports lack of comprehensiveness, incorrectness, and vagueness. |
| RQ2 | **Medium.** Multiple reviewer perspectives improve coverage, but context quality is not independently operationalized. |
| RQ3 | **High.** Covers comprehensiveness, correctness, vagueness, helpfulness, readability, ablation, and cost. |
| RQ4 | **High.** Directly examines multi-agent quality/comprehensiveness versus cost and latency. |
| RQ5 | **Medium.** Annotation and evaluator validity are relevant but not the paper’s central contribution. |
| RQ6 | **High.** Supports mitigation-family classification and multi-agent trade-off analysis. |

---

## 1. Bibliographic Information

| Field | Value |
|---|---|
| Title | Hydra-Reviewer: A Holistic Multi-Agent System for Automatic Code Review Comment Generation |
| Authors | Xiaoxue Ren, Chaoqun Dai, Qiao Huang, Ye Wang, Chao Liu, Bo Jiang |
| Year | 2025 journal article; presented as FSE 2026 journal-first paper |
| Venue / Source | IEEE Transactions on Software Engineering; FSE 2026 Journal-First track |
| Publication type | Journal article + journal-first conference presentation + empirical/tool paper |
| Link | FSE 2026 journal-first page; DOI/public metadata pages |
| DOI / arXiv | DOI: 10.1109/TSE.2025.3621462 |
| Code / artifact | Not verified in this pass |

### Citation Note

- [x] This paper should be cited in the final report.
- [x] Citation key checked against `references/references.bib`.
- [x] Canonical BibTeX entry exists in `references/references.bib`.

```bibtex
```

## 2. One-Sentence Summary

> This paper proposes HYDRA-REVIEWER, a collaborative multi-agent LLM framework for code review comment generation, motivated by the claim that existing ACR methods often miss multi-perspective issues and produce comments that are incomplete, incorrect, or vague.

## 3. Main Goal of the Paper

### Focus Area

- [x] LLM-based code review generation
- [x] Code review comment evaluation
- [ ] Hallucination / unsupported claims
- [x] Context quality / context selection
- [ ] LLM-as-a-judge
- [x] Human annotation / human evaluation
- [x] User study / reviewer behavior
- [ ] Industrial deployment
- [x] Benchmark construction
- [x] Cost / latency / operational trade-off
- [x] Filtering / gating / aggregation

### Goal

The paper aims to improve automated review comment generation by decomposing review into multiple review dimensions and using a collaborative multi-agent LLM framework to generate more comprehensive, helpful, and readable review comments.

### Notes

This paper is useful for our framework because it makes the mitigation side more concrete. It does not only say that comments can be wrong; it names three failure modes of existing automated code review methods and evaluates a strategy that tries to reduce them.

## 4. Research Questions of the Paper

| RQ | Text | Status |
|---|---|---|
| RQ1 | What review dimensions should be considered for comprehensive code review? | `Reported / Inferred` |
| RQ2 | Can a multi-agent LLM framework generate more comprehensive code review comments than single-model baselines? | `Reported / Inferred` |
| RQ3 | How does HYDRA-REVIEWER compare with CodeReviewer, LLaMA-Reviewer, ChatGPT, Comprehensive-ChatGPT, and DeepSeek-V3? | `Reported` |
| RQ4 | Are the generated comments helpful and readable according to a user study? | `Reported` |
| RQ5 | What is the cost and latency of the multi-agent approach? | `Reported` |

## 5. Dataset / Study Context

| Field | Value |
|---|---|
| Dataset / study name | CodeReview, CodeReviewNew, and a newly constructed review comment generation dataset |
| Dataset / study source | Existing code review benchmark datasets plus a newly constructed dataset |
| Dataset / study size | Not verified in first pass |
| Number of repositories / projects | Not verified in first pass |
| Programming languages | Not verified in first pass |
| Repository type | Code review benchmark data; exact source projects need PDF verification |
| Input context available | Code changes / code review inputs; exact context fields need PDF verification |
| Output being evaluated | Generated code review comments |
| Time period | Not verified in first pass |
| Data availability | Not verified in first pass |

### Dataset / Study Validity Notes

- [x] Uses established code review generation benchmarks.
- [x] Adds a newly constructed dataset.
- [x] Evaluates against several model baselines.
- [x] Includes qualitative evaluation and user-study evidence.
- [x] Includes cost analysis.
- [ ] Full dataset construction, sampling, and annotation details need PDF-level verification.
- [ ] Exact ground-truth definition needs verification.

### Important Notes

The strongest available public evidence is from the FSE 2026 journal-first abstract. Because the full paper was not available in this pass, dataset details should be treated as provisional.

## 6. Methods, Models, or Systems Studied

| Field | Value |
|---|---|
| Models / systems | HYDRA-REVIEWER; CodeReviewer; LLaMA-Reviewer; ChatGPT; Comprehensive-ChatGPT; DeepSeek-V3 |
| Prompting strategy | Multi-agent / collaborative prompting strategy; exact prompts need PDF verification |
| Retrieval or context selection | Not verified in first pass |
| Post-generation verification | Qualitative evaluation, ablation study, user study, and cost analysis |
| Static analysis or rule-based checks | Not verified in first pass |
| Human-in-the-loop component | User study for helpfulness and readability |
| Filtering / gating / aggregation mechanism | Multi-agent collaboration/aggregation is used as a mitigation strategy; exact aggregation mechanism needs verification |
| Other mechanisms | Empirical taxonomy of code review dimensions; ablation study for components |

### Method Checklist

- [x] Evaluates generated review comments.
- [ ] Evaluates a judge/filter/gate at deployment time.
- [x] Evaluates aggregation / collaboration through multi-agent design.
- [x] Compares with model baselines.
- [x] Uses review-dimension taxonomy.
- [x] Includes qualitative evaluation.
- [x] Includes user-study evidence.
- [x] Includes cost/latency evidence.
- [ ] Includes production/workflow evidence.

## 7. Evaluation Method

| Field | Value |
|---|---|
| Automatic metrics | BLEU; HYDRA-REVIEWER reportedly scores 8.20 vs DeepSeek-V3 at 7.85 in the public abstract |
| Human evaluation / user study | User study confirms helpfulness and readability, according to the public abstract; protocol details need PDF verification |
| Qualitative analysis | Generated comments reportedly span an average of 7.8 review dimensions |
| Statistical analysis | Not verified in first pass |
| Cost / latency / time evaluation | Public abstract reports average cost of $0.018 and 62.63 seconds per code change |
| Reproducibility materials | Not verified in first pass |

### Evaluation Validity Checklist

- [x] Beyond BLEU/ROUGE alone.
- [x] Checks comprehensiveness / review-dimension coverage.
- [x] Checks helpfulness.
- [x] Checks readability.
- [x] Checks vagueness / clarity at least conceptually.
- [x] Includes ablation study.
- [x] Includes cost/latency.
- [ ] Explicitly checks hallucination/unsupported claims.
- [ ] Explicitly measures false-positive and false-negative consequences.
- [ ] Measures useful-feedback preservation under filtering.
- [ ] Measures production workflow impact.

## 8. Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Technical correctness | `Yes / Partially` | Incorrectness is one of the identified limitations of existing ACR methods. |
| Relevance to code change | `Partially` | Assumed in review generation; exact measurement needs PDF verification. |
| Grounding / context alignment | `Partially` | Multi-perspective review can improve coverage, but full claim grounding is not verified. |
| Usefulness | `Yes` | User study reportedly confirms helpfulness. |
| Actionability | `Partially` | Likely related to helpfulness/readability, but exact operationalization needs verification. |
| Specificity | `Yes / Partially` | Vagueness is one of the identified limitations. |
| Novelty / non-triviality | `Partially` | Multi-perspective review aims to identify omitted issues; novelty not central in public abstract. |
| Hallucination / unsupported claim | `No / Partially` | Incorrectness may include unsupported claims, but hallucination is not the main framing. |
| False positive rate | `Not verified` | Needs full paper. |
| False negative rate | `Partially` | Lack of comprehensiveness implies missed issues, but no explicit FN metric verified. |
| Preservation of useful comments | `No / Partially` | Not a filtering paper; useful-comment preservation not central. |
| Wrong removal of useful comments | `No` | Not central. |
| Review coverage / issue coverage | `Yes / Partially` | Average review-dimension coverage is reported; issue-level coverage details need verification. |
| Human escalation rate | `No` | Not central. |
| Human annotation cost | `Partially` | User study exists; annotation cost not verified. |
| Computational cost | `Yes` | Public abstract reports per-code-change dollar cost. |
| Latency | `Yes` | Public abstract reports seconds per code change. |
| Reviewer time overhead | `No / Partially` | User study exists, but workflow overhead not verified. |
| Operational complexity | `Yes / Partially` | Multi-agent design implies orchestration complexity. |
| Trade-off analysis | `Yes / Partially` | Quality/comprehensiveness vs cost/latency. |
| Developer trust | `Partially` | Helpfulness/readability relate to trust, but trust is not verified as a direct metric. |
| Workflow impact | `No` | Not a production deployment study in the public abstract. |

## 9. Problematic Comment Types / Error Taxonomy

### Explicitly Defined Error Types

The public abstract explicitly identifies three major limitations of existing automated code review methods:

- `Lack of comprehensiveness`: automated comments miss potential issues because review is not conducted from multiple perspectives.
- `Incorrectness`: generated comments can be wrong.
- `Vagueness`: generated comments can be too vague to be useful.

### Inferred Error Types

- `Inferred`: Missing issue / incomplete review coverage.
- `Inferred`: Single-perspective review blind spot.
- `Inferred`: Generic or under-specified feedback.
- `Inferred`: Technically incorrect suggestion.
- `Inferred`: Low-actionability feedback caused by vague wording.
- `Inferred`: Comment that appears plausible but does not reflect a reliable review dimension.

### Example Problematic Comments

| Type | Example / Paraphrase | Source | Label |
|---|---|---|---|
| Lack of comprehensiveness | A generated review misses issues that would be visible from other review perspectives. | Public abstract | `Reported / Paraphrased` |
| Incorrectness | A generated comment makes a wrong claim or suggestion. | Public abstract | `Reported / Paraphrased` |
| Vagueness | A generated comment is too vague to guide a concrete improvement. | Public abstract | `Reported / Paraphrased` |
| Multi-perspective blind spot | A single model comments from one angle and misses broader quality concerns. | Our interpretation | `Inferred` |

### Taxonomy Checklist

- [ ] Hallucinated or unsupported claim
- [x] Context-misaligned comment
- [x] Factually incorrect comment
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
- Explanation: The paper explicitly separates incorrectness and vagueness as limitations and separately reports helpfulness/readability through a user study. However, actionability and usefulness need PDF-level verification to see whether they are distinct constructs or bundled into qualitative judgments.

## 10. Context-Quality Extraction

| Context Dimension | Coverage | Evidence / Notes |
|---|---|---|
| Relevance | `Partially` | Review comments are generated for code changes; exact relevance metric needs verification. |
| Completeness | `Yes / Partially` | Multi-perspective review targets lack of comprehensiveness. |
| Specificity / focus | `Yes / Partially` | Vagueness is an explicit limitation. |
| Consistency | `Partially` | Incorrectness suggests need for consistency with code, but exact measurement needs verification. |
| Groundability | `Partially` | Not framed as reference-free grounding; needs full paper. |
| Locality | `Not verified` | Need PDF to inspect line/hunk-level treatment. |
| Freshness | `Not reported` | Not central. |
| Attention load | `Partially` | Multi-agent review increases review breadth but may increase cognitive and computational load. |
| Cost / token budget | `Yes / Partially` | Public abstract reports dollar cost and latency. |
| Context availability vs usability | `Yes / Partially` | The paper’s multi-perspective framing suggests that available code context must be turned into usable review dimensions. |

### Context Failure Types

- [x] Missing project context
- [x] Missing language/framework/version context
- [x] Missing surrounding code
- [x] Missing cross-file dependency
- [x] Irrelevant retrieved context
- [x] Excessive context / attention dilution
- [x] Generated/comment claim not grounded in code diff
- [x] Unsupported inference from partial context
- [x] Ambiguous relationship between diff and comment

## 11. Trade-off Extraction

| Strategy / Mechanism | Benefit | Risk / Cost | Missing Metric |
|---|---|---|---|
| Multi-agent review generation | Broader review coverage and more comprehensive comments. | Higher latency, token cost, orchestration complexity, possible duplicated feedback. | Marginal utility per added agent / dimension. |
| Review-dimension taxonomy | Makes comprehensiveness measurable. | Dimensions may overlap or encourage checklist-like comments. | Inter-rater agreement and construct validity for dimensions. |
| Qualitative dimension coverage | Captures quality beyond lexical similarity. | May reward broad but shallow comments. | Issue-level precision and usefulness-weighted coverage. |
| User study for helpfulness/readability | Adds human-centered evidence. | Protocol, participant expertise, and sample size need verification. | Reviewer time overhead and adoption behavior. |
| Cost analysis | Makes operational feasibility visible. | Cost may vary by model, token pricing, and infrastructure. | Quality-per-dollar and quality-per-second. |

### Trade-off Notes

P09 is useful for our trade-off matrix because it gives an explicit example of a mitigation that improves review breadth but has measurable computational cost and latency. It also shows why comment-level evaluation should include both quality and cost dimensions.

## 12. Human Annotation / User Study / Production Protocol

| Field | Value |
|---|---|
| Human annotators / participants | Yes, user study reported |
| Number of annotators / participants | Not verified in first pass |
| Expertise | Not verified in first pass |
| Guideline or study protocol provided | Not verified in first pass |
| Pilot phase | Not verified in first pass |
| Inter-rater agreement / validation reported | Not verified in first pass |
| Agreement metric used | Not verified in first pass |
| Conflict resolution method | Not verified in first pass |
| Production/workflow signal | No production signal verified; user-study signal only |

### Protocol Quality Checklist

- [x] Human/user evaluation is used.
- [ ] Number of participants verified.
- [ ] Participant expertise verified.
- [ ] Guideline/protocol verified.
- [ ] Inter-rater agreement verified.
- [ ] Conflict resolution verified.
- [ ] Live workflow signal included.

### Main Concerns About Validity

The user-study result is important but cannot be fully interpreted without participant profile, task setup, sample selection, and agreement/protocol details.

## 13. Key Findings

| Finding | Summary | Evidence / Metric | Importance for us |
|---|---|---|---|
| F1 | Existing ACR methods can suffer from lack of comprehensiveness, incorrectness, and vagueness. | Public abstract. | Direct input to problematic-comment taxonomy. |
| F2 | HYDRA-REVIEWER uses a collaborative multi-agent framework to improve review comment generation. | Public abstract. | Mitigation strategy. |
| F3 | HYDRA-REVIEWER outperforms reported baselines on BLEU. | BLEU 8.20 vs DeepSeek-V3 7.85 in public abstract. | Shows common metric but also reveals limits of relying on BLEU. |
| F4 | Generated comments cover more review dimensions. | Average 7.8 dimensions in qualitative evaluation. | Supports comprehensiveness as evaluation dimension. |
| F5 | User study supports helpfulness and readability. | Public abstract; protocol not verified. | Human-centered quality evidence. |
| F6 | Multi-agent review has measurable cost and latency. | $0.018 and 62.63 seconds per code change. | Strong input for trade-off matrix. |

## 14. Limitations from the Paper’s Own Perspective

- Not verified in this pass.
- Likely limitations include dependence on benchmark datasets, cost/latency of multi-agent orchestration, prompt/model sensitivity, and generalizability across projects and languages.

## 15. Limitations from Our Perspective

- Public sources do not expose enough detail about prompts, agents, annotation protocol, and user-study design.
- BLEU improvement is useful but still not sufficient for evaluating comment quality.
- Review-dimension coverage may reward breadth even when some comments are low-priority or not actionable.
- Cost and latency are reported, but quality-per-dollar and quality-per-second are not fully modeled.
- It is not yet clear whether the system reduces harmful comments or only increases breadth.
- It is not a production deployment study, so workflow impact, reviewer trust, and adoption behavior remain open.

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
| RQ1 — problematic comments | `High` | Lack of comprehensiveness, incorrectness, vagueness. |
| RQ2 — context quality | `Medium` | Multi-perspective review suggests context must be evaluated for coverage and usability. |
| RQ3 — evaluation dimensions | `High` | Comprehensiveness, helpfulness, readability, cost, latency, qualitative dimension coverage. |
| RQ4 — trade-offs | `High` | Quality/comprehensiveness vs cost/latency/orchestration. |
| RQ5 — framework design | `High` | Adds multi-agent mitigation to the trade-off matrix. |

### Explanation

P09 is one of the strongest sources for the mitigation-strategy side of our paper. It provides a concrete example of a system that tries to reduce incomplete, incorrect, and vague comments by broadening review perspectives. This helps us argue that evaluation should not only ask whether a generated comment matches a reference, but also whether a mitigation strategy improves useful coverage at an acceptable cost.

## 17. Extracted Evidence for Our Argument

| Argument Need | Evidence | Label |
|---|---|---|
| Need for problematic-comment taxonomy | Existing ACR methods suffer from lack of comprehensiveness, incorrectness, and vagueness. | `Reported` |
| Need for context-quality evaluation | Multi-perspective review suggests that useful review depends on coverage and usable context, not only raw input size. | `Reported / Our perspective` |
| Need for evaluation beyond text similarity | The paper combines BLEU with qualitative dimension coverage, user study, ablation, and cost analysis. | `Reported` |
| Need for trade-off-aware evaluation | Multi-agent design has measurable cost and latency. | `Reported` |
| Need for usefulness/readability dimensions | User study evaluates helpfulness and readability. | `Reported` |
| Need for mitigation-strategy comparison | Multi-agent collaboration can be treated as one mitigation strategy among filtering, RAG, static-analysis grounding, and human escalation. | `Our perspective` |
| Need for useful-feedback preservation metric | Broadening review coverage should be balanced against low-value, duplicate, or vague comments. | `Our perspective` |

## 18. Legacy Quality Appraisal (superseded by the canonical record)

| Criterion | Score | Evidence note |
|---|---:|---|
| Q1 | 2 | Motivation and evaluation objectives are clear. |
| Q2 | 2 | Hydra-Reviewer and agent configuration are specified. |
| Q3 | 2 | Evaluation data and comparison settings are described. |
| Q4 | 2 | Multi-agent generation and ablations are understandable. |
| Q5 | 2 | Quality, correctness, comprehensiveness, helpfulness, and cost are reported. |
| Q6 | 2 | Incorrect, vague, and incomplete comments are identified. |
| Q7 | 1 | Judging protocol is described but requires detailed verification. |
| Q8 | 1 | Reliability/validity checks are partial. |
| Q9 | 2 | Multi-agent mitigation is evaluated. |
| Q10 | 2 | Quality/comprehensiveness versus cost/latency is measured. |
| Q11 | 1 | Generalization and suppression risks remain. |
| Q12 | 2 | Direct support for RQ1, RQ3, RQ4, and RQ6. |
| **Total** | **21/24** | **High-quality core evidence.** |

### Evidence boundary correction

P09 supports multi-agent mitigation trade-offs, not useful-feedback preservation or human escalation.

## 19. Final Assessment

| Field | Value |
|---|---|
| Overall relevance to our study | `High` |
| Should we cite this paper? | `Yes` |
| Priority for deep reading | `High` |
| Confidence in this analysis | `Medium` |

### Short Justification

P09 is high-priority because it gives us a concrete multi-agent mitigation example and explicit problematic-comment types that map well to our taxonomy and trade-off-aware evaluation framework.

## Open Questions for Follow-up Reading

- [ ] What exact review dimensions are in the paper’s taxonomy?
- [ ] What is the architecture of each agent in HYDRA-REVIEWER?
- [ ] How are multi-agent outputs merged or filtered?
- [ ] What exact dataset size and sampling process are used?
- [ ] What are the user-study participant count, expertise, tasks, and questions?
- [ ] Does the paper report statistical significance or effect sizes?
- [ ] Does the paper report false positives, false negatives, or harmful-comment reduction?
- [ ] Does the paper release code, prompts, or data?

## Follow-up TODOs

- [ ] Verify IEEE Xplore metadata and BibTeX.
- [ ] Extract the exact review-dimension taxonomy.
- [ ] Extract examples of incomplete, incorrect, and vague comments.
- [ ] Verify full dataset statistics.
- [ ] Verify prompt/agent architecture.
- [ ] Verify user-study protocol.
- [ ] Add BibTeX.
- [ ] Update `matrices/cross-paper-synthesis.md` with multi-agent mitigation and cost/latency evidence.
- [ ] Update `synthesis/problematic-comment-taxonomy.md` with comprehensiveness/incorrectness/vagueness.
- [ ] Update `synthesis/evaluation-dimensions.md` with review-dimension coverage, helpfulness, readability, cost, and latency.
- [ ] Update `synthesis/trade-off-framework.md` with quality/comprehensiveness vs cost/latency trade-off.

<details>
<summary>Scratchpad</summary>

- Strongest use: mitigation strategy and cost-aware evaluation.
- Good bridge from P08: P08 cleans noisy data; P09 tries to generate broader and less vague review comments.
- Important caution: multi-agent breadth can increase useful coverage, but can also increase cost, latency, duplication, and cognitive load.

</details>
## Canonical citation record

Use citation key `p09_ren2025_hydra_reviewer` from `references/references.bib`; do not duplicate its BibTeX entry in this note.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative for synthesis and quality scoring. Earlier compact/legacy appraisal material is retained only for provenance.

### 1. Identification

- Project ID: P09; citation key: `p09_chen2025_hydra`.
- Source: local full PDF; included after full-text screening; no duplicate identified.

### 2. Screening and proposal alignment

- Decision: Include; Core; High relevance.
- Rationale: collaborative multi-agent review generation motivated by incomplete, incorrect, and vague comments.
- Deliverables: mitigation-family design and trade-off framework.

### 3. Study overview

HYDRA-REVIEWER derives review dimensions from an empirical study and assigns specialized agents to analyze and synthesize feedback. It evaluates generated comments on established and newly constructed datasets and includes a user study (Sections II–VI).

### 4. Evidence mapped to proposal RQ1–RQ6

| RQ | Evidence and interpretation | Type | Location |
|---|---|---|---|
| RQ1 | Lack of comprehensiveness, incorrectness, and vagueness motivate the system. | Reported | Section II |
| RQ2 | Quality dimensions, automated metrics, comparisons, and user judgments assess generation. | Reported | Sections IV–VI |
| RQ3 | Specialist-agent decomposition and aggregation intervene during and after generation. | Reported | Section III |
| RQ4 | Multiple agents can broaden coverage but add calls, latency, redundancy, and synthesis risk; preservation is absent. | Reported/Inferred | Sections III, V–VI |
| RQ5 | Dataset/reference quality and human-study validity are discussed, but context consistency is not central. | Reported/Our perspective | Sections IV, VI, VIII |
| RQ6 | Direct evidence for multi-agent mitigation and comprehensiveness-oriented evaluation. | Our perspective | Sections II–VI |

### 5. Failure and problematic-comment categories

| Category | Definition/example | Type | Location |
|---|---|---|---|
| Incomplete review | Generated output misses relevant review dimensions/issues. | Reported | Section II |
| Incorrect review | Feedback contains technically wrong claims. | Reported | Section II |
| Vague review | Feedback lacks specificity or actionable detail. | Reported | Section II |
| Aggregation conflict | Specialist outputs may conflict or duplicate one another. | Inferred | Section III |

### 6. Evaluation dimensions and metrics

| Dimension | Operationalization | Result/limitation | Location |
|---|---|---|---|
| Comprehensiveness | Dimension/issue coverage and human judgment | Reference completeness may limit estimate | Sections II, V–VI |
| Correctness | Automated/human quality assessment | Evaluator details require calibration | Sections V–VI |
| Specificity/vagueness | Review-quality dimensions | Subjective rubric boundary | Sections II, VI |
| User usefulness | User-study ratings | Participant/sample generalizability | Section VI |
| Cost | Per-patch time and USD cost by system/component | HYDRA-REVIEWER reports 62.63 s and USD 0.0178 per patch, the highest among compared API baselines | Table VII; Section V-E |

### 7. Mitigation and trade-offs

- Mitigation: specialist multi-agent generation and synthesis; during/after generation.
- Reduces: incompleteness, one-perspective blind spots, and vagueness.
- Useful feedback potentially lost: synthesis may omit minority-agent findings; not measured.
- Coverage: comprehensiveness is evaluated; retained unique-issue coverage after aggregation is partial.
- Human escalation: user study exists; explicit escalation workflow is not reported.
- Cost: Table VII reports 62.63 seconds and USD 0.0178 per patch for HYDRA-REVIEWER versus 4.63 s/USD 0.0002 for ChatGPT, 6.39 s/USD 0.0004 for C-ChatGPT, and 18.83 s/USD 0.0060 for DeepSeek-V3. Review agents dominate HYDRA's component cost. The experiments report USD 326 total API expenditure.
- New failures: inter-agent conflict, duplicated findings, and synthesizer hallucination.

### 8. Annotation and evaluator validity

- Judge/annotator: automated evaluators and user-study participants.
- Rubric: comprehensiveness, correctness, and review-quality dimensions.
- Reliability: the paper reports multiple independent-labeling checks, including κ=0.95 for the empirical taxonomy, κ=0.80 for limitation labels, κ values of 0.84–0.94 in ablations/qualitative evaluation, and κ=0.90 in the user-study assessment.
- Bias: selected dimensions/datasets and evaluator dependence.

### 9. Quality appraisal

| Criterion | Score | Evidence note |
|---|---:|---|
| Q1 | 2 | Motivation and empirical/evaluation questions are clear. |
| Q2 | 2 | Multi-agent architecture and artifact are specified. |
| Q3 | 2 | Evaluated datasets and study context are described. |
| Q4 | 2 | Agent workflow and experiments are understandable. |
| Q5 | 2 | Review dimensions and metrics are defined. |
| Q6 | 2 | Incomplete/incorrect/vague failures are explicit. |
| Q7 | 2 | Automated and user-study judging are described. |
| Q8 | 2 | Multiple Cohen's kappa checks, disagreement resolution, unseen-data evaluation, and ablations provide explicit reliability/validity evidence. |
| Q9 | 2 | Multi-agent mitigation is evaluated. |
| Q10 | 2 | Comprehensiveness, helpfulness, reviewer time, per-component latency, and per-patch cost directly quantify quality-versus-cost trade-offs; useful-feedback preservation remains absent. |
| Q11 | 2 | Section VIII explicitly discusses threats to validity, including model randomness, labeling, participant, and dataset concerns. |
| Q12 | 2 | Direct support for mitigation and trade-off RQs. |

- Total: 24/24 under the reporting-quality rubric; this score reflects completeness of reporting, not absence of preservation, generalizability, or deployment limitations.

### 10. Review-process reliability and bias

- Missing data: false suppression, explicit human-escalation policy, and production deployment effects. Per-patch and component costs are reported.
- Publication bias: positive multi-agent results may be selectively visible.
- Selection uncertainty: low; extraction uncertainty: medium for judge/reliability details.
- Second reviewer unavailable; no duplicate identified.

### 11. Synthesis-ready conclusion

- Contribution: supports multi-agent decomposition as a coverage-oriented mitigation.
- Does not establish: preservation of every useful specialist finding or cost-effectiveness.
- Candidate claim: aggregation should report unique-issue retention, conflict rate, and synthesis cost.
- Follow-up: verify user-study agreement and cost tables.
