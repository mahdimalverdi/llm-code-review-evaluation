# P13 — Prompting and Fine-tuning Large Language Models for Automated Code Review Comment Generation

> [!NOTE]
> This note follows the v2 framework-coding template. P13 is central for our prompting/fine-tuning, semantic-context augmentation, metric-validity, and resource trade-off arguments because it compares QLoRA fine-tuning, few-shot prompting, call-graph and summary augmentation, automatic metrics, and human evaluation by professional developers.

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

- Paper ID: `P13`
- Analysis status: `First pass completed from PDF; needs citation/BibTeX cleanup`
- Priority: `High`
- Reading depth: `Read once from PDF`
- Last updated: `2026-05-12`
- Confidence in extraction: `High`

## Our Research Questions

| RQ | Question | Relevance of this paper |
|---|---|---|
| RQ1 | What types of problematic comments appear in LLM-generated code review? | Moderate evidence for generic, less relevant, overconfident incorrect, distracted, unclear, and insufficiently informative comments. |
| RQ2 | How is context quality defined, used, or ignored? | Strong evidence: context is augmented using function call graphs and code summaries, but the paper shows augmentation can help or hurt depending on context window and metadata type. |
| RQ3 | Which evaluation dimensions are covered or missing? | Strong on BLEU-4, BERTScore, human relevance, information, and explanation clarity; also explicitly questions BLEU construct validity. |
| RQ4 | What trade-offs arise from filtering/gating/evaluation? | Strong on prompting vs fine-tuning, cost/resource limits, context-window limits, semantic metadata helpfulness vs distraction, and automatic-vs-human metric mismatch. |
| RQ5 | What should our framework include? | Supports context augmentation trade-offs, metric-validity analysis, human-evaluation dimensions, and resource-aware model adaptation. |

---

## 1. Bibliographic Information

| Field | Value |
|---|---|
| Title | Prompting and Fine-tuning Large Language Models for Automated Code Review Comment Generation |
| Authors | Md. Asif Haider, Ayesha Binte Mostofa, Sk. Sabit Bin Mosaddek, Anindya Iqbal, Toufique Ahmed |
| Year | 2024 |
| Venue / Source | arXiv |
| Publication type | Empirical study + prompting/fine-tuning comparison + human evaluation |
| Link | arXiv |
| DOI / arXiv | DOI: 10.48550/arXiv.2411.10129; arXiv:2411.10129 |
| Code / artifact | Replication package mentioned in paper; exact URL not extracted in first pass |

### Citation Note

- [x] This paper should be cited in the final report.
- [ ] Citation format has been checked.
- [ ] BibTeX entry has been collected.

```bibtex
% TODO: Paste BibTeX here after checking arXiv BibTeX.
```

## 2. One-Sentence Summary

> This paper compares QLoRA fine-tuning of open-source LLMs and few-shot prompting of closed-source LLMs for code review comment generation, showing that semantic metadata such as function call graphs can improve review generation while code summaries or excessive context can sometimes distract models.

## 3. Main Goal of the Paper

### Focus Area

- [x] LLM-based code review generation
- [x] Code review comment evaluation
- [ ] Hallucination / unsupported claims
- [x] Context quality / context selection
- [ ] LLM-as-a-judge
- [x] Human annotation / human evaluation
- [ ] User study / reviewer behavior
- [ ] Industrial deployment
- [ ] Benchmark construction
- [x] Cost / latency / operational trade-off
- [ ] Filtering / gating / aggregation

### Goal

The paper aims to improve automated review comment generation through two resource-aware strategies: parameter-efficient QLoRA fine-tuning of open-source LLMs and few-shot prompting of proprietary LLMs, including semantic prompt augmentation with function call graphs and code summaries.

### Notes

P13 is especially useful for our context-quality and metric-validity arguments. It shows that adding semantic metadata is not uniformly beneficial: call graphs can help, while code summaries can hurt, especially when context windows are limited.

