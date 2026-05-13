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
| P06 — ContextCRBench | Fine-grained benchmark with enriched textual/code context | Critiques missing semantic context, noisy data, and coarse granularity | Context enrichment is not the same as full context-quality scoring; cost and filtering trade-offs remain underdeveloped | Semantic context + data-quality + fine-grained evaluation |
| P07 — RevMate user study | Live open-/closed-source user study | Measures acceptance, perceived value, reviewer overhead, and downstream patch revisions | Acceptance/value are useful but do not fully isolate correctness; wrong removals by judge/filter remain underexplored | Human-centered evaluation + usefulness-vs-cost trade-off |
| P08 — Too Noisy To Learn | Data-quality cleaning for review-comment generation | Shows noisy, vague, and non-actionable review comments harm learning | Focuses on dataset cleaning rather than deployment-time filtering; valid/noisy can bundle correctness, usefulness, and actionability | Data-quality layer + noisy-comment taxonomy + filtering trade-offs |
| P09 — Hydra-Reviewer | Multi-agent review-comment generation | Concrete mitigation for lack of comprehensiveness, incorrectness, and vagueness | Needs deeper verification of prompts, agents, datasets, and user-study protocol; does not fully model harmful-comment reduction or useful-feedback preservation | Multi-agent mitigation + comprehensiveness + quality/cost trade-off |
| P10 — BitsAI-CR | Industrial LLM code review deployment | Strong production evidence: taxonomy, RuleChecker, ReviewFilter, Outdated Rate, survey/interviews, WAU/WPV, retention, and data flywheel | Private data limits reproducibility; Outdated Rate is a proxy not causal proof; precision-first filtering may lose useful comments | Industrial deployment + filter/gate trade-offs + proxy acceptance metrics |
| P11 — LAURA | Context-enriched RAG code review generation | Strong evidence for context augmentation, review exemplar retrieval, systematic guidance, high-quality dataset construction, I/IH/M-Score, and ablation | Not a live deployment; retrieval/context can distract; LLM filtering may remove useful samples; human usefulness remains limited by missing project context | Context-quality model + RAG trade-offs + useful/misleading/uncertain evaluation |
| P12 — SGCR | Specification-grounded trustworthy code review | Strong industrial evidence for human-authored specifications, explicit/implicit pathways, adoption-rate improvement, explainability, and trust | Adoption rate bundles correctness/usefulness/trust; specification maintenance and freshness are under-modeled; useful undocumented issues may be suppressed | Specification grounding + trust/explainability + explicit-vs-implicit trade-off |
| P13 — Prompting and Fine-tuning LLMs for Code Review | Prompting, QLoRA fine-tuning, and semantic metadata augmentation | Shows prompting/QLoRA can outperform CodeReviewer; call graphs can help; summaries/excessive context can hurt; human evaluation can disagree with BLEU/BERTScore | Small human study; no live workflow; heavy reliance on automatic metrics; no explicit harmful-comment/actionability labels | Resource-aware adaptation + semantic context trade-offs + metric-validity evidence |
| P14 — CodeReviewer | Foundational pre-trained code review model and benchmark | Introduces diff-hunk-based CodeReview dataset, CodeReviewer model, review-generation baseline, information/relevance human evaluation, and early BLEU critique | Hunk-level/single-comment setup loses PR/project/multi-reviewer context; BLEU and human references remain limited; no live workflow | Foundational baseline + benchmark-history + hunk-level context + BLEU/single-reference critique |
| P15 — LLaMA-Reviewer | PEFT adaptation for code review automation | Shows LoRA/prefix tuning, input representation, instruction tuning, and thresholding affect review tasks under resource constraints | BLEU-heavy; no human/workflow validation; no hallucination/actionability taxonomy | Resource-aware adaptation + PEFT trade-offs + threshold effects |
| P16 — Context-Aware Code Review Automation | RAG with expert routing | Shows context collapse, model-capacity-dependent RAG effects, hybrid routing, hallucination rate, severity overestimation, and LLM-judge calibration | Python/Home Assistant-specific; relies partly on LLM-as-judge; routing adds operational complexity | Retrieval depth + context collapse + model routing + evaluator calibration |
| P17 — CodeReviewQA | Comprehension benchmark | Decomposes code review understanding into CTR, CL, and SI probes; manually curates clean examples and checks contamination | MCQA probes are diagnostic but not full workflow; benchmark is small after strict filtering | Comprehension-step evaluation + contamination-aware benchmark design |
| P18 — CuRev / Curated Code Reviews | Data-quality curation | Defines type/nature/civility plus relevance/clarity/conciseness; filters/reformulates noisy comments; validates LLM-as-judge; improves downstream generation/refinement | Reformulation may change intent; relevance filtering may remove context-dependent useful comments; downstream metrics still include BLEU/CodeBLEU | Reference-quality layer + clarity/relevance/civility + LLM-as-judge calibration |
| P19 — Fine-Grained Review Comment Classification | Usefulness-linked taxonomy/classification | Classifies 17 review-comment categories linked to practitioner usefulness; shows LLMs help rare/useful categories | Single OpenStack dataset; moderate original annotation agreement; classification does not prove correctness/actionability | Taxonomy layer + usefulness categories + prioritization/evaluation support |
| P20 — RAG-Reviewer | Retrieval-augmented comment generation | Shows pair retrieval beats singleton, RAG improves EM/BLEU and low-frequency-token generation, and manual semantic equivalence improves | Java/Tufano-only; manual analysis is small; BLEU/EM still dominant; no live acceptance | Retrieval-quality + exemplar design + low-frequency-token coverage + token-budget trade-off |
| P21 — iCodeReviewer | Secure code review with mixture-of-prompts | Defines secure review as category + location + comment; uses feature-grounded prompt expert routing; reports issue F1, localization accuracy, I/H/M/U, and production acceptance | Private data; one-week deployment; routing false negatives and prompt-expert maintenance are under-modeled; no detailed cost/latency | Secure-review evaluation + routing-vs-coverage + category/location/helpfulness metrics |
| P22 — Combining LLMs with Static Analyzers | Hybrid static-analysis + LLM review generation | Compares DAT, RAG, and NCO; shows static-analyzer output is useful only when integrated carefully; calibrates LLM judge | Java/PMD/Checkstyle-specific; LLM-as-judge remains central; no live workflow | Hybrid mitigation + static-analysis context + accuracy/coverage trade-off |
| P23 — Leveraging Reviewer Experience | Reviewer-experience-aware training | Uses reviewer authoring/reviewing ownership as data-quality signal; evaluates applicability, semantic equivalence, informativeness, explanation, and issue types | Experience is only a proxy; open-source-only; manual sample is small | Data provenance + reviewer expertise + usefulness-linked reference quality |
| P24 — Reward Models for Code Review | RL/reward-guided comment generation | Uses semantic-similarity and downstream code-refinement rewards; validates o3-mini usefulness judgment with humans | Reward model may be imperfect; BLEU still dominant; no live developer outcome | Downstream usefulness + reward-model trade-offs + actionability proxy |
| P25 — Carllm | Comprehensible automated code review | Defines comprehensibility as issue detection, localization, explanation, and repair suggestion; uses CoT data curation and balanced loss | ChatGPT-annotated data may contain artifacts; no live deployment; ternary clarity labels are coarse | Structured evaluation + comprehensibility chain + decoding stability |
| P26 — Human-AI Synergy in Agentic Code Review | Human vs AI-agent review workflow | Large-scale GitHub analysis of feedback type, verbosity, interaction patterns, suggestion adoption, and code-quality impact | Public GitHub only; agent identity and PR status are proxies; metrics do not capture full semantic quality | Human-AI workflow + adoption + code-quality impact + oversight needs |
| P27 — From Industry Claims to Empirical Reality | CRA PR outcome and signal-to-noise | Links CRA-only review with lower merge rate, higher abandonment, and low signal ratios | Correlational; keyword/open-coding signal heuristic; AIDev/GitHub only | CRA signal-to-noise + abandonment proxy + human oversight |
| P28 — Support, Not Automation | Human-centered AI-supported review | Frames code review as socio-technical practice: knowledge transfer, team awareness, shared ownership, rationale tracking | Vision paper; no implemented system or empirical evaluation | Human-in-the-loop framing + socio-technical evaluation dimensions |
| P29 — Can LLMs Replace Human Evaluators? | LLM-as-a-judge validity in SE | Shows judge performance is task-dependent; output-based large judges best; pairwise comparisons are unstable | Not code-review-specific; 450 human-scored responses | Judge calibration + task dependence + pairwise/order-bias warning |
| P30 — CodeUltraFeedback | LLM-as-a-judge preference dataset | Defines five coding preferences and uses judge labels for SFT/DPO alignment; shows judge-selection sensitivity | Not code-review-specific; labels depend on GPT-3.5/4; reference-guided judging | Preference dimensions + judge-choice sensitivity + non-functional evaluation |
| P31 — CodeJudgeBench | Coding-task judge benchmark | 5,352 pairs, 26 judges; thinking judges perform best; position/source/preprocessing sensitivity exposed | Not review-comment-specific; correctness-focused and execution-free | Robustness checks for LLM-as-a-judge + prompting/preprocessing trade-offs |

