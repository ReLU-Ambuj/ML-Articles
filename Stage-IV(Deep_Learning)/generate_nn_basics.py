#!/usr/bin/env python3
"""
Generate the complete Neural Network Basics directory tree.
Each leaf and section node gets a directory with README.md containing a mastery prompt.
"""

import os

BASE = "/Users/ambuj/Summer-2026/ML-Journey_Notion/Stage-IV(Deep_Learning)/Neural_Network_Basics"

# Tree: { "dir_name": { "subdir": {...} | None } }
# None means leaf node (gets its own README only)
TREE = {
    "History_and_Motivation": {
        "Biological_Inspiration": {
            "Biological_Neurons": None,
            "Synapses": None,
            "Signal_Transmission": None,
            "Excitatory_Signals": None,
            "Inhibitory_Signals": None,
            "Brain_as_Parallel_Computer": None,
            "Limits_of_Biological_Analogy": None,
        },
        "McCulloch_Pitts_Neuron": {
            "Threshold_Logic": None,
            "Binary_Inputs": None,
            "Binary_Outputs": None,
            "Logic_Gates": None,
            "Computational_Universality": None,
            "Historical_Significance": None,
        },
        "Perceptron_Era": {
            "Rosenblatt_Perceptron": None,
            "Learning_from_Data": None,
            "Linear_Separability": None,
            "Pattern_Recognition": None,
            "Early_Optimism": None,
            "Hardware_Implementations": None,
        },
        "AI_Winter": {
            "Minsky_Papert_Criticism": None,
            "XOR_Problem": None,
            "Funding_Decline": None,
            "Computational_Limitations": None,
            "Symbolic_AI_Dominance": None,
            "Research_Slowdown": None,
        },
        "Backpropagation_Revival": {
            "Rumelhart_Hinton_Williams": None,
            "Multi_Layer_Learning": None,
            "Error_Propagation": None,
            "Differentiable_Models": None,
            "Gradient_Based_Training": None,
            "Practical_Successes": None,
        },
        "Deep_Learning_Revolution": {
            "GPU_Computing": None,
            "Big_Data_Era": None,
            "ImageNet_Breakthrough": None,
            "Representation_Learning": None,
            "Self_Supervised_Learning": None,
            "Foundation_Models": None,
            "Generative_AI": None,
        },
    },
    "Perceptrons": {
        "Mathematical_Model": {
            "Input_Vector_x": None,
            "Weight_Vector_w": None,
            "Bias_b": None,
            "Linear_Combination": None,
            "Activation_Function": None,
            "Output_Prediction": None,
        },
        "Linear_Decision_Boundaries": {
            "Hyperplanes": None,
            "Half_Spaces": None,
            "Separating_Classes": None,
            "Margin_Concept": None,
            "High_Dimensional_Geometry": None,
            "Visualization": None,
        },
        "Weighted_Sum": {
            "Dot_Product": None,
            "Feature_Importance": None,
            "Positive_Weights": None,
            "Negative_Weights": None,
            "Scaling_Effects": None,
            "Interpretation": None,
        },
        "Bias_Term": {
            "Threshold_Shift": None,
            "Affine_Transformations": None,
            "Intercept_Analogy": None,
            "Decision_Boundary_Translation": None,
            "Learnable_Parameter": None,
        },
        "Binary_Classification": {
            "Positive_Class": None,
            "Negative_Class": None,
            "Decision_Rules": None,
            "Classification_Errors": None,
            "Accuracy_Metrics": None,
        },
        "Geometric_Interpretation": {
            "Vectors": None,
            "Angles": None,
            "Projections": None,
            "Distance_from_Hyperplane": None,
            "Margin_Geometry": None,
        },
        "Perceptron_Learning_Rule": {
            "Mistake_Driven_Learning": None,
            "Update_Equation": None,
            "Convergence_Theorem": None,
            "Learning_Rate": None,
            "Epochs": None,
            "Online_Learning": None,
        },
        "XOR_Failure": {
            "Nonlinear_Separability": None,
            "XOR_Dataset": None,
            "Geometric_Proof": None,
            "Need_for_Hidden_Layers": None,
            "Historical_Impact": None,
            "Motivation_for_Deep_Networks": None,
        },
    },
    "Multi_Layer_Perceptrons": {
        "Hidden_Layers": {
            "Representation_Learning": None,
            "Feature_Extraction": None,
            "Intermediate_Features": None,
            "Hierarchical_Learning": None,
            "Deep_Feature_Spaces": None,
        },
        "Universal_Approximation_Theorem": {
            "Formal_Statement": None,
            "Assumptions": None,
            "Continuous_Functions": None,
            "Approximation_Guarantees": None,
            "Practical_Limitations": None,
            "Implications": None,
        },
        "Depth_vs_Width": {
            "Shallow_Networks": None,
            "Deep_Networks": None,
            "Parameter_Efficiency": None,
            "Expressive_Efficiency": None,
            "Theoretical_Results": None,
            "Empirical_Tradeoffs": None,
        },
        "Forward_Propagation": {
            "Layer_Computations": None,
            "Matrix_Multiplication": None,
            "Activation_Pipeline": None,
            "Prediction_Generation": None,
            "Computational_Complexity": None,
        },
        "Parameter_Counting": {
            "Weight_Matrices": None,
            "Bias_Vectors": None,
            "Memory_Requirements": None,
            "Model_Size": None,
            "Scaling_Laws": None,
        },
        "Expressive_Power": {
            "Piecewise_Linear_Functions": None,
            "Function_Composition": None,
            "Hierarchical_Features": None,
            "Complexity_Growth": None,
            "Neural_Tangent_Perspective": None,
            "Approximation_Theory": None,
        },
    },
    "Activation_Functions": {
        "Why_Activations_Matter": {
            "Nonlinearity": None,
            "Function_Approximation": None,
            "Gradient_Flow": None,
            "Optimization_Behavior": None,
            "Expressiveness": None,
        },
        "Step_Function": {
            "Binary_Output": None,
            "Threshold_Decision": None,
            "Non_Differentiability": None,
            "Historical_Usage": None,
            "Limitations": None,
        },
        "Sigmoid": {
            "Logistic_Function": None,
            "Probability_Interpretation": None,
            "Saturation": None,
            "Vanishing_Gradients": None,
            "Modern_Usage": None,
        },
        "Tanh": {
            "Zero_Centered_Outputs": None,
            "Saturation_Regions": None,
            "Gradient_Properties": None,
            "Comparison_to_Sigmoid": None,
            "Applications": None,
        },
        "ReLU": {
            "Piecewise_Linear_Form": None,
            "Sparsity": None,
            "Computational_Efficiency": None,
            "Dying_ReLU_Problem": None,
            "Dominance_in_Deep_Learning": None,
        },
        "Leaky_ReLU": {
            "Negative_Slope": None,
            "Dead_Neuron_Mitigation": None,
            "Hyperparameter_Alpha": None,
            "Variants": None,
        },
        "ELU": {
            "Exponential_Region": None,
            "Mean_Activation_Control": None,
            "Smoothness": None,
            "Training_Benefits": None,
        },
        "GELU": {
            "Gaussian_Interpretation": None,
            "Probabilistic_Gating": None,
            "Transformer_Usage": None,
            "Smooth_Nonlinearity": None,
            "Performance_Benefits": None,
        },
        "Swish": {
            "Self_Gating_Mechanism": None,
            "Smooth_Activation": None,
            "Non_Monotonicity": None,
            "Empirical_Performance": None,
        },
        "Softmax": {
            "Probability_Distribution": None,
            "Multi_Class_Outputs": None,
            "Temperature_Scaling": None,
            "Logits": None,
            "Numerical_Stability": None,
            "Cross_Entropy_Connection": None,
        },
    },
    "Loss_Functions": {
        "Statistical_Foundations": {
            "Risk_Minimization": None,
            "Likelihood_Theory": None,
            "Information_Theory": None,
            "Bayesian_View": None,
            "Empirical_Risk": None,
        },
        "Regression_Losses": {
            "Mean_Squared_Error": None,
            "Root_Mean_Squared_Error": None,
            "Mean_Absolute_Error": None,
            "Huber_Loss": None,
            "Quantile_Loss": None,
            "Log_Cosh_Loss": None,
        },
        "Classification_Losses": {
            "Binary_Cross_Entropy": None,
            "Multi_Class_Cross_Entropy": None,
            "Sparse_Cross_Entropy": None,
            "Focal_Loss": None,
            "Hinge_Loss": None,
            "Label_Smoothed_Loss": None,
        },
        "Information_Theoretic_Losses": {
            "KL_Divergence": None,
            "Jensen_Shannon_Divergence": None,
            "Entropy": None,
            "Cross_Entropy": None,
            "Mutual_Information": None,
        },
        "Metric_Learning_Losses": {
            "Contrastive_Loss": None,
            "Triplet_Loss": None,
            "ArcFace_Loss": None,
            "CosFace_Loss": None,
            "Center_Loss": None,
            "InfoNCE_Loss": None,
        },
    },
    "Backpropagation": {
        "Computational_Graphs": None,
        "Forward_Pass": None,
        "Reverse_Mode_Differentiation": None,
        "Chain_Rule": None,
        "Jacobians": None,
        "Vector_Jacobian_Products": None,
        "Gradient_Computation": None,
        "Weight_Updates": None,
        "Vanishing_Gradients": None,
        "Exploding_Gradients": None,
        "Gradient_Checking": None,
        "Automatic_Differentiation": None,
        "Reverse_Mode_AD": None,
        "Forward_Mode_AD": None,
        "Autograd_Systems": None,
    },
    "Optimization_Algorithms": {
        "Optimization_Landscape": {
            "Local_Minima": None,
            "Saddle_Points": None,
            "Flat_Regions": None,
            "Sharp_Minima": None,
            "Loss_Geometry": None,
        },
        "First_Order_Methods": {
            "Batch_Gradient_Descent": None,
            "Stochastic_GD": None,
            "Mini_Batch_GD": None,
            "Momentum": None,
            "Nesterov_Momentum": None,
        },
        "Adaptive_Methods": {
            "AdaGrad": None,
            "RMSProp": None,
            "Adam": None,
            "AdamW": None,
            "AdaFactor": None,
            "LAMB": None,
        },
        "Learning_Rate_Strategies": {
            "Constant_LR": None,
            "Step_Decay": None,
            "Exponential_Decay": None,
            "Cosine_Annealing": None,
            "Warmup": None,
            "One_Cycle_Policy": None,
            "Cyclic_Learning_Rates": None,
        },
    },
    "Regularization": {
        "Bias_Variance_Tradeoff": None,
        "L1_Regularization": None,
        "L2_Regularization": None,
        "Elastic_Net": None,
        "Weight_Decay": None,
        "Dropout": None,
        "DropConnect": None,
        "Early_Stopping": None,
        "Data_Augmentation": None,
        "Mixup": None,
        "CutMix": None,
        "Label_Smoothing": None,
        "Noise_Injection": None,
        "Stochastic_Depth": None,
        "Model_Averaging": None,
    },
    "Training_Tricks": {
        "Normalization_Methods": {
            "Batch_Normalization": None,
            "Layer_Normalization": None,
            "Instance_Normalization": None,
            "Group_Normalization": None,
            "RMS_Normalization": None,
        },
        "Initialization_Schemes": {
            "Random_Initialization": None,
            "Xavier_Initialization": None,
            "He_Initialization": None,
            "Orthogonal_Initialization": None,
            "LSUV_Initialization": None,
        },
        "Stability_Techniques": {
            "Gradient_Clipping": None,
            "Loss_Scaling": None,
            "Numerical_Stability": None,
            "Mixed_Precision_Training": None,
            "Checkpointing": None,
        },
        "Scheduling_Methods": {
            "Warmup": None,
            "Cosine_Scheduling": None,
            "Polynomial_Decay": None,
            "Linear_Decay": None,
            "Restart_Schedules": None,
        },
        "Engineering_Practices": {
            "Hyperparameter_Search": None,
            "Reproducibility": None,
            "Experiment_Tracking": None,
            "Distributed_Training": None,
            "Data_Pipelines": None,
            "Model_Checkpointing": None,
            "Inference_Optimization": None,
        },
    },
}


