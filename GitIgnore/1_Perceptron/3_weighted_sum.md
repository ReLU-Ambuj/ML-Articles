# The Weighted Sum

### The Fundamental Question

> **"How does a neuron combine evidence?"**

Every lesson in this curriculum so far has used the expression $z=\mathbf{w}\cdot\mathbf{x}+b$ without fully excavating what $\mathbf{w}\cdot\mathbf{x}$ *is*, in the formal sense — where it comes from in linear algebra, why it's the natural choice for combining evidence, and what its deeper algebraic structure reveals about feature importance, projections, and scale. This lesson opens that expression up completely. The weighted sum is not just "a formula that happens to work" — it is one specific instance of one of the most fundamental operations in all of linear algebra: the **inner product**.

---

## Linear Algebra Foundations

### The Raw Definition

The weighted sum, again, is:

$$z = w_1x_1 + w_2x_2 + \dots + w_nx_n = \sum_{i=1}^{n} w_ix_i$$

Each term $w_ix_i$ is the product of one weight and its corresponding input; the whole expression is their sum. This is the most literal reading: "multiply each piece of evidence by its importance, then add everything up."

### Vector Spaces

To talk about $\mathbf{w}$ and $\mathbf{x}$ as more than just "lists of numbers," it helps to be explicit about the structure they live in. A **vector space** (over the real numbers, for our purposes) is a set of objects — vectors — that can be added together and scaled by real numbers, subject to a small set of consistency rules (associativity, commutativity of addition, distributivity of scaling over addition, existence of a zero vector, and so on).

$\mathbb{R}^n$ — the set of all ordered $n$-tuples of real numbers — is the canonical example, and it's exactly where $\mathbf{w}$ and $\mathbf{x}$ live: $\mathbf{w}, \mathbf{x} \in \mathbb{R}^n$. The fact that $\mathbb{R}^n$ is a vector space is what licenses operations like $\mathbf{w}+\mathbf{x}$ (adding corresponding coordinates) or $3\mathbf{w}$ (scaling every coordinate by 3) — operations that show up constantly once you start thinking about *changing* weights during learning (the perceptron update rule, from *Perceptron Era*, is literally a vector addition: $\mathbf{w} \leftarrow \mathbf{w} + \eta \cdot e \cdot \mathbf{x}$).

### Inner Products

A vector space alone gives you addition and scaling, but not yet any notion of *length*, *angle*, or *alignment* between vectors. That extra structure comes from equipping the vector space with an **inner product** — a function $\langle \cdot,\cdot\rangle$ taking two vectors and returning a single real number, satisfying three axioms:

1. **Symmetry:** $\langle\mathbf{u},\mathbf{v}\rangle = \langle\mathbf{v},\mathbf{u}\rangle$
2. **Linearity (in each argument):** $\langle a\mathbf{u}+b\mathbf{v}, \mathbf{z}\rangle = a\langle\mathbf{u},\mathbf{z}\rangle + b\langle\mathbf{v},\mathbf{z}\rangle$
3. **Positive-definiteness:** $\langle\mathbf{u},\mathbf{u}\rangle \ge 0$, with equality only when $\mathbf{u}$ is the zero vector

The familiar **dot product**, $\mathbf{w}\cdot\mathbf{x} = \sum_i w_ix_i$, is not just *an example* of an inner product — it is *the* **standard inner product** on $\mathbb{R}^n$ (sometimes written $\langle\mathbf{w},\mathbf{x}\rangle$ interchangeably with $\mathbf{w}\cdot\mathbf{x}$). You can verify all three axioms hold directly from the summation definition: swapping $\mathbf{w}$ and $\mathbf{x}$ doesn't change the sum (symmetry); the sum distributes correctly over vector addition and scalar multiplication (linearity); and $\mathbf{w}\cdot\mathbf{w}=\sum_i w_i^2 \ge 0$, zero only when every $w_i=0$ (positive-definiteness).

### Why This Matters: The Weighted Sum *Is* an Inner Product Evaluation

Putting these pieces together: the weighted sum $z$ (before adding the bias) is nothing more or less than **the inner product of the weight vector and the input vector**, evaluated in $\mathbb{R}^n$ under its standard inner product:

