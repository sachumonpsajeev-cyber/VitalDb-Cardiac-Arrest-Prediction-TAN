# Literature Review

---

## Paper 1: VitalDB Dataset (Lee et al. 2022)
**Link:** https://www.nature.com/articles/s41597-022-01411-5
**Citation:** Lee, H.C., Park, Y., Yoon, S.B. et al. VitalDB, a high-fidelity 
multi-parameter vital signs database in surgical patients. Scientific Data 9, 279 (2022).
**Date Read:** 18 Feb 2026

### 1. Problem They Solved
No large scale high resolution biosignal dataset existed for 
machine learning research on surgical patients.

### 2. Dataset Used
- 6,388 surgery cases from Seoul National University Hospital
- Collected August 2016 to June 2017
- 196 monitoring parameters per patient
- 486,451 total data tracks

### 3. Methodology
- Used Vital Recorder software to collect data
- Connected to 10 operating rooms simultaneously
- Time synchronized data from all devices

### 4. Results
- Successfully created open public dataset
- Average 2.8 million data points per patient
- Numeric data every 1-7 seconds
- Waveform data at 62.5-500 Hz

### 5. Limitations
- Single hospital in Seoul South Korea
- Single race - Asian patients only
- Surgical patients only not general ICU
- Real world noise not cleaned

### 6. Relevance to MY Project
- Primary dataset for cardiac arrest prediction
- No direct cardiac arrest label - will use mortality outcome
- Key features: HR, Blood Pressure, SpO2,ECG (500Hz), BIS, Cardiac Output
- Must handle missing data and noise in preprocessing
- Label Strategy: Start with in-hospital mortality (exists in clinical_information.csv), 
  then attempt to derive cardiac arrest label from HR/BP collapse patterns as advanced step

---

## Paper 2: Kwon et al. 2018 - Deep Learning for In-Hospital Cardiac Arrest Prediction

**Citation:** Kwon, J., Lee, Y., Lee, Y., Lee, S., & Park, J. (2018). An Algorithm 
Based on Deep Learning for Predicting In-Hospital Cardiac Arrest. Journal of the 
American Heart Association, 7(13), e008678. https://doi.org/10.1161/JAHA.118.008678
**Link:** https://www.ahajournals.org/doi/10.1161/JAHA.118.008678
**Date Read:** 19 Feb 2026

### 1. Problem They Solved
- Traditional early warning systems (like MEWS) had low sensitivity and high false alarm rates
- They treated each vital sign independently, ignoring relationships between signals
- No deep learning approach existed for in-hospital cardiac arrest (IHCA) prediction

### 2. Dataset Used
- 52,131 patients from 2 hospitals in South Korea
- June 2010 to July 2017 (retrospective cohort study)
- Train: June 2010 - January 2017
- Test: February 2017 - July 2017
- ~1,233 cardiac arrest cases (only 2.3% of patients = severe class imbalance)

### 3. Methodology
- Model: Recurrent Neural Network (RNN) called DEWS (Deep learning Early Warning System)
- Input: Only 4 vital signs — Systolic BP, Heart Rate, Respiratory Rate, Temperature
- Prediction window: 0.5 to 24 hours before cardiac arrest event
- Compared against: MEWS, Random Forest, Logistic Regression

### 4. Results
| Model | AUROC | AUPRC |
|---|---|---|
| DEWS (Deep Learning) | 0.850 | 0.044 |
| Random Forest | 0.780 | 0.014 |
| Logistic Regression | 0.613 | 0.007 |
| MEWS (traditional) | 0.603 | 0.003 |

- Deep learning significantly outperformed all traditional methods
- Reduced false alarms while maintaining high sensitivity

### 5. Limitations
- Only 4 vital signs used — no ECG waveform, no SpO2, no lab values
- Single race — Korean patients only (same as VitalDB)
- Severe class imbalance — only 2.3% positive cases
- Black box model — not interpretable for clinical staff
- General ward vitals measured manually (3x/day) — very low resolution

