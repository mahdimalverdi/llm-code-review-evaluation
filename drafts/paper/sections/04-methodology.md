# Methodology

This study is designed as a controlled empirical comparison of mitigation strategies for problematic LLM-generated code review comments. The goal is not to conduct a broad survey of LLMs for software engineering, to build a leaderboard benchmark, or to identify one universally best review assistant. Instead, the study asks a narrower empirical question: when a review assistant produces potentially problematic comments, which mitigation strategies reduce which kinds of problems, and what do they cost in useful feedback, review coverage, human effort, and computation?

The literature synthesis and taxonomy are therefore supporting components, not the primary identity of the paper. A focused review of prior work is used to define the failure categories, evaluation dimensions, and representative mitigation strategies. The main methodological object is the planned comparative evaluation: the same code-review instances will be processed under a bounded set of representative strategies, the resulting comments and decisions will be annotated, and the strategies will be compared through both error-reduction and preservation metrics.

This design follows the paper's central motivation: reducing problematic comments is not sufficient by itself. A strategy can remove unsupported, irrelevant, or non-actionable comments while also removing useful weak signals, decreasing automatic review coverage, increasing latency, or shifting the burden to human reviewers. The study therefore evaluates mitigation as a trade-off, not as a single success/failure outcome.

## Study Design

The study has five planned stages:

1. a targeted literature review to define failure categories, evaluation dimensions, and strategy families;
2. construction and pilot refinement of an operational taxonomy of problematic generated review comments;
3. selection of a shared evaluation sample and generation of baseline review comments;
4. application of several representative mitigation strategies to the same sample;
5. human annotation and trade-off analysis of the resulting comments and mitigation decisions.

The unit of analysis is a generated review comment for a code change under review. Each instance contains a code change and, where available, review-relevant textual context such as a commit message, pull-request description, issue description, previous discussion, surrounding code, or retrieved project context. The same base instances are used across strategies so that observed differences are attributable to the mitigation strategy rather than to different input distributions.

The study is intentionally bounded. A feasible initial version uses one primary dataset, one main generation model, a fixed set of prompts and settings, a limited number of representative mitigation strategies, and a few hundred annotated comments. The purpose is to obtain interpretable empirical findings about mitigation trade-offs, not to make broad model-ranking claims.

## Research Questions

The study is guided by five research questions.

<!-- table: caption="Research questions and expected outputs." label="tab:methodology-rqs" -->
| RQ | Question | Expected output |
| --- | --- | --- |
| RQ1 | What types of problematic comments occur in LLM-generated code review? | Distribution of problematic-comment types and refined taxonomy labels. |
| RQ2 | Which mitigation strategies reduce which types of problematic comments? | Strategy-by-failure-type comparison. |
| RQ3 | How do mitigation strategies affect useful-feedback preservation, review coverage, human escalation, and execution cost? | Trade-off matrix and preservation/cost metrics. |
| RQ4 | Does combining context-quality control with post-generation verification produce a better trade-off than either strategy alone? | Hybrid-strategy analysis, if the combined strategy is included. |
| RQ5 | How does context quality or context inconsistency affect mitigation success? | Context-quality analysis and context-dependent failure patterns. |

RQ1 defines the problem space. RQ2 and RQ3 form the core empirical comparison. RQ4 tests whether a combined strategy improves the trade-off when feasible. RQ5 connects the empirical results back to the context-quality motivation of the paper.

## Targeted Literature Review and Initial Operationalization

Before running the empirical comparison, we conduct a targeted review of closely related work. This review is not intended to be a full systematic literature review. Its role is to support the empirical design by identifying the main categories of problematic comments, the main strategy families for reducing them, and the evaluation dimensions needed to interpret the results.

The paper pool is maintained in `matrices/paper-pool.md`. Papers are included when they provide evidence about LLM-based code review evaluation, generated review comments, hallucination or grounding, context-aware review, human or production feedback, data and reference quality, filtering or verification, static-analysis-guided review, or LLM-as-a-Judge evaluation. Papers are excluded when they only address general code generation, program repair, or model performance without evidence relevant to review-comment evaluation.

Each paper is coded using `templates/paper-analysis-template.md`. For each paper, we extract the evaluated artifact, input context, model or system setting, evaluation dimensions, failure types, mitigation mechanisms, human or automated judging protocol, cost or workflow indicators, and stated limitations. Extracted claims are marked as `Reported`, `Inferred`, or `Our perspective` so that the synthesis does not attribute our interpretation to individual papers.