$$z = \langle \mathbf{w}, \mathbf{x}\rangle = \mathbf{w}\cdot\mathbf{x}$$

This reframing matters because every theorem and intuition that holds for inner products in general — the Cauchy-Schwarz inequality, the notion of orthogonality, the existence of projections (below), the definition of length via $\|\mathbf{v}\|=\sqrt{\langle\mathbf{v},\mathbf{v}\rangle}$ — automatically applies to the weighted sum, for free, simply because it *is* an inner product. The perceptron's core computation isn't a clever ad hoc formula; it's a direct, specific instance of one of the oldest and most thoroughly studied structures in mathematics.

---

## Geometry

### Projections

A central geometric fact about inner products: $\langle\mathbf{w},\mathbf{x}\rangle$ measures **how much of $\mathbf{x}$ points in the direction of $\mathbf{w}$** (or equivalently, vice versa, by symmetry). This is made precise through the **projection** of $\mathbf{x}$ onto $\mathbf{w}$.

**Deriving the projection.** We want to decompose $\mathbf{x}$ into two parts: a component parallel to $\mathbf{w}$, and a component perpendicular to $\mathbf{w}$. Write the parallel component as $c\hat{\mathbf{w}}$, where $\hat{\mathbf{w}}=\mathbf{w}/\|\mathbf{w}\|$ is the unit vector in $\mathbf{w}$'s direction, and $c$ is the (signed) length of that component. For this decomposition to have the perpendicular part actually be perpendicular to $\mathbf{w}$, we need:

$$\langle \mathbf{x} - c\hat{\mathbf{w}}, \hat{\mathbf{w}}\rangle = 0 \implies \langle\mathbf{x},\hat{\mathbf{w}}\rangle - c\langle\hat{\mathbf{w}},\hat{\mathbf{w}}\rangle = 0$$

Since $\hat{\mathbf{w}}$ is a unit vector, $\langle\hat{\mathbf{w}},\hat{\mathbf{w}}\rangle=1$, so $c = \langle\mathbf{x},\hat{\mathbf{w}}\rangle = \frac{\mathbf{w}\cdot\mathbf{x}}{\|\mathbf{w}\|}$.

This means **$c$, the length of $\mathbf{x}$'s projection onto $\mathbf{w}$, is exactly the weighted sum $\mathbf{w}\cdot\mathbf{x}$, rescaled by $1/\|\mathbf{w}\|$.** Equivalently:

