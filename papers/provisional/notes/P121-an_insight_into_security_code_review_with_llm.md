# P121 — An Insight into Security Code Review with LLMs: Capabilities, Obstacles, and Influential Factors

## 1. Identification

| Field | Value |
|---|---|
| Project ID | `P121` |
| Citation key | `p121_yu2024_an_insight_into_security_code_` |
| Authors | Jiaxin Yu; Peng Liang; Yujia Fu; Amjed Tahir; Mojtaba Shahin; Chong Wang; Yangxiao Cai |
| Year | 2024 |
| Source | arXiv preprint, `2401.16310v6` |
| Study type | Security code-review benchmark, response-quality analysis, and regression study |

## 2. Screening

- **Scope decision:** Include as core evidence for security review, prompt/context effects, hallucination taxonomy, and influential factors.
- **Task:** Detect security defects in Python and C/C++ code files and provide locations/details for findings.
- **Evidence boundary:** The study reports manually assessed security findings and response-quality problems, but not developer acceptance or production vulnerability reduction.
- **Metadata caveat:** Publisher/duplicate status and the provisional BibTeX record require verification.

## 3. Study overview

The study evaluates seven LLMs under five prompt families and compares them with static-analysis tools. The manually curated dataset contains 534 code files—258 Python and 276 C/C++—derived from 614 review instances and human-identified security defects. Prompts vary basic instructions, auxiliary information, CWE lists, commit messages, and chain-of-thought/context guidance. Responses are manually checked for detection, location, and quality problems. The two best model-prompt combinations are analyzed for verbosity, vagueness, inaccurate code details, hallucination categories, consistency across three runs, and the effects of 11 code/context factors using ordinal regression.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | DeepSeek-R1 is the strongest evaluated model, followed by GPT-4 via ChatGPT; LLMs outperform the compared static tools in the reported setting. | Reported | RQ1; Tables 3–6 |
| RQ2 | Responses frequently contain verbosity; GPT-4 shows vague expressions and instruction-following problems, while DeepSeek-R1 produces inaccurate code details. | Reported | RQ2; Table 7 |
| RQ3 | Fewer tokens and security-relevant annotations help detection; higher code complexity improves DeepSeek-R1 performance for some defect types. | Reported | RQ3; Tables 8–9 |
| RQ4 | Commit messages, CWE lists, generated context, CoT, and guardrails are tested as context/prompt interventions. | Reported | Prompt design |
| RQ5 | Model/prompt selection, CWE grounding, commit-message context, and guardrails are practical mitigations, but prompt scope can reduce detection. | Reported/limitation | RQ1.2–RQ1.3 |
| RQ6 | Manual labels, repeated runs, response coding, regression, and static-tool comparison support evaluation; no downstream human workflow study is included. | Reported/limitation | Sections 2–6 |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Verbosity | Response contains unnecessary detail or excessive explanation. | Manually coded | RQ2 |
| Vague expression | Finding is too broad or imprecise to guide remediation. | Manually coded | RQ2 |
| Inaccurate code detail | Response misstates code behavior, location, or implementation details. | Manually coded | RQ2 |
| Misleading claim | Model indicates a defect that is not present or gives incorrect security reasoning. | Manually coded | RQ2 |
| Uncertain finding | Response cannot establish a defect confidently from the available context. | Manually coded | RQ2 |
| Missed defect | Existing human-identified security defect is not detected. | Detection metric | RQ1 |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Security detection | I-score/accuracy-style detection and location evaluation | DeepSeek-R1 leads; basic-prompt I-score is 5.41% Python and 12.64% C/C++ in reported analysis. | RQ1.1 |
| Prompt effect | Compare basic, auxiliary, CWE, CoT, and guardrail prompts | Commit+CoT works best for DeepSeek-R1; CWE-list prompt works best for GPT-4 ChatGPT. | RQ1.2–RQ1.3 |
| Consistency | Repeat each LLM–prompt combination three times | Non-determinism is explicitly measured and treated as a reliability concern. | RQ1.4 |
| Response quality | Frequencies of verbosity, vagueness, inaccuracy, misleading, and uncertainty categories | Verbosity is most prevalent for both top systems. | RQ2; Table 7 |
| Influential factors | Ordinal regression over tokens, annotations, complexity, defect type, position, and related variables | Effects differ by model and defect type. | RQ3; Tables 8–9 |
| Baseline comparison | Compare LLMs with Bandit, Cppcheck, and CodeQL/static analyzers | LLMs outperform compared tools in the reported dataset, but neither class dominates every defect. | RQ1 |

