# P10 — BitsAI-CR: Automated Code Review via LLM in Practice

> [!NOTE]
> This note follows the v2 framework-coding template. P10 is central for our industrial-evaluation, filtering, rule-taxonomy, and trade-off framework because it presents a deployed LLM-based code review system at ByteDance with RuleChecker, ReviewFilter, Comment Aggregation, a data flywheel, precision-oriented evaluation, Outdated Rate, survey/interview evidence, and production adoption metrics.

## Completion Checklist

- [x] Bibliographic fields are filled.
- [x] Dataset/study details are filled from the PDF.
- [x] Evaluation methods and metrics are described.
- [x] Human annotation / validation protocol is documented.
- [x] Evaluation dimensions are separated from problematic comment types.
- [x] Context-quality evidence is extracted.
- [x] Trade-offs are explicitly identified.
- [x] Mapping to our RQs is included.
- [x] Open questions and follow-up TODOs are listed.

## Status

- Paper ID: `P10`
- Analysis status: `First pass completed from PDF; needs citation/BibTeX cleanup`
- Priority: `High`
- Reading depth: `Read once from PDF`
- Last updated: `2026-05-12`
- Confidence in extraction: `High`

## Our Research Questions

| RQ | Question | Relevance of this paper |
|---|---|---|
| RQ1 | What types of problematic comments appear in LLM-generated code review? | Strong evidence for hallucination, factual errors, technically correct but low-value comments, irrelevant feedback, redundant comments, and difficult-to-understand comments. |
| RQ2 | How is context quality defined, used, or ignored? | Uses hunk partitioning, function-boundary expansion, tree-sitter, and line-level change annotation to make context precise, bounded, and usable. |
| RQ3 | Which evaluation dimensions are covered or missing? | Strong on precision, outdated rate, rule-level quality, filter rate, latency, user feedback, retention, deployment scale, and survey/interview evidence. |
| RQ4 | What trade-offs arise from filtering/gating/evaluation? | Explicitly prioritizes precision over recall due to trust and alert-fatigue concerns; ReviewFilter improves precision but lowers recall and filters more comments. |
| RQ5 | What should our framework include? | Supports a production-grade trade-off framework combining precision, acceptance/proxy impact, cost/latency, rule-level monitoring, feedback loops, and user trust. |

---

## 1. Bibliographic Information

| Field | Value |
|---|---|
| Title | BitsAI-CR: Automated Code Review via LLM in Practice |
| Authors | Tao Sun, Jian Xu, Yuanpeng Li, Zhao Yan, Ge Zhang, Lintao Xie, Lu Geng, Zheng Wang, Yueyan Chen, Qin Lin, Wenbo Duan, Kaixin Sui |
| Year | 2025 |
| Venue / Source | FSE 2025 Industry / arXiv |
| Publication type | Industrial system + empirical evaluation + deployment report |
| Link | arXiv / FSE Industry |
| DOI / arXiv | DOI: 10.1145/3696630.3728552; arXiv:2501.15134 |
| Code / artifact | Not applicable / not verified; system is an internal ByteDance deployment |

### Citation Note

- [x] This paper should be cited in the final report.
- [ ] Citation format has been checked.
- [ ] BibTeX entry has been collected.

```bibtex
% TODO: Paste BibTeX here after checking ACM/arXiv BibTeX.
```

## 2. One-Sentence Summary

> This paper presents BitsAI-CR, a large-scale ByteDance LLM-based code review system that combines a rule-taxonomy-guided RuleChecker, a precision-improving ReviewFilter, comment aggregation, and a data flywheel using precision and Outdated Rate to continuously optimize automated review comments in production.

## 3. Main Goal of the Paper

### Focus Area

- [x] LLM-based code review generation
- [x] Code review comment evaluation
- [x] Hallucination / unsupported claims
- [x] Context quality / context selection
- [x] LLM-as-a-judge
- [x] Human annotation / human evaluation
- [x] User study / reviewer behavior
- [x] Industrial deployment
- [ ] Benchmark construction
- [x] Cost / latency / operational trade-off
- [x] Filtering / gating / aggregation

### Goal

The paper aims to make LLM-based code review practical at enterprise scale by improving precision, reducing low-value or hallucinated comments, and creating an operational feedback loop that continuously tunes review rules based on developer feedback and observed code-change behavior.

### Notes

This is one of the strongest industrial papers for our work because it explicitly explains why precision is prioritized over recall in production, why technically correct comments can still be practically low-value, and why automated evaluation must include signals beyond manual precision.

