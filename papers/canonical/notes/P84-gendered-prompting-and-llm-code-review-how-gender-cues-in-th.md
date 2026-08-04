# P84 — Gendered Prompting and LLM Code Review: How Gender Cues Shape Code Quality and Evaluation

## 1. Identification

- Project ID: `P84` (provisional)
- Citation key: `p84_janzen2026_gendered_prompting_and_llm_cod`
- Full reference: Lynn Janzen; Üveys Eroglu; Dorothea Kolossa; Pia Knöferle; Sebastian Möller; Vera Schmitt; Veronika Solopova. “Gendered Prompting and LLM Code Review: How Gender Cues in the Prompt Shape Code Quality and Evaluation.” arXiv:2603.24359v1, 2026.
- DOI/URL: `https://arxiv.org/abs/2603.24359v1`
- Review date: 2026-08-04
- Source/database: arXiv full-text screening
- Selection stage: included for reconciliation; canonical corpus integration pending
- Duplicate or companion publication: Not reported; verify final metadata.

## 2. Screening

- Decision: `Include`
- Relevance: `High`
- Decision rationale: Mixed-methods study directly examines gender-coded prompts and systematic bias in LLM-based code-review approval.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: taxonomy / annotation protocol / mitigation design / trade-off framework
- Exact inclusion criterion: Core inclusion: reviewer bias, evaluation validity, and prompt-sensitive code quality.

## 3. Study overview

- Purpose: Identify whether gender-linked language affects generation and whether LLM reviewers evaluate comparable code differently.
- Research questions: Study I analyzes real prompts; Study II controls programming tasks and user gender; Study III manipulates gender-coded prompt style and reviewer persona across LLMs.
- Method: Mixed-methods pilot: 746 analyzed prompts, 59 controlled-study participants, and systematic gender-coded simulations across multiple model providers.
- Evaluated system/artifact: LLM-generated Python code and LLM reviewer decisions (APPROVE vs. CHANGES_REQUESTED).
- Dataset/benchmark: Real coding chat histories (536 training prompts plus test prompts), 34 Python prompt tasks, 59 participants, and five controlled prompt variants across five algorithmic tasks.
- Input context: Gender-coded linguistic cues, stereotypical agentic/communal wording, names/personas, identical coding tasks, and reviewer prompts.
- Main findings: Prompt-style differences are subtle; generation correctness showed no consistent gender gap, but reviewers approved female-authored code more often (73.5% vs. 62.9%) despite comparable quality. Gender-coded prompts also changed length/maintainability and reviewer behavior by provider.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Female-authored prompts use more personal pronouns, involved language, and certain interrogative/request forms; prompt gender is moderately predictable (weighted F1≈0.60–0.61). | Reported | Study I |
| RQ2 | No consistent functional correctness gap in Study II; Study III shows prompt style changes code length, maintainability, and surface metrics. | Reported | Studies II–III |
| RQ3 | LLM reviewers approve female-authored code more frequently despite comparable quality; provider effects are substantial. | Reported | Study II |
| RQ4 | Gender-coded reviewer personas and prompt variants interact with model provider; approval varies without corresponding correctness differences. | Reported | Study III |
| RQ5 | Unit tests, Pylint/Radon, and approval decisions operationalize correctness, static quality, and review evaluation. | Reported | Studies II–III |
| RQ6 | Demonstrates evaluator bias as distinct from generation accuracy, creating a fairness/quality trade-off. | Inferred | Abstract, Studies II–III |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Approval bias | Comparable code receives different approve rates based on gender-coded authorship cues. | Reported failure | Study II |
| Prompt-style confounding | Gender-coded wording changes code structure or maintainability independently of task. | Reported effect | Study III |
| Provider-dependent bias | Reviewer approval differences vary substantially across model families. | Reported effect | Studies II–III |
| Proxy-quality mismatch | Surface/static metrics and approval decisions do not necessarily reflect functional correctness. | Inferred | Studies II–III |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Prompt language | Length, pronouns, spelling, punctuation, directness, clause/request types. | Female prompts more personal/involved; differences subtle. | Study I |
| Functional correctness | Unit-test pass rates. | No consistent gender difference in Study II/III. | Studies II–III |
| Static quality | Pylint, Radon complexity/maintainability. | Prompt style affects maintainability and surface quality. | Studies II–III |
| Review decision | APPROVE vs. CHANGES_REQUESTED. | Female-authored approval 73.5% vs. male 62.9%. | Study II |
| Reviewer bias | Approval by gender-coded prompt/persona/provider. | Provider-dependent systematic differences. | Study III |