The output of this review is an initial operational vocabulary. The review identifies candidate problematic-comment types such as unsupported or hallucinated comments, irrelevant comments, wrong-location comments, incorrect technical claims, invalid fix suggestions, false positives, non-actionable comments, low-value comments, and context-dependent cases. It also identifies strategy families according to their intervention point: before generation, during generation, after generation, and before display to the user.

## Operational Taxonomy Construction

The taxonomy is constructed to support annotation in the empirical study. It is not meant to be only a conceptual list of possible problems. Each label should help annotators decide whether a generated comment is problematic, what kind of problem it has, and what mitigation decision is appropriate.

The initial taxonomy is derived from failure types reported in prior work and failure types inferred from examples and evaluation rubrics. During the pilot round, labels should be refined to reduce overlap, clarify borderline cases, and add missing categories if the generated comments reveal failure modes not covered by the initial taxonomy.

<!-- TODO: After pilot annotation, replace the planned refinement description with concrete details: pilot size, label changes, merged categories, removed labels, and unresolved ambiguity. -->

Each taxonomy category should include a definition, inclusion criteria, exclusion criteria, and decision notes. For example, an unsupported claim is a comment that makes a factual or causal claim not supported by the available context. A non-actionable comment is one where the developer cannot determine a concrete next step. A low-value comment may be technically correct but not worth reviewer attention. A useful-but-not-directly-acceptable comment contains a useful signal but should be rewritten, softened, grounded, or escalated before being shown.

The taxonomy separates failure types from evaluation dimensions. Correctness, grounding, usefulness, actionability, and severity are dimensions. Unsupported claim, wrong cause, invalid fix suggestion, irrelevant comment, and low-value nitpick are failure types. This separation is needed because a comment can be correct but low-value, useful but weakly grounded, or relevant but not directly actionable.

## Dataset and Sample Selection

The dataset should contain code changes and enough review-relevant context to generate and evaluate comments. Candidate sources include existing code review comment generation datasets, pull-request-level review benchmarks, or code changes paired with commit messages, pull-request descriptions, issue descriptions, and review discussion. The key selection criterion is not dataset size alone, but whether the instances are judgeable and support comparison across strategies.

Each selected instance should ideally include:

- the code diff or changed file region;
- surrounding code or project context where available;
- textual context such as a commit message or pull-request description;
- enough information to judge whether a generated comment is grounded, useful, and actionable.

If the selected dataset already contains generated comments from prior systems, those comments may be used as input artifacts. Otherwise, comments are generated using a fixed base model and fixed prompt. The same dataset split, model configuration, decoding settings, and prompts are used throughout the final evaluation. Prompt or strategy tuning should happen only during pilot development, not on the final evaluation sample.

A practical initial setup is one primary dataset, one main generation model, four or five strategies, and approximately 100--300 annotated generated comments. If resources are limited, the first study may use a smaller pilot and report the results as exploratory. The empirical claims should match the sample size and should avoid broad generalization across all models, languages, repositories, or review settings.

<!-- TODO: After dataset selection, replace this generic sampling description with the actual dataset name, inclusion criteria, sample size, programming languages, filtering rules, and licensing constraints. -->

## Compared Mitigation Strategies

The study compares a limited number of representative strategies. These strategies are chosen to represent different intervention points rather than to exhaust all possible systems.

<!-- table: caption="Representative mitigation strategies for the empirical comparison." label="tab:methodology-strategies" -->
| Strategy | Intervention point | Description |
| --- | --- | --- |
| Baseline LLM reviewer | Generation | Generates review comments using a fixed base prompt and the available context. |
| Robust prompting | Generation | Uses a constrained prompt that asks the model to avoid unsupported claims, focus on actionable feedback, and avoid low-value comments. |
| Context-quality gate | Before generation or before display | Detects insufficient, inconsistent, or weak context and skips, downgrades, or escalates uncertain instances. |
| Post-generation verification | After generation | Checks a generated comment for support, relevance, correctness, actionability, or risk before showing it. |
| Hybrid gate plus verifier | Before and after generation | Combines context-quality control with post-generation verification to test whether the trade-off improves. |

A retrieval-augmented context strategy may be added if implementation time allows and the dataset supports retrieval. If included, it should be treated as a context-enrichment strategy and evaluated with the same trade-off metrics, including cost and added context noise.

The baseline is not expected to be the best strategy. It provides the reference point for measuring how many problematic comments appear without additional mitigation. Robust prompting tests whether generation-time constraints are enough. The context-quality gate tests whether preventing or routing low-context cases reduces problematic comments. Post-generation verification tests whether checking comments after generation improves quality before display. The hybrid strategy tests whether pre-generation and post-generation controls complement each other.

