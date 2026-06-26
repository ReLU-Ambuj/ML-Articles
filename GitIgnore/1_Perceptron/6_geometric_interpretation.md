# Geometric Interpretation of the Perceptron

### The Fundamental Question

> **"What does a perceptron *look like* as a geometric object in input space?"**

Every algebraic fact about the perceptron — the weighted sum, the bias, the sign function, the update rule — has an exact geometric counterpart. Developing both views simultaneously is not redundant: the geometric picture makes many non-obvious algebraic facts immediately obvious, and vice versa.

---

## The Decision Hyperplane

### Definition

The perceptron's decision boundary is the set of all input vectors $\mathbf{x}$ where the output is exactly zero — the boundary between the positive and negative half-spaces:

$$\mathcal{H} = \{\mathbf{x} \in \mathbb{R}^n : \mathbf{w}\cdot\mathbf{x} + b = 0\}$$

For $n=2$ (two input features), $\mathcal{H}$ is a **line** in 2D space.  
For $n=3$, $\mathcal{H}$ is a **plane** in 3D space.  
For general $n$, $\mathcal{H}$ is a **(n−1)-dimensional hyperplane**.

### Normal Vector

The weight vector $\mathbf{w}$ is the **normal vector** to the hyperplane — it points perpendicularly to the decision surface and toward the positive half-space. This means:
- $\mathbf{w}$ tells you the *orientation* of the decision boundary
- $b$ tells you its *position* (how far it is from the origin along $\mathbf{w}$)

### Signed Distance from the Hyperplane

The signed distance from a point $\mathbf{x}$ to the hyperplane $\mathcal{H}$ is:

$$d(\mathbf{x}, \mathcal{H}) = \frac{\mathbf{w}\cdot\mathbf{x} + b}{\|\mathbf{w}\|}$$

This is the raw score $z$, divided by $\|\mathbf{w}\|$. Key properties:
- **Positive distance** → point is in the positive half-space → perceptron predicts +1
- **Negative distance** → point is in the negative half-space → perceptron predicts −1
- **Zero distance** → point is exactly on the boundary

The magnitude of $z = \mathbf{w}\cdot\mathbf{x} + b$ is therefore a *scaled* distance — proportional to the true geometric distance, with scale factor $\|\mathbf{w}\|$.

---

## Vectors, Angles, and Projections

### The Projection Revisited

From the weighted sum lesson, $\mathbf{w}\cdot\mathbf{x} = \|\mathbf{w}\|\|\mathbf{x}\|\cos\theta$. Combined with the signed distance formula:

$$d(\mathbf{x}, \mathcal{H}) = \frac{\|\mathbf{w}\|\|\mathbf{x}\|\cos\theta + b}{\|\mathbf{w}\|} = \|\mathbf{x}\|\cos\theta + \frac{b}{\|\mathbf{w}\|}$$

The decision rule is determined by whether $\mathbf{x}$'s projection onto $\hat{\mathbf{w}}$ exceeds $-b/\|\mathbf{w}\|$.

### Geometric View of the Update Rule

When the perceptron misclassifies a point, the update is $\mathbf{w} \leftarrow \mathbf{w} + \eta \cdot y \cdot \mathbf{x}$. Geometrically:
- This **rotates** the weight vector $\mathbf{w}$ toward the misclassified example (if $y=+1$, the example should be on the positive side, so $\mathbf{w}$ is pulled toward $\mathbf{x}$)
- The hyperplane **pivots** around its intersection with the origin (before considering $b$)
- With $b$, the boundary **translates and rotates** simultaneously

---

## Margin Geometry

### The Concept of Margin

Given a dataset that is **linearly separable**, many different hyperplanes correctly classify all points. The **margin** of a particular classifier $(\mathbf{w}, b)$ is the minimum distance from any training point to the decision boundary:

