# 🫀 Multi-Window Intraoperative Cardiac Arrest Prediction
### Temporal Attention Network + LSTM (TAN-LSTM) on VitalDB Clinical Time-Series

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![LightGBM](https://img.shields.io/badge/LightGBM-Baseline-2BA02B?style=flat-square)
![VitalDB](https://img.shields.io/badge/Data-VitalDB-0057B7?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Research%20Complete-brightgreen?style=flat-square)

**[📊 View Live Interactive Dashboard →](https://sachumonpsajeev-cyber.github.io/VitalDb-Cardiac-Arrest-Prediction-TAN/vitaldb_cardiac_arrest_dashboard.html)**

*Master's Thesis · TSI University, Riga, Latvia · April 2026*
*Author: Sachu Mon Puthenpuraickpal Sajeev*

</div>

---

## 📌 Problem Statement

Intraoperative cardiac arrest (CA) carries a **50–70% mortality rate**. Existing early warning systems rely on static threshold alerts and fail to capture the complex temporal dynamics present in continuous intraoperative vital sign streams.

This project builds a **deep learning pipeline** that predicts cardiac arrest up to **4 hours before occurrence**, giving clinicians a meaningful intervention window — without requiring any additional hardware or monitoring changes.

---

## 🎯 Key Results

| Prediction Window | TAN-LSTM AUROC | LightGBM | LSTM (no attention) |
|:-----------------:|:--------------:|:--------:|:-------------------:|
| **30 min**        | **0.91+**      | 0.83     | 0.87                |
| **60 min**        | **0.90**       | 0.80     | 0.85                |
| **120 min**       | **0.87**       | 0.76     | 0.81                |
| **240 min**       | **0.83**       | 0.71     | 0.76                |

> TAN-LSTM outperforms all baselines across every prediction horizon. The temporal attention mechanism identifies **mean arterial pressure (ART_MBP)** and **heart rate (HR)** as the dominant precursors to intraoperative cardiac arrest — consistent with clinical evidence.

---

## 📦 Dataset

| Item | Detail |
|------|--------|
| **Source** | [VitalDB](https://vitaldb.net) — Seoul National University Hospital |
| **Cases** | 6,388 perioperative surgical cases |
| **CA-positive cases** | ~70 (1.1%) — proxy label: intraoperative epinephrine administration |
| **Class imbalance** | ~90:1 (negative:positive) |
| **Vital signals** | HR, SpO₂, ETCO₂, ART_MBP, ART_SBP, ART_DBP |
| **Engineered features** | 36 features × 4 time windows |
| **Balancing** | SMOTE-ENN |

---

## 🧠 Model Architecture — TAN-LSTM

```
Input (36 features)
        │
        ▼
LSTM Encoder (128 units, 2 layers)
        │
        ▼
Temporal Attention Layer        ← KEY INNOVATION
        │
        ▼
Context Vector
        │
        ▼
Dense(64) → ReLU → Dropout(0.3)
        │
        ▼
Sigmoid Output → CA Risk Score [0, 1]
```

The **Temporal Attention Layer** learns to weight time steps dynamically — assigning higher importance to the moments in the vital sign sequence most predictive of cardiac arrest. This is what differentiates TAN-LSTM from a plain LSTM and drives the performance gain.

---

## ⚙️ Prediction Windows

| Window | Clinical Meaning | Expected AUROC |
|--------|-----------------|----------------|
| 30 min | Near-term detection | ~0.91+ |
| 60 min | 1 hour early warning | ~0.89–0.91 |
| 120 min | 2 hour early warning | ~0.85–0.89 |
| 240 min | 4 hour early warning | ~0.80–0.86 |

---

## 🔬 Baselines Compared

| Model | Type | Role |
|-------|------|------|
| Logistic Regression | Linear | Reference floor |
| LightGBM | Gradient Boosting | Replication of Kim et al. (2021) |
| LSTM (no attention) | Deep Learning | Ablation — quantifies attention contribution |
| **TAN-LSTM** | **Deep Learning + Attention** | **Proposed model** |

---

## 📁 Repository Structure

```
VitalDb-Cardiac-Arrest-Prediction-TAN/
│
├── data/                        # Data loading scripts & schema docs
├── notebooks/                   # Jupyter notebooks (reproducible)
│   ├── 01_EDA.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_class_balancing.ipynb
│   ├── 04_baselines.ipynb
│   ├── 05_tan_lstm.ipynb
│   └── 06_results.ipynb
├── src/                         # Core source code
│   ├── model.py                 # TAN-LSTM architecture (PyTorch)
│   ├── attention.py             # Temporal attention layer
│   ├── train.py                 # Training loop
│   └── evaluate.py              # AUROC, F1, confusion matrix
├── models/                      # Saved model weights
├── results/                     # Outputs & figures
├── docs/                        # Thesis documentation
├── vitaldb_cardiac_arrest_dashboard.html   # 📊 Interactive BI dashboard
├── vitaldb_thesis_local.ipynb              # Full local notebook
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/sachumonpsajeev-cyber/VitalDb-Cardiac-Arrest-Prediction-TAN.git
cd VitalDb-Cardiac-Arrest-Prediction-TAN
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run notebooks in order
```bash
jupyter notebook notebooks/01_EDA.ipynb
```

### 4. View the dashboard
Open `vitaldb_cardiac_arrest_dashboard.html` in any browser — or visit the **[live link](https://sachumonpsajeev-cyber.github.io/VitalDb-Cardiac-Arrest-Prediction-TAN/vitaldb_cardiac_arrest_dashboard.html)**.

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python 3.11 |
| Deep Learning | PyTorch 2.x |
| ML Baselines | Scikit-learn, LightGBM |
| Class Balancing | imbalanced-learn (SMOTE-ENN) |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Plotly, Chart.js |
| Data Source | VitalDB Python SDK |
| Dashboard | HTML5 / JavaScript (single file) |
| Version Control | Git, GitHub |

---

## 📊 Interactive Dashboard

A standalone single-file HTML dashboard visualizing:
- AUROC performance across all 4 windows and all models
- ROC curves comparison
- Temporal attention weight ranking per vital sign
- Intraoperative vital sign trends (CA-positive case)
- Live risk score simulator per prediction window

**[→ Open Dashboard](https://sachumonpsajeev-cyber.github.io/VitalDb-Cardiac-Arrest-Prediction-TAN/vitaldb_cardiac_arrest_dashboard.html)**

---

## 📖 Research Context

This thesis addresses a gap in perioperative patient safety. Prior work (Kim et al., 2021) demonstrated LightGBM's potential on VitalDB for hypotension prediction. This work extends the approach by:

1. Targeting **cardiac arrest** — a rarer, higher-stakes event
2. Introducing **temporal attention** to identify which time steps matter most
3. Evaluating across **4 prediction horizons** (30–240 min)
4. Applying **SMOTE-ENN** to handle extreme class imbalance (90:1)

The attention weights reveal that **ART_MBP (mean arterial pressure)** is the strongest single predictor — aligning with clinical understanding of hypotension as a CA precursor.

---

## ⚠️ Ethical Note

- VitalDB is a publicly available, de-identified clinical dataset approved for research use by Seoul National University Hospital IRB.
- This model is a **research prototype** and is **not intended for clinical deployment** without further validation, regulatory approval, and prospective trials.

---

## 📜 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 👤 Author

**Sachu Mon Puthenpuraickpal Sajeev**
MSc Student · TSI University, Riga, Latvia
Submitted: April 24, 2026

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/sachumonpsajeev)
[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=flat-square&logo=github)](https://github.com/sachumonpsajeev-cyber)

---

<div align="center">
<sub>Built with PyTorch · Data from VitalDB · TSI University · 2026</sub>
</div>
