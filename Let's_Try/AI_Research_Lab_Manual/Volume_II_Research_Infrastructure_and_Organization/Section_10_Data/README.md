# Section 10 — Data

**Volume:** II — Research, Infrastructure & Organization  
**Status:** 🔲 Not Started  
**Estimated Depth:** 20–25 pages

---

## Objectives

1. Understand the full data lifecycle in AI research: collection → curation → cleaning → labeling → versioning
2. Know the legal, ethical, and copyright landscape around training data
3. Build high-quality datasets with limited resources
4. Understand how synthetic data changes the data economics equation

---

## The Data Lifecycle

```
Data Lifecycle
├── Collection
│   ├── Web crawling (Common Crawl, custom crawlers)
│   ├── API pulls (Wikipedia, arXiv, PubMed, GitHub)
│   ├── Licensing / purchasing datasets
│   └── Human generation (crowdsourcing, expert annotation)
├── Curation & Filtering
│   ├── Quality filtering (perplexity, classifier-based)
│   ├── Deduplication (MinHash LSH, exact match)
│   ├── Language identification
│   └── Domain classification
├── Cleaning
│   ├── HTML removal, normalization
│   ├── PII detection and removal
│   └── Format standardization
├── Labeling
│   ├── Crowdsourcing (MTurk, Scale AI, Toloka)
│   ├── Expert annotation
│   └── RLHF preference data collection
├── Synthetic Data
│   ├── LLM-generated data
│   ├── Simulation (robotics, code)
│   └── Data augmentation
└── Versioning & Governance
    ├── Dataset cards (HuggingFace standard)
    ├── Lineage tracking
    └── Access control
```

---

## Prompt for Deep Content Generation

```
You are a data engineer, ML researcher, and legal analyst writing 
a comprehensive data guide for AI research labs.

Write Section 10 of "Building an AI Research Lab From Scratch" — 
a complete reference on data collection, curation, cleaning, labeling, 
synthetic data, and data governance.

PART A — DATA COLLECTION
For each collection method, provide:
   - How it works technically
   - Cost and time requirements
   - Legal considerations (robots.txt, ToS, copyright)
   - Quality characteristics of the resulting data
   - Recommended tools with specific commands

Methods:
   1. Web crawling (Common Crawl processing, custom Scrapy/Playwright crawlers)
   2. API-based collection (Wikipedia API, arXiv API, GitHub API, PubMed E-utilities)
   3. Dataset licensing (HuggingFace Hub, Kaggle, academic data repositories)
   4. Crowdsourcing (Amazon MTurk, Scale AI, Prolific, Appen)
   5. Expert annotation (when crowdsourcing fails — medical, legal, scientific domains)
   6. Synthetic collection (LLM-generated + human-verified)

PART B — CURATION AND FILTERING
   - Quality filtering: how to use perplexity scoring (KenLM) to filter low-quality text
   - Classifier-based filtering: fastText language ID, quality classifiers
   - Deduplication at scale: MinHash LSH implementation, exact n-gram dedup
   - Near-dedup vs. exact-dedup: when to use each
   - Reference: how The Pile (EleutherAI) and RedPajama were curated
   - Reference: how FineWeb (HuggingFace) improved on Common Crawl

PART C — CLEANING AND NORMALIZATION
   - HTML tag removal and text extraction: Trafilatura, BeautifulSoup, jusText
   - Unicode normalization: why it matters, how to do it correctly
   - PII detection and removal: presidio, regex patterns, risk levels
   - Format standardization: JSON Lines vs. Parquet vs. HDF5 for different use cases

PART D — LABELING AND ANNOTATION
   - When to crowdsource vs. use experts vs. use models
   - Label quality control: inter-annotator agreement (Cohen's kappa, Krippendorff's alpha)
   - Annotation tools: Label Studio (self-hosted), Prodigy, Scale AI, Toloka
   - RLHF preference data: how OpenAI, Anthropic, and others collect it
   - Building a small annotation team in India: costs, platforms, quality management
   - Active learning: how to minimize annotation cost by annotating strategically

PART E — SYNTHETIC DATA
   - What synthetic data is, what it is not, when it helps and when it hurts
   - LLM-generated data: distillation, self-play, constitutional AI style
   - Code generation as synthetic data: how Phi-1 and others used it
   - Simulation-based data: robotics, game environments, physics simulators
   - Data augmentation for NLP: back-translation, paraphrase, EDA
   - The model collapse problem: what happens when you train on synthetic data recursively
   - Current frontier: how o1-style reasoning data is generated

PART F — LICENSING, COPYRIGHT, AND ETHICS
   - Copyright law and training data: the current legal landscape (2024–2025 cases)
   - The NYT vs. OpenAI lawsuit: what it means for future training data strategy
   - Creative Commons licenses: which allow training, which do not
   - The GDPR and training data: right to erasure, consent requirements
   - Dataset licenses to know: CC0, CC BY, CC BY-SA, CC BY-NC, ODC-By, CDLA
   - Ethical considerations: bias in training data, representation, harm
   - The "data provenance" movement: why it matters and how to document it

PART G — BENCHMARK DATASETS
   - The role of benchmarks in research: why they matter, how they get corrupted
   - Major benchmarks by area: MMLU, BIG-Bench, HumanEval, MATH, GSM8K, 
     SQuAD, GLUE, SuperGLUE, BoolQ, HellaSwag, ARC, WinoGrande
   - How to create a new benchmark: design principles, evaluation criteria, 
     contamination prevention
   - Benchmark contribution as a research strategy for small labs

PART H — DATA PIPELINE ENGINEERING
   - Building a reproducible data pipeline with DVC
   - Processing large datasets efficiently: multiprocessing, HuggingFace datasets
   - Streaming datasets: how to train on data that doesn't fit in RAM or disk
   - Data versioning: how to track which data produced which model

Format: technical markdown, code snippets for key operations,
cost comparison tables for labeling services,
legal risk matrix for data sources.
Depth target: ~20–25 pages.
```

---

## Deliverables

- [ ] Data collection method comparison table
- [ ] Curation pipeline tutorial (code included)
- [ ] Legal risk matrix: data source × jurisdiction
- [ ] Annotation cost comparison: crowdsource vs. expert vs. LLM
- [ ] Benchmark creation checklist
- [ ] Dataset card template (HuggingFace format)

---

## Notes
