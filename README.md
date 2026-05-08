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
- context quality and context misalignment;
- problematic or low-value review comments;
- human annotation, user-study, and production-feedback protocols;
- trade-offs between reducing harmful comments and preserving useful comments;
- filtering, gating, aggregation, and LLM-as-a-Judge mechanisms;
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
  P01-deepcrceval.md
  P02-hallujudge.md
  P03-rovodev-code-reviewer.md
  P04-swe-prbench.md
  P05-swrbench.md
  P06-contextcrbench.md
  P07-revmate-user-study.md

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

## Current Status

| ID | Paper | Status | Main Use |
|---|---|---|---|
| P01 | DeepCRCEval | First pass completed | Evaluation dimensions; critique of text similarity |
| P02 | HalluJudge | First pass completed | Hallucination; context alignment; safeguard/gate framing |
| P03 | RovoDev Code Reviewer | First pass completed | Industrial deployment; workflow metrics; quality gates |
| P04 | SWE-PRBench | First pass completed; needs second verification pass | PR-level benchmark; context degradation evidence |
| P05 | SWRBench | First pass completed; needs PDF-level verification | PR-centric benchmark; full project context; structured ground truth |
| P06 | ContextCRBench | First pass completed; needs PDF-level verification | Enriched semantic/code context; fine-grained evaluation; data-quality critique |
| P07 | RevMate user study | First pass completed; needs PDF-level verification | Live user study; acceptance; perceived value; reviewer time overhead |

## Important Synthesis Files

- `synthesis/research-gap.md`: main gap statement and research questions.
- `synthesis/evaluation-dimensions.md`: dimensions to measure in generated review comments.
- `synthesis/problematic-comment-taxonomy.md`: failure types for generated review comments.
- `synthesis/context-quality.md`: context-quality dimensions and context failure types.
- `synthesis/trade-off-framework.md`: trade-off matrix for filtering/gating/aggregation decisions.
- `matrices/cross-paper-synthesis.md`: cross-paper mapping from evidence to arguments.

## Next Steps

- Verify high-priority papers against their PDFs.
- Add BibTeX entries for cited papers.
- Refine the taxonomy after 8–10 papers.
- Convert `research-gap.md` into the introduction and related-work critique.
- Decide whether to add a small illustrative mini-validation using 20–50 generated review comments.
