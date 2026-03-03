# Multi-Window Intraoperative Cardiac Arrest Prediction
### Using Temporal Attention Networks on VitalDB Clinical Time-Series Data

**Student:** Sachu Mon Puthenpuraickpal Sajeev  
**University:** TSI University, Riga, Latvia  
**Submission:** April 24, 2026

---

## Problem Statement

Intraoperative cardiac arrest carries 50–70% mortality. Current early 
warning systems use static thresholds and miss the temporal patterns 
in continuous vital sign data. This thesis builds a deep learning model 
to predict cardiac arrest before it happens — giving clinicians time to intervene.

---

## Dataset

| Item | Detail |
|------|--------|
| Source | VitalDB (Seoul National University Hospital) |
| Cases | 6,388 perioperative surgical cases |
| CA cases | ~70 (1.1%) — proxy: intraoperative epinephrine |
| Class ratio | ~90:1 |
| Signals | HR, SpO2, ETCO2, ART_MBP, ART_SBP, ART_DBP |

---

## Model Architecture — TAN-LSTM
```
Input (36 features) → LSTM Encoder (128 units, 2 layers)
→ Temporal Attention Layer → Context Vector
→ Dense(64) → ReLU → Dropout → Sigmoid Output
```

---

## Prediction Windows

| Window | Clinical Meaning | Expected AUROC |
|--------|-----------------|----------------|
| 30 min | Near-term detection | ~0.91+ |
| 60 min | 1 hour early warning | ~0.89–0.91 |
| 120 min | 2 hour early warning | ~0.85–0.89 |
| 240 min | 4 hour early warning | ~0.80–0.86 |

---

## Baselines

| Model | Type | Role |
|-------|------|------|
| Logistic Regression | Linear | Reference floor |
| LightGBM | Gradient Boost | Direct baseline (Kim et al. 2021) |
| LSTM | Deep Learning | Ablation — no attention |
| **TAN-LSTM** | **Deep Learning + Attention** | **Proposed model** |

---

## Progress

- [x] Section 1 — Data Exploration & Labels
- [x] Section 2 — Feature Engineering (36 features × 4 windows)
- [ ] Section 3 — Class Balancing (SMOTE-ENN)
- [ ] Section 4 — Baseline Models
- [ ] Section 5 — TAN-LSTM Ablation Study
- [ ] Section 6 — Results & Comparison
- [ ] Section 7 — Model Export

---

## Tech Stack

Python · Pandas · NumPy · PyTorch · Scikit-learn · LightGBM · imbalanced-learn · Kaggle · GitHub

LinkedIn
□ Headline updated
□ About section updated
□ Thesis added as Featured project
□ Skills added
□ Open to Work turned ON

GitHub
□ Profile README created (sachumonpsajeev-cyber repo)
□ Thesis repo README updated
□ Thesis repo pinned on profile