## 4. Research Questions of the Paper

| RQ | Text | Status |
|---|---|---|
| RQ1 | Can taxonomy-guided LLM code review improve precision compared with generic strong LLM baselines? | `Reported` |
| RQ2 | Does adding ReviewFilter improve production-grade reliability by removing hallucinated/factually incorrect comments? | `Reported` |
| RQ3 | Which ReviewFilter reasoning pattern best balances precision, recall, filter rate, latency, and deployability? | `Reported` |
| RQ4 | Can Outdated Rate serve as a scalable proxy for developer action/acceptance and rule-level usefulness? | `Reported` |
| RQ5 | Can a deployed data flywheel improve review quality and adoption at large scale? | `Reported` |

## 5. Dataset / Study Context

| Field | Value |
|---|---|
| Dataset / study name | Internal ByteDance MR review data; offline code review evaluation dataset; online production deployment data |
| Dataset / study source | ByteDance internal code repositories, MR comments, static-analysis results, manual review feedback, online user feedback |
| Dataset / study size | 120,000 original review comments; refined training datasets of ~18,000 samples each for Go and front-end languages and ~5,000 samples each for other languages; offline evaluation dataset of 1,397 production-code cases; additional 400 data points for ReviewFilter reasoning-pattern experiment |
| Number of repositories / projects | Not reported in first pass |
| Programming languages | Go, JavaScript, TypeScript, Python, Java |
| Repository type | Large-scale industrial/private repositories |
| Input context available | Code diff segmented by hunk, expanded to function boundaries or bounded context, line-level old/new status annotations |
| Output being evaluated | Structured review comments with review category, problematic code location, issue explanation, severity, and suggestion |
| Time period | 18-week online performance tracking; 8-week retention tracking; exact calendar dates not specified in first pass |
| Data availability | Internal/private; PDF text available; public dataset/code not verified |

### Dataset / Study Validity Notes

- [x] Real industrial deployment evidence.
- [x] Large-scale online usage evidence.
- [x] Includes production-code offline evaluation.
- [x] Includes user survey and expert interviews.
- [x] Includes weekly online metrics.
- [x] Includes systematic manual precision sampling.
- [ ] Dataset cannot be independently reproduced because data is private.
- [ ] Ground truth uses LLM-as-a-judge for offline evaluation; human validation details need deeper review.

### Important Notes

The paper is especially useful for our evaluation framework because it shows that a deployable review system needs operational metrics, not only offline benchmark scores. It introduces Outdated Rate as a practical metric for large-scale monitoring, while also openly noting that it does not definitively prove causality.

## 6. Methods, Models, or Systems Studied

| Field | Value |
|---|---|
| Models / systems | BitsAI-CR; RuleChecker; ReviewFilter; Qwen2.5-Coder-32b-instruct; DeepSeek-v2.5; Doubao-Pro-32K-0828; BitsAI-CR without taxonomy |
| Prompting strategy | Context preparation plus fine-tuned LLM-based rule checking/filtering; exact prompts not fully extracted in first pass |
| Retrieval or context selection | Hunk partitioning, bounded context expansion to function boundaries using tree-sitter, and line-level change annotation |
| Post-generation verification | ReviewFilter validates RuleChecker output and makes a yes/no retain decision |
| Static analysis or rule-based checks | Taxonomy includes internal static-analysis rules and manually mined review rules; static-analysis rule metadata includes recommendation index and acceptance rate |
| Human-in-the-loop component | Manual precision annotation, user likes/dislikes, survey with 137 users, interviews with 12 expert developers |
| Filtering / gating / aggregation mechanism | ReviewFilter for precision verification; rule category blocker for dynamic rule exclusion; comment aggregation using embedding similarity to reduce redundant feedback |
| Other mechanisms | Data flywheel; Outdated Rate monitoring; dynamic rule adjustment/removal; weekly online evaluation |

### Method Checklist

- [x] Evaluates generated review comments.
- [x] Evaluates a judge/filter/gate at deployment time.
- [x] Evaluates aggregation.
- [x] Compares model variants and baselines.
- [x] Uses context-aware semantic preparation.
- [x] Includes post-generation quality verification.
- [x] Includes human annotation/evaluation.
- [x] Includes production/workflow evidence.

## 7. Evaluation Method