## 4. Research Questions of the Paper

| RQ | Text | Status |
|---|---|---|
| RQ1 | How effective is code review comment generation using fine-tuned open-source LLMs? | `Reported` |
| RQ2 | How well do closed-source LLMs perform in review comment generation when prompt engineered in a few-shot setting? | `Reported` |
| RQ3 | What are the impacts of function call graph and code summary when incorporated into prompts? | `Reported` |
| RQ4 | How effective are LLMs in generating review comments from a real-world developer perspective? | `Reported` |

## 5. Dataset / Study Context

| Field | Value |
|---|---|
| Dataset / study name | CodeReviewer dataset |
| Dataset / study source | Public CodeReviewer dataset from Microsoft Research, derived from high-quality open-source repositories |
| Dataset / study size | Train set ~118k; validation set ~10k; test set ~10k; Test Subset 1: 5,000; Test Subset 2: 500 |
| Number of repositories / projects | Not extracted in first pass; dataset split is project-level |
| Programming languages | C, C++, C#, Go, Java, JavaScript, PHP, Python, Ruby |
| Repository type | Public open-source repositories |
| Input context available | Old file, code diff, review comment; prompt variants add BM25-retrieved few-shot examples, function call graph, and CodeT5-generated code summary |
| Output being evaluated | Generated review comments |
| Time period | Not reported in first pass |
| Data availability | CodeReviewer is public; replication package mentioned |

### Dataset / Study Validity Notes

- [x] Uses a standard code review generation dataset.
- [x] Project-level split reduces train/test leakage across projects.
- [x] Uses two test subsets due to cost constraints.
- [x] Conducts Wilcoxon signed-rank tests to compare subsets and reports no statistically significant difference.
- [x] Includes human evaluation by professional software developers.
- [ ] CodeReviewer dataset quality limitations still apply.
- [ ] Test subsets are smaller than the full test set due to API/resource constraints.
- [ ] Open-source data may not generalize to industrial projects.

### Important Notes

The paper is a good source for resource-aware evaluation. Its decisions are strongly shaped by cost and hardware constraints: closed-source API cost, 16GB VRAM, token-length limits, and limited exploration of hyperparameters.

## 6. Methods, Models, or Systems Studied

| Field | Value |
|---|---|
| Models / systems | CodeReviewer baseline; QLoRA-fine-tuned Llama 2, Code Llama, Llama 3, Llama 3.1, Llama 3.2; prompted GPT-3.5 Turbo, GPT-4o, Gemini-1.0 Pro |
| Prompting strategy | Few-shot prompting with BM25-retrieved exemplars; GPT-4o uses an explicit instruction to produce concise one-sentence formal review comments |
| Retrieval or context selection | BM25 retrieves top-k examples from training data; k=5 for GPT models, k=3 for Gemini in reported setup |
| Post-generation verification | No explicit judge/filter; top-n=5 outputs generated and best BLEU result selected for further comparison |
| Static analysis or rule-based checks | Tree-sitter-based AST extraction for function call graphs and relevant-function extraction for code summaries |
| Human-in-the-loop component | 8 professional software developers evaluate generated comments through a web portal |
| Filtering / gating / aggregation mechanism | None as deployment gate; prompt augmentation and fine-tuning are the main strategies |
| Other mechanisms | CodeT5-generated summaries; function call graph adjacency lists; QLoRA with 4-bit quantization and LoRA adapters |

### Method Checklist

- [x] Evaluates generated review comments.
- [ ] Evaluates a deployment-time judge/filter/gate.
- [ ] Evaluates aggregation.
- [x] Compares model variants and baselines.
- [x] Uses context-aware semantic augmentation.
- [x] Includes prompting and fine-tuning strategies.
- [x] Includes human evaluation.
- [ ] Includes production/workflow evidence.

## 7. Evaluation Method

