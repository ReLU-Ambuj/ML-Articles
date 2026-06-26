# Perceptron Learning Rule

### The Fundamental Question

> **"Given a classification mistake, how exactly should the weights and bias be updated, and is there a guarantee this process terminates?"**

The perceptron learning rule is the first complete learning algorithm in this curriculum: it directly specifies how parameters change in response to errors. Unlike gradient descent (which will appear later), the perceptron rule is **mistake-driven** — parameters only change when the model is wrong, not in response to a smooth continuous loss signal.

---

## The Learning Rule: Derivation and Motivation

### Setup

Given training point $(\mathbf{x}, y)$ where $y \in \{-1, +1\}$, the current perceptron produces:

$$\hat{y} = \text{sign}(\mathbf{w}\cdot\mathbf{x} + b)$$

A **mistake** occurs when $\hat{y} \neq y$. This happens when:
- $y = +1$ but $\mathbf{w}\cdot\mathbf{x}+b < 0$ (true positive classified as negative)
- $y = -1$ but $\mathbf{w}\cdot\mathbf{x}+b \geq 0$ (true negative classified as positive)

### The Update Rule

On any mistake, update:

$$\mathbf{w} \leftarrow \mathbf{w} + \eta \cdot y \cdot \mathbf{x}$$
$$b \leftarrow b + \eta \cdot y$$

where $\eta > 0$ is the **learning rate**.

### Why This Works Intuitively

**Case 1: False negative** ($y=+1$, predicted −1, meaning $\mathbf{w}\cdot\mathbf{x}+b < 0$)

After update: $\mathbf{w}' = \mathbf{w} + \eta\mathbf{x}$. The new score on this point:

$$\mathbf{w}'\cdot\mathbf{x}+b' = (\mathbf{w}+\eta\mathbf{x})\cdot\mathbf{x}+(b+\eta) = (\mathbf{w}\cdot\mathbf{x}+b) + \eta(\|\mathbf{x}\|^2 + 1)$$

Since $\eta > 0$ and $\|\mathbf{x}\|^2 \geq 0$, the score **strictly increases** on this point after the update. The new weights are more inclined to classify this point as +1.

**Case 2: False positive** ($y=-1$, predicted +1, meaning $\mathbf{w}\cdot\mathbf{x}+b \geq 0$)

After update with $y=-1$: the score **strictly decreases** on this point. ∎

Note: a single update does not guarantee correct classification of this point (the increase may not be large enough to cross 0). But over repeated passes, the algorithm converges — this is what the Convergence Theorem proves.

---

## Convergence Theorem (Novikoff, 1962)

### Statement

**Perceptron Convergence Theorem:** If the training data is **linearly separable**, the perceptron algorithm with $\eta = 1$ (any fixed positive $\eta$ gives the same bound up to constants) makes at most

$$T \leq \left(\frac{R}{\gamma}\right)^2$$

mistakes before converging to a solution that correctly classifies all training examples, where:
- $R = \max_i \|\mathbf{x}^{(i)}\|$ is the maximum norm of any training point
- $\gamma$ is the geometric margin of the best separating hyperplane

### Proof Sketch

Let $\mathbf{w}^*$ be a unit-norm weight vector achieving margin $\gamma$ (so $y^{(i)}(\mathbf{w}^*\cdot\mathbf{x}^{(i)}+b^*) \geq \gamma$ for all $i$, with $b^*$ absorbed via augmentation).

Using the augmented vector trick, write $\tilde{\mathbf{w}} = (\mathbf{w}, b)$ and $\tilde{\mathbf{x}} = (\mathbf{x}, 1)$.

After $T$ mistakes, two bounds hold simultaneously:

**Lower bound on alignment:** Each update increases $\tilde{\mathbf{w}}_T \cdot \tilde{\mathbf{w}}^*$ by at least $\gamma$ (because the update is made on a misclassified point with margin $\gamma$). So $\tilde{\mathbf{w}}_T \cdot \tilde{\mathbf{w}}^* \geq T\gamma$.

**Upper bound on growth:** Each update increases $\|\tilde{\mathbf{w}}_T\|^2$ by at most $R^2$ (because the update adds $\tilde{\mathbf{x}}$ to $\tilde{\mathbf{w}}$, and $\|\tilde{\mathbf{x}}\|^2 \leq R^2 + 1$). So $\|\tilde{\mathbf{w}}_T\|^2 \leq TR^2$.

By Cauchy-Schwarz: $\tilde{\mathbf{w}}_T \cdot \tilde{\mathbf{w}}^* \leq \|\tilde{\mathbf{w}}_T\|\|\tilde{\mathbf{w}}^*\| = \|\tilde{\mathbf{w}}_T\|$.

Combining: $T\gamma \leq \|\tilde{\mathbf{w}}_T\| \leq \sqrt{T} \cdot R$, which gives $T \leq (R/\gamma)^2$. ∎

### Implications

1. **Finite convergence is guaranteed** for linearly separable data — not just "probably converges," but definitely, in at most $(R/\gamma)^2$ mistakes.
2. The bound depends on the **margin** $\gamma$ — data that is barely separable (small margin) can require many more mistakes than data with a large margin.
3. **If data is not linearly separable, the algorithm never terminates** — it cycles through mistakes forever. This is a fundamental limitation.

---

## Learning Rate and Epochs

### Learning Rate $\eta$

