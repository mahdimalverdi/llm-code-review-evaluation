# Revised Research Roadmap

This document records the revised research direction after supervisor feedback. It should be used as the project compass for future writing, synthesis, annotation, and empirical work.

## Why This Roadmap Exists

The initial idea risked being framed as a small empirical comparison of several mitigation strategies for problematic LLM-generated code review comments. That framing is too narrow and may have limited publication value if the main contribution becomes only “method A works better than method B.”

The revised direction is stronger:

> This project should show that current evaluations of LLM-generated code review comments are incomplete, and then propose a trade-off-aware evaluation framework supported by an operational taxonomy and a small but carefully annotated evidence layer.

The comparison of mitigation strategies may still be useful, but it should support the framework. It should not be the main contribution.

## Supervisor Feedback: Main Interpretation

The key feedback can be summarized as follows:

1. Do not position the paper as a comparison of a few methods to find which one is better.
2. Show that existing evaluations are incomplete.
3. Propose a new framework for evaluating trade-offs between error reduction and cost.
4. Provide an operational taxonomy of problematic comments, preferably supported by data.
5. Provide a multi-dimensional evaluation framework that includes error, usefulness, and cost.
6. Add one or more concrete insights, not only a catalog of methods.
7. Avoid relying only on an existing dataset without adding a careful annotation layer.
8. Use a transparent, repeatable annotation protocol and report inter-annotator agreement.
9. Make the analysis deep enough to produce a meaningful insight.

## Revised Paper Identity

The paper should be framed as:

> a focused evidence synthesis and trade-off-aware evaluation framework for LLM-generated code review comments, supported by an operational taxonomy and a small annotated study.

It should not be framed as:

- a generic survey of LLMs for software engineering;
- a benchmark leaderboard;
- a comparison of several mitigation methods;
- a model-performance paper;
- a standalone hallucination detector;
- a RAG/context expansion paper.

## Central Claim

Current evaluations of LLM-generated code review comments are fragmented. They often measure error reduction, hallucination, usefulness, context enrichment, or evaluator quality separately, but they rarely evaluate the trade-offs among:

- error reduction;
- useful-feedback preservation;
- review coverage;
- human effort;
- computational cost;
- context quality;
- and evaluator validity.

This project addresses that gap by proposing an operational taxonomy of problematic comments and a multi-dimensional, trade-off-aware evaluation framework, supported by a small human-annotated study.

## Proposed Title Options

### Option A

```text
Toward Trade-off-Aware Evaluation of LLM-Generated Code Review Comments: A Taxonomy, Framework, and Annotated Study
```

### Option B

```text
Evaluating Problematic LLM-Generated Code Review Comments: An Operational Taxonomy and a Trade-off-Aware Framework
```

### Option C

```text
A Trade-off-Aware Evaluation Framework for LLM-Generated Code Review Comments with an Operational Taxonomy and Human Annotation Protocol
```

Recommended working title: **Option B**.

It is concise, framework-oriented, and does not overemphasize method comparison.

## Revised Contributions

### Contribution 1 — Operational Taxonomy

Develop an operational taxonomy of problematic LLM-generated code review comments.

The taxonomy should include definitions, decision rules, examples, and ambiguous cases. It should not be only a conceptual list.

Candidate categories:

| Category | Meaning |
|---|---|
| Unsupported / hallucinated comment | The comment makes a claim not supported by the available diff or context. |
| Irrelevant comment | The comment is not related to the reviewed change. |
| Incorrect technical claim | The comment is technically wrong. |
| Wrong location / wrong cause | The comment identifies the wrong location or explains the wrong cause. |
| Non-actionable comment | The developer cannot determine what to do next. |
| Low-value nitpick | The comment may be technically valid but is not worth reviewer attention. |
| Invalid fix suggestion | The suggested change does not fix the issue or may introduce a regression. |
| Context-dependent / insufficient-context case | The comment cannot be judged reliably without more context. |
| Useful but not directly acceptable | The comment is not directly applicable but still provides useful insight. |

### Contribution 2 — Multi-Dimensional Evaluation Framework

Develop a framework that evaluates generated review comments across multiple dimensions:

```text
Input/context quality
→ Generated comment quality
→ Problematic comment type
→ Usefulness and actionability
→ Mitigation decision
→ Cost and workflow impact
→ Evaluator validity
```

The framework should make explicit that reducing problematic comments is not enough. A mitigation strategy may reduce one type of error while increasing cost, reducing review coverage, suppressing useful comments, or increasing human burden.

### Contribution 3 — Human Annotation Protocol

Add a new annotation layer over an existing dataset or a generated sample.

The annotation protocol should include:

- clear label definitions;
- a pilot annotation round;
- at least two annotators if possible;
- inter-annotator agreement reporting;
- conflict resolution rules;
- examples and counterexamples for each label;
- a reproducible data and prompt setup.

This annotation layer is important because using an existing dataset without additional structured labeling may be considered weak by reviewers.

### Contribution 4 — Concrete Findings

The paper should report a small number of specific insights. These findings should be more important than a raw method-comparison table.

Candidate findings to investigate:

1. Post-generation verification may reduce unsupported or hallucinated comments, but this improvement can come with higher computational or operational cost.
2. Context-quality gates may be more effective for context-dependent failures than for low-value or non-actionable comments.
3. Reducing problematic comments does not necessarily improve review utility if useful comments are also suppressed or review coverage decreases.
4. Useful but non-directly-acceptable comments form a gray zone that is missed by binary accepted/rejected or correct/incorrect evaluation.

## Revised Research Questions

### RQ1

```text
What types of problematic comments occur in LLM-generated code review, and how can they be operationally annotated?
```

