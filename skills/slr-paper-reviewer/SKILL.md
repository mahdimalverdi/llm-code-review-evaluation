---
name: slr-paper-reviewer
description: Review individual research papers for a systematic literature review on trade-off-aware evaluation of LLM-based code review. Use when given a paper, PDF, DOI, URL, or paper note and asked to screen, extract, summarize, assess quality, map evidence to review questions, or prepare a structured SLR record.
---

# SLR paper reviewer

Review one paper at a time and produce a traceable record that can later be synthesized into the proposed SLR, **“Literature Review Proposal on Trade-off-aware Evaluation of LLM-based Code Review.”** The proposal defines the review scope and outputs; Kitchenham's *Guidelines for Performing Systematic Literature Reviews in Software Engineering* (EBSE-2007-01, version 2.3) defines the review process. Follow the repository instructions and `docs/academic-writing-style.md` when writing English prose.

## Workflow

1. Identify the paper and record complete bibliographic metadata. Do not invent missing fields; mark them `Not reported`.
2. Read the full paper when available. If only an abstract or metadata is available, state the limitation and do not present inferred details as reported evidence.
3. Apply the protocol's search, selection, and study-classification logic. Decide `Include`, `Include as supporting`, or `Exclude`; give a concise reason and record the selection stage.
4. Extract evidence relevant to RQ1–RQ6. Separate every claim into `Reported`, `Inferred`, or `Our perspective`, and attach page/section/table/figure locations whenever possible.
5. Apply the predefined quality instrument below. Score only what the paper reports, not what can be guessed. Pilot or calibrate the instrument before reviewing the full corpus and periodically check consistency.
6. Map the paper to taxonomy categories, evaluation dimensions, mitigation families, trade-offs, and research gaps. Distinguish direct evidence from contextual relevance.
7. Record missing data, ambiguous reporting, duplicate publications, and possible publication bias. Link companion papers when multiple papers use the same dataset or experiment.
8. Write or update one Markdown note under `papers/` using the repository’s existing paper-note convention. Preserve paper IDs and citation keys. Do not edit synthesis files during single-paper review unless explicitly requested.
9. End with a short synthesis-ready summary: what this paper contributes, what it does not establish, and which SLR RQs it supports.

## Proposal research questions

Map each paper to these exact questions; do not replace them with generic summaries:

- **RQ1:** Which problematic-comment types and failure categories have been reported for LLM-generated or automated code review comments?
- **RQ2:** Which evaluation dimensions have prior studies used to judge correctness, grounding, relevance, usefulness, actionability, context quality, and evaluator validity?
- **RQ3:** Which mitigation families have been proposed or evaluated, and where do they intervene: before generation, during generation, after generation, or before display?
- **RQ4:** What evidence exists about mitigation trade-offs, especially error reduction versus useful-feedback preservation, review coverage, human escalation, and computational or operational cost?
- **RQ5:** How have studies treated context quality, context inconsistency, dataset validity, and annotation difficulty?
- **RQ6:** Which papers, systems, datasets, benchmarks, or methodological references directly support the planned taxonomy, annotation protocol, mitigation-family design, and trade-off analysis?

The review should support three proposal deliverables: an operational taxonomy of problematic comments, a structured annotation protocol, and a multi-dimensional trade-off-aware evaluation framework.

## Proposal screening scope

Classify papers using the proposal’s two inclusion groups:

- **Core:** LLM-based, AI-assisted, or automated code review; generated comments or pull-request feedback; code-review benchmarks, metrics, rubrics, or evaluation frameworks; hallucination, grounding, context quality, usefulness, actionability, relevance; or mitigation such as prompting, filtering, gating, verification, retrieval, static-analysis support, rewriting, or human escalation.
- **Supporting:** LLM-as-a-Judge/evaluator validity in software engineering; human–AI interaction and workflow impact; reviewer burden/usefulness; annotation, inter-annotator agreement, taxonomy, empirical-SE, or review-protocol methodology; and foundational modern-code-review concepts.

Exclude general code generation without review relevance, program repair or vulnerability detection without a review-feedback connection, papers lacking usable method/evaluation evidence, non-research blog/tutorial/opinion material, non-English papers, and papers whose method or evaluation cannot be identified. Record the exact exclusion reason.

## Quality rubric

Score each item 0, 1, or 2. This is a project-specific quality instrument derived for the review; it must be fixed in the protocol before full extraction:

- Q1: research goal/questions are clear
- Q2: evaluated system or artifact is specified
- Q3: dataset, benchmark, and input context are described
- Q4: generation/evaluation procedure is reproducible enough to understand
- Q5: evaluation dimensions or metrics are defined
- Q6: failure/problematic-comment categories are reported
- Q7: human or automated judging protocol is described
- Q8: reliability or validity checks are reported
- Q9: mitigation or intervention is evaluated, if applicable
- Q10: trade-offs are measured rather than merely mentioned
- Q11: limitations and threats to validity are discussed
- Q12: evidence directly supports the SLR framework or research questions

Report total `/24`, but do not use the total as a substitute for judgment:

- 19–24: high-quality core evidence
- 13–18: relevant evidence with limitations
- 7–12: supporting/background evidence
- 0–6: normally exclude, unless uniquely relevant

Also record relevance separately as `High`, `Medium`, or `Low`. A methodologically weak paper can still be relevant background; a high-quality but unrelated paper should not become a core study.

For review reliability, use the same interpretation across papers, record disagreements or uncertain scores, and if a second reviewer is available, independently assess a sample and calculate inter-rater agreement. Do not silently change the instrument after seeing results; log protocol amendments.

## Required note structure

Use the template in `references/paper-review-template.md`. At minimum include:

- citation and screening decision;
- selection stage, source/database, search string or citation-chaining route, and duplicate-publication status;
- study purpose, method, artifact, dataset, and context;
- findings mapped to RQ1–RQ6;
- problematic-comment/failure taxonomy;
- evaluation dimensions and metrics;
- mitigation and intervention point;
- trade-off evidence, including useful-feedback preservation, coverage, escalation, and cost;
- evaluator/annotation validity and limitations;
- quality scores with evidence notes;
- missing-data and publication-bias observations;
- direct quotations only when necessary and short; otherwise paraphrase;
- synthesis-ready contribution and gap statement.

## Evidence discipline

Never treat a paper’s motivation or future work as empirical evidence. Mark claims that are inferred. Preserve citation keys from `references/references.bib`; if none exists, use a temporary `TODO_CITATION_KEY` and flag it for later resolution. Do not duplicate BibTeX entries in paper notes.

For papers outside LLM-based code review, include them only as supporting methodology or context and explain the boundary. Do not silently broaden the SLR corpus.

## Input handling

- For a local PDF, extract text and inspect tables/figures where needed; retain page numbers.
- For a DOI or URL, use the authoritative paper or publisher source when available.
- For an existing note, improve traceability and completeness without erasing valid existing evidence.
- If the paper cannot be accessed, create a screening record only and list the missing evidence needed before inclusion.
