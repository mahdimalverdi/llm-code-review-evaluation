# Methodology

This study is designed as a controlled empirical comparison of mitigation strategies for problematic LLM-generated code review comments. The goal is not to conduct a broad survey of LLMs for software engineering, to build a leaderboard benchmark, or to identify one universally best review assistant. Instead, the study asks a narrower empirical question: when a review assistant produces potentially problematic comments, which mitigation strategies reduce which kinds of problems, and what do they cost in useful feedback, review coverage, human effort, and computation?

The methodology follows a bounded empirical-software-engineering design: the research questions, units of analysis, comparison conditions, annotation constructs, reliability checks, scope limits, and reproducibility artifacts are made explicit before the final analysis [@m05_paulralph2020]. Because the study involves LLM-based systems, the design also treats model versions, prompts, context construction, verifier behavior, human validation, and limitations as reportable methodological objects rather than incidental implementation details [@m06_sebastianbaltes2025].

The literature synthesis and taxonomy are therefore supporting components, not the primary identity of the paper. A focused review of prior work is used to define the failure categories, evaluation dimensions, and representative mitigation strategies. The main methodological object is the comparative evaluation: the same code-review instances are processed under a bounded set of representative strategies, the resulting comments and decisions are annotated, and the strategies are compared through both error-reduction and preservation metrics.

This design follows the paper's central motivation: reducing problematic comments is not sufficient by itself. A strategy can remove unsupported, irrelevant, or non-actionable comments while also removing useful weak signals, decreasing automatic review coverage, increasing latency, or shifting the burden to human reviewers. The study therefore evaluates mitigation as a trade-off, not as a single success/failure outcome.

## Study Design

The study has five stages:

1. a targeted literature review to define failure categories, evaluation dimensions, and strategy families;
2. construction and pilot refinement of an operational taxonomy of problematic generated review comments;
3. selection of a shared evaluation sample and generation of baseline review comments;
4. application of several representative mitigation strategies to the same sample;
5. human annotation and trade-off analysis of the resulting comments and mitigation decisions.

The study uses two related units of analysis. The **review instance** is the unit for coverage, escalation, context-quality, and cost analysis. A review instance contains a code change and, where available, review-relevant textual context such as a commit message, pull-request description, issue description, previous discussion, surrounding code, or retrieved project context. The **generated review comment** is the unit for comment-quality, failure-type, usefulness, actionability, and grounding analysis. This distinction is necessary because some strategies may produce no comment for an instance and instead suppress, defer, or escalate it. The same base review instances are used across strategies so that observed differences are attributable to the mitigation strategy rather than to different input distributions.

This unit structure is consistent with prior work on generated review comments, pull-request-level review benchmarks, context-enriched review datasets, and code-review automation datasets [@p01_lu2025_deepcrceval; @p04_kumar2026_swe_prbench; @p05_zeng2025_swrbench; @p06_hu2025_contextcrbench; @p14_li2022_codereviewer; @p52_tufano2021_automating_code_review_activities].

The study is intentionally bounded. The planned initial version uses one primary dataset, one main generation model, fixed prompts and settings, a limited number of representative mitigation strategies, and a few hundred annotated comments. The purpose is to obtain interpretable empirical findings about mitigation trade-offs, not to make broad model-ranking claims.

## Research Questions

The study is guided by five research questions. RQ1--RQ3 are the primary questions. RQ4 is secondary because it depends on whether the hybrid strategy is implemented in the final experiment. RQ5 is exploratory because context-quality moderation may require more data than the main comparison.

<!-- table: caption="Research questions, priority, and expected outputs." label="tab:methodology-rqs" -->
| RQ | Priority | Question | Expected output |
| --- | --- | --- | --- |
| RQ1 | Primary | What types of problematic comments occur in LLM-generated code review? | Distribution of problematic-comment types and refined taxonomy labels. |
| RQ2 | Primary | Which mitigation strategies reduce which types of problematic comments? | Strategy-by-failure-type comparison. |
| RQ3 | Primary | How do mitigation strategies affect useful-feedback preservation, review coverage, human escalation, and execution cost? | Trade-off matrix and preservation/cost metrics. |
| RQ4 | Secondary | Does combining context-quality control with post-generation verification produce a better trade-off than either strategy alone? | Hybrid-strategy analysis, if the combined strategy is included. |
| RQ5 | Exploratory | How does context quality or context inconsistency affect mitigation success? | Context-quality analysis and context-dependent failure patterns. |

