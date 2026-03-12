# Literature Review
**Thesis:** Cardiac Arrest Prediction Using VitalDB + Temporal Attention Network (TAN)
**Author:** Sachu Mon Puthenpuraickkal Sajeev | TSI University
**Last Updated:** 23 Feb 2026

---

## 📁 Core Papers

---

### Paper 1: Lee et al. 2022 — VitalDB High-Fidelity Vital Signs Dataset

**Citation:** Lee, H.C., Park, Y., Yoon, S.B. et al. VitalDB, a high-fidelity multi-parameter vital signs database in surgical patients. *Scientific Data* 9, 279 (2022). https://doi.org/10.1038/s41597-022-01411-5 **Link:** https://www.nature.com/articles/s41597-022-01411-5 **Date Read:** 18 Feb 2026

> 🔴 **CORE PAPER** — Primary dataset for entire thesis

#### 1. Problem They Solved

- No large-scale, high-resolution biosignal dataset existed for machine learning research on surgical patients
- Existing datasets were small, low-resolution, or not publicly available
- No standardised perioperative monitoring database for AI development

#### 2. Dataset Used

- 6,388 surgical cases from Seoul National University Hospital
- Collected August 2016 to June 2017
- 196 monitoring parameters per patient
- 486,451 total data tracks
- Average 2.8 million data points per patient
- Numeric data recorded every 1–7 seconds
- Waveform data at 62.5–500 Hz

#### 3. Methodology

- Used Vital Recorder software to collect continuous intraoperative data
- Connected simultaneously to 10 operating rooms
- Time-synchronised data streams from all monitoring devices
- Released as open public dataset

#### 4. Results

- Successfully created the largest open perioperative biosignal database
- Covers ECG, arterial blood pressure, SpO₂, BIS, cardiac output, and 190+ additional parameters

#### 5. Limitations

- Single-centre study — Seoul National University Hospital, South Korea only
- Predominantly Asian patient population — limits generalisability
- Surgical patients only — not applicable to general ICU settings
- Raw data includes real-world noise — no preprocessing applied

#### 6. Relevance to My Project

- Primary dataset for cardiac arrest prediction model
- No direct cardiac arrest label — initial label strategy uses in-hospital mortality from `clinical_information.csv`
- Advanced step: derive cardiac arrest label from HR/BP collapse patterns
- Key features: HR, Blood Pressure, SpO₂, ECG (500 Hz), BIS, Cardiac Output
- Key challenge: substantial missing data and signal noise must be handled in preprocessing
- **Cite in:** Methodology (dataset description), Data chapter (preprocessing justification)

---

### Paper 3: Nie et al. 2024 — TSCAN: Temporal-Spatial Correlation Attention Network

**Citation:** Nie, W., Yu, Y., Zhang, C., Song, D., Zhao, L., & Bai, Y. (2024). Temporal-Spatial Correlation Attention Network for Clinical Data Analysis in Intensive Care Unit. *IEEE Transactions on Knowledge and Data Engineering.* https://doi.org/10.1109/TKDE.2023.3309148 **Link:** https://ieeexplore.ieee.org/document/10234629 **Date Read:** 19 Feb 2026

> 🔴 **CORE PAPER** — Primary architecture reference for the Temporal Attention Network (TAN) implemented in this thesis

#### 1. Problem They Solved

- ICU clinical data is multivariate and temporal — conventional models struggled to capture both dimensions simultaneously
- Existing methods treated temporal and spatial (inter-feature) dimensions separately, losing cross-dimensional information
- Medical time series data is sparse and strongly correlated — standard deep learning models (LSTM, Transformer) could not handle this effectively
- No unified architecture existed that jointly modelled temporal trends AND inter-feature correlations for multi-task ICU prediction

#### 2. Dataset Used

- **Dataset:** MIMIC-IV v0.4
- **Source:** Beth Israel Deaconess Medical Center, Boston, USA
- **Period:** 2008–2019
- **Raw size:** 76,540 ICU stays from 53,150 patients
- **After processing:** 47,046 ICU stays
- **Test set:** 15% of patients — 7,057 patients, 8,906 ICU stays
- **Mortality rate:** ~15%
- **Features:** 155 physiological variables (5 categorical + 150 continuous)