## Cross-Paper Patterns

### 1. Evaluation is moving beyond lexical similarity, but old metrics still dominate

P14 already recognized that BLEU is weak for review comment generation because review comments are diverse and non-unique. Later work extends this concern in many directions: P01 critiques text similarity directly; P11/P21 use I/H/M/U-style categories; P16/P18/P22 calibrate LLM-as-a-Judge with human labels; P17 decomposes correctness into comprehension probes; P18 adds relevance, clarity, conciseness, and civility; P20 adds semantic-equivalence and alternative-solution labels; P23 evaluates semantic equivalence, applicability, informativeness, explanation, and issue type; P24 evaluates downstream code-refinement usefulness through rewards; P25 evaluates clarity/comprehensibility; P26 measures suggestion adoption and code-quality deltas; P27 adds signal-to-noise and abandonment; P29/P31 warn that LLM judges themselves are unstable; and P30 adds non-functional coding preferences. Still, BLEU, EM, CodeBLEU, BERTScore, and ROUGE remain common.

**Implication for us:** The field has known for years that lexical overlap is incomplete, but evaluation practice still inherits single-reference and similarity-score assumptions. Our contribution should synthesize richer evidence into a trade-off-aware framework, not just propose another metric.

### 2. Context quality is now broader than code context

Earlier papers focus on diff hunks, PR context, repository context, RAG exemplars, and specifications. P22 adds static-analysis output as structured context. P23 adds reviewer experience and ownership as provenance signals. P24 adds downstream refinement as evaluation context. P25 treats context as a structured reasoning chain: issue decision, location, explanation, and repair. P26 adds socio-technical project context. P28 explicitly broadens context to requirements, issue trackers, CI, API docs, team process, user preferences, and rationale. P29/P31 show that evaluator prompts and response formatting are also context: a judge can fail because it misunderstands task intent, response order, source model style, or preprocessing.