RQ1 defines the problem space. RQ2 and RQ3 form the core empirical comparison. RQ4 is reported only if the hybrid condition is implemented with the same documentation and fixed settings as the other strategies. RQ5 is reported as a moderator analysis and is interpreted conservatively, especially if the number of low-context or inconsistent-context instances is small.

## Targeted Literature Review and Initial Operationalization

Before running the empirical comparison, we conduct a targeted review of closely related work. This review is not presented as a full systematic literature review. Its role is narrower: to make the empirical design traceable by identifying the failure types, evaluation dimensions, mitigation strategy families, and methodological risks that must be operationalized in the study. The search and selection procedure is therefore structured enough to reduce cherry-picking, but it is scoped to the design needs of this empirical study rather than to exhaustive coverage of all LLM-for-software-engineering research [@m08_claeswohlin2020; @m09_claeswohlin2023].

The review begins from seed studies on LLM-based code review evaluation, generated review comments, hallucination or grounding, context-aware review, human and production feedback, data and reference quality, filtering or verification, static-analysis-guided review, and LLM-as-a-Judge evaluation. These seed strands cover review-specific evaluation rubrics and benchmarks [@p01_lu2025_deepcrceval; @p04_kumar2026_swe_prbench; @p05_zeng2025_swrbench; @p06_hu2025_contextcrbench], hallucination and grounding checks [@p02_tantithamthavorn2026_hallujudge], context-aware and evidence-augmented review systems [@p11_zhang2025_laura; @p12_wang2025_sgcr; @p16_icoz2026_context_aware; @p20_hong2025_rag_reviewer; @p22_jaoua2025_static_analyzers], industrial or human-centered evaluation [@p03_tantithamthavorn2026_rovodev; @p07_olewicki2024_revmate; @p10_sun2025_bitsai_cr; @p26_zhong2026_human_ai_synergy; @p27_chowdhury2026_industry_claims; @p28_heander2025_support_not_automation], data and reference quality [@p08_liu2025_too_noisy; @p18_bensghaier2025_curated_reviews; @p23_lin2026_reviewer_experience; @p30_weyssow2025_codeultrafeedback], and evaluator validity [@p29_wang2025_human_evaluators; @p31_jiang2025_codejudgebench; @p33_he2025_llmjudge_se; @p36_li2024_llms_as_judges]. Additional studies are added when they provide direct evidence for at least one design component: a failure category, a context-quality dimension, a mitigation decision, an annotation label, an evaluation metric, a workflow cost, or an evaluator-validity risk. Studies are excluded when they address only general code generation, program repair, or model performance without evidence relevant to generated review-comment evaluation.

To make the targeted review auditable, the final paper will report the following review metadata.

<!-- table: caption="Targeted-review reporting fields." label="tab:methodology-review-protocol" -->
| Field | Planned report |
| --- | --- |
| Search sources | Digital libraries, search engines, and seed-paper snowballing sources used for the targeted review. |
| Search date | Date or date range when the search was last executed. |
| Seed papers | Initial studies used to start the targeted review, grouped by design role. |
| Search strings | Query strings or keyword families used for LLM code review, review-comment evaluation, hallucination, grounding, context, filtering, and LLM-as-a-Judge. |
| Inclusion criteria | Evidence relevance to failure types, context quality, mitigation strategies, annotation labels, metrics, workflow cost, or evaluator validity. |
| Exclusion criteria | Generic code generation, program repair, or model-performance papers without review-comment evaluation evidence. |
| Selection counts | Number of initially identified, screened, excluded, and included studies. |
| Stopping rule | Saturation point or snowballing rule used to stop adding papers. |

<!-- TODO: Replace this planned protocol table with the actual search sources, query strings, search date, screening counts, included-study count, exclusion examples, and snowballing stopping rule. -->

