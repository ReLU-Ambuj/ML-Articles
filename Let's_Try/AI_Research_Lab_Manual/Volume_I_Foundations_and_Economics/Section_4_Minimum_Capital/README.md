# Section 4 — Minimum Capital Scenarios

**Volume:** I — Foundations & Economics  
**Status:** 🔲 Not Started  
**Estimated Depth:** 20–25 pages

---

## Objectives

1. Develop three concrete, actionable financial plans for different starting capital levels
2. Understand exactly what compute, software, and infrastructure each budget unlocks
3. Know which research areas are tractable at each budget level and which are not
4. Build a timeline of expected outputs with honest risk assessment

---

## The Three Scenarios

| Scenario | Capital | Classification |
|----------|---------|----------------|
| A | ₹50,000 (~$600) | Bootstrapped, cloud-only, solo |
| B | ₹5,00,000 (~$6,000) | Seed-level personal capital |
| C | ₹50,00,000 (~$60,000) | Early-stage, small team feasible |

---

## Prompt for Deep Content Generation

```
You are a compute economist, ML systems engineer, and research lab founder.

Write a highly specific, realistic financial and operational analysis of three 
capital scenarios for starting an AI research lab from scratch in India in 2026.
This is Section 4 of a multi-volume manual "Building an AI Research Lab From Scratch."

Include real prices (cloud GPU rates, hardware costs, software subscriptions).
No optimism bias — include failure modes and realistic timelines.

SCENARIO A — ₹50,000 (~$600)

Hardware:
   - No owned GPU hardware at this budget
   - Analyze: Google Colab Pro+, Kaggle, Lambda Labs, RunPod, Vast.ai, 
     Lightning AI, Modal — current pricing, limitations, hidden costs
   - Can you train a 7B parameter model on this budget? A 1B? A 100M?
   - What is the compute ceiling in FLOPs given ₹50,000 on cloud?

Software & Infrastructure:
   - Free tier stack: GitHub, HuggingFace Hub, Weights & Biases (free), 
     wandb, Colab, VS Code
   - Cost of essential subscriptions: Overleaf, Zotero, GitHub Pro

Hiring:
   - Solo only. No hiring possible.
   - Collaborator network strategy: open source contributions, 
     academic collaborations, Discord communities

Research that IS possible at this budget:
   - Fine-tuning open models (LoRA, QLoRA)
   - Interpretability research on small models
   - Mathematical theory contributions (no compute needed)
   - Dataset curation and benchmark creation
   - Paper replications for learning

Research NOT possible at this budget:
   - Pre-training frontier models
   - Large-scale RL experiments
   - Compute-intensive ablation studies

Expected output in 12 months:
   - Realistic paper targets (1–2 papers? 0?)
   - Open source contributions
   - Benchmark contributions
   
Expected timeline for each output type.
Risks: underestimate compute cost, cloud bill shock, no paper = no credibility path.

---

SCENARIO B — ₹5,00,000 (~$6,000)

Hardware:
   - Can you buy a used GPU? 
     (RTX 3090 ₹60,000, RTX 4090 ₹1,20,000 — analyze second-hand market)
   - Analysis: own-hardware vs. cloud at this budget
   - If cloud only: how many A100-hours does ₹5L buy? 
     (Lambda Labs: ~$1.10/hr for A100 → ~5,500 GPU-hours)
   - If hybrid: one RTX 4090 + cloud credits

Software & Infrastructure:
   - Paid tools: Weights & Biases Team, GitHub Team, domain + hosting
   - MLFlow vs wandb vs Comet — cost comparison
   - Storage: S3 vs Backblaze B2 vs Cloudflare R2 (cost per TB)

Hiring:
   - Potentially one part-time collaborator (intern, PhD student)
   - Stipend range for Indian ML intern: ₹15,000–₹30,000/month
   - ₹5L ÷ ₹20K/month = 25 months solo OR 8 months with one intern + cloud

Research that IS possible:
   - Pre-training small models (<1B parameters) from scratch
   - Full RLHF pipeline experiments on small models
   - Systematic ablation studies on architecture choices
   - Producing 2–4 competitive workshop papers at NeurIPS/ICLR/ICML
   
Expected output in 12 months.
Timeline with milestones.
Risks: compute overrun, hardware failure without warranty, burn rate.

---

SCENARIO C — ₹50,00,000 (~$60,000)

Hardware:
   - Analyze: building a 4× or 8× GPU server
   - NVIDIA H100 SXM: ~$30,000 each (₹25L+) — not feasible
   - NVIDIA A100 80GB PCIe: ~$15,000 (₹12.5L) 
   - RTX 4090 ×8 server: ~$15,000–$20,000 (₹12–17L) — feasible
   - Full build spec: GPU + CPU + RAM + NVMe + networking + power
   - Ongoing cost: electricity (~₹5–10/unit in India), cooling, maintenance
   - Break-even vs. cloud rental analysis

Software & Infrastructure:
   - Kubernetes or bare metal Slurm cluster setup
   - Monitoring: Prometheus + Grafana
   - Experiment tracking: wandb Teams
   - Storage: local NAS + S3 backup
   - VPN + security

Hiring:
   - First hire analysis: Research Engineer vs. Research Scientist vs. ML Engineer
   - Salary ranges in India (Bengaluru/Hyderabad): 
     Junior: ₹8–15L/yr, Mid: ₹18–35L/yr, Senior: ₹40–80L/yr
   - ₹50L ÷ ₹12L/yr (junior RE) = ~4 years solo OR team of 2 for 2 years
   - Recommended: 1 junior Research Engineer + compute investment

Research that IS possible:
   - Pre-training models up to 3B–7B parameters
   - Competitive NeurIPS/ICLR/ICML submissions
   - Building a benchmark dataset with human annotation (outsourced)
   - Running a small open-source model release

Expected output in 24 months.
Milestones per 6-month sprint.
Risks: team conflict, hardware failure, research dead-ends.

---

CROSS-SCENARIO ANALYSIS
   - Create a comparison table: capital vs. compute capacity vs. expected publications vs. timeline to first revenue
   - The compounding effect: how ₹50K in publications can unlock ₹50L in grants
   - Capital efficiency ranking: which research areas give most output per rupee?
   - The "leverage points": what activities have 10× return (open source, conferences, Twitter presence)?

Format: structured markdown with tables, cost breakdowns, 
ASCII compute capacity diagrams, explicit failure modes per scenario.
All prices in both INR and USD.
Depth target: ~20–25 pages.
```

---

## Key Resources

- Lambda Labs GPU pricing: https://lambdalabs.com/service/gpu-cloud
- RunPod pricing: https://www.runpod.io/gpu-instance/pricing
- Vast.ai marketplace: https://vast.ai/
- Backblaze B2 pricing: https://www.backblaze.com/cloud-storage/pricing
- Indian GPU hardware market: OLX, Rashi Peripherals, MD Computers

---

## Deliverables

- [ ] Scenario A budget breakdown + research plan
- [ ] Scenario B budget breakdown + research plan
- [ ] Scenario C budget breakdown + research plan
- [ ] Capital efficiency comparison table
- [ ] Cloud GPU cost comparison spreadsheet (actual 2026 prices)
- [ ] Hardware purchase decision tree

---

## Notes

_(Track actual prices as you research — these change frequently)_
