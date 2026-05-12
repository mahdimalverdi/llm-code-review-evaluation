# Cross-Paper Synthesis Matrix

> [!NOTE]
> This matrix turns individual paper notes into the backbone of the related-work, gap, taxonomy, and evaluation-framework sections.

## Compact Matrix

| Paper | Evaluation Focus | Main Strength | Missing Piece for Our Work | Best Use in Our Paper |
|---|---|---|---|---|
| P01 — DeepCRCEval | Multi-dimensional review-comment quality evaluation | Moves beyond BLEU/ROUGE/text similarity and introduces domain-specific quality criteria | Does not fully model filtering, mitigation, useful-comment preservation, or deployment trade-offs | Motivation + evaluation dimensions |
| P02 — HalluJudge | Hallucination / context misalignment detection | Strong reference-free safeguard/gate framing with claim-to-diff grounding | Focuses mainly on hallucination, not all low-value or non-actionable comments; limited downstream filtering analysis | Hallucination taxonomy + context alignment + gate design |
| P03 — RovoDev Code Reviewer | Production deployment and workflow impact | Strong industrial evidence using code resolution, PR cycle time, human-comment reduction, and developer feedback | Production metrics are realistic but noisy; limited fine-grained taxonomy and controlled annotation | Industrial validation + workflow-aware evaluation |
| P04 — SWE-PRBench | PR-level benchmark against human pull-request feedback | Strong evidence that more context can hurt review performance | Benchmark ground truth is realistic but incomplete; cost/workflow effects are underdeveloped | Context-quality argument + benchmark discussion |
| P05 — SWRBench | PR-centric benchmark with full project context and structured ground truth | Strong critique of fine-grained benchmarks; provides 1,000 manually verified PRs and issue-coverage evaluation | Full-context realism does not automatically solve context-quality, cost, or filtering trade-offs | Benchmark realism + full-project-context discussion |
| P06 — ContextCRBench | Fine-grained benchmark with enriched textual/code context | Explicitly critiques missing semantic context, noisy data, and coarse granularity; provides 67,910 context-enriched entries | Context enrichment is not the same as full context-quality scoring; cost and filtering trade-offs remain underdeveloped | Semantic context + data-quality + fine-grained evaluation |
| P07 — RevMate user study | Live open-/closed-source user study | Measures acceptance, perceived value, reviewer overhead, and downstream patch revisions in Mozilla/Ubisoft settings | Acceptance and value are useful but do not fully isolate correctness; wrong removals by judge/filter remain underexplored | Human-centered evaluation + usefulness-vs-cost trade-off |
| P08 — Too Noisy To Learn | Data-quality cleaning for review-comment generation | Shows noisy, vague, and non-actionable review comments harm learning and that semantic cleaning can improve generated-comment quality | Focuses on dataset cleaning rather than deployment-time filtering; valid/noisy can bundle correctness, usefulness, and actionability | Data-quality layer + noisy-comment taxonomy + filtering trade-offs |
| P09 — Hydra-Reviewer | Multi-agent review-comment generation | Concrete mitigation strategy for lack of comprehensiveness, incorrectness, and vagueness; reports qualitative, user-study, ablation, cost, and latency evidence | Needs deeper verification of prompts, agents, datasets, and user-study protocol; does not fully model harmful-comment reduction or useful-feedback preservation | Multi-agent mitigation + comprehensiveness + quality/cost trade-off |
| P10 — BitsAI-CR | Industrial LLM code review deployment | Strong production evidence: 219-rule taxonomy, RuleChecker, ReviewFilter, aggregation, Outdated Rate, survey/interviews, WAU/WPV, retention, and data flywheel | Private data limits reproducibility; Outdated Rate is a proxy not causal proof; precision-first filtering may lose useful comments | Industrial deployment + filter/gate trade-offs + proxy acceptance metrics |
| P11 — LAURA | Context-enriched RAG code review generation | Strong open-source evidence for context augmentation, review exemplar retrieval, systematic guidance, high-quality dataset construction, I/IH/M-Score, and ablation | Not a live deployment; retrieval/context can distract; LLM filtering may remove useful samples; human usefulness remains limited by missing project context | Context-quality model + RAG trade-offs + useful/misleading/uncertain evaluation |
| P12 — SGCR | Specification-grounded trustworthy code review | Strong industrial evidence for grounding LLM review in human-authored specifications, explicit/implicit pathways, adoption-rate improvement, explainability, and trust | Adoption rate bundles correctness/usefulness/trust; specification maintenance and freshness are under-modeled; useful undocumented issues may be suppressed | Specification grounding + trust/explainability + explicit-vs-implicit trade-off |
| P13 — Prompting and Fine-tuning LLMs for Code Review | Prompting, QLoRA fine-tuning, and semantic metadata augmentation | Shows prompting and QLoRA can outperform CodeReviewer; call graphs can help; code summaries and excessive context can hurt; human evaluation can disagree with BLEU/BERTScore | Uses small human study; no live workflow; heavy reliance on automatic metrics; no explicit harmful-comment or actionability labels | Resource-aware adaptation + semantic context trade-offs + metric-validity evidence |