#### 3. Methodology

- **Model:** TSCAN — dual-branch design
- **Temporal Branch:** Recursive merged attention — integrates features from previous time periods without information loss
- **Spatial Branch:** Inter-feature attention — captures correlations between clinical variables (e.g., BP ↔ HR ↔ SpO₂)
- **Fusion-Encoder:** Fuses temporal + spatial representations for final prediction
- **Tasks evaluated:** Mortality prediction, Length of Stay, Physiologic Decline, Phenotype Classification
- **Baselines compared:** LSTM, Transformer, Informer, TimesNet

#### 4. Results

| Task | TSCAN Result | Improvement over SOTA |
|---|---|---|
| In-hospital Mortality | **90.7% AUROC** | +2.0% |
| Length of Stay | **45.1%** | +2.0% |
| Physiologic Decline | Best among all baselines | ✅ |
| Phenotype Classification | Best among all baselines | ✅ |

- Ablation confirmed both branches are essential
- Attention maps identified blood protein, blood pressure, and heart rate as most predictive

#### 5. Limitations

- Validated on MIMIC-IV only — no external dataset validation
- Focuses on mortality and LOS — not cardiac arrest as a specific acute prediction target
- No perioperative or surgical patient context
- No real-time or streaming inference discussion

#### 6. Relevance to My Project

- **Primary architectural reference** — TSCAN's dual-branch temporal-spatial attention design is the closest existing model to my TAN
- **Dataset gap I fill** — TSCAN not validated on VitalDB
- **Task gap I fill** — I extend temporal-spatial attention to cardiac arrest prediction
- **Cite in:** Methodology (justifying TAN architecture), Related Work, Discussion (interpretability)

---

## 📁 Benchmark Papers

---

### Paper 2: Kwon et al. 2018 — Deep Learning for In-Hospital Cardiac Arrest Prediction

**Citation:** Kwon, J., Lee, Y., Lee, Y., Lee, S., & Park, J. (2018). An Algorithm Based on Deep Learning for Predicting In-Hospital Cardiac Arrest. *Journal of the American Heart Association*, 7(13), e008678. https://doi.org/10.1161/JAHA.118.008678 **Link:** https://www.ahajournals.org/doi/10.1161/JAHA.118.008678 **Date Read:** 19 Feb 2026

> 🟡 **BENCHMARK PAPER** — Primary deep learning benchmark, AUROC 0.850 target to beat

#### 1. Problem They Solved

- Traditional early warning systems (MEWS) had low sensitivity and high false alarm rates
- They treated each vital sign independently, ignoring relationships between signals
- No deep learning approach existed for in-hospital cardiac arrest (IHCA) prediction

#### 2. Dataset Used

- Clinical database — vital signs from general ward patients
- Features: vital signs including HR, BP, RR, SpO₂, temperature

#### 3. Methodology

- Recurrent neural network (RNN) based early warning model
- Real-time prediction capability
- Cross-validation performed

#### 4. Results

- **AUROC: 0.850** — primary benchmark target for this thesis
- Superior to MEWS and traditional scoring systems
- Real-time prediction demonstrated

#### 5. Limitations

- General ward patients only — not perioperative surgical setting
- Limited feature set compared to VitalDB's 196 parameters
- No attention mechanism or interpretability

#### 6. Relevance to My Project

- **Primary benchmark** — AUROC 0.850 is the minimum performance target my TAN must beat
- Establishes RNN as the deep learning baseline for IHCA prediction
- My TAN adds temporal-spatial attention on top of this recurrent approach
- **Cite in:** Related Work, Results (direct benchmark comparison)

---

### Paper 6 (Soudan et al. 2022) — AI on EHR Vital Signs for Cardiac Arrest Prediction

**Citation:** Soudan, B., Dandachi, F.F., & Bou Nassif, A. (2022). Attempting cardiac arrest prediction using artificial intelligence on vital signs from Electronic Health Records. *Smart Health*, 26, 100352. https://doi.org/10.1016/j.smhl.2022.100352 **Link:** https://www.sciencedirect.com/science/article/abs/pii/S2352648322000290 **Date Read:** 21 Feb 2026

> 🟡 **BENCHMARK PAPER** — Traditional ML baseline for cardiac arrest prediction using vital signs