def human_name(slug: str) -> str:
    """Convert slug like 'Dying_ReLU_Problem' to 'Dying ReLU Problem'."""
    return slug.replace("_", " ")


def make_prompt(topic: str, parent: str, ancestors: list[str]) -> str:
    """Generate a precise mastery prompt for a given topic node."""
    breadcrumb = " > ".join(ancestors + [topic])
    h = human_name(topic)
    ctx = human_name(parent) if parent else "Neural Network Basics"

    prompt = f"""# {h}

**Context:** {breadcrumb}

---

## Mastery Prompt

Paste the following prompt into an AI assistant (ChatGPT, Claude, Gemini) to master this topic completely:

```
You are an expert deep learning educator and researcher.

Teach me "{h}" as part of the topic "{human_name(parent or 'Neural Network Basics')}" in deep learning.

Structure your response as follows:

1. INTUITION FIRST (2–3 sentences)
   - What is {h} in plain language?
   - What problem does it solve or what phenomenon does it describe?

2. MATHEMATICAL FOUNDATION
   - Write out the exact formula(s) with every symbol defined.
   - Derive or explain where the formula comes from — do not just state it.
   - Show the gradient / derivative if applicable (I need to implement backprop).

3. STEP-BY-STEP WORKED EXAMPLE
   - Use concrete numbers. Walk through the computation manually.
   - Show what happens before and after this concept is applied.

4. CODE IMPLEMENTATION (Python / NumPy from scratch)
   - Implement {h} from scratch in NumPy — no PyTorch/sklearn for the core logic.
   - Then show the PyTorch/JAX equivalent.
   - Run it on a small example and print intermediate values.

5. COMMON MISTAKES AND MISCONCEPTIONS
   - What do beginners get wrong about {h}?
   - What edge cases or failure modes exist?

6. CONNECTIONS
   - How does {h} connect to the broader context of "{human_name(parent or 'Neural Network Basics')}"?
   - What concepts come before it (prerequisites)?
   - What concepts build on top of it (next steps)?

7. MINI PROJECT
   - Give me one hands-on mini project (< 50 lines of Python) that lets me verify
     I have understood {h} correctly, using a real or toy dataset.
   - The project should break in an obvious way if I misunderstood the concept.

8. QUIZ (5 questions)
   - 3 conceptual questions (no code)
   - 2 numerical questions (I compute by hand)
   - Provide answers at the end.

Do not skip any section. Use LaTeX math notation ($...$) for all equations.
Be precise — treat me as a graduate student, not a beginner.
```

---

## Quick Reference

| Field | Value |
|-------|-------|
| **Topic** | {h} |
| **Parent Section** | {ctx} |
| **Full Path** | `{breadcrumb}` |
| **Difficulty** | Graduate / Research level |
| **Prerequisites** | Review the parent directory README first |

---

## Notes

*(Add your personal notes, key equations to remember, and links to papers here)*
"""
    return prompt


