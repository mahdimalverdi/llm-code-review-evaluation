# LLM Code Review Mitigation Evaluation

This repository contains paper notes, synthesis material, and manuscript drafts for a research project on **empirical evaluation of mitigation strategies for problematic LLM-generated code review comments**.

The current paper direction is:

> Reducing Problematic LLM-Generated Code Review Comments: An Empirical Study of Mitigation Trade-offs

The project studies how different mitigation strategies reduce problematic review comments and what trade-offs they introduce in useful-feedback preservation, review coverage, human escalation, context quality, and computational cost.

## Main Research Question

> Which mitigation strategies reduce which types of problematic LLM-generated code review comments, and what useful feedback, review coverage, human effort, and computational cost are lost or introduced in the process?

## Current Research Roadmap

The current direction is documented in:

```text
docs/research-roadmap.md
```

The project should be treated as a **small controlled empirical study**, supported by a targeted literature review, an operational taxonomy, and a trade-off-aware evaluation framework.

The strongest framing is not:

```text
framework only
or
method A beats method B
```

The stronger framing is:

```text
representative mitigation strategies
+ shared review instances
+ operational taxonomy
+ human annotation protocol
+ error-reduction metrics
+ useful-feedback preservation metrics
+ review coverage, escalation, and cost analysis
```

## Working Research Questions

| RQ | Question | Expected Output |
|---|---|---|
| RQ1 | What types of problematic comments occur in LLM-generated code review? | Label distribution and refined operational taxonomy |
| RQ2 | Which mitigation strategies reduce which types of problematic comments? | Strategy-by-failure-type comparison |
| RQ3 | How do mitigation strategies affect useful-feedback preservation, review coverage, human escalation, and execution cost? | Trade-off matrix and preservation/cost metrics |
| RQ4 | Does combining context-quality control with post-generation verification produce a better trade-off than either strategy alone? | Hybrid-strategy analysis, if included |
| RQ5 | How does context quality or context inconsistency affect mitigation success? | Context-quality analysis and context-dependent failure patterns |

## Research Focus

This project studies:

- LLM-generated code review comments;
- problematic, unsupported, irrelevant, non-actionable, low-value, or misleading comments;
- mitigation strategies such as robust prompting, context-quality gates, post-generation verification, and hybrid designs;
- trade-offs between reducing harmful comments and preserving useful feedback;
- context quality, reviewability, and context inconsistency;
- human annotation, agreement reporting, and evaluator validity;
- cost, latency, reviewer overhead, human escalation, and review coverage.

## Methodological Positioning

The project should be framed as a **controlled empirical comparison of representative mitigation strategies**.

The working pipeline is:

```text
Targeted literature review
  → operational taxonomy
  → annotation guideline and evaluation schema
  → dataset and sample selection
  → baseline comment generation
  → mitigation strategy application
  → human annotation
  → error-reduction analysis
  → useful-feedback preservation and cost analysis
  → empirical findings about mitigation trade-offs
```

The targeted literature review and taxonomy are important, but they support the empirical study. They are not the whole contribution by themselves.

## Writing Style

All English research prose in this repository should follow:

```text
docs/academic-writing-style.md
```

The main writing rule is to use clear, precise, measured academic English. Drafts should avoid inflated claims, define important terms, separate evidence from interpretation, and align the strength of claims with the size and quality of the empirical study.

Agent-specific editing instructions are also available in:

```text
AGENTS.md
```

## What This Is Not

This project should not be positioned as:

- just another comparison of LLMs for code review;
- just another benchmark leaderboard;
- just another hallucination detector;
- just another RAG/context expansion method;
- a generic survey of LLMs for software engineering;
- a framework-only paper without empirical grounding;
- or a method-comparison paper whose only result is choosing a winner.

The intended contribution is:

> an empirical trade-off analysis of mitigation strategies for problematic LLM-generated code review comments, supported by an operational taxonomy and reproducible annotation protocol.

## Repository Structure

```text
templates/
  paper-analysis-template.md

papers/
  P01-...md through P50-...md

synthesis/
  evaluation-dimensions.md
  problematic-comment-taxonomy.md
  context-quality.md
  trade-off-framework.md
  research-gap.md

matrices/
  paper-pool.md
  cross-paper-synthesis.md

references/
  references.bib
  README.md

docs/
  academic-writing-style.md
  research-roadmap.md

drafts/paper/sections/
  00-abstract.md
  01-introduction.md
  02-background.md
  03-related-work.md
  04-methodology.md
  05-operational-taxonomy.md
  06-framework.md
  07-illustrative-study.md
  08-findings.md
  09-discussion.md
  10-threats-to-validity.md
  11-conclusion.md
```

## Canonical Files

Use these files as the main working sources:

| File | Purpose |
|---|---|
| `docs/research-roadmap.md` | Current project direction and Q1-oriented empirical framing. |
| `drafts/paper/sections/00-abstract.md` | Current manuscript abstract. |
| `drafts/paper/sections/01-introduction.md` | Main problem framing and contributions. |
| `drafts/paper/sections/04-methodology.md` | Controlled empirical study design. |
| `matrices/paper-pool.md` | Compact inventory of papers and their role in the project. |
| `matrices/cross-paper-synthesis.md` | Cross-paper argument map and gap synthesis. |
| `synthesis/problematic-comment-taxonomy.md` | Failure types for generated comments, context, workflow, and evaluators. |
| `synthesis/context-quality.md` | Context-quality dimensions, context failure types, and gating implications. |
| `synthesis/trade-off-framework.md` | Trade-off matrix for filtering, gating, context expansion, and human escalation. |
| `references/references.bib` | Central bibliography database for all drafts. |
| `docs/academic-writing-style.md` | Academic English writing rules for research prose. |

## Current Status

- Paper notes exist for **P01–P50**.
- `matrices/paper-pool.md` is aligned with the spreadsheet metadata after the latest cleanup pass.
- `matrices/cross-paper-synthesis.md` is the canonical cross-paper synthesis and covers **P01–P50**.
- `references/references.bib` contains entries for **P01–P50**, based on the spreadsheet metadata.
- The manuscript has been reframed toward an empirical mitigation-trade-off study.
- The title, abstract, introduction, methodology, taxonomy, framework, and empirical evaluation design have been updated to match the current direction.
- Remaining cleanup: replace `TODO_PUBLISHER_BIBTEX` entries with official publisher-exported BibTeX and do PDF-level verification for lower-confidence paper notes.

## Core Working Rule

Every empirical claim should be tied to a measurable artifact:

```text
annotation label
or
strategy output
or
failure-type distribution
or
preservation/coverage metric
or
cost/escalation metric
```

For literature-based claims, separate:

```text
Reported evidence
vs
Inferred interpretation
vs
Our perspective
```

## Next Steps

- Create `method/annotation-guideline.md`.
- Create `method/evaluation-schema.md`.
- Decide the dataset and sampling plan.
- Decide the generation model and prompts.
- Define the implementation details for the mitigation strategies.
- Create metric-computation scripts.
- Run a small pilot annotation.
- Replace core `TODO_PUBLISHER_BIBTEX` entries with official publisher-exported BibTeX.

## Current Priority

The next work should not be adding more papers. The next work should be making the empirical study executable.

Recommended next step:

```text
Choose the dataset and create the annotation guideline/evaluation schema.
```
