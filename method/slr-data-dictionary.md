# SLR Data Dictionary

This dictionary defines the study-level fields used to answer RQ1--RQ5 and the separate framework-traceability objective. One row in `data/slr-extraction.csv` represents one authoritative P01--P121 record. Multi-valued fields use semicolon-separated controlled labels. `NR` means that the authoritative note lacks the expected field or does not contain enough evidence to determine applicability; it does not mean zero or absence in the underlying study. For RQ4 reporting fields, `no` means that the standardized extraction identified no measurement or reporting of the outcome in the available full text. Publication-facing tables label these states as `Unclear or not applicable` and `No extractable evidence identified`, respectively.

| ID | CSV field | Meaning | Review use |
|---|---|---|---|
| F01 | `paper_id` | Stable project identifier | Traceability |
| F02 | `citation_key` | Key in `references/references.bib` | Traceability |
| F03 | `title` | Bibliographic title | Demographics |
| F04 | `year` | Publication year from bibliography | Demographics |
| F05 | `venue` | Journal, booktitle, or publication source | Demographics |
| F06 | `publication_type` | Journal, conference, preprint, or other | Demographics |
| F07 | `evidence_tier` | Core, Supporting, or Peripheral | Framework traceability and evidence weighting |
| F08 | `decision` | Include, supporting inclusion, or exclusion state in the note | Selection audit |
| F09 | `relevance` | High, Medium, Low, or compound label | Evidence weighting |
| F10 | `quality_score` | Q1–Q12 total on a 0–24 scale | Quality summary |
| F10a | `rq4_independent_appraisal_score` | Q1–Q9 plus Q11 reporting and methodological appraisal on a 0–20 scale; excludes Q10 and Q12 | RQ4 sensitivity analysis |
| F11 | `confidence` | Extraction confidence from the progress log | Reliability |
| F12 | `context_types` | Controlled context categories evidenced in the note | RQ5 |
| F13 | `failure_types` | Controlled problematic-comment/failure categories | RQ1 |
| F14 | `evaluation_dimensions` | Controlled quality or validity constructs | RQ2 |
| F15 | `mitigation_families` | Controlled mitigation/evaluation mechanisms | RQ3 |
| F16 | `intervention_points` | Before generation, during generation, after generation, or before display | RQ3 |
| F17 | `preservation_reported` | Whether useful-feedback preservation is substantively reported | RQ4 |
| F18 | `coverage_reported` | Whether review/issue coverage is substantively reported | RQ4 |
| F19 | `escalation_reported` | Whether human escalation policy/rate is substantively reported | RQ4 |
| F20 | `cost_reported` | Whether computational, latency, reviewer, or workflow cost is reported | RQ4 |
| F21 | `annotation_reported` | Whether a human annotation/user-study protocol is reported | RQ5 |
| F22 | `evaluator_types` | Human, LLM judge, automatic metric, tool/execution, or none reported | RQ2/RQ5 |
| F23 | `limitations_reported` | Whether study/review limitations are substantively recorded | RQ5 and validity |
| F24–F28 | `rq1_evidence`–`rq5_evidence` | Reported, inferred/mixed, perspective-only, NR, or present | RQ completeness |
| F29 | `rq6_evidence` | Legacy field retained as the framework-traceability projection | Framework derivation |
| F30 | `source_note` | Authoritative Markdown record | Auditability |

## Controlled Coding Rules

The extraction script searches only the authoritative numbered sections of each note. It uses conservative phrase families and records `NR` when no phrase family is found. A positive code means that the note contains evidence for the category; it does not mean that the paper evaluated the category as a primary outcome.

### Failure types

`unsupported_or_hallucinated`, `incorrect_claim`, `irrelevant`, `wrong_location_or_cause`, `vague_or_generic`, `non_actionable`, `low_value_or_nitpick`, `redundant`, `invalid_fix`, `severity_miscalibration`, `context_dependent`, `spurious_or_false_positive`, `missed_issue_or_false_negative`, `adversarial_or_bias`.

### Evaluation dimensions

`correctness`, `grounding`, `relevance`, `usefulness`, `actionability`, `specificity`, `explanation_quality`, `context_quality`, `coverage`, `acceptance_or_adoption`, `workflow_impact`, `cost_or_latency`, `evaluator_validity`, `security_validity`, `repair_validity`, `efficiency_validity`, `lexical_similarity`.

### Mitigation families

`data_cleaning`, `prompting`, `fine_tuning`, `retrieval_or_rag`, `context_gate`, `specification_grounding`, `static_analysis_hybrid`, `routing`, `multi_agent`, `verification_or_critic`, `filtering_or_suppression`, `rewriting`, `human_escalation`, `reward_optimization`, `benchmark_or_rubric`, `adversarial_defense`.

### Context types

`diff_or_hunk`, `file_or_function`, `pr_or_issue`, `repository_or_project`, `retrieved_history`, `specification_or_documentation`, `static_analysis_or_tool`, `reviewer_or_workflow`, `execution_or_test`, `adversarial_context`.

## Reproducibility Boundary

The dataset is a deterministic projection of the current notes, not a replacement for manual coding. Changes to phrase families can change counts and must be reviewed as protocol amendments. Before publication, ambiguous and high-impact categories should be manually audited against the source notes and PDFs.
