# Evaluation Schema

> [!NOTE]
> This schema defines the columns and allowed values for the annotated evidence layer. It should be used with `method/annotation-guideline.md`.

## 1. Purpose

The schema is designed to support a small annotated study of LLM-generated code review comments. It records both comment-level quality labels and trade-off-relevant information.

The schema supports four goals:

1. applying the operational taxonomy;
2. measuring annotation agreement;
3. analyzing useful-feedback preservation;
4. connecting mitigation decisions to cost, context quality, and evaluator validity.

## 2. Recommended File Layout

Recommended data files:

```text
data/annotation_samples.csv
data/annotations_raw.csv
data/annotations_resolved.csv
data/agreement_report.md
data/label_distribution.md
```

Suggested meaning:

| File | Purpose |
|---|---|
| `annotation_samples.csv` | Sample metadata and generated comments before annotation. |
| `annotations_raw.csv` | Independent annotator labels. One row per annotator per sample. |
| `annotations_resolved.csv` | Final adjudicated labels. One row per sample. |
| `agreement_report.md` | Agreement metrics and disagreement summary. |
| `label_distribution.md` | Label distribution and main observations. |

## 3. Sample Table Schema

`annotation_samples.csv` should contain one row per generated comment.

| Column | Type | Required | Description |
|---|---|---|---|
| `sample_id` | string | yes | Stable unique sample ID. |
| `source_dataset` | string | yes | Dataset or source of the code change. |
| `source_project` | string | no | Repository or project name, if available. |
| `source_url` | string | no | Link to PR, commit, benchmark item, or artifact. |
| `language` | string | no | Programming language. |
| `diff` | text | yes | Code diff or changed hunk shown to annotators. |
| `context` | text | no | Additional context, such as file context, PR description, issue text, retrieved examples, or static-analysis output. |
| `pr_title` | string | no | Pull-request title, if available. |
| `pr_description` | text | no | Pull-request description, if available. |
| `generated_comment` | text | yes | Generated review comment being annotated. |
| `generator_model` | string | no | Model used to generate the comment. |
| `generation_prompt_id` | string | no | Prompt or strategy ID. |
| `mitigation_strategy` | string | no | Strategy used before annotation, if any. |
| `post_verification_result` | string | no | Result of any post-generation check, if available. |
| `contains_multiple_concerns` | boolean | no | Whether the generated comment contains more than one independent concern. |
| `notes_for_annotators` | text | no | Non-leading information needed by annotators. |

## 4. Raw Annotation Schema

`annotations_raw.csv` should contain one row per annotator per sample.

| Column | Type | Required | Allowed Values / Notes |
|---|---|---|---|
| `sample_id` | string | yes | Must match `annotation_samples.csv`. |
| `annotator_id` | string | yes | Stable anonymized annotator ID, e.g., `A1`, `A2`. |
| `annotation_round` | string | yes | `pilot`, `main`, or `relabel`. |
| `technical_correctness` | enum | yes | `correct`, `incorrect`, `partially_correct`, `not_judgeable`, `not_applicable` |
| `groundedness` | enum | yes | `grounded`, `weakly_grounded`, `ungrounded`, `contradicted`, `not_judgeable` |
| `usefulness` | enum | yes | `useful`, `somewhat_useful`, `not_useful`, `harmful`, `not_judgeable` |
| `actionability` | enum | yes | `actionable`, `partially_actionable`, `not_actionable`, `not_applicable` |
| `context_quality` | enum | yes | `sufficient`, `partially_sufficient`, `insufficient`, `misleading_or_inconsistent` |
| `primary_problematic_type` | enum | yes | See Section 6. |
| `secondary_problematic_types` | list[string] | no | Semicolon-separated list of additional labels. |
| `decision` | enum | yes | `show`, `suppress`, `rewrite`, `escalate` |
| `severity_or_value` | enum | no | `high`, `medium`, `low`, `not_applicable` |
| `needs_human_escalation` | boolean | yes | `true` or `false` |
| `confidence` | enum | yes | `high`, `medium`, `low` |
| `rationale` | text | yes | Short explanation of the labels. |
| `evidence_span` | text | no | Diff/context span that supports the label, if identifiable. |
| `missing_context` | text | no | Context needed to decide, if any. |
| `annotation_time_seconds` | integer | no | Optional estimate of human effort. |

