# P28 — Support, Not Automation: Towards AI-supported Code Review for Code Quality and Beyond

> [!NOTE]
> Compact v2 analysis. P28 is a position/vision paper, not an empirical benchmark. It is important because it frames AI in code review as support for human reviewers rather than full automation, preserving non-code-quality benefits of review.

## Status

- Paper ID: `P28`
- Analysis status: `First pass completed from PDF; needs citation/BibTeX cleanup`
- Priority: `Medium`
- Reading depth: `Read once from PDF`
- Confidence: `High`

## Bibliographic Information

| Field | Value |
|---|---|
| Title | Support, Not Automation: Towards AI-supported Code Review for Code Quality and Beyond |
| Authors | Lo Heander, Emma Söderberg, Christofer Rydenfält |
| Year | 2025 |
| Venue / Source | FSE Companion 2025 |
| DOI | 10.1145/3696630.3728505 |

```bibtex
```

## One-Sentence Summary

> P28 argues that AI should support code review rather than automate it, because code review provides socio-technical benefits such as knowledge transfer, team awareness, shared ownership, and rationale tracking that can be lost under full automation.

## Main Contribution

The paper proposes an AI-agent-based architecture for an adaptive code review platform that collects information from tools such as version control, issue trackers, requirements databases, CI, API documentation, and team processes to support reviewers throughout the workflow.

## Core Argument

Code review is not only defect finding. Based on prior code review literature, it also supports:

- code improvement,
- alternative-solution discovery,
- knowledge transfer,
- team awareness,
- shared code ownership,
- rationale tracking,
- process improvement,
- team assessment.

Full automation risks preserving only the code-quality dimension while losing team-learning and coordination benefits.

## Proposed Architecture

| Component | Role |
|---|---|
| Central LLM | Coordinates the review workflow, interprets user input, plans, and orchestrates agents. |
| Specialized agents | Integrate with VCS, issue trackers, requirements DBs, CI, API docs, and project knowledge. |
| User/team configuration | Encodes reviewer preferences and team review process. |
| Familiar review UI | Keeps GitHub/GitLab/Gerrit-like interface central, with AI support in sidebars/below. |
| Adaptive workflow | Customizes support by role, review goal, experience level, and context. |

## Key Claims

| Claim | Summary |
|---|---|
| C1 | Developers spend roughly 10–20% of work time on code review, so optimization matters. |
| C2 | Modern code review has several benefits beyond defect finding. |
| C3 | Full automation can lose interpersonal and team benefits. |
| C4 | AI agents can reduce mental load by gathering scattered review context. |
| C5 | AI can support defect finding, alternative solutions, rationale discovery, and knowledge transfer without taking the final decision away from humans. |
| C6 | Human approval/rejection decisions preserve accountability and shared ownership. |
| C7 | The field lacks a unified way to measure code review effectiveness beyond defect finding. |

## Evaluation Dimensions Suggested by the Paper

| Dimension | Why It Matters |
|---|---|
| Knowledge transfer | Review exposes developers to unfamiliar code and reduces turnover risk. |
| Team awareness | Review keeps developers aware of ongoing work. |
| Shared ownership | Review distributes responsibility and mitigates blame culture. |
| Rationale tracking | Review connects implementation to issues, product plans, meetings, and team discussions. |
| Reviewer mental load | AI should reduce tool-switching and information-gathering burden. |
| User need fit | Review support should vary by author/reviewer/expert/newcomer/gatekeeper role. |
| Human accountability | Final decision should remain with humans. |

## Problematic Comment / Review Types

- AI-generated review that replaces human interaction and removes learning opportunities.
- Review automation that preserves defect finding but loses rationale/knowledge/team-awareness benefits.
- AI support that ignores user role and experience level.
- AI support that hides or over-summarizes important project rationale.
- Tool design that increases rather than reduces context-switching.

## Context-Quality Evidence

P28 broadens the definition of review context. Useful context includes not just code and diffs, but also requirements, issue tracker items, CI results, API docs, team process, reviewer goals, rationale, architecture, performance profile, and user experience.

## Trade-off Extraction

| Strategy | Benefit | Risk / Cost |
|---|---|---|
| Full automation | Saves reviewer time and may preserve code-quality checks. | Loses knowledge transfer, team awareness, ownership, accountability. |
| AI-supported review | Reduces mental load while preserving human judgment. | Requires careful UX, orchestration, and user-specific adaptation. |
| Multi-agent architecture | Can gather scattered context from many tools. | Integration complexity and risk of information overload. |
| Human-in-the-loop | Preserves accountability and shared ownership. | Does not eliminate review effort completely. |

## Relevance to Our Paper

P28 is useful for positioning: our evaluation framework should not assume that the goal of LLM code review is full automation. It should measure support quality, human attention, learning, rationale, team awareness, and preservation of human value.

