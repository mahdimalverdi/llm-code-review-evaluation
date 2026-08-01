# SLR paper-review progress

> Quality-control note: the first batch pass identified structural depth differences across notes. Rows previously marked `Completed` are batch-pass records; they require the uniformity re-review before final SLR synthesis. A paper is final only after all 11 canonical sections are populated with PDF-traceable evidence.

## Uniformity re-review status

| Batch | Scope | Status | Remaining work |
|---|---|---|---|
| Batch 1 | P01–P10 | Uniform canonical extraction completed | Full-PDF verification of unresolved protocol/metric details before final synthesis |
| Batch 2 | P11–P20 | Uniform canonical extraction completed | Full-PDF verification of unresolved protocol/metric details before final synthesis |
| Batch 3 | P21–P30 | Uniform canonical extraction completed | Full-PDF verification of specialized/security/judge protocol details before final synthesis |
| Batch 4 | P31–P40 | Uniform canonical extraction completed | Full-PDF verification of judge-survey and foundational workflow evidence before final synthesis |
| Batch 5 | P41–P50 | Uniform canonical extraction completed | Full-PDF verification of supporting/context and specialized non-functional evidence before final synthesis |
| Batch 6 | P51–P60 | Uniform canonical extraction completed | Full-PDF verification of survey, benchmark, industrial, annotation, and usefulness evidence before final synthesis |
| Batch 7 | P61–P71 | Uniform canonical extraction completed | Full-PDF verification of experience, industrial, security, adversarial, benchmark, and refinement evidence before final synthesis |

## Corpus integrity audit

- Unique PDF project IDs: 71.
- Markdown note files: 73.
- Duplicate note IDs requiring consolidation or explicit companion labeling: P18 and P21.
- Final SLR study count must be frozen only after this audit.

> [!WARNING]
> All seven calibration batches pass the eleven-section structural gate. `Completed` indicates that the authoritative note contains RQ1–RQ6, Q1–Q12, trade-off, evaluator-validity, and reliability fields. It does not imply independent second-reviewer agreement or a reconstructed database-search history.

## Gate-compliance batches

| Batch | Records | Result | Validation basis | Date |
|---|---|---|---|---|
| Calibration 1 | P01–P10 | Passed | Structural gate checked by `validate-note.sh`; reported sample sizes, agreement statistics, costs, and quality scores rechecked against the full local PDFs, including a second calibration of P04/P05/P08/P09 | 2026-08-02 |
| Calibration 2 | P11–P20 | Passed | Canonical eleven-section records validated; Q1–Q12 totals recalculated consistently; compact extractions retained as provenance only | 2026-08-02 |
| Calibration 3 | P21–P30 | Passed | Canonical eleven-section records validated; Q1–Q12 arithmetic corrected; P21 archived duplicate excluded from the study count | 2026-08-02 |
| Calibration 4 | P31–P40 | Passed | Canonical records validated; supporting/core boundaries preserved; Q1–Q12 arithmetic corrected | 2026-08-02 |
| Calibration 5 | P41–P50 | Passed | Canonical records validated; indirect/supporting evidence boundaries retained; systematic Q1–Q12 arithmetic errors corrected | 2026-08-02 |
| Calibration 6 | P51–P60 | Passed | Full local PDFs extracted; canonical records validated; P54–P60 advanced from in-progress with Medium confidence pending independent calibration | 2026-08-02 |
| Calibration 7 | P61–P71 | Passed | Full local PDFs extracted; canonical records validated; provisional labels removed while Medium confidence is retained for transfer and second-reviewer limitations | 2026-08-02 |

