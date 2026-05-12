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
| P09 — Hydra-Reviewer | Multi-agent review-comment generation | Provides a concrete mitigation strategy for lack of comprehensiveness, incorrectness, and vagueness; reports qualitative, user-study, ablation, cost, and latency evidence | Needs deeper verification of prompts, agents, datasets, and user-study protocol; does not fully model harmful-comment reduction or useful-feedback preservation | Multi-agent mitigation + comprehensiveness + quality/cost trade-off |
| P10 — BitsAI-CR | Industrial LLM code review deployment | Strong production evidence: 219-rule taxonomy, RuleChecker, ReviewFilter, comment aggregation, Outdated Rate, survey/interviews, WAU/WPV, retention, and data flywheel | Private data limits reproducibility; Outdated Rate is a proxy not causal proof; precision-first filtering may lose useful comments | Industrial deployment + filter/gate trade-offs + proxy acceptance metrics |
| P11 — LAURA | Context-enriched RAG code review generation | Strong open-source evidence for context augmentation, review exemplar retrieval, systematic guidance, high-quality dataset construction, I/IH/M-Score, and ablation | Not a live deployment; retrieval/context can distract; LLM filtering may remove useful samples; human usefulness remains limited by missing project context | Context-quality model + RAG trade-offs + useful/misleading/uncertain evaluation |
| P12 — SGCR | Specification-grounded trustworthy code review | Strong industrial evidence for grounding LLM review in human-authored specifications, explicit/implicit pathways, adoption-rate improvement, explainability, and trust | Adoption rate bundles correctness/usefulness/trust; specification maintenance and freshness are under-modeled; useful undocumented issues may be suppressed | Specification grounding + trust/explainability + explicit-vs-implicit trade-off |

## Cross-Paper Patterns

### 1. Evaluation is moving beyond lexical similarity

P01 directly attacks text-similarity metrics such as BLEU/ROUGE. P03 also argues that offline human-comment similarity is insufficient for production value. P04 reinforces the same direction by evaluating models against PR-level human review feedback instead of generic code-generation tasks. P05 further strengthens this pattern by arguing that ACR benchmarks should use PR-centric review and structured ground-truth issue coverage. P06 adds that benchmark realism also requires semantic context, data quality filtering, and fine-grained tasks. P07 extends the shift to live reviewer behavior, showing that acceptance, perceived value, and reviewer overhead are distinct from offline quality. P08 adds that even human-written training/reference comments may be noisy, vague, or non-actionable. P09 shows a system-level evaluation pattern that combines BLEU with qualitative review-dimension coverage, user study, ablation, and cost analysis. P10 adds production-grade metrics such as precision, recall, filter rate, inference time, Outdated Rate, retention, WAU/WPV, survey responses, and expert interviews. P11 adds human usefulness categories and LLM metrics for readability, relevance, brevity, sufficiency, and operability. P12 adds adoption rate, developer trust, explainability, specification traceability, and component ablation in a production setting.

**Implication for us:** Our paper should not present “better accuracy” as the main contribution. The stronger framing is that code review evaluation needs task-specific, context-aware, PR-realistic, fine-grained, human-centered, data-quality-aware, mitigation-aware, operational, uncertainty-aware, trust-aware, and trade-off-aware dimensions.

### 2. Context matters, but context quantity and context quality are different

P02 treats hallucination as claim-to-diff misalignment. P03 shows that missing project, framework, language, or surrounding-code context can lead to incorrect or non-actionable comments. P04 provides the strongest counterexample to naive context expansion: performance can degrade as more context is added. P05 argues that realistic ACR evaluation should include full project context. P06 adds another layer: enriched textual context and code context can improve benchmark realism and model performance when extracted and filtered carefully. P07 shows a practical RAG-based assistant where code/review context and LLM-as-a-Judge filtering affect live reviewer exposure. P08 shows that semantic alignment between diff and comment matters even before generation, because noisy comments in the dataset can harm learning. P09 reframes context coverage as multi-perspective review: useful context must be turned into review dimensions rather than merely passed as raw input. P10 operationalizes context quality through hunk partitioning, bounded function-level expansion, tree-sitter-based boundary detection, and line-level old/new annotations. P11 makes context quality even more explicit through PR title, PR body, commit message, file path, language, imports, context-extended diffs, line-number annotations, and retrieved diff-comment exemplars. P12 reframes context quality as specification grounding: human-authored business, security, performance, quality, and architectural rules become an authoritative source of truth.

