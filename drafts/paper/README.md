# Paper Draft Workflow

This directory contains the section-by-section draft of the paper.

The goal is to write the paper gradually, one section at a time, while keeping the final LaTeX output reproducible.

## Structure

```text
drafts/paper/
  README.md
  sections_order.txt
  sections/
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

## Writing Rule

All prose should follow:

```text
docs/academic-writing-style.md
```

In particular:

- write clear and measured academic English;
- avoid promotional or inflated claims;
- synthesize prior work instead of listing papers;
- define important terms before relying on them;
- cite literature-based claims using keys from `references/references.bib`.

## Citation Format

Use Pandoc-style citation keys in Markdown sections:

```markdown
Prior work has shown that lexical similarity is insufficient for generated code review comments [@p14_li2022_codereviewer; @p01_lu2025_deepcrceval].
```

The build script converts this form into LaTeX `\citep{...}` commands.

## Build LaTeX

From the repository root, run:

```bash
python scripts/build_latex.py
```

This generates:

```text
build/paper.tex
```

The generated file uses:

```latex
\bibliography{../references/references}
```

when written to `build/paper.tex`.

## Editing Workflow

1. Edit one section under `drafts/paper/sections/`.
2. Keep the section focused and citation-supported.
3. Run `python scripts/build_latex.py`.
4. Inspect `build/paper.tex`.
5. Later, compile the LaTeX file with a standard BibTeX workflow.

## Important Rule

Do not manually edit `build/paper.tex`. It is generated from the Markdown section files.