**Implication for us:** Context quality should include code context, retrieval context, static-analysis context, reviewer/provenance context, specification context, structured reasoning context, downstream repair context, socio-technical workflow context, and evaluator-context quality.

### 3. Data, reference, and provenance quality are first-class evaluation concerns

P14/P08/P18 show that human review comments are noisy or incomplete. P17 shows strict benchmark curation improves reliability but reduces coverage. P22 shows static-analysis-based data can improve coverage but may introduce contradictions. P23 shows human reference quality depends on reviewer experience. P25 shows raw comments are too sparse for comprehensible ACR and need logic-rich curation. P26 shows real-world agent/human comments differ in verbosity, scope, and adoption. P30 shows preference labels can be created at scale but become judge-dependent. P31 shows hard, recent, carefully paired benchmarks can expose failures hidden by easier judge benchmarks.

**Implication for us:** Evaluation must model reference completeness, provenance, clarity, annotation reliability, multiple-valid-comment cases, reviewer expertise, judge provenance, and workflow origin.

### 4. Taxonomy should combine harmfulness, usefulness, type, severity, workflow effect, and evaluator failure

The taxonomy should include hallucination, irrelevance, vagueness, non-actionability, wrong location, wrong category, redundancy, severity miscalibration, uncivil/unclear comments, generic high-frequency output, low-frequency-token omission, confused questions, hybrid contradictions, missing explanation, missing repair suggestion, verbose/narrow AI-agent feedback, incorrect AI code suggestions, complexity-increasing adopted suggestions, low-signal CRA comments, automation that removes knowledge-transfer value, task-misaligned judges, verbosity-biased judges, position-biased judges, and preprocessing-sensitive judges.

