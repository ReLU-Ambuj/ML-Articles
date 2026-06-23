# Linear Decision Boundaries

### The Fundamental Question

> **"How does a perceptron divide the world into classes?"**

The previous lesson established the perceptron as a function, $y = f(\mathbf{w}\cdot\mathbf{x}+b)$, and touched briefly on its geometric meaning. This lesson takes that geometric thread and pulls on it fully: classification, it turns out, is not fundamentally a statistical or symbolic operation — for a perceptron, it is **pure geometry**. Every question about what a perceptron *can* and *cannot* classify correctly has a direct, visualizable geometric answer, and this lesson builds that geometric picture from the ground up.

---

## Geometry

### Why Classification Becomes Geometry

A perceptron's decision rule is $y = 1$ if $\mathbf{w}\cdot\mathbf{x}+b \ge 0$, and $y=0$ otherwise. Notice that this rule never refers to "classes" in any abstract sense — it only ever asks a single numeric question: *which side of zero is $\mathbf{w}\cdot\mathbf{x}+b$ on?* Since this question has a precise geometric meaning (as the next section shows), **every classification decision a perceptron makes is equivalent to asking which side of a fixed geometric surface a point falls on.** This is why "can a perceptron learn this function?" and "can this dataset be cut into two pieces by a single flat surface?" turn out to be exactly the same question — not analogous to each other, but **literally identical**, which Section "Proofs" below makes fully precise.

### Line in 2D, Plane in 3D, Hyperplane in $n$D

Consider the equation $\mathbf{w}\cdot\mathbf{x}+b=0$ as a constraint on $\mathbf{x}$, in increasing dimension:

- **In 2D** ($\mathbf{x}=(x_1,x_2)$): $w_1x_1+w_2x_2+b=0$ is the equation of a **straight line**. This is just the familiar line equation in disguise — solving for $x_2$ gives $x_2 = -\frac{w_1}{w_2}x_1 - \frac{b}{w_2}$, the standard slope-intercept form.
- **In 3D** ($\mathbf{x}=(x_1,x_2,x_3)$): $w_1x_1+w_2x_2+w_3x_3+b=0$ is the equation of a flat **plane** cutting through 3D space.
- **In $n$ dimensions**: $w_1x_1+\dots+w_nx_n+b=0$ defines a **hyperplane** — an $(n-1)$-dimensional flat surface embedded in $n$-dimensional space. A hyperplane always has exactly one fewer dimension than the space it lives in: a point (0D) divides a line (1D); a line (1D) divides a plane (2D); a plane (2D) divides 3D space; and so on, with no limit on how far this pattern continues algebraically, even once it stops being directly visualizable.

The key unifying fact: **regardless of dimension, $\mathbf{w}\cdot\mathbf{x}+b=0$ always describes a flat object that splits the entire space into exactly two pieces.** This is what makes the perceptron's geometric behavior so uniform and predictable across any number of input features.

### Half-Spaces

The hyperplane itself is only the *boundary*. The two regions it separates are called **half-spaces**:

$$H^+ = \{\mathbf{x} : \mathbf{w}\cdot\mathbf{x}+b > 0\}, \qquad H^- = \{\mathbf{x} : \mathbf{w}\cdot\mathbf{x}+b < 0\}$$

