# Section 22 — Technical Stack

**Volume:** VII — Technical Reference & Appendices  
**Status:** 🔲 Not Started  
**Estimated Depth:** 25–30 pages

---

## Objectives

1. Build comprehensive proficiency in every layer of the AI research technical stack
2. Know when to use each tool and what its trade-offs are
3. Set up a complete research development environment from scratch
4. Understand low-level performance optimization (CUDA, Triton, C++)

---

## Full Technical Stack Map

```
Languages
├── Python (primary research language)
├── CUDA C/C++ (GPU kernel programming)
├── C++ (systems, inference engines)
├── Rust (performance-critical infrastructure)
└── Julia (scientific computing, niche)

ML Frameworks
├── PyTorch (primary)
├── JAX (functional, JIT, TPU support)
├── TensorFlow (legacy support)
└── MLX (Apple Silicon research)

Distributed Training
├── PyTorch FSDP
├── DeepSpeed (ZeRO stages)
├── Megatron-LM (tensor/pipeline parallelism)
└── Ray Train

GPU Optimization
├── NVIDIA CUDA toolkit
├── cuBLAS, cuDNN, cuSPARSE
├── Triton (Python-level GPU kernel writing)
├── FlashAttention / FlashAttention-2
└── CUTLASS (CUDA Templates for Linear Algebra)

Inference & Serving
├── vLLM (PagedAttention, continuous batching)
├── SGLang (structured generation)
├── TGI (HuggingFace Text Generation Inference)
├── NVIDIA TensorRT / TensorRT-LLM
└── ONNX Runtime

Experiment Management
├── Weights & Biases (wandb)
├── MLflow
├── Comet ML
└── Neptune AI

Orchestration & MLOps
├── Ray (distributed compute)
├── Kubernetes (container orchestration)
├── SLURM (HPC job scheduling)
├── Docker / Apptainer
└── GitHub Actions (CI/CD)

Data & Storage
├── HuggingFace Datasets
├── WebDataset
├── DVC (Data Version Control)
├── Apache Arrow / Parquet
└── LanceDB (vector search)

Monitoring
├── Prometheus + Grafana
├── DCGM (GPU monitoring)
└── Sentry (error tracking)
```

---

## Prompt for Deep Content Generation

