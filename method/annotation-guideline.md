# Annotation Guideline

> [!NOTE]
> This guideline operationalizes the taxonomy of problematic LLM-generated code review comments. It is designed for a small annotated evidence layer, not for a large-scale benchmark. The goal is to test whether the taxonomy and trade-off-aware evaluation framework can be applied consistently.

## 1. Annotation Goal

The goal is to label LLM-generated code review comments along several dimensions that are often collapsed into a single quality score.

The annotation should help answer:

- What type of problem, if any, appears in the generated comment?
- Is the comment technically correct?
- Is the comment grounded in the available diff or context?
- Is the comment useful to the developer or reviewer?
- Is the comment actionable?
- Should the comment be shown, suppressed, rewritten, or escalated?
- Does the comment require more context to judge reliably?
- What kinds of disagreements occur between annotators?

## 2. Unit of Annotation

The unit of annotation is one generated review comment for one code change.

Each sample should include, when available:

- the code diff or changed hunk;
- surrounding context, if provided;
- pull-request or issue metadata, if provided;
- the generated review comment;
- the generation strategy or model, if known;
- any post-generation verification result, if available.

If a generated output contains multiple independent concerns, annotators should either:

1. annotate the most important concern and mark `contains_multiple_concerns = true`; or
2. split the output into separate comment-level units before annotation.

The preferred approach for the first study is to keep one generated review comment as one unit and add a flag for multiple concerns.

## 3. Required Annotation Fields

Each annotator should fill at least these fields:

| Field | Type | Purpose |
|---|---|---|
| `technical_correctness` | categorical | Is the comment technically correct? |
| `groundedness` | categorical | Is the comment supported by the available context? |
| `usefulness` | categorical | Does the comment provide value to the developer/reviewer? |
| `actionability` | categorical | Does the comment make a next step clear? |
| `primary_problematic_type` | categorical | Main failure type, if any. |
| `secondary_problematic_types` | list | Additional failure types, if needed. |
| `decision` | categorical | Show, suppress, rewrite, or escalate. |
| `context_quality` | categorical | Is the available context sufficient and usable? |
| `confidence` | ordinal | Annotator confidence. |
| `rationale` | free text | Short explanation of the label. |

## 4. Label Scales

### 4.1 Technical Correctness

| Label | Definition |
|---|---|
| `correct` | The technical claim appears correct given the available evidence. |
| `incorrect` | The technical claim is wrong or contradicts the code/context. |
| `partially_correct` | The comment contains a valid concern but also includes an incorrect or overstated claim. |
| `not_judgeable` | The available context is insufficient to judge technical correctness. |
| `not_applicable` | The comment does not make a technical claim. |

Decision rule:

- Use `not_judgeable` when the comment may be correct but cannot be verified from the available context.
- Use `partially_correct` when part of the comment is valid but the recommendation, explanation, or severity is wrong.

### 4.2 Groundedness

| Label | Definition |
|---|---|
| `grounded` | The comment is supported by the diff or provided context. |
| `weakly_grounded` | The comment is plausibly related to the context but lacks enough evidence. |
| `ungrounded` | The comment makes a claim not supported by the available context. |
| `contradicted` | The comment is contradicted by the available context. |
| `not_judgeable` | The required context is missing. |

Decision rule:

- A comment can be technically plausible but still `ungrounded`.
- A comment can be useful but still `weakly_grounded`; this should usually lead to `rewrite` or `escalate`, not automatic `show`.

### 4.3 Usefulness

| Label | Definition |
|---|---|
| `useful` | The comment provides clear value for correctness, maintainability, readability, security, performance, or understanding. |
| `somewhat_useful` | The comment contains a useful signal but is incomplete, weakly grounded, or requires rewriting. |
| `not_useful` | The comment does not provide meaningful value for the review. |
| `harmful` | The comment is likely to mislead, waste reviewer effort, or encourage a bad change. |
| `not_judgeable` | The available context is insufficient to judge usefulness. |

Decision rule:

- Do not equate direct acceptability with usefulness.
- A comment can be `somewhat_useful` even if it should not be shown as-is.
- Use `harmful` for comments that are wrong, misleading, or likely to cause a regression.

### 4.4 Actionability

| Label | Definition |
|---|---|
| `actionable` | The developer can infer a concrete next step. |
| `partially_actionable` | The comment points to a concern but needs clarification or rewriting. |
| `not_actionable` | The comment is too vague or abstract to guide action. |
| `not_applicable` | The comment is explanatory or informational and does not require action. |

Decision rule:

- A design-level comment can be actionable if it clearly explains what decision or investigation is needed.
- Do not mark a comment as `not_actionable` only because it lacks a patch; a concrete recommendation can be enough.

### 4.5 Context Quality

| Label | Definition |
|---|---|
| `sufficient` | The provided context is enough to judge the comment. |
| `partially_sufficient` | The context supports a partial judgment but leaves important uncertainty. |
| `insufficient` | The context is not enough to judge the comment reliably. |
| `misleading_or_inconsistent` | The context appears stale, contradictory, or inconsistent. |

