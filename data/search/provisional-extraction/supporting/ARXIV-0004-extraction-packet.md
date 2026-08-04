# ARXIV-0004 extraction packet

- Title: ALIBI: Adaptive Agentic Attacks on LLM-Based Vulnerability Detectors via Adversarial Code Comments
- arXiv: 2607.24964v1
- Authors: Zixuan Wu; Cristina Nita-Rotaru
- Full text: `data/search/provisional-extraction/supporting/ARXIV-0004.txt`
- Screening tier: supporting

## Required extraction

1. Purpose: studies adversarial source-code comments that manipulate LLM-based vulnerability detectors without changing program behavior.
2. System/context: adaptive black-box attack framework; the attacker inserts comments and uses detector feedback to refine attacks.
3. Study design: four LLM-based vulnerability detectors evaluated on 125 real-world null-pointer-dereference vulnerabilities reconstructed as coding tasks.
4. Problematic risks: fabricated tool results, adversarial comments, misleading natural-language claims, and detector over-trust in comments.
5. Metrics/results: attack success exceeds 90% across the reported vulnerability set and reaches 100% for one system; prompt-level defenses are limited, while comment sanitization and architectural isolation improve resilience.
6. Trade-off: comment sanitization and isolation may reduce contextual information, but retaining unverified comments creates security risk; the paper emphasizes evidence weighting and robustness.
7. Limitations: security-vulnerability setting and adversarial benchmark may not represent ordinary review comments or developer usefulness. Quality score: provisional, medium.
8. Synthesis claim: supporting evidence for context integrity, adversarial robustness, provenance, and the risk of treating natural-language comments as evidence.