```
You are a senior ML systems engineer and performance optimization expert 
writing a technical reference for AI researchers.

Write Section 22 of "Building an AI Research Lab From Scratch" — 
a comprehensive technical stack reference.

For EACH technology, provide:
   - What it is and what problem it solves
   - When to use it vs. alternatives
   - Installation and basic setup (OS: Ubuntu 22.04 / macOS)
   - The 5 most important commands or APIs to know
   - Performance characteristics and limitations
   - Common pitfalls and how to avoid them
   - Resources: official docs, best tutorials, example repos

PART A — PYTHON FOR ML RESEARCH
   - Python version management: pyenv, conda, uv — comparison and recommendation
   - Essential libraries: NumPy, Pandas, Matplotlib, Seaborn, SciPy, Scikit-learn
   - Python performance: vectorization, numba JIT, multiprocessing
   - Virtual environments: conda vs. venv vs. uv — when to use each
   - Python profiling: cProfile, line_profiler, memory_profiler

PART B — PYTORCH IN DEPTH
   - Tensor operations: the 20 most important tensor operations for ML research
   - Autograd: how it works, gradient tapes, when to use no_grad()
   - Custom autograd functions: torch.autograd.Function
   - DataLoader and Dataset: efficient data loading for training
   - torch.compile: what it does, when to use, current limitations
   - DDP (DistributedDataParallel): setup, debugging, gradient synchronization
   - FSDP (FullyShardedDataParallel): configuration guide for large models
   - Mixed precision training: torch.cuda.amp, BF16 vs. FP16
   - Memory optimization: gradient checkpointing, activation offloading

PART C — JAX FOR RESEARCH
   - The JAX mental model: pure functions, no in-place operations
   - jit, vmap, grad, pmap — the four transformations
   - When JAX beats PyTorch (and when it doesn't)
   - Flax and Optax: JAX's ML libraries
   - JAX on TPUs: the TPU Research Cloud access program
   - JAX gotchas: random number handling, tracing vs. execution

PART D — CUDA AND GPU PROGRAMMING
   - How GPUs work: SIMD, warps, thread blocks, shared memory
   - CUDA kernel anatomy: grid, block, thread hierarchy
   - Memory hierarchy: global, shared, registers, L1/L2 cache
   - Writing your first CUDA kernel: vector addition example
   - cuBLAS for matrix multiplication: when and how
   - Profiling CUDA code: Nsight Compute, nvprof
   - Common CUDA bugs: race conditions, bank conflicts, memory coalescing

PART E — TRITON: GPU KERNELS IN PYTHON
   - What Triton is and why it exists (between Python and CUDA)
   - Triton kernel anatomy: @triton.jit decorator, tl.load/store
   - Writing a fused attention kernel (simplified)
   - FlashAttention-2 concepts: how it achieves IO-awareness
   - When Triton wins over raw CUDA
   - Triton debugging and profiling

PART F — RUST AND C++ FOR AI INFRASTRUCTURE
   - When Rust is appropriate: data processing pipelines, tokenizers, inference servers
   - HuggingFace Tokenizers (Rust): why it's 10–100× faster than Python tokenizers
   - Candle (HuggingFace's Rust ML library): when to use it
   - C++ for inference: llama.cpp as a case study
   - GGUF format: understanding quantized model files

PART G — DEEPSPEED AND MEGATRON-LM
   - DeepSpeed ZeRO: Stage 1 (optimizer state), Stage 2 (+ gradients), Stage 3 (+ parameters)
   - ZeRO-Infinity: CPU and NVMe offloading
   - When to use ZeRO-3 vs. FSDP: performance comparison
   - Megatron-LM: tensor parallelism, pipeline parallelism, sequence parallelism
   - Setting up a 3D parallelism (tensor + pipeline + data) training run

PART H — VLLM AND INFERENCE OPTIMIZATION
   - PagedAttention: how it works and why it matters
   - Continuous batching: why it 5–20× improves GPU utilization
   - vLLM setup: installation, serving command, API usage
   - Quantization in vLLM: GPTQ, AWQ, FP8
   - SGLang: when it beats vLLM (structured generation, RadixAttention)
   - TensorRT-LLM: NVIDIA's optimized inference engine

PART I — EXPERIMENT TRACKING (WANDB IN DEPTH)
   - wandb.init, wandb.log, wandb.watch — the essentials
   - Sweeps: hyperparameter optimization with wandb
   - Artifacts: tracking datasets, models, evaluations
   - Reports: sharing results with collaborators
   - wandb offline mode: for air-gapped clusters
   - Alternative: MLflow setup for self-hosted experiment tracking

PART J — RAY FOR DISTRIBUTED RESEARCH
   - ray.init and the Ray cluster setup
   - Ray Remote: distributing Python functions
   - Ray Train: distributed ML training
   - Ray Tune: hyperparameter search at scale
   - Ray Serve: model serving
   - Ray Data: distributed data processing

PART K — KUBERNETES FOR ML
   - When you need Kubernetes (team of 5+, multiple GPU nodes)
   - k8s concepts for ML engineers: pods, deployments, jobs, services
   - GPU workloads in k8s: NVIDIA device plugin
   - Kubeflow: ML workflows on Kubernetes
   - Helm for ML deployments: model serving charts

Format: structured markdown, code snippets for key operations,
installation commands (Ubuntu 22.04), performance benchmark tables.
Depth target: ~25–30 pages.
```

---

## Quick Reference: Tool Selection Decision Tree

```
Training a model?
├── < 7B parameters, single GPU → PyTorch + DDP
├── 7B–70B parameters, multi-GPU → PyTorch FSDP or DeepSpeed ZeRO-3
└── > 70B parameters, multi-node → Megatron-LM + DeepSpeed

Serving a model?
├── Development / low traffic → vLLM standalone
├── Production, unstructured → vLLM with OpenAI-compatible API
├── Production, structured output → SGLang
└── NVIDIA enterprise → TensorRT-LLM

Tracking experiments?
├── Solo researcher, budget-conscious → wandb free tier
├── Team, privacy needed → MLflow self-hosted
└── Team, ease of use → wandb Teams
```

---

## Deliverables

- [ ] Language and framework comparison matrix
- [ ] CUDA kernel tutorial (basic to intermediate)
- [ ] Triton kernel examples
- [ ] DeepSpeed vs. FSDP comparison guide
- [ ] Complete development environment setup script (Ubuntu 22.04)
- [ ] Tool selection decision trees

---

## Notes

_(Track version numbers of all tools you actually use — pin them for reproducibility)_