(The perceptron's actual decision rule uses $\ge 0$ for class 1, which means class 1 technically includes the boundary itself, while class 0 is the strict open half-space $H^-$ — a minor convention detail, but worth being precise about.)

Every possible input $\mathbf{x}$ in the entire space falls into exactly one of three places: strictly inside $H^+$, strictly inside $H^-$, or exactly on the hyperplane itself ($z=0$). The perceptron's entire classification behavior is fully described by stating which half-space a point belongs to — nothing more.

### High-Dimensional Intuition

Visualizing a line or a plane is easy; visualizing a "hyperplane" in, say, 300 dimensions (a realistic feature count for many real datasets) is not something the human visual system can do directly. A few facts help build working intuition anyway:

- **The algebra doesn't care about dimension.** Every formula in this lesson — the hyperplane equation, half-space membership, distance to the hyperplane — is written using dot products and norms, operations that are defined identically whether $n=2$ or $n=20{,}000$. You don't need to *picture* a 300-dimensional hyperplane to compute exactly which side of it a point falls on.
- **"Flat" still means flat.** No matter the dimension, a hyperplane has zero curvature — it cannot bend around points the way a curved surface could. This is exactly why linear separability remains a strict, binary, dimension-independent property: either some flat cut exists, or it doesn't, regardless of how many dimensions you have to work with.
- **More dimensions generally make linear separability *easier* to achieve, not harder.** A famous and somewhat counterintuitive fact in high-dimensional geometry: as the number of features grows, a randomly-labeled set of points becomes increasingly likely to be linearly separable by *some* hyperplane, simply because there is so much more "room" to maneuver a flat cut around. (This is part of why mapping data into a higher-dimensional space — the core trick behind certain SVM kernels, discussed below — can turn a non-linearly-separable problem into a linearly separable one.)
- **A useful mental model:** think of a hyperplane in high dimensions not as a picture, but as a single number — the dot product $\mathbf{w}\cdot\mathbf{x}$ — measuring "how much does $\mathbf{x}$ point in the $\mathbf{w}$ direction." Classification, in any number of dimensions, is just thresholding that one number.

---

## Derivations

### Deriving $\mathbf{w}\cdot\mathbf{x}+b=0$ as the Decision Boundary

Start directly from the perceptron's prediction rule:

$$y = \begin{cases} 1 & \mathbf{w}\cdot\mathbf{x}+b \ge 0 \\ 0 & \mathbf{w}\cdot\mathbf{x}+b < 0 \end{cases}$$

The **decision boundary**, by definition, is the set of points where the prediction is *about to flip* — the exact transition between the two output regions. Algebraically, this transition happens precisely where the inequality becomes an equality, i.e., where the quantity being compared to zero **is** zero:

$$\mathbf{w}\cdot\mathbf{x}+b = 0$$

This is not an assumption or a design choice — it is a direct, forced consequence of how the step function $f$ is defined. Any model using a threshold-at-zero activation will always have its decision boundary located exactly where its raw score $z$ equals zero, by the same reasoning.

### Deriving the Class Assignment Rule, Geometrically

Restating the perceptron's output rule in purely geometric language:

$$y = \begin{cases} 1 & \mathbf{x} \in H^+ \text{ (including the boundary)} \\ 0 & \mathbf{x} \in H^- \end{cases}$$

This is exactly the same rule as before — only now expressed as "which half-space is the point in?" instead of "is this number non-negative?" The two phrasings are interchangeable by construction; the entire purpose of defining $H^+$ and $H^-$ algebraically (via the sign of $\mathbf{w}\cdot\mathbf{x}+b$) was to make this equivalence exact.

### Distance to the Hyperplane, and Signed Distance

It's often useful to know not just *which side* of the boundary a point is on, but **how far** it is from the boundary — this becomes essential for the margin concept next.

**Deriving the formula.** Take any point $\mathbf{x}_0$. We want the shortest (perpendicular) distance from $\mathbf{x}_0$ to the hyperplane $\mathbf{w}\cdot\mathbf{x}+b=0$. Recall from Section "Geometry" that $\mathbf{w}$ is normal (perpendicular) to the hyperplane. The shortest path from any point to a flat surface is always along the direction perpendicular to that surface — so the distance we want is the length of the projection of $\mathbf{x}_0$ onto the unit normal direction $\hat{\mathbf{w}} = \mathbf{w}/\|\mathbf{w}\|$, measured relative to the hyperplane.

A clean way to derive this: pick any point $\mathbf{x}_p$ that lies exactly on the hyperplane (so $\mathbf{w}\cdot\mathbf{x}_p+b=0$). The vector from $\mathbf{x}_p$ to $\mathbf{x}_0$ is $\mathbf{x}_0-\mathbf{x}_p$, and the distance we want is the length of this vector's projection onto $\hat{\mathbf{w}}$:

$$d = \hat{\mathbf{w}} \cdot (\mathbf{x}_0 - \mathbf{x}_p) = \frac{\mathbf{w}\cdot\mathbf{x}_0 - \mathbf{w}\cdot\mathbf{x}_p}{\|\mathbf{w}\|}$$

Since $\mathbf{w}\cdot\mathbf{x}_p = -b$ (because $\mathbf{x}_p$ is on the hyperplane), substitute:

$$d = \frac{\mathbf{w}\cdot\mathbf{x}_0 - (-b)}{\|\mathbf{w}\|} = \frac{\mathbf{w}\cdot\mathbf{x}_0+b}{\|\mathbf{w}\|}$$

This quantity, $\frac{\mathbf{w}\cdot\mathbf{x}_0+b}{\|\mathbf{w}\|}$, is the **signed distance** from $\mathbf{x}_0$ to the hyperplane: positive if $\mathbf{x}_0 \in H^+$, negative if $\mathbf{x}_0\in H^-$, and exactly zero on the boundary itself. The (unsigned) **distance** is simply its absolute value:

$$\boxed{d(\mathbf{x}_0) = \frac{|\mathbf{w}\cdot\mathbf{x}_0+b|}{\|\mathbf{w}\|}}$$

The sign tells you *which side*; the magnitude tells you *how far*. This single formula packs together everything the raw score $z=\mathbf{w}\cdot\mathbf{x}+b$ was only telling you implicitly: dividing by $\|\mathbf{w}\|$ converts the raw, scale-dependent score into an actual geometric distance, independent of how large or small the weight vector happens to be.

### Margins

The **margin** of a labeled point is, informally, "how confidently and how far on the correct side of the boundary" that point sits. Two related, precise definitions are used across the literature:

- **Functional margin:** for a labeled point $(\mathbf{x}_i, y_i)$ with $y_i \in \{-1,+1\}$ (a common convention switch from $\{0,1\}$ for this purpose), the functional margin is $y_i(\mathbf{w}\cdot\mathbf{x}_i+b)$ — positive exactly when the point is correctly classified, and larger when the raw score is further from zero in the correct direction.
- **Geometric margin:** the functional margin divided by $\|\mathbf{w}\|$ — i.e., the *actual distance* from the point to the boundary, signed so that correctly classified points have a positive geometric margin. This is exactly the signed distance derived above, just restricted to the labeled, signed-correctness framing.

The **margin of the entire dataset**, with respect to a given hyperplane, is the *smallest* geometric margin across all training points — i.e., how close the single most marginal (least confidently classified) point is to the boundary. A large dataset margin means every point is comfortably, confidently on its correct side; a small margin means at least one point sits dangerously close to flipping sides under tiny perturbations of the data or the weights.

This matters enormously in practice, even though the basic perceptron learning rule (from *Perceptron Era*) doesn't explicitly optimize for it: **a separating hyperplane with a small margin is fragile** — a small amount of noise in new, unseen data can push points across the boundary, leading to brittle generalization, even if the hyperplane perfectly separates the training data itself.

---

## Visual Intuition

### Example 1 — A Confidently Separated Dataset

```
        x2
         |
         |        ●  ●
         |      ●   ●     (class 1, well clear of the line)
         |
─────────┼──────────────────  ← w·x + b = 0
         |
      ○  ○
   ○    ○            (class 0, well clear of the line)
         |________________  x1
```

Every point sits far from the boundary on its correct side — a large dataset margin. Small perturbations to any point, or small adjustments to $\mathbf{w}$ and $b$, are very unlikely to flip any classification.

### Example 2 — A Fragile, Small-Margin Separation

```
        x2
         |
         |   ●  ○ ●  ○        ← points of both classes
         |  ●  ○  ●  ○          crowd right up against
─────────┼──────────────────    the boundary on both sides
         |
         |________________  x1
```

The classes are still technically linearly separable here — a line can still be drawn with all $\bullet$ on one side and all $\circ$ on the other — but only barely. The dataset margin is small, and a slightly different (but still perfectly separating) choice of line could classify a new, nearby test point completely differently than another equally valid separating line would. This is exactly the scenario margin-maximizing methods (next section) are designed to avoid.

### Example 3 — Varying the Bias, Visually

Using the same weight vector $\mathbf{w}$ (same orientation) but three different values of $b$:

```
   b = +2:  ──────────────────────  (shifted toward
                                       the ○ region)

   b =  0:      ──────────────────  (passes through
                                       the origin)

   b = -2:          ──────────────  (shifted toward
                                       the ● region)
```

The line's slope/orientation never changes (it's entirely determined by $\mathbf{w}$) — only its position shifts, exactly as derived algebraically in the previous lesson's exercises.

