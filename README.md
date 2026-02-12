---

# 📊 Law of Large Numbers Simulation

A lightweight Python project demonstrating the **Law of Large Numbers (LLN)** through simple, visual simulations. The goal is to show how the **sample mean** of random variables stabilizes and converges to the **true mean** as the number of samples increases.

---

## ✨ What the LLN Says

For i.i.d. random variables X₁, X₂, … with finite expectation:

$$
\frac{1}{n} \sum_{i=1}^{n} X_i \;\longrightarrow\; \mathbb{E}[X] \quad \text{as } n \to \infty
$$

This means:  
👉 **Averages become predictable when the sample size grows.**

---

## 📁 Repository Structure

```
law-of-large-numbers-simulation/
│
├── src/
│   └── simulations
        └──simulate_lln.py
    └── plots
        └── plots_lln.py
│
├── notebooks/
│   └── LLN_Demo.ipynb
│
├── README.md
└── requirements.txt
```

---

## ▶️ Running the Simulation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the demo:

```bash
python src/simulate_lln.py
```

You’ll see a plot showing how the running sample mean approaches the true mean.

---

## 📈 Example: Normal Distribution

For a normal distribution X ~ 𝒩(0, 1):

- **True mean:** \( 0 \)

Running mean:

$$
\bar{X}_n = \frac{1}{n} \sum_{i=1}^{n} X_i
$$

**As \(n\) increases, (X̄ₙ) gets closer to \(0\), illustrating LLN in action.**

---
