# Paper 8: Chae et al. 2021 — Prediction of In-Hospital Cardiac Arrest Using Shallow and Deep Learning

**Citation:** Chae, M., Han, S., Gil, H., Cho, N., & Lee, H. (2021). Prediction of in-hospital cardiac arrest using shallow and deep learning. *Diagnostics, 11*(7), 1255. https://doi.org/10.3390/diagnostics11071255
**Link:** https://www.mdpi.com/2075-4418/11/7/1255
**Date Read:** Feb 26, 2026

> 🟡 **BENCHMARK PAPER** — Traditional ML + deep learning baseline for cardiac arrest prediction — SMOTE ratio evaluation — LR outperforms MEWS/NEWS — Korean hospital setting

---

## 1. Problem They Solved

- Traditional early warning systems (NEWS, MEWS) have low sensitivity and high false positive rates — not reliable for CA prediction
- No systematic comparison existed of shallow (DT, RF, LR) vs deep learning (LSTM, GRU, LSTM-GRU hybrid) for CA prediction
- Class imbalance in CA datasets was unaddressed — no prior study evaluated the effect of SMOTE ratio on model performance
- Clinical teams lacked advance warning tools using only routinely measured vital signs and basic lab data

---

## 2. Dataset Used

| Field | Details |
|---|---|
| **Hospital** | Soonchunhyang University Cheonan Hospital, South Korea |
| **Study Period** | January 2016 – June 2019 |
| **Total Patients** | 83,543 |
| **CA Cases** | 1,154 in-hospital cardiac arrests |
| **Features** | 13 input variables |
| **Input Variables** | Age, Sex, DBP, SBP, Body Temperature, Respiratory Rate, Blood Pressure, Albumin, Creatinine, Hb (+ presence flags) |
| **Data per Patient** | 72 hours of time-series data, sliced into 8-hour segments |
| **Setting** | General hospital ward — not ICU, not perioperative OR |

---

## 3. Methodology

- Evaluated **6 models:** Decision Tree, Random Forest, Logistic Regression, LSTM, GRU, LSTM-GRU Hybrid
- **SMOTE** applied to training data only — evaluated 8 different ratios (1:1 down to 1:0.025)
- Best F1 at ratio **1:0.07** — best PPV at ratio **1:0.05** — final ratio used: 1:0.05
- Stratified K-fold cross-validation for shallow models (k=4, 5, or 10)
- 72-hour window before CA extracted; measurement interval standardised to 1 hour
- Missing values replaced with last measured value

---

## 4. Results

| Algorithm | PPV | Sensitivity | Specificity | F1 Score |
|---|---|---|---|---|
| Decision Tree | 46.80% | 28.99% | 99.54% | 35.80% |
| **Random Forest** | **98.22%** | 24.25% | **100.00%** | 38.94% |
| Logistic Regression | 5.14% | **76.33%** | 80.35% | 9.64% |
| LSTM | 38.37% | 32.66% | 99.27% | 35.28% |
| GRU | 34.59% | 34.59% | 99.09% | 34.69% |
| LSTM-GRU Hybrid | 30.53% | 38.65% | 98.77% | 34.12% |

- RF achieved near-perfect PPV (98.22%) and perfect specificity — almost zero false alarms
- LR achieved highest sensitivity (76.33%) — best at catching CA but many false alarms
- All proposed models outperformed traditional EWS (MEWS, NEWS) in PPV and/or sensitivity
- ⚠️ AUROC not reported — PPV and sensitivity are the primary metrics used throughout

---

## 5. Limitations

- **No AUROC reported** — cannot directly compare to Kwon (0.850), FAST-PACE (0.896), HRV-LGBM (0.881)
- **Lab data required** — Albumin, Creatinine, Hb not available in VitalDB intraoperative setting
- **General ward setting only** — not ICU, not perioperative OR
- **Single-centre** — Soonchunhyang University Cheonan Hospital only
- **Hourly resolution** — much lower than VitalDB's continuous OR monitoring
- **SMOTE only** — no SMOTE-ENN, ADASYN, or cost-sensitive learning comparison

---

## 6. Relevance to My Project

- **Vital signs + minimal lab data sufficient for CA prediction** — supports your 6-feature VitalDB approach; your model achieves this with purely haemodynamic signals, no lab data required
- **RF achieves 98.22% PPV** — strongest traditional ML baseline reference; your LGBM should be compared against this RF performance level
- **SMOTE ratio evaluation** — their systematic test of 8 ratios directly informs your SMOTE-ENN tuning; best results at 1:0.07 is a practical starting reference point
- **LSTM, GRU, hybrid all underperform RF and LR** — supports the argument that standard deep learning alone is insufficient; TAN's attention mechanism is the justified upgrade
- **LR beats MEWS/NEWS** — confirms your MEWS/NEWS baseline will similarly be outperformed by ML
- **No perioperative setting** — general ward data vs intraoperative OR — completely different monitoring context; your thesis fills this gap
- **No AUROC** — your use of AUROC as primary metric enables proper benchmarking that this paper could not provide
- **Cite in:** Related Work (traditional ML approaches), Methodology (SMOTE ratio discussion), Discussion (RF and LR as classical baselines)

---

## 7. Benchmarks Summary (Updated)

| Paper | Model | AUROC | Window | Setting | Dataset |
|---|---|---|---|---|---|
| Kwon et al. 2018 | RNN (DEWS) | 0.850 | 8hr | ICU | Custom |
| FAST-PACE 2019 | LSTM | 0.896 | 1–6hr | ICU | Custom |
| Lee et al. 2023 | LGBM (HRV) | 0.881 | 0.5–24hr | ICU | SNUH |
| **Chae et al. 2021** | **RF / LR / LSTM** | **N/A (PPV/Sens)** | **8hr** | **Ward** | **SCHMC** |
| Lee et al. 2024 | RF+LSTM+SVM | 0.91 | 1–13hr | ICU | MIMIC-IV |
| Li et al. 2026 | TrGRU | 0.957 | 1hr | ICU | MIMIC-III |

> Your TAN model target: **AUROC ≥ 0.89** — competitive against best externally validated ICU benchmark

---

## 8. Citation (APA)

Chae, M., Han, S., Gil, H., Cho, N., & Lee, H. (2021). Prediction of in-hospital cardiac arrest using shallow and deep learning. *Diagnostics, 11*(7), 1255. https://doi.org/10.3390/diagnostics11071255

---

*Notes by: Sachu Mon Puthenpuraickkal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
