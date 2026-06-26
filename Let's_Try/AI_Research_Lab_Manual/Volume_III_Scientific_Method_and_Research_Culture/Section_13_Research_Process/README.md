# Section 13 — The Research Process

**Volume:** III — Scientific Method & Research Culture  
**Status:** 🔲 Not Started  
**Estimated Depth:** 20–25 pages

---

## Objectives

1. Understand the complete research loop from first idea to deployed product
2. Know how to evaluate whether a research direction is worth pursuing
3. Build a personal experiment management system
4. Understand how to move from paper to open source to commercialization

---

## The Research Loop

```
[Observation / Anomaly / Gap]
         ↓
    [Hypothesis]
    "What if X caused Y?"
         ↓
    [Experimental Design]
    Baselines, controls, metrics, ablations
         ↓
    [Preliminary Experiment]
    Quick check: is this plausible?
         ↓
    [Main Experiments]
    Full scale, multiple seeds, ablations
         ↓
    [Analysis]
    Why did it work? What does this tell us?
         ↓
    [Paper Writing]
    Claim, evidence, implications
         ↓
    [Peer Review + Rebuttal]
         ↓
    [Publication + Open Source]
         ↓
    [Community Extension]
    Others build on your work
         ↓
    [Commercialization] (if applicable)
         ↓
    [Next Research Question]
    (loop repeats, informed by prior results)
```

---

## Prompt for Deep Content Generation

```
You are a senior research scientist and lab director explaining the research process 
to a PhD student who is also founding a research lab.

Write Section 13 of "Building an AI Research Lab From Scratch" — 
the complete research process from first idea to commercialization.

PART A — IDEA TO HYPOTHESIS
   - What makes a research question researchable (vs. speculative)?
   - The hypothesis formulation process: falsifiability in ML research
   - Estimating research difficulty: how long will this take to resolve?
   - The "back of the envelope" compute estimate before starting
   - How to scope a research project for a 3-month vs. 1-year timeline
   - Research debt: why solving a small clear problem beats exploring a big fuzzy one

PART B — EXPERIMENT DESIGN
   - The null hypothesis in ML research: what is the baseline?
   - Ablation study design: how to isolate variables in complex systems
   - Evaluation metric selection: why the choice of metric changes the conclusion
   - Statistical significance in ML: why single-seed results are unreliable
     (explain: variance across seeds, confidence intervals, statistical testing)
   - Compute budget allocation: how to split budget between exploration and confirmation
   - The 80/20 rule of experiments: the first 20% of experiments give 80% of the insight

PART C — RUNNING EXPERIMENTS
   - Experiment tracking discipline: what metadata to record before pressing run
   - The experiment log: date, hypothesis, configuration, result, interpretation
   - Handling variance: how many seeds, how to aggregate results
   - Early stopping heuristics: when to kill a run vs. let it finish
   - Parallel experiments: how to design experiments that can run simultaneously
   - The "sanity check first" principle: overfit on 1 batch before full training

PART D — ANALYSIS AND INTERPRETATION
   - How to read your own results without confirmation bias
   - Why your model works: methods for causal understanding
     (ablations, probing, attention visualization, mechanistic analysis)
   - Negative results: how to extract value from failed experiments
   - The "surprisingly good result" danger: when results that look too good mean bugs
   - Reproducing your own results: why this is essential before submission

PART E — PAPER WRITING PROCESS
   - Writing timeline: when to start writing (answer: before experiments finish)
   - The paper skeleton first: structure before prose
   - Writing the results section before the intro: why this order matters
   - The "story" of a paper: what narrative arc makes reviewers engage
   - Revision cycles: self-review → peer review → advisor review → submission
   - LaTeX setup for ML papers: templates, bibliography management (BibTeX/Zotero)

PART F — OPEN SOURCE STRATEGY
   - When to open source: immediately after paper? After acceptance?
   - What to include in a research release: code, weights, data, demo
   - README quality for research repos: what frontier labs do
   - Model release checklist (safety, documentation, license selection)
   - HuggingFace Spaces demo: how to build one in 2 hours

PART G — DEPLOYMENT AND COMMERCIALIZATION
   - When does research become a product?
   - The research → API → product pipeline
   - MVP deployment: FastAPI + vLLM + cloud in 1 day
   - Pricing model for research-backed APIs
   - How to maintain a research lab while running a product team

PART H — THE FEEDBACK LOOP
   - How product usage informs the next research cycle
   - User feedback as a research signal: what it reveals about model failure modes
   - The "research agenda from product failures" technique
   - Balancing fundamental and applied research within the same lab

Format: structured markdown, experiment log template, 
paper writing checklist, timeline diagrams.
Depth target: ~20–25 pages.
```

---

## Deliverables

- [ ] Experiment design template
- [ ] Experiment log format (markdown table)
- [ ] Paper writing timeline and checklist
- [ ] Open source release checklist
- [ ] Research → product decision framework

---

## Notes