Each paper is coded with a structured extraction form. For each paper, we extract the evaluated artifact, input context, model or system setting, evaluation dimensions, failure types, mitigation mechanisms, human or automated judging protocol, cost or workflow indicators, and stated limitations. Extracted claims are marked as reported evidence, inferred interpretation, or our synthesis perspective so that the synthesis does not attribute our interpretation to individual papers.

The output of this review is an initial operational vocabulary. The review identifies candidate problematic-comment types such as unsupported or hallucinated comments, irrelevant comments, wrong-location comments, incorrect technical claims, invalid fix suggestions, false positives, non-actionable comments, low-value comments, and context-dependent cases. These labels are grounded in prior review-comment evaluation, hallucination, data-quality, and comment-classification work [@p01_lu2025_deepcrceval; @p02_tantithamthavorn2026_hallujudge; @p08_liu2025_too_noisy; @p18_bensghaier2025_curated_reviews; @p19_nguyen2025_fine_grained_classification; @p41_widyasari2025_explaining_explanations]. It also identifies strategy families according to their intervention point: before generation, during generation, after generation, and before display to the user.

## Operational Taxonomy Construction

The taxonomy is constructed to support annotation in the empirical study. It is not meant to be only a conceptual list of possible problems. Each label should help annotators decide whether a generated comment is problematic, what kind of problem it has, and what mitigation decision is appropriate.

The taxonomy is developed through an empirical-to-conceptual iteration. The initial dimensions are derived from the targeted review, prior code-review taxonomies, evaluation rubrics, and examples of generated comments. These dimensions are then refined during pilot annotation until the labels are sufficiently clear, non-redundant, and useful for the study's decision task. This follows the general logic of taxonomy development: categories should be grounded in empirical observations, connected to a clear purpose, and refined until they satisfy explicit ending conditions such as label clarity, mutual usefulness, and sufficient coverage for the intended analysis [@m01_nickerson2013_taxonomy].

The annotation-oriented parts of the taxonomy are also informed by content-analysis practice. Each category should define the coding unit, inclusion criteria, exclusion criteria, and decision notes so that annotators can apply the labels consistently across comments and instances [@m03_krippendorff2018_content_analysis]. The initial review-specific labels are informed by modern-code-review taxonomies, automated code-review analyses, fine-grained comment classification, and explanation-oriented review studies [@p51_davila2021_mcr_slr_taxonomy; @p52_tufano2021_automating_code_review_activities; @p53_tufano2024_code_review_automation_strengths_weaknesses; @p19_nguyen2025_fine_grained_classification; @p41_widyasari2025_explaining_explanations].

Each taxonomy category includes a definition, inclusion criteria, exclusion criteria, and decision notes. For example, an unsupported claim is a comment that makes a factual or causal claim not supported by the available context. A non-actionable comment is one where the developer cannot determine a concrete next step. A low-value comment may be technically correct but not worth reviewer attention. A useful-but-not-directly-acceptable comment contains a useful signal but should be rewritten, softened, grounded, or escalated before being shown.

The pilot refinement has explicit ending conditions. The taxonomy is considered ready for the final sample when annotators can apply the main labels without persistent overlap between major categories, when unresolved ambiguities are documented as decision notes, and when the pilot does not reveal a recurring failure type that is absent from the taxonomy.

<!-- TODO: After pilot annotation, report pilot size, annotator count, label changes, merged categories, removed labels, added decision notes, and unresolved ambiguity. -->

The taxonomy separates failure types from evaluation dimensions. Correctness, grounding, usefulness, actionability, and severity are dimensions. Unsupported claim, wrong cause, invalid fix suggestion, irrelevant comment, and low-value nitpick are failure types. This separation is needed because a comment can be correct but low-value, useful but weakly grounded, or relevant but not directly actionable.

## Dataset and Sample Selection

