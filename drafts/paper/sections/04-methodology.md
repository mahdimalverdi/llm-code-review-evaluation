# Review Method

## Review Design

We conducted a targeted structured literature review using documented multi-source search streams. The method covers question definition, eligibility assessment, quality appraisal, data extraction, thematic synthesis, and reporting. It draws on software-engineering SLR guidance [@m00_kitchenham2007_slr_guidelines], while taxonomy construction and reliability planning draw on established taxonomy and agreement methods [@m01_nickerson2013_taxonomy; @m02_cohen1960_kappa; @m03_krippendorff2018_content_analysis].

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

The review protocol identified ACM Digital Library, IEEE Xplore, ScienceDirect, SpringerLink, arXiv, Semantic Scholar, Google Scholar, and Scopus where available, with a primary focus on work from 2021 onward and earlier foundational modern-code-review studies. Query families covered LLM code review, automated review, generated comments, evaluation metrics, hallucination and grounding, context-aware review, LLM-as-a-Judge, and human--AI review. Only the arXiv stream produced a complete, retained result set with reproducible counts. The other sources contributed partial discovery or attempted searches and must not be interpreted as completed database searches.

The synthesis corpus contains 121 unique full-text studies identified across arXiv, OpenAlex, Crossref, publisher indexes, and general scholarly-web search. Separate topic families covered direct code review, generated comments, evaluator validity, modern code review, surveys, security, refinement, efficiency, and industrial evidence. Every included study was verified as retrievable through at least one topic-level query without using its title, identifier, system name, or author name as the query. All included studies subsequently underwent the same eligibility, extraction, evidence-tier, and appraisal procedure.

### Search execution and corpus closure

The principal reproducible run began with arXiv because its public API returned exact-query results and stable retrieval counts. Topic-level searches in OpenAlex, Crossref, publisher indexes, and the scholarly web broadened coverage for adjacent and foundational evidence. Complete native result sets were not available from every publisher index, and Semantic Scholar access was rate-limited. A later export from five external sources therefore served as a partial cross-check rather than an independent denominator.

The arXiv search was executed on 2 August 2026 for records submitted from 1 January 2021 through 2 August 2026. Table \ref{tab:arxiv-queries} reports the exact API queries. The raw API responses and screening decisions were retained during the review process but are not included with this PDF.

<!-- table: caption="Exact queries used in the reproducible arXiv search stream." label="tab:arxiv-queries" longtable="false" first-column-width="0.9in" -->
| Query (retrieved) | Exact arXiv query |
| --- | --- |
| Q1 (200) | `(ti:"code review" OR abs:"code review") AND (ti:"large language model" OR abs:"large language model" OR ti:LLM OR abs:LLM) AND submittedDate:[202101010000 TO 202608022359]` |
| Q2 (61) | `(ti:"review comment" OR abs:"review comment") AND (ti:"large language model" OR abs:"large language model" OR ti:LLM OR abs:LLM) AND submittedDate:[202101010000 TO 202608022359]` |
| Q3 (156) | `(ti:"code review" OR abs:"code review") AND (all:hallucination OR all:grounding OR all:context) AND submittedDate:[202101010000 TO 202608022359]` |

Table \ref{tab:source-search-status} reports the execution status of every source named in the protocol. Blank counts denote unavailable result sets, not zero results.

<!-- table: caption="Execution status of the planned search sources on 2 August 2026." label="tab:source-search-status" longtable="false" -->
| Source | Exact executed or attempted query | Result status |
|---|---|---|
| arXiv | Q1--Q3 in Table \ref{tab:arxiv-queries} | Complete retained run: 417 raw, 293 unique |
| Semantic Scholar | `("LLM" OR "large language model") AND ("code review" OR "review comment" OR "pull request review")` | Graph API returned HTTP 403 on 6 August 2026; count unavailable |
| ACM Digital Library | `"code review" AND "large language model"` | Cloudflare Turnstile blocked direct and headless-browser runs; count unavailable |
| IEEE Xplore | `"code review" AND "large language model"` | Official search routes timed out from the current network; count unavailable |
| ScienceDirect | `"code review" AND "large language model"` | Official search route timed out from the current network; count unavailable |
| SpringerLink | `"code review" AND "large language model"` | Official search route timed out from the current network; count unavailable |
| Google Scholar | `"code review" "large language model"` | Google refused the automated request; manual run required |
| Scopus | `TITLE-ABS-KEY("code review" AND "large language model")` | Scopus API timed out; authenticated or institutional run required |

The retained partial export contained 38 source rows from ACM Digital Library, IEEE Xplore, ScienceDirect, SpringerLink, and Semantic Scholar, which reconciled to 30 candidate records. Because native totals and complete result sets were unavailable, this export is a cross-check rather than a reproducible database-search denominator.

The three result sets contained 417 raw records. Deduplication by arXiv identifier removed 124 cross-query repetitions while preserving every matching query identifier, leaving 293 unique records. Conservative title/abstract screening assigned one of four outcomes: include for full text, exclude, duplicate/companion, or uncertain. The controlled exclusion vocabulary was `out of scope`, `no review-feedback connection`, `insufficient method/evaluation`, `duplicate/companion`, `non-English`, `inaccessible`, and `supporting-only methodology`. This stage retained 140 records for full-text assessment, excluded 116, and identified 37 duplicate or likely companion records.

Full-text inclusion required a recorded decision, inclusion group, eligibility criterion, evidence location, rationale, reviewer, and screening date. Of the 140 records assessed in the arXiv stream, 132 were retained for consideration and eight were excluded. Fifty-three retained records met core criteria; identity reconciliation found one overlap with the existing candidate pool and two duplicate or companion identities. A candidate entered the final corpus only after its identity, eligibility decision, evidence record, and bibliographic entry were complete.

