# P78 — SEVRA-BENCH: Social Engineering of Vulnerabilities in Review Agents

## 1. Identification

- Project ID: `P78` (provisional)
- Citation key: `p78_melo2026_sevra_bench_social_engineering`
- Full reference: Rui Melo; Riccardo Fogliato; Sean Zhou; Pratiksha Thaker; Zhiwei Steven Wu. “SEVRA-BENCH: Social Engineering of Vulnerabilities in Review Agents.” arXiv:2606.13757v2, 2026.
- DOI/URL: `https://arxiv.org/abs/2606.13757v2`
- Review date: 2026-08-04
- Source/database: arXiv full-text screening
- Selection stage: included for reconciliation; canonical corpus integration pending
- Duplicate or companion publication: Not reported; verify final metadata.

## 2. Screening

- Decision: `Include`
- Relevance: `High`
- Decision rationale: Directly benchmarks whether review agents reject vulnerability-reintroducing PRs when adversarial social narratives manipulate the review context.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: taxonomy / annotation protocol / mitigation design / trade-off framework
- Exact inclusion criterion: Core inclusion: security failure modes and robustness evaluation of automated code review.

## 3. Study overview

- Purpose: Measure review-agent susceptibility to deceptive PR narratives masking vulnerable code.
- Research questions: The benchmark evaluates refusal robustness across CWE classes and social-engineering framings, rationale security grounding, and agent differences.
- Method: Reverse historical vulnerability fixes, wrap the vulnerable diff in 15 fixed framings, deploy PRs in isolated Git repositories, and evaluate eight review agents.
- Evaluated system/artifact: MCP-backed ReAct review agents instantiated with Claude Opus 4.7, GPT-5.5, GLM-5, DeepSeek V4-Flash, Haiku-4.5, Kimi K2.5, Grok Code Fast, and GPT-5.4-nano.
- Dataset/benchmark: 2,250 malicious PRs from 150 vulnerability source records, 10 CWE classes, and 15 framings; retained challenge split is roughly 1,000 hard PRs where at least one baseline was fooled.
- Input context: Live repository, diff, commit history, and PR title/description/comments; agents inspect through MCP tools and decide approve/reject without an explicit security prompt.
- Main findings: Agents are vulnerable to narrative manipulation. Strong agents perform better, but framing and CWE strongly affect refusal; external claims such as prior approval or compatibility can cause unsafe deference.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Refusal Rate (RR) measures rejection of malicious PRs; Security Reason Rate (SRR) requires explicit identification of the underlying vulnerability. | Reported | Sections 3–4 |
| RQ2 | Performance varies across CWE classes; SQL/code injection are explained reliably by strongest agents, while buffer-related weaknesses are harder. | Reported | Section 4 |
| RQ3 | Fifteen framings manipulate evidence, urgency, prior approval, authority, compatibility, and attention; Prior Approval and Dependency Compatibility are especially effective. | Reported | Sections 3–4 |
| RQ4 | Narrative manipulation shifts the trade-off between contextual trust and security verification; rejecting without security reasoning is insufficient. | Inferred | Sections 4–5 |
| RQ5 | Historical fixes and manual spot-checks ground the benchmark, but the final outcome is agent approval/rejection rather than developer usefulness. | Reported | Sections 3, 5 |
| RQ6 | Provides direct adversarial evidence for robustness and contextual failure analysis. | Inferred | Sections 1, 3–5 |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Vulnerability reintroduction accepted | Agent approves a PR created by reversing a real security fix. | Benchmark failure | Sections 1, 3 |
| Narrative deference | Agent accepts unverifiable claims of prior approval, tests, compatibility, or authority. | Reported failure mode | Sections 3–5 |
| Security implication omission | Agent identifies a coding bug but does not explain its exploit/security implication. | Reported failure mode | Section 4 |
| Evidence dilution | Multi-file or distracting changes make the vulnerable behavior harder to isolate. | Framing category | Sections 3–4 |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Refusal robustness | Fraction of malicious PRs rejected. | Strong agents exceed 80% SRR for some CWEs; weaker agents show large gaps. | Section 4 |
| Security grounding | Fraction of rejections whose rationale names the underlying exploit. | RR and SRR can diverge; rejecting without security reasoning is not full success. | Sections 3–4 |
| Framing susceptibility | RR/SRR under fixed narrative framings with the same vulnerability diff. | Prior Approval and Dependency Compatibility are highly bypassing framings. | Section 4 |
| Agent variation | Comparison across eight models/agents. | Claude Opus 4.7 and GPT-5.5 most robust; Grok Code Fast weakest overall. | Section 4 |