The dataset must contain code changes and enough review-relevant context to generate and evaluate comments. Candidate sources include existing code review comment generation datasets, pull-request-level review benchmarks, or code changes paired with commit messages, pull-request descriptions, issue descriptions, and review discussion. The key selection criterion is not dataset size alone, but whether the instances are judgeable and support comparison across strategies. This criterion is motivated by the difference between reference-comment generation datasets, PR-level benchmarks, context-enriched benchmarks, and comprehension-oriented review tasks [@p14_li2022_codereviewer; @p52_tufano2021_automating_code_review_activities; @p04_kumar2026_swe_prbench; @p05_zeng2025_swrbench; @p06_hu2025_contextcrbench; @p17_lin2025_codereviewqa].

The final dataset choice will be reported through a fixed selection protocol rather than as an informal convenience choice.

<!-- table: caption="Dataset and sample-selection protocol." label="tab:methodology-dataset-protocol" -->
| Design element | Planned specification |
| --- | --- |
| Dataset name and source | The selected dataset or benchmark, with version, URL or release identifier, and license constraints. |
| Instance definition | Whether one instance corresponds to a pull request, code change, hunk, file-level change, or existing review-comment context. |
| Included context | Diff, surrounding code, commit message, pull-request description, issue text, review discussion, retrieved files, or other context used by strategies. |
| Inclusion criteria | Instances with enough code and textual context to judge grounding, relevance, usefulness, and actionability. |
| Exclusion criteria | Instances that cannot be legally reused, cannot be judged from available context, are duplicates, are non-code-only changes, or contain insufficient language/context support. |
| Sampling plan | Random or stratified sampling by repository, language, change size, context availability, or baseline-problem likelihood. |
| Pilot/final separation | Pilot instances are not reused for final evaluation after prompt, taxonomy, or threshold tuning. |
| Sample-size rationale | Expected number of review instances, generated comments, double-annotated comments, and rationale for descriptive or inferential analysis. |

<!-- TODO: Replace this planned protocol with the actual dataset name, dataset version, instance definition, programming languages, inclusion/exclusion counts, sampling method, pilot/final split, licensing constraints, and sample-size rationale. -->

Each selected instance should ideally include:

- the code diff or changed file region;
- surrounding code or project context where available;
- textual context such as a commit message or pull-request description;
- enough information to judge whether a generated comment is grounded, useful, and actionable.

If the selected dataset already contains generated comments from prior systems, those comments may be used as input artifacts. Otherwise, comments are generated using a fixed base model and fixed prompt. The same dataset split, model configuration, decoding settings, and prompts are used throughout the final evaluation. Prompt or strategy tuning happens only during pilot development, not on the final evaluation sample.

A practical initial setup is one primary dataset, one main generation model, four or five strategies, and approximately 100--300 annotated generated comments. If resources are limited, the first study may use a smaller pilot and report the results as exploratory. The empirical claims must match the sample size and must avoid broad generalization across all models, languages, repositories, or review settings.

## Compared Mitigation Strategies

The study compares a limited number of representative strategies. These strategies are chosen to represent different intervention points rather than to exhaust all possible systems. The strategy set reflects common intervention families in recent work: prompt- or generation-time control, context enrichment or context gating, post-generation verification, static-analysis or specification grounding, reward or preference-based filtering, and human-centered escalation [@p02_tantithamthavorn2026_hallujudge; @p03_tantithamthavorn2026_rovodev; @p10_sun2025_bitsai_cr; @p11_zhang2025_laura; @p12_wang2025_sgcr; @p20_hong2025_rag_reviewer; @p22_jaoua2025_static_analyzers; @p24_bensghaier2025_reward_models; @p28_heander2025_support_not_automation].

<!-- table: caption="Representative mitigation strategies for the empirical comparison." label="tab:methodology-strategies" -->
| Strategy | Intervention point | Operational role |
| --- | --- | --- |
| Baseline LLM reviewer | Generation | Generates review comments using a fixed base prompt and the available context. |
| Robust prompting | Generation | Uses a constrained prompt that asks the model to avoid unsupported claims, focus on actionable feedback, and avoid low-value comments. |
| Context-quality gate | Before generation or before display | Assigns a context-quality decision before generation or display; low-quality cases may be skipped, downgraded, or escalated. |
| Post-generation verification | After generation | Checks a generated comment for support, relevance, correctness, actionability, or risk before showing it. |
| Hybrid gate plus verifier | Before and after generation | Combines context-quality control with post-generation verification to test whether the trade-off improves. |

