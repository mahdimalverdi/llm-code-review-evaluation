# Project Roadmap and Progress Log

Last updated: 2026-08-04

## Purpose

This document is the living plan for the focused evidence synthesis and trade-off-aware evaluation framework for LLM-generated code review comments. It records the current project state, the order of remaining work, the completion criteria for each phase, and dated progress updates.

The current review must be described as a **targeted structured literature review** or **focused evidence synthesis**. It must not be described as a fully reproducible systematic literature review until the database-search and selection requirements in Phase 3 are satisfied.

## How to Maintain This File

1. Update the date at the top whenever project status changes materially.
2. Use only these status values: `Complete`, `In progress`, `Planned`, `Blocked`, `Optional`, or `Not started`.
3. Change a phase to `Complete` only when its exit criteria are satisfied and its listed outputs exist.
4. Record material scope, method, or evidence decisions in the decision log.
5. Add one concise row to the progress log after each substantial work session.
6. Keep counts linked to generated data or screening files. Do not reconstruct unavailable historical counts.

## Current Snapshot

| Area | Current state | Evidence |
|---|---|---|
| Local evidence corpus | 71 records: 41 core, 24 supporting, and 6 peripheral | `data/slr-summary.md` |
| Paper notes | 71 authoritative notes; all pass the eleven-section structural validator | `papers/slr-review-progress.md` |
| Structured extraction | 71 study-level rows and 550 coded evidence rows | `data/slr-extraction.csv`; `data/slr-coding-evidence.csv` |
| Canonical synthesis | Taxonomy, evaluation dimensions, context model, trade-off framework, and research gap drafted | `synthesis/` |
| Manuscript | Twelve section files exist; several sections remain short or provisional | `drafts/paper/sections/` |
| Reproducible arXiv amendment | 293 unique records screened by title/abstract; 140 assessed at full text; local acquisition state synchronized | `method/search-protocol-amendment.md`; `data/search/` |
| arXiv full-text queue | 132 included for consideration and 8 excluded; 52 core records extracted and held for final freeze; supporting records remain to be assessed | `data/search/arxiv-full-text-screening-reviewed.csv`; `data/search/core-reconciliation-queue.csv` |
| External candidate export | 18 duplicates, 3 full-text includes, 8 provisional includes, and 1 exclusion | `data/search/external-candidate-screening.csv` |
| External acquisition | 9 already downloaded, 3 newly downloaded, and 9 metadata-only records | `data/search/external-pdf-acquisition.csv` |
| Citation-key integrity | 125 citation blocks checked across 22 synthesis and draft files; all 64 used keys exist in the bibliography | Audit completed 2026-08-04 |
| Review label | Targeted structured review; formal SLR criteria are not yet met | `method/slr-readiness-audit.md` |

The 132 arXiv inclusions are full-text screening outcomes, not 132 automatically accepted additions to the 71-record evidence corpus. Duplicate and companion resolution, relevance weighting, and corpus-freeze decisions are still required.

## Roadmap Overview

| Phase | Scope | Status | Immediate output | Exit criterion |
|---|---|---|---|---|
| 0 | Protocol and project foundations | Complete | Review protocol, RQs, controlled vocabulary, and reporting boundary | Scope, RQs, eligibility criteria, extraction fields, and synthesis method are documented |
| 1 | Baseline 71-paper corpus | Complete | Canonical notes, quality appraisal, and structured extraction | Every P01–P71 record has one valid note, a decision, a tier, and RQ-linked evidence |
| 2 | Initial synthesis and manuscript structure | Complete | Canonical synthesis files and twelve manuscript section files | All framework components and manuscript sections exist in draft form |
| 3 | Supplementary search consolidation | In progress | Deduplicated and reconciled candidate set | Every supplementary candidate has a final duplicate, include, or exclude outcome supported by evidence |
| 4 | Final evidence-set freeze | Planned | Versioned final included-study register | Each included study appears exactly once with a stable ID and final evidence tier |
| 5 | Evidence integration and data rebuild | Planned | Updated notes, bibliography, matrices, extraction data, and summary counts | All frozen studies pass validation and all generated datasets rebuild successfully |
| 6 | Evidence and citation assurance | Planned | Semantic citation audit, metadata verification, and calibration record | High-impact claims are traceable; metadata issues are resolved or disclosed; calibration is documented |
| 7 | Manuscript completion and quality control | Planned | Submission-ready Markdown, LaTeX, and PDF | All sections are coherent, denominator-based results are current, and the PDF passes visual inspection |
| 8 | Submission package | Not started | Final manuscript and reproducibility package | Submission checklist is complete and the review label matches achieved search coverage |
| 9 | Empirical framework validation | Optional | Annotated evidence layer or controlled mitigation study | A separately scoped study reports protocol, agreement, metrics, and trade-offs |