#### 1. Problem They Solved

- No systematic comparison of AI algorithms for CA prediction using routine EHR vital signs
- Unclear which vital signs, models, and time windows produced the most accurate prediction
- Clinical teams lacked advance warning tools for cardiac arrest

#### 2. Dataset Used

- Hospital Electronic Health Records (EHR)
- Routinely recorded vital signs
- Time windows tested: 1 to 12 hours prior to event

#### 3. Methodology

- Compared six AI algorithms including Random Forest, logistic regression, SVM, decision tree, KNN, and neural network
- Tested multiple vital sign combinations and time windows systematically

#### 4. Results

- **Best model:** Random Forest — >80% accuracy
- **Best time window:** Immediately preceding 60 minutes
- +10% improvement using last 60 min vs longer windows

#### 5. Limitations

- Traditional ML only — no deep learning or attention mechanisms
- EHR vital signs only — no high-resolution waveform data
- Accuracy metric used — AUROC not reported

#### 6. Relevance to My Project

- Confirms vital signs alone are sufficient signal for CA prediction
- 60-minute time window informs my sliding window design
- Random Forest provides a traditional ML benchmark to compare against my TAN
- **Cite in:** Related Work (traditional ML approaches), Discussion

---

### Paper 7: Li, Lv & Wang 2026 — TrGRU: Early Prediction of Cardiac Arrest Using Deep Learning

**Citation:** Li, Y., Lv, L., & Wang, X. (2026). Early Prediction of Cardiac Arrest Based on Time-Series Vital Signs Using Deep Learning: Retrospective Study. *JMIR Formative Research*, 10, e78484. https://doi.org/10.2196/78484 **Link:** https://formative.jmir.org/2026/1/e78484 **Date Read:** 22 Feb 2026

> 🟡 **BENCHMARK PAPER** — Current SOTA deep learning model for cardiac arrest prediction — primary performance target to beat

#### 1. Problem They Solved

- Existing CA prediction models suffered from low sensitivity and high false alarm rates
- No hybrid Transformer-GRU architecture had been applied to cardiac arrest prediction
- Models lacked real-time prediction capability and cross-dataset generalisation

#### 2. Dataset Used

- **Primary:** MIMIC-III waveform database — 4,063 patients
- **External validation:** eICU-CRD — 200,000+ ICU admissions across 208 US hospitals
- **Features:** 6 vital signs — HR, respiratory rate, systolic BP, diastolic BP, MAP, SpO₂
- **Prediction window:** 2-hour input → predict CA within next 1 hour at 5-minute intervals

#### 3. Methodology

- **Model:** TrGRU — 3 stacked Transformer encoder layers → 2 GRU layers → Global Average Pooling → Fully Connected output
- Statistical features via 2-hour sliding window
- Meta-learning for cross-dataset generalisation
- **Baselines:** Logistic Regression, XGBoost, LGBM, Random Forest

#### 4. Results

| Metric | TrGRU (MIMIC-III) | eICU-CRD (External) |
|---|---|---|
| Accuracy | **0.904** | — |
| Sensitivity | **0.859** | 0.813 |
| AUROC | **0.957** | 0.920 |
| AUPRC | **0.949** | 0.848 |

- Sensitivity at 30 min before CA: 90.6%
- Sensitivity at 10 min before CA: 94.8%

#### 5. Limitations

- Only 6 features — does not exploit high-resolution waveform data
- Not tested on VitalDB perioperative data
- No attention interpretability — black box predictions

#### 6. Relevance to My Project

- **Primary SOTA benchmark** — AUROC 0.957 is the current performance ceiling I am targeting
- **Gap I fill** — TrGRU uses only 6 features; I use VitalDB's high-resolution waveform data
- **Gap I fill** — No interpretability in TrGRU; my TAN provides clinical explainability
- **Gap I fill** — Perioperative surgical patients not studied — VitalDB fills this gap
- **Cite in:** Related Work, Methodology (architectural comparison), Results, Discussion

---

## 📁 Supporting Papers

---

### Paper 8: Kim et al. 2019 — FAST-PACE: Feasible AI with Simple Trajectories for CA Prediction

