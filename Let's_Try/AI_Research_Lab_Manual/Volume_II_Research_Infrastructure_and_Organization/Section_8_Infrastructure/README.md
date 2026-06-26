# Section 8 — Infrastructure

**Volume:** II — Research, Infrastructure & Organization  
**Status:** 🔲 Not Started  
**Estimated Depth:** 25–30 pages

---

## Objectives

1. Understand the complete technical infrastructure stack of an ML research lab
2. Know how to build each layer from scratch with specific tools and configurations
3. Design infrastructure that scales from solo to team without complete rewrites
4. Understand security, reliability, and cost optimization at each layer

---

## Infrastructure Stack Layers

```
Layer 1: Compute
   Physical servers, GPU racks, networking (InfiniBand/Ethernet)
   Cloud instances, spot instances, preemptible VMs

Layer 2: Storage
   Local NVMe, NAS, object storage (S3/GCS/R2)
   Dataset versioning, checkpoint storage

Layer 3: Orchestration
   Job schedulers: SLURM, Kubernetes, Ray
   Container management: Docker, Apptainer/Singularity

Layer 4: Distributed Training
   Data parallelism, model parallelism, pipeline parallelism
   Frameworks: DeepSpeed, FSDP, Megatron-LM

Layer 5: Experiment Tracking
   Weights & Biases, MLflow, Comet, Neptune
   Checkpointing strategies

Layer 6: Version Control & CI/CD
   Git, DVC (Data Version Control), GitHub Actions
   Model registry, dataset registry

Layer 7: Monitoring & Logging
   GPU utilization monitoring, training loss tracking
   Alerting: PagerDuty/Prometheus/Grafana

Layer 8: Security
   SSH key management, secrets management (Vault)
   Network isolation, firewall rules

Layer 9: Evaluation & Deployment
   Eval harnesses: lm-evaluation-harness, HELM
   Inference servers: vLLM, TGI, SGLang, Triton

Layer 10: Data Pipelines
   ETL pipelines, streaming data, preprocessing
   Tools: Apache Spark, Dask, HuggingFace datasets
```

---

## Prompt for Deep Content Generation

```
You are a principal infrastructure engineer at a frontier AI research lab 
writing a technical reference for founders building ML infrastructure from scratch.

Write Section 8 of "Building an AI Research Lab From Scratch" — 
a complete infrastructure reference.

Assume the reader has strong Python skills and basic Linux/systems knowledge 
but has not built large-scale ML infrastructure before.

For EACH infrastructure layer below, provide:
   - What it is and why it is necessary
   - The minimum viable setup (solo, ₹5L budget)
   - The production-grade setup (team of 10, ₹50L budget)
   - Specific tool recommendations with justification
   - Configuration examples (actual commands, not pseudocode)
   - Common mistakes and how to avoid them
   - Cost estimate per month

LAYERS TO COVER:

1. COMPUTE HARDWARE
   Physical: GPU servers, CPU servers, networking (InfiniBand vs Ethernet)
   Cloud: EC2 P4d, A2, H100 instances — how to provision and manage
   Mixed: hybrid cloud-physical setup

2. STORAGE SYSTEMS
   Local NVMe RAID for active training
   Object storage: S3, GCS, Cloudflare R2 — pricing and use cases
   Dataset versioning: DVC, LakeFS, Delta Lake
   Checkpoint storage strategy: when to checkpoint, how often, what to keep

3. JOB SCHEDULING AND ORCHESTRATION
   SLURM: installation, job submission, priority queues, fair-share scheduling
   Kubernetes: when to use it, when not to, how to set up for ML
   Ray: ray.init(), Ray Train, Ray Tune — practical setup
   Comparison table: SLURM vs. Kubernetes vs. Ray for different lab sizes

4. CONTAINERIZATION
   Docker for reproducibility: writing research Dockerfiles
   Apptainer/Singularity for HPC environments
   Container registry: Docker Hub vs. GitHub Container Registry vs. self-hosted

5. DISTRIBUTED TRAINING
   Data Parallelism: DDP (PyTorch), when and how to use
   Model Parallelism: Tensor, Pipeline, Sequence parallelism
   FSDP (Fully Sharded Data Parallel): configuration guide
   DeepSpeed: ZeRO stages 1/2/3 — when to use each
   Megatron-LM: for very large model training
   Practical guide: how to debug a distributed training job that hangs

6. EXPERIMENT TRACKING
   Weights & Biases: setup, sweeps, artifact tracking
   MLflow: self-hosted option, tracking server setup
   Checkpointing: naming conventions, storage, resuming interrupted runs
   Hyperparameter logging: what to always log

7. VERSION CONTROL AND CI/CD
   Git for code: branching strategy for research (not software engineering)
   DVC for data and models: practical tutorial
   GitHub Actions for automated testing of training scripts
   Model registry: tracking model versions, linking to experiments

8. MONITORING AND ALERTING
   GPU monitoring: nvidia-smi, DCGM, Prometheus + Grafana
   Training monitoring: loss curves, gradient norms, learning rate schedules
   Alerting: when training diverges, when GPU utilization drops
   Cost monitoring: cloud spend tracking

9. SECURITY
   SSH key management and bastion hosts
   Secrets management: environment variables vs. Vault vs. AWS Secrets Manager
   Network security: VPCs, security groups, firewall rules
   Data security: encryption at rest, access control for sensitive datasets

10. EVALUATION INFRASTRUCTURE
    lm-evaluation-harness: setup and custom task addition
    HELM: when to use vs. lm-eval
    Custom eval pipelines: how to build and automate
    Benchmark versioning: reproducible evaluation

11. INFERENCE AND DEPLOYMENT
    vLLM: installation, serving, batching, quantization
    TGI (Text Generation Inference): Hugging Face's serving solution
    SGLang: structured generation, when it wins over vLLM
    NVIDIA Triton: enterprise inference server
    Quantization: GPTQ, AWQ, GGUF — when each is appropriate

12. DATA PIPELINES
    Raw data ingestion: web scraping, API pulls, dataset downloads
    Preprocessing: tokenization at scale, deduplication (MinHash LSH)
    Quality filtering: perplexity filtering, classifier-based filtering
    HuggingFace Datasets: efficient multi-process data loading
    Streaming datasets: for datasets too large to fit in memory

REFERENCE ARCHITECTURE:
   Draw an ASCII diagram showing how all layers connect for:
   (a) A solo researcher setup
   (b) A 5-person team setup

Format: technical markdown, actual code snippets where helpful, 
cost tables, comparison matrices.
Depth target: ~25–30 pages.
```

---

## Deliverables

- [ ] Layer-by-layer infrastructure reference
- [ ] Solo researcher infrastructure setup guide (< 2 hours to complete)
- [ ] Team infrastructure setup guide
- [ ] Cost table: solo vs. team infrastructure per month
- [ ] ASCII architecture diagrams (solo, team)
- [ ] Security checklist for research data

---

## Notes
