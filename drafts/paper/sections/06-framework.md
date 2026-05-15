# Trade-Off-Aware Evaluation Framework

The planned empirical study compares mitigation strategies, but the comparison needs a framework that prevents misleading conclusions. A strategy that removes more generated comments is not necessarily better. It may remove harmful comments, but it may also remove useful feedback, reduce review coverage, increase latency, or route too many cases to human reviewers. This section defines the trade-off-aware evaluation framework that will be used to interpret the empirical results once the study is executed.

The framework connects six layers: input and context quality, generated-comment quality, problematic-comment type, mitigation decision, preservation and coverage, and cost and evaluator validity. These layers turn evaluation from passive scoring into a workflow decision problem.

<!-- TODO: After running the empirical study, update this opening to summarize how the framework was actually used in the analysis and whether any layers needed to be revised. -->

## Framework Overview

<!-- table: caption="Layers of the trade-off-aware evaluation framework." label="tab:framework-layers" -->
| Layer | Evaluation question | Example measurements |
| --- | --- | --- |
| Input and context quality | Is the instance judgeable under the available evidence? | context sufficiency, consistency, freshness, reviewability |
| Generated-comment quality | Is the comment technically sound, grounded, relevant, useful, and actionable? | correctness, grounding, relevance, usefulness, actionability |
| Problematic-comment type | What kind of failure, if any, explains why the comment is problematic? | unsupported, irrelevant, wrong cause, invalid fix, low-value |
| Mitigation decision | What should happen before the comment reaches the user? | show, suppress, rewrite, escalate |
| Preservation and coverage | What useful feedback or review coverage is preserved or lost? | useful comments retained, useful comments wrongly suppressed, coverage retained |
| Cost and evaluator validity | What effort, computation, latency, or measurement risk is introduced? | model calls, human escalation, annotation agreement, judge robustness |

The framework is designed to be applied to each strategy in the same way. For every generated comment, the study will ask whether the comment is problematic, what type of problem it has, what decision should be taken, what useful feedback would be preserved or lost, and what cost the decision introduces.

## Layer 1: Input and Context Quality

Context quality determines whether a generated comment can be judged and whether a mitigation strategy has enough evidence to act. Context quality includes relevance, completeness, specificity, consistency, freshness, reviewability, provenance, behavioral evidence, attention load, and cost.

A context-quality gate can use this layer before generation or before display. If the available context is too weak, the system may skip automatic review, request more context, or escalate the case. This is not a failure of the model alone; it may be a limitation of the evaluation instance. Treating context as an evaluation object helps separate unsupported model output from insufficient or inconsistent input evidence.

## Layer 2: Generated-Comment Quality

Generated-comment quality is evaluated across several dimensions rather than a single correctness score. The key dimensions are technical correctness, grounding, relevance, specificity, explanation quality, usefulness, and actionability.

These dimensions can disagree. A comment can be relevant but ungrounded, grounded but low-value, technically plausible but non-actionable, or useful but too uncertain to show directly. The framework therefore avoids a single pass/fail judgment and instead maps quality dimensions to mitigation decisions.

## Layer 3: Problematic-Comment Type

The taxonomy labels explain why a comment is problematic. The failure type matters because different failures require different interventions. Unsupported claims may be caught by verification, context-dependent cases may be routed by a context-quality gate, non-actionable comments may be improved by rewriting, and low-value comments may be suppressed or aggregated.

This layer is the bridge between annotation and strategy comparison. It allows the study to report not only that a strategy reduces problematic comments, but which categories it reduces and which categories remain.

## Layer 4: Mitigation Decision

The framework uses four mitigation decisions.

- `show`: the comment is suitable to present as review feedback.
- `suppress`: the comment should not be shown because it is harmful, unsupported, irrelevant, incorrect, or too low-value.
- `rewrite`: the comment contains a useful signal but needs clarification, grounding, softening, or actionability improvements.
- `escalate`: the comment may matter but requires human judgment or additional context.

These decisions are intentionally more expressive than binary accept/reject labels. They capture cases where a comment should not be shown as-is but should not be discarded either.

## Layer 5: Preservation, Coverage, and Cost

This layer measures the trade-off introduced by each mitigation strategy. Error reduction is measured by the rate of problematic comments removed or corrected. Preservation is measured by useful comments retained, useful comments wrongly suppressed, and useful-but-not-directly-acceptable comments rewritten rather than removed. Coverage is measured by the proportion of review instances that still receive useful automatic feedback after filtering, gating, or escalation.

Cost includes additional model calls, verifier calls, retrieval operations, latency proxies, human escalation, and annotation or verification effort. Cost should be reported even when it is approximate because a strategy that improves quality at excessive cost may not be practical in real review workflows.

## Layer 6: Evaluator Validity

The final layer concerns the reliability of the measurement itself. Human annotators may disagree on usefulness, actionability, or severity. LLM-based judges may be sensitive to prompts, output order, model choice, and verbosity. Evaluator validity is therefore part of the evaluation, not an implementation detail.

The empirical study should report inter-annotator agreement where feasible and should avoid treating LLM-as-a-Judge outputs as ground truth without validation. If LLM-based judges are used, their role should be explicit: they may support screening or provide auxiliary evidence, but the main claims about mitigation quality should be grounded in the annotation protocol.

## Using the Framework in the Empirical Study

For each strategy, the planned analysis reports a trade-off profile rather than a single ranking. A profile includes the failure types reduced, the useful comments preserved, the useful comments wrongly suppressed, the coverage retained, the number of comments rewritten or escalated, and the added cost.

This design makes it possible to compare strategies without assuming that one strategy is universally best. Robust prompting may reduce non-actionable comments but leave unsupported claims. Post-generation verification may reduce unsupported comments but wrongly suppress useful weak signals. A context-quality gate may reduce context-dependent failures but lower coverage. A hybrid strategy may improve safety while adding cost and escalation burden. The framework is designed to make these trade-offs visible.

<!-- TODO: After empirical analysis, replace the hypothetical strategy examples with the actual observed trade-off profiles and note any framework dimensions that were unmeasurable or revised. -->
