# Review Method

## Review Design

We conducted a targeted structured literature review with a documented supplementary search amendment. The method covers question definition, eligibility assessment, quality appraisal, data extraction, thematic synthesis, and reporting. It draws on software-engineering SLR guidance, while taxonomy construction and reliability planning draw on established taxonomy and agreement methods [@m01_nickerson2013_taxonomy; @m02_cohen1960_kappa; @m03_krippendorff2018_content_analysis]. The method does not reconstruct the search for the historical baseline.

### Goal definition

Following a Goal--Question--Metric structure, the review goal is defined as follows:

- **Purpose:** analyze and characterize;
- **Issue:** evaluation and mitigation trade-offs;
- **Object:** LLM-generated and automated code review comments and their evaluation instruments; and
- **Viewpoint:** researchers and tool builders designing reliable code-review evaluation.

Five review questions refine this goal, while the extraction fields identify the evidence required to answer each question. Framework derivation is treated separately as a traceability objective rather than as a research question, because the framework is an author-derived synthesis artifact.

## Review Questions

<!-- table: first-column-width="0.55in" -->
| RQ | Question |
|---|---|
| RQ1 | Which problematic-comment types and failure categories have been reported? |
| RQ2 | Which evaluation dimensions have been used for correctness, grounding, relevance, usefulness, actionability, context quality, and evaluator validity? |
| RQ3 | Which mitigation families have been proposed or evaluated, and where do they intervene? |
| RQ4 | What evidence exists about error reduction versus useful-feedback preservation, coverage, escalation, and cost? |
| RQ5 | How are context quality, dataset validity, and annotation difficulty treated? |

Table \ref{tab:rq-traceability} links each question to its evidence and synthesis path. The unit for all frequency counts is the included study unless a result names a different denominator.

<!-- table: caption="Traceability from review questions to evidence and reported outputs." label="tab:rq-traceability" longtable="true" -->
| RQ | Eligibility scope | Extracted fields | Unit of analysis | Synthesis method | Reported output | Principal validity limitation |
| --- | --- | --- | --- | --- | --- | --- |
| RQ1 | Direct or supporting evidence about problematic review feedback or related failure modes | failure categories, evidence status, evidence location | study-level presence of coded evidence | controlled-vocabulary tabulation and thematic grouping | failure-frequency table and proposed taxonomy | source studies use different labels; comment-level prevalence is not estimated |
| RQ2 | Studies evaluating comment quality, workflow outcomes, context, or evaluator behavior | evaluation dimensions, artifact, context, evaluator type | study-level presence of an evaluated construct | frequency tabulation and construct synthesis | evaluation-dimension table and construct map | definitions and measurement protocols differ across studies |
| RQ3 | Studies proposing or evaluating an intervention relevant to review feedback | mitigation family, intervention point, reported outcomes | study-level presence of a mitigation family | intervention-point classification | mitigation-family table and strategy map | frequency does not establish comparative effectiveness |
| RQ4 | Studies reporting preservation, coverage, escalation, or cost | reporting-availability fields and evidence status | study-level reporting availability within the stated corpus or subset | descriptive counts and sensitivity analysis | trade-off availability and subset tables | missing reporting is not a zero effect; effect sizes are not pooled |
| RQ5 | Studies addressing context, dataset, annotation, or judge validity | context types, data validity, annotation, evaluator-validity evidence | study-level coded evidence and cross-study theme | thematic synthesis and context-frequency tabulation | context-validity synthesis and framework qualifications | coding is single-reviewer and adjacent evidence requires transfer judgment |

### Framework-traceability objective

For each taxonomy category, annotation decision, and framework layer, we record whether support is direct code-review evidence, supporting evidence, or a bounded transfer from peripheral evidence. This mapping documents derivation; it is not treated as independent validation of the proposed framework.

## Search Scope and Corpus Assembly

The review protocol identified ACM Digital Library, IEEE Xplore, ScienceDirect, SpringerLink, arXiv, Semantic Scholar, Google Scholar, and Scopus where available, with a primary focus on work from 2021 onward and earlier foundational modern-code-review studies. Query families covered LLM code review, automated review, generated comments, evaluation metrics, hallucination and grounding, context-aware review, LLM-as-a-Judge, and human--AI review.

The synthesis corpus contains 121 unique full-text studies. It combines a 71-study historical baseline with 50 unique core studies admitted through a dated supplementary amendment. The historical set is treated as an assembled corpus, not as the output of a reproducible search flow. We report verified corpus and amendment counts and leave unavailable historical identification-stage counts as `NR`.

### Dated supplementary amendment and corpus closure

The amendment began with arXiv because its public API returned exact-query results and stable retrieval counts. Searches of ACM Digital Library, IEEE Xplore, ScienceDirect, and SpringerLink were attempted, but the available environment did not expose complete result sets. Semantic Scholar returned a rate-limit response, while Google Scholar and Scopus were not searched without a documented manual or institutional-access route. A later export from five external sources served only as a partial cross-check because it omitted native result totals and was not exhaustive. The amendment improves recency coverage, but it does not replace the missing historical search or provide complete multi-database coverage.