The remaining 79 records form the supporting reserve: 53 have substantive provisional extraction, 16 have scaffolds only, and ten have no extraction packet. They are not included in the 121-study denominator. Inaccessible records without enough evidence for classification were excluded; seven access-limited records from the later external export remain metadata-only and outside the frozen corpus.

An external 30-record export was screened separately after corpus closure. Reconciliation found 20 duplicates, two full-text candidates retained outside the closed corpus, seven access-limited metadata-only candidates, and one exclusion. The external export therefore contributes no study to the 121-study denominator. The two eligible full-text candidates were not incorporated because the corpus had already been frozen, but corpus closure was not specified prospectively. Their exclusion is therefore a post hoc boundary and a threat to selection validity. Candidate-level decisions are retained in the replication package.

<!-- table: caption="Accounting of the unified corpus and auxiliary candidate sets." label="tab:corpus-flow-audit" -->
| Record set | Identified or retained | Full text assessed | Included in synthesis corpus | Outside corpus |
|---|---:|---:|---:|---:|
| Unified synthesis corpus | 121 | 121 | 121 | 0 |
| Reproducible arXiv stream | 293 unique | 140 | Reconciled into unified corpus | 79 supporting-reserve records |
| External cross-check export | 30 | 3 | Reconciled into unified corpus | 2 post-closure candidates; 20 duplicates; 7 access-limited; 1 exclusion |

The rows are not additive because the search streams overlap and are reconciled by study identity. The synthesis denominator is the 121 unique studies that passed the unified eligibility and extraction procedure.

Figure \ref{fig:corpus-assembly-flow} summarizes the unified corpus assembly and the auxiliary records retained outside its denominator.

<!-- figure: path="figures/corpus_assembly_flow.tex" caption="Unified corpus assembly. Overlapping multi-source search streams were reconciled into 121 included studies; the supporting reserve and external cross-check remain outside the synthesis denominator." label="fig:corpus-assembly-flow" -->

## Eligibility and Evidence Tiers

Core eligibility covered LLM-based, AI-assisted, or automated code review; generated review comments or PR feedback; code-review benchmarks and rubrics; relevant failure types; and mitigation through prompting, filtering, retrieval, verification, tool support, rewriting, or escalation. Supporting eligibility covered evaluator validity, human review, workflow value, annotation, context quality, and methodological foundations. General code generation or repair without a review connection was excluded unless retained as explicitly bounded peripheral evidence.

The synthesis corpus assigns 91 studies to the core tier, 24 to supporting evidence, and six to peripheral evidence. These tiers indicate argumentative role, not methodological quality. The 24 supporting studies in the corpus completed the same structured extraction as the core studies. The 79 reserve studies did not: 53 have substantive but provisional packets, 16 have scaffolds only, and ten lack packets. Mixing this partial coding with standardized study records would make quantitative counts non-comparable. Their exclusion is therefore based on extraction completeness rather than timing alone.

## Quality Appraisal

The quality-appraisal instrument contains 12 criteria scored from 0 (`not reported`) to 2 (`clearly reported`). The complete definitions, scoring rules, and interpretation limits are provided in the supplementary rubric. Its final calibration on 1 August 2026 separated review relevance, trade-off reporting, workflow consequences, and evaluator validity. All 121 included studies were scored with this same instrument, yielding a maximum of 24 points. Criterion-level scores and evidence notes are retained in the study records. The total is descriptive and does not represent a validated quality scale or an inclusion threshold.

Because the final categories were calibrated during review preparation, we retain criterion-level evidence and do not use the total score as a mechanical inclusion threshold. Evidence tier and confidence remain separate from methodological appraisal.

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

Consistency checks ensured that each included study occurred once, evidence tiers did not overlap, included studies received the intended tier, citations resolved, and appraisal scores were available. Findings were organized by research question. Every reported count uses the 121-study evidence pool as its denominator unless another denominator is stated.

### Supporting-reserve sensitivity analysis

We separately mapped the bounded synthesis claims in the 53 substantively extracted reserve packets to five framework-level themes defined before the mapping: evaluation or evaluator validity, context or grounding quality, annotation or dataset validity, human-review or workflow value, and trade-off or mitigation design. This directional analysis asks whether the reserve would require a new top-level component for RQ2, RQ5, or framework traceability. It does not compare effect sizes or add reserve records to the 121-study frequency tables. All 53 packets mapped to at least one existing theme: 26 to evaluation or evaluator validity, 25 to context or grounding quality, two to annotation or dataset validity, 29 to human-review or workflow value, and 23 to trade-off or mitigation design. No new top-level component was required. Because the mapping was conducted by the same reviewer and 26 reserve candidates lack substantive extraction, this result provides a bounded robustness check rather than evidence that the reserve cannot alter lower-level categories or relative emphasis.

## Protocol Consolidation

The search documentation was consolidated retrospectively; however, all included studies were subsequently verified against the unified eligibility, extraction, and appraisal procedure. The 12-item appraisal instrument was finalized during extraction calibration on 1 August 2026, before the standardized corpus-wide scoring pass. Evidence-tier assignment distinguishes direct from supporting and peripheral evidence. Seven otherwise relevant records remain outside the frozen corpus because verified full text was unavailable. Any future search rerun will be dated and reported as an update to the consolidated protocol. RQ4 separates quantitative measurement, qualitative evaluation, limitation/design mention, and review inference; only the first two are treated as measured or evaluated evidence.
