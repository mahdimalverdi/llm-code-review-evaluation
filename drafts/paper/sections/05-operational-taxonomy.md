# Operational Taxonomy of Problematic Comments

The reviewed literature requires labels that distinguish different kinds of problematic LLM-generated code review comments. A binary label such as correct or incorrect is insufficient because a comment may be unsupported, irrelevant, vague, non-actionable, incorrectly localized, or valid but too low-value to justify attention [@p02_tantithamthavorn2026_hallujudge; @p08_liu2025_too_noisy; @p19_nguyen2025_fine_grained_classification; @p35_mcaleese2024_llm_critics; @p57_heumuller2025_relevance_reviews; @p60_ahmed2025_feedback_useful]. It may also contain a recoverable signal while being unsuitable to show directly. This section defines the literature-derived taxonomy for future annotation and mitigation analysis.

The taxonomy is operational rather than only descriptive. Each label is intended to support three tasks: human annotation, strategy-by-failure-type comparison, and mitigation-decision analysis. The initial labels are derived from the targeted literature review and the cross-paper synthesis. The taxonomy is intentionally smaller than the full failure inventory in the synthesis notes: specialized, context-specific, and workflow-specific details are represented as secondary modifiers unless they are necessary to explain the dominant reason that a comment should not be shown directly.

The taxonomy is a protocol-level measurement proposal, not an empirically validated instrument. Future work should test it through pilot annotation, agreement analysis, and adjudication of ambiguous cases, reporting any labels added, merged, removed, demoted, or clarified.

## Design Principles

The taxonomy follows five design principles.

First, it separates failure types from evaluation dimensions. Correctness, grounding, relevance, usefulness, actionability, severity, and context quality are evaluation dimensions. Unsupported claim, wrong cause, irrelevant comment, and invalid fix suggestion are failure types. Keeping these separate prevents annotation from collapsing distinct concerns into one coarse quality label.

Second, it separates failure types from mitigation decisions. The purpose of labeling is not only to describe a comment but also to support decisions about whether it should be shown, suppressed, rewritten, or escalated. However, the decision is not itself a failure label. A comment may have the same core failure label but lead to different mitigation decisions depending on usefulness, grounding, severity, and context availability.

Third, it captures gray-zone cases. Some comments are not clearly good or bad. A comment may be useful but weakly grounded, correct but low-value, or impossible to judge without additional context. These cases are central to the study because they reveal the cost of aggressive filtering.

Fourth, it supports paired strategy comparison. The same taxonomy is applied to comments and decisions produced by all strategies. This allows the analysis to ask which failure types are reduced by robust prompting, context-quality gating, post-generation verification, or hybrid mitigation.

Fifth, it is designed for annotator use. Each category should have a definition, inclusion criteria, exclusion criteria, and decision notes in the annotation guideline. The paper-level taxonomy gives the conceptual structure; the annotation guideline provides concrete examples and counterexamples.

## Label Architecture

The annotation uses five kinds of labels: core failure labels, secondary modifiers, evaluation-dimension labels, mitigation-decision labels, and confidence labels. Figure \ref{fig:taxonomy-label-architecture} summarizes their roles.

<!-- figure: path="figures/taxonomy_label_architecture.tex" caption="Label architecture used in the operational taxonomy." label="fig:taxonomy-label-architecture" -->

The **core failure label** captures the dominant reason a comment should not be shown directly. The **secondary modifiers** capture additional details that matter for interpretation, cost, or mitigation but should not usually become the primary class. For example, a comment may have the core label **Incorrect technical claim** and the secondary modifier **wrong API, type, or framework assumption**. Evaluation-dimension labels record graded or categorical judgments such as correctness, grounding, usefulness, actionability, severity, and context quality. Mitigation-decision labels record the human reference action used for decision-confusion analysis.

This architecture avoids forcing all information into a single class. It also supports the decision-confusion analysis described in the methodology: a strategy decision can be compared with the resolved human reference decision, while the taxonomy explains the reason for disagreement.

## Core Failure Labels

Table \ref{tab:problematic-comment-taxonomy} defines the core failure labels used for primary annotation. These labels are intentionally limited so that annotators can apply them consistently. More specific details are captured as secondary modifiers in Table \ref{tab:taxonomy-secondary-modifiers}.

