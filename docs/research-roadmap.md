# Research Roadmap

## Current Deliverable

The immediate deliverable is:

> a targeted structured literature review and focused evidence synthesis on trade-off-aware evaluation of LLM-generated code review comments.

The review supports an operational taxonomy, annotation protocol, and evaluation framework. A controlled empirical comparison of mitigation strategies is a possible follow-on study, not the current seminar output.

## Working Title

```text
Trade-off-aware Evaluation of LLM-based Code Review:
A Structured Review of Comment Quality, Mitigation, and Evaluation Validity
```

## Review Boundary

The local corpus contains 71 full-text records. It combines direct code-review studies with supporting work on human review, evaluator validity, security, static analysis, code refinement, and non-functional evaluation. Evidence must therefore be tiered rather than counted as homogeneous.

| Tier | Role in synthesis | Claim boundary |
|---|---|---|
| Core | Direct evidence about generated review comments, review agents, benchmarks, or mitigation | May support review-specific findings |
| Supporting | Human-review, evaluator, annotation, context, or workflow evidence | Supports constructs and interpretation |
| Peripheral | Adjacent security, refinement, code-generation, or efficiency evidence | Supports only explicitly bounded transfer claims |

## Review Questions and Deliverables

| RQ | Deliverable |
|---|---|
| RQ1: reported problematic-comment types | Operational taxonomy with traceable evidence |
| RQ2: evaluation dimensions and instruments | Dimension/metric/evaluator-validity matrix |
| RQ3: mitigation families and intervention points | Before/during/after-generation and pre-display classification |
| RQ4: reported trade-offs | Preservation, coverage, escalation, workflow, and cost evidence map |
| RQ5: context, dataset, and annotation validity | Context-quality and methodological-risk synthesis |
| RQ6: direct and indirect framework support | Tiered paper-to-framework mapping |

## Current Evidence Status

- P01–P71 each have one authoritative full-text note.
- All notes pass the canonical structural validator.
- All IDs have bibliography entries.
- Cross-paper synthesis covers the full corpus.
- The arXiv full-text queue has been screened in the reviewed ledger: 140 records, 132 included and 8 excluded.
- Search-history reconstruction and independent selection/calibration remain incomplete.
- The current review must not be called a completed SLR until those requirements are satisfied.

## Work Packages

### WP1 — Corpus and protocol closure

- Freeze inclusion and evidence tiers.
- Resolve remaining bibliographic and extraction-confidence items.
- If required, execute reproducible searches and record database-specific strings, dates, counts, deduplication, and exclusions.

### WP2 — RQ-oriented synthesis

- Build one result table for each RQ.
- Count studies only after defining the denominator and evidence tier.
- Keep incompatible metrics as narrative or structured thematic synthesis.
- Link every category and finding to paper IDs and citation keys.

### WP3 — Seminar manuscript

Use this structure:

```text
1. Introduction
2. Background
3. Review Method
4. Study Selection and Characteristics
5. Results by RQ
6. Trade-off-aware Evaluation Framework
7. Discussion and Research Gaps
8. Threats to Validity
9. Conclusion
```

### WP4 — Quality control

- Verify bibliography metadata.
- Check citation-key resolution.
- Reconcile all corpus counts.
- Audit claim strength against evidence tiers and quality scores.
- Build and visually inspect the final PDF.

## Deferred Empirical Study

The existing annotation guideline and evaluation schema can support a later controlled study comparing prompting, context gates, verification, and hybrid mitigation. That study would require dataset selection, generated outputs, pilot annotation, agreement analysis, preservation/coverage metrics, and cost reporting. It should be described as future work until executed.

## Current Priority

The next priority is not collecting additional convenience papers or implementing mitigation strategies. It is closing the review method and producing traceable RQ1–RQ6 findings from the existing corpus.