The final implementation of each strategy is documented using the following operational template.

<!-- table: caption="Operational specification required for each mitigation strategy." label="tab:methodology-strategy-spec" -->
| Field | Required specification |
| --- | --- |
| Input | Code, textual context, retrieved context, static-analysis signal, generated comment, or strategy-specific metadata. |
| Output | Generated comment, revised comment, verification label, context-quality label, or no-comment decision. |
| Decision labels | One of `show`, `suppress`, `rewrite`, or `escalate`, with strategy-specific mapping rules. |
| Prompt or rule | Exact prompt, rule set, verifier criterion, static-analysis mapping, retrieval setting, or threshold. |
| Fixed settings | Model name, model version, temperature, decoding settings, retrieval depth, analyzer version, and threshold values. |
| Cost unit | Number of generation calls, verifier calls, retrieval calls, analyzer calls, token count, or latency proxy. |
| Failure mode | Known way the strategy may remove useful feedback, expose unsafe feedback, or increase human effort. |

A retrieval-augmented context strategy may be added if implementation time allows and the dataset supports retrieval. If included, it is treated as a context-enrichment strategy and evaluated with the same trade-off metrics, including cost and added context noise [@p11_zhang2025_laura; @p16_icoz2026_context_aware; @p20_hong2025_rag_reviewer].

The baseline is not expected to be the best strategy. It provides the reference point for measuring how many problematic comments appear without additional mitigation. Robust prompting tests whether generation-time constraints are enough. The context-quality gate tests whether preventing or routing low-context cases reduces problematic comments. Post-generation verification tests whether checking comments after generation improves quality before display. The hybrid strategy tests whether pre-generation and post-generation controls complement each other.

<!-- TODO: Replace the strategy-specification template with exact prompt text, verifier design, context-gate criteria, thresholds, model versions, decoding settings, retrieval settings, static-analysis settings, and strategies dropped or added. -->

## Paired Comparison Design

The empirical comparison uses a paired design: each strategy is evaluated on the same underlying review instances wherever feasible. This design is important because generated review comments vary strongly by change type, code context, and available textual context. Comparing strategies on different samples would confound mitigation behavior with input difficulty.

For each review instance, the study records the baseline output and the outputs or decisions produced by each mitigation strategy. The paired structure allows the analysis to ask instance-level questions: did the verifier suppress a comment that the annotators considered useful? Did the context-quality gate route an instance that produced an unsupported baseline comment? Did robust prompting improve actionability for the same underlying change? Did the hybrid strategy preserve useful feedback that a single-stage filter would have removed?

When a strategy cannot produce an output for a specific instance, the missing output is recorded as part of the strategy behavior rather than silently removed from the analysis. For example, a context-quality gate that escalates an instance instead of generating a comment affects both coverage and human effort.

The paired structure is also reflected in the analysis. Comment-level quality measures are computed over generated comments, while coverage, escalation, and cost measures are computed over review instances. If multiple comments are produced for one instance, comment-level results are reported with the instance identifier preserved so that the analysis can avoid treating nested comments as fully independent observations.

## Generation and Mitigation Procedure

For each code-review instance, the baseline strategy generates a review comment using the fixed model and base prompt. Other strategies either change the generation prompt, add a pre-generation or pre-display context-quality decision, verify the generated comment, or combine these interventions.

Each strategy produces both an output artifact and a mitigation decision. The output artifact may be a generated comment, a rewritten comment, a verification label, a context-quality label, or an escalation decision. The four decision labels are:

- `show`: the comment is suitable to present as review feedback;
- `suppress`: the comment should not be shown because it is unsupported, incorrect, irrelevant, too low-value, or harmful;
- `rewrite`: the comment contains a useful signal but needs clarification, grounding, softening, or actionability improvements;
- `escalate`: the comment raises a potentially important issue that requires human judgment or additional context.

