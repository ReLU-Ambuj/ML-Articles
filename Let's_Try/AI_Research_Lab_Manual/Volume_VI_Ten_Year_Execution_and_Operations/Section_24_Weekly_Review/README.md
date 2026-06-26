# Section 24 — Weekly Review & KPIs

**Volume:** VI — Ten-Year Execution & Operations  
**Status:** 🔲 Not Started  
**Estimated Depth:** 10–15 pages

---

## Objectives

1. Build a weekly review system that catches problems before they become crises
2. Define the right KPIs for a research lab (different from a software company)
3. Create a dashboard that tracks research velocity, team health, and financial position

---

## KPI Framework for a Research Lab

```
Research KPIs
├── Research Velocity
│   ├── Experiments run per week
│   ├── Experiments with positive results (%)
│   ├── Papers in progress / submitted / accepted
│   └── Time from idea to first experiment (days)
├── Output Quality
│   ├── Venue tier of accepted papers
│   ├── Citation count (lagging indicator)
│   └── Open source repo stars / downloads
├── Knowledge Growth
│   ├── Papers read per week
│   └── New research areas explored

Team KPIs
├── Researcher productivity (papers/experiments per person)
├── Team morale (1–5 scale, qualitative)
├── Time to hire for open positions
└── Retention rate

Financial KPIs
├── Monthly burn rate
├── Cash runway (months)
├── MRR (if product exists)
└── Grant pipeline value

Community KPIs
├── GitHub stars (weekly change)
├── Discord members (weekly change)
├── Twitter followers (weekly change)
└── HuggingFace downloads
```

---

## Prompt for Deep Content Generation

```
You are a research lab COO, management consultant, and data-driven operations 
expert writing for AI research lab founders.

Write Section 24 of "Building an AI Research Lab From Scratch" — 
a complete weekly review and KPI system for AI research labs.

PART A — WHY STANDARD KPIs DON'T WORK FOR RESEARCH LABS
   - Why "lines of code" and "story points" are the wrong metrics for research
   - The measurement problem: research quality lags 2–3 years in citations
   - Leading vs. lagging indicators: what predicts paper quality 6 months out?
   - The Goodhart's Law danger: how measuring experiments can incentivize 
     running meaningless experiments

PART B — THE RIGHT RESEARCH KPIs
   For each KPI, explain:
   - What it measures and why it matters
   - How to measure it (specific method, frequency)
   - What a "healthy" vs. "concerning" range looks like
   - What action to take if it's in the concerning range

   KPIs to define:
   Research Velocity:
   - Experiments run per researcher per week (healthy: 3–7 for ML, 1–2 for theory)
   - Experiment positive rate (healthy: 20–40% have interesting results)
   - Idea-to-experiment latency (healthy: < 1 week)
   - Paper draft in progress count (healthy: 1–3 per researcher)
   - Submission frequency (healthy: 2–4 major venue attempts per researcher per year)

   Output Quality:
   - Paper acceptance rate at tier-1 venues (healthy: 20–40%, improving)
   - Review scores (track NeurIPS/ICLR scores over time)
   - Open source engagement (stars, forks, issues, PRs)
   - External citations starting to appear

   Learning:
   - Papers read and notes taken per week
   - New area explorations per quarter
   - Seminar attendance and paper discussion quality

PART C — TEAM AND OPERATIONAL KPIs
   - Researcher satisfaction (1–5 weekly pulse, qualitative note)
   - Time blocked for deep work (hours/researcher/week, healthy: > 20 hrs)
   - Meeting overhead (hours/researcher/week, healthy: < 5 hrs)
   - Hiring funnel: applications → screens → offers → acceptances
   - Compute utilization rate (healthy: 70–90%, underutilization is waste)

PART D — FINANCIAL KPIs
   - Monthly burn rate: what it should be and how to track it
   - Cash runway: how to calculate and what minimum is safe (healthy: > 12 months)
   - Revenue run rate (if applicable): MRR and growth rate
   - Grant pipeline: value of submitted but unapproved grants
   - CAC and LTV if there's a product

PART E — THE WEEKLY REVIEW PROCESS
   Design a complete weekly review meeting / solo review session:
   
   SOLO RESEARCHER (30 minutes, Friday afternoon):
   - 5 min: experiment results review — what worked this week?
   - 5 min: paper progress check — where is each active paper?
   - 5 min: financial check — burn rate, runway
   - 5 min: community check — engagement metrics
   - 10 min: next week planning — what are the top 3 priorities?
   - Journal entry: "What did I learn this week that changed how I think?"
   
   TEAM REVIEW (60 minutes, weekly):
   - Research updates: each researcher presents 1 slide on experiments
   - Blocked items: what is each person waiting on?
   - Paper updates: submissions, reviews, rebuttal status
   - Financial update: burn rate, runway, incoming revenue
   - Community/marketing update: releases, engagement, upcoming events

PART F — THE MONTHLY REVIEW
   More comprehensive monthly review:
   - Research direction evaluation: is this area still worth pursuing?
   - Hiring review: who do we need to hire in the next 90 days?
   - Financial forecast: 6-month cash position model
   - Community health: is the open source ecosystem growing?
   - Competitive landscape: what have other labs published this month?

PART G — DASHBOARDS AND TOOLING
   - Building a research lab dashboard in Notion or Linear
   - Automated data collection: W&B API → dashboard, GitHub API → stars tracking
   - Financial dashboard: simple spreadsheet that tracks burn, runway, grant pipeline
   - Templates: weekly review document, monthly review document

Format: structured markdown, KPI tables with healthy/concerning ranges,
weekly review agenda template, dashboard screenshot mockup in ASCII.
Depth target: ~10–15 pages.
```

---

## Weekly Review Template

```markdown
## Week of [DATE] — Weekly Review

### Research
- Experiments run: __
- Positive results: __
- Papers in progress: __
- Papers submitted this week: __
- Top insight this week: ___

### Team
- Morale (1–5): __
- Blockers: ___
- Decisions needed: ___

### Financial
- Burn this week: ₹__
- Cash remaining: ₹__
- Runway: __ months
- Grant pipeline: ₹__

### Community
- GitHub stars: __ (Δ +__)
- Discord members: __ (Δ +__)

### Next Week Top 3 Priorities
1. ___
2. ___
3. ___

### What I learned that changed how I think
___
```

---

## Deliverables

- [ ] Full KPI framework with measurement methods
- [ ] Weekly review template (solo and team versions)
- [ ] Monthly review template
- [ ] Dashboard setup guide (Notion or Linear)
- [ ] Automated metrics collection setup (W&B API, GitHub API)

---

## Notes
