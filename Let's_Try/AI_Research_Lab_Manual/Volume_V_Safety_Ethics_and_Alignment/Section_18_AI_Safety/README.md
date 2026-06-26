# Section 18 — AI Safety

**Volume:** V — Safety, Ethics & Alignment  
**Status:** 🔲 Not Started  
**Estimated Depth:** 25–30 pages

---

## Objectives

1. Understand the technical and philosophical landscape of AI safety and alignment
2. Know how to implement practical safety measures in your own models
3. Position your lab credibly in the safety discourse
4. Understand the current frontier of interpretability and alignment research

---

## Safety Research Taxonomy

```
AI Safety Research
├── Alignment
│   ├── Value Learning and Preference Elicitation
│   ├── Constitutional AI
│   ├── Debate and Amplification
│   └── Cooperative AI
├── Interpretability
│   ├── Mechanistic Interpretability
│   ├── Concept Probing
│   ├── Circuit Analysis
│   └── Sparse Autoencoders (SAEs)
├── Evaluation
│   ├── Capability Evaluations
│   ├── Dangerous Capability Evals
│   └── Red Teaming
├── Robustness
│   ├── Adversarial Attacks
│   ├── Jailbreaking and Prompt Injection
│   └── Distribution Shift
├── Societal Safety
│   ├── Bias and Fairness
│   ├── Misinformation
│   └── Privacy and Surveillance
└── Catastrophic Risk
    ├── Loss of Control
    ├── Misaligned Optimization
    └── AI-enabled CBRN risks
```

---

## Prompt for Deep Content Generation

```
You are an AI safety researcher, alignment theorist, and red team lead 
writing for an audience of AI lab founders.

Write Section 18 of "Building an AI Research Lab From Scratch" — 
a comprehensive technical and strategic guide to AI safety.

Do not be dismissive of safety concerns or catastrophize them —
provide a rigorous, evidence-based analysis.

PART A — THE ALIGNMENT PROBLEM
   - Formal definition: why AI systems might pursue goals misaligned with human values
   - The specification problem: why it's hard to formally specify what we want
   - The Goodhart's Law in AI: "when a measure becomes a target, it ceases to be a good measure"
   - Reward hacking: examples in RL systems
   - Inner alignment vs. outer alignment: the mesa-optimizer problem
   - RLHF and its limitations: what it solves and what it doesn't
   - Constitutional AI (Anthropic): how it works and what it improves
   - DPO (Direct Preference Optimization): the RLHF alternative and its alignment properties

PART B — MECHANISTIC INTERPRETABILITY
   - What mechanistic interpretability (MI) is trying to achieve
   - Key findings from Anthropic and Neel Nanda's work:
     circuits, induction heads, superposition hypothesis
   - Sparse Autoencoders (SAEs): the current frontier tool for MI
   - Probing classifiers: how they work, what they reveal, their limitations
   - Activation patching: causal intervention for understanding model behavior
   - Open problems in MI: polysemanticity, scaling challenges, causal vs. correlational
   - Why MI is tractable for a small lab: it requires minimal compute, just analysis

PART C — EVALUATION AND RED TEAMING
   - Capability evaluations: what are "dangerous capabilities"?
   - ARC Evals / Apollo Research / METR: organizations doing capability evals
   - Red teaming methodologies: black-box, white-box, structured threat modeling
   - WMDP (Weapons of Mass Destruction Proxy) benchmark
   - GPQA (Graduate-Level Google-Proof Q&A) as a capability ceiling test
   - Jailbreaking: taxonomy of attack types, empirical results, defenses
   - Prompt injection: the enterprise deployment risk
   - How to run a red team with limited resources

PART D — BIAS AND FAIRNESS
   - Technical definition: what is "bias" in an ML model?
   - Demographic bias, representation bias, measurement bias
   - Fairness metrics: demographic parity, equalized odds, calibration
   - Why fairness metrics conflict with each other (impossibility theorems)
   - Bias detection tools: Fairlearn, AI Fairness 360
   - Debiasing techniques: reweighting, adversarial debiasing, post-processing

PART E — ADVERSARIAL ATTACKS AND ROBUSTNESS
   - White-box attacks: FGSM, PGD, Carlini-Wagner
   - Black-box attacks: transfer attacks, query-based attacks
   - Certified robustness: randomized smoothing
   - Adversarial training: PGD adversarial training, TRADES
   - LLM-specific attacks: universal adversarial triggers, token manipulation
   - Model stealing attacks

PART F — MODEL COLLAPSE AND TRAINING DATA RISKS
   - The model collapse problem: what happens when LLMs train on LLM-generated data
   - Theoretical analysis: Shumailov et al. (2023) results
   - Practical prevention: maintaining a "clean" human data reservoir
   - Membership inference attacks: can you tell if a data point was in training data?
   - Data poisoning: attacks on training data and defenses

PART G — AI SAFETY STRATEGY FOR A SMALL LAB
   - Why safety can be a competitive advantage, not just a cost
   - Safety as positioning: how small labs can out-safety larger ones
   - Practical safety measures for every model release:
     system prompts, refusal training, output filtering, monitoring
   - Model cards and responsible release practices
   - When NOT to release a model
   - How to engage with the safety community: ARC, Redwood, Apollo, METR

PART H — THE EXISTENTIAL RISK DEBATE
   - The "x-risk" position: Yudkowsky, Russell, Bostrom — core arguments
   - The skeptic position: LeCun, Marcus, Mitchell — core arguments
   - The middle position: what most working safety researchers actually believe
   - How your position on this affects your research agenda

Format: structured markdown, attack taxonomy tables,
safety evaluation checklist, MI technique comparison.
Depth target: ~25–30 pages with specific paper citations throughout.
```

---

## Deliverables

- [ ] AI safety research taxonomy with open problem list
- [ ] Red teaming checklist for model releases
- [ ] Bias audit procedure for model evaluation
- [ ] Model card template (including safety section)
- [ ] MI research starter guide (tools, papers, first experiments)

---

## Notes
