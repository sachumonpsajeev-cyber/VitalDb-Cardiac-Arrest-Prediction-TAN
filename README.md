# 🫀 Intraoperative Cardiac Arrest Prediction — TAN-LSTM

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Clinical AI](https://img.shields.io/badge/Clinical%20AI-Healthcare-brightgreen)
![AUROC](https://img.shields.io/badge/AUROC-0.9180-blue)
![Status](https://img.shields.io/badge/Status-MSc%20Thesis%20(In%20Progress)-orange)

> MSc Thesis Project — Multi-window intraoperative cardiac arrest prediction using Temporal Attention Networks on clinical time-series data from VitalDB.

---

## 🎯 Project Goal

Predict cardiac arrest 30, 60, 120, and 240 minutes before the event during surgery, using real-time vital sign signals — enabling clinical teams to intervene earlier.

- **Target benchmark:** AUROC > 0.91 (based on Lee et al., 2024)
- **Achieved:** Ensemble AUROC **0.9180** (vs. baseline NEWS2: 0.6295)

---

## 📊 Results

| Prediction Window | Model | AUROC | Baseline (NEWS2) | Improvement |
|---|---|---|---|---|
| 30 min | LSTM | 0.9312 | 0.6295 | +0.3017 |
| 60 min | LightGBM | 0.9747 | 0.6295 | +0.3452 |
| 120 min | TAN-LSTM | 0.918+ | 0.6295 | +0.288 |
| 240 min | TAN-LSTM | 0.918+ | 0.6295 | +0.288 |
| Ensemble | TAN-LSTM | 0.9180 | 0.6295 | +0.2885 |

---

## 🏗️ Architecture

**Stage 1 — Per-Window Models:**
- VitalDB Clinical Data (6,388 cases)
- Feature Engineering: 36 statistical features × 6 vital signals (HR, SpO₂, ETCO₂, ART_MBP, ART_SBP, ART_DBP)
- Class Imbalance Handling: SMOTE-ENN (90:1 ratio)
- Models: LSTM, LightGBM, Random Forest, XGBoost, Logistic Regression
- Stratified 5-Fold Cross-Validation per window (30 / 60 / 120 / 240 min)

**Stage 2 — TAN Aggregation:**
- 4-Head Self-Attention Network (cross-window)
- Learns temporal importance across all 4 prediction horizons
- Hybrid Ensemble: LSTM 10% + TAN 90% (grid search optimized)
- Output: Cardiac Arrest Risk Score

---

## 📁 Dataset

| Property | Details |
|---|---|
| Source | VitalDB — Seoul National University Hospital |
| Cases | 6,388 perioperative surgical cases |
| CA Patients | 65 confirmed cardiac arrest cases |
| Vital Signals | HR, SpO₂, ETCO₂, ART_MBP, ART_SBP, ART_DBP |
| Features Extracted | 36 statistical features (mean, std, min, max, range, slope) |
| Class Imbalance | 90:1 (non-arrest : arrest) |
| Prediction Windows | 30 / 60 / 120 / 240 minutes before event |

---

## 🛠️ Tech Stack

- **Deep Learning:** PyTorch (TAN-LSTM custom architecture)
- **ML Baselines:** LightGBM, Random Forest, XGBoost, Logistic Regression
- **Data:** Pandas, NumPy, Scikit-learn
- **Imbalance Handling:** SMOTE-ENN (imbalanced-learn)
- **Explainability:** SHAP (SHapley Additive exPlanations)
- **Validation:** Stratified 5-Fold Cross-Validation
- **Environment:** Google Colab, VS Code, GitHub

---

## 🚀 Quick Start

```bash
git clone https://github.com/sachumonpsajeev-cyber/VitalDb-Cardiac-Arrest-Prediction-TAN
cd VitalDb-Cardiac-Arrest-Prediction-TAN
pip install -r requirements.txt
python cardiac_arrest_prediction.py
```

---

## 📌 Key Findings

- TAN-LSTM achieves **AUROC 0.9180** vs NEWS2 baseline of 0.6295 (+0.2885)
- Cross-window attention weights increase monotonically (0.197 → 0.228 → 0.269 → 0.307), proving physiological deterioration is detectable earliest at 240 minutes before arrest
- TAN produces **66% fewer false alarms** than standard LSTM
- SMOTE-ENN outperforms standard SMOTE for severe clinical class imbalance (90:1)
- NEWS2 drops to AUROC 0.4345 in intraoperative setting — below random prediction
- Multi-window approach (4 prediction horizons) improves clinical utility vs. single-window models

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

## 👤 Author

**Sachu Mon Puthenpuraickpal Sajeev**
MSc Data Science & AI — TSI University, Riga, Latvia
LinkedIn: https://linkedin.com/in/sachu-mon
GitHub: https://github.com/sachumonpsajeev-cyber