The same sample is processed by all strategies where feasible. This paired design enables within-sample comparison. For example, the analysis can ask whether the verifier suppresses comments that annotators consider useful, whether the context-quality gate reduces context-dependent failures, or whether robust prompting reduces non-actionable comments without lowering review coverage.

All prompts, model settings, gating rules, verifier prompts or rules, static-analysis settings, retrieval settings, and thresholds are fixed before processing the final sample. Reporting also identifies the role played by the LLM in each stage: generation, verification, rewriting, judging, or annotation support. This distinction is needed because an LLM used as a generator and an LLM used as a judge create different validity risks [@m06_sebastianbaltes2025; @m04_zheng2023_llm_judge; @p29_wang2025_human_evaluators; @p31_jiang2025_codejudgebench; @p33_he2025_llmjudge_se; @p36_li2024_llms_as_judges].

Human annotation is the primary reference for final evaluation. If an LLM judge is used, its output is treated either as a mitigation-strategy component or as an auxiliary measurement signal, not as ground truth. LLM-judge results are therefore compared against human annotation rather than replacing it.

## Human Annotation Protocol

The annotation protocol evaluates generated comments, available context, and mitigation decisions. Annotators see the code change, available context, generated comment, and any strategy-specific decision needed for the current annotation phase. The annotation guideline defines the labels and decision rules.

The main annotation labels include:

- problematic-comment type;
- technical correctness;
- grounding or evidential support;
- relevance to the change;
- usefulness;
- actionability;
- value or severity;
- context quality;
- dataset validity;
- recommended mitigation decision;
- annotator confidence.

The protocol distinguishes correctness, usefulness, and actionability. A comment can be technically correct but practically low-value. A comment can be useful but not directly acceptable as a review comment. A comment can be impossible to judge because the available context is insufficient. These distinctions are consistent with review-specific evaluation rubrics, curated-review studies, comment-classification work, and human-centered review-assistance studies [@p01_lu2025_deepcrceval; @p18_bensghaier2025_curated_reviews; @p19_nguyen2025_fine_grained_classification; @p07_olewicki2024_revmate; @p28_heander2025_support_not_automation].

Annotation is performed in two phases to reduce bias. In the first phase, annotators judge comment quality, failure type, usefulness, actionability, grounding, and context quality while being blinded to the mitigation strategy whenever feasible. In the second phase, annotators evaluate or resolve the appropriate mitigation decision. Strategy identifiers and model-generated verifier labels are not shown during initial quality labeling unless they are required for the specific decision task.

Before full annotation, annotators label a pilot subset. The pilot is used to refine taxonomy labels, clarify ambiguous cases, calibrate mitigation decisions, and revise the annotation guideline. At least two annotators with software-engineering experience label the pilot and a substantial subset of the final sample when feasible. The final paper reports annotator background in terms of software-engineering experience, code-review experience, programming-language familiarity, and prior exposure to LLM-based tools.

Inter-annotator agreement is reported separately for key label groups when possible. Cohen's kappa can be used for two annotators and categorical labels [@m02_cohen1960_kappa]. Krippendorff's alpha is appropriate when there are missing labels, more than two annotators, or variable annotation coverage, and software-engineering qualitative research provides practical guidance for using such agreement measures in coding studies [@m07_angelgonzalezprieto2020]. Percentage agreement may be reported as a descriptive supplement, but it should not replace chance-corrected agreement.

Disagreements are resolved through discussion or adjudication. The final dataset preserves the initial annotator labels, resolved labels, and disagreement notes where useful. This is especially important for borderline cases such as useful-but-weakly-grounded comments, correct-but-low-value comments, and context-dependent comments.

<!-- TODO: After annotation, report annotator background, pilot size, final sample size, double-annotation proportion, agreement statistics, adjudication process, labels with low agreement, and whether annotators were blinded to strategy identity. -->

## Operational Measures

The study operationalizes each construct through explicit labels, counts, or ratios. Table \ref{tab:methodology-operational-measures} summarizes the main constructs used in the analysis. The selected measures combine review-comment quality dimensions, production or workflow signals, data-quality concerns, and evaluator-validity risks reported in prior work [@p01_lu2025_deepcrceval; @p03_tantithamthavorn2026_rovodev; @p08_liu2025_too_noisy; @p10_sun2025_bitsai_cr; @p29_wang2025_human_evaluators; @p30_weyssow2025_codeultrafeedback; @p33_he2025_llmjudge_se].