---

## Proofs

### Bridge: From Separating Hyperplanes to SVMs

The margin concept above leads naturally to a key conceptual fork in the road. The basic perceptron learning rule (covered in *Perceptron Era*) stops the moment it finds **any** hyperplane that correctly separates the training data — it has no preference between a hyperplane with a tiny margin and one with a large, comfortable margin, as long as both achieve zero training error.

**Support Vector Machines (SVMs)** start from exactly the same geometric object — a separating hyperplane, $\mathbf{w}\cdot\mathbf{x}+b=0$ — but add an explicit optimization objective: **find the hyperplane that maximizes the geometric margin** (the smallest distance from any training point to the boundary), rather than settling for the first separating hyperplane found. This is typically formalized as the constrained optimization problem:

$$\min_{\mathbf{w},b} \ \frac{1}{2}\|\mathbf{w}\|^2 \quad \text{subject to} \quad y_i(\mathbf{w}\cdot\mathbf{x}_i+b) \ge 1 \ \text{ for all training points } i$$

The training points that end up sitting *exactly* on the margin boundary (i.e., where the constraint is tight) are called **support vectors** — they are the only points that actually determine the final hyperplane's position; every other point could be moved or removed without changing the solution at all. This is a meaningfully different philosophy from the perceptron's mistake-driven rule: instead of stopping at the first valid separator, SVMs explicitly search for the *most robust* one, directly addressing the small-margin fragility illustrated in Example 2 above. (SVMs also extend, via the "kernel trick," to non-linearly-separable data by implicitly mapping inputs into a higher-dimensional space where a separating hyperplane *does* exist — a direct application of the high-dimensional intuition from the Geometry section.)

