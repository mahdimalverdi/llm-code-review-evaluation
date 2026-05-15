# Core Claim

> [!NOTE]
> This file is the compact research-positioning anchor for the project. It should be checked before writing the introduction, methodology, framework, or empirical sections. Its purpose is to prevent the paper from drifting back into a small method-comparison study.

## One-Sentence Claim

Current evaluations of LLM-generated code review comments are fragmented because they often measure error reduction, hallucination, usefulness, context enrichment, or evaluator quality separately, but rarely evaluate the trade-offs among error reduction, useful-feedback preservation, review coverage, human effort, computational cost, context quality, and evaluator validity.

## Revised Paper Identity

This paper should be positioned as:

> a focused evidence synthesis and trade-off-aware evaluation framework for LLM-generated code review comments, supported by an operational taxonomy and a small annotated evidence layer.

It should not be positioned as:

- a comparison of several mitigation methods;
- a benchmark leaderboard;
- a model-performance paper;
- a standalone hallucination detector;
- a RAG/context expansion paper;
- a generic survey of LLMs for software engineering.

## Why the Previous Framing Was Risky

A framing such as “compare several strategies for reducing problematic comments and identify the best one” is too narrow. It risks becoming a small empirical comparison where the contribution depends on which strategy wins.

That framing is weak because:

- the result may be dataset- or prompt-specific;
- the comparison may not generalize across review settings;
- error reduction alone does not capture review usefulness;
- a strategy can reduce bad comments while also suppressing useful feedback;
- computational cost, human effort, and workflow impact may be hidden;
- LLM-as-a-judge results may introduce evaluator bias;
- and the paper would compete with larger benchmark or system papers.

The stronger framing is to show that current evaluation practice is incomplete, then propose a framework for evaluating the trade-offs.

## Core Gap

Existing work has studied several important pieces of the problem:

- lexical and semantic evaluation metrics;
- hallucination and grounding;
- PR-level and project-aware benchmarks;
- context enrichment and retrieval;
- production deployment signals;
- data curation and reference quality;
- human-centered usefulness;
- LLM-as-a-judge validity;
- secure review and static-analysis-guided review.

However, these pieces remain fragmented. The literature does not yet provide a unified evaluation framework that connects:

```text
problematic comment type
+ context quality
+ generated comment quality
+ usefulness and actionability
+ useful-feedback preservation
+ review coverage
+ human and computational cost
+ evaluator validity
+ mitigation decision
```

## Central Argument

Evaluation should not only ask:

```text
Is this generated review comment good?
```

It should also ask:

```text
What kind of failure occurred?
What evidence supports the judgment?
Was the comment grounded in the available context?
Was the comment useful even if not directly acceptable?
Would filtering it remove useful feedback?
What review coverage is lost or preserved?
What human or computational cost is introduced?
How reliable is the evaluator or judge used to make this decision?
Should the comment be shown, suppressed, rewritten, or escalated?
```

This shifts the paper from a method-comparison study to a framework-oriented evaluation study.

## Contribution Statement

This paper makes four intended contributions.

### C1 — Operational Taxonomy

It develops an operational taxonomy of problematic LLM-generated code review comments.

The taxonomy should include:

- definitions;
- decision rules;
- positive and negative examples;
- ambiguous cases;
- and links to evaluation dimensions.

The taxonomy must be usable for annotation, not merely conceptual.

### C2 — Multi-Dimensional Evaluation Framework

It proposes a framework for evaluating generated review comments across multiple dimensions:

```text
Input/context quality
→ Generated comment quality
→ Problematic comment type
→ Usefulness and actionability
→ Mitigation decision
→ Cost and workflow impact
→ Evaluator validity
```

The framework should make explicit that reducing problematic comments is not enough if useful feedback, review coverage, or human workflow value is lost.

### C3 — Annotation Protocol and Evidence Layer

It adds a structured annotation protocol and a small annotated evidence layer.

This layer should include:

- transparent label definitions;
- a pilot annotation round;
- at least two annotators if feasible;
- inter-annotator agreement reporting;
- conflict resolution rules;
- and a reproducible sampling and generation setup.