## 7. Mitigation and trade-offs

- **Mitigation family:** CWE grounding, commit-message context, CoT reasoning, generated context, guardrails, and smaller focused code-file prompts.
- **Intervention point:** Prompt/context construction and output constraints.
- **What it reduces:** Context ambiguity, missed security categories, and unsupported reasoning.
- **Useful feedback potentially lost:** Specific CWE lists may narrow detection and miss vulnerabilities outside the supplied categories; aggressive context reduction may omit relevant dependencies.
- **Coverage:** Smaller files and security annotations help detection, but repository-wide interactions and multi-file vulnerabilities are harder to capture.
- **Human escalation:** Security findings and uncertain/misleading outputs require expert verification; no formal escalation protocol is tested.
- **Cost:** Multiple models, prompts, repeated runs, and manual response coding increase computational and annotation cost.
- **New failure modes:** Prompt distraction, hallucinated context, vague explanations, inaccurate code details, and unstable repeated outputs.

## 8. Annotation and evaluator validity

- **Dataset validity:** Human-curated security-review data are stronger than synthetic-only vulnerability benchmarks and cover file-level context.
- **Manual coding:** Detection labels and response-quality problems are manually inspected; conflicts are discussed among authors.
- **Reliability:** Repeated runs support consistency analysis, and multiple authors participate in coding; the extracted evidence does not provide one central agreement statistic for every label.
- **Regression validity:** Ordinal regression examines factors beyond aggregate model scores, but associations are not causal effects.
- **Threats:** Security expertise, model version drift, prompt construction, token truncation, and subjectivity in quality categories.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Three RQs and subquestions clearly define the study. |
| Q2 | 2 | Human-curated Python/C/C++ dataset and defect scope are described. |
| Q3 | 2 | Seven models, prompts, context construction, and procedures are detailed. |
| Q4 | 2 | Detection, consistency, quality categories, and regression metrics are reported. |
| Q5 | 2 | Manual inspection and quality codebook are used. |
| Q6 | 1 | Multi-author review is described, but agreement details are incomplete. |
| Q7 | 2 | Multiple models, prompts, and static-analysis baselines are compared. |
| Q8 | 2 | Realistic file-level, multi-language security data support breadth. |
| Q9 | 2 | Prompt/context interventions and guardrail variants are evaluated. |
| Q10 | 1 | Runtime/repetition cost is discussed, not fully quantified. |
| Q11 | 2 | Detailed response failure categories and influential factors are analyzed. |
| Q12 | 2 | Direct security-review evidence with practical failure taxonomy. |

**Total: 22/24 — high confidence for security-response quality and prompt-factor evidence, with external-validity caveats.**

## 10. Review-process reliability and bias

- **Dataset bias:** Human-curated defects may emphasize detectable/security-known issues and omit undiscovered vulnerabilities.
- **Model drift:** Results depend on versions, API/platform access, default settings, and a rapidly changing model ecosystem.
- **Prompt bias:** Auxiliary information can help or distract; CWE-limited prompts may artificially constrain scope.
- **Annotation bias:** Manual quality categories require security judgment and may conflate uncertainty with incorrectness.
- **Regression interpretation:** Significant associations do not establish that changing complexity or context will causally improve detection.
- **Missing outcomes:** No developer trust, remediation acceptance, secure-fix rate, or production incident reduction is measured.

## 11. Synthesis-ready conclusion

- P121 provides strong evidence that security code review requires evaluation beyond binary vulnerability detection.
- DeepSeek-R1 and GPT-4 show different failure profiles: inaccurate code details versus vague/instruction-incomplete explanations.
- Prompt context matters, but more context is not uniformly better; CWE lists, commit messages, CoT, and guardrails have model-specific effects.
- Response-quality taxonomies and factor analyses expose reliability risks that aggregate F1/accuracy can hide.
- Use as core evidence for security review, prompt/context trade-offs, hallucination categories, and the need for expert escalation.