## 7. Mitigation and trade-offs

- Mitigation family: Bias auditing and fairness-aware reviewer evaluation.
- Intervention point: Prompt construction, reviewer evaluation, and model/provider selection.
- What it reduces: Unwarranted approval differences caused by gender-coded cues.
- Useful feedback potentially lost: Fairness normalization could suppress genuine quality-related signals if prompt style is correlated with substantive context; not tested.
- Coverage effect: Not measured; study focuses on approval parity and code metrics.
- Human escalation effect: Not measured.
- Computational/operational cost: Multi-provider audits and repeated controlled runs are required; cost is not reported.
- New failure modes: Gender inference from language, stereotypical prompt construction, and provider-specific fairness regressions.

## 8. Annotation and evaluator validity

- Judge/annotator: Unit tests and static analyzers evaluate code; multiple LLM reviewers evaluate approval; human participant gender is self-reported.
- Rubric: Pass rate, Pylint/Radon, prompt linguistic features, and binary approval.
- Agreement/reliability: Statistical tests compare groups; no inter-rater reliability applies to automated approval, and the LLM judge is itself the object of audit.
- Validity checks: Real prompts plus controlled tasks plus synthetic prompt manipulations, multiple providers, and repeated decoding profiles.
- Possible bias: Small pilot samples, binary/limited gender coding, stereotypical operationalization, provider/model versions, and simulation realism.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Three-study design and bias target are clear. |
| Q2 | 2 | Prompt corpora, participants, and controlled tasks are reported. |
| Q3 | 2 | Multiple providers/reviewer personas are included. |
| Q4 | 2 | Correctness, static quality, language, and approval metrics are explicit. |
| Q5 | 2 | Controlled prompt/persona manipulations are specified. |
| Q6 | 1 | Statistical tests are reported; evaluator reliability is not applicable/absent. |
| Q7 | 2 | Mixed real/controlled/simulated design triangulates findings. |
| Q8 | 1 | Small pilot and gender operationalization limit validity. |
| Q9 | 1 | Bias audit is evaluated, but mitigation is not experimentally tested. |
| Q10 | 1 | Repeated model runs are described; cost is not measured. |
| Q11 | 2 | Sample, simulation, and interpretation limits are acknowledged. |
| Q12 | 2 | Directly evaluates bias in LLM-based code-review decisions. |

- Total: `20/24` provisional
- Quality interpretation: Important exploratory evidence for evaluator bias, with limitations from small samples and gender-cue operationalization.

## 10. Review-process reliability and bias

- Missing data: Human review usefulness, causal mechanism of approval bias, long-term impact, and mitigation efficacy are not measured.
- Publication-bias concern: Not assessed; pilot/simulation results require replication.
- Selection uncertainty: Included by full-text screening; final metadata should be reconciled.
- Extraction uncertainty: Moderate/high for simulated gender cues and provider-specific effects.
- Second-reviewer agreement: Not available for this note.
- Duplicate-publication handling: Pending version reconciliation.

## 11. Synthesis-ready conclusion

- Contribution to the SLR: Shows that LLM review decisions can be biased by gender-coded authorship/prompt cues even when generated code quality is comparable.
- What the paper does not establish: It does not establish the prevalence of this bias in production or a reliable mitigation.
- Research gap supported: Fair review evaluation needs controlled demographic/cue audits alongside correctness, quality, and usefulness metrics.
- Candidate synthesis claims: Evaluator behavior may be a fairness risk independent of generation accuracy; approval should not be treated as a neutral quality signal without bias auditing.
- Follow-up verification needed: Replicate with larger, more diverse participants, less stereotypical cue designs, and blinded human review outcomes.
