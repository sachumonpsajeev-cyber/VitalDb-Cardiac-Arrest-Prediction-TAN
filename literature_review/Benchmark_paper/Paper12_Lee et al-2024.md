# Paper 12: Lee et al. 2024 (RF+LSTM+SVM — Multimodal IHCA)

> 🟡 **BENCHMARK PAPER** — Multimodal stacked ensemble RF+LSTM+SVM for in-hospital cardiac arrest prediction — AUROC 0.91 at 1 hour before CA — MIMIC-IV + eICU external validation

---

## Metadata
 
| Field | Details |
|---|---|
| **Title** | Prediction of In-Hospital Cardiac Arrest in the Intensive Care Unit: Machine Learning–Based Multimodal Approach |
| **Authors** | Hsin-Ying Lee, Po-Chih Kuo, Frank Qian, Chien-Hung Li, Jiun-Ruey Hu, Wan-Ting Hsu, Hong-Jie Jhou, Po-Huang Chen, Cho-Hao Lee, Chin-Hua Su, Po-Chun Liao, I-Ju Wu, Chien-Chang Lee |
| **Institution** | National Taiwan University; National Tsing Hua University; Boston Medical Center; Yale School of Medicine; Harvard T.H. Chan School of Public Health |
| **Journal** | JMIR Medical Informatics |
| **Year** | 2024 |
| **Volume** | Volume 12, Article e49142 |
| **DOI** | 10.2196/49142 |
| **Full Text** | https://medinform.jmir.org/2024/1/e49142 |
| **PMC** | https://pmc.ncbi.nlm.nih.gov/articles/PMC11287234/ |
| **PubMed** | https://pubmed.ncbi.nlm.nih.gov/39051152/ |
| **Citation** | Lee HY, Kuo PC, Qian F, et al. Prediction of in-hospital cardiac arrest in the intensive care unit: machine learning–based multimodal approach. *JMIR Med Inform*. 2024;12:e49142. doi:10.2196/49142 |
| **Read Date** | Feb 24, 2026 |
| **Category** | 🟡 Benchmark Paper |
| **Thesis Relevance** | ⭐⭐⭐⭐⭐ Critical — directly predicts IHCA using same vital signs (HR, SpO2, BP), AUROC 0.91 at 1hr before CA is highest ICU benchmark, multimodal RF+LSTM stacking comparable to TAN architecture |

---

## 1. Problem They Solved

- Early identification of impending in-hospital cardiac arrest (IHCA) improves clinical outcomes but remains elusive for clinicians
- Existing models relied either on **static baseline features** (demographics, comorbidities) OR **temporal vital signs** — never combined both effectively
- Traditional early warning scores (MEWS, CART) showed poor sensitivity and insufficient lead time — CART could not detect 65% of events even 1 hour before arrest
- Lab-based models (e.g., eCART with lactic acid) had high missingness rates (~68% in MIMIC-IV), limiting practical deployment
- No validated multimodal model had combined structured EHR data with time-series vital signs for IHCA prediction with external validation

---

## 2. Dataset Used

| Field | Details |
|---|---|
| **Primary Dataset** | MIMIC-IV v0.4 |
| **Total patients (MIMIC-IV)** | 23,909 (after exclusions) |
| **IHCA cases (MIMIC-IV)** | 452 patients (1.9%) |
| **Control (MIMIC-IV)** | 23,457 patients |
| **External Validation 1** | eICU-CRD v2.0 — 10,049 patients (85 IHCA) |
| **External Validation 2** | National Taiwan University Hospital (NTUH) — 1,935 IHCA + 3,692 control (2008–2018) |
| **Setting** | ICU — critically ill patients, ≥24 hours admission, age >20 years |
| **Prediction window** | 13 hours prior to IHCA — hourly measurements |
| **Vital signs** | HR, RR, SpO2, sBP, dBP, MAP — extracted hourly |
| **Baseline features** | Demographics, presenting illness (ICD codes), comorbidities (Elixhauser Index) |
| **Missing data handling** | Last observation carried forward; SMOTE for class imbalance |

---

## 3. Methodology

### Three-Stage Stacked Ensemble Architecture