**Implication for us:** Context quality should be evaluated as its own construct. Context should not be represented only by quantity, token count, number of retrieved files, full repository availability, RAG usage, or even context enrichment. We need to ask whether the context is relevant, complete, specific, clean, usable, review-dimension-covering, project-grounded, specification-grounded, fresh, and bounded enough to avoid attention/cost overload.

### 3. Gate-like, filtering, cleaning, and aggregation mechanisms are promising but under-theorized

P02 is explicitly a safeguard/gate for hallucinated comments. P03 uses quality gates for factual correctness and actionability. P05 reports a multi-review aggregation strategy that improves F1 by synthesizing multiple review sources and filtering invalid points. P06 uses rule-based and LLM-based filtering to improve dataset quality. P07 uses LLM-as-a-Judge to discard irrelevant generated comments before reviewer exposure. P08 uses semantic data cleaning to retain valid comments and remove noisy training examples. P09 uses multi-agent collaboration and review-dimension coverage as a mitigation strategy for incomplete, incorrect, and vague comments. P10 uses RuleChecker, ReviewFilter, rule blockers, and embedding-based comment aggregation to improve precision and reduce redundant/low-quality feedback. P11 uses rule-based and LLM-based dataset filtering, retrieval exemplars, and structured guidance rather than a deployment-time gate. P12 uses explicit specification injection, implicit specification discovery, retrieval-backed verification, ensemble LLM reviewers, verifier ensembles, and final aggregation. P01 is an evaluation framework rather than a deployment gate, but it supports post-generation quality assessment.

**Implication for us:** A gate, filter, cleaner, blocker, retrieval step, verification step, specification path, or aggregation strategy should be evaluated not only by how much it improves F1, BLEU, precision, adoption, or quality scores, but also by what useful comments or samples it suppresses, how much cost/latency it adds, whether it increases or reduces duplicate/low-value feedback, whether retrieved context distracts the model, whether specifications are fresh and complete, and when it should escalate to humans.

### 4. Production and live-study metrics are valuable but noisy

P03 provides real workflow metrics: code resolution, PR cycle time, reduced human-written comments, and developer feedback. P06 reports industrial deployment at ByteDance with a 61.98% improvement in a self-evolving code review system. P07 measures live reviewer behavior in Mozilla and Ubisoft: accepted comments, valuable tips, reviewer time overhead, and downstream patch revisions. P09 includes user-study evidence for helpfulness/readability and cost/latency evidence, but not full production workflow impact. P10 provides the strongest operational deployment signal so far: more than 12k weekly active users, 210k weekly page views, user retention, survey/interview results, weekly precision trends, and Outdated Rate. P11 is not a production study, but it adds a useful “Uncertain” human-evaluation category to avoid overclaiming usefulness when evaluators lack project context. P12 adds adoption rate in a live Java production workflow and qualitative developer feedback about trust, explainability, relevance, noise reduction, education, and specification-maintenance overhead.

**Implication for us:** A good framework should combine controlled annotation, benchmark issue coverage, context-quality analysis, data-quality checks, mitigation-specific metrics, uncertainty labels, adoption/retention/workflow signals, and qualitative developer feedback, instead of treating any one of them as sufficient.

### 5. Human feedback is realistic but incomplete ground truth

P04 uses human PR feedback as a benchmark target. P05 uses manually verified PRs and structured ground-truth reports. P03 uses developer behavior and feedback in production. P06 constructs a large benchmark through issue/PR linkage and multi-stage filtering. P07 uses live reviewer acceptance and value judgments. P08 uses manual valid/noisy labels and reports annotation agreement challenges. P09 uses a user study for helpfulness/readability, but protocol details still need verification. P10 uses manual precision sampling, likes/dislikes, surveys, expert interviews, and line-change-based Outdated Rate. P11 uses human evaluation with Instrumental, Helpful, Uncertain, and Misleading categories, and explicitly notes that evaluators may lack enough project context to judge usefulness confidently. P12 uses adoption rate and developer interviews/surveys, but adoption bundles correctness, usefulness, priority, convenience, trust, and team norms. These signals are realistic, but they can still miss valid AI comments or mix correctness with priority, preference, style, trust, workload, team norms, missing context, and non-causal behavior.

**Implication for us:** Human review feedback, benchmark ground truth, and production telemetry should be treated as imperfect evidence, not absolute truth. Structured issue reports, filtering pipelines, annotation agreement, live user studies, production telemetry, adoption rate, and uncertainty labels improve reliability, but they still require annotation-quality, construct-validity, proxy-validity, and context-availability analysis.