## Cross-Paper Patterns

### 1. Evaluation is moving beyond lexical similarity

P01 directly attacks text-similarity metrics such as BLEU/ROUGE. P03 argues that offline human-comment similarity is insufficient for production value. P04 and P05 move evaluation toward PR-level and issue-coverage realism. P06 adds semantic context, data-quality filtering, and fine-grained tasks. P07, P10, and P12 add live or production-facing signals such as acceptance, value, reviewer overhead, Outdated Rate, retention, adoption, trust, and explainability. P08 shows that even human-written references can be noisy. P09 combines BLEU with qualitative/user/cost evaluation. P11 adds I/IH/M-Score and the explicit Uncertain category. P13 is especially useful for metric validity because it reports BLEU/BERTScore results but also notes that human evaluation can rank models differently, raising BLEU construct-validity concerns.

**Implication for us:** Our paper should not present “better accuracy” as the main contribution. The stronger framing is that code review evaluation needs task-specific, context-aware, PR-realistic, fine-grained, human-centered, data-quality-aware, mitigation-aware, operational, uncertainty-aware, trust-aware, metric-aware, and trade-off-aware dimensions.

### 2. Context matters, but context quantity and context quality are different

P02 treats hallucination as claim-to-diff misalignment. P03 shows that missing project, framework, language, or surrounding-code context can lead to incorrect or non-actionable comments. P04 shows that adding more context can degrade performance. P05 argues that realistic evaluation needs full project context. P06 adds enriched textual/code context. P07 shows RAG in a live tool. P08 shows that diff/comment pairs can be semantically noisy. P09 reframes context as multi-perspective review coverage. P10 operationalizes context preparation through hunk partitioning, bounded function-level expansion, tree-sitter, and line annotations. P11 adds PR title/body, commit message, file path, imports, context-extended diffs, and retrieved diff-comment exemplars. P12 reframes context as specification grounding. P13 adds another important nuance: function call graphs can help, while code summaries can hurt; the same metadata can be signal or noise depending on model context window, token budget, and attention behavior.

**Implication for us:** Context quality should be evaluated as its own construct. Context should not be represented only by quantity, token count, number of retrieved files, full repository availability, RAG usage, semantic metadata, or specification availability. We need to ask whether context is relevant, complete, specific, clean, usable, review-dimension-covering, project-grounded, specification-grounded, fresh, bounded, and worth its token/cost budget.

### 3. Gate-like, filtering, cleaning, retrieval, prompting, fine-tuning, and aggregation are different mitigation choices

P02 uses hallucination detection. P03/P10 use quality gates and production filters. P05 uses multi-review aggregation. P06/P08/P11 use filtering/cleaning for dataset quality. P07 uses LLM-as-a-Judge before reviewer exposure. P09 uses multi-agent generation. P10 uses RuleChecker, ReviewFilter, rule blockers, aggregation, and a data flywheel. P11 uses context augmentation, retrieval exemplars, and systematic guidance. P12 uses explicit specification injection, implicit specification discovery, specification retrieval, verifier ensembles, and aggregation. P13 compares another family of mitigations: QLoRA fine-tuning, few-shot prompting, BM25 exemplar retrieval, function call graph augmentation, and code-summary augmentation.

**Implication for us:** A mitigation strategy should be evaluated by what it reduces, what useful feedback it preserves or suppresses, what cost/latency/complexity it adds, whether it improves trust and traceability, and whether it introduces new failure modes such as context distraction, checklist fixation, prompt sensitivity, or poor generalization.

### 4. Production and live-study metrics are valuable but noisy

P03, P07, P10, and P12 provide the strongest workflow-facing signals. P03 gives PR cycle time, code resolution, human-comment reduction, and developer feedback. P07 separates acceptance, perceived value, reviewer overhead, and downstream patch revisions. P10 adds WAU/WPV, retention, Outdated Rate, weekly precision, survey, and interviews. P12 adds production adoption rate and developer feedback on trust/explainability. P11 and P13 are not live deployment studies, but they add useful human-evaluation designs: P11 uses Instrumental/Helpful/Uncertain/Misleading; P13 uses developer-rated relevance, information, and explanation clarity.

