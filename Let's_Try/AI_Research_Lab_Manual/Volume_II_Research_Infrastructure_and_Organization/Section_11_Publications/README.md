# Section 11 — Publications

**Volume:** II — Research, Infrastructure & Organization  
**Status:** 🔲 Not Started  
**Estimated Depth:** 20–25 pages

---

## Objectives

1. Understand the academic publication system: venues, review processes, timelines
2. Learn how frontier research papers are actually written and structured
3. Develop a personal publication strategy for maximum scientific impact
4. Master the arXiv preprint strategy used by top labs

---

## The Publication Pipeline

```
Idea Generation
    ↓
Literature Review (weeks)
    ↓
Hypothesis Formulation
    ↓
Experiment Design
    ↓
Preliminary Experiments (weeks–months)
    ↓
Main Experiments (weeks–months)
    ↓
Paper Writing (2–6 weeks)
    ↓
Internal Review (1–2 weeks)
    ↓
arXiv Preprint (optional)
    ↓
Conference/Journal Submission
    ↓
Peer Review (2–4 months)
    ↓
Rebuttal (2 weeks)
    ↓
Decision (acceptance / rejection / revision)
    ↓
Camera-Ready (2 weeks)
    ↓
Presentation + Open Source Release
```

---

## Prompt for Deep Content Generation

```
You are a frontier AI researcher with 50+ publications at NeurIPS, ICLR, ICML, 
ACL, and Nature, writing a publishing guide for early-career researchers and lab founders.

Write Section 11 of "Building an AI Research Lab From Scratch" — 
a complete guide to publishing AI research.

PART A — THE PUBLICATION ECOSYSTEM
   - Conference vs. journal publishing in AI: why conferences dominate
   - Tier 1 conferences by area:
     ML/DL: NeurIPS, ICLR, ICML
     NLP: ACL, EMNLP, NAACL
     Vision: CVPR, ICCV, ECCV
     Robotics: CoRL, ICRA, RSS
     Systems: MLSys, OSDI, SOSP (for ML systems papers)
     AI: AAAI, IJCAI
   - For each tier-1 conference: submission deadline calendar, review timeline, 
     acceptance rate, paper length, reviewer assignment process
   - Workshop papers vs. main track: when workshops matter for a new lab
   - Journal publishing: JMLR, TACL, Nature, Science — when and why

PART B — HOW IDEAS FOR FRONTIER PAPERS EMERGE
   - The idea generation process at top labs (based on public accounts)
   - Observational approach: noticing something surprising in experiments
   - Principled approach: starting from a theoretical gap
   - Engineering approach: "what if we just scaled X?"
   - The "stolen" idea problem: how to protect ideas during the development phase
   - Idea journaling: how to systematically track and develop half-baked ideas
   - How to tell a good research idea from a bad one before spending compute

PART C — LITERATURE REVIEW AT RESEARCH LEVEL
   - Efficient reading strategy: abstract → intro → conclusion → experiments → full
   - Connected Papers, Semantic Scholar, Elicit — how to use them for lit review
   - Building a personal knowledge graph of the literature
   - Citation mapping: how to trace the genealogy of an idea back 10 years
   - How to read a paper in 20 minutes vs. how to deeply understand it in 2 hours
   - Reproducing papers: the fastest way to deeply understand a method

PART D — PAPER STRUCTURE AND WRITING
   - The anatomy of a NeurIPS/ICLR paper:
     Abstract (150–200 words): what you did, why it matters, key result
     Introduction: problem, why hard, why now, your key insight, contributions
     Related Work: not a survey — compare and contrast to justify your approach
     Method: the core technical contribution
     Experiments: ablations, baselines, main results, failure cases
     Discussion/Conclusion: what you proved, what you didn't, future work
   
   - Writing the abstract: the 4-sentence formula
   - Writing the introduction: the problem-solution-impact structure
   - Experiment section design: how to choose baselines, how to design ablations
   - Figure design: what makes a great paper figure
   - Common writing mistakes in ML papers (and how to avoid them)
   - Writing in LaTeX: essential packages for ML papers (neurips2024, iclr2025)

PART E — HOW TO PERFORM LITERATURE REVIEW AND FIND GAPS
   - Survey papers as gap maps
   - Reading 100 papers in a month: systematic approach
   - The "open problem" section in survey papers — how to exploit it
   - Negative results in literature: why they're underreported and how to find them
   - Replication failures: what they reveal about gaps
   - The "what hasn't been tried" heuristic

PART F — ARXIV STRATEGY
   - When to post to arXiv (before submission? after acceptance?)
   - arXiv vs. embargo policy at different conferences
   - How to write an arXiv abstract that gets 10K downloads
   - Timing: why posting on Monday morning matters
   - Twitter/X announcement strategy for paper launches
   - Version management: when to update arXiv preprints

PART G — PEER REVIEW UNDERSTANDING
   - How peer review works at NeurIPS/ICLR/ICML
   - Area Chairs, Senior Area Chairs, Program Chairs — the hierarchy
   - What reviewers look for (and what irritates them)
   - How to write a rebuttal that actually changes reviewer opinions
   - Desk rejection: how to avoid it
   - Reviewer calibration: why a 6/10 score means different things at different venues

PART H — PUBLICATION STRATEGY FOR A NEW LAB
   - How to build a publication track record with no compute and no team
   - Positioning theory papers: advantage of small labs
   - Workshop papers as pipeline for main track submissions
   - Co-authorship strategy: collaborating with established researchers
   - The "one strong paper" theory vs. "quantity" strategy
   - How many papers is too few to establish a lab's credibility?
   - Building an arXiv presence and Google Scholar profile from zero

PART I — OPEN SOURCE AND RESEARCH IMPACT
   - Why open-sourcing code triples citation rate (empirically)
   - The paper + code + demo trifecta
   - HuggingFace Model Hub as research impact amplifier
   - Papers With Code: how to get listed and why it matters

Format: structured markdown, conference calendar table, 
paper structure template, rebuttal writing guide.
Depth target: ~20–25 pages.
```

---

## Conference Calendar (Approximate)

| Conference | Submission | Notification | Event |
|------------|-----------|--------------|-------|
| NeurIPS | May | September | December |
| ICLR | October | January | May |
| ICML | February | May | July |
| ACL | February | May | August |
| EMNLP | June | September | November |
| CVPR | November | March | June |
| ICCV (odd years) | March | July | October |

---

## Deliverables

- [ ] Personal publication strategy document
- [ ] Paper writing template (LaTeX-ready structure)
- [ ] Rebuttal writing guide
- [ ] arXiv announcement checklist
- [ ] Conference calendar 2026–2027
- [ ] Lit review system setup (Connected Papers + Zotero + Obsidian)

---

## Notes