| Field | Value |
|---|---|
| Automatic metrics | Precision, recall, filter rate, inference time, Outdated Rate, retention rate, WAU, WPV |
| Human evaluation / user study | Daily manual precision sampling up to 10%; survey with N=137; expert interviews with N=12 |
| Qualitative analysis | Examples of hallucination/factual error and correct-but-superfluous comments; expert feedback categories |
| Statistical analysis | Not emphasized in first pass; no effect-size/statistical-test extraction yet |
| Cost / latency / time evaluation | ReviewFilter reasoning-pattern comparison includes inference time; expert interview reports latency concerns; retention/adoption tracked online |
| Reproducibility materials | Private system/data; public reproducibility limited |

### Evaluation Validity Checklist

- [x] Beyond BLEU/ROUGE alone.
- [x] Checks semantic validity of review comments.
- [x] Checks relevance to code change.
- [x] Checks hallucination/factual error through ReviewFilter examples.
- [x] Measures false positives through precision.
- [x] Measures false negatives through recall, but recall is intentionally deprioritized.
- [x] Measures effect of filtering on precision/recall/filter rate/latency.
- [x] Measures developer action/acceptance proxy through Outdated Rate.
- [x] Measures deployment-scale adoption.
- [x] Measures retention.
- [x] Measures user perception through survey/interview.
- [ ] Measures useful-feedback preservation directly.
- [ ] Measures causal acceptance of each comment directly.
- [ ] Provides fully reproducible public benchmark/data.

## 8. Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Technical correctness | `Yes` | Precision and ReviewFilter target correctness and factual reliability. |
| Relevance to code change | `Yes / Partially` | Comments are tied to flagged code ranges; irrelevant feedback is captured in survey categories. |
| Grounding / context alignment | `Yes / Partially` | Context preparation and ReviewFilter address hallucination/factual errors, but no formal claim-to-diff grounding metric. |
| Usefulness | `Yes` | Outdated Rate, user survey, likes/dislikes, and expert interviews address practical utility. |
| Actionability | `Yes / Partially` | Output includes suggestions; Outdated Rate approximates whether developers act. |
| Specificity | `Yes` | Output includes category, line, issue, severity, and suggestion. |
| Novelty / non-triviality | `Partially` | Correct but superfluous comments are explicitly discussed. |
| Hallucination / unsupported claim | `Yes` | ReviewFilter is introduced to mitigate hallucination and factual errors. |
| False positive rate | `Yes` | Precision is central. |
| False negative rate | `Partially` | Recall is measured but intentionally deprioritized. |
| Preservation of useful comments | `Partially` | Recall/filter-rate trade-offs reveal possible suppression, but useful-comment preservation is not directly modeled. |
| Wrong removal of useful comments | `Partially` | ReviewFilter can reduce recall; not framed as useful-comment loss. |
| Review coverage / issue coverage | `Partially` | Taxonomy covers dimensions/rules; recall exists but not the main operational metric. |
| Human escalation rate | `No / Partially` | Not central; reviewers/developers still operate in MR workflow. |
| Human annotation cost | `Yes / Partially` | Manual precision measurement is acknowledged as costly and limited; daily sampling usually <=10%. |
| Computational cost | `Partially` | Inference time is reported; explicit dollar cost not central in PDF first pass. |
| Latency | `Yes` | Reasoning pattern inference time and expert latency feedback. |
| Reviewer time overhead | `Partially` | Motivation says reviewers spend >=15 minutes in many reviews; system impact on reviewer time is not fully isolated. |
| Operational complexity | `Yes` | Taxonomy, fine-tuning, ReviewFilter, aggregation, monitoring, and rule updates are operationally complex. |
| Trade-off analysis | `Yes` | Precision vs recall, filter rate, latency, trust, low-value comments, and adoption. |
| Developer trust | `Yes` | The paper explicitly says inaccurate early comments damage user trust. |
| Workflow impact | `Yes` | Deployment metrics include WAU, WPV, retention, survey, interviews, and online metrics. |

## 9. Problematic Comment Types / Error Taxonomy

### Explicitly Defined Error Types

The paper identifies several practical failure modes:

- `Technically inaccurate comment`: LLM-generated comment is wrong or factually incorrect.
- `Hallucinated comment`: ReviewFilter is introduced because RuleChecker can produce hallucination-related bad cases.
- `Technically correct but practically superfluous comment`: comment is correct by rule but not valuable in context.
- `Irrelevant feedback`: reported by users in survey categories.
- `Comprehension difficulty`: users may find feedback hard to understand.
- `Redundant/similar comments`: comment aggregation exists to avoid overwhelming developers with similar comments.
- `Low-precision rule output`: some review rules produce too many wrong or low-value comments.

### Inferred Error Types

