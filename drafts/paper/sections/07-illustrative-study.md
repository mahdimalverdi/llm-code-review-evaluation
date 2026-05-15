# Empirical Evaluation Design

This section defines the controlled empirical comparison used to evaluate mitigation strategies. The study is designed to be small enough to execute with careful annotation, but structured enough to produce evidence beyond a pilot demonstration. The goal is to compare representative strategies on the same review instances and measure both the errors they reduce and the useful feedback or coverage they may lose.

## Study Goal

The empirical evaluation has three goals. First, it estimates the distribution of problematic generated review comments in the selected sample. Second, it compares how representative mitigation strategies affect different failure types. Third, it measures trade-offs that would be hidden by simple accuracy, acceptance, or hallucination metrics.

The study is not a model leaderboard. It uses a fixed generation setup so that the analysis focuses on mitigation behavior. The comparison should therefore be interpreted as evidence about intervention types, not as a general ranking of all possible models or prompts.

## Experimental Units and Sample

The experimental unit is a code-review instance consisting of a code change, available review-relevant context, a generated review comment, and a mitigation decision. The same base instances are used across strategies where feasible. This paired design allows direct comparison between strategies on the same underlying review situation.

The sample should be selected from an existing code review dataset or pull-request-level benchmark when possible. A suitable instance should contain a code diff and enough context to judge whether a generated comment is relevant, grounded, useful, and actionable. Instances that are not judgeable under the available context should be retained when they are useful for studying context-quality failures, but they should be labeled as such rather than treated as ordinary model failures.

A feasible first version uses approximately 100--300 generated comments after pilot development. The final sample size should be justified by annotation resources and by the need to compare strategies across failure types. If the study remains smaller, the paper should frame the results as exploratory and avoid broad claims.

## Compared Strategies

The evaluation compares a limited set of representative strategies:

1. **Baseline LLM reviewer**: generates comments from the available code-change context using a fixed base prompt.
2. **Robust prompting**: uses a constrained prompt that asks the model to avoid unsupported, vague, or low-value feedback.
3. **Context-quality gate**: detects insufficient or inconsistent context and skips, downgrades, or escalates low-context cases.
4. **Post-generation verification**: checks generated comments for support, relevance, correctness, and actionability before display.
5. **Hybrid gate plus verifier**: combines context-quality gating and post-generation verification.

If the dataset and implementation allow it, a retrieval-augmented context strategy can be added. It should be evaluated with the same metrics and should include the cost and noise introduced by additional context.

## Procedure

The evaluation proceeds in six steps.

1. Select a fixed sample of review instances.
2. Generate baseline comments using a fixed model, prompt, and decoding configuration.
3. Apply each mitigation strategy to the same sample where feasible.
4. Record the generated comment, mitigation decision, verifier output, context-quality judgment, and cost proxies.
5. Annotate the resulting comments and decisions using the operational taxonomy and annotation guideline.
6. Compute error-reduction, preservation, coverage, escalation, and cost metrics for each strategy.

All prompts, model versions, temperature settings, retrieval settings, static-analysis settings, gating rules, verifier prompts, and decision thresholds should be fixed before the final evaluation run. Pilot tuning should be separated from the final sample.

## Annotation Procedure

Annotators are shown the code change, available context, generated comment, and strategy output. They label the problematic-comment type, correctness, grounding, relevance, usefulness, actionability, context quality, decision, and confidence.

At least two annotators with software-engineering experience should label the pilot and a substantial subset of the final sample when feasible. The pilot should be used to refine the taxonomy and annotation guideline. Agreement should be reported separately for major label groups because labels such as usefulness and actionability may be more subjective than correctness or relevance.

Disagreements should be resolved through discussion or adjudication. The final dataset should preserve both initial labels and resolved labels where feasible. Preserving disagreement reasons is especially useful for understanding ambiguous categories such as useful-but-not-directly-acceptable comments or context-dependent comments.

## Metrics

The main error-reduction metrics are:

- overall problematic-comment rate;
- failure-type-specific rates;
- unsupported or hallucinated comment rate;
- irrelevant comment rate;
- wrong-location or wrong-cause rate;
- invalid fix suggestion rate;
- non-actionable and low-value comment rates.

The main preservation and workflow metrics are:

- useful comments retained;
- useful comments wrongly suppressed;
- review coverage retained;
- rewrite rate;
- human escalation rate;
- context-dependent cases routed correctly;
- number of additional model or verifier calls;
- approximate token cost;
- latency proxy where measurable.

The study should report confidence intervals or uncertainty summaries where the sample size permits. When the sample is small, descriptive results should be paired with qualitative examples and conservative interpretation.

## Planned Result Tables

The empirical section should include at least three result tables once the study is run.

<!-- table: caption="Planned empirical result tables." label="tab:planned-result-tables" -->
| Table | Purpose |
| --- | --- |
| Strategy-by-failure-type table | Shows which problematic-comment categories are reduced by each strategy. |
| Preservation and coverage table | Shows useful comments retained, useful comments wrongly suppressed, review coverage, rewrite rate, and escalation rate. |
| Cost and effort table | Shows additional calls, token cost, latency proxy, and human effort or escalation burden. |

These tables should be accompanied by a small number of qualitative examples. The examples should illustrate trade-offs rather than merely show successful or failed comments.

## Interpretation Rules

A strategy should not be described as better only because it suppresses more comments. A strategy is preferable only when its error reduction is balanced against useful-feedback preservation, coverage, cost, and human escalation.

The hybrid strategy should not be assumed to dominate the individual strategies. It may reduce complementary failure types, but it may also increase suppression, cost, or escalation. The analysis should therefore report where the hybrid improves the trade-off and where it does not.

Context quality should be analyzed as a moderator. The study should examine whether low-context or inconsistent-context instances produce different failure patterns and whether mitigation strategies behave differently under such conditions.