### Proof: A Perceptron Can Only Correctly Classify Linearly Separable Data

**Claim.** A perceptron, using the decision rule $y=f(\mathbf{w}\cdot\mathbf{x}+b)$ with a step activation, can achieve zero classification error on a labeled dataset $D = \{(\mathbf{x}_i, y_i)\}$ if and only if $D$ is linearly separable.

**Definition (linear separability).** $D$ is linearly separable if there exists *some* hyperplane (i.e., some $\mathbf{w}, b$) such that all class-1 points lie in $H^+$ and all class-0 points lie in $H^-$.

**Proof, forward direction ($\Rightarrow$).** Suppose some perceptron, with specific weights $\mathbf{w}^*$ and bias $b^*$, achieves zero classification error on $D$. By definition of zero error, every class-1 point $\mathbf{x}_i$ satisfies $\mathbf{w}^*\cdot\mathbf{x}_i+b^*\ge 0$ (i.e., lies in $H^+\cup\partial H$), and every class-0 point satisfies $\mathbf{w}^*\cdot\mathbf{x}_i+b^*<0$ (i.e., lies in $H^-$). But this is *precisely* the definition of $D$ being linearly separable, with the separating hyperplane being $\mathbf{w}^*\cdot\mathbf{x}+b^*=0$. Therefore, $D$ must be linearly separable. $\blacksquare$

**Proof, reverse direction ($\Leftarrow$).** Suppose $D$ is linearly separable — by definition, this means there exists *some* hyperplane, defined by some $\mathbf{w}, b$, with all class-1 points in $H^+$ and all class-0 points in $H^-$. But a perceptron with exactly those weights $\mathbf{w}$ and bias $b$ would then classify every point in $D$ correctly, by its decision rule — achieving zero classification error. (Separately, the Perceptron Convergence Theorem, covered in *Perceptron Era*, guarantees that the perceptron *learning algorithm* will actually find such weights in finite time, given that they exist — but the existence of correct weights, which is all this proof requires, follows immediately and directly from the definition of linear separability itself.) $\blacksquare$

