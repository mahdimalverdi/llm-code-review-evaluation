# LLM Code Review Evaluation

This repository contains paper notes and synthesis material for a research project on **trade-off-aware evaluation of LLM-generated code review comments**.

The project is not just a literature-summary workspace. Its goal is to synthesize evidence from recent LLM-based code review studies and derive:

1. a taxonomy of problematic generated review comments;
2. an evaluation framework for generated review comments;
3. a context-quality model for code review automation;
4. and a trade-off matrix for filtering, gating, aggregation, and human-in-the-loop decisions.

## Main Research Question

> How can we evaluate LLM-generated code review comments in a trade-off-aware way that accounts for context quality, problematic comment types, and the balance between reducing harmful comments and preserving useful feedback?

## Current Research Roadmap

The current direction is documented in:

```text
docs/research-roadmap.md
```

This roadmap records the revised framing after supervisor feedback. The project should no longer be treated as a comparison of several mitigation strategies. The comparison of strategies may support the paper, but the main contribution should be:

```text
operational taxonomy
+ trade-off-aware evaluation framework
+ human annotation protocol
+ small annotated evidence layer
+ concrete insights about error reduction, useful-feedback preservation, and cost
```

## Working Research Questions

| RQ | Question | Expected Output |
|---|---|---|
| RQ1 | What types of problematic comments occur in LLM-generated code review, and how can they be operationally annotated? | Operational taxonomy and annotation guideline |
| RQ2 | Which evaluation dimensions are needed to assess problematic comments beyond technical correctness? | Multi-dimensional evaluation matrix |
| RQ3 | How do common mitigation strategies trade off error reduction against useful-feedback preservation, review coverage, human effort, and computational cost? | Trade-off framework and measurable trade-off dimensions |
| RQ4 | How does context quality affect the occurrence, detection, and mitigation of problematic review comments? | Context-quality layer and context-failure analysis |
| RQ5 | What framework can guide trade-off-aware evaluation of LLM-generated code review comments? | Final evaluation framework |

## Research Focus

This project studies:

- LLM-based code review comment generation and evaluation;
- hallucination and unsupported claims in generated review comments;
- context quality, reviewability, and context misalignment;
- problematic, low-value, or non-actionable review comments;
- human annotation, user-study, production-feedback, and LLM-as-a-judge protocols;
- trade-offs between reducing harmful comments and preserving useful comments;
- filtering, gating, aggregation, RAG, static-analysis hybrids, and human-in-the-loop mechanisms;
- cost, latency, reviewer overhead, human verification, and workflow impact.

## Methodological Positioning

The project should be framed as a **focused evidence synthesis**, not as a generic survey or a benchmark/model paper.

The working pipeline is:

```text
Paper selection
  → structured coding using the template
  → extraction of evaluation dimensions
  → extraction of problematic comment types
  → extraction of context-quality dimensions
  → extraction of trade-offs
  → cross-paper synthesis
  → taxonomy + framework + trade-off matrix
  → annotation guideline + small annotated evidence layer
```

## Writing Style

All English research prose in this repository should follow:

```text
docs/academic-writing-style.md
```

The main writing rule is to use clear, precise, measured academic English. Drafts should synthesize evidence rather than list papers, avoid promotional or inflated language, define important terms, and support literature-based claims with citation keys from `references/references.bib`.

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
- just a generic survey of LLMs for software engineering;
- a small empirical method-comparison paper whose main contribution is choosing a winning strategy.

The stronger framing is:

> a framework-oriented synthesis of LLM-based code review evaluation, focused on context quality, problematic comment types, trade-off-aware evaluation, and a carefully annotated evidence layer.

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

drafts/
  methodology.md
  introduction.md
  related-work.md
```

## Canonical Files

Use these files as the main working sources:

| File | Purpose |
|---|---|
| `docs/research-roadmap.md` | Current project direction after supervisor feedback. |
| `matrices/paper-pool.md` | Compact inventory of all papers and their role in the project. |
| `matrices/cross-paper-synthesis.md` | Main cross-paper argument map and gap synthesis. |
| `synthesis/evaluation-dimensions.md` | Evaluation dimensions for generated review comments and review workflows. |
| `synthesis/problematic-comment-taxonomy.md` | Failure types for generated comments, context, workflow, and evaluators. |
| `synthesis/context-quality.md` | Context-quality dimensions, context failure types, and gating implications. |
| `synthesis/trade-off-framework.md` | Trade-off matrix for filtering, gating, context expansion, and human escalation. |
| `synthesis/research-gap.md` | Main gap statement and research positioning. |
| `references/references.bib` | Central bibliography database for all drafts. |
| `docs/academic-writing-style.md` | Academic English writing rules for research prose. |

## Current Status

- Paper notes exist for **P01–P50**.
- `matrices/paper-pool.md` is aligned with the spreadsheet metadata after the latest cleanup pass.
- `matrices/cross-paper-synthesis.md` is the canonical cross-paper synthesis and covers **P01–P50**.
- `references/references.bib` contains entries for **P01–P50**, based on the spreadsheet metadata.
- `docs/research-roadmap.md` records the revised paper direction after supervisor feedback.
- Temporary synthesis files for P37–P41 and P42–P50 were removed after their content was merged into canonical synthesis/matrix files.
- Remaining cleanup: replace `TODO_PUBLISHER_BIBTEX` entries with official publisher-exported BibTeX and do PDF-level verification for lower-confidence paper notes.

## Core Working Rule

Each paper should be analyzed using the Markdown template. The analysis should extract evidence for the framework, not merely summarize the paper.

For each paper, we explicitly separate:

```text
Reported evidence
vs
Inferred interpretation
vs
Our perspective
```

## Next Steps

- Create `synthesis/core-claim.md`.
- Update `synthesis/research-gap.md` and `drafts/methodology.md` according to `docs/research-roadmap.md`.
- Create `method/annotation-guideline.md`.
- Create `method/evaluation-schema.md`.
- Create `synthesis/final-framework.md`.
- Create `drafts/introduction.md`.
- Replace core `TODO_PUBLISHER_BIBTEX` entries with official publisher-exported BibTeX.