**Citation:** Kim, J., Chae, M., Chang, H.J., Kim, Y.A., & Park, E. (2019). Predicting Cardiac Arrest and Respiratory Failure Using Feasible Artificial Intelligence with Simple Trajectories of Patient Data. *Journal of Clinical Medicine*, 8(9), 1336. https://doi.org/10.3390/jcm8091336 **Link:** https://pmc.ncbi.nlm.nih.gov/articles/PMC6780058/ **Date Read:** 21 Feb 2026

> 🟢 **SUPPORTING PAPER** — LSTM baseline for CA prediction + 1–6hr prediction window reference + feature minimalism strategy

#### 1. Problem They Solved

- Existing CA prediction models relied heavily on lab results — not feasible in wards or emergency settings
- Score-based systems (MEWS, NEWS) had low sensitivity and high false alarm rates
- No model existed that could predict CA using only basic vital signs without lab data

#### 2. Dataset Used

- 29,181 ICU patients from two hospitals (surgical ICU + mixed ICU)
- 242 CA cases, 1,231 respiratory failure cases
- Data source: EMR — periodic vital signs only

#### 3. Methodology

- **Model:** LSTM on time-series vital sign trajectories
- **Features:** 9 only — HR, SBP, DBP, RR, SpO₂, temperature, surgical history, treatment history, ASA classification
- **Prediction windows:** 1hr, 2hr, 4hr, 6hr before event
- **Baselines:** MEWS and NEWS scoring systems

#### 4. Results

| Time Window | FAST-PACE AUROC | MEWS AUROC | NEWS AUROC |
|---|---|---|---|
| 1 hour | **0.896** | 0.746 | 0.759 |
| 6 hours | **0.886** | — | — |

- Average sensitivity: 0.844 (vs MEWS 0.400, NEWS 0.695)

#### 5. Limitations

- ICU setting only — not validated in perioperative OR environment
- Single country (South Korea)
- RR and Body Temperature included — both excluded in this thesis due to VitalDB missing data

#### 6. Relevance to My Project

- **1–6hr prediction window clinically validated** — supports shorter window discussion with supervisor
- **LSTM is the established deep learning baseline** — TAN should be compared against LSTM
- **Minimal feature set works** — 9 features achieved AUROC 0.896, supports 6-feature VitalDB approach
- **AUROC 0.896 at 1hr window** — secondary benchmark to beat alongside Kwon et al. 0.850
- **Cite in:** Related Work, Methodology (feature selection + window justification), Discussion

---

## 📋 Papers To Be Added

> The following papers are still to be documented. Add notes below each entry as you read them.

---

### Paper 4: Kim et al. 2004
**Status:** 🔴 Notes not yet written
**File:** `kim et al 2004.pdf`
**Category:** Supporting Paper

---

### Paper 5: Kim et al. 2018
**Status:** 🔴 Notes not yet written
**File:** `kim et al 2018.pdf`
**Category:** Supporting Paper

---

### Paper 6: HRV Paper
**Status:** 🔴 Notes not yet written
**File:** `hrv.pdf`
**Category:** Supporting Paper

---

### Papers 9–15: To Be Identified
**Status:** 🔴 Not yet added
**Action:** Add paper details here as you read each one

---

## 📊 Summary Table

| # | Authors | Year | Category | AUROC | Relevance |
|---|---|---|---|---|---|
| 1 | Lee et al. | 2022 | 🔴 Core | — | Primary dataset |
| 2 | Kwon et al. | 2018 | 🟡 Benchmark | 0.850 | Primary DL benchmark |
| 3 | Nie et al. | 2024 | 🔴 Core | 0.907 | Primary architecture ref |
| 4 | Kim et al. | 2004 | 🟢 Supporting | TBC | TBC |
| 5 | Kim et al. | 2018 | 🟢 Supporting | TBC | TBC |
| 6 | Soudan et al. | 2022 | 🟡 Benchmark | >0.80 | Traditional ML baseline |
| 7 | Li, Lv & Wang | 2026 | 🟡 Benchmark | 0.957 | Current SOTA target |
| 8 | Kim et al. | 2019 | 🟢 Supporting | 0.896 | LSTM baseline + window ref |
| 9–15 | TBC | TBC | TBC | TBC | TBC |

---

*Notes by: Sachu Mon Puthenpuraickkal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
