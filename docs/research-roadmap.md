# Research Roadmap

This document records the current research direction for the paper. It should be used as the project compass for future writing, synthesis, annotation, and empirical work.

## Current Paper Identity

The paper should be framed as:

> a planned controlled empirical study of mitigation strategies for problematic LLM-generated code review comments, supported by an operational taxonomy and a trade-off-aware evaluation framework.

The main goal is not to choose one universally best method. The main goal is to understand which mitigation strategies reduce which kinds of problematic comments and what trade-offs they introduce in useful-feedback preservation, review coverage, human escalation, and computational cost.

This framing is stronger for a Q1 journal submission than a framework-only paper, but it will only become submission-ready after the empirical execution is completed: dataset selection, strategy implementation, annotation, agreement reporting, result tables, and findings.

## Working Title

```text
Reducing Problematic LLM-Generated Code Review Comments: An Empirical Study of Mitigation Trade-offs
```

This title foregrounds the intended empirical contribution and the trade-off problem. The taxonomy and framework remain important, but they support the empirical comparison rather than replacing it.

## Current Execution Status

The manuscript is currently a design-stage draft. The following pieces are drafted or partially drafted:

- targeted literature review;
- related-work synthesis;
- initial operational taxonomy;
- trade-off-aware evaluation framework;
- methodology and planned empirical design;
- planned findings placeholders.

The following pieces are still TODO:

- choose the dataset and sampling frame;
- implement or define the mitigation strategies precisely;
- generate or collect strategy outputs;
- create the annotation guideline and evaluation schema;
- run pilot annotation;
- revise taxonomy based on pilot annotation;
- run final annotation;
- compute agreement statistics;
- compute error-reduction, preservation, coverage, escalation, and cost metrics;
- replace planned findings with actual results;
- revise abstract, introduction, discussion, threats, and conclusion in result-oriented language.

## Central Claim

Current evaluations of LLM-generated code review comments are fragmented. They often measure correctness, usefulness, hallucination, context enrichment, acceptance, or evaluator quality separately. However, mitigation strategies should be evaluated by both what they remove and what they lose.

This project is designed to address that gap by comparing representative mitigation strategies on a shared set of review instances and measuring:

- problematic-comment reduction;
- failure-type-specific effects;
- useful-feedback preservation;
- wrongly suppressed useful comments;
- review coverage;
- human escalation;
- computational cost;
- context-quality effects;
- and evaluator validity.

## Contributions

### Contribution 1 — Operational Taxonomy

Develop an operational taxonomy of problematic LLM-generated code review comments. The taxonomy should support annotation and empirical comparison, not only conceptual discussion.

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

### Contribution 2 — Controlled Empirical Comparison

Compare a limited set of representative mitigation strategies on the same review instances.

Initial strategies:

| Strategy | Role |
|---|---|
| Baseline LLM reviewer | Measures the unmitigated problematic-comment rate. |
| Robust prompting | Tests whether generation-time constraints reduce problematic comments. |
| Context-quality gate | Tests whether low-context or inconsistent-context cases should be skipped, downgraded, or escalated. |
| Post-generation verification | Tests whether comments can be checked before display. |
| Hybrid gate plus verifier | Tests whether pre-generation/context control and post-generation verification complement each other. |

Optional strategy if feasible: retrieval-augmented context enrichment.

### Contribution 3 — Trade-Off-Aware Metrics

Evaluate strategies using both error-reduction and preservation/cost metrics.

Required dimensions:

- overall problematic-comment rate;
- rate of each problematic-comment type;
- technical correctness;
- groundedness;
- relevance;
- usefulness;
- actionability;
- useful comments retained;
- useful comments wrongly suppressed;
- review coverage retained;
- rewrite rate;
- human escalation rate;
- computational cost;
- context quality;
- evaluator validity.

### Contribution 4 — Annotation Protocol and Evidence Artifact

Add a structured human annotation layer over the generated comments and mitigation decisions.

The annotation protocol should include:

- clear label definitions;
- a pilot annotation round;
- at least two annotators if feasible;
- inter-annotator agreement reporting;
- conflict resolution rules;
- examples and counterexamples;
- reproducible prompts, settings, and metric scripts.