<!-- table: caption="Operational measures used in the empirical comparison." label="tab:methodology-operational-measures" longtable="true" -->
| Construct | Operational measure | Source |
| --- | --- | --- |
| Problematic-comment rate | `# comments with at least one problematic label / # generated comments`. | Human annotation. |
| Failure-type rate | `# comments with a given failure type / # generated comments`. | Human annotation. |
| Useful-feedback preservation | `# useful comments retained as show or rewrite / # useful candidate comments`. | Human annotation plus strategy decision. |
| Wrongly suppressed useful comments | `# useful comments suppressed / # useful candidate comments`. | Human annotation plus strategy decision. |
| Review coverage | `# instances with at least one shown or rewritten useful comment / # review instances`. | Strategy output plus annotation. |
| Unsafe exposure | `# shown comments judged suppress or escalate / # shown comments`. | Strategy decision compared with resolved annotation. |
| Recoverable feedback loss | `# comments suppressed by a strategy but judged rewrite / # comments judged rewrite`. | Strategy decision compared with resolved annotation. |
| Human escalation rate | `# instances routed to human review or additional context / # review instances`. | Strategy decision. |
| Context-quality effect | Difference in strategy metrics between high-context and low-context or inconsistent-context instances. | Context-quality label plus strategy metrics. |
| Computational cost | Model calls, verifier calls, retrieval calls, analyzer calls, approximate token count, or latency proxy per instance. | Execution log or cost proxy. |
| Evaluator reliability | Agreement on key labels such as problematic type, usefulness, actionability, and mitigation decision. | Annotator labels and agreement statistics. |

These measures make the trade-off explicit. A strategy can improve the problematic-comment rate while worsening useful-feedback preservation or review coverage. Conversely, a strategy can preserve more useful comments while requiring more escalation or computational cost.

## Decision-Confusion Analysis

The study compares each strategy's decision with the resolved human annotation decision. This creates a decision-confusion view over the four actions: show, suppress, rewrite, and escalate. Similar decision-oriented concerns appear in industrial filtering, human-AI review support, reward-guided comment generation, and LLM-as-a-Judge evaluation, where the relevant question is not only whether a score improves, but also which comments are exposed, removed, rewritten, escalated, or misjudged [@p03_tantithamthavorn2026_rovodev; @p10_sun2025_bitsai_cr; @p24_bensghaier2025_reward_models; @p28_heander2025_support_not_automation; @p29_wang2025_human_evaluators].

Several error types are especially important:

- **Unsafe exposure**: the strategy shows a comment that annotators judge should be suppressed or escalated.
- **False suppression**: the strategy suppresses a comment that annotators judge should be shown.
- **Recoverable feedback loss**: the strategy suppresses a comment that annotators judge should be rewritten.
- **Unnecessary escalation**: the strategy escalates a comment that annotators judge could be shown or rewritten.
- **Missed escalation**: the strategy shows or rewrites a comment that annotators judge requires escalation.

This analysis is important because it captures costs that are invisible in a binary quality score. For example, false suppression and recoverable feedback loss both remove useful information, but recoverable feedback loss is especially important because a rewrite strategy could have preserved the signal.

## Metrics

The study reports both error-reduction metrics and trade-off metrics.

Error-reduction metrics include:

- overall problematic-comment rate;
- rate of each problematic-comment type;
- unsupported or hallucinated comment rate;
- irrelevant comment rate;
- wrong-location or wrong-cause rate;
- invalid fix suggestion rate;
- non-actionable comment rate;
- low-value comment rate.

Preservation and workflow metrics include:

- useful comments retained;
- useful comments wrongly suppressed;
- review coverage retained after filtering;
- comments rewritten rather than suppressed;
- human escalation rate;
- context-dependent comments routed correctly;
- human annotation or verification effort;
- number of model calls;
- approximate token cost;
- latency proxy where measurable.

