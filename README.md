# Trade-off-aware Evaluation of LLM-based Code Review

This repository supports a seminar literature-review project on **trade-off-aware evaluation of LLM-generated code review comments**. Its immediate deliverable is a focused evidence synthesis of how prior work defines problematic comments, evaluates review quality, mitigates failures, and reports consequences for useful-feedback preservation, coverage, human escalation, and cost.

Because the original database-specific retrieval history was not preserved, the current work must be reported as a **targeted structured literature review**, not as a fully reproducible systematic literature review (SLR). It can be upgraded to an SLR only after a documented search and screening run is completed.

## Review Goal

> Synthesize the available evidence on evaluation and mitigation of problematic LLM-generated code review comments, and derive a corpus-bounded taxonomy, annotation protocol, and trade-off-aware evaluation framework.

## Review Questions

| RQ | Question | Review output |
|---|---|---|
| RQ1 | Which problematic-comment types and failure categories have been reported? | Literature-derived failure taxonomy |
| RQ2 | Which dimensions are used to assess correctness, grounding, relevance, usefulness, actionability, context quality, and evaluator validity? | Evaluation-dimension map |
| RQ3 | Which mitigation families have been proposed or evaluated, and where do they intervene? | Intervention-point classification |
| RQ4 | What evidence exists about error reduction versus useful-feedback preservation, coverage, escalation, and cost? | Trade-off evidence map |
| RQ5 | How are context quality, dataset validity, and annotation difficulty treated? | Context and evidence-validity synthesis |
| RQ6 | Which studies directly or indirectly support the taxonomy, annotation protocol, and framework? | Core/supporting/peripheral evidence map |

## Methodological Positioning

The current evidence pipeline is:

```text
71 locally available full texts
  → explicit eligibility and relevance decisions
  → uniform eleven-section extraction records
  → Q1–Q12 quality appraisal
  → RQ1–RQ6 evidence mapping
  → cross-paper thematic synthesis
  → taxonomy, annotation protocol, and trade-off framework
  → seminar review report
```

The review does not pool incompatible metrics quantitatively. It distinguishes reported evidence from project interpretation and gives direct code-review studies more argumentative weight than indirect methodological or adjacent evidence.

## Evidence Tiers

- **Core:** directly evaluates LLM/automated review comments, review agents, review benchmarks, or mitigation relevant to the review workflow.
- **Supporting:** informs human-review value, evaluator validity, annotation, context quality, or workflow interpretation.
- **Peripheral:** supplies bounded background from adjacent code-generation, refinement, security, static-analysis, or non-functional evaluation work.

The 71-paper local corpus is an evidence pool, not automatically 71 equally weighted primary studies. The final included set and evidence tier must be frozen before the report is submitted.

## Current Status

- 71 unique project IDs, PDFs, authoritative notes, and bibliography entries are present.
- All 71 notes pass `skills/slr-paper-reviewer/scripts/validate-note.sh`.
- Duplicate P18 and P21 notes were consolidated and removed.
- `matrices/cross-paper-synthesis.md` covers P01–P71.
- The taxonomy, context model, evaluation dimensions, annotation guideline, evaluation schema, and trade-off framework are drafted.
- The original database queries, dates, retrieval counts, and title/abstract screening history remain unavailable.
- Several synthesis files still require publication-facing citations and integration into the final RQ-oriented report.

## Canonical Files

| File | Purpose |
|---|---|
| `method/slr-protocol.md` | Review scope, questions, eligibility, quality assessment, extraction, and synthesis plan |
| `method/slr-screening-log.md` | Verified corpus counts and missing search-history fields |
| `method/slr-readiness-audit.md` | Current readiness decision and remaining blockers |
| `papers/slr-review-progress.md` | Paper-level decisions, quality scores, confidence, and unresolved items |
| `matrices/paper-pool.md` | Compact study inventory |
| `matrices/cross-paper-synthesis.md` | Cross-paper thematic and argument synthesis |
| `synthesis/problematic-comment-taxonomy.md` | Literature-derived failure taxonomy |
| `synthesis/evaluation-dimensions.md` | Evaluation constructs and metric boundaries |
| `synthesis/context-quality.md` | Context-quality and context-failure model |
| `synthesis/trade-off-framework.md` | Mitigation trade-off framework |
| `synthesis/research-gap.md` | Corpus-bounded research gap |
| `method/annotation-guideline.md` | Annotation definitions and decision rules |
| `method/evaluation-schema.md` | Structured annotation and derived-metric schema |
| `references/references.bib` | Single bibliography source |

## Reporting Rules

- Call the current work a `targeted structured literature review` or `focused evidence synthesis`.
- Use Pxx IDs for internal traceability and bibliography keys for publication-facing claims.
- Separate reported evidence, inferred interpretation, and the project perspective.
- State that gap claims are bounded by the reviewed corpus.
- Do not treat a structural validation pass as independent reviewer agreement.
- Do not infer search or screening counts from the local PDF directory.

## Next Steps

1. Re-run and document database searches if the course requires the formal SLR label.
2. Freeze the final included set and evidence tier for each paper.
3. Complete citation traceability in all synthesis prose.
4. Produce RQ1–RQ6 result tables and narrative findings.
5. Rewrite the manuscript as a review report rather than an unexecuted empirical study.
6. Verify unresolved bibliographic metadata and lower-confidence extraction details.

Any controlled mitigation experiment is future work that can use the taxonomy and framework developed here; it is not part of the current seminar deliverable.
