# Section 2 — History of AI (1956–2026)

**Volume:** I — Foundations & Economics  
**Status:** 🔲 Not Started  
**Estimated Depth:** 30–40 pages

---

## Objectives

1. Understand the full 70-year arc of AI research — not as a triumphal march but as a story of booms, busts, paradigm shifts, and compound institutional learning
2. Identify the economic and social forces that caused each transition
3. Know the specific technical breakthroughs that mattered and why
4. Extract strategic lessons for your own lab timing and positioning

---

## Timeline Spine

```
1956  ─── Dartmouth Conference (Birth of AI as a field)
1960s ─── Early optimism: Logic Theorist, General Problem Solver, LISP
1969  ─── Minsky & Papert: Perceptrons (XOR problem → killed connectionism)
1970s ─── First AI Winter (1974–1980): funding collapse, unmet promises
1980s ─── Expert Systems boom: XCON, R1, commercial AI
1987  ─── Second AI Winter begins: Lisp Machine market collapses
1990s ─── Statistical NLP, SVMs, reinforcement learning foundations
1997  ─── Deep Blue beats Kasparov
1998  ─── LeCun: LeNet, backpropagation applied to vision
2006  ─── Hinton: Deep Belief Networks — deep learning renaissance
2012  ─── AlexNet: ImageNet, GPU-accelerated deep learning goes viral
2014  ─── GANs (Goodfellow), Attention mechanism (Bahdanau)
2015  ─── ResNets, Batch Norm — deep learning matures
2017  ─── Transformer: "Attention Is All You Need"
2018  ─── BERT, GPT-1 — language model pretraining era
2019  ─── GPT-2, XLNet, T5 — scaling experiments
2020  ─── GPT-3 (175B) — emergent abilities, few-shot learning
2021  ─── CLIP, DALL-E, Codex, AlphaFold 2
2022  ─── ChatGPT, Stable Diffusion, RLHF-tuned models go mainstream
2023  ─── GPT-4, Claude, Gemini, LLaMA, Mistral — open model race
2024  ─── o1 reasoning, Sora video, Gemini 1.5 (1M context), DeepSeek
2025  ─── Agentic AI, multimodal reasoning, robotics renaissance
2026  ─── (Current: World models, reasoning at scale, scientific AI)
```

---

## Thematic Threads to Trace

### 1. The Winters
- Why they happened (technically and economically)
- What researchers did during the winters (survivorship strategies)
- How each winter seeded the next boom

### 2. The Scaling Hypothesis
- When did people start believing scaling would work?
- Sutton's "Bitter Lesson" — compute > cleverness
- Kaplan et al. scaling laws (2020)
- How this changed lab strategy and compute investment

### 3. The Architecture Lineage
- Perceptrons → MLPs → CNNs → RNNs/LSTMs → Attention → Transformers → State Space Models (Mamba)
- Why each transition happened
- What mathematical insight drove each shift

### 4. The Data Hypothesis
- ImageNet (2009) as infrastructure
- Common Crawl, C4, The Pile, RedPajama
- Synthetic data emergence (2023–2025)

### 5. The Economics
- DARPA funding role (1960s–1990s)
- VC discovery of AI (2012–2016)
- Big Tech compute arms race (2016–2022)
- Government strategic interest (2022–present)
- India, China, EU AI policy trajectories

### 6. The Talent Market
- How Hinton, LeCun, Bengio built the field
- The "Toronto Mafia" and academic origin of frontier labs
- Talent concentration and its effects on science

---

## Prompt for Deep Content Generation