<!-- table: caption="Core failure labels for problematic generated review comments." label="tab:problematic-comment-taxonomy" longtable="true" -->
| Core label | Definition | Typical mitigation implication |
| --- | --- | --- |
| Unsupported or hallucinated claim | The comment makes a factual, causal, behavioral, or risk claim that is not supported by the available diff, surrounding code, or supplied context. | Suppress when unsupported; rewrite with uncertainty or escalate when the signal may be important. |
| Context-dependent or insufficient-context comment | The comment cannot be judged reliably because required project, API, version, specification, runtime, or cross-file context is missing or inconsistent. | Escalate, request more context, or apply a context-quality gate. |
| Incorrect technical claim | The comment states something technically false about the code, API, type, behavior, control flow, language semantics, configuration, or runtime behavior. | Suppress; do not rewrite unless a correct related concern can be separated. |
| Wrong location or wrong cause | The comment identifies the wrong line, hunk, component, or causal explanation for an otherwise plausible concern. | Rewrite if the concern is useful; suppress if the wrong location or cause makes it misleading. |
| Irrelevant or out-of-scope comment | The comment is unrelated to the reviewed change, ignores the pull-request intent, or targets a concern outside the review scope. | Suppress unless it should be routed as a separate issue. |
| Non-actionable or weakly explained comment | The developer cannot determine a concrete next step, or the comment gives a vague, generic, or weak explanation of why the concern matters. | Rewrite when the concern is useful; suppress when it adds little value. |
| Invalid fix suggestion | The suggested fix does not resolve the issue, introduces a regression, changes intended behavior, or is unsafe without further validation. | Suppress the fix suggestion; possibly rewrite as a concern without the fix. |
| Low-value or redundant comment | The comment may be technically valid but is too obvious, stylistic, redundant, minor, or costly relative to its review value. | Suppress, aggregate, or show only under low-noise settings. |

A generated comment can have one core label and multiple secondary modifiers. The core label should capture the dominant reason the comment should not be shown directly. Secondary modifiers should capture additional properties that affect mitigation, cost, or later analysis.

The taxonomy intentionally does not use **useful but not directly acceptable** or **specialized-risk comment** as default core failure labels. The first is a mitigation-relevant state that is better represented through usefulness, actionability, grounding, and the **recoverable signal** modifier. The second is usually a domain-risk modifier because specialized evidence may be required for several different core failures. If pilot annotation shows that either state is frequent, reliably identifiable, and decision-changing, the executed study may promote it to a core label and must report that change explicitly.

## Secondary Modifiers

Secondary modifiers capture details that are important for analysis but too fine-grained or context-dependent to serve as stable primary labels. They can be used to explain disagreements, refine mitigation decisions, and support later sub-analyses.

<!-- table: caption="Secondary modifiers for additional failure details." label="tab:taxonomy-secondary-modifiers" longtable="true" -->
| Modifier | Use when | Typical parent label |
| --- | --- | --- |
| Wrong API, type, or framework assumption | The comment assumes an incorrect API contract, return type, framework behavior, version, configuration, or runtime invariant. | Incorrect technical claim. |
| Wrong location | The comment points to the wrong line, hunk, file, component, or changed region while the underlying concern may still be valid. | Wrong location or wrong cause. |
| Wrong causal explanation | The comment identifies a plausible issue but explains the cause incorrectly or attributes the problem to the wrong mechanism. | Wrong location or wrong cause. |
| Stale or contradictory context | The comment relies on documentation, retrieved evidence, examples, or assumptions that are stale or inconsistent with the code. | Unsupported or context-dependent comment. |
| Weak rationale | The comment identifies a possible concern but gives a vague, generic, or unsupported explanation of why it matters. | Non-actionable or weakly explained comment. |
| Workflow-friction risk | The comment is likely to increase reviewer or author burden without improving correctness, maintainability, understanding, or decision quality. | Low-value or redundant comment. |
| Specialized evidence required | The comment concerns security, privacy, concurrency, performance, data loss, financial risk, or another high-impact area requiring stronger evidence. | Unsupported, context-dependent, invalid-fix, or low-value comment. |
| Overconfident phrasing | The comment presents an uncertain concern as certain. | Unsupported claim or context-dependent comment. |
| Recoverable signal | The comment contains a useful concern that could be preserved through rewriting even though the current wording should not be shown. | Non-actionable, weakly grounded, invalid-fix, wrong-location, or unsupported comment. |
| Separate-issue candidate | The comment is out of scope for the current review but may be valid as a separate issue. | Irrelevant or out-of-scope comment. |