Expected output: operational taxonomy and annotation guideline.

### RQ2

```text
Which evaluation dimensions are needed to assess problematic comments beyond technical correctness?
```

Expected output: multi-dimensional evaluation matrix.

### RQ3

```text
How do common mitigation strategies trade off error reduction against useful-feedback preservation, review coverage, human effort, and computational cost?
```

Expected output: trade-off framework and measurable trade-off dimensions.

### RQ4

```text
How does context quality affect the occurrence, detection, and mitigation of problematic review comments?
```

Expected output: context-quality layer and context-failure analysis.

### RQ5

```text
What framework can guide trade-off-aware evaluation of LLM-generated code review comments?
```

Expected output: final framework.

## Expected Paper Structure

```text
1. Introduction
2. Background and Motivation
3. Related Work
   3.1 LLM-based code review evaluation
   3.2 Hallucination, grounding, and context
   3.3 Human-centered review usefulness
   3.4 LLM-as-a-judge and evaluator validity
4. Methodology
   4.1 Focused evidence synthesis
   4.2 Paper selection and coding
   4.3 Taxonomy construction
   4.4 Annotation protocol
   4.5 Evaluation dimensions and metrics
5. Operational Taxonomy of Problematic Comments
6. Trade-off-Aware Evaluation Framework
7. Annotated Study / Illustrative Evaluation
8. Findings
9. Discussion
10. Threats to Validity
11. Conclusion
```

If the empirical part remains small, Section 7 should be framed as an **illustrative annotation study**, not as a large-scale empirical benchmark.

## Minimum Viable Study

A realistic minimum version of the paper can include:

```text
50-paper evidence base
+ operational taxonomy
+ annotation guideline
+ 100–200 annotated generated review comments
+ inter-annotator agreement report
+ trade-off-aware framework
+ 2–3 concrete findings
```

The empirical component should support the framework. It should not become the main identity of the paper.

## Data Strategy

Preferred strategy:

```text
Use an existing code review dataset
+ generate or collect review comments for a controlled subset
+ add our own annotation layer
+ report agreement and disagreement patterns
```

This balances feasibility and contribution strength.

### Option A — Safer and Smaller

Use an existing dataset and add our own annotation layer.

Benefits:

- feasible;
- lower execution cost;
- enough for a framework-oriented paper;
- easier to control scope.

Risk:

- empirical contribution is smaller.

### Option B — Stronger but More Expensive

Generate new review comments using a fixed LLM and prompts, then annotate them.

Benefits:

- stronger empirical contribution;
- more control over prompts and mitigation strategies.

Risk:

- higher cost;
- more design choices;
- higher annotation burden.

### Recommended Path

Use **Option A plus a small controlled generation layer**.

That means:

1. Start from an existing dataset.
2. Select a manageable subset.
3. Generate comments for that subset using a fixed model and fixed prompt.
4. Apply the annotation guideline.
5. Report agreement, label distribution, and trade-off observations.

## Annotation Plan

Create:

```text
method/annotation-guideline.md
method/evaluation-schema.md
```

The annotation schema should include fields such as:

```text
sample_id
diff
context
generated_comment
strategy
problematic_type
technical_correctness
groundedness
usefulness
actionability
severity_or_value
decision
context_quality
needs_human_escalation
annotator_1
annotator_2
final_label
disagreement_reason
```

Decision labels:

| Decision | Meaning |
|---|---|
| Show | The comment is useful enough to show. |
| Suppress | The comment should not be shown. |
| Rewrite | The comment contains a useful signal but needs rewriting. |
| Escalate | The comment may matter, but requires human or additional-context review. |

## Evaluation Dimensions

The evaluation should not be limited to error rate.

Required dimensions:

- problematic-comment rate;
- rate of each problematic-comment type;
- technical correctness;
- groundedness;
- usefulness;
- actionability;
- useful-feedback preservation;
- wrongly suppressed useful comments;
- review coverage;
- human escalation rate;
- computational cost;
- human annotation or verification cost;
- context quality;
- evaluator validity, if LLM-as-a-judge is used.

## Risk Register

| Risk | Mitigation |
|---|---|
| Paper becomes a generic survey | Keep the focus on evaluation trade-offs and problematic comments. |
| Paper becomes only a method comparison | Make taxonomy and framework the main contributions. |
| Annotation quality is weak | Use clear guidelines, pilot annotation, multiple annotators, and agreement reporting. |
| No strong insight emerges | Design metrics around trade-offs, not only error rates. |
| Scope becomes too large | Use one dataset, one primary model, limited strategies, and a manageable sample size. |
| Reviewers see the framework as subjective | Support it with annotated samples and agreement analysis. |
| Cost is ignored | Report computational cost, human effort, escalation rate, and review coverage. |
| LLM-as-a-judge is overtrusted | Add evaluator-validity checks or use it only as support, not ground truth. |

## Immediate Repository Tasks

1. Create `synthesis/core-claim.md`.
2. Update RQs in `README.md`, `synthesis/research-gap.md`, and `drafts/methodology.md`.
3. Create `method/annotation-guideline.md`.
4. Create `method/evaluation-schema.md`.
5. Create `synthesis/final-framework.md`.
6. Create `drafts/introduction.md`.
7. Revise `drafts/related-work.md` to match this revised framing.
8. Decide the dataset and sampling plan.
9. Replace core `TODO_PUBLISHER_BIBTEX` entries with official publisher BibTeX.

## Current Priority

The next work should not be adding more papers. The next work should be consolidating the project into a publishable paper direction.

Recommended next step:

```text
Create synthesis/core-claim.md and update the research questions across canonical files.
```
