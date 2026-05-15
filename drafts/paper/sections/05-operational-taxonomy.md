# Operational Taxonomy of Problematic Comments

The empirical comparison requires labels that distinguish different kinds of problematic generated comments. A single binary label such as correct or incorrect is not enough because a generated review comment can fail in several ways. It may be technically wrong, unsupported by the available context, irrelevant to the changed code, too vague to act on, or valid but too low-value to justify reviewer attention. It may also contain a useful signal while being unsuitable to show directly. This section defines the operational taxonomy used to annotate generated comments, compare mitigation strategies, and interpret trade-offs.

The taxonomy is operational rather than only descriptive. Each label is intended to support three tasks: human annotation, strategy-by-failure-type comparison, and mitigation-decision analysis. The labels are derived from the targeted literature review, the cross-paper synthesis, and pilot inspection of generated comments. The taxonomy is intentionally smaller than the full failure inventory in the synthesis notes: highly specialized cases such as security-specific, performance-specific, static-analysis-specific, and evaluator-specific failures are handled as optional sublayers or decision modifiers unless they directly affect the generated comment being annotated.

## Design Principles

The taxonomy follows five design principles.

First, it separates failure types from evaluation dimensions. Correctness, grounding, relevance, usefulness, actionability, severity, and context quality are evaluation dimensions. Unsupported claim, wrong cause, irrelevant comment, and invalid fix suggestion are failure types. Keeping these separate prevents annotation from collapsing distinct concerns into one coarse quality label.

Second, it supports mitigation decisions. The purpose of labeling is not only to describe a comment but also to decide whether it should be shown, suppressed, rewritten, or escalated. A useful taxonomy should explain why a strategy removes, preserves, rewrites, or routes a comment.

Third, it captures gray-zone cases. Some comments are not clearly good or bad. A comment may be useful but weakly grounded, correct but low-value, or impossible to judge without additional context. These cases are central to the study because they reveal the cost of aggressive filtering.

Fourth, it supports paired strategy comparison. The same taxonomy is applied to comments and decisions produced by all strategies. This allows the analysis to ask which failure types are reduced by robust prompting, context-quality gating, post-generation verification, or hybrid mitigation.

Fifth, it is designed for annotator use. Each category should have a definition, inclusion criteria, exclusion criteria, and decision notes in the annotation guideline. The paper-level taxonomy gives the conceptual structure; the annotation guideline should provide concrete examples and counterexamples.

## Label Architecture

The annotation uses three kinds of labels: primary failure labels, secondary failure labels, and evaluation-dimension labels.

The **primary failure label** captures the dominant reason a comment should not be shown as-is. The **secondary failure labels** capture additional issues that matter for analysis. For example, a comment may primarily be an unsupported claim and secondarily be a specialized-risk comment because it makes an unverified security claim. Evaluation-dimension labels record graded or categorical judgments such as correctness, grounding, usefulness, actionability, and context quality.

<!-- table: caption="Label architecture used in the operational taxonomy." label="tab:taxonomy-label-architecture" -->
| Label type | Purpose | Example |
| --- | --- | --- |
| Primary failure label | Dominant reason the comment should not be shown as-is. | Unsupported claim. |
| Secondary failure label | Additional failure mode relevant to interpretation or mitigation. | Wrong location; invalid fix suggestion. |
| Evaluation-dimension label | Judgment dimension used to compare comments and decisions. | Grounding, usefulness, actionability, severity. |
| Mitigation decision label | Recommended action before the comment reaches the user. | Show, suppress, rewrite, escalate. |
| Confidence label | Annotator confidence in the judgment under the available context. | High, medium, low. |

This architecture avoids forcing all information into a single class. It also supports the decision-confusion analysis in Section 4: a strategy decision can be compared with the resolved human decision, while the taxonomy explains the reason for disagreement.

## Core Taxonomy

Table \ref{tab:problematic-comment-taxonomy} defines the core failure labels used in the empirical comparison. The labels are grouped by the kind of failure they represent, but annotators select labels at the failure-label level rather than only at the group level.