| Field | Value |
|---|---|
| Automatic metrics | BLEU-4 and BERTScore |
| Human evaluation / user study | 8 professional software developers evaluate generated comments through a web portal |
| Qualitative analysis | Human metrics: relevance, information, explanation clarity, each scored 0–5 |
| Statistical analysis | Wilcoxon signed-rank test for subset representativeness; no significant difference reported |
| Cost / latency / time evaluation | Cost/resource constraints discussed: API cost, 16GB GPU, 2048 token limit, limited hyperparameter exploration |
| Reproducibility materials | Replication package mentioned, but exact link not extracted |

### Evaluation Validity Checklist

- [x] Uses automatic metrics.
- [x] Uses human evaluation.
- [x] Evaluates relevance.
- [x] Evaluates information/completeness.
- [x] Evaluates explanation clarity.
- [x] Discusses BLEU construct-validity concerns.
- [x] Discusses LLM nondeterminism as conclusion-validity threat.
- [x] Discusses external-validity limits from open-source dataset.
- [ ] Measures correctness separately.
- [ ] Measures actionability separately.
- [ ] Measures hallucination/unsupported claims separately.
- [ ] Measures live acceptance/adoption.
- [ ] Measures harmful-comment reduction or useful-comment preservation.

## 8. Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Technical correctness | `Partially` | Incorrect answers and overconfidence are discussed, but no explicit correctness label. |
| Relevance to code change | `Yes` | Human evaluation includes relevance score. |
| Grounding / context alignment | `Partially` | Function call graphs and summaries provide semantic context; no formal grounding metric. |
| Usefulness | `Partially / Yes` | Human relevance/information/clarity approximate usefulness. |
| Actionability | `Partially` | Review comment generation may imply actionability, but no explicit metric. |
| Specificity | `Partially` | Prompt requests concise one-sentence comments; no explicit specificity metric. |
| Novelty / non-triviality | `No / Partially` | Not central. |
| Hallucination / unsupported claim | `No / Partially` | Not central; overconfident incorrect baseline noted. |
| False positive rate | `No` | Not measured. |
| False negative rate | `No` | Not measured. |
| Preservation of useful comments | `No` | Not a filtering paper. |
| Wrong removal of useful comments | `No` | Not applicable. |
| Review coverage / issue coverage | `Partially` | Information score may capture completeness; no issue-coverage metric. |
| Human escalation rate | `No` | Not a deployment study. |
| Human annotation cost | `Partially` | Human study uses 8 participants; cost not quantified. |
| Computational cost | `Yes / Partially` | QLoRA and API cost/resource constraints are central motivations. |
| Latency | `Partially` | Gemini output speed and context windows are mentioned; latency not directly evaluated. |
| Reviewer time overhead | `No` | Not measured. |
| Operational complexity | `Partially` | Fine-tuning, prompt retrieval, call-graph extraction, summary generation add complexity. |
| Trade-off analysis | `Yes` | Prompting vs fine-tuning, context augmentation vs distraction, BLEU vs human judgment, cost vs coverage. |
| Developer trust | `Partially` | Human evaluation reflects developer perception, but trust is not directly measured. |
| Workflow impact | `No` | Not a live workflow study. |

## 9. Problematic Comment Types / Error Taxonomy

### Explicitly Defined Error Types

The paper does not provide a formal error taxonomy, but it explicitly or implicitly discusses several problematic outcomes:

- `Generic or less relevant comment`: caused by lack of project-specific knowledge or weak context.
- `Overconfident incorrect comment`: baseline CodeReviewer is described as showing high confidence in incorrect answers.
- `Distracted generated comment`: GPT-3.5 Turbo can be affected by large input tokens after augmentation.
- `Poorly informative comment`: human information score evaluates completeness of information.
- `Unclear explanation`: human explanation clarity score evaluates clarity of review rationale.
- `Summary-induced degradation`: code summaries can negatively affect generated-comment quality.
- `Poor generalization`: fine-tuned Code Llama can generalize poorly and fail to address specific changes in detail.