## Phase Details

### Phase 0 — Protocol and Project Foundations

Status: `Complete`

- [x] Define the review goal and RQ1–RQ6.
- [x] Define core, supporting, and peripheral evidence roles.
- [x] Define eligibility, quality-appraisal, extraction, and synthesis procedures.
- [x] Establish the targeted-structured-review reporting boundary.
- [x] Define the annotation guideline and evaluation schema.

Primary outputs: `method/slr-protocol.md`, `method/slr-data-dictionary.md`, `method/annotation-guideline.md`, and `method/evaluation-schema.md`.

### Phase 1 — Baseline 71-Paper Corpus

Status: `Complete`

- [x] Maintain one authoritative note for each P01–P71 record.
- [x] Complete RQ1–RQ6 extraction and Q1–Q12 appraisal.
- [x] Remove duplicate note identities.
- [x] Validate all 71 notes with the structural gate.
- [x] Generate the study-level and evidence-level datasets.

Primary outputs: `papers/slr-review-progress.md`, `data/slr-extraction.csv`, `data/slr-coding-evidence.csv`, and `data/slr-summary.md`.

### Phase 2 — Initial Synthesis and Manuscript Structure

Status: `Complete`

- [x] Draft the problematic-comment taxonomy.
- [x] Draft the evaluation-dimension map.
- [x] Draft the context-quality model.
- [x] Draft the trade-off framework and research-gap synthesis.
- [x] Create the complete manuscript section structure.
- [x] Integrate P51–P71 evidence into the main synthesis.

Completion here means that all components exist and support the intended argument. It does not mean that the manuscript is submission-ready.

### Phase 3 — Supplementary Search Consolidation

Status: `In progress`

Current focus:

- [x] Complete title/abstract screening for the 293-record arXiv set.
- [x] Complete full-text screening decisions for the 140-record arXiv queue.
- [x] Triage the 30 externally supplied candidate records.
- [x] Validate and log three newly acquired external PDFs.
- [ ] Reconcile all arXiv inclusions with P01–P71, external candidates, and other preprint/publisher versions.
- [x] Generate an initial arXiv-to-corpus reconciliation ledger using exact arXiv-ID and title-similarity matching.
- [x] Generate a provisional queue for the 52 unmatched core candidates with local arXiv metadata.
- [ ] Resolve the eight provisional external inclusions through full-text assessment or a documented access limitation.
- [ ] Resolve the metadata conflict recorded for EXT-0012.
- [ ] Update `method/next-session-todo.md` and search documentation whose counts predate completed screening.
- [ ] Execute or formally close the remaining planned source searches: Semantic Scholar, ACM Digital Library, IEEE Xplore, ScienceDirect, SpringerLink, Google Scholar, and Scopus.
- [ ] Record exact queries, dates, native result counts, deduplication counts, and access limitations for every executed source.

Exit criteria:

- Every identified candidate has one final screening outcome.
- Every included candidate has an accessible and validated full text, or an explicit documented limitation.
- Duplicate and companion relationships are resolved across all discovery routes.
- Search coverage is sufficient for the final claimed review type.

### Phase 4 — Final Evidence-Set Freeze

Status: `Planned`

- [ ] Define whether the submission uses only the baseline corpus or an expanded corpus.
- [ ] Apply an explicit relevance and evidence-weighting rule to the 132 arXiv inclusions.
- [ ] Assign stable P-IDs only to studies accepted into the final evidence set.
- [ ] Treat preprints and published versions as one study unless a documented reason requires separate treatment.
- [ ] Freeze each study as core, supporting, or peripheral exactly once.
- [ ] Produce a final included-study register and final exclusion counts with reasons.
- [ ] Record the freeze date and version or commit identifier.

Exit criteria:

- The final corpus denominator is fixed.
- Every included study has one stable identity, one citation key, one evidence tier, and one provenance trail.
- Reported counts can be regenerated from the frozen set.

### Phase 5 — Evidence Integration and Data Rebuild

Status: `Planned`

