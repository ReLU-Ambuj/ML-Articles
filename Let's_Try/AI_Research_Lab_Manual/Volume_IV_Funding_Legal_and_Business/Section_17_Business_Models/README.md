# Section 17 — Business Models

**Volume:** IV — Funding, Legal & Business  
**Status:** 🔲 Not Started  
**Estimated Depth:** 20–25 pages

---

## Objectives

1. Understand every viable business model for an AI research lab
2. Know which models preserve research independence and which destroy it
3. Design a business model that funds fundamental research sustainably
4. Understand the unit economics and profitability path of each model

---

## Business Model Taxonomy

```
AI Lab Business Models
├── Pure Research (Non-profit / Academic)
│   └── Funded by grants, philanthropy, government
├── Foundation Model Company
│   ├── API (inference revenue)
│   ├── Enterprise (custom deployments, SLAs)
│   └── Consumer subscriptions
├── Research Consultancy
│   └── Custom research, advisory, training
├── Vertical AI
│   ├── Healthcare AI
│   ├── Finance AI
│   ├── Legal AI
│   ├── Education AI
│   └── Scientific Discovery
├── Infrastructure / Platform
│   ├── ML tools (W&B, Comet, LangSmith model)
│   └── Developer platform (HuggingFace model)
├── Open Core
│   ├── Open source + premium features
│   └── Open source + managed cloud
├── Robotics
│   └── Embodied AI products
└── Data / Evaluation as a Service
    └── Benchmarks, eval platforms, data curation
```

---

## Prompt for Deep Content Generation

```
You are a business strategist, economist, and research lab founder writing 
for an audience building a research-first AI company.

Write Section 17 of "Building an AI Research Lab From Scratch" — 
a complete analysis of business models for AI research labs.

Emphasize the tension between funding research and commercial execution.
Be specific about unit economics, profitability timelines, and failure modes.

PART A — THE CORE TENSION
   - Why pure research labs need money and why money changes research
   - The "research for research's sake" vs. "research for product" spectrum
   - How to design a business model that funds fundamental research without corrupting it
   - The spin-off model: pure research → applied research → product → subsidiary
   - Examples: DeepMind (research → AlphaFold → DeepMind Health), 
     FAIR (research → Meta AI products), OpenAI (research → API → ChatGPT)

PART B — FOUNDATION MODEL COMPANY MODEL
   - API model: pay-per-token pricing, how to set it, what margin is realistic
   - Enterprise model: custom fine-tuning, private deployments, SLAs
   - Consumer subscription: $20/month model — what revenue scales are possible?
   - The "hyperscaler dependency" risk: OpenAI on Azure, Anthropic on AWS
   - Unit economics: cost per API call vs. revenue per API call at scale
   - Gross margin analysis: inference cost vs. revenue (GPT-3.5 estimated at 80%+)
   - Path to profitability: typical timeline for a foundation model company

PART C — RESEARCH CONSULTANCY MODEL
   - What research consulting is: not generic ML consulting but research expertise
   - Typical projects: custom training data strategy, novel architecture evaluation,
     benchmark design, safety evaluation
   - Pricing: project-based ($50K–$500K) vs. retainer ($20K–$100K/month)
   - Client types: governments, large enterprises, other AI companies
   - How consulting funds research: the intellectual surplus model
   - Risk: consulting becomes the core business and kills research

PART D — VERTICAL AI MODEL
   For each vertical (Healthcare, Finance, Legal, Scientific Discovery, Education):
   - Specific AI problems that are solved and worth paying for
   - Revenue model: SaaS, usage-based, outcome-based (e.g., drug discovery)
   - Regulatory requirements: FDA, HIPAA, SEC, etc.
   - Competitive landscape: is this vertical saturated or open?
   - Research integration: what research questions does the vertical naturally generate?
   - Case study: one company per vertical (e.g., Recursion Pharmaceuticals for biotech)

PART E — OPEN CORE MODEL
   - What open core means: open foundation + paid enterprise layer
   - Examples: Weights & Biases, MLflow (Databricks), MinIO, Grafana
   - What features go in the free tier vs. the paid tier
   - The "open source then charge for cloud" pattern (HashiCorp, MongoDB)
   - License risk: GPL relicensing controversy, BSL (Business Source License)
   - Revenue projections: what % of free users convert to paid?

PART F — INFRASTRUCTURE / PLATFORM MODEL
   - The developer tools market: how companies like W&B, Comet, Scale AI generate revenue
   - Building ML tooling as a research lab: why it generates community faster than papers
   - Platform network effects: why HuggingFace is worth $4.5B
   - API platform strategy: designing an API that developers build on top of

PART G — ROBOTICS AND EMBODIED AI MODEL
   - Hardware + software revenue: why robotics businesses have different economics
   - B2B robotics: warehouse automation, manufacturing, agriculture
   - The research → hardware product pipeline: timelines and capital requirements
   - Battery/actuator/sensor costs and trends

PART H — UNIT ECONOMICS DEEP DIVE
   Create a unit economics model for each major business model:
   - Revenue per customer
   - Gross margin
   - Customer acquisition cost (CAC)
   - Lifetime value (LTV)
   - LTV/CAC ratio (must be > 3 for a viable business)
   - Time to payback
   - Monthly burn rate vs. MRR growth

PART I — CHOOSING A BUSINESS MODEL
   - Decision framework: research depth, capital efficiency, time to revenue
   - The "research lab → product company" transition: when and how
   - Avoiding premature productization: the research lab failure mode
   - Building a hybrid: research division + product division under one entity
   - When to spin off a product company from the research lab

Format: structured markdown, unit economics tables,
business model comparison matrix, revenue projection examples.
Depth target: ~20–25 pages.
```

---

## Deliverables

- [ ] Business model comparison matrix
- [ ] Unit economics template for each model
- [ ] Revenue projection model (simple spreadsheet-style table)
- [ ] Business model selection decision tree
- [ ] Vertical AI opportunity ranking by tractability for small labs

---

## Notes
