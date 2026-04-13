# 🔴 CORE PAPERS — Foundation of the Thesis

This folder contains the **core scientific foundations** of the thesis:

> *Cardiac Arrest Prediction using VitalDB and Temporal Attention Network (TAN)*

These papers define:
- The **dataset (VitalDB)**
- The **core architectural ideas (attention + transformers + temporal modeling)**
- The **design inspiration for TAN**

---

## 📌 Purpose of Core Papers

Core papers answer:

- What dataset is used?
- What architecture inspires TAN?
- What temporal modeling strategies are foundational?

They are NOT performance benchmarks — they are **conceptual building blocks**.

---

## 📚 Included Papers

| ID | Paper | Type | Role in Thesis |
|---|---|---|---|
| 1 | VitalDB (Lee et al., 2022) | Dataset | Primary dataset for all experiments |
| 3 | TSCAN (Li et al., 2024) | Attention model | Temporal-spatial attention design |
| 10 | TERTIAN (An et al., 2022) | Transformer | Hierarchical time-aware attention |
| 11 | TFT (Kapral et al., 2024) | Transformer (VitalDB) | Validates transformer use on intraoperative data |

---

## 🧠 Why These Are Core

### 1. VitalDB
- Provides high-resolution intraoperative signals
- Enables real-world OR-based prediction tasks

### 2. TSCAN
- Introduces **dual attention (temporal + spatial)**
- Direct inspiration for TAN dual-branch design

### 3. TERTIAN
- Introduces **time-aware transformer mechanisms**
- Helps model irregular physiological time-series

### 4. TFT (Kapral et al.)
- Demonstrates transformers work on **VitalDB itself**
- Validates feasibility of deep temporal architectures in OR setting

---

## 🏗️ How These Are Used in Thesis

- TAN architecture design is derived from:
  - Temporal attention → TERTIAN
  - Spatial attention → TSCAN
  - Transformer validation → TFT
- VitalDB is the **experimental backbone**

---

## ⚠️ Important Note

These papers are NOT compared using AUROC.
They define **how the model is built**, not how it performs.


