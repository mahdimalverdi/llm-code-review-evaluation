# LLM Code Review Evaluation

This repository contains paper notes and synthesis material for a research project on **trade-off-aware evaluation of LLM-generated code review comments**.

The project is not just a literature-summary workspace. Its goal is to synthesize evidence from recent LLM-based code review studies and derive:

1. a taxonomy of problematic generated review comments;
2. an evaluation framework for generated review comments;
3. a context-quality model for code review automation;
4. and a trade-off matrix for filtering, gating, aggregation, and human-in-the-loop decisions.

## Main Research Question

> How can we evaluate LLM-generated code review comments in a trade-off-aware way that accounts for context quality, problematic comment types, and the balance between reducing harmful comments and preserving useful feedback?

## Working Research Questions

| RQ | Question | Expected Output |
|---|---|---|
| RQ1 | What types of problematic comments appear in LLM-generated code review? | Problematic-comment taxonomy |
| RQ2 | How is context quality defined, used, or ignored in current LLM-based code review evaluation? | Context-quality model |
| RQ3 | Which evaluation dimensions are covered or missing in current studies? | Evaluation-dimension matrix |
| RQ4 | What trade-offs arise when generated review comments are filtered, gated, aggregated, or enriched with context? | Trade-off matrix |
| RQ5 | What should a trade-off-aware evaluation framework for LLM-generated code review comments include? | Final framework |

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
```

## What This Is Not

This project should not be positioned as:

- just another comparison of LLMs for code review;
- just another benchmark leaderboard;
- just another hallucination detector;
- just another RAG/context expansion method;
- just a generic survey of LLMs for software engineering.

The stronger framing is:

> a framework-oriented synthesis of LLM-based code review evaluation, focused on context quality, problematic comment types, and trade-off-aware evaluation.

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

drafts/
  methodology.md
  introduction.md
  related-work.md
```

## Canonical Files

Use these files as the main working sources:

| File | Purpose |
|---|---|
| `matrices/paper-pool.md` | Compact inventory of all papers and their role in the project. |
| `matrices/cross-paper-synthesis.md` | Main cross-paper argument map and gap synthesis. |
| `synthesis/evaluation-dimensions.md` | Evaluation dimensions for generated review comments and review workflows. |
| `synthesis/problematic-comment-taxonomy.md` | Failure types for generated comments, context, workflow, and evaluators. |
| `synthesis/context-quality.md` | Context-quality dimensions, context failure types, and gating implications. |
| `synthesis/trade-off-framework.md` | Trade-off matrix for filtering, gating, context expansion, and human escalation. |
| `synthesis/research-gap.md` | Main gap statement and research positioning. |

## Current Status

- Paper notes exist for **P01–P50**.
- `matrices/paper-pool.md` is aligned with the spreadsheet metadata after the latest cleanup pass.
- `matrices/cross-paper-synthesis.md` is the canonical cross-paper synthesis and covers **P01–P50**.
- Temporary synthesis files for P37–P41 and P42–P50 were removed after their content was merged into canonical synthesis/matrix files.
- Remaining cleanup: add checked BibTeX entries and do PDF-level verification for lower-confidence paper notes.

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

- Add checked BibTeX entries for cited papers.
- Deep-read P39 and P40 because they directly strengthen usefulness and context-quality arguments.
- Deep-read P49 if context consistency becomes a core part of the framework.
- Update draft sections from the canonical synthesis files.
- Decide whether to add a small illustrative mini-validation using 20–50 generated review comments.