- [ ] Create canonical notes for newly included studies using the eleven-section template.
- [ ] Add verified bibliography records to `references/references.bib` without duplicate entries.
- [ ] Update `matrices/paper-pool.md` and `matrices/cross-paper-synthesis.md`.
- [ ] Integrate new evidence into the taxonomy, dimensions, context model, trade-off framework, and research gap.
- [ ] Create `synthesis/final-framework.md` as the consolidated framework specification.
- [ ] Rebuild `data/slr-extraction.csv`, `data/slr-coding-evidence.csv`, and `data/slr-summary.md`.
- [ ] Re-run the note validator and dataset checks.
- [ ] Recalculate RQ1–RQ6 tables using explicit denominators and evidence tiers.

Exit criteria:

- Every frozen study passes the same structural and quality gates.
- Generated datasets and summary tables agree with the final corpus.
- New evidence is integrated analytically rather than appended as paper-by-paper summaries.

### Phase 6 — Evidence and Citation Assurance

Status: `Planned`

- [x] Check that every citation key used in synthesis and draft files exists in `references/references.bib`.
- [ ] Audit literature-based claims sentence by sentence for semantic citation support.
- [ ] Confirm that each citation supports the exact scope and strength of its associated claim.
- [ ] Verify publisher or canonical preprint metadata for unresolved bibliography records.
- [ ] Manually recheck ambiguous, medium-confidence, and high-impact extraction codes.
- [ ] Conduct independent calibration on a documented sample of selection, tier, and extraction decisions.
- [ ] Report agreement, disagreements, resolution procedure, and residual uncertainty.
- [ ] Separate reported evidence, project interpretation, and proposed framework elements throughout the manuscript.

Exit criteria:

- No unsupported literature-based claim remains in the submission draft.
- No invalid citation key or unresolved high-impact metadata error remains.
- Calibration evidence and limitations are reported accurately.

### Phase 7 — Manuscript Completion and Quality Control

Status: `Planned`

- [ ] Reconcile terminology, especially “LLM-generated” versus “LLM-based” code review comments.
- [ ] Add a concise motivating example if it improves the introduction.
- [ ] Align the introduction and contribution statements with `synthesis/final-framework.md`.
- [ ] Expand and connect the discussion, threats-to-validity, and conclusion sections.
- [ ] Replace provisional wording and stale counts throughout the manuscript.
- [ ] Ensure all findings use explicit denominators and distinguish evidence tiers.
- [ ] Copyedit all English prose using `docs/academic-writing-style.md`.
- [ ] Build the LaTeX manuscript from the Markdown sources.
- [ ] Compile and visually inspect the PDF, including tables, citations, references, headings, and page breaks.
- [ ] Run a final consistency check across the abstract, RQs, method, findings, contributions, and conclusion.

Exit criteria:

- The manuscript presents one coherent, corpus-bounded argument.
- All tables, counts, citations, and terminology are internally consistent.
- The generated PDF has no visible formatting or bibliography defects.

### Phase 8 — Submission Package

Status: `Not started`

- [ ] Select the final title and submission venue or course format.
- [ ] Confirm length, format, anonymization, artifact, and citation requirements.
- [ ] Select the defensible final label: targeted structured review or systematic literature review.
- [ ] Archive the protocol, search logs, screening decisions, extraction data, synthesis files, and build instructions.
- [ ] Record unresolved limitations and future work without presenting them as completed evidence.
- [ ] Tag or otherwise identify the exact submission version.

Exit criteria:

- The manuscript and reproducibility package correspond to the same frozen evidence set.
- All venue requirements and the final submission checklist are satisfied.

### Phase 9 — Optional Empirical Framework Validation

Status: `Optional`

This phase is future work and is not required for the current seminar review unless the project scope is expanded explicitly.

- [ ] Select a bounded sample of generated code review comments.
- [ ] Pilot the annotation guideline and revise ambiguous rules.
- [ ] Conduct multi-annotator labeling and report agreement.
- [ ] Evaluate show, suppress, rewrite, and escalate decisions.
- [ ] Measure error reduction together with useful-feedback preservation, coverage, reviewer effort, cost, and evaluator validity.
- [ ] Compare at least one mitigation policy against a transparent baseline.

## Immediate Next Actions

Work should resume in this order:

1. Reconcile the 132 arXiv inclusions against the existing corpus and external candidate list.
2. Resolve the eight provisional external inclusions and the EXT-0012 metadata conflict.
3. Decide and document the final search-coverage boundary.
4. Freeze the evidence set and evidence tiers.
5. Integrate newly accepted evidence and rebuild all generated counts.
6. Complete semantic citation, metadata, and calibration audits.
7. Finish, build, and visually inspect the manuscript.