**Implication for us:** A good framework should combine controlled annotation, benchmark issue coverage, context-quality analysis, data-quality checks, mitigation-specific metrics, uncertainty labels, adoption/retention/workflow signals, and qualitative developer feedback. No single signal is sufficient.

### 5. Human feedback is realistic but incomplete ground truth

P04/P05 use human PR feedback and manually verified issue reports. P03/P07/P10/P12 use developer behavior and feedback in production or live settings. P08/P11 use manual data labels and report agreement. P13 uses professional developers but with only 8 participants and no live workflow signal. Human signals can still mix correctness, priority, preference, style, convenience, trust, workload, missing project context, and non-causal behavior.

**Implication for us:** Human review feedback, benchmark ground truth, and production telemetry should be treated as imperfect evidence, not absolute truth. We need annotation-quality, construct-validity, proxy-validity, and context-availability analysis.

### 6. Usefulness is not the same as direct acceptance, adoption, or similarity

P07 shows that a non-accepted comment may still be valuable. P08 shows that human-written comments can be noisy. P10 shows that technically correct comments can be practically superfluous. P11 separates Instrumental, Helpful, Uncertain, and Misleading. P12 shows that adoption is useful but not equivalent to correctness. P13 shows that a model can look strong under BLEU/BERTScore while human relevance/information/clarity judgments tell a different story.

**Implication for us:** Our framework should distinguish acceptance, adoption, usefulness, actionability, correctness, readability, specificity, sufficiency, operability, information value, explanation clarity, downstream impact, uncertainty, trust, and value-to-attention ratio.

### 7. Data quality is part of evaluation, not just preprocessing

P06 critiques noisy benchmark data. P08 makes noisy review comments central. P10 adds an industrial data flywheel. P11 constructs a filtered context-rich dataset with manual annotation. P12 adds specification-library quality as another data-quality layer. P13 relies on the CodeReviewer dataset and therefore inherits its benchmark limitations, while also showing how subset selection, cost constraints, and top-n best-BLEU selection can affect conclusions.

**Implication for us:** Our framework should include a data-quality layer before output evaluation. The quality of reference comments, linked issues, retrieved context, annotations, training samples, review rules, specifications, semantic metadata, prompt exemplars, and production feedback affects what evaluation results mean.

### 8. Precision-first and context-rich strategies create useful-feedback preservation problems

P10 prioritizes precision to protect trust, but recall suffers. P08 and P11 show that cleaning/filtering can remove useful examples. P12 shows that specification verification can suppress useful but undocumented issues. P13 shows that context augmentation can hurt when metadata is noisy or too long, meaning a strategy that appears to add useful information can suppress model focus on the actual diff.

**Implication for us:** Every gate, filter, cleaner, retrieval step, specification verifier, or context augmenter should report useful-feedback preservation, not just harmful-comment reduction or metric improvement.

### 9. Retrieval, semantic metadata, and context enrichment add both signal and distraction

P06/P11 show context enrichment and RAG can help. P04 warns that more context can degrade performance. P10 shows bounded context preparation is needed. P12 shows long specifications cause attention dilution and explicit specifications can cause checklist fixation. P13 provides concrete metadata evidence: function call graph alone improves GPT-3.5 in ablation, but code summary often degrades performance; GPT-4o benefits more from larger augmented context because of a larger context window.

**Implication for us:** Context quality should include retrieval relevance, exemplar safety, metadata quality, target-diff focus, specification relevance, segmentation, attention load, context-window fit, and marginal value per token.

### 10. Explainability and traceability are evaluation dimensions

P02 grounds hallucination decisions in claim-to-diff alignment. P10 makes rule-level monitoring operationally important. P11 ties generated comments to lines and retrieved examples. P12 makes explainability explicit through links to human-authored specifications. P13 adds explanation clarity as a human-evaluation dimension.

**Implication for us:** The evaluation framework should include traceability and explanation clarity: can the comment be traced to code evidence, retrieved context, semantic metadata, specification, rule, issue report, or human feedback, and is the explanation understandable enough to act on?

### 11. Resource constraints shape evaluation conclusions

P10 reports cost/latency-like operational concerns. P11 uses token thresholds and context caps. P12 uses ensembles and segmentation but does not quantify latency/cost. P13 makes resource constraints explicit: QLoRA enables fine-tuning on 16GB VRAM, closed-source prompting is limited by API cost, and context-window size changes whether augmentation helps or hurts.

**Implication for us:** The trade-off matrix should include computational cost, token budget, API cost, training cost, latency, context-window capacity, and quality-per-cost metrics.