This core and modifier split is intended to improve annotation reliability. If pilot annotation shows that a modifier is frequently selected and reliably distinguished, it may be promoted to a core label. Conversely, if a core label has low agreement, it may be merged with another label or demoted to a modifier. The executed study must report frequent modifiers, low-agreement labels, and any boundary changes between core labels and modifiers.

## Inclusion and Exclusion Rules

The following rules reduce ambiguity during annotation.

An **unsupported or hallucinated claim** should be used when the comment asserts a concrete issue, behavior, risk, or causal relationship without enough evidence in the available context. It should not be used merely because the comment is low-value or stylistic. If the available context directly contradicts the claim, the stronger label is **incorrect technical claim**.

A **context-dependent or insufficient-context comment** should be used when the comment may be valid but the annotator cannot judge it reliably under the provided evidence. This label is different from unsupported claim: unsupported claim describes an overconfident comment without evidence; context-dependent describes an evaluation situation where the missing evidence is central to the judgment.

An **incorrect technical claim** should be used when the comment is demonstrably false under the available code, API, language semantics, or configuration. If the falsehood comes from an incorrect API, type, framework, version, or runtime assumption, use **wrong API, type, or framework assumption** as a secondary modifier. If the claim cannot be judged, use context-dependent rather than incorrect.

A **wrong location or wrong cause** label should be used when the underlying concern may be valid but the comment points to the wrong file, hunk, line, component, or causal explanation. Use **wrong location** when the target is misplaced, and **wrong causal explanation** when the target may be relevant but the explanation of why it matters is wrong. This label is especially important for rewrite decisions because the useful signal may be preserved after correction.

A **non-actionable or weakly explained comment** should be used when the author cannot infer a clear next step or cannot understand why the concern matters. It should not be used for high-level design comments that are intentionally exploratory but still actionable as discussion prompts. Those comments may receive the **recoverable signal** modifier if they need reframing rather than removal.

A **low-value or redundant comment** should be used when the comment is technically acceptable but not worth showing under normal review-noise constraints. It should not be used for comments that are false, unsupported, or irrelevant; those labels take priority. If the issue is mainly the expected burden on reviewers or authors, use **workflow-friction risk** as a modifier rather than as a core label.

An **invalid fix suggestion** should be used when the comment's proposed change is the main unsafe or misleading element. If the comment also contains a demonstrably false explanation about current behavior, assign **incorrect technical claim** as the core label and use the invalid-fix information as a modifier or note. If the concern is valid but the proposed implementation is unsafe, assign **invalid fix suggestion** as the core label and add **recoverable signal** when the concern can be preserved.

A **recoverable signal** modifier should be used when suppressing the comment would lose a useful concern, but showing it as written would be inappropriate. This modifier is central to the preservation analysis because it identifies cases where rewrite or escalation may be better than suppression.

A **specialized evidence required** modifier should be used when the comment concerns a domain where ordinary code-context evidence is not enough to show the comment safely. This modifier should not override grounding requirements: a high-impact claim still requires support, verification, or escalation before display.

## Boundary Rules for Common Ambiguities

Some label boundaries are expected to be difficult in pilot annotation. Figure \ref{fig:taxonomy-boundary-logic} summarizes the main decision logic, and Table \ref{tab:taxonomy-boundary-rules} records the intended decision rule for the most important ambiguous pairs. The annotation guideline should expand these rules with concrete examples and counterexamples.

<!-- figure: path="figures/taxonomy_boundary_logic.tex" caption="Summary of the main boundary logic used to separate common ambiguous taxonomy cases." label="fig:taxonomy-boundary-logic" -->

