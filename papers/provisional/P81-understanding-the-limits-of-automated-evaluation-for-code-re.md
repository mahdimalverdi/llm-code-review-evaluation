# P81 — Understanding the Limits of Automated Evaluation for Code Review Bots in Practice

## 1. Identification

- Project ID: `P81` (provisional)
- Citation key: `p81_karakaya2026_understanding_the_limits_of_automated`
- Full reference: Veli Karakaya; Utku Boran Torun; Baykal Mehmet Uçar; Eray Tüzün. “Understanding the Limits of Automated Evaluation for Code Review Bots in Practice.” EASE 2026; arXiv:2604.24525v1.
- DOI/URL: `https://arxiv.org/abs/2604.24525v1`
- Review date: 2026-08-04
- Source/database: arXiv full-text screening
- Selection stage: included for reconciliation; canonical corpus integration pending
- Duplicate or companion publication: ACM metadata contains placeholder DOI; verify final record.

## 2. Screening

- Decision: `Include`
- Relevance: `High`
- Decision rationale: Industrial study directly tests whether G-Eval and LLM-as-a-Judge recover developer labels for bot-review usefulness.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: taxonomy / annotation protocol / mitigation design / trade-off framework
- Exact inclusion criterion: Core inclusion: review-comment evaluation, evaluator validity, and human-label limitations.

## 3. Study overview

- Purpose: Assess feasibility and limits of automated evaluation of ACR comments in industrial practice.
- Research questions: RQ1 G-Eval alignment with human labels; RQ2 plain LLM-as-a-Judge alignment; RQ3 differences across models/rubrics and implications for ground truth.
- Method: Compare G-Eval and direct LLM judging under binary and 0–4 Likert formulations on an industrial dataset, supplemented by an interview with a software-engineering director.
- Evaluated system/artifact: 2,604 bot-generated PR comments from Beko, originally produced by a Qodo-based review agent.
- Dataset/benchmark: 1,733 comments labeled fixed and 871 wontFix/closed; only fixed comments are treated as useful in the main mapping. 227 comments (8.7%) required diff truncation.
- Input context: Bot comment and PR diff; repository-wide guidelines, historical discussions, and broader organizational context are not supplied to evaluators.
- Main findings: Agreement ratios range about 0.44–0.62. Best G-Eval Likert GPT-4.1-mini reaches agreement 0.61, F1 0.76, precision 0.66, recall 0.90, but MCC −0.059, showing weak calibrated discrimination.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | G-Eval Likert generally aligns better than direct binary evaluation, but agreement remains moderate and model-sensitive. | Reported | Sections 3–4 |
| RQ2 | Plain LLM-as-a-Judge also shows moderate alignment; rubric/formulation affects outcomes. | Reported | Sections 3–4 |
| RQ3 | Developer labels reflect workflow pressure, prioritization, timing, and organizational constraints, not usefulness alone. | Reported/interview | Sections 1, 5 |
| RQ4 | Diff-only evaluation cannot capture project conventions, hidden context, or severity/priority trade-offs. | Reported | Section 5 |
| RQ5 | Agreement, F1, precision, recall, and MCC reveal that one headline metric can mask poor calibration. | Reported | Section 4 |
| RQ6 | The paper directly supports treating automated scores as triage signals requiring periodic human sampling. | Inferred | Sections 5–6 |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Contextually misclassified comment | Evaluator lacks repository/project context needed to judge applicability. | Reported limitation | Section 5 |
| Workflow-driven label | Fixed/ignored action reflects deadline, scope, or prioritization rather than technical usefulness. | Reported | Sections 1, 5 |
| Over-notification | Technically valid low-severity comment is treated as not useful due to attention cost. | Interview/synthesis | Section 5 |
| Metric miscalibration | High recall/F1 coexists with near-zero/negative MCC and moderate agreement. | Reported | Section 4 |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Agreement | Automated useful/not-useful label matches developer label. | Approx. 0.44–0.62 across models/settings. | Table 1 |
| Classification quality | F1, precision, recall, Matthews correlation coefficient. | Best F1 0.76, precision 0.66, recall 0.90, MCC −0.059. | Table 2 |
| Rubric sensitivity | Binary vs. 0–4 Likert judge formulation. | Likert generally higher agreement. | Sections 3–4 |
| Ecological validity | Industrial Beko data and director interview. | Labels remain organizationally contingent. | Sections 3, 5 |