- `Inferred`: Alert-fatigue-inducing comment.
- `Inferred`: Comment with poor value-to-attention ratio.
- `Inferred`: Correct but low-priority best-practice comment.
- `Inferred`: Rule-compliant but context-insensitive comment.
- `Inferred`: Comment that harms trust early in adoption.
- `Inferred`: Overly broad or duplicated rule-triggered feedback.
- `Inferred`: Comment that passes technical correctness but fails practical acceptance.

### Example Problematic Comments

| Type | Example / Paraphrase | Source | Label |
|---|---|---|---|
| Hallucinated formatting issue | RuleChecker claims a variable name contains an underscore and should be changed, even though the variable already complies with standards. | Paper Section 4.2 | `Reported / Paraphrased` |
| Misinterpreted magic number | RuleChecker mistakes a function name containing digits as a magic-number issue. | Paper Section 4.2 | `Reported / Paraphrased` |
| Correct but superfluous | BitsAI-CR flags a magic number that is technically against Go standards, but the user dislikes it as not practically useful. | Paper Section 3.5 / Figure 3 | `Reported / Paraphrased` |
| Redundant feedback | Multiple files/hunks in one MR can generate similar comments, so aggregation removes duplicates. | Paper Section 3.3 | `Reported / Paraphrased` |

### Taxonomy Checklist

- [x] Hallucinated or unsupported claim
- [x] Context-misaligned comment
- [x] Factually incorrect comment
- [x] Wrong API/type assumption
- [x] Wrong-location comment
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

- Answer: `Yes / Strongly`
- Explanation: P10 explicitly distinguishes technical precision from practical utility. The paper argues that precision alone cannot capture whether developers accept or act upon comments, motivating Outdated Rate. It also identifies comments that are technically correct but practically superfluous.

## 10. Context-Quality Extraction

| Context Dimension | Coverage | Evidence / Notes |
|---|---|---|
| Relevance | `Yes` | Code comments are linked to specific code changes and line ranges. |
| Completeness | `Yes / Partially` | Context is expanded to function boundaries within bounded size limits. |
| Specificity / focus | `Yes` | Hunk partitioning, line annotations, and structured output improve focus. |
| Consistency | `Yes / Partially` | ReviewFilter validates detected issues; exact consistency metric not formalized. |
| Groundability | `Yes / Partially` | Comments point to flagged code ranges; no full claim-grounding formalism. |
| Locality | `Yes` | Output includes problematic code locations; context preparation preserves old/new line positions. |
| Freshness | `Yes / Partially` | Outdated Rate observes subsequent commits within a one-week measurement window. |
| Attention load | `Yes` | Aggregation prevents overwhelming developers; precision prioritized to avoid alert fatigue. |
| Cost / token budget | `Yes` | Hunk partitioning and bounded context expansion manage token consumption. |
| Context availability vs usability | `Yes` | Tree-sitter and line annotations convert raw diff into more usable model context. |

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
| Prioritizing precision over recall | Protects user trust and reduces alert fatigue in early production adoption. | Misses potentially useful comments/issues. | Utility-weighted recall / missed useful issue rate. |
| ReviewFilter | Improves precision and mitigates hallucination/factual errors. | Reduces recall and filters potentially useful comments. | Useful-comment preservation rate after filtering. |
| Conclusion-First reasoning | High precision and low inference time. | Lower recall than Reasoning-First. | Impact on missed high-severity issues. |
| Reasoning-First filtering | Better recall and explainability. | Much slower inference time. | Quality-per-second / deployment cost. |
| Comment aggregation | Reduces duplicate comments and attention load. | May remove distinct but similar useful comments. | Duplicate-removal false negative rate. |
| Outdated Rate | Scalable proxy for developer action/acceptance. | Does not prove causality; line may change for other reasons. | Causal acceptance metric / direct developer action label. |
| Rule removal based on precision + Outdated Rate | Removes low-value rules and improves practical acceptance. | May suppress low-frequency but important issues. | Severity-weighted acceptance and safety-risk retention. |
| Data flywheel | Enables continuous targeted improvement. | Requires annotation pipeline, monitoring, and operational maintenance. | Operational cost and annotation burden over time. |

### Trade-off Notes

P10 is one of the best papers for our trade-off matrix. It directly argues that production code review should not optimize recall blindly because low-precision comments harm trust and cause developers to ignore the system. At the same time, its own results show the risk: the best production-friendly filter pattern improves precision and speed but lowers recall.

## 12. Human Annotation / User Study / Production Protocol