## Emerging Gap Statement

The first thirteen papers show that the field is improving its evaluation of LLM-based code review: moving beyond lexical similarity, introducing richer rubrics, detecting hallucinations, evaluating real deployments, building PR-level benchmarks, adding full-project-context benchmarks, enriching context with issue/PR and surrounding-code information, measuring live reviewer behavior, cleaning noisy training data, designing multi-agent mitigation systems, deploying precision-first industrial review pipelines, using context-enriched RAG with useful/misleading/uncertain human evaluation, grounding review in human-authored specifications, and comparing prompting/fine-tuning/semantic-metadata augmentation strategies. However, they still do not provide a unified framework that jointly evaluates:

- context quality,
- retrieval quality,
- semantic-metadata quality,
- specification quality,
- data quality,
- problematic comment types,
- hallucination and grounding,
- traceability and explanation clarity,
- issue coverage and benchmark ground truth,
- fine-grained localization and comment generation,
- actionability, usefulness, readability, sufficiency, operability, information value, acceptance, adoption, practical utility, uncertainty, trust, and downstream impact,
- preservation of useful comments under filtering, cleaning, aggregation, rule blocking, retrieval, prompt augmentation, specification verification, or multi-agent generation,
- false-positive and false-negative consequences,
- severity-weighted missed issues,
- human annotation, user-study, and production-telemetry validity,
- proxy-validity limits of metrics such as BLEU, BERTScore, Outdated Rate, and adoption rate,
- comprehensiveness vs duplication / cognitive load,
- cost, token budget, latency, training cost, API cost, reviewer overhead, retention, specification maintenance, and workflow impact.

## Working Contribution Direction

A promising contribution is a **taxonomy and trade-off-aware evaluation framework** for LLM-generated code review comments, with special emphasis on context quality, retrieval quality, semantic-metadata quality, specification quality, data quality, human-centered value, traceability, explanation clarity, problematic-comment types, useful-feedback preservation, uncertainty, proxy-validity analysis, and the consequences of filtering, cleaning, prompting, fine-tuning, retrieving, verifying, aggregating, suppressing, blocking, or expanding generated comments.

## Paper-to-Argument Mapping

| Argument Need | Best Supporting Papers | Notes |
|---|---|---|
| Text similarity is insufficient | P01, P03, P04, P05, P06, P07, P08, P09, P10, P11, P12, P13 | P13 is useful because it explicitly raises BLEU construct-validity concerns and shows human-eval differences. |
| Hallucination should be grounded in context | P02, P12, P10, P03, P09, P11 | P13 is secondary; it discusses overconfident incorrect outputs but not a hallucination metric. |
| Context quality matters | P02, P03, P04, P05, P06, P07, P08, P09, P10, P11, P12, P13 | P13 adds call graph/summary augmentation and context-window effects. |
| Retrieval quality matters | P11, P12, P13, P06, P07 | P13 uses BM25 few-shot retrieval; P11 is stronger for RAG exemplars. |
| Semantic metadata quality matters | P13, P11, P10, P06 | P13 is strongest for call graph vs summary trade-off. |
| Specification quality matters | P12, P10 | P12 is strongest; P10’s rule taxonomy is related. |
| Data quality matters | P06, P08, P10, P11, P12, P13, P01, P04, P05 | P13 adds dataset/subset/cost constraints and inherited CodeReviewer limitations. |
| Current work lacks trade-off-aware filtering/aggregation/mitigation analysis | P01-P13 | P13 adds prompting-vs-fine-tuning and semantic-augmentation trade-offs. |
| Human annotation and data quality must be rigorous | P01, P02, P04, P05, P06, P08, P09, P10, P11, P12, P13 | P13 has professional developers but small sample and no extracted agreement metric. |
| Live user-study metrics matter | P03, P07, P09, P10, P12 | P13 is human-eval but not live. |
| Production value needs workflow metrics | P03, P06, P07, P10, P12, P09 | P13 has no workflow signal. |
| Benchmark ground truth is incomplete | P04, P05, P03, P06, P07, P08, P10, P11, P12, P13 | P13’s reliance on CodeReviewer and automatic metrics reinforces this. |
| Issue coverage is a better benchmark target than text overlap | P04, P05, P06, P09, P10, P11, P12 | P13 does not directly measure issue coverage. |
| Fine-grained evaluation is necessary | P06, P01, P10, P11, P09, P12, P13 | P13 adds human relevance/information/clarity but lacks line-level labels. |
| Usefulness must be separated from acceptance/adoption/similarity | P07, P03, P08, P10, P11, P12, P13, P09 | P13 is important for similarity-vs-human-perception tension. |
| Multi-agent mitigation needs cost-aware evaluation | P09, P12, P10, P03, P07, P11 | P13 generalizes the cost point to fine-tuning and prompting. |
| Production filters need useful-comment preservation metrics | P10, P07, P08, P11, P12, P02 | P13 is relevant for context augmentation, not filters. |
| Uncertainty should be explicit in evaluation | P11, P12, P07, P04, P05 | P13 does not formalize uncertainty. |
| Explainability and traceability matter | P12, P02, P10, P11, P13 | P13 adds explanation clarity as a developer-rated metric. |
| Resource-aware evaluation matters | P13, P10, P11, P12, P09 | P13 is strongest for QLoRA/API/context-window constraints. |