### Inferred Error Types

- `Inferred`: Context-window-overloaded comment.
- `Inferred`: Prompt-augmentation noise.
- `Inferred`: Lexically similar but practically weak comment.
- `Inferred`: Comment optimized for BLEU but not human preference.
- `Inferred`: Comment that misses code-change-specific detail.
- `Inferred`: Comment with low explanation clarity.

### Example Problematic Comments

| Type | Example / Paraphrase | Source | Label |
|---|---|---|---|
| Overconfident incorrect baseline | CodeReviewer is described as having high confidence in incorrect answers. | Discussion | `Reported / Paraphrased` |
| Context-window distraction | GPT-3.5 Turbo is negatively affected by large numbers of input tokens after adding call graph and summary. | RQ3 discussion | `Reported / Paraphrased` |
| Summary-induced degradation | Adding code summary alone or with call graph often degrades GPT-3.5 performance. | RQ3 / Table V | `Reported / Paraphrased` |
| Poor generalization | Fine-tuned Code Llama can fail to address specific changes in greater detail. | Discussion | `Reported / Paraphrased` |

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
- Explanation: The paper separates relevance, information, and explanation clarity in human evaluation, but it does not separately label correctness, actionability, harmfulness, or acceptance. This makes it useful for evaluation dimensions, but weaker for problematic-comment taxonomy.

## 10. Context-Quality Extraction

| Context Dimension | Coverage | Evidence / Notes |
|---|---|---|
| Relevance | `Yes / Partially` | BM25 retrieves relevant few-shot examples; human evaluation includes relevance. |
| Completeness | `Partially` | Function call graphs and summaries aim to add semantic information; information score approximates completeness. |
| Specificity / focus | `Partially` | Prompt asks for concise one-sentence formal reviews; fine-tuned models may still fail to address specific changes. |
| Consistency | `Partially` | Nondeterminism is acknowledged as a conclusion-validity threat. |
| Groundability | `Partially` | Call graphs and summaries ground prompts in extracted code structure, but no claim-grounding metric. |
| Locality | `Partially` | Code diff is the primary input; no explicit line-level evaluation. |
| Freshness | `Not central` | Not central. |
| Attention load | `Yes` | Large augmented prompts can distract GPT-3.5; context-window size matters. |
| Cost / token budget | `Yes` | API cost and 2048 token limit shape the design; closed-source prompting uses subsets. |
| Context availability vs usability | `Yes` | Call graphs are more useful than code summaries in ablation, showing not all available context is usable. |

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
| QLoRA fine-tuning | Enables low-resource adaptation of open-source models on consumer hardware. | Requires training setup, hyperparameter choices, and may generalize poorly. | Quality-per-training-cost and project-specific transfer. |
| Few-shot prompting | Avoids model training and improves closed-source LLM performance. | API cost and context-window limits; prompt sensitivity. | Cost-per-useful-comment. |
| BM25 exemplar retrieval | Provides relevant examples for in-context learning. | Retrieved examples may not be semantically sufficient or project-specific. | Exemplar quality and distraction rate. |
| Function call graph augmentation | Helps represent code structure and improves GPT-3.5 in ablation. | Adds tokens and extraction complexity. | Marginal value per token and per language. |
| Code summary augmentation | Intended to provide overall context. | Often degrades performance, likely due to noisy or excessive context. | Summary quality and conflict with diff signal. |
| Automatic metrics | Enables scalable comparison. | BLEU validity is questioned by mismatch with human evaluation. | Human correlation by metric/dimension. |
| Human evaluation | Captures developer perception of relevance, information, and clarity. | Only 8 participants; no live workflow/adoption; no correctness labels. | Inter-rater agreement and construct separation. |

### Trade-off Notes

P13 reinforces a major theme in our paper: more context is not automatically better. Function call graphs can help, but code summaries can hurt. The same augmentation behaves differently across models because context-window size and attention capacity change the value of added information.

