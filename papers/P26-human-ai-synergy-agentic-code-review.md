# P26 — Human-AI Synergy in Agentic Code Review

> [!NOTE]
> Compact v2 analysis. P26 is important for our human-AI workflow and production-proxy arguments because it compares AI-agent and human review comments across 278,790 GitHub conversations and measures adoption plus code-quality effects of suggestions.

## Status

- Paper ID: `P26`
- Analysis status: `First pass completed from PDF; needs citation/BibTeX cleanup`
- Priority: `High`
- Reading depth: `Read once from PDF`
- Confidence: `High`

## Bibliographic Information

| Field | Value |
|---|---|
| Title | Human-AI Synergy in Agentic Code Review |
| Authors | Suzhen Zhong, Shayan Noei, Ying Zou, Bram Adams |
| Year | 2026 |
| Venue / Source | arXiv |
| DOI / arXiv | arXiv:2603.15911 |
| Artifact | GitHub replication package: `Software-Evolution-Analytics-Lab-SEAL/AI_Vs_Human_Codereview` |

```bibtex
```

## One-Sentence Summary

> P26 analyzes 278,790 inline GitHub review conversations and finds that AI agents produce more verbose, narrower, less adopted suggestions than human reviewers, and adopted AI suggestions tend to increase code complexity and size more than human suggestions.

## Main Contribution

The paper studies real agentic code review conversations rather than isolated generated comments. It compares human and AI-agent reviewers across feedback types, interaction patterns, suggestion adoption, and code-quality impact.

## Dataset / Study Context

| Field | Value |
|---|---|
| Projects | 300 open-source GitHub projects |
| PRs | 54,330 closed PRs |
| Conversations | 278,790 inline code review conversations |
| Period | 2022–November 2025 |
| Review categories | HRH, HRA, ARH, ARA |
| AI agents | 16 identified AI-based review bots after manual verification |
| Suggestions | 113,684 conversations with code suggestions |

## Evaluation Method

| RQ | Method |
|---|---|
| RQ1 | Feedback taxonomy classification using GPT-4.1-mini; kappa 0.85 on 383 human-labeled comments; comment-to-code density; average comment count. |
| RQ2 | Interaction sequences modeled as finite state machines; acceptance/rejection by PR merge status. |
| RQ3 | Suggestion adoption detection plus code metric deltas using SciTools Understand over 111 metrics. |

## Key Findings

| Finding | Summary |
|---|---|
| F1 | AI-agent comments focus >95% on Code Improvement and Defect Detection. |
| F2 | Human reviewers provide broader feedback: Understanding, Testing, Knowledge Transfer, Social. |
| F3 | AI-agent reviews are much more verbose: 29.6 tokens per LOC vs 4.1 for HRH. |
| F4 | Understanding feedback in human-initiated reviews triggers the most back-and-forth. |
| F5 | Humans exchange 11.8% more comments when reviewing AI-generated code than human-written code. |
| F6 | 85–87% of AI-agent-initiated reviews end after first comment without follow-up. |
| F7 | Conversations ending with AI-agent responses have higher rejection rates than those ending with human responses. |
| F8 | AI agents generate more code suggestions than humans: 88,011 vs 25,673. |
| F9 | Human suggestions are adopted much more often: 56.5% vs 16.6%. |
| F10 | 28.7% of unadopted AI suggestions are incorrect; 24.0% are fixed differently. |
| F11 | Adopted AI suggestions increase code complexity and code size more than human suggestions. |

## Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Feedback type | Very high | Bacchelli and Bird taxonomy. |
| Verbosity / conciseness | High | Comment-to-code density. |
| Interaction effort | High | Conversation rounds and FSMs. |
| Acceptance/rejection | High | PR merge status and conversation end state. |
| Suggestion adoption | Very high | Adoption detection with line and Jaccard similarity. |
| Code-quality impact | High | 111 code metrics. |
| Project context | High | Knowledge transfer and namespace/build examples. |
| Incorrect suggestions | High | Manual/LLM categorization of unadopted AI suggestions. |
| Workflow impact | Very high | Real GitHub conversations. |

## Problematic Comment / Review Types

- Verbose AI feedback.
- Overly narrow technical feedback missing knowledge transfer.
- Incorrect AI code suggestion.
- Alternative-fix case where AI detects issue but proposes wrong/preferred-unmatched fix.
- Not-needed suggestion.
- Claimed-fixed but not committed suggestion.
- Preference conflict.
- Deferred suggestion.
- AI response that fails to incorporate human feedback.
- Complexity-increasing adopted suggestion.

## Context-Quality Evidence

P26 shows that AI agents often lack project-specific context such as build configurations, namespace conventions, previous review decisions, and renamed classes. This missing context explains low adoption and incorrect defect claims. It also shows that useful review requires social/project understanding, not only code-level inspection.

## Trade-off Extraction

| Strategy / Signal | Benefit | Risk / Cost |
|---|---|---|
| AI-agent review | Scales defect screening and code-improvement suggestions. | Verbose, narrow, lower adoption, higher incorrectness. |
| Human final response | Associated with lower rejection. | Requires human effort. |
| Code suggestion adoption | Stronger workflow signal than comment existence. | Adoption may reflect preference, time, or trust. |
| Code metric deltas | Measures downstream code effects. | Metrics may not capture semantic quality/security. |
| Agent-generated code review | Helps scale code production/review. | Human reviews AI code require more interaction rounds. |