**Conclusion.** Since both directions hold, "achievable zero error by some perceptron" and "linearly separable" are logically equivalent statements about a dataset — they are, in a precise sense, **the same property**, just described in two different vocabularies (one algebraic/model-based, one geometric/data-based). This is why XOR — proven not linearly separable in the *AI Winter* lesson — is unsolvable by a perceptron not as an empirical observation about a particular training run, but as a direct logical consequence of this equivalence: no amount of training, no learning rate adjustment, and no amount of additional training data can ever produce a correctly-classifying $\mathbf{w}, b$ for a dataset that is not linearly separable, because (by this proof) such weights would constitute a separating hyperplane that, by hypothesis, cannot exist.

---

## Exercises

1. Write the equation of the decision boundary for a perceptron with $\mathbf{w}=(3,-1)$, $b=6$, in standard slope-intercept form ($x_2 = mx_1+c$).
2. Compute the signed distance from the point $\mathbf{x}_0=(2,2)$ to the hyperplane defined by $\mathbf{w}=(3,4)$, $b=-10$. Is the point in $H^+$ or $H^-$?
3. For the same hyperplane as Exercise 2, find a *different* point that has the same signed distance but lies in the opposite half-space. (Hint: think about what "same magnitude of distance, opposite sign" implies geometrically.)
4. True or false, with justification: "If a dataset has a very small margin under some particular separating hyperplane, the data is not linearly separable." Use the definitions from this lesson to justify your answer precisely.
5. Without computing anything numerically, explain why scaling both $\mathbf{w}$ and $b$ by the same positive constant $c$ (i.e., using $c\mathbf{w}$ and $cb$ instead of $\mathbf{w}$ and $b$) does not change the decision boundary, but *does* change the raw score $z$ for any given point.

### Solutions

1. $3x_1 - x_2 + 6 = 0 \Rightarrow x_2 = 3x_1+6$. So $m=3$, $c=6$.
2. $\mathbf{w}\cdot\mathbf{x}_0+b = (3)(2)+(4)(2)+(-10) = 6+8-10=4$. $\|\mathbf{w}\|=\sqrt{3^2+4^2}=5$. Signed distance $=4/5=0.8$. Since the value is positive, the point is in $H^+$.
3. Any point with $\mathbf{w}\cdot\mathbf{x}+b = -4$ (i.e., signed distance $-0.8$) works — for example, solving $3x_1+4x_2-10=-4$, the point $(2,-1)$ satisfies $3(2)+4(-1)-10 = 6-4-10=-8$... let's instead pick directly: $(0,1.5)$ gives $3(0)+4(1.5)-10=6-10=-4$. ✓. This point lies in $H^-$, at the same distance (0.8) from the boundary as $\mathbf{x}_0$, but on the opposite side.
4. **False.** A small margin under a *particular* hyperplane only says that *that specific* hyperplane separates the data uncomfortably closely — it says nothing about whether a *different*, better-chosen hyperplane (e.g., the SVM-optimal maximum-margin one) might separate the same data with a much larger margin. Linear separability only requires that *some* separating hyperplane exists at all (Definition in the Proofs section) — it makes no claim about the margin of any specific one. A dataset could have one terrible, barely-separating hyperplane and also have a much better, large-margin hyperplane; both could be valid separators of the same linearly separable data.
5. The boundary is defined by the *equation* $\mathbf{w}\cdot\mathbf{x}+b=0$; multiplying both sides by a positive constant $c$ gives $c\mathbf{w}\cdot\mathbf{x}+cb=0$, which is satisfied by exactly the same set of points $\mathbf{x}$ as the original equation (scaling a "=0" equation by a nonzero constant doesn't change its solution set). However, for a point *not* on the boundary, the raw score itself scales directly: $c\mathbf{w}\cdot\mathbf{x}+cb = c(\mathbf{w}\cdot\mathbf{x}+b) = cz$, so the numeric value of $z$ changes proportionally with $c$, even though the classification decision (which side of zero) and the actual geometric distance (since $\|c\mathbf{w}\|=c\|\mathbf{w}\|$ also scales by $c$, canceling out in the distance formula) remain unchanged.