## 12. Human Annotation / User Study / Production Protocol

| Field | Value |
|---|---|
| Human annotators / participants | Yes |
| Number of annotators / participants | 8 professional software developers |
| Expertise | Participants affiliated with software industry companies |
| Guideline or study protocol provided | Partially; web portal shows code snippet, generated summary, ground truth reference, anonymized model outputs, and scoring instructions |
| Pilot phase | Not reported in first pass |
| Inter-rater agreement / validation reported | Not extracted/reported in first pass |
| Agreement metric used | Not reported |
| Conflict resolution method | Not reported |
| Production/workflow signal | No live production signal |

### Protocol Quality Checklist

- [x] Human evaluation is used.
- [x] Participants are professional developers.
- [x] Model names are anonymized.
- [x] Each example is evaluated twice by distinct participants.
- [x] Qualitative metrics are defined.
- [ ] Inter-rater agreement is reported.
- [ ] Full study instrument is provided in the paper.
- [ ] Live workflow signal included.

### Main Concerns About Validity

The human study is useful but small. It captures developer perception on relevance, information, and clarity, but does not directly measure correctness, actionability, harmfulness, acceptance, or downstream code changes.

## 13. Key Findings

| Finding | Summary | Evidence / Metric | Importance for us |
|---|---|---|---|
| F1 | QLoRA-fine-tuned open-source LLMs outperform CodeReviewer on BLEU-4 and BERTScore. | Table II. | Resource-aware adaptation evidence. |
| F2 | Code Llama 7B achieves best BLEU-4 among fine-tuned models: 5.58, +30.37%. | Table II. | Code-specific fine-tuning signal. |
| F3 | Llama 3.1 8B achieves best BERTScore among fine-tuned models: 0.8483, +1.62%. | Table II. | Semantic similarity signal. |
| F4 | Few-shot GPT-3.5 Turbo achieves BLEU-4 8.13, +89.95% over baseline on Test Subset 2. | Table III. | Prompting effectiveness. |
| F5 | Gemini-1.0 Pro and GPT-4o also outperform baseline with +83.41% and +61.68% BLEU-4 respectively. | Table III. | Closed-source prompting comparison. |
| F6 | Adding call graph + summary helps GPT-4o but hurts GPT-3.5 Turbo and Gemini. | Table IV. | Context-window/context-quality trade-off. |
| F7 | GPT-3.5 Turbo with call graph alone achieves best ablation BLEU-4: 8.36. | Table V. | Call graph usefulness. |
| F8 | Code summary tends to negatively affect GPT-3.5 Turbo performance. | Table V / RQ3. | Not all context is useful. |
| F9 | Human evaluation ranks Code Llama highest in relevance, information, and explanation clarity. | Table VI. | Automatic-vs-human metric tension. |
| F10 | The paper explicitly flags BLEU reliability as a construct-validity threat. | Threats to validity. | Metric-validity argument. |

## 14. Limitations from the Paper’s Own Perspective

- Cost and resource constraints limited hyperparameter exploration.
- BLEU may not reflect true review quality; human evaluation results raise construct-validity concerns.
- LLM nondeterminism threatens conclusion validity, especially with temperature 0.7.
- CodeReviewer open-source dataset may not generalize to industrial projects.
- GPT-4o could not be fully explored on the whole dataset because of budget constraints.
- Fine-tuned Code Llama may generalize poorly and fail to address specific changes in detail.

## 15. Limitations from Our Perspective