## Tensions Worth Highlighting

### Context tension

- **P04:** Adding more context can degrade review performance.
- **P05:** Realistic automated code review needs full project context.
- **P06:** Enriched semantic and code context can improve benchmark realism and performance when extracted and filtered carefully.
- **P07:** RAG context is useful in live tools, but generated comments still need reviewer-facing evaluation.
- **P08:** Even diff/comment pairs can be semantically noisy; data quality affects learning and evaluation.
- **P09:** Multi-perspective review can improve comprehensiveness, but broader generation adds cost and may increase attention load.
- **P10:** Bounded, structured context preparation is needed to control token cost and make model input usable.
- **P11:** PR metadata, extended diffs, and retrieved exemplars help, but too much or poorly guided context can distract the model.
- **P12:** Specifications improve grounding and trust, but long or incomplete specifications create attention dilution, maintenance, and coverage problems.
- **P13:** Function call graphs can improve generation, while code summaries can degrade it; context-window size changes the impact of augmentation.

This supports our central framing: the question is not whether to add more context, but how to evaluate, select, clean, retrieve, bound, segment, annotate, maintain, and use high-quality context under cost, data-quality, specification-quality, metadata-quality, and attention constraints.

### Usefulness tension

- **P03:** Code resolution and workflow metrics show practical value.
- **P07:** Direct acceptance is modest, but perceived value and downstream patch revisions still matter.
- **P08:** A comment may be present in a human dataset but still be too noisy, vague, or non-actionable to be useful.
- **P09:** More comprehensive comments may be helpful/readable, but cost, latency, and potential duplication still matter.
- **P10:** A comment can be technically correct but practically superfluous, so precision alone is not enough.
- **P11:** A comment can be helpful, misleading, or uncertain depending on ground-truth overlap and available project context.
- **P12:** A comment can be adopted because it is trusted and convenient, but adoption is not automatically correctness.
- **P13:** A comment can score well under BLEU/BERTScore while not being preferred by professional developers.

### Mitigation tension

- **P02:** Detect and suppress hallucinated/context-misaligned comments.
- **P08:** Clean noisy training data before generation.
- **P07:** Filter generated comments before reviewer exposure.
- **P09:** Expand review generation through multi-agent perspectives.
- **P10:** Use RuleChecker, ReviewFilter, rule blockers, comment aggregation, and rule-level data flywheel optimization in production.
- **P11:** Use context augmentation, retrieval exemplars, and systematic guidance to improve usefulness.
- **P12:** Use explicit specification injection and implicit specification discovery to balance controllability and discovery.
- **P13:** Use QLoRA fine-tuning, few-shot prompting, and semantic metadata augmentation, each with different cost and failure modes.

### Precision-vs-recall tension

- **P10:** Prioritizing precision protects trust and reduces alert fatigue, but suppresses recall.
- **P05/P06:** Benchmark issue coverage and fine-grained recall remain important for evaluating whether models actually find issues.
- **P07:** Some non-accepted comments may still be valuable.
- **P11:** LLM-based dataset filtering reduces low-quality data but removes some high-quality examples.
- **P12:** Explicit specification grounding increases adoption, but may miss useful issues outside explicit specifications unless supported by implicit discovery.
- **P13:** Top-n generation followed by best BLEU selection can overestimate metric performance without showing practical preservation of useful feedback.

### Grounding-vs-discovery tension

- **P02:** Grounding reduces hallucination.
- **P11:** Retrieval adds useful examples but can distract.
- **P12:** Explicit specifications increase control and trust, but can cause checklist fixation; implicit discovery broadens coverage but needs verification.
- **P13:** Semantic metadata may ground model generation in program structure, but noisy/overlong metadata can distract from the actual diff.

## Update Rule

Update this matrix after every 3–5 completed paper notes. New papers should be added only if they change at least one synthesis claim, taxonomy category, evaluation dimension, or gap statement.
