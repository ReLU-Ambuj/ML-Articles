# Section 16 — Legal

**Volume:** IV — Funding, Legal & Business  
**Status:** 🔲 Not Started  
**Estimated Depth:** 15–20 pages

---

## Objectives

1. Understand all legal structures available for an AI research lab
2. Know the IP landscape: patents, trade secrets, and open-source licenses
3. Navigate data privacy and AI regulation compliance
4. Protect yourself and your organization without expensive legal counsel

---

## Prompt for Deep Content Generation

```
You are a technology attorney and AI policy expert writing 
a legal reference for AI research lab founders. 
This is not legal advice — it is education about the legal landscape.

Write Section 16 of "Building an AI Research Lab From Scratch" — 
a complete legal reference for AI research organizations.

PART A — COMPANY FORMATION
   For each structure, explain: formation process, governance, tax treatment,
   liability protection, fundraising compatibility, and when to choose it.

   India:
   - Private Limited Company (the default for tech startups)
   - Section 8 Company (non-profit equivalent)
   - LLP (Limited Liability Partnership)
   - One Person Company (OPC) for solo founders
   - Society / Trust (for academic or charitable labs)
   
   US (if planning Delaware incorporation):
   - C-Corporation (required for VC funding)
   - Delaware LLC
   - Public Benefit Corporation (PBC)
   - 501(c)(3) Non-profit
   
   When to dual-incorporate (India + US): why, when, and how.
   
   Formation costs in India: CA fees, ROC registration, timeline.

PART B — INTELLECTUAL PROPERTY
   - Patent strategy for AI: what can be patented in AI research?
     (algorithms: generally no. Specific implementations: sometimes. 
      Training methods: sometimes. Model architectures: sometimes.)
   - Patent filing: provisional vs. full, India vs. US vs. PCT (international)
   - Cost of patent filing: India ₹5,000–₹15,000 vs. US $10,000–$30,000
   - Trade secrets as an alternative to patents for AI
   - IP ownership when collaborating with universities: assignment agreements
   - IP ownership for employees and contractors: what to include in contracts

PART C — OPEN SOURCE LICENSES — IN DEPTH
   For each license, explain: permissions, conditions, limitations,
   compatibility with other licenses, commercial use terms,
   and when an AI lab should choose it.
   
   - MIT License: permissive, widely compatible
   - Apache 2.0: permissive with patent grant — the preferred choice for many AI labs
   - GPL v2 and v3: copyleft, implications for ML models and code
   - LGPL: library-focused copyleft
   - AGPL: network use triggers copyleft — anti-SaaS provision
   - Creative Commons (for datasets and model weights):
     CC0, CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA
   - BigScience RAIL License: restricted use for harmful applications
   - Llama Community License: Meta's approach to open weights with restrictions
   - Custom model licenses: when labs write their own (and the risks)
   
   Open source license compatibility matrix (which licenses can be combined).

PART D — EMPLOYMENT AND CONTRACTOR LAW
   - Employee vs. contractor in India: legal definition, tax implications
   - Offer letter essentials for research roles
   - IP assignment clause: what it must contain
   - Non-compete clauses: enforceability in India vs. US
   - Equity documentation: ESOPs in India (Section 17(2) of Income Tax Act)
   - Research collaboration agreements with universities

PART E — DATA PRIVACY AND COMPLIANCE
   - GDPR (EU): scope, data processing basis, right to erasure, training data implications
   - India's Digital Personal Data Protection Act (DPDPA) 2023: 
     scope, consent requirements, penalties, data localization
   - CCPA (California): applicability to Indian labs with US users
   - HIPAA: when it applies (healthcare AI)
   - Data Processing Agreements (DPAs): when you need them with cloud providers
   - Privacy policy and terms of service: what an AI lab's must include

PART F — AI REGULATION
   - EU AI Act (2024): risk classification, prohibited AI, high-risk AI requirements
   - US Executive Order on AI (2023): what it requires from frontier labs
   - India's AI governance framework (MEITY guidelines, MeitY advisory)
   - China's generative AI regulations: implications for collaboration
   - What regulations apply to: model training, API deployment, open source release
   - How to perform an AI regulatory compliance audit

PART G — INTERNATIONAL CONSIDERATIONS
   - Export controls on AI: EAR (Export Administration Regulations), 
     implications for sharing model weights internationally
   - NVIDIA GPU export restrictions to certain countries
   - Publishing AI research: ITAR implications for some topics
   - Collaboration with Chinese researchers and institutions: current legal position

Format: structured markdown, license comparison table,
regulatory compliance checklist, entity formation comparison table.
Note: this is educational, not legal advice. Recommend real counsel for major decisions.
Depth target: ~15–20 pages.
```

---

## Deliverables

- [ ] Entity selection decision tree (India + US)
- [ ] Open source license comparison matrix
- [ ] IP assignment agreement template (for reference, not legal use)
- [ ] Data privacy compliance checklist (GDPR + DPDPA)
- [ ] AI regulation applicability matrix by jurisdiction

---

## Notes