The annotation layer gives empirical support to the taxonomy and reduces the risk that the framework appears purely subjective.

### C4 — Concrete Trade-off Findings

It reports a small number of concrete insights about trade-offs, rather than only listing methods.

Candidate findings to investigate:

1. Post-generation verification may reduce unsupported or hallucinated comments, but can increase computational or operational cost.
2. Context-quality gates may help with context-dependent failures, but may not solve low-value or non-actionable comments.
3. Reducing problematic comments does not necessarily improve review utility if useful comments are also suppressed or review coverage decreases.
4. Useful but non-directly-acceptable comments form a gray zone missed by binary accepted/rejected or correct/incorrect evaluation.

## Revised Research Questions

| RQ | Question | Expected Output |
|---|---|---|
| RQ1 | What types of problematic comments occur in LLM-generated code review, and how can they be operationally annotated? | Operational taxonomy and annotation guideline |
| RQ2 | Which evaluation dimensions are needed to assess problematic comments beyond technical correctness? | Multi-dimensional evaluation matrix |
| RQ3 | How do common mitigation strategies trade off error reduction against useful-feedback preservation, review coverage, human effort, and computational cost? | Trade-off framework and measurable trade-off dimensions |
| RQ4 | How does context quality affect the occurrence, detection, and mitigation of problematic review comments? | Context-quality layer and context-failure analysis |
| RQ5 | What framework can guide trade-off-aware evaluation of LLM-generated code review comments? | Final evaluation framework |

## Target Paper Type

The target paper is best described as:

```text
framework-oriented focused evidence synthesis
+ operational taxonomy
+ annotation protocol
+ illustrative annotated study
```

It is not a full systematic literature review unless the search protocol is expanded and formalized. It is also not a full empirical benchmark unless the annotated dataset and experimental setup become substantially larger.

## Minimum Viable Paper

The minimum viable version of the paper should include:

```text
50-paper evidence base
+ operational taxonomy
+ annotation guideline
+ 100–200 annotated generated review comments
+ inter-annotator agreement report
+ trade-off-aware framework
+ 2–3 concrete findings
```

The empirical part should support the taxonomy and framework. It should not become the main identity of the paper.

## Positioning Against Nearby Work

| Nearby Work Type | Why It Is Not Enough | Our Distinction |
|---|---|---|
| Metric/rubric papers | Improve quality measurement but often do not model trade-offs among usefulness, cost, and feedback preservation. | We connect quality dimensions to trade-off decisions. |
| Hallucination detectors | Focus on unsupported claims but not all low-value, non-actionable, or costly comments. | We include hallucination as one failure type in a broader taxonomy. |
| PR-level benchmarks | Improve realism but may not evaluate context quality, useful-feedback preservation, or mitigation costs. | We evaluate benchmark signals through a trade-off-aware framework. |
| RAG/context papers | Improve or vary context but may not distinguish context quantity from context quality. | We treat context quality as an evaluation object. |
| Industrial deployment papers | Provide useful workflow signals but are system-specific. | We generalize workflow signals into evaluation dimensions. |
| LLM-as-a-judge papers | Study evaluator validity but are often not code-review-specific. | We integrate evaluator validity into code review comment evaluation. |
| Human-review studies | Explain usefulness and review value but do not address LLM-generated comments directly. | We use them to ground human-centered evaluation dimensions. |

## Non-Goals

This paper should not attempt to:

- prove that one mitigation strategy is universally best;
- build a new state-of-the-art code review model;
- create a large benchmark leaderboard;
- solve hallucination detection as a standalone task;
- survey all LLM-for-SE literature;
- or evaluate every possible code review context.

## Immediate Next Steps

1. Update `synthesis/research-gap.md` to align fully with this core claim.
2. Update `drafts/methodology.md` to include taxonomy construction and annotation protocol.
3. Create `method/annotation-guideline.md`.
4. Create `method/evaluation-schema.md`.
5. Create `synthesis/final-framework.md`.
6. Create `drafts/introduction.md`.

## Writing Rule

When writing any draft section, use the style guide in:

```text
docs/academic-writing-style.md
```

The writing must be analytical, evidence-based, citation-supported, and careful about claim strength.