The arXiv search was executed on 2 August 2026 for records submitted from 1 January 2021 through 2 August 2026. Table \ref{tab:arxiv-queries} reports the exact API queries. The raw API responses and screening decisions were retained during the review process but are not included with this PDF.

<!-- table: caption="Exact queries used in the dated arXiv amendment." label="tab:arxiv-queries" longtable="false" first-column-width="0.9in" -->
| Query (retrieved) | Exact arXiv query |
| --- | --- |
| Q1 (200) | `(ti:"code review" OR abs:"code review") AND (ti:"large language model" OR abs:"large language model" OR ti:LLM OR abs:LLM) AND submittedDate:[202101010000 TO 202608022359]` |
| Q2 (61) | `(ti:"review comment" OR abs:"review comment") AND (ti:"large language model" OR abs:"large language model" OR ti:LLM OR abs:LLM) AND submittedDate:[202101010000 TO 202608022359]` |
| Q3 (156) | `(ti:"code review" OR abs:"code review") AND (all:hallucination OR all:grounding OR all:context) AND submittedDate:[202101010000 TO 202608022359]` |

The three result sets contained 417 raw records. Deduplication by arXiv identifier removed 124 cross-query repetitions while preserving every matching query identifier, leaving 293 unique records. Conservative title/abstract screening assigned one of four outcomes: include for full text, exclude, duplicate/companion, or uncertain. The controlled exclusion vocabulary was `out of scope`, `no review-feedback connection`, `insufficient method/evaluation`, `duplicate/companion`, `non-English`, `inaccessible`, and `supporting-only methodology`. This stage retained 140 records for full-text assessment, excluded 116, and identified 37 duplicate or likely companion records.

Full-text inclusion required a recorded decision, inclusion group, eligibility criterion, evidence location, rationale, reviewer, and screening date. Of the 140 assessed records, 132 were retained for consideration and eight were excluded. Fifty-three retained records met core criteria. One matched a baseline study and two represented duplicate or companion identities, leaving 50 unique additions to the corpus. A core candidate entered the final corpus only after its identity, eligibility decision, evidence record, and bibliographic entry were complete.

The remaining 79 records form the supporting reserve: 53 have substantive provisional extraction, 16 have scaffolds only, and ten have no extraction packet. They are not included in the 121-study denominator. Inaccessible records without enough evidence for classification were excluded; seven access-limited records from the later external export remain metadata-only and outside the frozen corpus.

An external 30-record export was screened separately after corpus closure. Reconciliation found 20 duplicates, two full-text candidates retained outside the closed corpus, seven access-limited metadata-only candidates, and one exclusion. The external export therefore contributes no study to the 121-study denominator. Candidate-level decisions are not included with this PDF.

<!-- table: caption="Accounting of the baseline corpus and dated search amendment." label="tab:corpus-flow-audit" -->
| Source | Identified | Full text assessed | Corpus records contributed | Reserve or post-closure | Overlaps or duplicate identities | Access-limited |
|---|---:|---:|---:|---:|---:|---:|
| Historical baseline | NR | 71 | 71 | 0 | NR | NR |
| Dated arXiv amendment | 293 | 140 | 50 | 79 supporting: 53 substantive, 16 scaffolds, 10 without packets | 3 core identities | 0 |
| External cross-check export | 30 | 3 | 0 | 2 full-text candidates | 20 | 7 |

The rows are not additive identification stages: the external export is a post-closure cross-check and overlaps the baseline and arXiv records. The corpus arithmetic is therefore `71 + 50 = 121`.

Figure \ref{fig:corpus-assembly-flow} summarizes the documented corpus arithmetic. It is not a complete PRISMA flow diagram because identification and exclusion records for the historical baseline were not retained.

<!-- figure: path="figures/corpus_assembly_flow.tex" caption="Corpus assembly and supplementary search amendment. The 79-record supporting reserve and 30-record external cross-check remain outside the 121-study synthesis corpus." label="fig:corpus-assembly-flow" -->

## Eligibility and Evidence Tiers

Core eligibility covered LLM-based, AI-assisted, or automated code review; generated review comments or PR feedback; code-review benchmarks and rubrics; relevant failure types; and mitigation through prompting, filtering, retrieval, verification, tool support, rewriting, or escalation. Supporting eligibility covered evaluator validity, human review, workflow value, annotation, context quality, and methodological foundations. General code generation or repair without a review connection was excluded unless retained as explicitly bounded peripheral evidence.

The synthesis corpus assigns 91 studies to the core tier, 24 to supporting evidence, and six to peripheral evidence. These tiers indicate argumentative role, not methodological quality. The 24 supporting studies in the corpus completed the same structured extraction as the core studies. The 79 reserve studies did not: 53 have substantive but provisional packets, 16 have scaffolds only, and ten lack packets. Mixing this partial coding with standardized study records would make quantitative counts non-comparable. Their exclusion is therefore based on extraction completeness rather than timing alone.