### 6. Usefulness is not the same as direct acceptance

P07 is especially important because it separates direct acceptance from perceived value and downstream revisions. Some generated comments are not accepted directly but are still marked valuable as review or development tips. P08 adds that a comment can be human-written yet too vague or non-actionable to be useful as training/evaluation data. P09 adds helpfulness and readability as human-centered dimensions alongside comprehensiveness. P10 explicitly separates technical precision from practical utility by showing technically correct but superfluous comments and introducing Outdated Rate as a scalable proxy for developer action. P11 separates Instrumental, Helpful, Uncertain, and Misleading comments, showing that useful feedback can partially match the ground truth or be hard to judge without project-specific context. P12 shows that adoption can reflect trust and relevance, but it still bundles several constructs and should not be treated as correctness alone.

**Implication for us:** Our framework should distinguish acceptance, adoption, usefulness, actionability, correctness, readability, specificity, sufficiency, operability, downstream impact, practical utility, uncertainty, trust, and value-to-attention ratio.

### 7. Data quality is part of evaluation, not just preprocessing

P06 explicitly critiques noisy benchmark data and uses filtering to improve context-enriched benchmark quality. P08 makes this issue central by showing that noisy comments persist in code review generation datasets and that training on predicted-valid comments can improve generated-comment quality. P10 adds an industrial data flywheel: internal comments and static-analysis results are refined, sampled, annotated, monitored, and used to update rules and filters. P11 constructs a high-quality dataset through project selection, rule-based filtering, LLM-based filtering, comment merging, time-based splitting, and manual evaluation-sample annotation. P12 introduces specification-library quality as another data-quality layer: if specifications are stale, incomplete, or poorly maintained, grounded review can still be misleading. P01, P04, and P05 also imply the problem: if reference comments or human feedback are incomplete or noisy, evaluation against them becomes construct-limited.

**Implication for us:** Our framework should include a data-quality layer before output evaluation. The quality of reference comments, linked issues, retrieved context, annotations, training samples, review rules, specifications, retrieval exemplars, and production feedback affects what evaluation results mean.

### 8. Mitigation strategies should be compared as trade-off choices

P02 uses hallucination detection, P05 uses aggregation, P06/P08 use filtering/cleaning, P07 uses LLM-as-a-Judge before reviewer exposure, P09 uses multi-agent review generation, P10 uses a production pipeline with RuleChecker, ReviewFilter, rule blockers, comment aggregation, and rule-level optimization, P11 uses context augmentation, review exemplar retrieval, and systematic guidance, and P12 uses specification grounding with explicit and implicit pathways. These are not interchangeable. They optimize different things and introduce different costs.

**Implication for us:** The paper should compare mitigation strategies by what they reduce, what they preserve, what they cost, where they fail, how they are grounded, and which proxy metrics can or cannot validate their practical value. This directly motivates the trade-off matrix.

### 9. Precision-first deployment creates a useful-comment preservation problem

P10 explicitly prioritizes precision over recall because inaccurate comments damage user trust and create alert fatigue. P07 shows that comments can still be valuable even if not directly accepted. P08 shows that filtering noisy comments can improve quality but may remove borderline useful examples. P11 reports that its LLM-based dataset filter reduces low-quality data but has only 0.606 recall for high-quality comments, meaning useful samples can be removed. P12 shows a related grounding problem: verification against specifications can suppress hallucinations, but it may also suppress useful but undocumented issues if the specification library is incomplete. P02 and P07 show that post-generation filtering can suppress harmful comments but may also suppress useful feedback.

**Implication for us:** Every filter/gate should report not only harmful-comment reduction but also useful-comment preservation. A production-safe system may need severity-weighted recall, value-weighted filtering, uncertainty-aware labels, specification-coverage checks, and escalation rather than simple suppression.

### 10. Retrieval and context enrichment add both signal and distraction

P06 and P11 show that enriched context can improve benchmark realism and generated-comment quality. P11 also shows that retrieved exemplars and systematic guidance interact: without proper guidance, the model may target the exemplar instead of the target diff. P04 shows that more context can degrade performance. P10 shows that production systems need bounded context preparation to control token cost and attention load. P12 adds another version of the same tension: long specification documents can cause attention dilution, requiring segmentation, while strict explicit specification injection can cause checklist fixation.

**Implication for us:** Context quality should include retrieval relevance, exemplar safety, target-diff focus, specification relevance, specification segmentation, attention load, and marginal value per token, not just the presence of RAG, more files, or longer specs.