## 5. Resolved Annotation Schema

`annotations_resolved.csv` should contain one row per sample after adjudication.

| Column | Type | Required | Description |
|---|---|---|---|
| `sample_id` | string | yes | Stable unique sample ID. |
| `final_technical_correctness` | enum | yes | Resolved correctness label. |
| `final_groundedness` | enum | yes | Resolved groundedness label. |
| `final_usefulness` | enum | yes | Resolved usefulness label. |
| `final_actionability` | enum | yes | Resolved actionability label. |
| `final_context_quality` | enum | yes | Resolved context-quality label. |
| `final_primary_problematic_type` | enum | yes | Resolved primary failure type. |
| `final_secondary_problematic_types` | list[string] | no | Resolved secondary labels. |
| `final_decision` | enum | yes | `show`, `suppress`, `rewrite`, or `escalate`. |
| `final_severity_or_value` | enum | no | Resolved severity/value label. |
| `final_needs_human_escalation` | boolean | yes | Resolved escalation flag. |
| `disagreement_present` | boolean | yes | Whether annotators disagreed on any major label. |
| `disagreement_fields` | list[string] | no | Fields with disagreement. |
| `disagreement_reason` | text | no | Short summary of why disagreement occurred. |
| `resolution_method` | enum | yes | `discussion`, `adjudicator`, `majority_vote`, `single_annotator`, `not_resolved` |
| `final_notes` | text | no | Notes for later analysis. |

## 6. Allowed Problematic Types

Use these values for `primary_problematic_type` and `secondary_problematic_types`.

| Label | Meaning |
|---|---|
| `none` | No clear problem under the taxonomy. |
| `unsupported_or_hallucinated` | Claim is not supported by the available diff/context. |
| `irrelevant` | Comment is unrelated to the reviewed change. |
| `incorrect_technical_claim` | Comment makes a wrong technical claim. |
| `wrong_location_or_cause` | Comment points to the wrong line, component, or cause. |
| `vague_or_generic` | Comment is too broad or generic to be useful. |
| `non_actionable` | Comment does not provide a clear next step. |
| `low_value_nitpick` | Comment is technically valid but low value. |
| `redundant` | Comment repeats obvious or already-covered information. |
| `invalid_fix_suggestion` | Suggested fix is wrong, unsafe, or not implementable. |
| `context_dependent` | More context is needed to judge the comment. |
| `useful_but_not_directly_acceptable` | Comment has useful signal but should not be shown as-is. |
| `security_false_alarm` | Security concern is unsupported, overstated, or wrong. |
| `unsupported_efficiency_claim` | Performance claim lacks workload or benchmark evidence. |
| `other` | Use only with an explanation in `rationale`. |

## 7. Derived Metrics

These metrics can be computed from the raw and resolved annotation files.

### 7.1 Quality and Failure Metrics

| Metric | Definition |
|---|---|
| `problematic_comment_rate` | Fraction of samples where `final_primary_problematic_type != none`. |
| `unsupported_comment_rate` | Fraction labeled `unsupported_or_hallucinated`. |
| `incorrect_comment_rate` | Fraction with `final_technical_correctness = incorrect`. |
| `low_value_rate` | Fraction labeled `low_value_nitpick` or `redundant`. |
| `context_dependent_rate` | Fraction labeled `context_dependent` or `final_context_quality != sufficient`. |
| `useful_comment_rate` | Fraction with `final_usefulness = useful` or `somewhat_useful`. |
| `harmful_comment_rate` | Fraction with `final_usefulness = harmful`. |

### 7.2 Decision Metrics

