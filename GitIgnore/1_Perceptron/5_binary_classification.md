# Binary Classification

### The Fundamental Question

> **"Given a new data point, which of the two classes does it belong to?"**

Binary classification is the simplest complete learning task: every input belongs to exactly one of two mutually exclusive categories, and the model must decide which. The perceptron, as derived in previous lessons, is one specific solution to this problem — but understanding *binary classification as a problem class* before diving into perceptron mechanics clarifies why each architectural choice exists and what alternatives look like.

---

## Formal Setup

### The Two Classes

By convention, the two classes are labeled **positive (+1)** and **negative (−1)** — or equivalently, 1 and 0 in logistic regression convention. The perceptron uses ±1.

Every training example is a pair $(\mathbf{x}^{(i)}, y^{(i)})$ where:
- $\mathbf{x}^{(i)} \in \mathbb{R}^n$ is the feature vector
- $y^{(i)} \in \{-1, +1\}$ is the ground-truth label

The task: learn a function $f: \mathbb{R}^n \to \{-1, +1\}$ that maps new, unseen inputs to the correct class.

### The Decision Rule

For the perceptron, the decision rule is:

$$\hat{y} = \text{sign}(z) = \text{sign}(\mathbf{w} \cdot \mathbf{x} + b) = \begin{cases} +1 & \text{if } \mathbf{w}\cdot\mathbf{x}+b \ge 0 \\ -1 & \text{if } \mathbf{w}\cdot\mathbf{x}+b < 0 \end{cases}$$

This defines a hyperplane $\{\mathbf{x} : \mathbf{w}\cdot\mathbf{x}+b = 0\}$ that partitions input space into two half-spaces: the positive half-space (output = +1) and the negative half-space (output = −1).

---

## Classification Errors

### The Four Outcomes

For any single prediction, exactly one of four cases holds:

| Ground Truth | Prediction | Name | Consequence |
|---|---|---|---|
| +1 | +1 | **True Positive (TP)** | Correct |
| −1 | −1 | **True Negative (TN)** | Correct |
| −1 | +1 | **False Positive (FP)** | Type I error |
| +1 | −1 | **False Negative (FN)** | Type II error |

These four quantities define the **confusion matrix** — the complete picture of a classifier's behavior beyond a single summary statistic.

### Accuracy

$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN} = \frac{\text{correct predictions}}{\text{total predictions}}$$

Accuracy is intuitive but misleading on **imbalanced datasets**. If 95% of examples are class −1 (e.g., non-fraud in fraud detection), a classifier that always predicts −1 achieves 95% accuracy while being completely useless.

### Precision and Recall

$$\text{Precision} = \frac{TP}{TP + FP} \qquad \text{Recall} = \frac{TP}{TP + FN}$$

- **Precision**: of all the points predicted positive, what fraction truly are positive? Measures the cost of false alarms.
- **Recall**: of all truly positive points, what fraction did we catch? Measures the cost of misses.

The precision-recall tradeoff is fundamental: most classifiers (not just perceptrons) can be tuned to increase one at the expense of the other.

### F1 Score

The harmonic mean of precision and recall:

$$F_1 = \frac{2 \cdot \text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$$

The harmonic mean (not arithmetic) is used because it penalizes extreme imbalance between the two: if either precision or recall is near zero, $F_1$ is near zero regardless of the other.

### For the Perceptron Specifically

The perceptron makes hard binary decisions — it has no notion of confidence or probability. This means:
- There is no natural way to tune the precision/recall tradeoff (no threshold to adjust)
- The decision boundary is fixed once training converges
- All misclassifications are treated equally by the learning rule

These limitations motivate logistic regression (which outputs probabilities) and SVMs (which maximize the margin rather than just finding *any* separating hyperplane).

---

## Why Two Classes Before Many?

Multiclass classification (k > 2 classes) is typically reduced to binary classification via:
- **One-vs-Rest:** train k binary classifiers, one per class against all others
- **One-vs-One:** train k(k−1)/2 binary classifiers, one per class pair

Understanding binary classification fully is prerequisite to understanding these reductions. The perceptron, and later logistic regression and SVMs, all begin in the binary case and generalize.

---

## Worked Example: Medical Diagnosis

**Problem:** Classify patients as having a condition (+1) or not (−1) based on two blood markers $x_1$ (glucose level) and $x_2$ (inflammatory marker).

**Learned weights** (hypothetical, after training): $\mathbf{w} = (0.3, 0.5)$, $b = -40$.

For a new patient with $\mathbf{x} = (110, 60)$:

$$z = (0.3)(110) + (0.5)(60) - 40 = 33 + 30 - 40 = 23$$

Since $z = 23 > 0$, $\hat{y} = +1$ → predicted to have the condition.

For $\mathbf{x} = (80, 20)$:

$$z = (0.3)(80) + (0.5)(20) - 40 = 24 + 10 - 40 = -6$$

Since $z = -6 < 0$, $\hat{y} = -1$ → predicted healthy.

---

## Project: Binary Classification on a Real Dataset

**Dataset:** Breast Cancer Wisconsin (from `sklearn.datasets.load_breast_cancer`)

**Task:** Classify tumors as malignant (+1) or benign (−1) from 30 features.

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

# Load and prepare data
data = load_breast_cancer()
X, y = data.data, data.target
y = np.where(y == 1, 1, -1)  # Convert to ±1 convention

# Split and scale
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Implement Perceptron from scratch
class Perceptron:
    def __init__(self, lr=0.01, epochs=100):
        self.lr = lr
        self.epochs = epochs
        self.w = None
        self.b = None
        self.errors_per_epoch = []

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.w = np.zeros(n_features)
        self.b = 0.0
        for epoch in range(self.epochs):
            errors = 0
            for xi, yi in zip(X, y):
                z = np.dot(self.w, xi) + self.b
                y_pred = np.sign(z) if z != 0 else -1
                if y_pred != yi:
                    self.w += self.lr * yi * xi
                    self.b += self.lr * yi
                    errors += 1
            self.errors_per_epoch.append(errors)
        return self

    def predict(self, X):
        z = np.dot(X, self.w) + self.b
        return np.where(z >= 0, 1, -1)

# Train
model = Perceptron(lr=0.01, epochs=200)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred, target_names=['Malignant', 'Benign']))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
```

**What to observe:**
- Accuracy before vs. after feature scaling (run both)
- Number of errors per epoch (plot `model.errors_per_epoch`)
- What happens with different learning rates (0.001, 0.01, 0.1)
- Cases where the perceptron fails to converge (add noise to make data non-linearly separable)

---

## Connections to Next Topics

- **Geometric Interpretation** (next): the confusion matrix error types correspond directly to points on the wrong side of the decision hyperplane
- **Perceptron Learning Rule**: the update rule is triggered precisely by classification errors (TP and TN generate no update)
- **Logistic Regression**: replaces the hard sign() decision with a smooth probability, enabling gradient-based training and probability calibration