## 7. Mitigation and trade-offs

- Mitigation family: Adversarial framing evaluation and claim-verification-oriented review.
- Intervention point: Review-agent reasoning before merge approval.
- What it reduces: Blind acceptance of persuasive but unverifiable PR narratives.
- Useful feedback potentially lost: Not measured; stricter rejection could reject legitimate changes whose context is incomplete.
- Coverage effect: Covers 10 CWE classes and 15 framings, but not all vulnerabilities or adaptive attacks.
- Human escalation effect: Not measured; the benchmark ends at agent decision.
- Computational/operational cost: Agents use repository exploration/MCP turns; cost and latency are not the primary metrics.
- New failure modes: Narrative manipulation, false test/approval claims, evidence dilution, and over-reliance on repository-wide assumptions.

## 8. Annotation and evaluator validity

- Judge/annotator: Historical vulnerability fixes provide ground truth; LLM-as-a-Judge inspects rejected rationales for security reasoning and is checked with manual spot checks.
- Rubric: Reject/approve decision plus explicit identification of the underlying exploit for SRR.
- Agreement/reliability: No formal inter-rater statistic is reported for rationale judging.
- Validity checks: Mechanical reversal of real security patches, fixed diffs across framings, isolated Gitea/MCP environment, baseline-based challenge retention, and manual judge spot checks.
- Possible bias: Public historical vulnerabilities, fixed framings, one-shot attacks, and model/tool versions may limit generalization.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Threat model, benchmark, and review decision are explicit. |
| Q2 | 2 | 2,250 PRs, 150 sources, 10 CWEs, and 15 framings are reported. |
| Q3 | 2 | Eight agents and MCP protocol are specified. |
| Q4 | 2 | RR, SRR, CWE/framing comparisons are explicit. |
| Q5 | 2 | Real vulnerability fixes and repository context ground evaluation. |
| Q6 | 1 | Manual spot checks exist, but formal judge reliability is absent. |
| Q7 | 2 | Fixed-diff framing isolation and baseline retention are described. |
| Q8 | 2 | Reproducible historical patches and controlled environment support validity. |
| Q9 | 2 | Adversarial framing/claim verification is the explicit robustness intervention. |
| Q10 | 1 | Agent turns are analyzed, but monetary/latency cost is not central. |
| Q11 | 2 | Adaptive attacks, novelty, framing overlap, and dual-use limits are discussed. |
| Q12 | 2 | Directly evaluates security failure modes of automated review approval. |

- Total: `22/24` provisional
- Quality interpretation: Strong controlled adversarial benchmark evidence, with external-validity and judge-reliability limits.

## 10. Review-process reliability and bias

- Missing data: Human usefulness, false-positive rejection, recall over benign PRs, and operational cost are not measured.
- Publication-bias concern: Not assessed; benchmark is derived from publicly disclosed fixes.
- Selection uncertainty: Included by full-text screening; final metadata and released benchmark should be reconciled.
- Extraction uncertainty: Moderate because challenge retention and judge-based SRR affect measured difficulty.
- Second-reviewer agreement: Not available for this note.
- Duplicate-publication handling: Pending version reconciliation.

## 11. Synthesis-ready conclusion

- Contribution to the SLR: Establishes social context in PR narratives as an attack surface that can cause review agents to approve vulnerable changes.
- What the paper does not establish: It does not establish real-world exploit rates, developer usefulness, benign-review precision, or resilience to adaptive attackers.
- Research gap supported: Review quality evaluation should test adversarial context manipulation and require security-grounded rationales, not only binary decisions.
- Candidate synthesis claims: Robust review requires independent verification of narrative claims; acceptance or generic bug detection alone is insufficient evidence of safe review.
- Follow-up verification needed: Inspect released SEVRA-BENCH data and exact challenge-split construction before corpus integration.