### 6. Relevance to MY Project
- This is the KEY baseline paper my thesis builds on
- Benchmark to beat: AUROC > 0.850
- MY improvement over Kwon: richer features (ECG, SpO2 continuous) + TAN architecture
- Class imbalance lesson: expect ~2-3% positive rate in VitalDB — plan SMOTE or class weights
- Prediction window to replicate: 0.5 to 24 hours before event


### Paper 3: TSCAN — Temporal-Spatial Correlation Attention Network (Nie et al., 2024)
**Link:** https://arxiv.org/abs/2306.01970 | https://ieeexplore.ieee.org/document/10234629/
**Date Read:** 19 Feb 2026

### 1. Problem They Solved
* ICU clinical data is multivariate and temporal — conventional models struggled to capture both dimensions simultaneously
* Existing methods treated temporal and spatial (inter-feature) dimensions separately, losing cross-dimensional information
* Medical time series data is sparse and strongly correlated — standard deep learning models (LSTM, Transformer) could not handle this effectively
* No unified architecture existed that jointly modelled temporal trends AND inter-feature correlations for multi-task ICU prediction

### 2. Dataset Used
* **Dataset:** MIMIC-IV v0.4
* **Source:** Beth Israel Deaconess Medical Center, Boston, USA
* **Period:** 2008–2019
* **Size:** 76,540 ICU stays from 53,150 patients (after processing: 47,046 stays)
* **Test Set:** 15% of patients — 7,057 patients, 8,906 ICU stays
* **Mortality Rate:** ~15%
* **Features:** 155 physiological variables (5 categorical + 150 continuous) including vitals, lab tests, demographics, medication, diagnosis

### 3. Methodology
* **Model:** TSCAN — Temporal-Spatial Correlation Attention Network
* **Architecture:** Dual-branch design:
  * **Temporal Branch:** Recursive merged attention — integrates features from previous time periods into the current end-time period; handles long ICU sequences without information loss
  * **Spatial Branch:** Inter-feature attention — captures correlations between clinical variables (e.g., BP ↔ HR ↔ SpO2)
  * **Fusion-Encoder:** Fuses temporal + spatial representations to produce the final prediction feature
* **Tasks Evaluated:** Mortality prediction, Length of Stay (LOS), Physiologic Decline, Phenotype Classification
* **Baselines Compared:** LSTM, Transformer, Informer, TimesNet, and other SOTA models
* Ablation studies conducted to validate each branch's individual contribution

### 4. Results
| Task | TSCAN Result | Improvement over SOTA |
|------|--------------|-----------------------|
| In-hospital Mortality | **90.7% AUROC** | +2.0% |
| Length of Stay | **45.1%** | +2.0% |
| Physiologic Decline | Best among all baselines | ✅ |
| Phenotype Classification | Best among all baselines | ✅ |

* Ablation confirmed removing either branch degrades performance — both branches are essential
* Attention maps identified **blood protein, blood pressure, and heart rate** as the most predictive clinical indicators

### 5. Limitations
* Validated on **MIMIC-IV only** — no external dataset validation (e.g., VitalDB, eICU)
* Focuses on **mortality and LOS** — not cardiac arrest as a specific acute prediction target
* No **perioperative or surgical** patient context — general ICU population only
* No discussion of **real-time or streaming inference** — limits direct ICU deployment applicability
* Dataset limited to a **single US hospital system** — generalisability across health systems unclear

### 6. Relevance to MY Project
* **Primary architectural reference** — TSCAN's dual-branch temporal-spatial attention design is the closest existing model to the Temporal Attention Network (TAN) I am implementing
* **Dataset gap I fill** — TSCAN is not validated on VitalDB; my thesis applies a similar attention approach to VitalDB's high-resolution perioperative data
* **Task gap I fill** — TSCAN targets mortality and LOS; I extend temporal-spatial attention to **cardiac arrest prediction** — a more acute and time-critical outcome
* **Benchmark reference** — TSCAN's 90.7% AUROC on mortality provides a strong ICU prediction performance anchor for contextualising my results
* **Interpretability validation** — TSCAN proves attention-based ICU models can surface clinically meaningful features (BP, HR), supporting my TAN design choice
* **Cite in:** Methodology chapter (justifying TAN architecture), Related Work section (positioning against SOTA), and Discussion (comparing interpretability findings)