**Stage 1 — Random Forest (RF)**
- Input: Time-independent baseline features — demographics, presenting illness (ICD codes for MI, pneumonia, respiratory failure, H's and T's), comorbidity scores
- Hyperparameters: n_estimators = 5, max_depth = 20, Gini impurity, min samples leaf = 2
- Output: Baseline risk probability score
- Standalone AUROC: **0.80** (95% CI 0.779–0.844)
- Top features: respiratory failure/acidosis, uncomplicated hypertension, fluid/electrolyte disorder, cardiac ICU admission

**Stage 2 — LSTM (Long Short-Term Memory)**
- Input: 6 vital signs hourly over 24 hours — HR, RR, SpO2, sBP, dBP, MAP
- Architecture: 3 hidden layers, 8 cells each, tanh + sigmoid activation
- Training: Adam optimizer, learning rate 0.001, dropout 0.4, SMOTE applied
- Output: Temporal risk probability from vital sign trajectories
- Key finding: IHCA patients showed ~12 mmHg lower sBP, ~1.5% lower SpO2, ~9 bpm higher HR throughout 24-hour window vs controls, with sharp deterioration in final hours

**Stage 3 — SVM Stacking**
- Input: RF probability + LSTM probability (late fusion)
- Kernel: Radial basis function (RBF), L2 penalty, C=1
- Output: Final IHCA prediction probability
- SVM vs LR stacking at 1hr: AUROC 0.91 vs 0.80 — SVM clearly superior
- Rationale for late fusion: avoids feature discrepancy between static and temporal modalities; enables independent model training

### Class Imbalance Handling
- SMOTE (synthetic minority oversampling) applied — nearest neighbor interpolation k=1
- Near-miss algorithm tested and found inferior

### Model Interpretability
- RF feature importance ranked by "gain" metric
- LSTM explained via SHAP values at patient level — shows which vital sign contributed to risk at each timepoint

---

## 4. Results

### Internal Validation (MIMIC-IV)

| Hours Before CA | AUROC | Sensitivity | Specificity | F1-score |
|---|---|---|---|---|
| **13 hours** | **0.85** (0.815–0.885) | — | — | — |
| **1 hour** | **0.91** (0.874–0.935) | **0.80** | **0.86** | **0.85** |
| RF alone | 0.80 | 0.71 | 0.78 | 0.79 |

- Steady rise in AUROC from 13hr to 1hr before CA
- Sharp increase in detection rate in the final 3 hours
- Stacked model consistently outperforms RF-alone and LSTM-alone at all timepoints
- At 12 hours before CA: model detects >70% of patients at risk (vs CART: <65% even at 1hr)

### External Validation

| Dataset | AUROC (1hr before CA) | Sensitivity | Specificity | F1-score |
|---|---|---|---|---|
| eICU-CRD | 0.89 (0.849–0.920) | 0.79 | 0.83 | 0.81 |
| NTUH (clinical) | **0.945** (0.934–0.956) | High | — | — |

- eICU-CRD validation closely mirrors MIMIC-IV performance — confirms generalisability
- NTUH clinical validation highest at 0.945 — home-institution advantage likely
- Outperforms CART score at all timepoints throughout the 13-hour prediction window

### Calibration
- Calibration plots showed some overestimation risk
- Brier scores steadily low throughout 13-hour window — acceptable accuracy

---

## 5. Limitations

- **ICU-only setting** — model developed on ICU patients; generalisability to ward or perioperative settings not demonstrated
- **Single-center development** — trained on MIMIC-IV (Beth Israel Deaconess Medical Center, Boston)
- **No clinical interventions** — treatment data (vasopressors, intubation, fluid boluses) excluded due to complexity and missingness
- **No body temperature or neurological status** — prevented comparison to MEWS and APACHE
- **IHCA labeling relies on ICD codes and procedure timestamps** — documentation delays and operator-dependent accuracy introduce label noise
- **Missing lab data** — lactic acid 68.2% missing — forces vital signs–only approach (though arguably a strength for practical deployment)
- **Hourly resolution** — less granular than high-frequency monitoring; may miss rapid deterioration between measurements
- **Not tested on perioperative/OR patients** — intraoperative physiology differs fundamentally from ICU baseline