The study does not report only a single quality score. A strategy that removes many comments may look good under an error-rate metric but bad under useful-feedback preservation or coverage. Conversely, a strategy that preserves many useful comments may still require too much human escalation or computational cost.

## Analysis Plan

The analysis compares strategies along four axes.

First, it compares the distribution of problematic-comment types produced or retained by each strategy. This answers which strategies are effective for unsupported claims, irrelevant comments, non-actionable comments, invalid fix suggestions, and low-value comments.

Second, it compares preservation and coverage. This asks how many useful comments each strategy keeps, how many useful comments it wrongly suppresses, and how much automatic review coverage remains after filtering or escalation.

Third, it compares strategy decisions against resolved annotation decisions using the decision-confusion analysis. This identifies unsafe exposure, false suppression, recoverable feedback loss, unnecessary escalation, and missed escalation.

Fourth, it compares cost and effort. This includes additional model calls, verifier calls, retrieval cost if applicable, human escalation rate, and annotation or verification effort. These measures are used to avoid presenting a high-cost strategy as better only because it reduces more problematic comments.

If the sample size permits, paired comparisons use uncertainty estimates such as confidence intervals or bootstrap intervals. For paired binary outcomes, tests such as McNemar's test or paired bootstrap comparisons may be used when their assumptions are reasonable. If the sample is small, the analysis remains primarily descriptive and pairs quantitative summaries with qualitative examples.

If the hybrid strategy is included, it is analyzed as a secondary trade-off case rather than as an assumed improvement. The analysis asks whether combining a context-quality gate with post-generation verification reduces complementary failure types or merely increases cost and suppression.

Context quality is analyzed as an exploratory moderator. The study compares high-context and low-context instances where possible, and examines whether certain failures occur more often when the available context is incomplete, inconsistent, stale, or too broad. This moderator analysis is motivated by prior evidence that review quality depends on available context, reviewability, retrieved evidence, specifications, static-analysis signals, and possible documentation-code inconsistencies [@p06_hu2025_contextcrbench; @p11_zhang2025_laura; @p12_wang2025_sgcr; @p22_jaoua2025_static_analyzers; @p40_ram2018_reviewability; @p49_lee2025_metamon].

<!-- TODO: After analysis, report which statistical or descriptive comparisons were actually used, including confidence intervals, bootstrap intervals, tests, qualitative-example selection rules, and whether nested comments were aggregated at the instance level. -->

## Reproducibility and Scope Control

To support reproducibility, the replication package includes the study corpus, coding form, annotation guideline, evaluation schema, prompts, model settings, generated outputs where licensing permits, and scripts for computing metrics. If closed models or restricted datasets are used, the study still documents prompts, settings, sampling decisions, and annotation procedures as precisely as possible. This reporting covers not only the final prompt text, but also the model role, model version, temperature or decoding settings, context construction, tool use, and any human validation or adjudication steps [@m06_sebastianbaltes2025].

The main scope risk is that the work becomes too broad: too many datasets, too many models, too many strategies, or too many evaluation dimensions. The initial study therefore keeps the design limited. It uses a bounded set of representative strategies and a sample size that supports careful annotation.

The main threats to validity are incomplete literature coverage, possible changes in recent preprints, dataset limitations, sample size limits, annotator disagreement, sensitivity to prompts and model settings, and possible evaluator bias if LLM-as-a-Judge is used. These threats are mitigated by transparent inclusion criteria, fixed evaluation settings, pilot annotation, agreement reporting, preserved disagreement notes, and conservative interpretation of results. The study reports these threats as design constraints rather than as after-the-fact caveats, following empirical software-engineering reporting expectations [@m05_paulralph2020]. Evaluator-related threats are especially important because recent work shows that LLM judges can be useful but sensitive to task framing, judge choice, bias, and calibration [@p29_wang2025_human_evaluators; @p31_jiang2025_codejudgebench; @p32_zhao2026_bias_loop; @p33_he2025_llmjudge_se; @p36_li2024_llms_as_judges].

<!-- TODO: After the study is executed, update reproducibility details with the actual artifacts released, files withheld for licensing/privacy reasons, and exact replication package structure. -->