Decision rule:

- Use `insufficient` when the right decision depends on project-level, cross-file, dependency, or runtime context that is not provided.
- Use `misleading_or_inconsistent` when the comment depends on documentation, metadata, or tool output that conflicts with the code/context.

### 4.6 Decision Label

| Label | Definition |
|---|---|
| `show` | The comment is useful enough and safe enough to show as-is. |
| `suppress` | The comment should not be shown. |
| `rewrite` | The comment contains a useful signal but should be rewritten before showing. |
| `escalate` | The comment may matter, but a human or additional context is needed before deciding. |

Decision rule:

- Use `show` only when the comment is sufficiently grounded, useful, and not misleading.
- Use `suppress` for clearly irrelevant, ungrounded, harmful, or low-value comments.
- Use `rewrite` for comments with a useful signal but poor wording, weak actionability, or incomplete rationale.
- Use `escalate` when the possible issue is important but cannot be judged reliably from the available context.

### 4.7 Annotator Confidence

| Label | Definition |
|---|---|
| `high` | The annotator is confident in the label. |
| `medium` | The annotator is reasonably confident but recognizes some ambiguity. |
| `low` | The label is uncertain and should be reviewed during adjudication. |

## 5. Problematic Comment Types

Use one primary problematic type. Add secondary types only when they materially affect the decision.

### 5.1 No Problem

| Label | Definition |
|---|---|
| `none` | No clear problem is detected. The comment may still be imperfect, but it is not problematic under this taxonomy. |

Use `none` only when the comment is at least reasonably grounded, useful, and not misleading.

### 5.2 Unsupported or Hallucinated Comment

Definition: The comment makes a claim not supported by the available diff or context.

Use when:

- the comment invents a behavior not visible in the context;
- the comment assumes an API, dependency, or side effect not shown;
- the comment reports a problem without evidence.

Do not use when:

- the comment is correct but low-value;
- the context is missing and the claim cannot be judged. In that case, use `context_dependent` unless the claim is clearly unsupported.

Likely decision: `suppress` or `escalate`.

### 5.3 Irrelevant Comment

Definition: The comment is unrelated to the reviewed change.

Use when:

- the comment discusses code not affected by the change;
- the comment ignores the actual diff;
- the comment gives generic advice unrelated to the PR.

Likely decision: `suppress`.

### 5.4 Incorrect Technical Claim

Definition: The comment is technically wrong.

Use when:

- the comment misunderstands the code;
- the comment makes a wrong claim about behavior, API, type, or language semantics;
- the proposed reasoning contradicts the code.

Likely decision: `suppress`, unless the comment contains a separable useful signal that should be rewritten.

### 5.5 Wrong Location or Wrong Cause

Definition: The comment points to the wrong line, component, or cause of a real or possible issue.

Use when:

- the issue may exist but not where the comment says;
- the comment identifies the symptom but explains the wrong cause;
- the suggested fix targets the wrong part of the code.

Likely decision: `rewrite` or `escalate`.

### 5.6 Vague or Generic Comment

Definition: The comment is too broad or generic to support a useful review decision.

Use when:

- the comment says something like “improve error handling” without explaining where or why;
- the comment uses generic best-practice language without tying it to the diff;
- the comment lacks enough specificity to be checked.

Likely decision: `rewrite` or `suppress`.

### 5.7 Non-Actionable Comment

Definition: The comment does not give the developer a clear next step.

Use when:

- the concern is unclear;
- the recommendation is missing;
- the comment explains a problem but not what should be investigated or changed.

Do not use when:

- the comment is a high-level design concern but clearly states what decision needs attention.

Likely decision: `rewrite` or `escalate`.

### 5.8 Low-Value Nitpick

Definition: The comment may be technically valid but is not worth reviewer or developer attention in the given context.

Use when:

- the comment focuses on a minor style issue with little practical value;
- the comment creates review noise;
- the comment has poor value-to-time ratio.

Likely decision: `suppress` or lower priority.

### 5.9 Redundant Comment

Definition: The comment repeats information already obvious from the diff or already covered by another comment.

Use when:

- the comment states what the code already clearly shows;
- the same concern is already present in another comment;
- the comment does not add new review value.

Likely decision: `suppress` or merge.

### 5.10 Invalid Fix Suggestion

Definition: The suggested fix does not solve the issue, introduces a likely regression, or is incompatible with the code context.

Use when:

- the comment identifies a real concern but proposes a bad fix;
- the fix changes semantics incorrectly;
- the fix is not implementable in the project context.

Likely decision: `rewrite` or `suppress`.

### 5.11 Context-Dependent / Insufficient-Context Case

Definition: The comment cannot be judged reliably from the available context.

Use when:

- correctness depends on cross-file behavior, project conventions, dependency versions, runtime behavior, or product requirements;
- the available diff is too narrow;
- the comment may be important but needs more evidence.

Likely decision: `escalate`.

### 5.12 Useful but Not Directly Acceptable

Definition: The comment is not ready to apply as-is, but it provides useful insight.