### 11. Explainability and traceability are evaluation dimensions

P02 grounds hallucination decisions in claim-to-diff alignment. P10 makes rule-level monitoring operationally important. P11 ties generated comments to lines and review examples. P12 makes explainability explicit: developers trust SGCR more because suggestions are linked to human-authored specifications rather than black-box model behavior.

**Implication for us:** The evaluation framework should include traceability: can the comment be traced to code evidence, retrieved context, specification, rule, issue report, or human feedback? Traceability is not just an implementation feature; it affects trust, actionability, and auditability.

## Emerging Gap Statement

The first twelve papers show that the field is improving its evaluation of LLM-based code review: moving beyond lexical similarity, introducing richer rubrics, detecting hallucinations, evaluating real deployments, building PR-level benchmarks, adding full-project-context benchmarks, enriching context with issue/PR and surrounding-code information, measuring live reviewer behavior, cleaning noisy training data, designing multi-agent mitigation systems, deploying precision-first industrial review pipelines with feedback loops, using context-enriched RAG with useful/misleading/uncertain human evaluation, and grounding review in human-authored specifications. However, they still do not provide a unified framework that jointly evaluates:

- context quality,
- retrieval quality,
- specification quality,
- data quality,
- problematic comment types,
- hallucination and grounding,
- traceability and explainability,
- issue coverage and benchmark ground truth,
- fine-grained localization and comment generation,
- actionability, usefulness, readability, sufficiency, operability, acceptance, adoption, practical utility, uncertainty, trust, and downstream impact,
- preservation of useful comments under filtering, cleaning, aggregation, rule blocking, retrieval, specification verification, or multi-agent generation,
- false-positive and false-negative consequences,
- severity-weighted missed issues,
- human annotation, user-study, and production-telemetry validity,
- proxy-validity limits of metrics such as Outdated Rate and adoption rate,
- comprehensiveness vs duplication / cognitive load,
- cost, latency, escalation, reviewer overhead, trust, retention, specification maintenance, and workflow impact.

## Working Contribution Direction

A promising contribution is a **taxonomy and trade-off-aware evaluation framework** for LLM-generated code review comments, with special emphasis on context quality, retrieval quality, specification quality, data quality, human-centered value, traceability, problematic-comment types, useful-feedback preservation, uncertainty, proxy-validity analysis, and the consequences of filtering, cleaning, retrieving, verifying, aggregating, suppressing, blocking, or expanding generated comments through production, specification-grounded, and multi-agent systems.

## Paper-to-Argument Mapping

| Argument Need | Best Supporting Papers | Notes |
|---|---|---|
| Text similarity is insufficient | P01, P03, P04, P05, P06, P07, P08, P09, P10, P11, P12 | P01 is strongest for direct critique; P11 adds I/IH/M-Score; P12 adds adoption/trust/explainability. |
| Hallucination should be grounded in context | P02, P12, P10, P03, P09, P11 | P02 provides claim-to-diff grounding; P12 provides specification grounding; P10 gives production hallucination examples. |
| Context quality matters | P02, P03, P04, P05, P06, P07, P08, P09, P10, P11, P12 | P11 is strongest for concrete context dimensions and RAG; P12 is strongest for specification-grounded context. |
| Retrieval quality matters | P11, P12, P06, P07 | P11 is strongest for retrieval exemplars; P12 adds retrieval of specifications for verification. |
| Specification quality matters | P12, P10 | P12 is strongest; P10’s rule taxonomy and review rules are a related industrial form. |
| Data quality matters | P06, P08, P10, P11, P12, P01, P04, P05 | P12 adds specification-library quality as a new data-quality layer. |
| Current work lacks trade-off-aware filtering/aggregation/mitigation analysis | P01, P02, P03, P04, P05, P06, P07, P08, P09, P10, P11, P12 | P12 makes grounding-vs-discovery and specification-maintenance trade-offs explicit. |
| Human annotation and data quality must be rigorous | P01, P02, P04, P05, P06, P08, P09, P10, P11, P12 | P12 adds developer adoption/interview evidence but needs proxy-validity caution. |
| Live user-study metrics matter | P03, P07, P09, P10, P12 | P12 adds live adoption and developer perception. |
| Production value needs workflow metrics | P03, P06, P07, P10, P12, P09 | P10 is strongest for production adoption at scale; P12 is strongest for specification-grounded adoption rate. |
| Benchmark ground truth is incomplete | P04, P05, P03, P06, P07, P08, P10, P11, P12 | P12 shows adoption is useful but not equivalent to correctness. |
| Issue coverage is a better benchmark target than text overlap | P04, P05, P06, P09, P10, P11, P12 | P12 adds explicit/implicit path coverage and specification coverage. |
| Fine-grained evaluation is necessary | P06, P01, P10, P11, P09, P12 | P12 adds rule/spec-level traceability but lacks detailed line-level metrics in first pass. |
| Usefulness must be separated from acceptance/adoption | P07, P03, P08, P10, P11, P12, P09 | P12 is important because adoption bundles many constructs. |
| Multi-agent mitigation needs cost-aware evaluation | P09, P12, P10, P03, P07, P11 | P12 uses ensembles and aggregators, so cost/latency should be measured. |
| Production filters need useful-comment preservation metrics | P10, P07, P08, P11, P12, P02 | P12 raises useful-but-undocumented issue preservation. |
| Uncertainty should be explicit in evaluation | P11, P12, P07, P04, P05 | P11 has formal Uncertain; P12 needs uncertainty around adoption and spec coverage. |
| Explainability and traceability matter | P12, P02, P10, P11 | P12 is strongest for rule/spec traceability and developer trust. |

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