## Limitations from Our Perspective

- Vision/position paper; no empirical system evaluation.
- Architecture is high-level and not implemented.
- Does not provide concrete metrics for non-code-quality benefits.
- Does not directly evaluate LLM-generated comments.

## Follow-up TODOs

- [ ] Add socio-technical review benefits to evaluation dimensions.
- [ ] Add human-support-not-replacement framing to synthesis.
- [ ] Add knowledge-transfer/team-awareness preservation to trade-off framework.
- [ ] Update `matrices/cross-paper-synthesis.md` with P28 evidence.
## Legacy proposal-aligned quality appraisal (superseded by the canonical record)

P28 is **Supporting / High relevance**. It supports RQ1 through risks of over-automation and low-value feedback; RQ2–RQ3 through knowledge transfer, accountability, awareness, and review value; RQ4 through support versus automation and human-escalation trade-offs; and RQ5–RQ6 through socio-technical framework design.

**Quality score: 18/24.** Q1–Q5=2, Q6=1, Q7=1, Q8=1, Q9=1, Q10=2, Q11=1, Q12=2. It is primarily a conceptual/supporting paper rather than a controlled evaluation study.
## Canonical citation record

Use citation key `p28_heander2025_support_not_automation` from `references/references.bib`; do not duplicate its BibTeX entry in this note.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p28_heander2025_support_not_automation`; Supporting; Include; High relevance.
- Study overview: Conceptual and socio-technical argument for AI-supported rather than fully automated code review.
- RQ1: Over-automation, low-value feedback, and loss of knowledge-transfer functions (Reported/Our perspective).
- RQ2: Team context, rationale, awareness, and accountability (Reported).
- RQ3: Human oversight, learning, shared ownership, and workflow value (Reported).
- RQ4: Support versus automation, human escalation, accountability, and reviewer burden (Reported).
- RQ5: Socio-technical validity and human-centered evaluation (Reported).
- RQ6: Strong conceptual framework support.
- Failure taxonomy: low-value; over-automated; context-insensitive; accountability-losing feedback.
- Metrics: proposed workflow/usefulness dimensions; no new benchmark metrics.
- Mitigation/trade-off: human-supported automation; preserves oversight but may retain cost and delay.
- Validity: conceptual/supporting evidence, not controlled empirical mitigation.
- Quality: 18/24; supporting evidence.
- Synthesis conclusion: supports human escalation and socio-technical dimensions in the framework.

### 1. Identification
- P28; `p28_heander2025_support_not_automation`; local full PDF; included; authoritative record.
### 2. Screening and proposal alignment
- Include as supporting. `p28_heander2025_support_not_automation`; Supporting; Include; High relevance.
### 3. Study overview
Conceptual and socio-technical argument for AI-supported rather than fully automated code review.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Over-automation, low-value feedback, and loss of knowledge-transfer functions (Reported/Our perspective). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Team context, rationale, awareness, and accountability (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Human oversight, learning, shared ownership, and workflow value (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Support versus automation, human escalation, accountability, and reviewer burden (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Socio-technical validity and human-centered evaluation (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Strong conceptual framework support. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| low-value | Reported/Inferred | Full PDF |
| over-automated | Reported/Inferred | Full PDF |
| context-insensitive | Reported/Inferred | Full PDF |
| accountability-losing feedback. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| proposed workflow/usefulness dimensions | Not an end-to-end outcome | Full PDF |
| no new benchmark metrics. | Not an end-to-end outcome | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: human-supported automation; preserves oversight but may retain cost and delay.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: partial; useful-issue retention after intervention is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- conceptual/supporting evidence, not controlled empirical mitigation.
- Q7–Q8 encode judging and reliability depth.
### 9. Quality appraisal
| Criterion | Score | Evidence note |
|---|---:|---|
| Q1 | 2 | goal at scored depth. |
| Q2 | 2 | artifact at scored depth. |
| Q3 | 2 | dataset/context at scored depth. |
| Q4 | 2 | procedure at scored depth. |
| Q5 | 2 | metrics at scored depth. |
| Q6 | 1 | failures at scored depth. |
| Q7 | 1 | judging at scored depth. |
| Q8 | 1 | reliability at scored depth. |
| Q9 | 1 | intervention at scored depth. |
| Q10 | 2 | trade-offs at scored depth. |
| Q11 | 1 | threats at scored depth. |
| Q12 | 2 | SLR support at scored depth. |
- Total: 19/24; reporting-quality score.
### 10. Review-process reliability and bias
- Missing preservation/escalation evidence and selection/publication bias remain explicit; second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: Conceptual and socio-technical argument for AI-supported rather than fully automated code review.
- Boundary: supports human escalation and socio-technical dimensions in the framework.