**Implication for us:** The final taxonomy should not be only about generated review comments. It should also include evaluator failure modes and workflow-level harms.

### 5. Mitigation strategies should be compared as trade-off choices

The papers cover many mitigation families: diff-aware pre-training, PEFT, hallucination detection, data cleaning/reformulation, RAG, LLM-as-a-Judge filtering, rule checking, multi-agent review, specification grounding, semantic metadata, comprehension probes, taxonomy/classification, prompt routing, static-analyzer hybrids, reviewer-experience weighting, RL rewards, CoT fine-tuning, human-AI workflow oversight, signal-to-noise monitoring, support-not-automation architectures, preference tuning, and thinking-judge evaluation.

**Implication for us:** The trade-off matrix should compare what each strategy reduces, what useful feedback it may suppress, what it costs, and what new failure modes it introduces.

### 6. Useful-feedback preservation is still under-measured

Many methods reduce harmful comments or improve metrics, but few report what useful feedback is lost. P10/P21 optimize precision/routing and may miss issues. P11/P18/P25 clean or restructure data and may remove context-dependent signals. P22 hybridizes static analyzers and LLMs but can introduce contradictions. P23 weights experienced reviewers but may down-weight useful novice perspectives. P24 rewards downstream refinability but may favor model-easy comments. P26 shows adopted AI suggestions may still increase complexity. P27 shows CRA comments can be present but low-signal. P28 warns that automation may preserve defect detection while losing knowledge transfer, team awareness, and shared ownership.

**Implication for us:** Every filter, cleaner, retriever, router, reward, judge, or workflow policy should report harmful-comment reduction and useful-feedback preservation separately, including socio-technical value preservation.

### 7. LLM-as-a-Judge is useful but validity is fragile

P16/P18/P22/P24 calibrate LLM judges with human labels. P29 shows that such calibration is task-dependent: judges can align well on code translation, be comparable on code generation, and fail on summarization. P30 shows judge choice changes preference scores and model rankings. P31 shows coding judges are sensitive to response order, source model, prompt format, and preprocessing; thinking judges help but add cost and still lack full robustness.

**Implication for us:** LLM-as-a-Judge should be evaluated as a measurement instrument. The framework should require task-specific rubrics, human spot checks, order-swap tests, judge-choice sensitivity analysis, source-model sensitivity analysis, preprocessing sensitivity analysis, and cost reporting.

### 8. Structured review output is becoming essential

P21 defines secure review as category + location + comment. P25 defines comprehensible review as issue detection + location + explanation + repair suggestion. P17 decomposes comprehension into change type, localization, and solution identification. P26 evaluates suggestions by adoption and code-quality impact. P27 evaluates comment streams by signal density. P30 evaluates coding output by preference dimensions. P31 evaluates judge decisions by task, difficulty, and robustness properties.

**Implication for us:** Evaluation should not treat review comments as a single text string. It should evaluate structured subclaims, comment streams, and downstream outcomes separately.

### 9. Human-AI workflow is now part of code-review evaluation

P26 shows that AI agents are scalable but verbose, narrow, less interactive, and lower-adoption than humans. P27 shows CRA-only PRs have lower merge rates and higher abandonment than human-only PRs. P28 argues that review should be supported, not automated, because review preserves knowledge transfer, team awareness, shared ownership, rationale tracking, and accountability.

**Implication for us:** A trade-off-aware framework must include reviewer attention, verbosity, interaction rounds, human-final-response need, signal-to-noise, suggestion adoption, code-quality deltas, knowledge transfer, team awareness, and shared ownership.