## 7. Mitigation and trade-offs

- Mitigation family: Human-in-the-loop evaluation, rubric calibration, and periodic sampling.
- Intervention point: Evaluation/quality monitoring of generated comments, not comment generation itself.
- What it reduces: Overreliance on developer actions or one automated score as objective quality ground truth.
- Useful feedback potentially lost: A gate based on noisy labels may suppress technically valid but low-priority feedback.
- Coverage effect: Not measured; evaluation concerns label recovery rather than issue recall.
- Human escalation effect: Recommended for triage and periodic validation; not experimentally measured.
- Computational/operational cost: Automated judging reduces manual evaluation cost, but evaluator model/rubric experiments and human sampling remain necessary; monetary cost is not reported.
- New failure modes: Evaluator bias, model coupling with the review generator, context truncation, and threshold-driven label artifacts.

## 8. Annotation and evaluator validity

- Judge/annotator: Software engineers label bot comments; G-Eval and LLM-as-a-Judge produce automated labels; one software-engineering director provides interview evidence.
- Rubric: Fixed/useful vs. wontFix/closed/not useful mapping, plus direct binary and 0–4 usefulness scoring.
- Agreement/reliability: Agreement ratios are reported; no independent inter-rater reliability for developer labels is reported.
- Validity checks: Multiple evaluator models (Gemini-2.5-pro, GPT-4.1-mini, GPT-5.2), two rubric formats, F1/precision/recall/MCC, and interview triangulation.
- Possible bias: Single organization, Qodo/GPT-4 Turbo generator, developer-action labels, missing repository context, and model-family coupling.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Industrial setting and evaluation target are explicit. |
| Q2 | 2 | 2,604 comments and label composition are reported. |
| Q3 | 2 | Multiple judge models and formulations are specified. |
| Q4 | 2 | Agreement and classification metrics are explicit. |
| Q5 | 2 | Binary/Likert usefulness rubrics are defined. |
| Q6 | 1 | Agreement ratios reported; label reliability unclear. |
| Q7 | 2 | Controlled comparison and interview triangulation are described. |
| Q8 | 2 | MCC, truncation analysis, and context limitations are considered. |
| Q9 | 1 | Human-in-loop recommendation is conceptual, not tested as intervention. |
| Q10 | 1 | Automation motivation is clear; cost is not quantified. |
| Q11 | 2 | Industrial, contextual, metric, and coupling threats are discussed. |
| Q12 | 2 | Directly evaluates the validity of review-comment usefulness metrics. |

- Total: `21/24` provisional
- Quality interpretation: Strong industrial evidence that automated evaluation is context- and rubric-sensitive, with single-organization limits.

## 10. Review-process reliability and bias

- Missing data: Independent label reliability, human time, cross-organization transfer, and cost are not reported.
- Publication-bias concern: Not assessed; one industrial setting may underrepresent failures elsewhere.
- Selection uncertainty: Included by full-text screening; final EASE metadata should be reconciled.
- Extraction uncertainty: Moderate because useful labels derive from workflow actions.
- Second-reviewer agreement: Not available for this note.
- Duplicate-publication handling: Pending final-version reconciliation.

## 11. Synthesis-ready conclusion

- Contribution to the SLR: Shows that automated judges can only moderately recover industrial developer labels and that labels themselves encode workflow/context constraints.
- What the paper does not establish: It does not establish a universally valid usefulness rubric or that automated evaluation improves review practice.
- Research gap supported: Review evaluation needs context-rich, multi-dimensional human protocols and calibration beyond action-derived labels.
- Candidate synthesis claims: Automated evaluators are useful for triage, but agreement/F1 alone should not be treated as objective review quality, especially under context scarcity and organizational pressure.
- Follow-up verification needed: Obtain final EASE version, inspect label-generation protocol, and test cross-organization generalization.