Use when:

- the comment points to a real area worth checking but needs refinement;
- the comment is directionally useful but too broad;
- the comment is a useful review prompt rather than a directly actionable comment.

Likely decision: `rewrite` or `escalate`.

### 5.13 Security False Alarm

Definition: The comment reports a vulnerability or security risk that is unsupported, overstated, or unlikely in the given context.

Use when:

- the comment labels code as vulnerable without sufficient evidence;
- severity is exaggerated;
- the reported vulnerability does not match the code path.

Likely decision: `suppress` or `escalate`, depending on severity.

### 5.14 Unsupported Efficiency Claim

Definition: The comment makes a performance or efficiency claim without workload, benchmark, or code-path evidence.

Use when:

- the comment recommends optimization without evidence;
- the comment claims a performance issue that is not supported by the context;
- the suggested optimization may harm readability or maintainability.

Likely decision: `rewrite`, `suppress`, or `escalate`.

## 6. Labeling Order

Annotators should label in this order:

1. Read the diff and available context.
2. Read the generated comment.
3. Identify the main claim made by the comment.
4. Judge technical correctness.
5. Judge groundedness.
6. Judge usefulness.
7. Judge actionability.
8. Assign the primary problematic type, if any.
9. Assign secondary problematic types, if needed.
10. Assign context quality.
11. Assign the final decision: `show`, `suppress`, `rewrite`, or `escalate`.
12. Write a short rationale.
13. Mark confidence.

## 7. Handling Ambiguous Cases

### Case A — Correct but Low Value

If the comment is technically correct but adds little value, mark:

- `technical_correctness = correct`
- `groundedness = grounded`
- `usefulness = not_useful` or `somewhat_useful`
- `primary_problematic_type = low_value_nitpick` or `redundant_comment`
- `decision = suppress` or `rewrite`

### Case B — Useful but Weakly Grounded

If the comment may be useful but is not sufficiently supported, mark:

- `groundedness = weakly_grounded`
- `usefulness = somewhat_useful` or `useful`
- `primary_problematic_type = useful_but_not_directly_acceptable` or `context_dependent`
- `decision = rewrite` or `escalate`

### Case C — Not Judgeable Because of Missing Context

If the comment cannot be judged without more context, mark:

- `technical_correctness = not_judgeable`
- `groundedness = not_judgeable`
- `context_quality = insufficient`
- `primary_problematic_type = context_dependent`
- `decision = escalate`

### Case D — Correct Issue, Bad Fix

If the issue is real but the suggested fix is wrong, mark:

- `technical_correctness = partially_correct`
- `primary_problematic_type = invalid_fix_suggestion`
- `decision = rewrite` or `escalate`

### Case E — Security or Performance Claim

If the comment makes a security or performance claim, require stronger evidence. If evidence is missing, prefer:

- `groundedness = weakly_grounded` or `ungrounded`
- `primary_problematic_type = security_false_alarm` or `unsupported_efficiency_claim`
- `decision = escalate` or `suppress`

## 8. Pilot Annotation Procedure

Before full annotation:

1. Select a pilot subset of 20 samples.
2. Each annotator labels the samples independently.
3. Compare label distributions and disagreements.
4. Discuss disagreements and ambiguous cases.
5. Revise label definitions and examples.
6. Re-label the pilot subset if needed.
7. Freeze the guideline before full annotation.

## 9. Inter-Annotator Agreement

Report agreement where feasible.

Recommended metrics:

| Label Group | Suggested Metric |
|---|---|
| Primary problematic type | Cohen’s kappa or Krippendorff’s alpha |
| Technical correctness | Cohen’s kappa |
| Groundedness | Cohen’s kappa |
| Usefulness | Cohen’s kappa plus percentage agreement |
| Actionability | Cohen’s kappa plus percentage agreement |
| Final decision | Cohen’s kappa |

If sample size is small, report agreement descriptively and avoid overclaiming reliability.

## 10. Conflict Resolution

After independent annotation:

1. Identify samples where annotators disagree.
2. Record the disagreement type.
3. Discuss the disagreement using the guideline.
4. Assign a final resolved label.
5. Preserve the original annotator labels and final label in the dataset.

Common disagreement reasons:

- insufficient context;
- different interpretation of usefulness;
- different threshold for low-value nitpick;
- uncertainty about technical correctness;
- ambiguity between `rewrite` and `escalate`;
- multiple concerns in one comment.

## 11. Reporting Requirements

The paper should report:

- number of samples;
- source of samples;
- generation model and prompt, if applicable;
- number of annotators;
- annotator background;
- pilot procedure;
- final label set;
- agreement metrics;
- conflict resolution process;
- label distribution;
- examples of each major label;
- main disagreement patterns.

## 12. Non-Goals

This annotation layer is not intended to:

- prove that one LLM is better than another;
- create a large public benchmark by itself;
- replace expert security or performance review;
- provide universal labels for all code review settings;
- or make broad claims from a small sample.

Its purpose is to support the operational taxonomy and trade-off-aware framework.
