# Section 9 — Compute Strategy

**Volume:** II — Research, Infrastructure & Organization  
**Status:** 🔲 Not Started  
**Estimated Depth:** 15–20 pages

---

## Objectives

1. Make an informed, quantitative decision: buy vs. rent vs. cloud
2. Understand the economics of each compute acquisition strategy
3. Know how to maximize research output per compute dollar
4. Design a compute roadmap as the lab scales

---

## Decision Framework

```
Compute Options
├── Own Hardware
│   ├── Consumer GPUs (RTX 4090, RTX 3090)
│   ├── Professional GPUs (A100, H100, H200)
│   └── Full server builds (8× GPU nodes)
├── Cloud Computing
│   ├── Reserved instances (1–3 year commitment)
│   ├── On-demand instances
│   └── Spot/Preemptible instances
├── GPU Rental Marketplaces
│   ├── Lambda Labs
│   ├── RunPod
│   ├── Vast.ai
│   ├── CoreWeave
│   └── Together AI
└── Academic / Free Resources
    ├── Google Colab / TPU Research Cloud
    ├── Kaggle
    └── University HPC clusters
```

---

## Prompt for Deep Content Generation

```
You are an ML infrastructure economist and systems engineer writing 
a compute strategy guide for AI research labs.

Write Section 9 of "Building an AI Research Lab From Scratch" — 
a rigorous, quantitative compute strategy guide.

PART A — GPU HARDWARE ANALYSIS
For each of the following GPU families, provide:
   - Architecture name and generation
   - VRAM capacity options
   - FP16 TFLOPS / BF16 TFLOPS / INT8 TOPS
   - Memory bandwidth (GB/s)
   - NVLink / NVSwitch interconnect support
   - Power consumption (TDP)
   - Current market price (new and used, as of 2025–2026)
   - Best use cases (fine-tuning, pre-training, inference)
   - Effective cost per TFLOP per dollar

GPUs to analyze:
   Consumer: RTX 3090, RTX 4090, RTX 5090 (if available)
   Professional/Data Center: A100 40GB, A100 80GB, H100 SXM, H100 PCIe, 
                              H200, B100/B200 (upcoming)
   Alternative: AMD MI300X, Intel Gaudi 3

PART B — BUY VS. RENT ANALYSIS
Build a full economic model:

   Assumptions:
   - Training job: 7B parameter model, 100B tokens
   - Hardware: 8× H100 SXM (owned) vs. Lambda Labs 8× H100 (rented at $24/hr)
   - Owned hardware: $200,000 purchase, 3-year depreciation, 
     $500/month electricity, $200/month maintenance
   
   Calculate:
   - Break-even point: at what utilization % does owning become cheaper?
   - If utilization < X%, rent is better. What is X for each hardware class?
   - Total 3-year cost of ownership vs. rental
   
   Then analyze for a solo researcher:
   - At ₹5L budget, what is the economically correct decision?
   - At ₹50L budget?

PART C — CLOUD PROVIDER COMPARISON
Compare AWS, GCP, Azure, CoreWeave, Lambda Labs for:
   - H100 instance pricing (on-demand, reserved, spot)
   - Availability and reliability
   - Networking (inter-node bandwidth for distributed training)
   - Storage integration
   - Startup credits programs (AWS Activate, Google for Startups, Azure for Startups)
   - How to access $100K–$350K in cloud credits as a startup

PART D — SPOT/PREEMPTIBLE INSTANCE STRATEGY
   - What research workloads can tolerate preemption?
   - How to design training jobs that checkpoint and resume automatically
   - Spot instance survival strategies: bid pricing, region diversification
   - Cost savings from spot vs. on-demand: realistic numbers (60–90% cheaper)
   - Tools: AWS Spot Fleet, GCP Preemptible, Vast.ai interrupt handling

PART E — CONSUMER GPU STRATEGY
   - When does the RTX 4090 make sense for research?
   - Multi-GPU consumer setup: 2×, 4×, 8× RTX 4090
   - NVLink absence on consumer GPUs: workarounds (GLOO, gradient checkpointing)
   - Power and cooling requirements for home/office setup
   - Comparison: 8× RTX 4090 ($15,000) vs. 1× H100 ($30,000) for LLM research

PART F — DISTRIBUTED TRAINING ECONOMICS
   - Communication bottleneck: when does inter-node bandwidth limit scaling?
   - InfiniBand HDR (200Gb/s) vs. Ethernet (100GbE) cost comparison
   - When to scale vertically (bigger GPU) vs. horizontally (more GPUs)
   - The "critical batch size" concept and its effect on compute strategy
   - Gradient accumulation as a poor man's multi-GPU training

PART G — COMPUTE ROADMAP
Design a compute scaling roadmap for a research lab:
   Year 0 (solo): cloud only — specific recommendation
   Year 1: first owned hardware — specific recommendation
   Year 2: small cluster — specific recommendation  
   Year 3: production cluster — specific recommendation
   Year 5: data center scale

For each year: total compute capacity (A100-equivalents), 
monthly cost, expected training job size.

Format: structured markdown, cost comparison tables, 
break-even calculation formulas, ASCII cost curves.
Depth target: ~15–20 pages.
```

---

## Deliverables

- [ ] GPU comparison table (all major chips, 2026 prices)
- [ ] Buy vs. rent break-even calculator (as a markdown formula table)
- [ ] Cloud provider comparison matrix
- [ ] Spot instance strategy guide
- [ ] Compute roadmap: Year 0 → Year 5

---

## Notes