## Emerging Gap Statement

The first thirty-one papers show that the field is improving its evaluation of LLM-based code review: from diff-aware pre-training and BLEU-plus-human evaluation to richer rubrics, hallucination detection, PR-level benchmarks, context enrichment, live studies, data cleaning, multi-agent systems, production filters, RAG, specification grounding, PEFT, semantic metadata, comprehension probes, curated references, usefulness-linked taxonomies, secure-review routing, static-analyzer hybrids, reviewer-experience weighting, reward-guided generation, comprehensible ACR, agentic human-AI workflow analysis, CRA signal-to-noise analysis, AI-supported review visions, and LLM-as-a-judge robustness benchmarks. However, they still do not provide a unified framework that jointly evaluates:

- context quality, context granularity, and model-capacity fit,
- retrieval quality, exemplar quality, static-analysis context quality, and evaluator-context quality,
- feature-grounded routing and prompt-expert maintenance,
- semantic-metadata quality and specification quality,
- reference/comment/data quality, reviewer-experience provenance, and judge-label provenance,
- hallucination, grounding, false positives, false negatives, severity calibration, category correctness, and location correctness,
- traceability, explanation clarity, issue detection, localization, repair suggestion, downstream refinability, and signal-to-noise,
- usefulness, relevance, information value, clarity, conciseness, civility, applicability, semantic equivalence, acceptance, adoption, uncertainty, trust, workflow impact, and abandonment,
- socio-technical review value: knowledge transfer, team awareness, shared ownership, rationale tracking, accountability, and reviewer learning,
- useful-feedback preservation under filtering, cleaning, reformulation, routing, aggregation, static-analysis hybridization, reward optimization, specification verification, judge-based filtering, or agentic review,
- human annotation, LLM-as-a-Judge, user-study, production-telemetry, and code-metric validity,
- LLM-judge task dependence, position/order bias, source-model sensitivity, prompt-format sensitivity, preprocessing sensitivity, and judge-selection sensitivity,
- proxy-validity limits of BLEU, BERTScore, ROUGE, EM, CodeBLEU, LLM-judge scores, Outdated Rate, acceptance rate, adoption rate, signal-to-noise ratio, abandonment, and code metric deltas,
- cost, token budget, latency, training cost, API cost, routing cost, reward-model cost, judge cost, expert-maintenance cost, reviewer overhead, retention, and human-AI interaction cost.

## Working Contribution Direction

A promising contribution is a **taxonomy and trade-off-aware evaluation framework** for LLM-generated code review comments, with special emphasis on context quality, retrieval/static-analysis/specification quality, reference provenance, reviewer experience, structured review outputs, downstream usefulness, signal-to-noise, socio-technical review benefits, evaluator validity, problematic-comment types, useful-feedback preservation, proxy-validity analysis, and the consequences of filtering, cleaning, prompting, fine-tuning, pre-training, retrieving, routing, rewarding, judging, verifying, aggregating, suppressing, blocking, or expanding generated comments.

## Paper-to-Argument Mapping