For the standard perceptron with {−1, +1} labels:
- $\eta$ **does not affect the final solution** (just the scale of $\mathbf{w}$), only the number of updates required
- Common choices: $\eta = 0.01$, $0.1$, $1.0$

For practical implementations with noisy or non-separable data, smaller $\eta$ can reduce oscillation.

### Online Learning

The perceptron is an **online learning** algorithm — it updates after each individual example, not after seeing the full dataset. Contrast with:
- **Batch gradient descent**: compute gradient over entire dataset, then update
- **Mini-batch SGD**: compute gradient over small batch, then update

Online learning has advantages: it can handle streaming data and is often faster in early training. It has disadvantages: updates can be noisy, and the order of examples affects convergence.

### Epochs

An **epoch** is one full pass through the entire training set. For the perceptron:
- After each epoch, count how many mistakes were made
- If 0 mistakes in a full epoch → the algorithm has converged (for separable data)
- Track `errors_per_epoch` as the primary convergence diagnostic

---

## Full Implementation with Convergence Tracking

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification, make_moons
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

class Perceptron:
    """
    Rosenblatt Perceptron with convergence tracking.
    Uses ±1 label convention.
    """
    def __init__(self, lr=0.01, max_epochs=500):
        self.lr = lr
        self.max_epochs = max_epochs
        self.w = None
        self.b = 0.0
        self.errors_per_epoch = []
        self.converged = False
        self.converged_at = None

    def fit(self, X, y):
        n_features = X.shape[1]
        self.w = np.zeros(n_features)
        self.b = 0.0

        for epoch in range(self.max_epochs):
            errors = 0
            for xi, yi in zip(X, y):
                z = np.dot(self.w, xi) + self.b
                y_pred = 1 if z >= 0 else -1
                if y_pred != yi:
                    self.w += self.lr * yi * xi
                    self.b += self.lr * yi
                    errors += 1
            self.errors_per_epoch.append(errors)
            if errors == 0:
                self.converged = True
                self.converged_at = epoch + 1
                break

        return self

    def predict(self, X):
        z = X @ self.w + self.b
        return np.where(z >= 0, 1, -1)

    def score(self, X, y):
        return np.mean(self.predict(X) == y)


# ── Experiment 1: Linearly Separable Data ──
X_lin, y_lin = make_classification(n_samples=200, n_features=2, n_informative=2,
                                    n_redundant=0, n_clusters_per_class=1,
                                    class_sep=2.0, random_state=42)
y_lin = np.where(y_lin == 1, 1, -1)
X_train, X_test, y_train, y_test = train_test_split(X_lin, y_lin, test_size=0.2, random_state=42)

p1 = Perceptron(lr=0.01, max_epochs=500)
p1.fit(X_train, y_train)
print(f"Linear data: converged={p1.converged}, epoch={p1.converged_at}")
print(f"Test accuracy: {p1.score(X_test, y_test):.3f}")

# ── Experiment 2: Non-Linearly Separable (Moons) ──
X_moon, y_moon = make_moons(n_samples=200, noise=0.2, random_state=42)
y_moon = np.where(y_moon == 1, 1, -1)
scaler = StandardScaler()
X_moon = scaler.fit_transform(X_moon)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X_moon, y_moon, test_size=0.2)

p2 = Perceptron(lr=0.01, max_epochs=100)
p2.fit(X_train2, y_train2)
print(f"\nMoon data: converged={p2.converged} (expected: False)")
print(f"Test accuracy: {p2.score(X_test2, y_test2):.3f}")

# ── Plot convergence ──
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(p1.errors_per_epoch, color='steelblue')
axes[0].set_title(f'Linear data — Errors per epoch\n(Converged at epoch {p1.converged_at})')
axes[0].set_xlabel('Epoch'); axes[0].set_ylabel('Mistakes')
axes[0].axvline(p1.converged_at - 1, color='red', linestyle='--', label='Convergence')
axes[0].legend()

axes[1].plot(p2.errors_per_epoch, color='tomato')
axes[1].set_title('Non-linear data — Errors per epoch\n(Never converges)')
axes[1].set_xlabel('Epoch'); axes[1].set_ylabel('Mistakes')

plt.tight_layout()
plt.savefig('perceptron_convergence.png', dpi=150)
plt.show()

# ── Learning rate comparison ──
lrs = [0.001, 0.01, 0.1, 1.0]
fig, ax = plt.subplots(figsize=(10, 5))
for lr in lrs:
    p = Perceptron(lr=lr, max_epochs=100)
    p.fit(X_train, y_train)
    ax.plot(p.errors_per_epoch, label=f'η={lr}')
ax.set_title('Effect of learning rate on convergence speed')
ax.set_xlabel('Epoch'); ax.set_ylabel('Mistakes')
ax.legend(); plt.tight_layout()
plt.savefig('perceptron_lr_comparison.png', dpi=150)
plt.show()
```

**Key observations to note:**
1. On linearly separable data: errors reach 0 and stay 0 (convergence proof verified empirically)
2. On moons data: errors oscillate indefinitely — the algorithm has no stopping criterion
3. Learning rate affects *speed* not *final accuracy* on separable data

---

## Connections

- **XOR Failure** (next): direct consequence of the convergence theorem — if data is not linearly separable, the theorem gives no guarantee
- **Gradient Descent** (Optimization chapter): the perceptron rule is a special case of gradient descent on the hinge loss, but only computed on misclassified examples
- **SVM**: the SVM modifies the learning objective to find the *maximum-margin* separator, not just any separator
