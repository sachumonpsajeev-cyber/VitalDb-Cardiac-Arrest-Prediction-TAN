# 📘 Literature Review Repository — Cardiac Arrest Prediction using VitalDB + TAN

This repository contains the **structured literature review** supporting the Master’s thesis:

> **Cardiac Arrest Prediction using VitalDB and Temporal Attention Network (TAN)**

All papers are organized into three categories:
- 🔴 CORE PAPERS (foundation)
- 🟡 BENCHMARK PAPERS (performance comparison)
- 🟢 SUPPORTING PAPERS (methodology + gaps)

---

# 📂 Repository Structure

CORE
BENCHMARK
SUPPORTING


---

# 🔴 CORE PAPERS — Model & Dataset Foundation

## 📌 Purpose

Core papers define the **fundamental building blocks** of the thesis:

- Primary dataset (VitalDB)
- Core architectural ideas (attention, transformers, temporal modeling)
- Design inspiration for TAN model

These papers are **NOT performance comparisons**.  
They define *how the model is built*.

---

## 📚 Core Papers

| ID | Paper | Contribution |
|---|---|---|
| 1 | VitalDB (Lee et al., 2022) | Primary intraoperative dataset |
| 3 | TSCAN (Li et al., 2024) | Temporal-spatial attention mechanism |
| 10 | TERTIAN (An et al., 2022) | Time-aware hierarchical transformer |
| 11 | TFT (Kapral et al., 2024) | Transformer validation on VitalDB |

---

## 🧠 Role in Thesis

- Defines **data foundation (VitalDB)**
- Inspires **TAN architecture design**
- Validates **transformer applicability in OR setting**
- Provides **attention mechanism blueprint**

---

## ⚙️ Key Insight

> Core papers define *what the model is built from*, not how well it performs.

---

# 🟡 BENCHMARK PAPERS — Performance Comparison Standards

## 📌 Purpose

Benchmark papers define the **performance landscape** of cardiac arrest prediction models.

They are used to:

- Compare AUROC / AUPRC performance
- Establish state-of-the-art (SOTA)
- Define performance targets for TAN

---

## 📊 Performance Hierarchy
ML Models (0.84–0.88)
↓
LSTM / RNN Models (0.88–0.90)
↓
Hybrid Deep Learning (0.90–0.91)
↓
Transformer-based SOTA (≈0.92)


---

## 📚 Benchmark Papers

| ID | Paper | Model | AUROC | Role |
|---|---|---|---|---|
| 2 | Kwon et al., 2018 | RNN | 0.850 | Early DL baseline |
| 5 | FAST-PACE (Cho et al., 2020) | LSTM | 0.896 | Temporal DL baseline |
| 6 | Lee et al., 2022 | LGBM | 0.881 | ML baseline |
| 7 | Li et al., 2026 | TrGRU | 0.920 | Current SOTA |
| 8 | Chae et al., 2021 | Deep ML | 0.840 | Weak baseline |
| 12 | Lee et al., 2024 | Multimodal ML | 0.910 | Ensemble benchmark |
| 13 | Han et al., 2020 | Nested LSTM | 0.890 | Advanced RNN |

---

## 🎯 Thesis Target

The proposed TAN model aims to:

- Exceed **0.896 (LSTM baseline)**
- Compete with **0.910 (ensemble ML)**
- Approach or exceed **0.920 (SOTA TrGRU)**

---

## ⚙️ Key Insight

> Benchmark papers define *how hard the problem is and what must be beaten*.

---

# 🟢 SUPPORTING PAPERS — Methodology & Evidence Base

## 📌 Purpose

Supporting papers provide **scientific justification and methodological grounding** for the thesis.

They are used for:

- Explainability validation
- Feature engineering justification
- Literature gap identification
- ML vs statistical model comparison
- Temporal modeling motivation

---

## 📚 Supporting Papers

| ID | Paper | Contribution |
|---|---|---|
| 4 | Kim et al., 2024 | SHAP explainability framework |
| 9 | TA-RNN (Al Olaimat, 2024) | Time-aware irregular sequence modeling |
| 14 | Chen et al., 2022 | Systematic review + research gap analysis |
| 15 | Park et al., 2022 | VitalDB preprocessing + feature engineering |
| 16 | Churpek et al., 2016 | ML vs regression performance gap |

---

## 🧠 Role in Thesis

- Justifies **use of deep learning over regression/ML**
- Supports **interpretability via SHAP vs attention**
- Validates **VitalDB preprocessing pipeline**
- Identifies **research gaps in literature**
- Supports **temporal modeling assumptions**

---

## ⚙️ Key Insight

> Supporting papers define *why the thesis approach is necessary and valid*.

---

# 🎯 Overall Literature Review Logic
CORE → What the model is built on
BENCHMARK → What performance must be beaten
SUPPORTING → Why this approach is scientifically valid


---

# 🧠 Thesis Positioning Summary

This literature review establishes:

- VitalDB as a **high-fidelity intraoperative dataset**
- Temporal attention as the **key modeling paradigm**
- Transformer + RNN hybrids as **state-of-the-art direction**
- Gap in current research:  
  → Lack of **attention-based CA prediction in OR setting**

---

# 📌 Final Objective

This structured literature review supports development of:

> **Temporal Attention Network (TAN) for Cardiac Arrest Prediction using VitalDB**

---