<!-- table: caption="Boundary rules for common annotation ambiguities." label="tab:taxonomy-boundary-rules" longtable="true" -->
| Ambiguous pair | Use the first label when | Use the second label when |
| --- | --- | --- |
| Unsupported or hallucinated claim and context-dependent or insufficient-context comment | The comment makes an overconfident claim without support in the available evidence. | The missing evidence is central enough that the annotator cannot judge whether the claim is valid. |
| Incorrect technical claim and context-dependent or insufficient-context comment | The available code, API, configuration, or semantics shows that the claim is false. | The available evidence is insufficient to determine whether the claim is true or false. |
| Incorrect technical claim and wrong location or wrong cause | The underlying technical concern is false. | The concern may be valid, but the comment points to the wrong place or gives the wrong causal explanation. |
| Incorrect technical claim and invalid fix suggestion | The explanation of the current behavior, API, type, or semantics is demonstrably false. | The concern may be valid, but the proposed fix is unsafe, behavior-changing, or does not solve the issue. |
| Non-actionable or weakly explained comment and recoverable signal modifier | The concern is too vague or weak to preserve without substantial inference. | A useful signal is present, but it needs rewriting, softening, grounding, or clarification before display. |
| Low-value or redundant comment and irrelevant or out-of-scope comment | The comment is related to the change but too minor, redundant, or not worth reviewer attention. | The comment is not meaningfully related to the reviewed change or belongs outside the current review scope. |
| Specialized evidence required modifier and context-dependent or insufficient-context comment | The concern belongs to a high-impact domain that needs stronger evidence than ordinary feedback. | The main issue is that required project, API, runtime, or cross-file context is missing. |

The executed study should report examples for the most frequent boundary disagreements and update the annotation guideline if annotators use a different decision rule during pilot annotation.

## Illustrative Boundary Examples

Table \ref{tab:taxonomy-boundary-examples} provides compact examples of how the taxonomy should be applied. These examples are illustrative rather than empirical results; the final annotation guideline should replace or extend them with examples observed during pilot annotation.

<!-- table: caption="Illustrative examples for difficult taxonomy boundaries." label="tab:taxonomy-boundary-examples" longtable="true" -->
| Boundary | Illustrative comment pattern | Preferred label or modifier | Rationale |
| --- | --- | --- | --- |
| Unsupported and context-dependent cases | "This change will break retries" when no retry path or runtime behavior is available in the supplied context. | Unsupported or hallucinated claim, with overconfident phrasing if stated as certain. | The comment asserts a concrete failure without evidence in the available context. |
| Unsupported and context-dependent cases | "This may break retries, but the retry configuration is not shown." | Context-dependent or insufficient-context comment. | The comment explicitly depends on missing evidence and should be routed for more context. |
| Incorrect claims and invalid fixes | "This function returns null, so replace the caller with a null check" when the shown signature is non-nullable. | Incorrect technical claim. | The explanation of current behavior is false, so the fix rests on a false premise. |
| Invalid fixes and recoverable signals | "Use a global cache here" for a valid repeated-work concern when the global cache would introduce stale data. | Invalid fix suggestion with recoverable signal. | The performance concern may be useful, but the proposed fix is unsafe. |
| Non-actionable comments and recoverable signals | "This is risky" without naming the risk, affected path, or suggested next step. | Non-actionable or weakly explained comment. | The signal is too vague to preserve without substantial inference. |
| Non-actionable comments and recoverable signals | "This may make the error path harder to debug; consider preserving the original exception context." | Recoverable signal, usually rewrite if wording or grounding is weak. | The concern and possible next step are identifiable even if the comment needs refinement. |
| Wrong location and wrong cause | The comment flags the changed caller, but the actual issue is in the callee contract shown nearby. | Wrong location modifier. | The concern may be valid, but the target is misplaced. |
| Wrong cause and incorrect claim | The comment flags the right line but attributes the issue to caching when the visible cause is input validation. | Wrong causal explanation modifier. | The concern may be located correctly, but the explanation is misleading. |

## Decision Rules for Ambiguous Cases

Ambiguous cases are central to the study because they expose mitigation trade-offs.

A comment that is technically correct but too minor should be labeled low-value rather than incorrect. This distinction matters because a low-value comment may be suppressed for signal-to-noise reasons, while an incorrect comment should not be preserved.

A comment that raises a plausible concern but lacks enough evidence should be labeled context-dependent or unsupported, depending on whether additional context could reasonably resolve the judgment. If the available evidence contradicts the claim, the stronger label is incorrect technical claim. If the available evidence is simply insufficient, the stronger label is context-dependent or unsupported.

A comment that contains a useful concern but is phrased too strongly should not automatically be counted as useless. It should receive the **recoverable signal** and **overconfident phrasing** modifiers when rewriting, softening, or grounding could preserve the signal.