- The study uses lexical/semantic similarity metrics heavily, even while acknowledging their limitations.
- Human evaluation is small and does not report agreement metrics in the extracted text.
- No live adoption or production workflow signal.
- No explicit harmful-comment taxonomy.
- No correctness/actionability/hallucination labels.
- Top-n generation followed by best BLEU selection may overestimate practical performance.
- Function call graphs and summaries are evaluated mainly through output similarity, not actual issue coverage or usefulness preservation.

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
| RQ1 — problematic comments | `Medium` | Generic, distracted, unclear, less informative, overconfident incorrect comments. |
| RQ2 — context quality | `High` | Function call graph and code summary augmentation show context usability trade-offs. |
| RQ3 — evaluation dimensions | `High` | BLEU-4, BERTScore, relevance, information, explanation clarity, construct-validity concerns. |
| RQ4 — trade-offs | `High` | Prompting vs fine-tuning, cost, context-window limits, augmentation helpfulness vs distraction. |
| RQ5 — framework design | `High` | Supports resource-aware, metric-aware, and context-quality-aware evaluation. |

### Explanation

P13 is useful because it provides a controlled comparison of adaptation strategies and semantic context augmentation. It also explicitly shows that evaluation conclusions change when moving from BLEU/BERTScore to professional-developer qualitative judgments.

## 17. Extracted Evidence for Our Argument

| Argument Need | Evidence | Label |
|---|---|---|
| Need for context-quality evaluation | Function call graphs help in some settings, while code summaries can degrade performance. | `Reported` |
| Need for attention/cost-aware context selection | GPT-3.5 can be distracted by large augmented prompts; GPT-4o benefits more due to longer context. | `Reported` |
| Need for metric-validity analysis | Human evaluation ranks Code Llama highest while BLEU favors GPT-3.5 variants, raising BLEU validity concerns. | `Reported / Our perspective` |
| Need for resource-aware evaluation | QLoRA enables fine-tuning on 16GB VRAM; closed-source prompting incurs API cost. | `Reported` |
| Need for human-centered dimensions | Developers rate relevance, information, and explanation clarity. | `Reported` |
| Need for nondeterminism control | LLM outputs are nondeterministic and temperature 0.7 increases variability. | `Reported` |
| Need for project-specific context | General pretraining can produce generic or less relevant comments lacking project-specific nuance. | `Reported` |

## 18. Final Assessment

| Field | Value |
|---|---|
| Overall relevance to our study | `High` |
| Should we cite this paper? | `Yes` |
| Priority for deep reading | `Medium / High` |
| Confidence in this analysis | `High` |

### Short Justification

P13 is highly relevant because it strengthens our argument that context augmentation and model adaptation must be evaluated as trade-offs. It also provides useful evidence that automatic similarity metrics can disagree with professional developer judgments.

## Open Questions for Follow-up Reading

- [ ] What is the exact replication package URL?
- [ ] Does a peer-reviewed version exist after the arXiv preprint?
- [ ] Are human-evaluation agreement statistics available in supplementary material?
- [ ] How were examples selected for the human study?
- [ ] How often did augmented context cause incorrect or irrelevant comments?
- [ ] Can call-graph quality be scored independently?
- [ ] Should code summary be treated as context enrichment or potential context noise in our framework?

## Follow-up TODOs

- [ ] Verify arXiv metadata and BibTeX.
- [ ] Add exact replication-package link.
- [ ] Update `synthesis/context-quality.md` with call graph, code summary, context-window, and metadata-noise trade-offs.
- [ ] Update `synthesis/evaluation-dimensions.md` with relevance, information, explanation clarity, BLEU/BERTScore validity concerns.
- [ ] Update `synthesis/problematic-comment-taxonomy.md` with overconfident incorrect, distracted, and low-information comments.
- [ ] Update `synthesis/trade-off-framework.md` with prompting-vs-fine-tuning and semantic-augmentation trade-offs.
- [ ] Update `matrices/cross-paper-synthesis.md` with P13 evidence.

<details>
<summary>Scratchpad</summary>

- Strongest use: context augmentation can help or hurt.
- Good bridge from P11: LAURA finds context/RAG helpful; P13 shows some metadata augmentation hurts depending on model/context limits.
- Important caution: BLEU improvement should not be equated with better review quality.

</details>