$$\mathbf{w}\cdot\mathbf{x} = \|\mathbf{w}\| \cdot (\text{length of } \mathbf{x}\text{'s projection onto } \mathbf{w})$$

This gives an exact geometric meaning to the raw score $z$ (ignoring bias for a moment): **it is the length of the weight vector, multiplied by how far the input extends in the weight vector's direction.** An input that points entirely *opposite* to $\mathbf{w}$ produces a large *negative* $z$; an input perpendicular to $\mathbf{w}$ contributes exactly $z=0$, regardless of how large the input vector itself is.

### Geometric Interpretation of the Full Picture

Recall from trigonometry that $\mathbf{w}\cdot\mathbf{x} = \|\mathbf{w}\|\|\mathbf{x}\|\cos\theta$, where $\theta$ is the angle between the two vectors. This single identity unifies the algebra and the geometry:

- When $\theta=0$ (vectors point the same direction), $\cos\theta=1$, and $z$ is maximized for given vector lengths.
- When $\theta=90°$ (vectors are **orthogonal**, i.e., perpendicular), $\cos\theta=0$, and $z=0$ regardless of how long either vector is — the input contributes *zero* weighted evidence, because none of it lies in a direction the weights care about.
- When $\theta=180°$ (vectors point in exactly opposite directions), $\cos\theta=-1$, and $z$ is as negative as possible.

This is the deepest sense in which the weighted sum measures **alignment**: it isn't really measuring the input's raw magnitude, but how much that magnitude is "pointed toward" the direction the model considers important.

### Scaling Effects

Two distinct scaling questions are worth separating cleanly:

**Scaling the weight vector** ($\mathbf{w} \to c\mathbf{w}$, for $c>0$): every term $w_ix_i$ scales by $c$, so $z \to cz$. The *direction* $\mathbf{w}$ points in is unchanged, so (as derived in the previous lesson) the decision boundary's location and orientation are unaffected — but the raw score's magnitude scales linearly, and so does its sensitivity to small changes in the input (small changes in $\mathbf{x}$ now produce $c\times$ larger changes in $z$).

**Scaling an individual input feature** ($x_i \to cx_i$, leaving $\mathbf{w}$ fixed): only the $i$-th term changes, becoming $w_i(cx_i) = c(w_ix_i)$ — the contribution of *that one feature* scales by $c$, while every other term is untouched. This is precisely why feature scaling (normalizing inputs to comparable ranges before training) matters in practice: if one feature is measured in the thousands (e.g., annual income in dollars) and another ranges between 0 and 1 (e.g., a normalized score), a "naturally small" weight on the income feature can still dominate the weighted sum purely due to the input's scale — not because the model has judged income more important. The raw weight values alone, in other words, can be deeply misleading about *true* relative importance unless the inputs are on comparable scales.

---

## Intuition

### Positive, Negative, and Zero Weights

Return to the alignment picture from the previous section, restated in plain terms:

- **Positive weight ($w_i>0$):** increasing $x_i$ increases $z$ — this feature pushes *toward* a "yes" decision. The larger $w_i$, the stronger this push per unit of $x_i$.
- **Negative weight ($w_i<0$):** increasing $x_i$ *decreases* $z$ — this feature pushes *toward* a "no" decision. This is the direct mathematical residue of an inhibitory influence (Section 3.5 of *Biological Inspiration*).
- **Zero weight ($w_i=0$):** $x_i$ has **no effect whatsoever** on $z$, no matter its value. The model has, in effect, declared this feature entirely irrelevant — geometrically, this is the same as the input feature's axis being exactly orthogonal to $\mathbf{w}$ in that coordinate.

### Feature Importance

A direct, calculus-flavored way to state "how important is feature $i$" is to ask: *how much does $z$ change if $x_i$ changes by a small amount, holding everything else fixed?* Differentiating $z=\sum_jw_jx_j+b$ with respect to $x_i$:

$$\frac{\partial z}{\partial x_i} = w_i$$

**The weight $w_i$ is, quite literally, the sensitivity of the weighted sum to feature $i$.** This is a clean, formal definition of "importance" for this model: it is not a vague notion, but the exact rate of change of the model's evidence score with respect to that one input — assuming, as noted above, the inputs are on comparable scales so that this rate-of-change comparison is meaningful across different features.

### Why the Weighted Sum Is the Heart of Every Neural Network

Every architecture introduced later in this curriculum — convolutional layers, recurrent layers, the attention mechanism inside Transformers — performs, at its smallest computational step, the exact same operation derived here: **take some collection of values, multiply each by a learned weight, and sum the results.** A convolution is a weighted sum over a local neighborhood of pixels. An attention mechanism, at its core, computes a weighted sum of "value" vectors, where the weights themselves are dynamically computed rather than fixed — but the underlying operation, once those weights are in hand, is still exactly $\sum_i w_iv_i$. Even the enormous matrix multiplications inside a large language model decompose, entry by entry, into millions of individual instances of this exact same weighted sum. Every other concept in this curriculum — activation functions, learning rules, backpropagation, entire architectures — exists either to compute the inputs to a weighted sum, to decide what to do with its output, or to figure out how to adjust its weights. The weighted sum itself never goes away; it is the one operation present, in some form, at every single layer of every neural network ever built.

---

## Examples

### Example 1 — Positive, Negative, and Zero Weights Together

Let $\mathbf{w}=(2, -3, 0)$ and $\mathbf{x}=(4,1,100)$.

$$z = (2)(4) + (-3)(1) + (0)(100) = 8 - 3 + 0 = 5$$

Notice $x_3=100$ — a large number — contributes **nothing**, because its weight is exactly zero. This is a direct numerical illustration of the orthogonality point above: no matter how large $x_3$ is, it doesn't move $z$ at all.

### Example 2 — Projection, Computed Directly

Let $\mathbf{w}=(3,4)$ (so $\|\mathbf{w}\|=5$) and $\mathbf{x}=(6,8)$ (note: $\mathbf{x}$ points in exactly the same direction as $\mathbf{w}$, since $\mathbf{x}=2\mathbf{w}$).

$$\mathbf{w}\cdot\mathbf{x} = (3)(6)+(4)(8) = 18+32=50$$

Using the projection formula, the length of $\mathbf{x}$'s projection onto $\mathbf{w}$ is $\frac{\mathbf{w}\cdot\mathbf{x}}{\|\mathbf{w}\|} = \frac{50}{5}=10$. Since $\mathbf{x}$ points exactly along $\mathbf{w}$'s direction, this should equal $\mathbf{x}$'s full length: $\|\mathbf{x}\| = \sqrt{6^2+8^2}=\sqrt{36+64}=\sqrt{100}=10$. ✓ — confirming the formula, since when $\theta=0$, the entire length of $\mathbf{x}$ is "used" in the projection.

### Example 3 — An Orthogonal Case

Let $\mathbf{w}=(1,0)$ and $\mathbf{x}=(0,5)$ — these are perpendicular (one lies entirely on the $x_1$-axis, the other entirely on the $x_2$-axis).

$$z = (1)(0)+(0)(5) = 0$$

Even though $\mathbf{x}$ has a substantial length ($\|\mathbf{x}\|=5$), it contributes exactly zero weighted evidence, because it points in a direction the weight vector assigns no importance to whatsoever — a direct numerical confirmation of the $\cos(90°)=0$ relationship.

### Example 4 — The Effect of Scaling Weights vs. Scaling One Feature

Start with $\mathbf{w}=(2,1)$, $\mathbf{x}=(3,4)$: $z = 6+4=10$.

- **Scale all weights by 2** ($\mathbf{w}'=(4,2)$): $z' = 12+8=20$ — exactly double, confirming $z\to cz$ under uniform weight scaling.
- **Scale only $x_1$ by 2** ($\mathbf{x}'=(6,4)$, $\mathbf{w}$ unchanged): $z' = (2)(6)+(1)(4)=12+4=16$ — only the first term doubled (from 6 to 12); the second term ($w_2x_2=4$) is untouched, since only $x_1$ was rescaled.

---

## Connections, Recap

This lesson formally connects the weighted sum to three pillars of linear algebra: it is computed within a **vector space** ($\mathbb{R}^n$, where $\mathbf{w}$ and $\mathbf{x}$ live and can be added/scaled); it **is** an **inner product** (specifically, the standard dot product, satisfying symmetry, linearity, and positive-definiteness); and its geometric meaning is fully captured by **projection** (the weighted sum equals $\|\mathbf{w}\|$ times the length of $\mathbf{x}$'s projection onto $\mathbf{w}$'s direction).

---

## Limitations

Even with this much richer linear-algebraic understanding, the weighted sum's limitations remain exactly what they were in the *Mathematical Model* lesson — but now they can be stated more precisely:

- **It is fundamentally a measure of linear alignment, not of arbitrary relationships.** The weighted sum can only ever express "how much does $\mathbf{x}$ point toward $\mathbf{w}$" — it has no mechanism for capturing relationships between *pairs* of input features (e.g., "this matters only when $x_1$ is large *and* $x_2$ is small"), because the inner product, by construction, only ever combines each $x_i$ with a single fixed scalar $w_i$, never with another input.
- **It is scale-sensitive in ways that can mislead interpretation**, as shown in the Scaling Effects section — a feature's true importance ($\partial z/\partial x_i = w_i$) is only directly comparable across features when those features share a comparable scale.
- **A single weighted sum produces one number** — it collapses an entire input vector down to a single scalar measure of alignment with one direction, $\mathbf{w}$. Capturing richer structure in the input requires *many* weighted sums computed in parallel (i.e., many neurons, each with its own $\mathbf{w}$, forming a layer) — which is exactly the architectural step taken in moving from a single perceptron to a full layer, and eventually a full network.
- **Without a nonlinear activation function afterward, stacking weighted sums adds no expressive power.** A weighted sum of weighted sums is still just another weighted sum (linear combinations of linear combinations remain linear) — this is precisely why every architecture in this curriculum interleaves weighted sums with nonlinear activation functions; the nonlinearity is what allows depth to actually increase what the network can represent, not the mere act of stacking more linear layers.