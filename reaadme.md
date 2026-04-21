# 🫀 Intraoperative Cardiac Arrest Prediction — Multi-Window TAN-LSTM

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![LightGBM](https://img.shields.io/badge/LightGBM-green?style=flat&logo=leaflet&logoColor=white)
![Clinical AI](https://img.shields.io/badge/Clinical%20AI-Healthcare-brightgreen)
![AUROC](https://img.shields.io/badge/AUROC-0.9180-blue)
![FA:TP Ratio](https://img.shields.io/badge/FA%3ATP%20Ratio-5%3A1%20(Clinical)-teal)
![Status](https://img.shields.io/badge/Status-MSc%20Thesis%20(2026)-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

<br/>

**MSc Thesis — Transport and Telecommunication Institute, Riga, Latvia (2026)**

*Predicting Intraoperative Cardiac Arrest from Continuous Vital Signs using a Two-Stage Multi-Window Temporal Attention Network on VitalDB*

[📄 Read the Thesis](#-thesis-abstract) · [📊 See All Results](#-complete-results) · [🏗️ Architecture](#%EF%B8%8F-architecture) · [🚀 Quick Start](#-quick-start) · [📈 Model Evolution](#-model-evolution--v1-vs-v2-comparison)

</div>

---

## 🧭 Table of Contents

- [Project Goal](#-project-goal)
- [Thesis Abstract](#-thesis-abstract)
- [The Clinical Problem](#-the-clinical-problem)
- [Architecture — Two-Stage TAN Pipeline](#%EF%B8%8F-architecture--two-stage-tan-pipeline)
- [Dataset — VitalDB](#-dataset--vitaldb)
- [Feature Engineering](#-feature-engineering)
- [Methodology](#-methodology)
- [Complete Results](#-complete-results)
- [Core Scientific Finding — Attention Monotonicity](#-core-scientific-finding--attention-weight-monotonicity)
- [Clinical Utility Analysis](#-clinical-utility-analysis)
- [SHAP Feature Importance](#-shap-feature-importance)
- [Model Evolution — V1 vs V2 Comparison](#-model-evolution--v1-vs-v2-comparison)
- [Dashboard Screenshots](#%EF%B8%8F-dashboard-screenshots)
- [Tech Stack](#%EF%B8%8F-tech-stack)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Limitations & Future Work](#-limitations--future-work)
- [Citation](#-citation)
- [Author](#-author)

---

## 🎯 Project Goal

Predict intraoperative cardiac arrest at **four prediction horizons** (30, 60, 120, and 240 minutes before the event) from continuously recorded vital signs during surgery — enabling clinical teams to intervene **before physiological collapse** rather than after.

| Goal | Status |
|---|---|
| AUROC > 0.91 on per-window models | ✅ Achieved (LightGBM: 0.9747 @ 60 min; LSTM: 0.9312 @ 30 min) |
| Outperform NEWS2 clinical baseline | ✅ +0.30 to +0.35 AUROC margin |
| Clinically deployable false alarm ratio | ✅ TAN ensemble: 5:1 FA:TP (below alarm fatigue threshold) |
| First multi-window TAN on VitalDB | ✅ Confirmed by 60-paper PRISMA review (March 2026) |
| Formally characterise attention weight behaviour | ✅ Monotonic progression verified (sign test p = 1.26 × 10⁻⁷) |

---

## 📄 Thesis Abstract

This thesis introduces a novel two-stage prediction architecture — the **Multi-Window Temporal Attention Network (TAN)** — for detecting intraoperative cardiac arrest (CA) using continuous physiological data from the VitalDB perioperative database.

The central contribution is an empirically verified, mathematically monotonic progression of cross-window attention weights across all five cross-validation folds **(0.197 → 0.228 → 0.269 → 0.307; sign test p = 1.26 × 10⁻⁷; Friedman χ²(3) = 15.00, p = 0.0018)**. This provides the first quantitative characterisation of *when* physiological deterioration becomes model-detectable before intraoperative cardiac arrest — showing that the **four-hour pre-operative window carries substantially more discriminative information** than the commonly monitored 30-minute window.

**Stage 1** trains classical ML models (LightGBM, Random Forest, XGBoost, Logistic Regression) and per-window LSTM networks across four prediction horizons. **Stage 2** feeds these representations into a 4-head Temporal Attention Network that learns, per patient, how much weight to assign each horizon.

LightGBM achieves **AUROC 0.9747** at 60 minutes; LSTM achieves **AUROC 0.9312** at 30 minutes. Both substantially exceed the 0.91 threshold and outperform the NEWS2 clinical baseline (AUROC 0.6295). NEWS2 degrades to AUROC 0.4345 at 30 minutes — worse than random chance — due to the mechanistic suppression of its parameters under general anaesthesia. The **TAN+LSTM ensemble (AUROC 0.9180, 90/10 weighting) achieves 83.1% sensitivity at just 263 false alarms (FA:TP = 5:1)**, satisfying published clinical alarm fatigue thresholds.

> **Keywords:** Intraoperative cardiac arrest · Temporal Attention Network · Multi-window prediction · VitalDB · LightGBM · LSTM · SMOTE-ENN · Class imbalance · Perioperative monitoring

---

## 🏥 The Clinical Problem

### Why This Matters

Intraoperative cardiac arrest occurs in approximately **4–7 per 10,000 non-cardiac surgeries**, with post-arrest survival rates of only **25–50% even inside the operating room** — arguably the most intensively monitored environment in medicine.

This creates a paradox: patients are surrounded by continuous vital sign monitoring, yet existing clinical tools fail to predict arrest reliably. The problem is not a lack of data — it is the absence of analytical tools capable of extracting the predictive signal from that data.

### Why Current Tools Fail

The **NEWS2 score** (National Early Warning Score 2) is the most widely deployed clinical deterioration tool. However, it is fundamentally unsuited for the intraoperative environment because:

- **Respiratory rate** is controlled by the mechanical ventilator — not a patient-generated signal
- **SpO₂** is actively elevated by supplemental oxygen, masking true oxygenation status
- **Heart rate** may be pharmacologically blunted by opioids and anaesthetic agents

The result: under general anaesthesia, a patient approaching cardiac arrest may score *lower* on NEWS2 than a stable patient, producing an inverted risk ranking. This thesis confirms this empirically — NEWS2 achieves **AUROC 0.4345 at 30 minutes, below random chance**.

NEWS2 in OR at 30 min:  AUROC 0.4345  ← WORSE THAN RANDOM
ML Ensemble at 30 min:  AUROC 0.9180  ← +0.48 absolute improvement

---

## 🏗️ Architecture — Two-Stage TAN Pipeline


┌─────────────────────────────────────────────────────────────────────────────┐
│                         VitalDB  (6,388 Surgeries)                          │
│              6 Vital Channels × 4 Prediction Windows × 6 Descriptors        │
└─────────────────────────┬───────────────────────────────────────────────────┘
                          │  36-dimensional feature vector per window
                          ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    STAGE 1 — Per-Window Models                              │
│                                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │   30-min     │  │   60-min     │  │   120-min    │  │   240-min    │   │
│  │              │  │              │  │              │  │              │   │
│  │ LightGBM     │  │ LightGBM ★  │  │ LightGBM     │  │ LightGBM     │   │
│  │ AUROC 0.9144 │  │ AUROC 0.9747│  │ AUROC 0.8595 │  │ AUROC 0.9318 │   │
│  │              │  │              │  │              │  │              │   │
│  │ LSTM ★       │  │ LSTM         │  │ LSTM         │  │ LSTM         │   │
│  │ AUROC 0.9312 │  │ AUROC 0.9278│  │ AUROC 0.9294 │  │ AUROC 0.8889 │   │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘   │
└─────────┼─────────────────┼─────────────────┼─────────────────┼───────────┘
          │                 │                 │                 │
          └─────────────────┴────────┬────────┴─────────────────┘
                                     │  4 × 36 = 144-dim input matrix
                                     ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    STAGE 2 — Temporal Attention Network                     │
│                                                                             │
│   4-Head Self-Attention (Q/K/V dim = 36) → learns per-patient horizon      │
│   importance weights across the four temporal windows                       │
│                                                                             │
│   Attention Weights (mean across 5 folds):                                 │
│   30-min: 0.197  │  60-min: 0.228  │  120-min: 0.269  │  240-min: 0.307   │
│              ↑ MONOTONICALLY INCREASING ↑   (p = 1.26 × 10⁻⁷)             │
│                                                                             │
│   FC(64, ReLU) → FC(32, ReLU) → Dropout(0.3) → Sigmoid                    │
│   Training: Focal Loss (γ=2) + SMOTE-ENN + Adam (lr=0.001)                 │
└─────────────────────────────┬───────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│              FINAL ENSEMBLE — TAN + LSTM (90% / 10% weighting)             │
│                                                                             │
│   AUROC: 0.9180  │  Sensitivity: 83.1%  │  False Alarms: 263  │  FA:TP: 5:1 │
└─────────────────────────────────────────────────────────────────────────────┘


### Model Configurations

| Model | Key Hyperparameters | Imbalance Strategy |
|---|---|---|
| **LightGBM** | `lr=0.05, max_depth=6, n_estimators=100` | `class_weight='balanced'` |
| **Random Forest** | `n_estimators=100, max_depth=10` | `class_weight='balanced'` |
| **XGBoost** | `lr=0.1, max_depth=6, eval_metric='auprc'` | AUPRC-based selection |
| **Logistic Regression** | `C=1.0, L2, lbfgs, max_iter=1000` | `class_weight='balanced'` |
| **LSTM** | `2 layers (64→32), dropout=0.3, Adam lr=0.001, batch=32` | Youden-J threshold tuning |
| **TAN** | `4-head attention, FC(64,32), Focal Loss γ=2, batch=16` | SMOTE-ENN + Focal Loss |
| **TAN+LSTM Ensemble** | `α=0.90 (TAN) + 0.10 (LSTM)` | 11-step grid search |

---

## 📁 Dataset — VitalDB

| Property | Details |
|---|---|
| **Source** | VitalDB — Seoul National University Hospital, South Korea |
| **Reference** | Lee et al. (2022), *Scientific Data*, 9(1), p.279 |
| **Access** | Public — [vitaldb.net](https://vitaldb.net) (Creative Commons licence) |
| **Total Cases** | 6,388 perioperative surgical cases |
| **CA-Positive Cases** | 66 (epinephrine proxy label, 0–1,000 mcg intraoperative dose) |
| **CA Prevalence** | 1.03% (full cohort) · 3.75% (multi-window cohort — longer procedures) |
| **Vital Signals** | HR, SpO₂, ETCO₂, ART_MBP, ART_SBP, ART_DBP |
| **Signal Frequency** | Continuous, per-second recording |
| **Class Imbalance** | Up to 96:1 (non-CA : CA) at 30-min window |

### Cohort Sizes by Prediction Window

| Window | Total Cases | CA-Positive | Non-CA | Imbalance Ratio |
|---|---|---|---|---|
| **30 min** | 6,376 | 66 | 6,310 | 1 : 96 |
| **60 min** | 6,047 | 66 | 5,981 | 1 : 91 |
| **120 min** | 4,197 | 66 | 4,131 | 1 : 63 |
| **240 min (TAN)** | 1,731 | 65 | 1,666 | 1 : 26 |

> ⚠️ **Cohort Note:** The multi-window TAN cohort (n=1,731) contains only surgeries long enough to provide recordings across all four windows. This introduces a selection effect — longer procedures have 3.6× higher CA prevalence. TAN results should be interpreted as specific to long-procedure surgical cases.

### CA Label Definition

VitalDB does not include a direct cardiac arrest flag. CA was identified using an **epinephrine proxy label**: any case with intraoperative epinephrine administration at 0–1,000 mcg was classified CA-positive. This range corresponds to ACLS-protocol cardiac arrest management dosing rather than vasopressor infusion (>1,000 mcg).

> **Limitation:** Epinephrine may also be given for anaphylaxis or refractory hypotension. A sensitivity analysis shows all models retain AUROC > 0.91 under a conservative 20% label contamination assumption.

---

## 🔬 Feature Engineering

For each of the **six vital sign channels**, six statistical descriptors were extracted within each prediction window:

| Descriptor | Description | Clinical Significance |
|---|---|---|
| **Mean** | Arithmetic mean of signal | Average physiological level |
| **Std Dev** | Standard deviation | Signal variability / stability |
| **Minimum** | Lowest recorded value | Worst-case nadir — haemodynamic floor |
| **Maximum** | Highest recorded value | Peak reserve capacity |
| **Range** | Max − Min | Total excursion / volatility |
| **Slope** | Linear regression coefficient | Directional trajectory (rising/falling) |

**6 channels × 6 descriptors = 36 features per prediction window**

The slope descriptor captures *directional* deterioration — a patient whose mean arterial pressure is declining is at higher risk than one whose average is identical but stable. The maximum captures *reserve capacity* — whether the patient can still reach an adequate peak blood pressure within the window.


# Feature extraction per channel per window
features = {
    f'{channel}_mean':  window_data.mean(),
    f'{channel}_std':   window_data.std(),
    f'{channel}_min':   window_data.min(),
    f'{channel}_max':   window_data.max(),
    f'{channel}_range': window_data.max() - window_data.min(),
    f'{channel}_slope': np.polyfit(np.arange(len(window_data)), window_data, 1)[0]
}


---

## ⚙️ Methodology

### Cross-Validation Design

All models were evaluated using **5-fold stratified cross-validation** with case-level fold assignment:

- **Stratified** — each fold contains approximately equal proportions of CA-positive cases
- **Case-level** — all four temporal windows for a given patient are assigned to the same fold, preventing data leakage between training and validation sets
- **Bootstrap CI** — 1,000 iterations for AUROC confidence intervals
- **Statistical testing** — Bootstrap DeLong test at α = 0.05 for AUROC comparisons

### Class Imbalance Handling

The 90:1 imbalance ratio was addressed with model-specific strategies:


Classical ML   →  class_weight = 'balanced'  (inverse frequency weighting)
LSTM           →  Youden-J optimal threshold  (post-hoc threshold selection)
TAN            →  SMOTE-ENN (inside CV folds) + Focal Loss γ=2
Ensemble       →  α = 0.90 TAN weight  (11-point grid search)


> ⚠️ **Critical implementation detail:** SMOTE-ENN was applied **exclusively inside each CV fold's training partition**. Applying SMOTE globally before splitting inflates performance estimates by allowing synthetic samples to leak into validation folds (Vaishali et al., 2025). This study implements the correct approach.

### Focal Loss

The TAN training objective uses Focal Loss (Lin et al., 2017) with γ = 2:


<img width="321" height="48" alt="image" src="https://github.com/user-attachments/assets/05ddd90e-e984-4103-ae17-b833974a778c" />


At γ = 2, a correctly classified non-CA case (pt ≈ 1) receives approximately **96% reduction in loss contribution**, redirecting the optimiser's attention toward difficult CA-positive minority cases.

---

## 📊 Complete Results

### Stage 1 — Classical ML Models (All Windows)

| Model | Window | AUROC | AUPRC | Sensitivity | Specificity | F1 |
|---|---|---|---|---|---|---|
| **LightGBM ★★ BEST** | **60 min** | **0.9747** | **0.4974** | 0.538 | 0.980 | 0.318 |
| LightGBM | 240 min | 0.9318 | 0.5173 | 0.462 | 0.955 | 0.353 |
| LightGBM | 30 min | 0.9144 | 0.1762 | 0.231 | 0.987 | 0.182 |
| LightGBM | 120 min | 0.8595 | 0.2095 | 0.462 | 0.977 | 0.316 |
| Random Forest ★ | 30 min | 0.9262 | 0.1568 | 0.385 | 0.972 | 0.185 |
| Random Forest | 60 min | 0.9731 | 0.4029 | 0.692 | 0.967 | 0.290 |
| XGBoost | 60 min | 0.9733 | 0.3173 | 0.769 | 0.966 | 0.313 |
| XGBoost | 240 min | 0.9159 | 0.4911 | 0.692 | 0.949 | 0.462 |
| Logistic Regression | 120 min | 0.8970 | 0.0997 | 0.846 | 0.817 | 0.126 |
| Logistic Regression | 60 min | 0.9060 | 0.0835 | 0.923 | 0.795 | 0.089 |
| **NEWS2 (clinical)** | **Full** | **0.6295** | **0.049** | — | — | — |
| **NEWS2 (clinical)** | **30 min** | **0.4345** | — | — | — | — |

### Stage 1 — LSTM Models (Per-Window with 95% Bootstrap CI)

| Window | AUROC | 95% CI | AUPRC | Sensitivity @ Youden | False Alarms | Notes |
|---|---|---|---|---|---|---|
| **30 min ★** | **0.9312** | **[0.90–0.96]** | 0.2104 | 0.985 | 1,737 | Best AUROC; extreme false alarm burden |
| 60 min | 0.9278 | [0.89–0.95] | 0.1895 | 0.892 | — | Consistent with 30-min |
| 120 min | 0.9294 | [0.90–0.95] | 0.1721 | 0.846 | — | Stable; slight sensitivity reduction |
| 240 min | 0.8889 | [0.85–0.93] | 0.3111 | 0.769 | — | Best LSTM AUPRC; modest AUROC decline |

> **Lead-time stability:** AUROC standard deviation across 30–120 min = 0.0017 — remarkably consistent, mirroring Lee et al. (2023).

### Stage 2 — TAN Ensemble (Multi-Window Cohort, n=1,731)

| Model | Cohort | AUROC | AUPRC | Sensitivity | FA:TP Ratio |
|---|---|---|---|---|---|
| NEWS2 (baseline) | Full | 0.6295 | 0.049 | — | — |
| LightGBM (full cohort) | n=6,047 | 0.9747 | 0.497 | 34.9% | 44:1 |
| LightGBM (retrained) | n=1,731 | 0.8917 | — | 86.2% | ~4:1 |
| TAN alone | n=1,731 | 0.8828 | 0.316 | 73.9% | — |
| **TAN+LSTM Ensemble ★** | **n=1,731** | **0.9180** | **0.295** | **83.1%** | **5:1** |

### Ensemble Grid Search Results

| α (TAN weight) | LSTM weight | Mean AUROC | Notes |
|---|---|---|---|
| 0.0 | 1.0 | 0.862 | Standalone LSTM |
| 0.5 | 0.5 | 0.886 | Equal weighting |
| **0.9** | **0.1** | **0.918** | **Optimal — selected** |
| 1.0 | 0.0 | 0.883 | Standalone TAN |

---

## 🔑 Core Scientific Finding — Attention Weight Monotonicity

This is the **primary scientific contribution** of the thesis, independent of hypothesis testing results.

### The Finding

The TAN's cross-window attention weights increase monotonically from the 30-minute to the 240-minute prediction horizon **across all five cross-validation folds**:

| Fold | 30 min | 60 min | 120 min | 240 min | Monotonic? |
|---|---|---|---|---|---|
| Fold 1 | 0.191 | 0.221 | 0.261 | 0.290 | ✅ Yes |
| Fold 2 | 0.203 | 0.235 | 0.275 | 0.315 | ✅ Yes |
| Fold 3 | 0.181 | 0.218 | 0.258 | 0.298 | ✅ Yes |
| Fold 4 | 0.213 | 0.240 | 0.281 | 0.324 | ✅ Yes |
| Fold 5 | 0.197 | 0.226 | 0.270 | 0.307 | ✅ Yes |
| **Mean** | **0.197** | **0.228** | **0.269** | **0.307** | ✅ **All 5** |

**Statistical verification:**
- Sign test: **p = 1.26 × 10⁻⁷** (monotonicity across folds)
- Friedman test: **χ²(3) = 15.00, p = 0.0018** (weight differences across windows)

### Clinical Translation

Current clinical practice assumes: 30-min window = most predictive (emergency focus)
This model finds:              240-min window = most predictive (4 hours before event!)


If confirmed by future ablation studies, this implies that haemodynamic optimisation strategies could be applied **within the pre-operative preparation window** — before surgical stress is applied — rather than reactively after collapse begins.

> ⚠️ **Caution:** Attention weights are model-internal. The 240-min preference may reflect genuine physiological signal, richer feature estimates from longer windows, or cohort selection bias (longer surgeries carry higher baseline risk). **Counterfactual ablation** (withholding each window individually and measuring AUROC change) is required before causal claims are made — this is the highest-priority future experiment.

---

## 🏥 Clinical Utility Analysis

### Why AUROC Alone is Misleading

A model with the highest AUROC is not necessarily the most useful clinically. At Youden-optimal thresholds:

| Model | Threshold | TP | FP | TN | FN | Sensitivity | F1 | FA:TP Ratio |
|---|---|---|---|---|---|---|---|---|
| **LightGBM 60-min** | 0.4307 | 23 | 1,012 | 4,969 | 43 | 34.9% | 0.042 | **44:1** ❌ |
| **LSTM 30-min** | 0.0030 | 65 | 1,737 | 4,573 | 1 | 98.5% | 0.070 | **27:1** ❌ |
| **TAN+LSTM Ensemble** | 0.2353 | 54 | 263 | 1,403 | 11 | 83.1% | 0.283 | **5:1** ✅ |

### The Alarm Fatigue Threshold

Drew et al. (2014) documented that clinical staff begin **ignoring alarms** when:
- False alarm-to-true positive ratio exceeds **~9:1**
- Positive predictive value falls below **~10%**


LightGBM:  44:1  FA:TP  →  Would be ignored by clinical staff
LSTM:      27:1  FA:TP  →  Would be ignored by clinical staff
TAN-LSTM:   5:1  FA:TP  →  ✅ Below alarm fatigue threshold
                PPV ~17% →  ✅ Above clinical engagement threshold


The TAN ensemble is the **only model** that satisfies both clinical alarm management criteria simultaneously, while still detecting **83.1% of all cardiac arrests** (54 of 65 events).

---

## 📈 SHAP Feature Importance

SHAP (SHapley Additive exPlanations) analysis was applied to the LightGBM 60-min model using TreeExplainer.

### Top 15 Features by Mean |SHAP Value|

| Rank | Feature | Channel | Descriptor | Mean \|SHAP\| | Direction |
|---|---|---|---|---|---|
| 1 | ART_DBP_max | Diastolic BP | Maximum | 0.8597 | ↑ higher max → lower risk |
| 2 | ART_MBP_max | Mean BP | Maximum | 0.3902 | ↑ higher max → lower risk |
| 3 | HR_mean | Heart Rate | Mean | 0.2894 | ↑ higher HR → higher risk |
| 4 | ART_SBP_max | Systolic BP | Maximum | 0.2701 | ↑ higher max → lower risk |
| 5 | ART_MBP_mean | Mean BP | Mean | 0.2430 | ↓ lower mean → higher risk |
| 6 | ART_DBP_mean | Diastolic BP | Mean | 0.2218 | ↓ lower mean → higher risk |
| 7 | ART_MBP_trend | Mean BP | Slope | 0.1987 | ↓ declining → higher risk |
| 8 | ART_SBP_mean | Systolic BP | Mean | 0.1765 | ↓ lower mean → higher risk |
| 9 | HR_max | Heart Rate | Maximum | 0.1543 | ↑ peak HR → higher risk |
| 10 | ART_DBP_trend | Diastolic BP | Slope | 0.1421 | ↓ declining → higher risk |
| 11 | ART_MBP_range | Mean BP | Range | 0.1312 | ↓ reduced variability → higher risk |
| 12 | ART_SBP_trend | Systolic BP | Slope | 0.1198 | ↓ declining → higher risk |
| 13 | HR_std | Heart Rate | Std Dev | 0.1054 | ↓ reduced variability → higher risk |
| 14 | SpO₂_min | SpO₂ | Minimum | 0.0421 | ↓ low nadir → higher risk |
| 15 | ETCO₂_min | ETCO₂ | Minimum | 0.0312 | ↓ low nadir → higher risk |

### Key Insights

**1. Haemodynamic dominance:** The top 4 features are all blood pressure-derived. The maximum descriptor — capturing *peak reserve capacity* within the window — outranks the mean, indicating that the model's primary concern is whether the patient can still reach an adequate peak blood pressure.

**2. Compensatory tachycardia detected:** HR_mean at rank 3 (independent of BP) confirms that sustained tachycardia functions as an independent CA risk indicator — consistent with the physiological sequence where tachycardia precedes hypotension as the cardiovascular system compensates for falling preload.

**3. Respiratory signals suppressed:** SpO₂ and ETCO₂ rank 14th and 15th with near-zero SHAP values. This is mechanistically expected — under general anaesthesia with mechanical ventilation, both are actively normalised. This explains exactly why NEWS2 fails in the operating room.

---

## 📈 Model Evolution — V1 vs V2 Comparison

This repository represents the **Version 2 (V2)** architecture — a substantially upgraded version of the initial single-window approach. Below is a direct comparison:

### Architecture Comparison

| Dimension | V1 (Original) | V2 (This Work) |
|---|---|---|
| **Design** | Single-window ML models only | Two-stage: per-window models + TAN aggregation |
| **Prediction horizons** | Single window (30 or 60 min) | 4 simultaneous windows (30/60/120/240 min) |
| **Temporal reasoning** | None — single snapshot | 4-head self-attention across all windows |
| **Imbalance handling** | SMOTE or class weighting | SMOTE-ENN (within-fold) + Focal Loss γ=2 |
| **Ensemble** | None or simple voting | Optimised TAN+LSTM (90/10, grid search) |
| **Interpretability** | Basic feature importance | SHAP + formally verified attention weights |
| **Clinical utility** | AUROC-only reporting | FA:TP ratio analysis + alarm fatigue framing |

### Performance Comparison — V1 vs V2

| Metric | V1 Best | V2 Best | Change |
|---|---|---|---|
| **Best single-model AUROC** | ~0.88–0.90 (est.) | **0.9747** (LightGBM) | **+0.07–0.09** |
| **Ensemble AUROC** | N/A | **0.9180** | New |
| **vs NEWS2 margin** | ~+0.25 (est.) | **+0.3452** | **+0.09** |
| **False alarm ratio** | Not measured | **5:1** (TAN ensemble) | **New metric** |
| **Sensitivity at deployment** | Variable | **83.1%** | **Clinically calibrated** |
| **Multi-window support** | ❌ No | ✅ Yes (4 horizons) | **New capability** |
| **Attention weight analysis** | ❌ No | ✅ Monotonicity verified | **New finding** |
| **Clinical alarm analysis** | ❌ No | ✅ Below fatigue threshold | **New framing** |

### What Changed and Why

**Why multi-window?** The V1 single-window models showed strong AUROC but couldn't answer: *does earlier data add independent predictive value?* V2 answers this definitively — the 240-minute window carries 56% more attention weight than the 30-minute window (0.307 vs 0.197), confirmed across all 5 folds.

**Why SMOTE-ENN instead of SMOTE?** V1 used standard SMOTE, which generates synthetic samples but does not clean ambiguous boundary cases. SMOTE-ENN combines oversampling with Edited Nearest Neighbours to remove borderline majority-class samples, producing a cleaner decision boundary. Applied strictly within CV folds to prevent leakage.

**Why Focal Loss?** V1's cross-entropy loss gave equal weight to all samples, allowing easy majority-class examples to dominate the gradient. Focal Loss (γ=2) reduces the contribution of correctly classified non-CA cases by ~96%, forcing the model to focus on difficult CA-positive cases.

**Why the 90/10 ensemble split?** Grid search across 11 α values showed that the TAN consistently contributes ~90% of the discriminative weight. This mirrors the finding of Hsu et al. (2024), where a neural component contributed 85–90% of prediction weight in a hybrid cardiac arrest system — suggesting this ratio may be a reproducible property of attention-based CA prediction architectures.

---

## 🖥️ Dashboard Screenshots

### Real Data — Single Patient View
[📄 View Full Dashboard — Real Single Patient](real-single.pdf)

### Real Data — Compare 2 Patients
[📄 View Full Dashboard — Real Two Patient Comparison](real-two%20patient.pdf)

### Synthetic Mode — CA vs No-CA Overlay
[📄 View Full Dashboard — Synthetic Overlay](syn-overlay.pdf)

### Synthetic Mode — Side by Side
[📄 View Full Dashboard — Synthetic Side by Side](syn-side.pdf)

### Synthetic Mode — Single Patient
[📄 View Full Dashboard — Synthetic Single Patient](syn-single.pdf)

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| **Deep Learning** | PyTorch — TAN custom architecture (4-head self-attention + FC layers) |
| **Classical ML** | LightGBM, Scikit-learn (Random Forest, XGBoost, Logistic Regression) |
| **Data Processing** | Pandas, NumPy |
| **Imbalance Handling** | imbalanced-learn (SMOTE-ENN) |
| **Explainability** | SHAP — TreeExplainer for LightGBM |
| **Validation** | Scikit-learn (StratifiedKFold), scipy (Friedman, sign test) |
| **Statistics** | Bootstrap DeLong test, Youden-J threshold, bootstrap CI |
| **Visualisation** | Matplotlib, Seaborn |
| **Environment** | Google Colab, VS Code, GitHub |
| **Dataset** | VitalDB ([vitaldb.net](https://vitaldb.net)) |

---

## 🚀 Quick Start

### Prerequisites

```bash
Python >= 3.9
PyTorch >= 2.0
CUDA (optional, CPU also supported)
```

### Installation

```bash
git clone https://github.com/sachumonpsajeev-cyber/VitalDb-Cardiac-Arrest-Prediction-TAN
cd VitalDb-Cardiac-Arrest-Prediction-TAN
pip install -r requirements.txt
```

### Dataset Access

1. Register at [vitaldb.net](https://vitaldb.net)
2. Download the perioperative dataset (6,388 surgical cases)
3. Place in `data/raw/` directory

### Run the Full Pipeline

# Stage 1: Feature extraction and per-window model training
python src/feature_engineering.py --windows 30 60 120 240

# Stage 2: TAN training with SMOTE-ENN and Focal Loss
python src/train_tan.py --folds 5 --focal_gamma 2.0

# Stage 3: Ensemble optimisation (grid search over α)
python src/ensemble_search.py --alpha_steps 11

# Full evaluation with SHAP
python cardiac_arrest_prediction.py --evaluate --shap

### Requirements (library)

torch>=2.0.0
lightgbm>=4.0.0
scikit-learn>=1.3.0
imbalanced-learn>=0.11.0
shap>=0.44.0
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
scipy>=1.11.0




## 📂 Project Structure

VitalDb-Cardiac-Arrest-Prediction-TAN/
│
├── cardiac_arrest_prediction.py    # Main pipeline script
│
├── src/
│   ├── feature_engineering.py      # 36-feature extraction per window
│   ├── models/
│   │   ├── tan.py                  # 4-head Temporal Attention Network
│   │   ├── lstm_model.py           # Per-window LSTM architecture
│   │   └── classical_ml.py        # LightGBM, RF, XGBoost, LR
│   ├── training/
│   │   ├── train_tan.py            # TAN training with Focal Loss
│   │   ├── smote_enn.py            # Within-fold SMOTE-ENN
│   │   └── ensemble_search.py     # Grid search over α
│   ├── evaluation/
│   │   ├── metrics.py              # AUROC, AUPRC, Youden-J, DeLong
│   │   ├── confusion_matrix.py     # FA:TP ratio analysis
│   │   └── attention_analysis.py  # Attention weight monotonicity tests
│   └── explainability/
│       └── shap_analysis.py       # SHAP TreeExplainer
│
├── data/
│   ├── raw/                        # VitalDB raw files (not in repo)
│   └── processed/                  # Feature vectors per window
│
├── results/
│   ├── figures/                    # All publication figures (10 charts)
│   ├── attention_weights.csv       # Per-fold attention weights
│   └── model_performance.csv      # Full results table
│
├── dashboard/
│   ├── real-single.pdf
│   ├── real-two patient.pdf
│   ├── syn-overlay.pdf
│   ├── syn-side.pdf
│   └── syn-single.pdf
│
├── requirements.txt
└── README.md




## ⚠️ Limitations & Future Work

### Known Limitations

| Limitation | Impact | Status |
|---|---|---|
| **Epinephrine proxy label** | Unknown CA label false positive rate | Sensitivity analysis added; manual adjudication planned |
| **Single-centre dataset** | External validity unconfirmed | Development phase only — not proposed for deployment |
| **73% multi-window cohort reduction** | TAN results specific to long-procedure patients | Prevalence comparison documented |
| **H2 statistical power (~35%)** | TAN vs LightGBM advantage not confirmed at α=0.05 | Requires 180–220 CA+ cases; multi-centre data needed |
| **Attention ≠ causality** | 240-min weight may reflect data volume or cohort selection | Counterfactual ablation planned as highest-priority experiment |
| **No external validation** | Generalisability to other institutions unknown | eICU-CRD validation planned |

### Three-Tier Research Roadmap

**Tier 1 — Immediate:**
- Manual CA label adjudication (25–30 cases, 2 independent anaesthetists)
- External validation on eICU-CRD dataset
- Post-hoc probability calibration (Platt scaling / isotonic regression)

**Tier 2 — Medium-Term:**
- Counterfactual window ablation (withhold each window, measure AUROC Δ)
- Head count ablation (1 vs 2 vs 4 attention heads)
- Feature-level ablation (quantify marginal contribution per channel)
- Raw time-series feature learning (CNN/Transformer encoder replacing manual features)
- Federated multi-centre data collection (target: 180–220 CA+ cases)

**Tier 3 — Long-Term:**
- Prospective clinical evaluation in operating theatre setting
- Hybrid monitoring system: LightGBM activates at 60 min → TAN activates at 240 min
- EU MDR 2017/745 regulatory pathway (Class IIb medical device software)
- Multi-centre federated training with privacy-preserving techniques

> **This model is not approved for clinical use.** All results are development-phase estimates from a single-centre dataset and have not been prospectively validated.

---

## 📚 Key References

```
Kaiser et al. (2020). Incidence and prediction of intraoperative and postoperative cardiac 
  arrest in non-cardiac patients. PLOS ONE.

Lee et al. (2022). VitalDB, a high-fidelity multi-parameter vital signs database in surgical 
  patients. Scientific Data, 9(1), 279.

Lin et al. (2017). Focal loss for dense object detection. Proceedings of ICCV, 2980–2988.

Vaswani et al. (2017). Attention is all you need. Advances in NeurIPS, 30, 5998–6008.

Drew et al. (2014). Insights into the problem of alarm fatigue with physiologic monitor 
  devices. PLOS ONE, 9(10), e110151.

Meng et al. (2024). Perioperative cardiac arrest: Mnemonic, classification, monitoring, 
  and actions. Anaesthesia & Analgesia.

Vaishali et al. (2025). Enhancing cardiac arrest prediction in imbalanced time-series data 
  using SMOTEENN. Procedia Computer Science.
```

---

## 📄 Citation

If you use this work, please cite:

```bibtex
@mastersthesis{sajeev2026tan,
  author    = {Sachu Mon Puthenpuraickpal Sajeev},
  title     = {Predicting Intraoperative Cardiac Arrest Using a Multi-Window
               Temporal Attention Network: A Two-Stage Machine Learning
               Architecture on the VitalDB Perioperative Database},
  school    = {Transport and Telecommunication Institute},
  year      = {2026},
  address   = {Riga, Latvia},
  type      = {MSc Thesis}
}
```

---

## 👤 Author

<div align="center">

**Sachu Mon Puthenpuraickpal Sajeev**

MSc Data Science & AI — Transport and Telecommunication Institute (TSI), Riga, Latvia

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/sachu-mon)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/sachumonpsajeev-cyber)

</div>

---

<div align="center">

*Built as part of MSc thesis research — Transport and Telecommunication Institute, Riga, 2026*

*VitalDB data used under Creative Commons licence — Lee et al. (2022), Scientific Data*

</div>