A comment with a valid concern but an invalid fix suggestion should receive labels that preserve both facts: the concern may be useful, while the fix suggestion is invalid. This is important because a mitigation strategy that suppresses the whole comment may lose useful feedback, while a rewrite strategy may preserve the concern and remove the unsafe fix.

A comment that requires specialized evidence but is weakly grounded should not be shown simply because the issue is important. It should usually be escalated or verified with stronger evidence. This rule prevents high-severity labels from overriding grounding requirements.

## Mapping Failure Labels to Mitigation Decisions

The taxonomy does not map labels mechanically to one decision. Instead, labels constrain the plausible decisions. Table \ref{tab:taxonomy-decision-mapping} summarizes this mapping in a compact form. The final executed-study mapping must be reconciled with the human-decision mapping in the methodology and the annotation guideline.

<!-- table: caption="Typical mapping from core failure labels to mitigation decisions." label="tab:taxonomy-decision-mapping" longtable="true" -->
| Core label | Decision to avoid | Usually preferred decision |
| --- | --- | --- |
| Unsupported or hallucinated claim | Showing a confident claim that lacks evidence. | Suppress when there is no useful signal; rewrite with uncertainty or escalate when the concern may be important. |
| Context-dependent or insufficient-context comment | Showing the comment without revision or additional evidence. | Escalate or request more context; rewrite only when uncertainty can be stated clearly. |
| Incorrect technical claim | Showing the false claim as review feedback. | Suppress; rewrite only when a correct related concern can be separated from the false claim. |
| Wrong location or wrong cause | Showing the comment before correcting the target or explanation. | Rewrite if the concern is valid; suppress if it is misleading and not recoverable; escalate if the cause cannot be determined. |
| Irrelevant or out-of-scope comment | Showing it as feedback on the current review. | Suppress in the current review; route as a separate issue only when it is plausibly valid and useful. |
| Non-actionable or weakly explained comment | Showing vague feedback that the author cannot act on. | Rewrite when the concern is useful; suppress when the concern is weak or low-value. |
| Invalid fix suggestion | Showing an unsafe or behavior-changing fix. | Remove or rewrite the fix while preserving the concern when possible; escalate when validation is required. |
| Low-value or redundant comment | Showing ordinary review noise under normal settings. | Suppress or aggregate; show only when low-noise settings or review goals justify it. |

This mapping supports the decision-confusion analysis in the methodology. For example, suppressing a comment with the **recoverable signal** modifier is counted differently from suppressing a comment labeled irrelevant. The former may be recoverable feedback loss, while the latter may be successful noise reduction.

## Link to Future Empirical Evaluation

The taxonomy is designed to support four parts of a future empirical evaluation.

First, it measures the baseline distribution of problematic comments. Second, it supports strategy-by-failure-type comparison: each mitigation strategy can be evaluated by which categories it reduces. Third, it enables preservation analysis by identifying useful comments that are wrongly suppressed, comments that should be rewritten, and context-dependent cases that should be escalated rather than shown or removed. Fourth, it explains the decision-confusion analysis by linking each incorrect strategy decision to a failure label or modifier.

The taxonomy is a literature-derived measurement proposal, not a validated instrument. Its value should be tested by whether independent annotators can apply the labels consistently and whether the labels reveal trade-offs that a single correctness or acceptance score would miss. A future empirical report should document labels that are merged, revised, promoted, or demoted during pilot annotation.

## Recommended Pilot Refinement and Reliability Checks

A future pilot annotation round should test whether the taxonomy is usable by annotators. It should identify overlapping labels, inconsistent interpretations, and missing failure types before a final annotation sample is constructed.

Reliability is assessed on key labels, not only on the final mitigation decision. At minimum, the study reports agreement on problematic-comment presence, core failure label, usefulness, actionability, context quality, and recommended mitigation decision when feasible. Disagreements are treated as evidence about difficult judgment cases rather than only as noise. For example, repeated disagreement between unsupported and context-dependent labels may indicate that the available context is insufficient or that the annotation guideline needs clearer evidence requirements.

Any executed study should report pilot size, annotator background, revised labels, agreement problems, core/modifier changes, and taxonomy changes. Those changes should also be reflected in the annotation guideline and evaluation schema.
