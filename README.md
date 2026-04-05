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

Target benchmark: AUROC > 0.91 (based on Lee et al., 2024)
Achieved: Ensemble AUROC 0.9180 (vs. baseline LightGBM: 0.6295)

---

## 📊 Results

| Prediction Window | Model    | AUROC  | Baseline AUROC | Improvement |
|-------------------|----------|--------|----------------|-------------|
| 30 min            | TAN-LSTM | 0.918+ | 0.630          | +0.288      |
| 60 min            | TAN-LSTM | 0.918+ | 0.630          | +0.288      |
| 120 min           | TAN-LSTM | 0.918+ | 0.630          | +0.288      |
| 240 min           | TAN-LSTM | 0.918+ | 0.630          | +0.288      |
| Ensemble          | TAN-LSTM | 0.9180 | 0.6295         | +0.2885     |

---

## 🏗️ Architecture

Step 1: VitalDB Clinical Data (6,388 cases)
Step 2: Feature Engineering — 36 statistical features × 6 vital signals (HR, SpO2, ETCO2, ART_MBP, ART_SBP, ART_DBP)
Step 3: Class Imbalance Handling — SMOTE-ENN (90:1 ratio)
Step 4: Temporal Attention Network — 4-Head Self-Attention → captures temporal dependencies
Step 5: LSTM Layer → sequential pattern learning
Step 6: Stratified 5-Fold Cross-Validation
Step 7: Prediction Output → Cardiac Arrest Risk Score

---

## 📁 Dataset

| Property           | Details                                                      |
|--------------------|--------------------------------------------------------------|
| Source             | VitalDB — Seoul National University Hospital                 |
| Cases              | 6,388 perioperative surgical cases                           |
| Vital Signals      | HR, SpO2, ETCO2, ART_MBP, ART_SBP, ART_DBP                  |
| Features Extracted | 36 statistical features (mean, std, min, max, range, slope)  |
| Class Imbalance    | 90:1 (non-arrest : arrest)                                   |
| Prediction Windows | 30 / 60 / 120 / 240 minutes before event                     |

---

## 🛠️ Tech Stack

- Deep Learning: PyTorch (TAN-LSTM custom architecture)
- ML Baselines: LightGBM, standard LSTM, Logistic Regression
- Data: Pandas, NumPy, Scikit-learn
- Imbalance Handling: SMOTE-ENN (imbalanced-learn)
- Validation: Stratified 5-Fold Cross-Validation
- Environment: Google Colab, VS Code, GitHub

---

## 🚀 Quick Start

git clone https://github.com/sachumonpsajeev-cyber/VitalDb-Cardiac-Arrest-Prediction-TAN
cd VitalDb-Cardiac-Arrest-Prediction-TAN
pip install -r requirements.txt
python cardiac_arrest_prediction.py

---

## 📌 Key Findings

- TAN-LSTM outperforms LightGBM baseline by +0.29 AUROC on the same clinical cohort
- 4-head self-attention effectively captures temporal dependencies in vital sign sequences
- SMOTE-ENN is more effective than standard SMOTE for severe clinical class imbalance
- Multi-window approach (4 prediction horizons) improves clinical utility vs. single-window models
- Ensemble of window-specific models further boosts overall prediction stability

---

## 👤 Author

Sachu Mon Puthenpuraickpal Sajeev
MSc Data Science & AI — TSI University, Riga, Latvia
LinkedIn: https://linkedin.com/in/sachu-mon
GitHub: https://github.com/sachumonpsajeev-cyber
whatsapp: +371-22447242
