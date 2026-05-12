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
| P19 | Fine-Grained Review Comment Classification | Low / Medium | First pass completed from PDF; needs venue/DOI verification | 17-category taxonomy; usefulness-linked categories; LLM classification; code-context and class-imbalance trade-offs |
| P20 | RAG-Reviewer | Medium / High | First pass completed from PDF; needs citation/BibTeX cleanup | Retrieval-augmented comment generation; pair vs singleton exemplars; low-frequency-token coverage; k/token-budget trade-offs |

## Working Rule

Keep this file aligned with the spreadsheet, but use the Markdown files as the main working source for analysis.

## Next Reading Candidates

- P21 — iCodeReviewer: Improving Secure Code Review with Mixture of Prompts.
- P22 — Combining Large Language Models with Static Analyzers for Code Review Generation.
- Papers on LLM-as-a-judge reliability and bias for software engineering evaluation.
- Additional industrial deployment studies beyond Atlassian, Mozilla/Ubisoft, ByteDance, and SGCR.
- Papers on data cleaning, noisy labels, and dataset quality for code review generation.
