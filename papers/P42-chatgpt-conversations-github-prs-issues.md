# P42 — An Empirical Study on Developers Shared Conversations with ChatGPT in GitHub Pull Requests and Issues

> [!NOTE]
> Compact v2 analysis. P42 is not a code-review-generation paper, but it is useful background for understanding how developers expose, discuss, and reuse ChatGPT conversations in real GitHub collaboration spaces.

## Status

- Paper ID: `P42`
- Analysis status: `First pass completed from bibliographic metadata; needs PDF-level verification`
- Priority: `Low`
- Reading depth: `Background`
- Last updated: `2026-05-14`
- Confidence in extraction: `Medium`

## Bibliographic Information

| Field | Value |
|---|---|
| Title | An Empirical Study on Developers Shared Conversations with ChatGPT in GitHub Pull Requests and Issues |
| Authors | Daniel Wasserbaech, Carol Hanna Wagner, Tanja E. J. Vos, Sebastiano Panichella, Annibale Panichella, Marco Aniche |
| Year | 2024 |
| Venue / Source | Empirical Software Engineering / Springer |
| Publication type | Peer-reviewed journal article / empirical study |
| Link | https://link.springer.com/article/10.1007/s10664-024-10540-x |
| DOI / arXiv | DOI: 10.1007/s10664-024-10540-x; arXiv:2403.10468 |
| Code / artifact | Needs PDF-level verification |

```bibtex
% TODO: Add checked Springer BibTeX.
```

## One-Sentence Summary

> This paper studies how developers share ChatGPT conversations in GitHub pull requests and issues, offering evidence about real developer usage, collaboration context, and public AI-assisted development behavior.

## Main Goal of the Paper

The paper aims to characterize how ChatGPT conversations appear in GitHub collaboration artifacts and what roles these shared conversations play in developer communication and software work.

## Relevance to Our Research Questions

| Our RQ | Relevance | Evidence / Use |
|---|---|---|
| RQ1 — problematic comments | `Low / Medium` | Helps contextualize AI-generated advice in collaborative developer settings. |
| RQ2 — context quality | `Medium` | Shows that AI outputs are embedded in PR/issue context and developer explanations. |
| RQ3 — evaluation dimensions | `Medium` | Supports developer-practice and collaboration-aware evaluation. |
| RQ4 — trade-offs | `Medium` | Public AI sharing may help collaboration but can introduce trust, provenance, and accountability issues. |
| RQ5 — framework design | `Low / Medium` | Useful for socio-technical background, not core comment-quality taxonomy. |

## Dataset / Study Context

| Field | Value |
|---|---|
| Dataset / study name | ChatGPT conversations shared in GitHub PRs/issues |
| Dataset / study source | GitHub pull requests and issues |
| Dataset / study size | Needs PDF-level verification |
| Repository type | Open-source |
| Input context available | GitHub issues, pull requests, shared ChatGPT conversation links/content |
| Output being evaluated | Developer use and sharing of ChatGPT conversations |
| Data availability | Needs verification |

## Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Technical correctness | `Not central` | The study is about usage patterns, not correctness of outputs. |
| Usefulness | `Partially` | Shared conversations may be used because developers find them useful. |
| Context alignment | `Partially` | ChatGPT conversations are interpreted inside PR/issue context. |
| Developer trust | `Medium` | Public sharing reflects some level of trust or communicative value. |
| Workflow impact | `Medium` | Shows AI use in real collaborative workflows. |
| Knowledge transfer / team awareness | `Medium` | Shared conversations can communicate reasoning or background to others. |

## Problematic Comment Types / Error Taxonomy

### Explicitly Defined Error Types

Not a generated-review-comment taxonomy paper.

### Inferred Error Types

- `Inferred`: AI advice used without enough project context.
- `Inferred`: AI-generated explanation that may be trusted without verification.
- `Inferred`: Conversation provenance ambiguity.
- `Inferred`: Collaboration noise when AI outputs are shared without clear relevance.

## Context-Quality Extraction

| Context Dimension | Coverage | Evidence / Notes |
|---|---|---|
| Relevance | `Medium` | Shared ChatGPT conversations need to relate to PR/issue discussion. |
| Completeness | `Medium` | Conversations may omit project-specific context. |
| Consistency | `Medium` | AI advice may or may not align with repository discussion. |
| Groundability | `Medium` | Shared claims should be traceable to code, issue, or discussion context. |
| Socio-technical context | `High` | The paper is mainly valuable as workflow/collaboration evidence. |

## Trade-off Extraction

| Strategy / Mechanism | Benefit | Risk / Cost | Missing Metric for Our Work |
|---|---|---|---|
| Sharing AI conversations in PRs/issues | Increases transparency and may support discussion | Can create unverified authority or irrelevant noise | Trust and verification outcome |
| Using ChatGPT as collaboration support | Helps explanation and ideation | May lack repository-specific grounding | Grounded usefulness |
| Public AI-assisted discussion | Enables observation of real usage | Public GitHub may not represent private industry use | Generalizability |

## Key Findings for Our Synthesis

| Finding | Importance for us |
|---|---|
| Developers already integrate ChatGPT conversations into GitHub collaboration artifacts. | LLM review tools should be evaluated as part of developer workflows, not isolated outputs. |
| AI-generated text can become part of PR/issue communication. | Provenance, trust, and verification matter. |
| Public sharing creates socio-technical signals. | Supports including workflow and collaboration dimensions. |

## Limitations from Our Perspective

- Not focused on code review comment generation.
- Does not directly evaluate LLM-generated review comments.
- Public GitHub behavior may not generalize to private code review systems.
- Useful mainly for socio-technical background and developer-practice evidence.

## Final Assessment

| Field | Value |
|---|---|
| Overall relevance to our study | `Low / Medium` |
| Should we cite this paper? | `Maybe` |
| Priority for deep reading | `Low / Medium` |
| Confidence in this analysis | `Medium` |

### Short Justification

P42 can support a background claim that developers already use and share LLM outputs in collaborative software work. It is less central than LLM-code-review papers but useful for workflow and provenance framing.

## Follow-up TODOs

- [ ] Verify exact dataset size and coding scheme from PDF.
- [ ] Add checked Springer BibTeX.
- [ ] Extract examples of PR/issue usage categories.
- [ ] Decide whether to cite in related work or discussion only.