This supports our central framing: the question is not whether to add more context, but how to evaluate, select, clean, retrieve, bound, segment, annotate, maintain, and use high-quality context under cost, data-quality, specification-quality, and attention constraints.

### Usefulness tension

- **P03:** Code resolution and workflow metrics show practical value.
- **P07:** Direct acceptance is modest, but perceived value and downstream patch revisions still matter.
- **P08:** A comment may be present in a human dataset but still be too noisy, vague, or non-actionable to be useful.
- **P09:** More comprehensive comments may be helpful/readable, but cost, latency, and potential duplication still matter.
- **P10:** A comment can be technically correct but practically superfluous, so precision alone is not enough.
- **P11:** A comment can be helpful, misleading, or uncertain depending on ground-truth overlap and available project context.
- **P12:** A comment can be adopted because it is trusted and convenient, but adoption is not automatically correctness.

This supports another core framing: a generated review comment can be useful even if it is not directly accepted, and accepted, adopted, human-written, technically correct, context-enriched, or specification-grounded comments are not automatically actionable, high-value, or worth reviewer attention.

### Mitigation tension

- **P02:** Detect and suppress hallucinated/context-misaligned comments.
- **P08:** Clean noisy training data before generation.
- **P07:** Filter generated comments before reviewer exposure.
- **P09:** Expand review generation through multi-agent perspectives.
- **P10:** Use RuleChecker, ReviewFilter, rule blockers, comment aggregation, and rule-level data flywheel optimization in production.
- **P11:** Use context augmentation, retrieval exemplars, and systematic guidance to improve usefulness.
- **P12:** Use explicit specification injection and implicit specification discovery to balance controllability and discovery.

These strategies solve different problems. Suppression can reduce harm but lose useful feedback; cleaning can improve training but reduce coverage; multi-agent expansion can improve coverage but increase cost, latency, and reviewer attention load; production filters can improve trust but reduce recall; retrieval can improve relevance but introduce distraction; specification grounding improves traceability but depends on specification coverage and maintenance.

### Precision-vs-recall tension

- **P10:** Prioritizing precision protects trust and reduces alert fatigue, but suppresses recall.
- **P05/P06:** Benchmark issue coverage and fine-grained recall remain important for evaluating whether models actually find issues.
- **P07:** Some non-accepted comments may still be valuable.
- **P11:** LLM-based dataset filtering reduces low-quality data but removes some high-quality examples.
- **P12:** Explicit specification grounding increases adoption, but may miss useful issues outside explicit specifications unless supported by implicit discovery.

This supports a severity- and value-aware evaluation design: recall should not be ignored, but it should be measured in terms of missed useful/high-severity/spec-relevant feedback, not only raw issue count.

### Grounding-vs-discovery tension

- **P02:** Grounding reduces hallucination.
- **P11:** Retrieval adds useful examples but can distract.
- **P12:** Explicit specifications increase control and trust, but can cause checklist fixation; implicit discovery broadens coverage but needs verification.

This supports a framework dimension for “grounding strategy”: diff-grounding, retrieval-grounding, specification-grounding, and human-feedback grounding should be evaluated differently.

## Update Rule

Update this matrix after every 3–5 completed paper notes. New papers should be added only if they change at least one synthesis claim, taxonomy category, evaluation dimension, or gap statement.
