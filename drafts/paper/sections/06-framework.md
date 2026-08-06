# Trade-Off-Aware Evaluation Framework

The synthesis indicates that mitigation cannot be evaluated only by the number of comments it removes. Interventions may suppress useful signals, reduce coverage, change intent, or add latency and reviewer effort [@p04_kumar2026_swe_prbench; @p07_olewicki2024_revmate; @p10_sun2025_bitsai_cr; @p18_bensghaier2025_curated_reviews; @p35_mcaleese2024_llm_critics; @p65_ameen2026_qasecclaw]. The framework below is a proposal for future evaluation rather than an executed comparison.

The framework connects six layers: input and context quality, comment quality, failure type, handling decision, preservation and coverage, and cost and evaluator validity. Together, they connect quality assessment to concrete workflow decisions.

## Framework Overview

<!-- table: caption="Layers of the trade-off-aware evaluation framework." label="tab:framework-layers" -->
| Layer | Evaluation question | Example measurements |
| --- | --- | --- |
| Input and context quality | Is the instance judgeable under the available evidence? | context sufficiency, consistency, freshness, reviewability |
| Comment quality | Is the comment technically sound, grounded, relevant, useful, and actionable? | correctness, grounding, relevance, usefulness, actionability |
| Failure type | What kind of failure, if any, explains why the comment is problematic? | unsupported, irrelevant, wrong cause, invalid fix, low-value |
| Mitigation decision | What should happen before the comment reaches the user? | show, suppress, rewrite, escalate |
| Preservation and coverage | What useful feedback or review coverage is preserved or lost? | useful comments retained, useful comments wrongly suppressed, coverage retained |
| Cost and evaluator validity | What effort, computation, latency, or measurement risk is introduced? | model calls, human escalation, annotation agreement, judge robustness |

Applying the same layers across strategies makes their consequences comparable even when they address different failures.

## Layer 1: Input and Context Quality

Context quality determines whether a generated comment can be judged and whether a mitigation strategy has enough evidence to act. Context quality includes relevance, completeness, specificity, consistency, freshness, reviewability, provenance, behavioral evidence, attention load, and cost.

A context-quality gate can use this layer before generation or before display. If the available context is too weak, the system may skip automatic review, request more context, or escalate the case. This is not a failure of the model alone; it may be a limitation of the evaluation instance. Treating context as an evaluation object helps separate unsupported model output from insufficient or inconsistent input evidence.

## Layer 2: Comment Quality

Comment quality spans technical correctness, grounding, relevance, specificity, explanation quality, usefulness, and actionability rather than a single correctness score.

These dimensions can disagree. A comment can be relevant but ungrounded, grounded but low-value, technically plausible but non-actionable, or useful but too uncertain to show directly. The framework therefore avoids a single pass/fail judgment and instead maps quality dimensions to mitigation decisions.

## Layer 3: Failure Type

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

An empirical study should report inter-annotator agreement and avoid treating LLM-as-a-Judge outputs as ground truth without validation. If LLM-based judges are used, their role should be explicit: they may support screening or provide auxiliary evidence, but primary mitigation-quality claims should be grounded in a validated annotation protocol.

## Empirical Use

A strategy can be summarized by a trade-off profile: failures reduced, useful comments preserved or wrongly withheld, coverage retained, comments revised or escalated, and added cost.

Such profiles allow comparison without assuming that one strategy is universally best. Prompting may improve actionability while leaving unsupported claims; verification may remove those claims while also withholding weak but useful signals; context gates may improve reliability at the expense of coverage. Hybrid strategies can reduce several risks while adding cost and escalation burden.

These examples are hypotheses derived from the review, not empirical findings of the present study. Future work should test them and report any framework dimensions that prove unmeasurable or require revision.