<!-- table: caption="Operational taxonomy of problematic generated review comments." label="tab:problematic-comment-taxonomy" longtable="true" -->
| Failure group | Failure label | Definition | Typical mitigation implication |
| --- | --- | --- | --- |
| Grounding and context | Unsupported or hallucinated claim | The comment makes a factual, causal, behavioral, or risk claim that is not supported by the available diff, surrounding code, or supplied context. | Suppress when unsupported; rewrite with uncertainty or escalate when the signal may be important. |
| Grounding and context | Context-dependent or insufficient-context comment | The comment cannot be judged reliably because required project, API, version, specification, runtime, or cross-file context is missing or inconsistent. | Escalate, request more context, or apply a context-quality gate. |
| Grounding and context | Stale or contradictory-context comment | The comment relies on documentation, retrieved evidence, examples, or assumptions that are stale or inconsistent with the code. | Suppress or escalate until the evidence is verified. |
| Correctness | Incorrect technical claim | The comment states something technically false about the code, API, type, behavior, control flow, or language semantics. | Suppress; do not rewrite unless a correct related concern can be separated. |
| Correctness | Wrong API, type, or framework assumption | The comment assumes an incorrect return type, API contract, framework behavior, version, configuration, or runtime invariant. | Suppress or rewrite after adding project-specific evidence. |
| Localization and causality | Wrong location or wrong cause | The comment identifies the wrong line, hunk, component, or causal explanation for an otherwise plausible concern. | Rewrite if the concern is useful; suppress if the wrong location or cause makes it misleading. |
| Relevance and scope | Irrelevant or out-of-scope comment | The comment is unrelated to the reviewed change, ignores the pull-request intent, or targets a concern outside the review scope. | Suppress unless it should be routed as a separate issue. |
| Actionability and explanation | Non-actionable comment | The developer cannot determine a concrete next step because the comment is vague, underspecified, or lacks a clear review request. | Rewrite when the concern is useful; suppress when it adds little value. |
| Actionability and explanation | Weak or unsupported rationale | The comment identifies a possible concern but gives a vague, generic, or unsupported explanation of why it matters. | Rewrite with grounded rationale or suppress if the rationale is misleading. |
| Repair and suggestion quality | Invalid fix suggestion | The suggested fix does not resolve the issue, introduces a regression, changes intended behavior, or is unsafe without further validation. | Suppress the fix suggestion; possibly rewrite as a concern without the fix. |
| Value and workflow | Low-value or redundant comment | The comment may be technically valid but is too obvious, stylistic, redundant, minor, or costly relative to its review value. | Suppress, aggregate, or show only under low-noise settings. |
| Value and workflow | Workflow-friction comment | The comment increases reviewer or author burden without improving correctness, maintainability, understanding, or decision quality. | Suppress or aggregate; monitor signal-to-noise and reviewer burden. |
| Preservation gray zone | Useful but not directly acceptable comment | The comment contains a useful signal but is not suitable to show as-is because it is uncertain, overconfident, poorly phrased, weakly grounded, or insufficiently actionable. | Rewrite or escalate rather than suppress. |
| Specialized risk | Specialized-risk comment | The comment makes a security, privacy, concurrency, performance, data-loss, or financial-risk claim that requires stronger evidence than ordinary style or maintainability feedback. | Escalate or verify with specialized evidence before showing. |

The taxonomy is not intended to force every generated comment into exactly one failure type. A comment can have one primary label and multiple secondary labels. The primary label should capture the dominant reason the comment should not be shown as-is. Secondary labels should capture additional properties that affect mitigation, cost, or later analysis.

## Inclusion and Exclusion Rules

The following rules reduce ambiguity during annotation.

An **unsupported or hallucinated claim** should be used when the comment asserts a concrete issue, behavior, risk, or causal relationship without enough evidence in the available context. It should not be used merely because the comment is low-value or stylistic. If the available context directly contradicts the claim, the stronger label is **incorrect technical claim**.

A **context-dependent or insufficient-context comment** should be used when the comment may be valid but the annotator cannot judge it reliably under the provided evidence. This label is different from unsupported claim: unsupported claim describes an overconfident comment without evidence; context-dependent describes an evaluation situation where the missing evidence is central to the judgment.

An **incorrect technical claim** should be used when the comment is demonstrably false under the available code, API, language semantics, or configuration. If the claim cannot be judged, use context-dependent rather than incorrect.

A **wrong location or wrong cause** label should be used when the underlying concern may be valid but the comment points to the wrong file, hunk, line, component, or causal explanation. This label is especially important for rewrite decisions because the useful signal may be preserved after correction.

A **non-actionable comment** should be used when the author cannot infer a clear next step. It should not be used for high-level design comments that are intentionally exploratory but still actionable as discussion prompts. Those comments may be labeled useful but not directly acceptable if they need reframing rather than removal.

A **low-value or redundant comment** should be used when the comment is technically acceptable but not worth showing under normal review-noise constraints. It should not be used for comments that are false, unsupported, or irrelevant; those labels take priority.

A **useful but not directly acceptable comment** should be used when suppressing the comment would lose a useful signal, but showing it as written would be inappropriate. This label is central to the preservation analysis because it identifies cases where rewrite or escalation may be better than suppression.

A **specialized-risk comment** should be used as a secondary label when the comment concerns security, privacy, concurrency, performance, data loss, or other high-impact domains where stronger evidence is required. It can also be primary when the main reason for not showing the comment is that it needs specialized verification.

## Decision Rules for Ambiguous Cases

Ambiguous cases are central to the study because they expose mitigation trade-offs.

A comment that is technically correct but too minor should be labeled low-value rather than incorrect. This distinction matters because a low-value comment may be suppressed for signal-to-noise reasons, while an incorrect comment should not be preserved.

