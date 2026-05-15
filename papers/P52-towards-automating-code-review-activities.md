# P52 — Towards Automating Code Review Activities

## Metadata

- **ID:** P52
- **Title:** Towards Automating Code Review Activities
- **Authors:** Rosalia Tufano, Luca Pascarella, Michele Tufano, Denys Poshyvanyk, Gabriele Bavota
- **Year:** 2021
- **Venue:** IEEE Xplore / ICSE 2021
- **Official URL:** https://ieeexplore.ieee.org/abstract/document/9402025/
- **DOI:** TODO: extract from IEEE metadata
- **arXiv:** 2101.02518
- **Drive PDF:** https://drive.google.com/file/d/1X6BiupUKfz7raX9xn1Rkg_skyirno5fF
- **Drive PDF filename:** P52_towards_automating_code_review_activities.pdf
- **BibTeX key:** `p52_tufano2021_automating_code_review_activities`

## Status

- **Review status:** Not started
- **Verification status:** Official IEEE Xplore page verified from user-provided link; Drive PDF available; DOI still needs extraction.
- **Priority:** High

## Why This Paper Matters

This paper provides an important pre-LLM automated-code-review baseline. It helps position our work as part of a longer automation trajectory rather than as a response only to recent LLM-based review generation.

## Expected Use in Our Paper

Use this paper mainly in:

- `drafts/paper/sections/02-background.md`
- `drafts/paper/sections/03-related-work.md`
- `drafts/paper/sections/06-framework.md`

## Extraction Targets

When reading the paper, extract:

1. Which code review activities are automated.
2. What costs or human-effort reductions the paper motivates.
3. What evaluation criteria are used.
4. What limitations are reported for automation.
5. Whether generated artifacts are evaluated as directly actionable review outputs.
6. Any evidence that automation success depends on context or task type.

## Relevance to Our Framework

Potential links to our framework:

- cost and human effort;
- automation as review support rather than replacement;
- pre-LLM evaluation baselines;
- limits of direct automation metrics;
- connection between generated review output and developer action.

## Initial Notes

This paper should be used to show that code review automation had evaluation and cost trade-offs before LLMs. It can help avoid presenting the trade-off problem as unique to LLMs, while still showing that LLMs make the problem more acute because generated comments can be plausible, ungrounded, and context-sensitive.

## TODO

- [ ] Read the PDF.
- [ ] Extract the automated activities and evaluation setup.
- [ ] Extract any explicit cost/human-effort claims.
- [ ] Verify official DOI from IEEE metadata.
- [ ] Decide whether this paper should be cited in Introduction or only Background/Related Work.
