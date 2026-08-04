# P110 — Rethinking Code Review Workflows with LLM Assistance: An Empirical Study

## 1. Identification

| Field | Value |
|---|---|
| Project ID | `P110` |
| Citation key | `p110_a_alsteinsson2025_rethinking_code_review_workflo` |
| Authors | Fannar Steinn Aðalsteinsson; Björn Borgar Magnússon; Mislav Milicevic; Adam Nirving Davidsson; Chih-Hong Cheng |
| Year | 2025 |
| Source | arXiv preprint, `2505.16339v1` |
| Study type | Industrial qualitative field study and field experiment |

## 2. Screening

- **Scope decision:** Include as core evidence for workflow integration, context needs, interaction modes, trust, and human-AI collaboration.
- **Task:** Support practicing developers during pull-request review with RAG-based summaries and on-demand assistance.
- **Evidence boundary:** The study emphasizes developer experience and preferences rather than objective defect-detection accuracy or accepted fixes.
- **Metadata caveat:** Publisher/duplicate status and the provisional BibTeX record require verification.

## 3. Study overview

The study has two phases at WirelessCar Sweden. Phase 1 uses semi-structured interviews with seven participants to characterize current review practices and AI opportunities. Phase 2 is a field experiment with ten developers, each reviewing two pull requests using two modes: Mode A, an AI-led co-reviewer that proactively summarizes changes and concerns, and Mode B, an interactive assistant queried on demand. Both use semantic search/RAG to gather relevant project context. Post-review interviews and observation notes are analyzed thematically. Participants generally prefer the AI-led mode for large or unfamiliar pull requests, while preferences depend on code familiarity, severity, trust, false positives, and interface latency.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Interviews identify context switching, insufficient context, review fatigue, and opportunities for summaries and contextual assistance. | Reported | Phase 1 |
| RQ2 | Developers compare proactive AI-led review with on-demand interactive assistance; AI-led review is generally preferred for large/unfamiliar changes. | Reported | Phase 2 |
| RQ3 | Participants report faster understanding, greater thoroughness, trust concerns, false positives, unclear findings, and interface/latency limitations. | Reported | Phase 2 themes |
| RQ4 | Semantic search/RAG retrieves relevant code, requirements, source files, and project artifacts to support context. | Reported | Tool design |
| RQ5 | Adaptive interaction—proactive summaries for unfamiliar work and on-demand control for familiar/critical work—is proposed as the main mitigation. | Inferred/proposed | Discussion |
| RQ6 | The study uses interviews, observations, thematic analysis, rotated mode assignment, and real review settings, but no objective correctness or agreement metric is reported. | Reported/limitation | Methodology |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| False positives | Assistant surfaces issues that are incorrect, low-priority, or not useful. | Reported participant concern | Phase 2 |
| Context insufficiency | Review lacks broader architectural, requirement, or codebase context. | Reported workflow problem | Phase 1; discussion |
| Trust miscalibration | Reviewers either distrust useful output or risk over-relying on AI-led suggestions. | Reported concern | Phase 2 |
| Information overload | Summaries or many findings create noise and can obscure important issues. | Reported concern | Phase 2 |
| Interface/latency friction | Output presentation or slow responses disrupt the review flow. | Reported concern | Phase 2 |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Workflow efficiency | Developer perceptions of faster understanding and reduced effort | Positive reports, but no timed causal comparison is reported. | Phase 2 |
| Review thoroughness | Participant perception of coverage and contextual insight | AI-led mode is viewed as helpful, especially for large/unfamiliar PRs. | Phase 2 |
| Interaction preference | Qualitative comparison of Mode A and Mode B | Mode A generally preferred; Mode B useful for familiar or high-control contexts. | Phase 2 |
| Trust | Interview themes about reliability, over-reliance, and confidence | Trust is conditional and requires verification. | Phase 2 |
| Context quality | Relevance of retrieved project artifacts and explanations | RAG addresses context gaps, but retrieval accuracy is not quantitatively measured. | Tool design |
| Usability | Interface, integration, concision, and response-time feedback | Familiar IDE/GitHub/Slack integration and low latency are desired. | Discussion |