| ID | PDF | Note | Status | Decision | Relevance | Quality | Confidence | Unresolved items | Last reviewed |
|---|---|---|---|---|---|---:|---|---|---|
| P01 | `papers/pdfs/P01_DeepCRCEval_Revisiting_the_Evaluation_of_Code_Review_Comment_Generation.pdf` | `papers/P01-deepcrceval.md` | Completed | Include | High | 21/24 | Medium | Verify extended appendix and final citation metadata | 2026-08-01 |
| P02 | `papers/pdfs/P02_HalluJudge.pdf` | `papers/P02-hallujudge.md` | Completed | Include | High | 23/24 | Medium | Verify final metadata and cost assumptions | 2026-08-01 |
| P03 | `papers/pdfs/P03_RovoDev_Code_Reviewer.pdf` | `papers/P03-rovodev-code-reviewer.md` | Completed | Include | High | 21/24 | Medium | Verify ablation tables and final metadata | 2026-08-01 |
| P04 | `papers/pdfs/P04_SWE_PRBench.pdf` | `papers/P04-swe-prbench.md` | Completed | Include | High | 23/24 | High | Final publisher metadata remains to be checked | 2026-08-02 |
| P05 | `papers/pdfs/P05_SWRBench.pdf` | `papers/P05-swrbench.md` | Completed | Include | High | 23/24 | High | Useful-feedback preservation and consolidated generation cost remain unreported | 2026-08-02 |
| P06 | `papers/pdfs/P06_ContextCRBench.pdf` | `papers/P06-contextcrbench.md` | Completed | Include | High | 19/24 | Low/Medium | Verify annotation and judge protocol from full PDF | 2026-08-01 |
| P07 | `papers/pdfs/P07_Impact_of_LLM_based_Review_Comment_Generation.pdf` | `papers/P07-revmate-user-study.md` | Completed | Include | High | 22/24 | Medium | Verify acceptance and reviewer-overhead measures | 2026-08-01 |
| P08 | `papers/pdfs/P08_Too_Noisy_To_Learn.pdf` | `papers/P08-too-noisy-to-learn.md` | Completed | Include | High | 23/24 | High | Wrong-removal and category-specific retention remain unreported | 2026-08-02 |
| P09 | `papers/pdfs/P09_Hydra-Reviewer.pdf` | `papers/P09-hydra-reviewer.md` | Completed | Include | High | 24/24 | High | Preservation, escalation policy, and production effects remain unreported | 2026-08-02 |
| P10 | `papers/pdfs/P10_BitsAI_CR.pdf` | `papers/P10-bitsai-cr.md` | Completed | Include | High | 23/24 | High | Verify final production metadata | 2026-08-01 |
| P11 | `papers/pdfs/P11_LAURA.pdf` | `papers/P11-laura.md` | Completed | Include | High | 22/24 | High | Final publisher/artifact metadata remains | 2026-08-02 |
| P12 | `papers/pdfs/P12_SGCR.pdf` | `papers/P12-sgcr.md` | Completed | Include | High | 22/24 | High | Preservation and escalation remain unreported | 2026-08-02 |
| P13 | `papers/pdfs/P13_Prompting_and_Fine_tuning_LLMs_for_Code_Review.pdf` | `papers/P13-prompting-and-fine-tuning-llms-for-code-review.md` | Completed | Include | High | 22/24 | High | Preservation and workflow cost remain unreported | 2026-08-02 |
| P14 | `papers/pdfs/P14_CodeReviewer.pdf` | `papers/P14-codereviewer.md` | Completed | Include | High | 20/24 | High | Human/workflow validity remains limited | 2026-08-02 |
| P15 | `papers/pdfs/P15_LLaMA_Reviewer.pdf` | `papers/P15-llama-reviewer.md` | Completed | Include | Medium/High | 20/24 | High | Direct failure taxonomy and workflow evidence remain limited | 2026-08-02 |
| P16 | `papers/pdfs/P16_Context_Aware_Code_Review_Automation.pdf` | `papers/P16-context-aware-code-review-automation.md` | Completed | Include | High | 21/24 | High | Preservation and escalation remain unreported | 2026-08-02 |
| P17 | `papers/pdfs/P17_CodeReviewQA.pdf` | `papers/P17-codereviewqa.md` | Completed | Include | Medium/High | 19/24 | High | Verify annotation reliability | 2026-08-01 |
| P18 | `papers/pdfs/P18_Harnessing_LLMs_for_Curated_Code_Reviews.pdf` | `papers/P18-curated-code-reviews.md` | Completed | Include | High | 21/24 | High | Useful-intent preservation remains unmeasured | 2026-08-02 |
| P19 | `papers/pdfs/P19_Fine_Grained_Review_Comment_Classification.pdf` | `papers/P19-fine-grained-review-comment-classification.md` | Completed | Include | High | 19/24 | Medium/High | Verify category definitions and agreement | 2026-08-01 |
| P20 | `papers/pdfs/P20_Retrieval_Augmented_Code_Review_Comment_Generation.pdf` | `papers/P20-rag-reviewer.md` | Completed | Include | High | 21/24 | High | Preservation, escalation, and workflow cost remain unreported | 2026-08-02 |
| P21 | `papers/pdfs/P21_iCodeReviewer.pdf` | `papers/P21-icode-reviewer.md` | Completed | Include | High | 21/24 | High | Security-specific transfer and preservation remain limited | 2026-08-02 |
| P22 | `papers/pdfs/P22_Combining_LLMs_with_Static_Analyzers_for_Code_Review.pdf` | `papers/P22-combining-llms-with-static-analyzers.md` | Completed | Include | High | 21/24 | High | Preservation and workflow benefit remain unreported | 2026-08-02 |
| P23 | `papers/pdfs/P23_Leveraging_Reviewer_Experience.pdf` | `papers/P23-reviewer-experience.md` | Completed | Supporting | High | 21/24 | Medium/High | Verify study protocol and participant details | 2026-08-01 |
| P24 | `papers/pdfs/P24_Reward_Models_for_Code_Review_Comment_Generation.pdf` | `papers/P24-reward-models-code-review.md` | Completed | Include | High | 21/24 | High | Reward validity and preservation remain limited | 2026-08-02 |
| P25 | `papers/pdfs/P25_Fine_Tuning_LLMs_for_Automated_Code_Review.pdf` | `papers/P25-carllm.md` | Completed | Include | High | 21/24 | High | Preservation and escalation remain unreported | 2026-08-02 |
| P26 | `papers/pdfs/P26_Human_AI_Synergy_in_Agentic_Code_Review.pdf` | `papers/P26-human-ai-synergy-agentic-code-review.md` | Completed | Include | High | 22/24 | High | Context-specific causal interpretation remains limited | 2026-08-02 |
| P27 | `papers/pdfs/P27_From_Industry_Claims_to_Empirical_Reality.pdf` | `papers/P27-industry-claims-empirical-reality-code-review-agents.md` | Completed | Supporting | High | 21/24 | High | Production proxies do not isolate correctness | 2026-08-02 |
| P28 | `papers/pdfs/P28_Support_Not_Automation_AI_Supported_Code_Review.pdf` | `papers/P28-support-not-automation-ai-supported-code-review.md` | Completed | Supporting | High | 19/24 | High | Conceptual evidence; no controlled mitigation evaluation | 2026-08-02 |
| P29 | `papers/pdfs/P29_Can_LLMs_Replace_Human_Evaluators.pdf` | `papers/P29-can-llms-replace-human-evaluators.md` | Completed | Supporting | High | 21/24 | Medium/High | Verify evaluator comparison and bias measures | 2026-08-01 |
| P30 | `papers/pdfs/P30_CodeUltraFeedback.pdf` | `papers/P30-codeultrafeedback.md` | Completed | Supporting | High | 20/24 | Medium | Verify preference-data and evaluator details | 2026-08-01 |
| P31 | `papers/pdfs/P31_CodeJudgeBench.pdf` | `papers/P31-codejudgebench.md` | Completed | Supporting | High | 21/24 | Medium | Verify benchmark protocol and judge metrics | 2026-08-01 |
| P32 | `papers/pdfs/P32_Bias_in_the_Loop.pdf` | `papers/P32-bias-in-the-loop.md` | Completed | Supporting | High | 21/24 | Medium | Verify bias suite and reliability measures | 2026-08-01 |
| P33 | `papers/pdfs/P33_LLM_as_a_Judge_for_Software_Engineering_Survey.pdf` | `papers/P33-llm-as-a-judge-for-software-engineering-survey.md` | Completed | Supporting | High | 20/24 | High | Verify survey coverage and taxonomy boundaries | 2026-08-01 |
| P34 | `papers/pdfs/P34_From_Code_to_Courtroom.pdf` | `papers/P34-from-code-to-courtroom.md` | Completed | Supporting | Medium/High | 19/24 | High | Roadmap claims remain conceptual rather than deployment evidence | 2026-08-02 |
| P35 | `papers/pdfs/P35_LLM_Critics_Help_Catch_LLM_Bugs.pdf` | `papers/P35-llm-critics-help-catch-llm-bugs.md` | Completed | Supporting/Core | High | 21/24 | High | Transfer from generated-code critique to PR review remains bounded | 2026-08-02 |
| P36 | `papers/pdfs/P36_LLMs_as_Judges_Comprehensive_Survey.pdf` | `papers/P36-llms-as-judges-comprehensive-survey.md` | Completed | Supporting | High | 20/24 | High | Verify general judge taxonomy | 2026-08-01 |
| P37 | `papers/pdfs/P37_modern_code_review_google.pdf` | `papers/P37-modern-code-review-google.md` | Completed | Supporting | High | 18/24 | Medium | Verify foundational workflow evidence | 2026-08-01 |
| P38 | `papers/pdfs/P38_expectations_outcomes_challenges_modern_code_review.pdf` | `papers/P38-expectations-outcomes-challenges-modern-code-review.md` | Completed | Supporting | High | 18/24 | Medium | Verify study protocol and constructs | 2026-08-01 |
| P39 | `papers/pdfs/P39_characteristics_useful_code_reviews.pdf` | `papers/P39-characteristics-useful-code-reviews.md` | Completed | Supporting | High | 20/24 | Medium | Verify usefulness dimensions and participants | 2026-08-01 |
| P40 | `papers/pdfs/P40_code_change_reviewability.pdf` | `papers/P40-code-change-reviewability.md` | Completed | Supporting/Core | Medium/High | 20/24 | High | Reviewability evidence is input-side and not LLM-specific | 2026-08-02 |
| P41 | `papers/pdfs/P41_explanations_in_code_reviews.pdf` | `papers/P41-explaining-explanations-code-reviews.md` | Completed | Supporting | Medium | 18/24 | Medium | Verify explanation study and participant protocol | 2026-08-02 |
| P42 | `papers/pdfs/P42_chatgpt_conversations_github_prs_issues.pdf` | `papers/P42-chatgpt-conversations-github-prs-issues.md` | Completed | Supporting | Low/Medium | 14/24 | Medium | Verify review-specific evidence boundary | 2026-08-02 |
| P43 | `papers/pdfs/P43_llm_for_software_engineering_survey.pdf` | `papers/P43-llm-for-software-engineering-survey.md` | Completed | Supporting | Medium | 15/24 | Medium | Verify code-review coverage | 2026-08-02 |
| P44 | `papers/pdfs/P44_code_generation_with_llms_survey.pdf` | `papers/P44-llm-code-generation-survey.md` | Completed | Supporting | Low/Medium | 13/24 | Medium | Use only for broad background | 2026-08-02 |
| P45 | `papers/pdfs/P45_code_specific_llms_survey.pdf` | `papers/P45-code-specific-llms-survey.md` | Completed | Supporting | Low | 12/24 | Medium | Use only for model/resource context | 2026-08-02 |
| P46 | `papers/pdfs/P46_llm_vulnerability_detection_repair_explanation.pdf` | `papers/P46-llm-vulnerability-detection-repair.md` | Completed | Supporting | Medium | 17/24 | Medium | Keep security boundary explicit | 2026-08-02 |
| P47 | `papers/pdfs/P47_llm_misalignment_critical_survey.pdf` | `papers/P47-llm-misalignment-critical-survey.md` | Completed | Supporting | Low/Medium | 17/24 | Medium | Use for mitigation vocabulary only | 2026-08-02 |
| P48 | `papers/pdfs/P48_llms_for_code_quality_issues.pdf` | `papers/P48-llms-code-quality-issues.md` | Completed | Supporting | Medium | 17/24 | Medium | Verify review-comment connection | 2026-08-02 |
| P49 | `papers/pdfs/P49_metamon_documentation_behavior_inconsistency.pdf` | `papers/P49-metamon-documentation-behavior-inconsistency.md` | Completed | Supporting/Core | Medium | 19/24 | Medium | Verify context-consistency evidence | 2026-08-02 |
| P50 | `papers/pdfs/P50_coffe_code_efficiency_benchmark.pdf` | `papers/P50-coffe-code-efficiency-benchmark.md` | Completed | Supporting | Low | 15/24 | Medium | Keep as specialized non-functional context | 2026-08-02 |
| P51 | `papers/pdfs/P51_modern_code_review_slr_taxonomy.pdf` | `papers/P51-modern-code-review-slr-taxonomy.md` | Completed | Supporting | High | 19/24 | High | Verify taxonomy extraction | 2026-08-02 |
| P52 | `papers/pdfs/P52_towards_automating_code_review_activities.pdf` | `papers/P52-towards-automating-code-review-activities.md` | Completed | Supporting | Medium/High | 19/24 | High | Verify automation-boundary evidence | 2026-08-02 |
| P53 | `papers/pdfs/P53_code_review_automation_strengths_weaknesses.pdf` | `papers/P53-code-review-automation-strengths-weaknesses.md` | Completed | Supporting/Core | High | 20/24 | High | Verify empirical evidence and limitations | 2026-08-02 |
| P54 | `papers/pdfs/P54_CR-Bench_Evaluating_the_Real-World_Utility_of_AI_Code_Review_Agents.pdf` | `papers/P54-cr-bench.md` | Completed | Include | High | 19/24 | Medium | Complete canonical 11-part full-text extraction and reliability appraisal | 2026-08-02 |
| P55 | `papers/pdfs/P55_Automated_Code_Review_In_Practice.pdf` | `papers/P55-automated-code-review-in-practice.md` | Completed | Include | High | 20/24 | Medium | Complete canonical 11-part full-text extraction and confounding analysis | 2026-08-02 |
| P56 | `papers/pdfs/P56_Human_and_Machine_How_Software_Engineers_Perceive_and_Engage_with_AI-Assisted_Code_Reviews_Compared_to_Their_Peers.pdf` | `papers/P56-human-and-machine.md` | Completed | Supporting | High | 18/24 | Medium | Complete canonical 11-part interview extraction and validity details | 2026-08-02 |
| P57 | `papers/pdfs/P57_On_Assessing_the_Relevance_of_Code_Reviews_Authored_by_Generative_Models.pdf` | `papers/P57-assessing-relevance-code-reviews.md` | Completed | Include | High | 20/24 | Medium | Complete canonical 11-part ranking and agreement extraction | 2026-08-02 |
| P58 | `papers/pdfs/P58_Are_LLMs_Reliable_Code_Reviewers_Systematic_Overcorrection_in_Requirement_Conformance_Judgement.pdf` | `papers/P58-llm-reliability-overcorrection.md` | Completed | Include | High | 21/24 | Medium | Complete canonical 11-part benchmark and verification extraction | 2026-08-02 |
| P59 | `papers/pdfs/P59_Automated_Classification_of_Human_Code_Review_Comments_with_Large_Language_Models.pdf` | `papers/P59-automated-classification-human-comments.md` | Completed | Include | High | 21/24 | Medium | Complete canonical taxonomy, annotation, and agreement extraction | 2026-08-02 |
| P60 | `papers/pdfs/P60_Hold_On_Is_My_Feedback_Useful_Evaluating_the_Usefulness_of_Code_Review_Comments.pdf` | `papers/P60-hold-on-feedback-usefulness.md` | Completed | Include | High | 20/24 | Medium | Complete canonical usefulness-label and cross-project extraction | 2026-08-02 |
| P61 | `papers/pdfs/P61_AI-Assisted_Code_Review_as_a_Scaffold_for_Code_Quality_and_Self-Regulated_Learning_An_Experience_Report.pdf` | `papers/P61-ai-assisted-code-review-learning.md` | Completed | Supporting | High | 17/24 | Medium | Verify experience-report method and coding | 2026-08-02 |
| P62 | `papers/pdfs/P62_DeputyDev_--_AI_Powered_Developer_Assistant_Breaking_the_Code_Review_Logjam_through_Contextual_AI_to_Boost_Developer_Productivity.pdf` | `papers/P62-deputydev.md` | Completed | Include | High | 21/24 | Medium | Verify A/B design and confounders | 2026-08-02 |
| P63 | `papers/pdfs/P63_Measuring_and_Exploiting_Confirmation_Bias_in_LLM-Assisted_Security_Code_Review.pdf` | `papers/P63-confirmation-bias-security-review.md` | Completed | Supporting/Core | High | 18/24 | Medium | Verify bias benchmark and measures | 2026-08-02 |
| P64 | `papers/pdfs/P64_Can_Adversarial_Code_Comments_Fool_AI_Security_Reviewers_--_Large-Scale_Empirical_Study_of_Comment-Based_Attacks_and_Defenses_Against_LL.pdf` | `papers/P64-adversarial-comments-security-review.md` | Completed | Supporting/Core | High | 21/24 | Medium | Verify paired analysis and defenses | 2026-08-02 |
| P65 | `papers/pdfs/P65_QASecClaw_A_Multi-Agent_LLM_Approach_for_False_Positive_Reduction_in_Static_Application_Security_Testing.pdf` | `papers/P65-qasecclaw.md` | Completed | Supporting/Core | High | 19/24 | Medium | Verify SAST baselines and cost | 2026-08-02 |
| P66 | `papers/pdfs/P66_A_Survey_of_Code_Review_Benchmarks_and_Evaluation_Practices_in_Pre-LLM_and_LLM_Era.pdf` | `papers/P66-code-review-benchmarks-survey.md` | Completed | Supporting/Core | High | 21/24 | Medium | Verify survey search and reliability protocol | 2026-08-02 |
| P67 | `papers/pdfs/P67_Trust_Me_I_Know_This_Function_Hijacking_LLM_Static_Analysis_using_Bias.pdf` | `papers/P67-familiar-pattern-attack.md` | Completed | Supporting | Medium/High | 18/24 | Medium | Verify attack and defense results | 2026-08-02 |
| P68 | `papers/pdfs/P68_CoTDeceptor_Adversarial_Code_Obfuscation_Against_CoT-Enhanced_LLM_Code_Agents.pdf` | `papers/P68-cotdeceptor.md` | Completed | Supporting | Medium/High | 17/24 | Medium | Verify attack protocol and security boundary | 2026-08-02 |
| P69 | `papers/pdfs/P69_Deep_Assessment_of_Code_Review_Generation_Approaches_Beyond_Lexical_Similarity.pdf` | `papers/P69-deep-assessment-code-review.md` | Completed | Include | High | 21/24 | Medium | Verify GradedReviews annotation and correlation | 2026-08-02 |
| P70 | `papers/pdfs/P70_Exploring_the_Potential_of_ChatGPT_in_Automated_Code_Refinement_An_Empirical_Study.pdf` | `papers/P70-chatgpt-code-refinement.md` | Completed | Supporting | Medium | 14/24 | Medium | Verify review-task connection and evaluation | 2026-08-02 |
| P71 | `papers/pdfs/P71_Exploring_the_Potential_of_Llama_Models_in_Automated_Code_Refinement_A_Replication_Study.pdf` | `papers/P71-llama-code-refinement-replication.md` | Completed | Supporting | Medium | 17/24 | Medium | Verify manual annotation and replication validity | 2026-08-02 |