<!-- TODO: After implementation, document the exact prompt text, verifier design, context-gate criteria, thresholds, model versions, decoding settings, and any strategies that were dropped or added. -->

## Paired Comparison Design

The empirical comparison uses a paired design: each strategy is evaluated on the same underlying review instances wherever feasible. This design is important because generated review comments vary strongly by change type, code context, and available textual context. Comparing strategies on different samples would confound mitigation behavior with input difficulty.

For each review instance, the study records the baseline output and the outputs or decisions produced by each mitigation strategy. The paired structure allows the analysis to ask instance-level questions: did the verifier suppress a comment that the annotators considered useful? Did the context-quality gate route an instance that produced an unsupported baseline comment? Did robust prompting improve actionability for the same underlying change? Did the hybrid strategy preserve useful feedback that a single-stage filter would have removed?

When a strategy cannot produce an output for a specific instance, the missing output should be recorded as part of the strategy behavior rather than silently removed from the analysis. For example, a context-quality gate that escalates an instance instead of generating a comment affects both coverage and human effort.

## Generation and Mitigation Procedure

For each code-review instance, the baseline strategy generates a review comment using the fixed model and base prompt. Other strategies either change the generation prompt, add a pre-generation or pre-display context-quality decision, verify the generated comment, or combine these interventions.

Each strategy produces both an output comment and a mitigation decision. The four decision labels are:

- `show`: the comment is suitable to present as review feedback;
- `suppress`: the comment should not be shown because it is unsupported, incorrect, irrelevant, too low-value, or harmful;
- `rewrite`: the comment contains a useful signal but needs clarification, grounding, softening, or actionability improvements;
- `escalate`: the comment raises a potentially important issue that requires human judgment or additional context.

The same sample is processed by all strategies where feasible. This paired design enables within-sample comparison. For example, the analysis can ask whether the verifier suppresses comments that annotators consider useful, whether the context-quality gate reduces context-dependent failures, or whether robust prompting reduces non-actionable comments without lowering review coverage.

All prompts, model settings, gating rules, verifier prompts or rules, static-analysis settings, retrieval settings, and thresholds should be documented. Final evaluation settings should be fixed before processing the final sample.

## Human Annotation Protocol

The annotation protocol evaluates generated comments, available context, and mitigation decisions. Annotators see the code change, available context, generated comment, and any strategy-specific decision. The annotation guideline defines the labels and decision rules.

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

The protocol should distinguish correctness, usefulness, and actionability. A comment can be technically correct but practically low-value. A comment can be useful but not directly acceptable as a review comment. A comment can be impossible to judge because the available context is insufficient.

Before full annotation, annotators label a pilot subset. The pilot is used to refine taxonomy labels, clarify ambiguous cases, calibrate mitigation decisions, and revise the annotation guideline. At least two annotators with software-engineering experience should label the pilot and a substantial subset of the final sample when feasible.

Inter-annotator agreement should be reported separately for key label groups when possible. Cohen's kappa can be used for two annotators and categorical labels. Krippendorff's alpha can be used when there are missing labels or more than two annotators. Percentage agreement may be reported as a descriptive supplement, but it should not replace chance-corrected agreement.

Disagreements are resolved through discussion or adjudication. The final dataset should preserve the initial annotator labels, resolved labels, and disagreement notes where useful. This is especially important for borderline cases such as useful-but-weakly-grounded comments, correct-but-low-value comments, and context-dependent comments.

<!-- TODO: After annotation, report annotator background, pilot size, final sample size, double-annotation proportion, agreement statistics, adjudication process, and labels with low agreement. -->

## Operational Measures

The study operationalizes each construct through explicit labels, counts, or ratios. Table \ref{tab:methodology-operational-measures} summarizes the main constructs used in the analysis.