### Contribution 5 — Empirical Findings

The paper should report a small number of concrete findings after the study is run. The strongest findings will likely concern trade-offs, not simple wins.

Candidate findings to test:

1. Post-generation verification may reduce unsupported comments but suppress some useful weak signals.
2. Context-quality gates may help more with context-dependent failures than with low-value or non-actionable comments.
3. Robust prompting may improve actionability but may not reliably eliminate unsupported claims.
4. Hybrid strategies may improve safety but add cost, escalation, or over-suppression.
5. Useful-but-not-directly-acceptable comments reveal a gray zone missed by binary correct/incorrect evaluation.

## Research Questions

### RQ1

```text
What types of problematic comments occur in LLM-generated code review?
```

Expected output: label distribution and refined operational taxonomy.

### RQ2

```text
Which mitigation strategies reduce which types of problematic comments?
```

Expected output: strategy-by-failure-type comparison.

### RQ3

```text
How do mitigation strategies affect useful-feedback preservation, review coverage, human escalation, and execution cost?
```

Expected output: trade-off matrix and preservation/cost metrics.

### RQ4

```text
Does combining context-quality control with post-generation verification produce a better trade-off than either strategy alone?
```

Expected output: hybrid-strategy analysis, if the hybrid strategy is included.

### RQ5

```text
How does context quality or context inconsistency affect mitigation success?
```

Expected output: context-quality analysis and context-dependent failure patterns.

## Expected Paper Structure

```text
1. Introduction
2. Background and Motivation
3. Related Work
4. Methodology
5. Operational Taxonomy of Problematic Comments
6. Trade-Off-Aware Evaluation Framework
7. Empirical Evaluation Design
8. Findings
9. Discussion
10. Threats to Validity
11. Conclusion
```

## Minimum Viable Study

A realistic minimum version of the paper can include:

```text
one primary dataset
+ one main generation model
+ 4–5 representative mitigation strategies
+ 100–300 annotated generated comments
+ pilot annotation
+ agreement reporting on a substantial subset
+ error-reduction and preservation metrics
+ 2–4 concrete findings about mitigation trade-offs
```

If the sample is smaller, results should be framed as exploratory. If the sample is larger and annotations are strong, the work becomes more competitive for Q1 empirical software engineering venues.

## Data Strategy

Preferred strategy:

```text
Use an existing code review dataset or benchmark
+ select a manageable subset
+ generate comments with a fixed model and prompt
+ apply representative mitigation strategies
+ add structured human annotation
+ report agreement, trade-offs, and cost proxies
```

Selection criteria:

- code diff is available;
- review-relevant context is available or recoverable;
- generated comments can be evaluated for grounding, usefulness, and actionability;
- licensing permits analysis and release of derived artifacts where possible.

## Risk Register

| Risk | Mitigation |
|---|---|
| Paper becomes a generic survey | Keep the empirical comparison as the central study. |
| Paper becomes only a leaderboard | Emphasize failure types and trade-offs, not a single winner. |
| Annotation quality is weak | Use clear guidelines, pilot annotation, multiple annotators, and agreement reporting. |
| No strong insight emerges | Design metrics around trade-offs, not only error rates. |
| Scope becomes too large | Use one dataset, one main model, limited strategies, and a manageable sample size. |
| Reviewers see the taxonomy as subjective | Support it with annotation, agreement analysis, and examples. |
| Cost is ignored | Report model calls, token cost, escalation rate, and review coverage. |
| LLM-as-a-judge is overtrusted | Use it only as support unless validated against human labels. |

## Immediate Repository Tasks

1. Create `method/annotation-guideline.md`.
2. Create `method/evaluation-schema.md`.
3. Decide the dataset and sampling plan.
4. Decide the generation model and prompts.
5. Define the mitigation strategy implementations.
6. Create metric-computation scripts.
7. Replace core `TODO_PUBLISHER_BIBTEX` entries with official publisher BibTeX.
8. Run a small pilot annotation.

## Current Priority

The next work should not be adding more papers. The next work should be making the empirical design executable.

Recommended next step:

```text
Choose the dataset and create the annotation guideline/evaluation schema.
```
