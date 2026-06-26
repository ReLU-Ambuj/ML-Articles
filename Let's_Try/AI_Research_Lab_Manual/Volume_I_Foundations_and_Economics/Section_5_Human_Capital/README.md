# Section 5 — Human Capital

**Volume:** I — Foundations & Economics  
**Status:** 🔲 Not Started  
**Estimated Depth:** 20–25 pages

---

## Objectives

1. Know exactly which roles exist in a research lab and what each one does
2. Understand the hiring sequencing problem: who first, who never, who when
3. Build a compensation and talent acquisition model for each role
4. Design a talent strategy that can compete with better-funded labs

---

## Role Taxonomy

```
Research Roles
├── Research Scientist (RS)
├── Senior Research Scientist (SRS)  
├── Staff Research Scientist
└── Principal Researcher

Engineering Roles
├── Research Engineer (RE)
├── ML Engineer
├── Backend Engineer
├── Frontend Engineer
├── Infrastructure / Platform Engineer
└── DevOps / MLOps

Specialist Roles
├── Mathematician / Theorist
├── Statistician
├── Economist
├── Neuroscientist
├── Psychologist / Cognitive Scientist
└── Domain Scientist (Biology, Physics, Chemistry)

Business / Operations
├── Product Manager
├── Designer
├── Operations Manager
├── Legal Counsel
├── Finance / Controller
└── Recruiter
```

---

## Prompt for Deep Content Generation

```
You are a research lab director, organizational psychologist, and talent economist 
writing for an audience of solo AI research founders.

Write a graduate-level analysis of human capital for AI research labs as Section 5 
of a multi-volume manual "Building an AI Research Lab From Scratch."

PART A — ROLE DEFINITIONS AND RESPONSIBILITIES
For each of the following roles, provide:
   - Precise definition: what this person does day to day
   - The irreducible skill set: what they must know that cannot be taught quickly
   - The differentiator: what separates a great person in this role from an average one
   - How to evaluate candidates without a formal hiring process
   - Red flags in candidates for this role

Roles to cover:
   Research Scientist, Research Engineer, ML Engineer, Backend Engineer, 
   Frontend Engineer, Infrastructure Engineer, DevOps/MLOps, Mathematician/Theorist,
   Statistician, Economist, Neuroscientist, Psychologist/Cognitive Scientist,
   Designer, Product Manager, Operations, Legal Counsel.

PART B — HIRING SEQUENCING
This is the critical question: who do you hire first?

Analyze the hiring sequencing problem for a solo founder going from 1 → 2 → 5 → 10 → 25 people.

For each transition (1→2, 2→5, 5→10, 10→25), answer:
   - What is the bottleneck that forces this hire?
   - What role relieves that bottleneck?
   - What is the cost-benefit of waiting 6 more months before hiring?
   - What is the minimum viable person for this role (not ideal, minimum)?

Include: the "first research engineer" problem — why this is the hardest hire in a lab.

PART C — TALENT STRATEGY FOR CAPITAL-CONSTRAINED LABS
Given that you cannot match Big Tech salaries, analyze:

   Non-salary compensation levers:
   - Equity structure: what % for early research scientist? Range and vesting cliff.
   - Research freedom: how to document and offer this credibly
   - Publication policy: publishing everything vs. selective publishing as a talent signal
   - Prestige of problem: how problem selection attracts talent
   - Co-authorship: how offering authorship on papers substitutes for salary
   
   Alternative talent acquisition:
   - Collaborator model: unpaid or lightly paid academics who co-author
   - Contractor model: project-by-project ML engineers
   - Intern pipeline: IITs, IISc, CMI, IISERs in India — how to build this pipeline
   - Open source contributor → employee pipeline
   - PhD student collaboration through advisors

PART D — COMPENSATION ANALYSIS
Provide detailed salary/compensation analysis for each role:

India market (Bengaluru/Hyderabad/Pune):
   - Junior (0–2 years): range in LPA
   - Mid (3–5 years): range in LPA
   - Senior (6–10 years): range in LPA
   - Principal/Staff: range in LPA

Global market (San Francisco):
   - Junior, Mid, Senior, Staff ranges in USD/year

Remote-first strategy:
   - Hiring senior talent in Tier-2 Indian cities: 40–60% discount
   - Hiring in Eastern Europe, Latin America, Southeast Asia

PART E — CULTURE AND RESEARCH PRODUCTIVITY
   - What organizational structures maximize research output?
     (Compare: flat vs. hierarchical, team-based vs. solo, open vs. competitive)
   - How do frontier labs (DeepMind, FAIR) organize research teams internally?
   - The "principal researcher autonomy" model vs. directed research
   - How to prevent talent attrition in years 2–4 when you cannot match Big Tech raises
   - The founder's relationship with the first research scientist hire

PART F — WHEN EACH ROLE BECOMES NECESSARY
Build a decision tree:
   - Year 0: Solo founder — what you must do yourself
   - Year 1 trigger conditions for first hire
   - Year 2 trigger conditions for 3rd and 4th hire
   - Year 3–5: specialization begins — when do you need a dedicated theorist?
   - Year 5+: when do legal, finance, and operations become full-time?

PART G — PEOPLE YOU SHOULD NEVER HIRE
   - The "big company ex-research-manager" problem
   - The "pure theorist with no implementation instinct" problem
   - The "product manager in a research lab" problem (and when it's right)
   - The "hire fast fire fast" myth in research contexts

Format: structured markdown, salary tables in INR and USD, 
role vs. stage hiring timeline table, red flag lists per role.
Depth target: ~20–25 pages equivalent.
```

---

## Key References

- Sutton, R. & Barto, A. (2018). *Reinforcement Learning: An Introduction.* (Chapter on research methodology)
- Goodhart's Law applied to research productivity metrics
- DeepMind hiring philosophy: public talks by Demis Hassabis
- FAIR organizational design: Yann LeCun public talks
- Indian ML salary survey: AIM, Analytics Vidhya, Glassdoor India

---

## Deliverables

- [ ] Role-by-role analysis (16 roles)
- [ ] Hiring sequencing decision tree (1 → 25 people)
- [ ] Compensation table (India + global, by seniority)
- [ ] Talent acquisition strategy document for capital-constrained labs
- [ ] "Never hire" anti-pattern list

---

## Notes

_(Notes here)_