def build(tree: dict, current_path: str, parent: str, ancestors: list[str]):
    os.makedirs(current_path, exist_ok=True)

    # Write section-level README (overview prompt)
    section_name = os.path.basename(current_path)
    h = human_name(section_name)
    ctx = human_name(parent) if parent else "Deep Learning"
    breadcrumb = " > ".join(ancestors) if ancestors else h

    section_prompt = f"""# {h}

**Section:** {breadcrumb}

---

## Section Overview Prompt

Use this prompt to get an overview of the entire **{h}** section before diving into subtopics:

```
You are an expert deep learning educator.

Give me a complete structured overview of "{h}" as it appears in deep learning,
within the context of "{ctx}".

Cover:
1. Why this topic exists — what gap or need does it address?
2. The list of all subtopics in this section and how they relate to each other.
3. The correct learning order (which subtopics to study first).
4. The 3 most important concepts to deeply understand in this section.
5. Common misconceptions beginners have about {h}.
6. One overarching project that ties all subtopics in this section together,
   using a real dataset (MNIST, CIFAR-10, or UCI datasets).

Treat me as a graduate student with a strong math background.
Use LaTeX for equations. Be specific, not generic.
```

---

## Subtopics in This Section

"""
    # List children
    if isinstance(tree, dict):
        for child in tree:
            section_prompt += f"- [{human_name(child)}](./{child}/README.md)\n"

    section_prompt += "\n---\n\n## Notes\n\n*(Add section-level notes here)*\n"

    with open(os.path.join(current_path, "README.md"), "w") as f:
        f.write(section_prompt)

    # Recurse into children
    if isinstance(tree, dict):
        for child_name, child_tree in tree.items():
            child_path = os.path.join(current_path, child_name)
            child_ancestors = ancestors + [human_name(child_name)]

            if child_tree is None:
                # Leaf node — create dir + leaf README with mastery prompt
                os.makedirs(child_path, exist_ok=True)
                prompt_content = make_prompt(child_name, section_name, ancestors)
                with open(os.path.join(child_path, "README.md"), "w") as f:
                    f.write(prompt_content)
            else:
                # Intermediate node — recurse
                build(child_tree, child_path, section_name, child_ancestors)


