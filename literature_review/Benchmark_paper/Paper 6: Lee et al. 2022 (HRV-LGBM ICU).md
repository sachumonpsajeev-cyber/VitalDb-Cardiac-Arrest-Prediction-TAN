# Paper 6: Lee et al. 2022 (HRV-LGBM ICU)

> 🟡 BENCHMARK PAPER — LightGBM-based real-time cardiac arrest prediction using heart rate variability features in ICU

---

## Metadata

| Field | Details |
|---|---|
| Title | Real-Time Machine Learning-Based Cardiac Arrest Prediction Using Heart Rate Variability |
| Authors | Lee et al. |
| Journal | Not specified |
| Year | 2022 |
| Volume | N/A |
| DOI | N/A |
| Link | N/A |
| Read Date | Feb 2026 |
| Category | 🟡 |
| Thesis Relevance | High — Strong ML benchmark (AUROC 0.881) using HRV features; same hospital dataset as Paper 6 |

---

## 1. Problem Addressed

- Need for **real-time cardiac arrest (CA) prediction** in ICU settings  
- Traditional models:
  - Do not leverage **heart rate variability (HRV)** effectively  
  - Lack **continuous real-time monitoring capability**  
- Limited understanding of how **HRV-derived features** contribute to CA prediction  

---

## 2. Dataset Used

| Field | Details |
|---|---|
| Dataset | Hospital ICU dataset (same institution as Paper 6) |
| Setting | ICU |
| Population | Not specified |
| Time period | Not specified |
| Task | Cardiac arrest prediction |
| Class imbalance | Not specified |

Optional:
- Feature types (HRV features derived from ECG signals)

---

## 3. Methodology

### Model: LightGBM (LGBM)

- Gradient boosting model for **tabular time-series features**

- Architecture overview:
  - HRV feature extraction from ECG  
  - Feature engineering pipeline  
  - LightGBM classifier  

- Key components:
  - Uses **HRV metrics** (time-domain and frequency-domain features)  
  - Optimised for **real-time prediction**  
  - Handles non-linear relationships effectively  

- Input features:
  - HRV-derived features from ECG signals  

- Prediction window:
  - Real-time prediction (exact horizon not specified)

- Training strategy:
  - Standard supervised learning with engineered features  

### Baselines (if applicable)

- Compared with traditional statistical and ML approaches  

---

## 4. Results

| Model | AUROC | Other Metrics |
|---|---|---|
| LGBM (HRV-based) | **0.881** | N/A |

### Key Findings

- Achieves strong performance with **AUROC 0.881**  
- Demonstrates effectiveness of **HRV features for CA prediction**  
- Enables **real-time prediction capability** in ICU  
- Shows that engineered physiological features can perform well with ML models  

---

## 5. Limitations

- Relies on **feature engineering (HRV extraction)** rather than end-to-end learning  
- No use of **deep learning or attention mechanisms**  
- Dataset limited to **single institution**  
- Prediction window not clearly defined  
- Limited interpretability beyond feature importance  

---

## 6. Relevance to This Thesis

| Aspect | Paper | This Thesis |
|---|---|---|
| Model | LightGBM (ML) | TAN (Deep learning, attention-based) |
| Data | HRV features (engineered) | Raw + high-resolution VitalDB signals |
| Setting | ICU | Intraoperative OR |
| Task | Cardiac arrest prediction | Cardiac arrest prediction |

### Key Contributions to Thesis

- Provides **strong ML baseline (AUROC 0.881)**  
- Highlights importance of **HRV features for physiological prediction**  
- Demonstrates feasibility of **real-time CA prediction systems**  
- Same institutional dataset context improves **comparability (Paper 6 link)**  

### Research Gap Addressed

- No **end-to-end deep learning model**  
- No **temporal attention or sequence modeling**  
- Relies on **manual feature engineering**  
- No use of **high-resolution multi-parameter data (VitalDB advantage)**  
- Limited generalisation (single-center dataset)  

---

## 7. Position in Literature

| Paper | Model | Setting | Contribution |
|---|---|---|---|
| Soudan et al. 2022 | Random Forest | Hospital | Traditional ML baseline |
| Lee et al. 2022 | LGBM | ICU | HRV-based real-time ML prediction |
| Cho et al. 2020 | LSTM | ICU | Deep learning temporal baseline |
| Li et al. 2026 | TrGRU | ICU | State-of-the-art CA prediction |

---

## 8. Citation (APA)

Lee, et al. (2022). Real-time machine learning-based cardiac arrest prediction using heart rate variability.

---

## 9. Summary (For Thesis Writing)

Lee et al. (2022) proposed a LightGBM-based model using heart rate variability features for real-time cardiac arrest prediction in ICU settings, achieving an AUROC of 0.881. The study demonstrates the effectiveness of engineered physiological features but is limited by the absence of deep learning and temporal attention mechanisms, motivating the need for end-to-end attention-based models in this thesis.

---

*Notes by: Sachu Mon Puthenpuraickpal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
