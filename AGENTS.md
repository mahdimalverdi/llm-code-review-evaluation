# Repository Instructions for Agents

This repository contains research notes, synthesis files, and draft material for a paper on trade-off-aware evaluation of LLM-generated code review comments.

## Writing Style

All English research prose must follow:

```text
docs/academic-writing-style.md
```

In particular:

- Write clear, precise, measured academic English.
- Do not use promotional or inflated language.
- Do not overclaim beyond the evidence.
- Define important terms before relying on them.
- Prefer synthesis over paper-by-paper summaries.
- Support literature-based claims with citation keys from `references/references.bib`.
- Use Pandoc/Quarto-style citations, for example: `[@p14_li2022_codereviewer; @p01_lu2025_deepcrceval]`.

## Citation Rules

The single source of truth for bibliography data is:

```text
references/references.bib
```

Do not create duplicate BibTeX blocks inside paper notes or drafts.

Use stable citation keys with the project paper ID prefix:

```text
pXX_firstauthorYYYY_shortslug
```

Before final submission, entries marked with `TODO_PUBLISHER_BIBTEX` should be replaced or checked against official publisher-exported BibTeX.

## Canonical Project Files

Use these as the main working sources:

```text
matrices/paper-pool.md
matrices/cross-paper-synthesis.md
synthesis/evaluation-dimensions.md
synthesis/problematic-comment-taxonomy.md
synthesis/context-quality.md
synthesis/trade-off-framework.md
synthesis/research-gap.md
references/references.bib
```

## Paper Notes

Paper notes live in:

```text
papers/
```

Use the template:

```text
templates/paper-analysis-template.md
```

Paper notes should extract evidence for the framework. They should not merely summarize papers.

## Editing Rules

When editing drafts or synthesis files:

- Preserve citation keys.
- Keep internal paper IDs such as `P01` when they help trace back to the spreadsheet.
- Use citations for factual claims about prior work.
- Separate reported evidence, inferred interpretation, and our perspective.
- Avoid claiming that no prior work exists unless this has been carefully checked.
- Do not delete canonical files unless their content has been merged elsewhere.

## Preferred Research Framing

Frame the project as:

> a focused evidence synthesis and trade-off-aware evaluation framework for LLM-generated code review comments.

Do not frame it as:

- just another benchmark;
- just another model comparison;
- just another hallucination detector;
- just a generic survey of LLMs for software engineering.