$$\gamma = \min_i \frac{y^{(i)}(\mathbf{w}\cdot\mathbf{x}^{(i)} + b)}{\|\mathbf{w}\|}$$

A larger margin means more confident correct classification on all training points.

**Why margin matters:**
- The **Support Vector Machine (SVM)** is exactly the perceptron generalized to *maximize* this margin
- Larger margin → better generalization (VC theory proves this formally)
- The perceptron finds *some* separating hyperplane — it does not seek the *maximum-margin* one

### 2D Visualization

```
        x₂
         |     +  +
         |   +    +        ← positive class (+1)
         |         +
  - -    |
    - -  |
      - -|---- decision boundary (w·x + b = 0)
        -|-
         |      margin
         |   ←──────────→
         ──────────────── x₁
         ↑
    negative class (−1)
    
  ┌─ w is the normal to the boundary, pointing toward the positive half-space
  └─ |b|/‖w‖ is the distance from origin to boundary along w
```

---

## Project: Visualizing Perceptron Geometry

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow

# Generate linearly separable 2D data
np.random.seed(42)
X_pos = np.random.randn(30, 2) + np.array([2, 2])
X_neg = np.random.randn(30, 2) + np.array([-2, -2])
X = np.vstack([X_pos, X_neg])
y = np.array([1]*30 + [-1]*30)

# Train perceptron
w = np.zeros(2); b = 0.0; lr = 0.01
for _ in range(200):
    for xi, yi in zip(X, y):
        if np.sign(np.dot(w, xi) + b) != yi:
            w += lr * yi * xi
            b += lr * yi

# Plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(X_pos[:, 0], X_pos[:, 1], c='royalblue', marker='+', s=100, label='+1 class')
ax.scatter(X_neg[:, 0], X_neg[:, 1], c='tomato', marker='o', s=60, label='-1 class')

# Decision boundary: w[0]*x1 + w[1]*x2 + b = 0  →  x2 = (-w[0]*x1 - b) / w[1]
x1 = np.linspace(-5, 5, 200)
x2 = (-w[0]*x1 - b) / w[1]
ax.plot(x1, x2, 'k-', linewidth=2, label='Decision boundary')

# Plot weight vector (normal to boundary)
ax.annotate('', xy=(w[0], w[1]), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', color='purple', lw=2))
ax.text(w[0]+0.1, w[1]+0.1, 'w (normal vector)', color='purple', fontsize=12)

# Compute and display margin
margins = y * (X @ w + b) / np.linalg.norm(w)
margin = margins.min()
ax.set_title(f'Perceptron Decision Boundary\nMargin = {margin:.3f}', fontsize=14)
ax.legend()
ax.set_xlabel('x₁'); ax.set_ylabel('x₂')
ax.grid(True, alpha=0.3)
ax.set_aspect('equal')
plt.tight_layout()
plt.savefig('perceptron_geometry.png', dpi=150)
plt.show()

print(f"Weight vector: w = {w}")
print(f"Bias: b = {b:.4f}")
print(f"Normal vector direction: angle = {np.degrees(np.arctan2(w[1], w[0])):.1f}°")
print(f"Distance from origin to boundary = {abs(b)/np.linalg.norm(w):.4f}")
print(f"Geometric margin = {margin:.4f}")
```

**Experiments to run:**
1. Vary the random seed — observe how different data configurations lead to different learned boundaries
2. Compare the perceptron's margin vs. scikit-learn's `LinearSVC(C=1e10)` (SVM with hard margin) — the SVM's margin will always be ≥ the perceptron's
3. Add a point equidistant from the positive and negative clusters — observe how it influences the learned boundary

---

## Connections

- **Perceptron Learning Rule** (next): each update is a geometric rotation/translation of the hyperplane
- **XOR Failure**: the proof that no single hyperplane can separate XOR data is a direct geometric argument
- **SVMs**: the maximum-margin hyperplane is the unique "best" linear boundary; the perceptron finds one of infinitely many valid boundaries