| Metric | Definition |
|---|---|
| `show_rate` | Fraction with `final_decision = show`. |
| `suppress_rate` | Fraction with `final_decision = suppress`. |
| `rewrite_rate` | Fraction with `final_decision = rewrite`. |
| `escalation_rate` | Fraction with `final_decision = escalate`. |
| `human_escalation_rate` | Fraction with `final_needs_human_escalation = true`. |

### 7.3 Useful-Feedback Preservation Metrics

| Metric | Definition |
|---|---|
| `useful_suppressed_rate` | Fraction of useful/somewhat-useful comments with `final_decision = suppress`. |
| `useful_rewrite_or_escalate_rate` | Fraction of useful/somewhat-useful comments with `final_decision = rewrite` or `escalate`. |
| `harmful_shown_rate` | Fraction of harmful comments with `final_decision = show`. |
| `weakly_grounded_useful_rate` | Fraction of useful/somewhat-useful comments with `final_groundedness = weakly_grounded`. |
| `context_dependent_useful_rate` | Fraction of context-dependent comments with `final_usefulness = useful` or `somewhat_useful`. |

### 7.4 Agreement Metrics

| Metric | Definition |
|---|---|
| `kappa_primary_problematic_type` | Cohen’s kappa for primary problematic type. |
| `kappa_technical_correctness` | Cohen’s kappa for technical correctness. |
| `kappa_groundedness` | Cohen’s kappa for groundedness. |
| `kappa_usefulness` | Cohen’s kappa for usefulness. |
| `kappa_actionability` | Cohen’s kappa for actionability. |
| `kappa_decision` | Cohen’s kappa for final decision. |
| `percent_agreement_*` | Percent agreement for each major label. |

### 7.5 Cost and Effort Metrics

| Metric | Definition |
|---|---|
| `mean_annotation_time_seconds` | Average annotation time, if recorded. |
| `estimated_model_calls` | Number of model calls per sample, if generation or verification is evaluated. |
| `estimated_token_cost` | Estimated prompt/completion tokens per sample, if available. |
| `human_review_burden` | Escalation rate or annotation time used as a proxy for human effort. |

## 8. Trade-off Analysis Examples

### Example 1 — Strict Suppression

If a rule suppresses all ungrounded comments:

- expected benefit: lower unsupported-comment rate;
- possible risk: useful but weakly grounded comments may be lost;
- relevant metric: `useful_suppressed_rate`.

### Example 2 — Rewrite Instead of Suppress

If weakly grounded but useful comments are rewritten:

- expected benefit: useful signal is preserved;
- possible risk: rewrite may introduce new errors;
- relevant metric: `useful_rewrite_or_escalate_rate`.

### Example 3 — Human Escalation

If context-dependent comments are escalated:

- expected benefit: fewer unsafe automated decisions;
- possible risk: higher human burden;
- relevant metric: `human_escalation_rate` and `context_dependent_useful_rate`.

## 9. Minimal CSV Header

A minimal raw annotation CSV can start with:

```csv
sample_id,annotator_id,annotation_round,technical_correctness,groundedness,usefulness,actionability,context_quality,primary_problematic_type,secondary_problematic_types,decision,severity_or_value,needs_human_escalation,confidence,rationale,evidence_span,missing_context,annotation_time_seconds
```

A minimal resolved CSV can start with:

```csv
sample_id,final_technical_correctness,final_groundedness,final_usefulness,final_actionability,final_context_quality,final_primary_problematic_type,final_secondary_problematic_types,final_decision,final_severity_or_value,final_needs_human_escalation,disagreement_present,disagreement_fields,disagreement_reason,resolution_method,final_notes
```

## 10. Reporting Checklist

The final paper should report:

- number of samples;
- sample source;
- generation model and prompt, if applicable;
- number and background of annotators;
- annotation rounds;
- agreement metrics;
- label distribution;
- decision distribution;
- examples of major problematic types;
- disagreement patterns;
- useful-feedback preservation metrics;
- cost or effort proxies;
- limitations of the sample and labels.