| Field | Value |
|---|---|
| Human annotators / participants | Yes |
| Number of annotators / participants | Survey N=137; expert interviews N=12; daily manual precision annotation samples <=10% of online data |
| Expertise | ByteDance developers; 12 expert developers used BitsAI-CR for more than one month |
| Guideline or study protocol provided | Partially; survey categories and structured interviews are described, but full instrument not extracted in first pass |
| Pilot phase | Canary testing before full deployment |
| Inter-rater agreement / validation reported | Not extracted in first pass |
| Agreement metric used | Not extracted in first pass |
| Conflict resolution method | Not extracted in first pass |
| Production/workflow signal | Yes: WAU, WPV, retention, Outdated Rate, weekly precision trends, likes/dislikes |

### Protocol Quality Checklist

- [x] Manual annotation is used.
- [x] User survey is used.
- [x] Expert interviews are used.
- [x] Production deployment is used.
- [x] Canary testing is used.
- [x] Online behavior metrics are used.
- [ ] Inter-rater agreement reported.
- [ ] Full survey/interview protocol included.
- [ ] Causal relation between comment and code change fully established.

### Main Concerns About Validity

Outdated Rate is valuable but imperfect: a flagged line can be modified for reasons unrelated to BitsAI-CR’s comment. Also, internal/private data makes independent reproduction difficult. The paper uses LLM-as-a-judge for offline evaluation, which introduces evaluator-validity concerns that should be connected to our LLM-as-a-judge discussion.

## 13. Key Findings

| Finding | Summary | Evidence / Metric | Importance for us |
|---|---|---|---|
| F1 | BitsAI-CR uses a two-stage pipeline: RuleChecker detects issues, ReviewFilter validates them. | Methodology. | Concrete gate/filter architecture. |
| F2 | The taxonomy contains 219 review rules across Go, JavaScript, TypeScript, Python, and Java. | Section 3.2. | Rule-level taxonomy and evaluation. |
| F3 | The offline evaluation dataset contains 1,397 cases, with 767 violating and 630 following code best practices. | Section 4.2. | Evaluation design. |
| F4 | Taxonomy-guided BitsAI-CR with ReviewFilter achieves 65.59% overall precision and 39.77% recall in Table 2. | Table 2. | Precision/recall trade-off evidence. |
| F5 | ReviewFilter improves precision but lowers recall. | Table 2 and ablation discussion. | Filtering trade-off evidence. |
| F6 | Conclusion-First ReviewFilter achieves 77.09% precision, 69.00% recall, 55.25% filter rate, and 1.7s/sample inference time. | Table 3. | Quality/latency/filter-rate trade-off. |
| F7 | Weekly online precision improved over 18 weeks, with ReviewFilter reaching a peak of 75.0%. | Figure 6. | Data flywheel evidence. |
| F8 | Go Outdated Rate reaches 26.7% by week 18, while human outdated rate fluctuates around 35%–46%. | Figure 7. | Acceptance/proxy-impact metric. |
| F9 | Survey of 137 users: 74.5% affirmed BitsAI-CR’s value/effectiveness. | Section 4.3. | Human-centered deployment evidence. |
| F10 | Expert interviews show latency is a major concern and customization/one-click suggestions are highly desired. | Table 4. | Operational and UX trade-offs. |
| F11 | Deployment reaches over 12k WAU and 210k WPV, with ~48% retention around week 8. | Section 4.4 / Figure 8. | Industrial adoption evidence. |

## 14. Limitations from the Paper’s Own Perspective

- Current review rules focus primarily on function-level understanding with limited contextual information.
- Future work plans to develop cross-file review capabilities.
- Current language coverage includes five mainstream languages and should be expanded.
- Outdated Rate does not definitively prove that developers changed code because of BitsAI-CR’s comments.

## 15. Limitations from Our Perspective

- Private industrial data limits reproducibility.
- LLM-as-a-judge is used for offline evaluation and needs evaluator-validity analysis.
- Precision-first design is sensible for trust but can suppress useful high-severity comments.
- Outdated Rate is a useful proxy but not a causal acceptance metric.
- Survey/interview evidence is valuable but may be influenced by organizational context and opt-in usage.
- The system’s taxonomy is deeply company-specific, so transferability to open-source projects or other organizations is uncertain.
- The paper reports operational adoption metrics but does not fully quantify reviewer time saved or net productivity gain.

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
- [x] Industrial or live validation
- [x] Benchmark selection
- [x] Methodology design
- [x] Discussion / threats to validity

