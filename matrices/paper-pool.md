# Paper Pool

| ID | Paper | Priority | Status | Main Use |
|---|---|---|---|---|
| P01 | DeepCRCEval | High | First pass completed; migrated to v2 | Evaluation dimensions; critique of text similarity |
| P02 | HalluJudge | High | First pass completed; migrated to v2 | Hallucination; context alignment; safeguard/gate framing |
| P03 | RovoDev Code Reviewer | High | First pass completed; migrated to v2 | Industrial deployment; workflow metrics; quality gates |
| P04 | SWE-PRBench | High | First pass completed; migrated to v2; needs PDF-level verification | PR-level benchmark; context degradation evidence |
| P05 | SWRBench | High | First pass completed; migrated to v2; needs PDF-level verification | PR-centric benchmark; full project context; structured ground truth |
| P06 | ContextCRBench | High | First pass completed; migrated to v2; needs PDF-level verification | Enriched semantic/code context; fine-grained evaluation; data-quality critique |
| P07 | RevMate user study | High | First pass completed; migrated to v2; needs PDF-level verification | Live user study; acceptance; perceived value; reviewer time overhead |
| P08 | Too Noisy To Learn | High | First pass completed; needs PDF-level verification | Data quality; noisy/vague/non-actionable comments; semantic cleaning |
| P09 | Hydra-Reviewer | High | First pass completed; needs PDF-level verification | Multi-agent mitigation; comprehensiveness; vagueness/incorrectness; cost/latency |
| P10 | BitsAI-CR | High | First pass completed from PDF; needs citation/BibTeX cleanup | Industrial deployment; RuleChecker/ReviewFilter; Outdated Rate; data flywheel; precision-vs-recall trade-off |
| P11 | LAURA | High | First pass completed from PDF; needs citation/BibTeX cleanup | RAG/context-enriched review generation; context augmentation; retrieval exemplars; I/IH/M-Score |
| P12 | SGCR | High | First pass completed from PDF; needs citation/BibTeX cleanup | Specification-grounded review; explicit/implicit paths; trustworthiness; adoption rate; rule traceability |
| P13 | Prompting and Fine-tuning LLMs for Code Review | High | First pass completed from PDF; needs citation/BibTeX cleanup | Prompting vs QLoRA fine-tuning; call graph/summary augmentation; metric validity; human qualitative evaluation |
| P14 | CodeReviewer | High | First pass completed from PDF; needs citation/BibTeX cleanup | Foundational baseline; CodeReview dataset; diff-hunk representation; BLEU critique; information/relevance human evaluation |
| P15 | LLaMA-Reviewer | Medium / High | First pass completed from PDF; needs citation/BibTeX cleanup | PEFT/resource-aware adaptation; LoRA vs prefix tuning; input representation; threshold trade-offs |
| P16 | Context-Aware Code Review Automation | Medium / High | First pass completed from PDF; needs citation/BibTeX cleanup | RAG/context-aware review; context collapse; hybrid expert routing; hallucination/severity overestimation |
| P17 | CodeReviewQA | High | First pass completed from PDF; needs citation/BibTeX cleanup | Comprehension probes; CTR/CL/SI; contamination-aware benchmark; clean manual curation |
| P18 | Harnessing LLMs for Curated Code Reviews | Medium / High | First pass completed from PDF; needs citation/BibTeX cleanup | Data curation; relevance/clarity/conciseness/civility; LLM-as-judge calibration; downstream gains |
| P19 | Fine-Grained Review Comment Classification | Low / Medium | First pass completed from PDF; needs citation/BibTeX cleanup | 17-category taxonomy; usefulness-linked categories; LLM classification; code-context and class-imbalance trade-offs |
| P20 | RAG-Reviewer | Medium / High | First pass completed from PDF; needs citation/BibTeX cleanup | Retrieval-augmented comment generation; pair vs singleton exemplars; low-frequency-token coverage; k/token-budget trade-offs |
| P21 | iCodeReviewer | High | First pass completed from PDF; needs citation/BibTeX cleanup | Secure code review; mixture-of-prompts; prompt expert routing; CWE category/location; I/H/M/U; production acceptance |
| P22 | Combining LLMs with Static Analyzers | High | First pass completed from PDF; needs citation/BibTeX cleanup | Static analyzer + LLM hybrid review; DAT/RAG/NCO; accuracy/coverage trade-offs; LLM-as-judge calibration |
| P23 | Leveraging Reviewer Experience | High | First pass completed from PDF; needs citation/BibTeX cleanup | Reviewer experience as data-quality signal; ELF; applicability; informativeness; issue-type usefulness |
| P24 | Reward Models for Code Review Comment Generation | Medium / High | First pass completed from PDF; needs citation/BibTeX cleanup | RL/reward-guided comment generation; semantic reward; downstream code-refinement reward; LLM-as-judge usefulness |
| P25 | Carllm | High | First pass completed from PDF; needs citation/BibTeX cleanup | Comprehensible ACR; issue detection/localization/explanation/repair suggestion; CoT data curation; balanced loss |
| P26 | Human-AI Synergy in Agentic Code Review | High | First pass completed from PDF; needs citation/BibTeX cleanup | Human-vs-AI agent review; feedback diversity; interaction patterns; suggestion adoption; code-quality impact |
| P27 | From Industry Claims to Empirical Reality | Medium / High | First pass completed from PDF; needs citation/BibTeX cleanup | Code review agents in PRs; CRA-only vs human-only outcomes; signal-to-noise ratio; abandonment risk |
| P28 | Support, Not Automation | Medium | First pass completed from PDF; needs citation/BibTeX cleanup | AI-supported code review; human-in-the-loop; knowledge transfer; team awareness; shared ownership |
| P29 | Can LLMs Replace Human Evaluators? | High | First pass completed from PDF; needs citation/BibTeX cleanup | LLM-as-a-judge validity in SE; task dependence; pairwise instability; verbosity/order bias |
| P30 | CodeUltraFeedback | Medium / High | First pass completed from PDF; needs citation/BibTeX cleanup | Coding preferences; LLM-as-a-judge preference data; SFT/DPO alignment; judge-selection sensitivity |
| P31 | CodeJudgeBench | High | First pass completed from PDF; needs citation/BibTeX cleanup | Coding-task judge benchmark; thinking judges; position bias; source-model/preprocessing sensitivity |
| P32 | Bias in the Loop | High | First pass completed from PDF; needs citation/BibTeX cleanup | SE-specific LLM-as-judge bias audit; prompt perturbation; answer rate; A/B swap; consistency |
| P33 | LLM-as-a-Judge for Software Engineering Survey | High | First pass completed from PDF; needs citation/BibTeX cleanup | SE-specific judge survey; lifecycle artifact taxonomy; uncertainty/preferences; roadmap |
| P34 | From Code to Courtroom | Medium / High | First pass completed from PDF; needs citation/BibTeX cleanup | Early SE 2030 LLM-as-judge vision; strict judge definition; concise roadmap |
| P35 | LLM Critics Help Catch LLM Bugs | High | First pass completed from PDF; needs citation/BibTeX cleanup | Critic-assisted human oversight; CBI/comprehensiveness; hallucinated bugs/nitpicks; FSBS trade-off |
| P36 | LLMs-as-Judges Comprehensive Survey | Medium / High | First pass completed from PDF; needs citation/BibTeX cleanup | General LLM-as-judge taxonomy; bias taxonomy; adversarial attacks; meta-evaluation metrics |
| P37 | Modern Code Review at Google | High | First pass completed; needs PDF-level verification | Industrial code review goals; workflow impact; reviewer overhead; socio-technical baseline |
| P38 | Expectations, Outcomes, and Challenges of Modern Code Review | High | First pass completed; needs PDF-level verification | Review outcomes beyond defects; knowledge transfer; maintainability; human-review goals |
| P39 | Characteristics of Useful Code Reviews | High | First pass completed; needs PDF-level verification | Usefulness definition; human value; low-value comment framing; developer-centered evaluation |
| P40 | Code Change Reviewability | Medium / High | First pass completed; needs PDF-level verification | Reviewability; input-side context quality; change size, coherence, and description quality |
| P41 | Explaining Explanations | Low / Medium | First pass completed; needs PDF-level verification | Explanation quality; rationale clarity; grounded explanations; actionability |

## Working Rule

Keep this file aligned with the spreadsheet, but use the Markdown files as the main working source for analysis.

## Next Reading Candidates

- P42 — Developers shared ChatGPT conversations in GitHub PRs/issues.
- P43 — Survey on LLMs for software engineering.
- P44 — Survey on LLMs for code generation.
- P45–P50 — remaining background and related SE/LLM papers from the spreadsheet.