<!-- table: caption="Operational measures used in the empirical comparison." label="tab:methodology-operational-measures" longtable="true" -->
| Construct | Operational measure | Source |
| --- | --- | --- |
| Problematic-comment rate | Proportion of generated comments with at least one problematic-comment label. | Human annotation. |
| Failure-type rate | Proportion of comments labeled with each failure type, such as unsupported, irrelevant, non-actionable, or invalid fix. | Human annotation. |
| Useful-feedback preservation | Proportion of useful baseline or candidate comments retained as show or rewrite decisions. | Human annotation plus strategy decision. |
| Wrongly suppressed useful comments | Number or proportion of comments judged useful but suppressed by a strategy. | Human annotation plus strategy decision. |
| Review coverage | Proportion of review instances that still receive at least one shown or rewritten useful comment after mitigation. | Strategy output plus annotation. |
| Unsafe exposure | Number or proportion of comments shown by a strategy but judged suppress or escalate by annotators. | Strategy decision compared with resolved annotation. |
| Recoverable feedback loss | Number or proportion of comments suppressed by a strategy but judged rewrite by annotators. | Strategy decision compared with resolved annotation. |
| Human escalation rate | Proportion of instances routed to human review or additional context collection. | Strategy decision. |
| Context-quality effect | Difference in strategy behavior between high-context and low-context or inconsistent-context instances. | Context-quality label plus strategy metrics. |
| Computational cost | Number of model calls, verifier calls, retrieval calls, approximate token count, or latency proxy. | Execution log or cost proxy. |
| Evaluator reliability | Agreement on key labels such as problematic type, usefulness, actionability, and mitigation decision. | Annotator labels and agreement statistics. |

These measures make the trade-off explicit. A strategy can improve the problematic-comment rate while worsening useful-feedback preservation or review coverage. Conversely, a strategy can preserve more useful comments while requiring more escalation or computational cost.

## Decision-Confusion Analysis

The study compares each strategy's decision with the resolved human annotation decision. This creates a decision-confusion view over the four actions: show, suppress, rewrite, and escalate.

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

The study should not report only a single quality score. A strategy that removes many comments may look good under an error-rate metric but bad under useful-feedback preservation or coverage. Conversely, a strategy that preserves many useful comments may still require too much human escalation or computational cost.

## Analysis Plan

The analysis compares strategies along four axes.

First, it compares the distribution of problematic-comment types produced or retained by each strategy. This answers which strategies are effective for unsupported claims, irrelevant comments, non-actionable comments, invalid fix suggestions, and low-value comments.

Second, it compares preservation and coverage. This asks how many useful comments each strategy keeps, how many useful comments it wrongly suppresses, and how much automatic review coverage remains after filtering or escalation.

Third, it compares strategy decisions against resolved annotation decisions using the decision-confusion analysis. This identifies unsafe exposure, false suppression, recoverable feedback loss, unnecessary escalation, and missed escalation.

Fourth, it compares cost and effort. This includes additional model calls, verifier calls, retrieval cost if applicable, human escalation rate, and annotation or verification effort. These measures are used to avoid presenting a high-cost strategy as better only because it reduces more problematic comments.

If the sample size permits, paired comparisons should use uncertainty estimates such as confidence intervals or bootstrap intervals. For paired binary outcomes, tests such as McNemar's test or paired bootstrap comparisons may be used when their assumptions are reasonable. If the sample is small, the analysis should remain primarily descriptive and should pair quantitative summaries with qualitative examples.

If the hybrid strategy is included, it is analyzed as a trade-off case rather than as an assumed improvement. The analysis should ask whether combining a context-quality gate with post-generation verification reduces complementary failure types or merely increases cost and suppression.

Context quality is analyzed as a moderator. The study should compare high-context and low-context instances where possible, and should examine whether certain failures occur more often when the available context is incomplete, inconsistent, stale, or too broad.

<!-- TODO: After analysis, report which statistical or descriptive comparisons were actually used, including any confidence intervals, bootstrap intervals, tests, or qualitative-example selection rules. -->

## Reproducibility and Scope Control

To support reproducibility, the repository should include the paper pool, coding template, annotation guideline, evaluation schema, prompts, model settings, generated outputs where licensing permits, and scripts for computing metrics. If closed models or restricted datasets are used, the study should still document prompts, settings, sampling decisions, and annotation procedures as precisely as possible.

The main scope risk is that the work becomes too broad: too many datasets, too many models, too many strategies, or too many evaluation dimensions. The initial study therefore keeps the design limited. It should use a bounded set of representative strategies and a sample size that supports careful annotation.

The main threats to validity are incomplete literature coverage, possible changes in recent preprints, dataset limitations, sample size limits, annotator disagreement, sensitivity to prompts and model settings, and possible evaluator bias if LLM-as-a-Judge is used. These threats are mitigated by transparent inclusion criteria, fixed evaluation settings, pilot annotation, agreement reporting, preserved disagreement notes, and conservative interpretation of results.

<!-- TODO: After the study is executed, update reproducibility details with the actual artifacts released, files withheld for licensing/privacy reasons, and exact replication package structure. -->