# ── Build root README ──
os.makedirs(BASE, exist_ok=True)
root_readme = """# Neural Network Basics

**Course:** Stage-IV — Deep Learning

---

## Root Overview Prompt

```
You are a world-class deep learning educator.

Give me a complete roadmap for mastering "Neural Network Basics" — the foundational
layer of all deep learning.

Structure your answer as:
1. Why neural networks exist — the problem they solve that no prior method could.
2. The correct learning order for all major sections:
   History → Perceptrons → MLPs → Activation Functions → Loss Functions →
   Backpropagation → Optimization → Regularization → Training Tricks
3. For each section: one sentence on what it contributes to the overall understanding.
4. The 5 most important mathematical ideas that appear across all sections.
5. One capstone project (using MNIST or CIFAR-10) that requires understanding
   ALL sections to complete correctly.
6. The 3 most common failure modes when learning neural networks from scratch.

Treat me as a mathematics and CS graduate student. Use LaTeX for all equations.
```

---

## Sections

- [History and Motivation](./History_and_Motivation/README.md)
- [Perceptrons](./Perceptrons/README.md)
- [Multi-Layer Perceptrons](./Multi_Layer_Perceptrons/README.md)
- [Activation Functions](./Activation_Functions/README.md)
- [Loss Functions](./Loss_Functions/README.md)
- [Backpropagation](./Backpropagation/README.md)
- [Optimization Algorithms](./Optimization_Algorithms/README.md)
- [Regularization](./Regularization/README.md)
- [Training Tricks](./Training_Tricks/README.md)

---

## Capstone Project Prompt

```
You are a deep learning educator and engineer.

Design a complete end-to-end deep learning project that requires a student to
demonstrate mastery of ALL of the following:
- Perceptron / MLP architecture
- Activation function selection and justification
- Loss function selection and justification
- Manual backpropagation implementation (NumPy)
- Optimizer implementation (SGD + Adam from scratch)
- Regularization (L2 + Dropout)
- Batch normalization
- Learning rate scheduling
- Experiment tracking (loss curves, accuracy curves)
- Hyperparameter search

Dataset: MNIST (handwritten digits) or CIFAR-10.
Deliverable: A Python script (~300–500 lines) with detailed comments.
Evaluation: The project should fail in an obvious, diagnosable way
if any one of the above components is implemented incorrectly.

Provide the full project specification including expected output values,
so I can verify my implementation is correct.
```

---

## Notes

*(Track your progress here: check off each section as you complete it)*
"""

with open(os.path.join(BASE, "README.md"), "w") as f:
    f.write(root_readme)

# Build the full tree
build(TREE, BASE, "", [])

# Count what was created
total_files = sum(len(files) for _, _, files in os.walk(BASE))
total_dirs = sum(len(dirs) for _, dirs, _ in os.walk(BASE))
print(f"✓ Created {total_dirs} directories and {total_files} README.md files")
print(f"  Root: {BASE}")
