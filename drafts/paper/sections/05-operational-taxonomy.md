# Operational Taxonomy of Problematic Comments

The empirical comparison requires labels that distinguish different kinds of problematic generated comments. A single binary label such as correct or incorrect is not enough because a generated review comment can fail in several different ways. It may be technically wrong, unsupported by the available context, irrelevant to the changed code, too vague to act on, or valid but too low-value to justify reviewer attention. It may also contain a useful signal while being unsuitable to show directly. This section defines the operational taxonomy used to annotate generated comments and interpret mitigation trade-offs.

The taxonomy is operational rather than only descriptive. Each category is intended to support human annotation, strategy comparison, and mitigation decisions. The categories are derived from the targeted literature review, the cross-paper synthesis, and pilot inspection of generated comments. They are expected to be refined during the pilot annotation round.

## Design Goals

The taxonomy has four design goals.

First, it should separate failure types from evaluation dimensions. Correctness, grounding, relevance, usefulness, and actionability are dimensions. Unsupported claim, wrong cause, irrelevant comment, and invalid fix suggestion are failure types. Keeping these separate prevents the annotation from collapsing distinct concerns into one label.

Second, it should support mitigation decisions. The purpose of labeling is not only to describe comments but also to decide whether a comment should be shown, suppressed, rewritten, or escalated. A label is useful when it helps explain why a strategy removes, preserves, rewrites, or routes a comment.

Third, it should capture gray-zone cases. Some comments are not clearly good or bad. A comment may be useful but weakly grounded, correct but low-value, or impossible to judge without additional context. These cases are important because they reveal the cost of aggressive filtering.

Fourth, it should be usable by annotators with software-engineering experience. Each category should have a concise definition, inclusion criteria, exclusion criteria, and examples or decision notes in the annotation guideline.

## Taxonomy Overview

<!-- table: caption="Operational taxonomy of problematic generated review comments." label="tab:problematic-comment-taxonomy" longtable="true" -->
| Category | Definition | Typical mitigation implication |
| --- | --- | --- |
| Unsupported or hallucinated comment | The comment makes a claim that is not supported by the available diff, surrounding code, or supplied context. | Suppress, rewrite with uncertainty, or escalate when the issue may be important. |
| Irrelevant comment | The comment is unrelated to the reviewed change or targets a concern outside the review scope. | Suppress unless it exposes a broader issue that should be routed separately. |
| Incorrect technical claim | The comment states something technically false about the code, API, type, behavior, or control flow. | Suppress; do not rewrite unless a correct related issue is present. |
| Wrong location or wrong cause | The comment identifies the wrong line, component, or causal explanation for an otherwise plausible concern. | Rewrite if the concern is useful; suppress if the location or cause makes it misleading. |
| Invalid fix suggestion | The suggested fix does not resolve the issue, introduces a regression, or changes intended behavior. | Suppress the fix suggestion; possibly rewrite the comment as a concern without a fix. |
| Non-actionable comment | The developer cannot determine what to do next because the comment is vague, underspecified, or lacks a concrete review request. | Rewrite when the underlying concern is useful; suppress when it adds little value. |
| Low-value comment | The comment may be valid but is too obvious, stylistic, redundant, or minor to justify reviewer attention. | Suppress, aggregate, or show only under low-noise settings. |
| Context-dependent comment | The comment cannot be judged reliably because required context is missing, inconsistent, stale, or too broad. | Escalate, request more context, or apply a context-quality gate. |
| Useful but not directly acceptable comment | The comment contains a useful signal but is not suitable to show as-is because it is uncertain, poorly phrased, or insufficiently grounded. | Rewrite or escalate rather than suppress. |
| Specialized-risk comment | The comment makes a security, performance, concurrency, or data-loss claim that requires stronger evidence than ordinary style or maintainability feedback. | Escalate or verify with specialized evidence before showing. |

The taxonomy is not intended to force every generated comment into exactly one failure type. A comment may have a primary label and secondary labels. For example, a security warning may be both unsupported and specialized-risk. A comment that points to the wrong line may also include an invalid fix suggestion. The primary label should capture the dominant reason the comment should not be shown as-is.

## Decision Rules for Ambiguous Cases

Ambiguous cases are central to the study because they expose mitigation trade-offs. The following decision rules guide annotation.

A comment that is technically correct but too minor should be labeled low-value rather than incorrect. This distinction matters because a low-value comment may be a target for aggregation or suppression, while an incorrect comment should not be preserved.

A comment that raises a plausible concern but lacks enough evidence should be labeled context-dependent or unsupported, depending on whether additional context could reasonably resolve the judgment. If the available evidence contradicts the claim, the stronger label is incorrect technical claim. If the available evidence is simply insufficient, the stronger label is context-dependent or unsupported.

A comment that contains a useful concern but is phrased too strongly should not automatically be counted as useless. It should be labeled useful but not directly acceptable when rewriting or softening could preserve the signal.

A comment with a valid concern but an invalid fix suggestion should receive a label that preserves both facts: the concern may be useful, while the fix suggestion is invalid. This is important because a mitigation strategy that suppresses the whole comment may lose useful feedback, while a rewrite strategy may preserve the concern and remove the unsafe fix.

## Link to the Empirical Evaluation

The taxonomy is used in three parts of the empirical evaluation. First, it measures the baseline distribution of problematic comments. Second, it supports strategy-by-failure-type comparison: each mitigation strategy can be evaluated by which categories it reduces. Third, it enables preservation analysis: the study can identify useful comments that were wrongly suppressed, comments that should have been rewritten, and context-dependent cases that should have been escalated rather than shown or removed.

The taxonomy therefore functions as a measurement instrument for the empirical study. It is not the final result by itself. Its value is tested by whether annotators can apply the labels consistently and whether the labels reveal trade-offs that a single correctness or acceptance score would miss.
