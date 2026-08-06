# Operational Taxonomy of Problematic Comments

The reviewed literature requires labels that distinguish different kinds of problematic LLM-generated code review comments. A binary label such as correct or incorrect is insufficient because a comment may be unsupported, irrelevant, vague, non-actionable, incorrectly localized, or valid but too low-value to justify attention [@p02_tantithamthavorn2026_hallujudge; @p08_liu2025_too_noisy; @p19_nguyen2025_fine_grained_classification; @p35_mcaleese2024_llm_critics; @p57_heumuller2025_relevance_reviews; @p60_ahmed2025_feedback_useful]. It may also contain a recoverable signal while being unsuitable to show directly. This section defines the literature-derived taxonomy for future annotation and mitigation analysis.

The taxonomy supports annotation, comparison across mitigation strategies, and analysis of handling decisions. It is intentionally smaller than the full failure inventory: specialized and context-specific details are represented as modifiers unless they explain the main reason that feedback should not be shown directly.

## Design Principles

The taxonomy separates failure types, quality dimensions, and handling decisions. For example, grounding is a dimension, an unsupported claim is a failure, and withholding the comment is a possible decision. It also retains uncertain cases in which feedback is potentially useful but lacks evidence or requires revision. Applying the same labels across strategies permits paired comparison without assuming that one failure always implies one action. Detailed inclusion rules and counterexamples belong in the accompanying annotation guideline rather than the main argument.

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

The core/modifier split can be revised after reliability testing. Frequent, stable modifiers may become core labels, whereas low-agreement core labels may be merged or demoted. Such changes must be reported with the agreement results.

## Boundary Rules for Common Ambiguities

Some label boundaries are expected to be difficult in pilot annotation. Table \ref{tab:taxonomy-boundary-rules} records the intended rule for the most important ambiguous pairs; the annotation guideline expands these distinctions with examples and counterexamples.

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

The most frequent boundary disagreements and any revised rules should be reported with the annotation results. The supplementary guideline contains worked examples; Table \ref{tab:taxonomy-boundary-rules} retains only the distinctions needed to understand the taxonomy.

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

This mapping also distinguishes successful noise removal from recoverable feedback loss. Withholding an irrelevant comment and withholding a comment marked **recoverable signal** are therefore different outcomes even when the system action is identical.

## Reliability and Empirical Use

The taxonomy can describe baseline failures, compare strategies by failure type, and identify useful feedback that mitigation loses. Pilot annotation should report agreement for the core label, usefulness, actionability, context quality, and handling decision; recurrent disagreements should guide revisions to label boundaries.