### Mapping to Our RQs

| Our RQ | Relevance | Evidence |
|---|---|---|
| RQ1 — problematic comments | `High` | Hallucinated, incorrect, superfluous, irrelevant, redundant, hard-to-understand comments. |
| RQ2 — context quality | `High` | Context preparation, hunk segmentation, function-boundary expansion, line annotations, token-budget management. |
| RQ3 — evaluation dimensions | `High` | Precision, recall, filter rate, inference time, Outdated Rate, retention, survey, interviews, WAU/WPV. |
| RQ4 — trade-offs | `Very High` | Precision vs recall, trust vs coverage, latency vs explainability, acceptance vs correctness, rule removal vs rare-important issues. |
| RQ5 — framework design | `Very High` | Strong model for production evaluation and feedback-loop design. |

### Explanation

P10 should be one of the core industrial anchors of our paper. It gives concrete evidence that deployment-oriented evaluation must include trust, alert fatigue, filtering consequences, line-change proxies, rule-level monitoring, adoption, retention, and developer feedback.

## 17. Extracted Evidence for Our Argument

| Argument Need | Evidence | Label |
|---|---|---|
| Need for problematic-comment taxonomy | The paper identifies inaccurate, hallucinated, correct-but-superfluous, irrelevant, redundant, and hard-to-understand comments. | `Reported` |
| Need for context-quality evaluation | BitsAI-CR uses bounded function-level expansion, hunk segmentation, tree-sitter, and line-level annotations. | `Reported` |
| Need for trade-off-aware evaluation | The paper explicitly prioritizes precision over recall because low precision harms trust and creates alert fatigue. | `Reported` |
| Need for useful-feedback preservation metric | ReviewFilter improves precision but lowers recall, implying useful comments may be filtered. | `Our perspective based on reported metrics` |
| Need for operational metrics | Outdated Rate, WAU, WPV, retention, and weekly precision trends are central to deployment evaluation. | `Reported` |
| Need for human-centered metrics | Survey and expert interviews reveal value perception, incorrect comments, unnecessary comments, latency, customization, and UX needs. | `Reported` |
| Need for rule-level evaluation | Taxonomy and per-rule precision/Outdated Rate drive rule decommissioning and improvement. | `Reported` |
| Need for caution with proxy metrics | Outdated Rate does not prove direct causality. | `Reported / Our perspective` |

## 18. Final Assessment

| Field | Value |
|---|---|
| Overall relevance to our study | `Very High` |
| Should we cite this paper? | `Yes` |
| Priority for deep reading | `High` |
| Confidence in this analysis | `High` |

### Short Justification

P10 is one of the strongest papers for our trade-off-aware evaluation framework because it exposes the real deployment tension between precision, recall, developer trust, practical usefulness, latency, rule-level optimization, and adoption at scale.

## Open Questions for Follow-up Reading

- [ ] Is the final FSE/ACM version different from the arXiv PDF?
- [ ] Does the paper provide a full survey/interview instrument elsewhere?
- [ ] Are annotator roles and agreement metrics reported in supplementary materials?
- [ ] Can Outdated Rate be adapted to open-source PRs where line-level outdated status is available?
- [ ] How should severity be incorporated into precision-first filtering?
- [ ] How can we measure causal acceptance rather than line-change correlation?
- [ ] What is the correct way to compare Outdated Rate with direct acceptance/value labels from P07?

## Follow-up TODOs

- [ ] Verify ACM metadata and BibTeX.
- [ ] Add exact ACM citation.
- [ ] Extract the review-rule taxonomy categories into `synthesis/problematic-comment-taxonomy.md` if needed.
- [ ] Update `synthesis/evaluation-dimensions.md` with Outdated Rate, retention, WAU/WPV, filter rate, and inference time.
- [ ] Update `synthesis/context-quality.md` with hunk segmentation, function-boundary expansion, and line-level annotations.
- [ ] Update `synthesis/trade-off-framework.md` with precision-first filtering, useful-comment preservation, and proxy-acceptance limitations.
- [ ] Update `matrices/cross-paper-synthesis.md` with P10 industrial deployment evidence.

<details>
<summary>Scratchpad</summary>

- Strongest use: production trade-off framework.
- Good bridge from P03 and P07: P03 gives Atlassian production evaluation; P07 gives user-study acceptance/value; P10 gives ByteDance deployment, filter architecture, and Outdated Rate.
- Important caution: precision-first is defensible for adoption, but our framework should explicitly ask what useful comments are lost.

</details>
