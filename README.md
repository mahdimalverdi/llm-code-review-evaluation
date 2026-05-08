# LLM Code Review Evaluation

This repository contains literature-review notes and synthesis material for a research project on LLM-based code review evaluation.

The main focus is not only whether an LLM can generate review comments, but how those comments should be evaluated, filtered, and interpreted in realistic software engineering workflows.

## Research Focus

This project studies:

- LLM-based code review comment generation and evaluation
- Hallucination and unsupported claims in generated review comments
- Context quality and context misalignment
- Problematic or low-value review comments
- Human annotation protocols for review-comment quality
- Trade-offs between reducing harmful comments and preserving useful comments
- Cost, latency, human verification, and workflow impact

## Repository Structure

```text
papers/
  P01-deepcrceval.md
  P02-hallujudge.md
  P03-rovodev-code-reviewer.md
  P04-swe-prbench.md

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
  introduction.md
  related-work.md
  methodology.md
```

## Working Rule

Each paper should be analyzed using a stable template so that the notes can later be converted into the related-work section, taxonomy, evaluation framework, and research-gap argument.

## Current Status

The first analytical pass has started for the following papers:

| ID | Paper | Status |
|---|---|---|
| P01 | DeepCRCEval | First pass completed in notes |
| P02 | HalluJudge | First pass completed in notes |
| P03 | RovoDev Code Reviewer | First pass completed in notes |
| P04 | SWE-PRBench | First pass draft completed; needs second verification pass |