| Argument Need | Best Supporting Papers | Notes |
|---|---|---|
| Text similarity is insufficient | P14, P01, P11, P13, P16, P17, P18, P20, P21, P22, P23, P24, P25, P26, P29, P30, P31 | P29/P31 show even replacement judges require robustness checks. |
| Context quality matters | P14, P04, P05, P06, P10, P11, P12, P13, P16, P17, P20, P21, P22, P25, P26, P28, P29, P31 | P28 adds workflow/rationale context; P29/P31 add evaluator-context quality. |
| Data/reference quality matters | P14, P08, P18, P17, P11, P19, P20, P21, P22, P23, P25, P26, P30, P31 | P30 adds judge-labeled preference data; P31 adds challenging curated pairs. |
| Taxonomy/usefulness categories matter | P19, P21, P18, P10, P08, P02, P17, P20, P23, P25, P26, P27, P28, P30 | P27 adds low-signal comments; P28 adds socio-technical value categories. |
| Hybrid mitigation needs trade-off analysis | P22, P10, P21, P11, P12, P16, P20 | P22 directly compares DAT/RAG/NCO. |
| Downstream usefulness matters | P24, P25, P26, P27, P07, P10, P20 | P27 adds abandonment and signal-to-noise. |
| Comprehensibility should be decomposed | P25, P17, P21, P23, P30 | P30 adds explanation/readability/style preferences. |
| LLM-as-a-Judge needs calibration and robustness testing | P16, P18, P22, P24, P29, P30, P31, P11, P10 | P29/P31 add task dependence, order bias, source-model and preprocessing sensitivity. |
| Resource-aware evaluation matters | P14, P15, P13, P16, P20, P21, P22, P24, P25, P26, P29, P31 | P29/P31 add judge/inference cost and thinking-judge trade-offs. |
| Human-AI workflow matters | P26, P27, P28, P07, P03, P10, P12, P21 | P27/P28 strengthen support-not-replacement framing. |
| Useful-feedback preservation is missing | P10, P11, P18, P17, P12, P20, P21, P22, P23, P24, P25, P26, P27, P28 | P28 expands preservation to knowledge transfer and shared ownership. |

## Tensions Worth Highlighting

### Context tension

- **P04:** More context can degrade review performance.
- **P11/P20:** Retrieved exemplars help when relevant and structured.
- **P13:** Call graphs can help, summaries can hurt.
- **P16:** Smaller models can collapse under retrieval context.
- **P21:** Routing reduces false positives but can miss relevant security experts.
- **P22:** Static-analyzer output helps through RAG but post-hoc concatenation can conflict.
- **P25:** Structured CoT context improves clarity but may be rigid.
- **P26/P27:** Missing project/workflow context lowers adoption and signal quality.
- **P28:** Review context includes people, rationale, process, and learning goals, not just code.
- **P29/P31:** Evaluator context matters: task definition, prompt format, answer order, and preprocessing can change judgments.

### Usefulness tension

- **P07:** Non-accepted comments may still be valuable.
- **P10:** Technically correct comments may be practically superfluous.
- **P23:** Experienced-reviewer weighting improves applicability but does not make references absolute truth.
- **P24:** Comments useful for refinement models may not perfectly match human usefulness.
- **P25:** Clear comments require structure, but clarity labels are coarse.
- **P26:** Adopted AI suggestions may still increase complexity more than human suggestions.
- **P27:** CRA comments may exist but still be low-signal and associated with abandonment.
- **P28:** Automation may save time but remove knowledge transfer, team awareness, and shared ownership.

### Mitigation tension

- **P22:** DAT/RAG/NCO represent different static-analysis integration points with different risks.
- **P23:** Weighting by reviewer experience improves quality but may suppress useful low-experience perspectives.
- **P24:** Reward optimization improves target metrics but can be reward-model-dependent.
- **P25:** CoT curation improves comprehensibility but introduces ChatGPT-generated artifacts.
- **P26/P27:** AI agents scale review but still need human oversight for context and signal quality.
- **P28:** Support-oriented AI preserves review value but does not fully remove human effort.
- **P30:** Preference tuning improves alignment but may inherit judge preferences.
- **P31:** Thinking judges improve accuracy but add cost and still suffer robustness issues.

### Ground truth and evaluator-validity tension

- **P14:** Earliest-comment references are incomplete.
- **P18/P25:** LLM-curated references may be clearer but may change intent.
- **P23:** Human reference quality depends on reviewer experience.
- **P24:** Reward models define usefulness through proxies.
- **P26/P27:** Adoption, merge, abandonment, and signal-to-noise are strong workflow signals but not causal proof of semantic correctness.
- **P29:** LLM-as-a-judge works in some SE tasks and fails in others; pairwise evaluation is order-unstable.
- **P30:** Judge choice changes scores and model ranking.
- **P31:** Judge accuracy changes with response order, source model, prompt format, and preprocessing.

## Update Rule

Update this matrix after every 3–5 completed paper notes. New papers should be added only if they change at least one synthesis claim, taxonomy category, evaluation dimension, or gap statement.
