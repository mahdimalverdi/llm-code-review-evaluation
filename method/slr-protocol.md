# Systematic Literature Review Protocol

## Review scope

This review synthesizes evidence on trade-off-aware evaluation of LLM-based, AI-assisted, and automated code review. It focuses on problematic generated comments, evaluation dimensions, mitigation intervention points, context and dataset validity, evaluator validity, and consequences for useful-feedback preservation, review coverage, human escalation, and operational cost.

The protocol follows Kitchenham’s software-engineering SLR process: planning, study identification, selection, quality assessment, data extraction, synthesis, and reporting.

## Research questions

1. Which problematic-comment types and failure categories have been reported for LLM-generated or automated code review comments?
2. Which evaluation dimensions have prior studies used to judge correctness, grounding, relevance, usefulness, actionability, context quality, and evaluator validity?
3. Which mitigation families have been proposed or evaluated, and where do they intervene: before generation, during generation, after generation, or before display?
4. What evidence exists about mitigation trade-offs, especially error reduction versus useful-feedback preservation, review coverage, human escalation, and computational or operational cost?
5. How have studies treated context quality, context inconsistency, dataset validity, and annotation difficulty?
6. Which papers, systems, datasets, benchmarks, or methodological references directly support the planned taxonomy, annotation protocol, mitigation-family design, and trade-off analysis?

## Eligibility criteria

### Core inclusion

Include studies that address LLM-based, AI-assisted, or automated code review; generated review comments or PR feedback; code-review benchmarks/metrics/rubrics; hallucination, grounding, context quality, usefulness, actionability, relevance; or mitigation through prompting, filtering, gating, verification, retrieval, static-analysis support, rewriting, or human escalation.

### Supporting inclusion

Include studies on LLM-as-a-Judge/evaluator validity in software engineering; human-AI review workflows; reviewer burden/usefulness; annotation, agreement, taxonomy, empirical-SE, or review-protocol methodology; and foundational modern-code-review concepts.

### Exclusion

Exclude general code generation without review relevance; program repair or vulnerability detection without a review-feedback connection; papers without identifiable methods/evaluation; non-research opinion/tutorial material; non-English studies; and inaccessible studies lacking enough evidence for classification.

## Search and selection

The proposal specifies the following search sources: ACM Digital Library, IEEE Xplore, Elsevier ScienceDirect, SpringerLink, arXiv, Semantic Scholar, Google Scholar, and Scopus where available. The planned initial publication focus is 2021 onward, with earlier modern-code-review and empirical-methodology studies included when they provide foundational concepts for evaluation, taxonomy, annotation, or workflow analysis.

The proposal’s keyword families are: `LLM code review`, `automated code review`, `code review comment generation`, `generated code review comments`, `LLM-based code review`, `AI code review`, `code review automation`, `code review evaluation`, `review comment quality`, `LLM-as-a-Judge software engineering`, `hallucination in code review`, `context-aware code review`, `retrieval-augmented code review`, `human-AI code review`, and `software engineering evaluation`. Record the exact database-specific query for every search.

The proposal provides these query patterns for adaptation to each database syntax:

- (`LLM` OR `large language model`) AND (`code review` OR `review comment` OR `pull request review`)
- (`automated code review` OR `code review automation`) AND (`evaluation` OR `benchmark` OR `metric` OR `rubric`)
- (`code review comment generation` OR `generated review comments`) AND (`quality` OR `usefulness` OR `actionability` OR `relevance`)
- (`LLM` OR `large language model`) AND (`hallucination` OR `grounding` OR `context`) AND (`code review` OR `software engineering`)
- (`LLM-as-a-Judge` OR `LLM judge`) AND (`software engineering` OR `code review` OR `coding tasks`)
- (`human-AI` OR `AI-assisted` OR `AI-supported`) AND (`code review` OR `pull request review`)

The proposal requires recording database name, search string, search date, retrieved count, screened count, included count, and exclusion reason. Use these fields in the search log; do not infer counts from the local PDF folder.

The current corpus contains 71 locally available PDFs. Because the original database retrieval counts and screening history are not fully preserved, report this corpus as a targeted structured review unless the search log is reconstructed.

Selection stages are identification, duplicate removal, title/abstract screening, full-text eligibility, and evidence-tier assignment. Record exclusion reasons and companion publications.

### Evidence tiers and weighting

Included records are assigned one of three synthesis roles:

- **Core:** direct evidence about generated review comments, review agents, code-review benchmarks, or mitigation in the review workflow.
- **Supporting:** evidence about human review, evaluator validity, annotation, context, workflow, or closely related security/static-analysis settings.
- **Peripheral:** adjacent code-generation, refinement, misalignment, or non-functional evidence used only for bounded background claims.

Evidence tier is independent of methodological quality. A high-quality adjacent study remains peripheral for review-specific claims, while a lower-scoring direct study can remain core but should be interpreted cautiously. Report denominators by tier and by availability of the extracted field. The working assignment is maintained in `matrices/paper-pool.md`.

## Quality assessment

The proposal defines a 0–2 scale: `0 = not reported`, `1 = partially reported`, and `2 = clearly reported`. Its eight primary criteria are evaluated artifact, input context, dataset/benchmark/corpus, evaluation dimensions/metrics, human or automated judging protocol, reliability checks, limitations/threats to validity, and evidence about usefulness/actionability/grounding/preservation/escalation/cost. The project’s expanded 12-item instrument in `skills/slr-paper-reviewer/SKILL.md` subdivides these criteria for consistent paper-level extraction; it must not be presented as the proposal’s original rubric. Record criterion-level evidence and distinguish reported evidence from inference. Do not use the total score alone to determine inclusion.

## Data extraction

Use `skills/slr-paper-reviewer/references/paper-review-template.md`. Extract the proposal’s required fields: source and full reference; title, authors, year, venue; citation/reference counts when available; article type/topic; purpose/method; evaluated system/benchmark/artifact; dataset/input context; metrics and quality dimensions; reported failure types; mitigation approach; human annotation/judging; limitations/future work; and relevance to taxonomy, annotation protocol, mitigation design, and trade-off framework.

## Synthesis plan

Use tabulation, thematic grouping, and framework mapping as specified in the proposal. Produce: a thematic map of research streams; a summary of failure types; a comparison of evaluation dimensions and their limitations; a paper-to-framework mapping matrix; mitigation families classified by intervention point; a gap analysis; summaries of useful-feedback preservation, false suppression, coverage, escalation, cost, and evaluator/annotation risks; and open research directions. Keep core evidence separate from supporting and peripheral evidence. Do not pool incompatible metrics quantitatively. Every numerical summary must define its denominator, and every literature-derived category must retain paper-level traceability.

## Amendments and limitations

The corpus was assembled before a complete search log was available. This is a protocol limitation and must be reported. The current note set has undergone a full-text structural uniformity pass, but structural validation is not independent reviewer agreement. Under the proposal’s reporting note, the result remains a targeted structured review until all search sources, dates, counts, selection decisions, quality scores, and extraction records are complete. Any later search rerun is a protocol amendment and must be dated rather than presented as if it preceded corpus assembly.