## Submission Readiness Checklist

- [ ] Final review label is justified by the documented search process.
- [ ] Final corpus and evidence tiers are frozen.
- [ ] All included studies have validated full texts, canonical notes, and bibliography entries.
- [ ] Screening and exclusion counts are reproducible.
- [ ] RQ tables use the final denominator and identify relevant evidence tiers.
- [ ] Literature-based claims have semantically appropriate citations.
- [ ] Publisher or canonical preprint metadata has been checked.
- [ ] Independent calibration has been completed or its absence is disclosed as a limitation.
- [ ] Manuscript terminology and contribution claims are consistent.
- [ ] LaTeX and PDF builds succeed.
- [ ] The final PDF has been visually inspected.
- [ ] Reproducibility files correspond to the submitted manuscript version.

## Decision Log

Add a row when a decision changes the scope, method, evidence set, framework, or reporting position.

| Date | Decision | Rationale | Affected files | Follow-up |
|---|---|---|---|---|
| 2026-08-02 | Retain the targeted-structured-review label | The historical database search and screening trail is unavailable | `README.md`; `method/slr-readiness-audit.md` | Reassess after supplementary source coverage is complete |
| 2026-08-02 | Treat the new search as a dated amendment | A new run can be documented, but it cannot reconstruct the original search | `method/search-protocol-amendment.md`; `data/search/` | Preserve exact queries and source limitations |
| 2026-08-04 | Keep supplementary inclusions separate from the baseline corpus until freeze | Screening inclusion alone does not resolve duplicates, weighting, or final corpus scope | `data/search/arxiv-full-text-screening-reviewed.csv`; `data/search/external-candidate-screening.csv` | Complete Phases 3 and 4 before integration |
| YYYY-MM-DD | _Add decision_ | _Add rationale_ | _Add affected files_ | _Add follow-up_ |

## Progress Log

Add one row after each substantial work session. Keep entries concise and link them to durable outputs.

| Date | Phase | Work completed | Result or evidence | Next action |
|---|---|---|---|---|
| 2026-08-02 | 0–2 | Completed baseline extraction, validation, synthesis integration, and manuscript structure | 71 valid notes; generated extraction and summary files | Execute and document supplementary search |
| 2026-08-04 | 3 | Completed arXiv full-text screening and external-candidate triage; acquired three external PDFs | 132 arXiv includes, 8 excludes; external decisions recorded | Reconcile duplicates and provisional candidates |
| 2026-08-04 | 6 | Audited citation-key integrity across synthesis and draft Markdown files | 64 used keys checked; no missing bibliography key | Perform semantic citation audit after corpus freeze |
| 2026-08-04 | 3 | Synchronized local PDF acquisition, core reconciliation, and extraction checkpoint ledgers | 136 local PDFs no longer marked pending; 52 core records have validated notes; 50 held for final freeze and 2 duplicate/companion records retained | Process supporting records only where full text is available, then freeze the evidence set |
| YYYY-MM-DD | _Phase_ | _Describe completed work_ | _Link output or record result_ | _State the next concrete action_ |

## Known Blockers and Risks

| Item | Type | Current effect | Resolution path |
|---|---|---|---|
| Incomplete native coverage for planned external databases | Search coverage | Blocks a fully reproducible SLR claim | Execute documented searches through authorised access or retain the targeted-review label |
| Eight provisional external inclusions | Evidence access | Prevents final inclusion decisions | Obtain and assess full texts or record explicit access exclusions |
| EXT-0012 metadata conflict | Bibliographic identity | Prevents reliable duplicate and inclusion handling | Resolve title, DOI, and version identity using an authoritative source |
| Large supplementary inclusion set | Scope and workload | Risks an unfocused or weakly weighted corpus | Apply explicit deduplication, relevance, and evidence-weighting rules before integration |
| Independent calibration not completed | Reliability | Limits claims about selection and coding consistency | Calibrate a documented, risk-based sample and report disagreements |
| Recent preprints and changing metadata | Bibliographic validity | May produce stale venue or version information | Verify metadata near submission and record the verification date |

## Definition of Project Completion

The current review project is complete when the evidence set is frozen, all included studies are traceable through screening and extraction, the synthesis and manuscript use the final counts and semantically appropriate citations, metadata and calibration limitations are resolved or disclosed, and the built PDF passes content and visual quality checks. Optional empirical validation is a separate extension and must not delay completion unless it is formally added to the project scope.