## 7. Mitigation and trade-offs

- **Mitigation family:** RAG context retrieval, proactive summaries, on-demand querying, and embedding assistance in existing developer environments.
- **Intervention point:** Workflow interaction and contextual grounding rather than model training.
- **What it reduces:** Context switching, orientation time, and difficulty understanding large pull requests.
- **Useful feedback potentially lost:** Proactive summaries may anchor reviewers on highlighted issues and cause them to miss unhighlighted concerns.
- **Coverage:** RAG improves access to relevant artifacts but depends on retrieval quality and available project documentation.
- **Human escalation:** Human reviewers remain responsible; the preferred mode changes with familiarity and pull-request severity.
- **Cost:** Deployment requires retrieval infrastructure, interface integration, and response-time optimization; exact costs are not reported.
- **New failure modes:** Anchoring, automation bias, irrelevant retrieval, false positives, unclear output, and latency-related abandonment.

## 8. Annotation and evaluator validity

- **Participants:** Seven interviewees in Phase 1 and ten developers in Phase 2, spanning engineering, security, and QA roles across teams.
- **Sampling:** Convenience recruitment through internal Slack announcements; only some Phase 1 participants returned for Phase 2.
- **Design controls:** Each Phase 2 participant reviewed two comparable pull requests, used both modes, and mode assignment was rotated to reduce ordering effects.
- **Analysis:** Semi-structured interviews, observation notes, and thematic analysis; saturation was reported after seven Phase 1 interviews.
- **Validity limitations:** Small single-company sample, self-reported perceptions, no formal inter-rater agreement, and no objective review-quality oracle.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Research questions and workflow focus are explicit. |
| Q2 | 2 | Industrial setting and participant roles are described. |
| Q3 | 2 | Two modes, RAG design, tasks, and data collection are detailed. |
| Q4 | 1 | Qualitative experience dimensions are reported without objective metrics. |
| Q5 | 1 | Interview guide and thematic method are described, but rubric detail is limited. |
| Q6 | 0 | No formal agreement statistic is reported. |
| Q7 | 1 | Both modes are compared within participants, but sample is small. |
| Q8 | 1 | Real-work setting, but one company and convenience sample. |
| Q9 | 2 | Interaction modes and contextual retrieval directly address observed needs. |
| Q10 | 1 | Latency/interface concerns are reported, not quantified. |
| Q11 | 2 | Trust, false positives, anchoring, context, and workflow trade-offs are explicit. |
| Q12 | 2 | Direct evidence from practicing developers in real review conditions. |

**Total: 17/24 — useful industrial experience evidence, with limited quantitative and external validity.**

## 10. Review-process reliability and bias

- **Selection bias:** Convenience recruitment and a single company may favor participants already willing to use AI.
- **Expectation effects:** Participants knew the study purpose and may have adapted behavior during the field experiment.
- **Construct limitation:** Preference and perceived usefulness do not establish correctness or productivity benefit.
- **Mode confounding:** Differences may reflect proactive versus reactive interaction, presentation, or PR assignment rather than model capability.
- **Missing outcomes:** No accepted-fix rate, review time measurement, comment-level correctness, or long-term adoption is reported.
- **External validity:** Findings may transfer to workflow design principles, but not directly to other organizations, languages, or criticality levels.

## 11. Synthesis-ready conclusion

- P110 shows that effective LLM code-review assistance is a workflow and context-design problem, not only a model-quality problem.
- Proactive AI-led summaries are particularly useful for large or unfamiliar pull requests, while on-demand interaction preserves control in familiar or high-severity work.
- Trust, false positives, anchoring, and latency determine whether contextual assistance is accepted.
- The study supports adaptive human-AI collaboration and RAG-based context grounding, but does not establish objective review correctness or productivity gains.
- Use as core experience evidence for workflow integration, interaction preferences, and human escalation design.