```
You are an AI historian, economist, and research scientist writing for an audience of 
graduate students and PhD researchers who want to build AI labs.

Write a comprehensive, graduate-level history of AI from 1956 to 2026 as Section 2 
of a multi-volume manual titled "Building an AI Research Lab From Scratch."

Structure it as follows:

PART A — DECADE-BY-DECADE NARRATIVE
For each decade from 1950s to 2020s, write:
   - Dominant paradigm (what people believed AI was)
   - Key technical breakthroughs with mathematical insight (not just names)
   - Key papers and authors with exact citations
   - Economic context: who was funding it and why
   - Institutional context: which universities, labs, and companies led
   - Why the decade ended the way it did (transition or collapse)
   - What individual researchers did that compounded across time

PART B — THE TWO AI WINTERS IN DEPTH
For each winter (1974–1980 and 1987–1993):
   - Technical causes: what promises failed and why
   - Economic causes: funding collapse, Lighthill Report, DARPA reviews
   - Survivor strategies: what serious researchers worked on during the winter
   - Institutional effects: which labs died, which survived, which emerged post-winter
   - Lessons: what a researcher today must understand about how winters begin

PART C — THE DEEP LEARNING REVOLUTION (2006–2016)
   - Explain mathematically why deep learning worked when symbolic AI didn't
   - Trace: Hinton (2006) → LeCun (LeNet revival) → AlexNet (2012) → rapid adoption
   - Role of GPUs: why NVIDIA mattered more than any algorithm paper
   - ImageNet as institutional infrastructure (Fei-Fei Li's contribution)
   - The compute scaling curve: training cost vs. capability from 2012 to 2016

PART D — THE TRANSFORMER REVOLUTION (2017–2022)
   - Explain the Transformer architecture mathematically
     (self-attention, multi-head attention, positional encoding, why it matters)
   - Trace: "Attention Is All You Need" (2017) → BERT (2018) → GPT series → ChatGPT
   - RLHF: what it is, where it came from, why it changed product development
   - The emergent abilities debate: do they exist? Srivastava et al. vs. skeptics
   - Economic turning point: GPT-3 and the "AI is a product" moment

PART E — THE CURRENT ERA (2023–2026)
   - Reasoning models: chain-of-thought, tree-of-thought, o1-style inference-time compute
   - Agentic AI: definition, current capabilities, fundamental limitations
   - World models: what they are, current state, why they matter for robotics
   - Diffusion models: mathematical intuition (DDPM, score matching, flow matching)
   - Multimodal: CLIP lineage, GPT-4V, Gemini, unified architectures
   - Scientific AI: AlphaFold 2 as a case study in what AI can do for science
   - Open source ecosystem: LLaMA, Mistral, DeepSeek — what changed and why

PART F — ECONOMIC ANALYSIS
   - How AI funding changed from government grants to VC to sovereign wealth
   - The compute cost curve: what training a frontier model cost in 2012, 2016, 2020, 2024
   - Return on investment: has AI research been economically rational?
   - Geographic concentration: why San Francisco, London, and Toronto dominate
   - India's position: what has happened, what is possible
   - China's trajectory: DeepSeek as a case study in compute-efficient research

PART G — STRATEGIC LESSONS FOR A LAB FOUNDER
   - What timing in the historical cycle tells you about lab positioning today
   - Which research bets from history aged well? Which aged badly?
   - How to read the current landscape to identify what 2027–2030 will reward
   - The "last mover advantage" in research: when being early is wrong

Format: structured markdown, exact paper citations (author, year, venue, title), 
ASCII timelines, economic data where available, no motivational language.
Depth target: ~35–40 pages equivalent.
```

---

## Key References

### Papers
- McCarthy, J. et al. (1956). "A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence."
- Minsky, M. & Papert, S. (1969). *Perceptrons.* MIT Press.
- Hinton, G. et al. (2006). "A Fast Learning Algorithm for Deep Belief Nets." *Neural Computation.*
- Krizhevsky, A. et al. (2012). "ImageNet Classification with Deep CNNs." NeurIPS.
- Vaswani, A. et al. (2017). "Attention Is All You Need." NeurIPS.
- Devlin, J. et al. (2018). "BERT." NAACL.
- Brown, T. et al. (2020). "Language Models are Few-Shot Learners." NeurIPS.
- Ouyang, L. et al. (2022). "Training language models to follow instructions with human feedback." NeurIPS.
- Kaplan, J. et al. (2020). "Scaling Laws for Neural Language Models." arXiv.
- Jumper, J. et al. (2021). "Highly accurate protein structure prediction with AlphaFold." *Nature.*

### Books
- Nilsson, N. (2010). *The Quest for Artificial Intelligence.* Cambridge.
- Marcus, G. & Davis, E. (2019). *Rebooting AI.* Pantheon.
- Goodfellow, I. et al. (2016). *Deep Learning.* MIT Press.

---

## Deliverables

- [ ] Annotated decade-by-decade timeline (ASCII + prose)
- [ ] The two AI winters: cause, effect, survivor strategies
- [ ] Mathematical walkthrough of Transformer architecture
- [ ] Economic cost curve: training a frontier model by year (2012–2024)
- [ ] Strategic positioning memo: what does 2026 tell you to research?

---

## Notes

_(Write your personal notes and observations here)_