## Relevance to Our Paper

P26 is a major source for workflow-aware and trade-off-aware evaluation. It supports our claim that reducing harmful comments is not enough: AI review must be evaluated by adoption, interaction cost, project-context fit, code-quality impact, and human oversight needs.

## Limitations from Our Perspective

- GitHub public projects only; enterprise workflows may differ.
- AI-agent identification depends on release dates and account classification.
- Human accounts may include AI-assisted comments.
- PR merge status is a proxy for conversation outcome.
- Code metric changes do not fully capture maintainability, correctness, or security.
- Rapidly evolving agent capabilities may change results.

## Follow-up TODOs

- [ ] Add adoption and code-quality impact dimensions to `synthesis/evaluation-dimensions.md`.
- [ ] Add verbose/narrow/incorrect/complexity-increasing AI suggestions to taxonomy.
- [ ] Add human-AI interaction and final-human-oversight trade-offs to framework.
- [ ] Update `matrices/cross-paper-synthesis.md` with P26 evidence.
## Legacy proposal-aligned quality appraisal (superseded by the canonical record)

P26 is **Core / High relevance**. It supports RQ1 through verbose, narrow, incorrect, and complexity-increasing suggestions; RQ2–RQ3 through human–AI interaction and code-quality impact; RQ4 through automation, adoption, interaction cost, and oversight trade-offs; and RQ6 through workflow-aware framework design.

**Quality score: 21/24.** Q1–Q7=2, Q8=1, Q9=2, Q10=2, Q11=1, Q12=2. Human-AI synergy findings may be context-specific and should not be generalized without comparable settings.
## Canonical citation record

Use citation key `p26_zhong2026_human_ai_synergy` from `references/references.bib`; do not duplicate its BibTeX entry in this note.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p26_zhong2026_human_ai_synergy`; Core; Include; High relevance.
- Study overview: Agentic code review evaluated through human-AI interaction, feedback types, adoption, and code-quality outcomes.
- RQ1: Verbose, narrow, incorrect, and complexity-increasing AI suggestions (Reported).
- RQ2: Project context, interaction, and human oversight (Reported).
- RQ3: Adoption, interaction cost, verbosity, code quality, and human oversight (Reported).
- RQ4: Automation/adoption versus interaction cost, trust, and oversight (Reported).
- RQ5: Human annotation, workflow validity, and socio-technical context (Reported).
- RQ6: Strong workflow-aware mitigation framework support.
- Failure taxonomy: verbose; narrow; incorrect; complexity-increasing; non-adopted feedback.
- Metrics: adoption, interaction, comment density, code quality, human oversight, and feedback categories.
- Mitigation/trade-off: agentic collaboration/human oversight; adds interaction and review burden but may improve coverage.
- Validity: production/project context and adoption proxies require careful interpretation.
- Quality: 21/24; high-quality core evidence.
- Synthesis conclusion: supports evaluating downstream human interaction, not only comment correctness.

### 1. Identification
- P26; `p26_zhong2026_human_ai_synergy`; local full PDF; included; authoritative record.
### 2. Screening and proposal alignment
- Include as Core. `p26_zhong2026_human_ai_synergy`; Core; Include; High relevance.
### 3. Study overview
Agentic code review evaluated through human-AI interaction, feedback types, adoption, and code-quality outcomes.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Verbose, narrow, incorrect, and complexity-increasing AI suggestions (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Project context, interaction, and human oversight (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Adoption, interaction cost, verbosity, code quality, and human oversight (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Automation/adoption versus interaction cost, trust, and oversight (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Human annotation, workflow validity, and socio-technical context (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Strong workflow-aware mitigation framework support. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| verbose | Reported/Inferred | Full PDF |
| narrow | Reported/Inferred | Full PDF |
| incorrect | Reported/Inferred | Full PDF |
| complexity-increasing | Reported/Inferred | Full PDF |
| non-adopted feedback. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| adoption | Not an end-to-end outcome | Full PDF |
| interaction | Not an end-to-end outcome | Full PDF |
| comment density | Not an end-to-end outcome | Full PDF |
| code quality | Not an end-to-end outcome | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: agentic collaboration/human oversight; adds interaction and review burden but may improve coverage.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: partial; useful-issue retention after intervention is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- production/project context and adoption proxies require careful interpretation.
- Q7–Q8 encode judging and reliability depth.
### 9. Quality appraisal
| Criterion | Score | Evidence note |
|---|---:|---|
| Q1 | 2 | goal at scored depth. |
| Q2 | 2 | artifact at scored depth. |
| Q3 | 2 | dataset/context at scored depth. |
| Q4 | 2 | procedure at scored depth. |
| Q5 | 2 | metrics at scored depth. |
| Q6 | 2 | failures at scored depth. |
| Q7 | 2 | judging at scored depth. |
| Q8 | 1 | reliability at scored depth. |
| Q9 | 2 | intervention at scored depth. |
| Q10 | 2 | trade-offs at scored depth. |
| Q11 | 1 | threats at scored depth. |
| Q12 | 2 | SLR support at scored depth. |
- Total: 22/24; reporting-quality score.
### 10. Review-process reliability and bias
- Missing preservation/escalation evidence and selection/publication bias remain explicit; second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: Agentic code review evaluated through human-AI interaction, feedback types, adoption, and code-quality outcomes.
- Boundary: supports evaluating downstream human interaction, not only comment correctness.
