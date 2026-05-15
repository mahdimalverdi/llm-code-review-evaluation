# Reference Management

This directory is the canonical place for bibliography data.

## Files

| File | Purpose |
|---|---|
| `references.bib` | Main BibTeX database used by drafts and final paper. |
| `README.md` | Citation-key convention and workflow. |

## Citation-Key Convention

Use stable keys that include the paper ID so they remain easy to map back to the spreadsheet and paper notes.

```text
pXX_firstauthorYYYY_shortslug
```

Examples:

```text
p30_weyssow2025_codeultrafeedback
p33_he2025_llmjudge_se
p40_ram2018_reviewability
```

Rules:

- Keep the `pXX` prefix even if the title or venue changes later.
- Use the first author’s family name in lowercase ASCII.
- Use the official publication year if a peer-reviewed version exists.
- Use the arXiv year only when no official publication has been verified.
- Keep the slug short and stable.

## How to Cite in Markdown Drafts

When writing drafts intended for Pandoc/Quarto/LaTeX later, cite papers like this:

```markdown
LLM-generated review comments require evaluation beyond lexical similarity [@p14_li2022_codereviewer; @p01_deepcrceval].
```

Multiple citations:

```markdown
Recent work highlights context quality, hallucination, and workflow trade-offs [@p02_hallujudge; @p04_sweprbench; @p07_revmate].
```

Narrative citation style:

```markdown
Bosu et al. argue that useful code review feedback is developer-centered [@p39_bosu2015_useful_reviews].
```

## Paper Note Rule

Each paper note should include only the citation key, not a full duplicated BibTeX entry.

Recommended bibliographic block:

```markdown
| Citation key | `pXX_firstauthorYYYY_shortslug` |
```

If the BibTeX entry is missing, write:

```markdown
| Citation key | `TODO: add to references/references.bib` |
```

## Verification Levels

Use these comments above entries in `references.bib` when needed:

```bibtex
% VERIFIED: official publisher DOI page checked.
% TODO_VERIFY: metadata copied from spreadsheet/paper note; verify with publisher BibTeX.
% ARXIV_ONLY: no peer-reviewed publication verified yet.
```

## Workflow

1. Add or update the official metadata in the spreadsheet.
2. Add or update the paper note in `papers/PXX-*.md`.
3. Add the BibTeX entry in `references/references.bib`.
4. Add the citation key to the paper note.
5. Use only citation keys in drafts.
6. Before final submission, replace `TODO_VERIFY` entries with publisher-exported BibTeX when available.

## Important Rule

Do not paste separate BibTeX entries into every paper note. That creates duplicate, stale bibliography data. The single source of truth is:

```text
references/references.bib
```