---

## 6. Relevance to This Thesis

### Direct Connections

| Aspect | Lee et al. 2024 (RF+LSTM+SVM) | This Thesis |
|---|---|---|
| **Target outcome** | In-hospital cardiac arrest (IHCA) | Intraoperative cardiac arrest |
| **Setting** | ICU (critical care) | Surgical OR (perioperative) |
| **Architecture** | RF + LSTM + SVM stacking | TAN — Temporal Attention Network |
| **Vital signs** | HR, SpO2, sBP, dBP, MAP, RR | HR, SpO2, ETCO2, ART_MBP, ART_SBP, ART_DBP |
| **Dataset** | MIMIC-IV + eICU external | VitalDB (6,388 patients) |
| **Prediction window** | Up to 13 hours | 30–240 minute windows |
| **Best AUROC** | 0.91 (internal) / 0.945 (NTUH) | TAN target: ≥0.89 |
| **Class imbalance** | SMOTE | TBD |
| **Interpretability** | SHAP (LSTM) + RF feature importance | TAN attention weights |

### Key Takeaways for Thesis

1. **New highest ICU benchmark** — AUROC 0.91 (MIMIC-IV internal) and 0.945 (NTUH clinical) surpasses all prior cardiac arrest prediction benchmarks; fair external comparison target is eICU result: **0.89**
2. **Same vital signs** — HR, SpO2, BP used in identical fashion — directly comparable feature sets to your VitalDB inputs
3. **Multimodal stacking vs end-to-end** — demonstrates that combining static patient profile with temporal vital signs improves performance; TAN should be compared against this paradigm
4. **SHAP interpretability** — their use of SHAP for LSTM explanations is directly analogous to TAN attention weights as your interpretability mechanism
5. **Clinical lead time** — detecting CA 13 hours in advance is their key clinical claim; your 30–240 minute windows are more clinically focused on the immediate surgical context
6. **ICU vs OR gap** — your thesis addresses a fundamentally different and harder setting: intraoperative where physiology is actively manipulated by anaesthesia and surgery — this model does not address that gap
7. **Cite in Chapter 2 (Related Work)** — strongest direct benchmark for IHCA prediction; use to establish state-of-the-art before arguing your thesis fills the perioperative gap

### Benchmark Target Note
> The fair comparison target from this paper is AUROC **0.89** (eICU external validation), not 0.945 (home-institution NTUH). Targeting ≥0.89 on VitalDB would represent competitive performance against the best externally validated ICU benchmark, in a harder and clinically distinct perioperative setting.

---

## 7. Updated Benchmarks Summary

| Paper | Model | AUROC | Window | Setting | Dataset |
|---|---|---|---|---|---|
| Kwon et al. 2018 | RNN | 0.850 | 8hr | ICU | Custom |
| FAST-PACE 2019 | LSTM | 0.896 | 1–6hr | ICU | Custom |
| Lee et al. 2023 | LGBM | 0.881 | 0.5–24hr | ICU | SNUH |
| TA-RNN 2024 | TA-RNN | N/A (F2) | Per visit | EHR | ADNI/MIMIC |
| Kapral et al. 2024 | TFT | N/A (MAE 4mmHg) | 7 min | OR | VitalDB |
| **Lee et al. 2024** | **RF+LSTM+SVM** | **0.91 / 0.945** | **1–13hr** | **ICU** | **MIMIC-IV + eICU** |

> **Your TAN model target: AUROC ≥ 0.89** to achieve competitive performance against the best externally validated ICU benchmark in a harder perioperative setting

---

## 8. Citation (APA)

Lee, H.-Y., Kuo, P.-C., Qian, F., Li, C.-H., Hu, J.-R., Hsu, W.-T., Jhou, H.-J., Chen, P.-H., Lee, C.-H., Su, C.-H., Liao, P.-C., Wu, I.-J., & Lee, C.-C. (2024). Prediction of in-hospital cardiac arrest in the intensive care unit: machine learning–based multimodal approach. *JMIR Medical Informatics, 12*, e49142. https://doi.org/10.2196/49142

---

*Notes by: Sachu Mon Puthenpuraickpal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