## Quality Appraisal

The initial protocol specified eight criteria scored from 0 (`not reported`) to 2 (`clearly reported`). During extraction calibration on 1 August 2026, before the final standardized extraction pass and corpus-wide quantitative synthesis, the instrument was expanded to 12 items. The amendment separated broad criteria that otherwise combined review relevance, trade-off reporting, workflow consequences, and evaluator validity. All 121 included studies were subsequently scored with the same 12-item instrument, yielding a maximum of 24 points.

This amendment improves field-level consistency but introduces retrospective design risk: the finer categories were informed by issues encountered during review preparation rather than fixed in the initial protocol. We therefore report it as a protocol amendment dated 1 August 2026, retain criterion-level evidence, and do not use the total score as a mechanical inclusion threshold. Evidence tier and confidence remain separate from methodological appraisal.

## Data Extraction

Each included study has one structured extraction record derived from its available full text. Records contain bibliographic identity, screening decision, study design, RQ1--RQ5 evidence, traceability, quality appraisal, trade-off and evaluator-validity fields, evidence locations, and unresolved verification items. All 121 records pass the same completeness check. Extraction was performed by one reviewer; the validator checks required fields and controlled values but does not test whether another reviewer would make the same judgments.

Independent agreement was not measured. A future validation step should assign a random 10--20% sample to a second reviewer for blind eligibility screening and extraction of the principal fields. It should report raw agreement and Cohen's kappa for inclusion decisions, and Krippendorff's alpha for the core failure label, usefulness, actionability, context quality, and handling decision. Disagreements should be adjudicated before any revised rules are applied to affected records. This procedure is proposed future work, not part of the completed review.

<!-- table: caption="Study-level data items and their use in the review." label="tab:data-items" -->
| Data-item group | Fields | Use |
|---|---|---|
| Bibliographic | study identity, title, year, venue, publication type | Corpus demographics |
| Evidence weighting | evidence tier, decision, relevance, quality score, confidence | Framework traceability and validity |
| Review artifact | context types, evaluated artifact, evaluator types | RQ2 and RQ5 |
| Failure coding | problematic-comment and related failure categories | RQ1 |
| Evaluation coding | quality, workflow, cost, and evaluator-validity dimensions | RQ2 |
| Mitigation coding | family and intervention point | RQ3 |
| Trade-off reporting | preservation, coverage, escalation, and cost availability | RQ4 |
| Method validity | annotation, limitations, and RQ evidence status | RQ5 and framework traceability |

The main field definitions and controlled labels used in the synthesis are described in the manuscript.

## Synthesis

We used tabulation, thematic grouping, and framework mapping. We did not pool incompatible metrics. Initial categories were derived during cross-study synthesis and normalized into controlled vocabularies for failure types, evaluation dimensions, mitigation families, and context types. A deterministic transformation procedure produced one study-level record per included study, retained multi-valued controlled labels, and used `NR` when the extraction did not contain enough evidence. The resulting counts therefore describe coded evidence in the reviewed studies, not the prevalence of failures in deployed systems.

Consistency checks ensured that each included study occurred once, evidence tiers did not overlap, admitted supplementary studies received the intended tier, citations resolved, and appraisal scores were available. Findings were organized by research question. Every reported count uses the 121-study evidence pool as its denominator unless another denominator is stated.

### Supporting-reserve sensitivity analysis

We separately mapped the bounded synthesis claims in the 53 substantively extracted reserve packets to five framework-level themes defined before the mapping: evaluation or evaluator validity, context or grounding quality, annotation or dataset validity, human-review or workflow value, and trade-off or mitigation design. This directional analysis asks whether the reserve would require a new top-level component for RQ2, RQ5, or framework traceability. It does not compare effect sizes or add reserve records to the 121-study frequency tables. All 53 packets mapped to at least one existing theme: 26 to evaluation or evaluator validity, 25 to context or grounding quality, two to annotation or dataset validity, 29 to human-review or workflow value, and 23 to trade-off or mitigation design. No new top-level component was required. Because the mapping was conducted by the same reviewer and 26 reserve candidates lack substantive extraction, this result provides a bounded robustness check rather than evidence that the reserve cannot alter lower-level categories or relative emphasis.

## Protocol Deviations and Amendments

The main deviation is retrospective protocol formalization: the baseline corpus was assembled before the complete search log was available. The 12-item appraisal instrument was introduced during extraction calibration on 1 August 2026, replacing the broader eight-item protocol rubric before the final standardized scoring pass. Evidence-tier assignment was added after full-text extraction to prevent indirect studies from receiving the same argumentative weight as direct code-review studies. The dated arXiv run is a separate search amendment and does not reconstruct the historical search. The external export is partial, and seven otherwise relevant records remain outside the frozen corpus because verified full text was unavailable. Any future database-search rerun must be dated and reported as a further amendment rather than described as if it preceded corpus assembly.
