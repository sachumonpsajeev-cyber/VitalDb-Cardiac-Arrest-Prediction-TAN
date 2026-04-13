# 📘 Literature Review Repository — Cardiac Arrest Prediction using VitalDB + TAN

This repository contains the **background literature scoping document** that informed the Master's thesis:

> **Cardiac Arrest Prediction using VitalDB and Temporal Attention Network (TAN)**
> *Presented at RaTSiF-2026, Transport and Telecommunication Institute, Riga, April 2026*

> **Note:** This repository represents the **initial literature scoping phase** of the research. The final thesis references evolved as the methodology developed. The definitive citation list is in the submitted thesis document.

All papers are organized into three categories:
- 🔴 CORE PAPERS — dataset + confirmed architectural foundation
- 🟡 BENCHMARK PAPERS — performance comparison targets
- 🟢 SUPPORTING PAPERS — methodology, gaps, and validation

---

# 📂 Repository Structure
CORE/
BENCHMARK/
SUPPORTING/

---

# 🔴 CORE PAPERS — Dataset & Architectural Foundation

## 📌 Purpose

Core papers define the **primary dataset and the architectural landscape** that shaped the TAN design direction:

- Primary intraoperative dataset (VitalDB)
- Attention and transformer ideas explored during design
- Temporal modeling concepts considered for TAN

> These papers represent the **research foundation explored during planning**. The final thesis architecture was justified by additional papers discovered during implementation.

---

## 📚 Core Papers

| ID | Paper | Authors | Year | Contribution to Planning |
|---|---|---|---|---|
| 1 | VitalDB | Lee et al. | 2022 | Primary intraoperative dataset — confirmed in thesis |
| 3 | TSCAN | Li et al. | 2024 | Temporal-spatial attention — explored during design |
| 10 | TERTIAN | An et al. | 2022 | Time-aware hierarchical transformer — design reference |
| 11 | TFT | Kapral et al. | 2023 | Transformer on VitalDB — intraoperative validation |

---

## ⚙️ Key Insight

> Core papers define *what the model planning was built from*. VitalDB (#1) is the confirmed dataset foundation. Papers #3, #10, #11 were architectural references explored during the design phase.

---

# 🟡 BENCHMARK PAPERS — Performance Comparison Standards

## 📌 Purpose

Benchmark papers define the **performance landscape** of cardiac arrest prediction models and establish targets for the TAN to compete against.

---

## 📊 Performance Hierarchy
ML Models            (0.84 – 0.88)
↓
LSTM / RNN           (0.88 – 0.90)
↓
Hybrid Deep Learning (0.90 – 0.91)
↓
Transformer SOTA     (≈ 0.92)

---

## 📚 Benchmark Papers

| ID | Paper | Authors | Year | Model | AUROC | Role |
|---|---|---|---|---|---|---|
| 2 | DEWS | Kwon et al. | 2018 | RNN | 0.850 | First DL baseline |
| 5 | FAST-PACE | Cho et al. | 2020 | LSTM | 0.896 | Temporal DL baseline |
| 6 | HRV Real-Time | Lee et al. | 2022 | LGBM | 0.881 | ML real-time baseline |
| 7 | TrGRU | Li et al. | 2026 | GRU | 0.920 | Current SOTA target |
| 8 | Shallow vs Deep | Chae et al. | 2021 | Deep ML | 0.840 | Weak baseline |
| 12 | Multimodal IHCA | Lee et al. | 2024 | Multimodal | 0.910 | Ensemble benchmark |
| 13 | Nested LSTM | Han et al. | 2020 | Nested LSTM | 0.890 | Advanced RNN baseline |

---

## 🎯 Planning Target

During the scoping phase, the TAN was designed to:

- Exceed **0.896** (LSTM baseline — Cho et al.)
- Compete with **0.910** (ensemble ML — Lee et al.)
- Approach or exceed **0.920** (SOTA — Li et al.)

> **Actual thesis result:** TAN+LSTM ensemble achieved **AUROC 0.9180** on the multi-window VitalDB cohort, consistent with the targets set during this scoping phase.

---

## ⚙️ Key Insight

> Benchmark papers define *how hard the problem is and what performance must be beaten*.

---

# 🟢 SUPPORTING PAPERS — Methodology & Evidence Base

## 📌 Purpose

Supporting papers provide **scientific justification and methodological grounding** explored during the research planning phase.

---

## 📚 Supporting Papers

| ID | Paper | Authors | Year | Contribution |
|---|---|---|---|---|
| 4 | Explainable ML for CA | Kim et al. | 2024 | SHAP explainability framework |
| 9 | TA-RNN | Al Olaimat | 2024 | Time-aware irregular sequence modeling |
| 14 | Systematic Review | Chen et al. | 2022 | ML-CA landscape + gap analysis |
| 15 | Intraop Hypotension | Park et al. | 2022 | VitalDB preprocessing + feature engineering |
| 16 | ML vs Regression | Churpek et al. | 2016 | ML necessity over regression |

---

## ⚙️ Key Insight

> Supporting papers define *why a temporal attention approach to intraoperative CA prediction is scientifically necessary and valid*.

---

# 🎯 Overall Literature Scoping Logic

CORE       → What the model was planned to be built on
BENCHMARK  → What performance must be beaten
SUPPORTING → Why this approach is scientifically valid

---

# 🧠 Thesis Positioning Summary

This scoping review established the research direction toward:

- **VitalDB** as the primary high-fidelity intraoperative dataset
- **Temporal attention** as the key modeling paradigm
- **Transformer + RNN hybrids** as the state-of-the-art direction
- A clear research gap: no attention-based CA prediction model validated on VitalDB

---

# 📊 Scoping vs Final Thesis

| Aspect | This Scoping Document | Final Thesis |
|---|---|---|
| Papers reviewed | 16 focused papers | 60 papers across 7 themes |
| Purpose | Planning and direction-setting | Full empirical study |
| Dataset | VitalDB identified | VitalDB confirmed and used |
| Architecture | TAN planned | Two-stage TAN+LSTM implemented |
| Result | Target AUROC ~0.92 | Achieved AUROC 0.9180 |
| Status | Background research | Submitted and presented at RaTSiF-2026 |

---

# 📌 Final Note

This repository is a **research planning artifact**. The complete methodology, full citation list, and empirical results are documented in the submitted thesis. The 16 papers reviewed here represent the initial scoping phase that shaped the research direction — the final thesis expanded significantly beyond this foundation.