A comment that raises a plausible concern but lacks enough evidence should be labeled context-dependent or unsupported, depending on whether additional context could reasonably resolve the judgment. If the available evidence contradicts the claim, the stronger label is incorrect technical claim. If the available evidence is simply insufficient, the stronger label is context-dependent or unsupported.

A comment that contains a useful concern but is phrased too strongly should not automatically be counted as useless. It should be labeled useful but not directly acceptable when rewriting, softening, or grounding could preserve the signal.

A comment with a valid concern but an invalid fix suggestion should receive labels that preserve both facts: the concern may be useful, while the fix suggestion is invalid. This is important because a mitigation strategy that suppresses the whole comment may lose useful feedback, while a rewrite strategy may preserve the concern and remove the unsafe fix.

A comment that is specialized-risk but weakly grounded should not be shown simply because the issue is important. It should usually be escalated or verified with stronger evidence. This rule prevents high-severity labels from overriding grounding requirements.

## Mapping Failure Labels to Mitigation Decisions

The taxonomy does not map labels mechanically to one decision. Instead, labels constrain the plausible decisions. Table \ref{tab:taxonomy-decision-mapping} summarizes the typical mapping.

<!-- table: caption="Typical mapping from taxonomy labels to mitigation decisions." label="tab:taxonomy-decision-mapping" longtable="true" -->
| Failure label | Show | Suppress | Rewrite | Escalate |
| --- | --- | --- | --- | --- |
| Unsupported or hallucinated claim | Rarely appropriate. | Appropriate when the claim has no useful signal. | Appropriate if a weaker, grounded concern remains. | Appropriate if the concern may be important but evidence is missing. |
| Context-dependent or insufficient-context comment | Rarely appropriate as-is. | Appropriate when the concern is low-value. | Appropriate when uncertainty can be stated clearly. | Appropriate when judgment requires additional evidence. |
| Incorrect technical claim | Not appropriate. | Usually appropriate. | Appropriate only if a correct related concern can be separated. | Rarely needed unless specialized evidence is required. |
| Wrong location or wrong cause | Not appropriate as-is. | Appropriate if misleading and not recoverable. | Appropriate when the concern is valid but poorly localized or explained. | Appropriate when cause cannot be determined. |
| Irrelevant or out-of-scope comment | Usually not appropriate. | Usually appropriate. | Rarely appropriate. | Appropriate if it should become a separate issue. |
| Non-actionable comment | Not appropriate as-is. | Appropriate when the concern is weak. | Usually appropriate when the concern is useful. | Appropriate for high-level design or risk discussion. |
| Invalid fix suggestion | Not appropriate as-is. | Appropriate for the fix suggestion. | Appropriate if the concern can be preserved without the fix. | Appropriate when validation is required. |
| Low-value or redundant comment | Usually not appropriate. | Usually appropriate under normal noise constraints. | Appropriate if aggregation or concise rewriting preserves value. | Rarely appropriate. |
| Useful but not directly acceptable comment | Not appropriate as-is. | Risky because it loses useful feedback. | Usually appropriate. | Appropriate when additional judgment is needed. |
| Specialized-risk comment | Only after verification. | Appropriate for false alarms. | Appropriate if evidence or phrasing can be improved. | Often appropriate when evidence is incomplete. |

This mapping supports the decision-confusion analysis in Section 4. For example, suppressing a comment labeled useful but not directly acceptable is counted differently from suppressing a comment labeled irrelevant. The former may be recoverable feedback loss, while the latter may be successful noise reduction.

## Link to the Empirical Evaluation

The taxonomy is used in four parts of the empirical evaluation.

First, it measures the baseline distribution of problematic comments. Second, it supports strategy-by-failure-type comparison: each mitigation strategy can be evaluated by which categories it reduces. Third, it enables preservation analysis by identifying useful comments that were wrongly suppressed, comments that should have been rewritten, and context-dependent cases that should have been escalated rather than shown or removed. Fourth, it explains the decision-confusion analysis by linking each incorrect strategy decision to a failure label.

The taxonomy therefore functions as a measurement instrument for the empirical study. It is not the final result by itself. Its value is tested by whether annotators can apply the labels consistently and whether the labels reveal trade-offs that a single correctness or acceptance score would miss.

## Pilot Refinement and Reliability Checks

The pilot annotation round should test whether the taxonomy is usable by annotators. The pilot should identify labels that overlap too much, labels that annotators interpret inconsistently, and failure types that are missing from the core taxonomy. After the pilot, label definitions should be revised before the final annotation sample.

Reliability should be assessed on key labels, not only on the final mitigation decision. At minimum, the study should report agreement on problematic-comment presence, primary failure label, usefulness, actionability, and recommended mitigation decision when feasible. Disagreements should be treated as evidence about difficult judgment cases rather than only as noise. For example, repeated disagreement between unsupported and context-dependent labels may indicate that the available context is insufficient or that the annotation guideline needs clearer evidence requirements.
