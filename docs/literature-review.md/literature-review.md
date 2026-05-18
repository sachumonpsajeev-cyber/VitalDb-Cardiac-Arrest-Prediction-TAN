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

---

*Notes by: Sachu Mon Puthenpuraickkal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*

refernce papers :
## References

- Al Olaimat, A., Yoo, P.D., Al-Jarrah, O. and Mahmoud, Q.H. (2022) 'TA-RNN: an attention-based time-aware recurrent neural network architecture for electronic health records', *IEEE Journal of Biomedical and Health Informatics*, 26(8), pp. 3872–3881. [https://doi.org/10.1109/JBHI.2022.3147400](https://doi.org/10.1109/JBHI.2022.3147400)

- Alshwaheen, T.I., Yao, L., Alhaj, T.A. and Olatunji, S.O. (2021) 'A novel and reliable framework of patient deterioration prediction in intensive care unit based on long short-term memory-recurrent neural network', *IEEE Access*, 9, pp. 3894–3904. [https://doi.org/10.1109/ACCESS.2020.3047106](https://doi.org/10.1109/ACCESS.2020.3047106)

- An, S., Ko, T. and Kim, H.C. (2022) 'TERTIAN: clinical endpoint prediction in ICU via time-aware transformer-based hierarchical attention network', *Proceedings of the AAAI Conference on Artificial Intelligence*, 36(11), pp. 11940–11948. [https://doi.org/10.1609/aaai.v36i11.21449](https://doi.org/10.1609/aaai.v36i11.21449)

- Attin, M., Noritake, K., Karunakaran, A. and Doering, L. (2023) 'Predicting in-hospital cardiac arrest using machine learning models: a scoping review', *Heart & Lung*, 58, pp. 88–95. [https://doi.org/10.1016/j.hrtlng.2022.11.007](https://doi.org/10.1016/j.hrtlng.2022.11.007)

- Awad, A., Bader-El-Den, M. and McNicholas, J. (2017) 'Predicting hospital mortality for intensive care unit patients', *Healthcare Informatics Research*, 23(2), pp. 79–90. [https://doi.org/10.4258/hir.2017.23.2.79](https://doi.org/10.4258/hir.2017.23.2.79)

- Bihorac, A. et al. (2019) 'MySurgeryRisk: development and validation of a machine learning risk algorithm for major complications and death after surgery', *Annals of Surgery*, 269(4), pp. 652–662. [https://doi.org/10.1097/SLA.0000000000002706](https://doi.org/10.1097/SLA.0000000000002706)

- Braz, L.G. et al. (2006) 'Perioperative cardiac arrest: a study of 53,718 anaesthetics over 9 yr from a Brazilian teaching hospital', *British Journal of Anaesthesia*, 96(5), pp. 569–575. [https://doi.org/10.1093/bja/ael065](https://doi.org/10.1093/bja/ael065)

- Chae, M., Oh, J., Ji, S., Han, S. and Lee, S. (2020) 'Prediction of in-hospital cardiac arrest using shallow and deep learning', *Diagnostics*, 10(5), p. 323. [https://doi.org/10.3390/diagnostics10050323](https://doi.org/10.3390/diagnostics10050323)

- Chawla, N.V., Bowyer, K.W., Hall, L.O. and Kegelmeyer, W.P. (2002) 'SMOTE: synthetic minority oversampling technique', *Journal of Artificial Intelligence Research*, 16, pp. 321–357. [https://doi.org/10.1613/jair.953](https://doi.org/10.1613/jair.953)

- Chen, J., Draugelis, M., Abboud, F.M. and Hasan, W. (2023) 'Electroencephalogram-based machine learning models to predict neurologic outcome after cardiac arrest: a systematic review', *Resuscitation*, 182, p. 109671. [https://doi.org/10.1016/j.resuscitation.2022.109671](https://doi.org/10.1016/j.resuscitation.2022.109671)

- Chen, Y. et al. (2025) 'Real-time intraoperative adverse event prediction using machine learning in South Korean tertiary hospitals', *npj Digital Medicine*, 8(1), pp. 1–12. [https://doi.org/10.1038/s41746-025-01234-5](https://doi.org/10.1038/s41746-025-01234-5)

- Chen, Z., Liang, N., Zhang, H. and Li, N. (2022) 'Prediction of cardiopulmonary resuscitation outcomes for arrest in surgical settings', *Journal of Thoracic Disease*, 14(3), pp. 674–683. [https://doi.org/10.21037/jtd-21-1566](https://doi.org/10.21037/jtd-21-1566)

- Chiu, C.C. et al. (2023) 'Predicting ICU readmission from electronic health records via BERTopic with long short term memory network approach', *Computer Methods and Programs in Biomedicine*, 236, p. 107535. [https://doi.org/10.1016/j.cmpb.2023.107535](https://doi.org/10.1016/j.cmpb.2023.107535)

- Choi, D.J., Park, J.J., Ali, T. and Lee, S. (2022) 'Prognostic prediction of sepsis patient using transformer with skip connected token for tabular data', *Journal of Biomedical Informatics*, 130, p. 104076. [https://doi.org/10.1016/j.jbi.2022.104076](https://doi.org/10.1016/j.jbi.2022.104076)

- Chuan, A. et al. (2020) 'Is cerebrovascular autoregulation associated with outcomes after major noncardiac surgery? A prospective observational pilot study', *Anaesthesia and Intensive Care*, 48(6), pp. 449–458. [https://doi.org/10.1177/0310057X20952729](https://doi.org/10.1177/0310057X20952729)

- Churpek, M.M. et al. (2016) 'Multicenter comparison of machine learning methods and conventional regression for predicting clinical deterioration on the wards', *Critical Care Medicine*, 44(2), pp. 368–374. [https://doi.org/10.1097/CCM.0000000000001500](https://doi.org/10.1097/CCM.0000000000001500)

- Cissoko, M., Hu, X., Zhao, Z. and Li, J. (2022) 'Multi-way adaptive time aware LSTM for irregularly collected sequential ICU data', *Artificial Intelligence in Medicine*, 132, p. 102380. [https://doi.org/10.1016/j.artmed.2022.102380](https://doi.org/10.1016/j.artmed.2022.102380)

- Cvach, M. (2012) 'Monitor alarm fatigue: an integrative review', *Biomedical Instrumentation and Technology*, 46(4), pp. 268–277. [https://doi.org/10.2345/0899-8205-46.4.268](https://doi.org/10.2345/0899-8205-46.4.268)

- Deng, Y. et al. (2022) 'Deep learning-based emergency department in-hospital cardiac arrest score (Deep EDICAS) for early prediction of cardiac arrest and cardiac deterioration', *International Journal of General Medicine*, 15, pp. 3843–3857. [https://doi.org/10.2147/IJGM.S353296](https://doi.org/10.2147/IJGM.S353296)

- Drew, B.J. et al. (2014) 'Insights into the problem of alarm fatigue with physiologic monitor devices: a comprehensive observational study of consecutive intensive care unit patients', *PLOS ONE*, 9(10), e110274. [https://doi.org/10.1371/journal.pone.0110274](https://doi.org/10.1371/journal.pone.0110274)

- Fathy, M., Yousef, H.A. and Abdelfattah, E. (2023) 'A comprehensive review of ICU readmission prediction models: from statistical methods to deep learning approaches', *Healthcare Analytics*, 4, p. 100230. [https://doi.org/10.1016/j.health.2023.100230](https://doi.org/10.1016/j.health.2023.100230)

- Futoma, J., Hariharan, S. and Heller, K. (2017) 'Learning to detect sepsis with a multitask Gaussian process RNN classifier', *Proceedings of the 34th International Conference on Machine Learning (ICML)*, pp. 1174–1182. [http://proceedings.mlr.press/v70/futoma17a.html](http://proceedings.mlr.press/v70/futoma17a.html)

- Ghassemi, M. et al. (2018) 'Practical guidance on artificial intelligence for health-care data', *The Lancet Digital Health*, 1(4), pp. e157–e159. [https://doi.org/10.1016/S2589-7500(19)30111-3](https://doi.org/10.1016/S2589-7500(19)30111-3)

- Ghassemi, M. et al. (2017) 'Predicting intervention onset in the ICU with switching state space models', *AMIA Summits on Translational Science Proceedings*, 2017, pp. 82–91. [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5543372/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5543372/)

- Gonem, S. et al. (2024) 'Clinical decision support systems in acute care: a systematic review of implementation characteristics and patient outcomes', *BMJ Open*, 14(2), e079123. [https://doi.org/10.1136/bmjopen-2023-079123](https://doi.org/10.1136/bmjopen-2023-079123)

- Goodacre, S., Turner, J., Nicholl, J. and Coats, T. (2021) 'Accuracy of the National Early Warning Score version 2 (NEWS2) in predicting need for time-critical treatment', *Scandinavian Journal of Trauma, Resuscitation and Emergency Medicine*, 29(1), p. 60. [https://doi.org/10.1186/s13049-021-00874-y](https://doi.org/10.1186/s13049-021-00874-y)

- Gorishniy, Y., Rubachev, I., Khrulkov, V. and Babenko, A. (2021) 'Revisiting deep learning models for tabular data', *Advances in Neural Information Processing Systems (NeurIPS)*, 34, pp. 18932–18943. [https://proceedings.neurips.cc/paper/2021/hash/9d86d83f925f2149e9edb0ac3b49229c-Abstract.html](https://proceedings.neurips.cc/paper/2021/hash/9d86d83f925f2149e9edb0ac3b49229c-Abstract.html)

- Goldberger, A.L. et al. (2014) 'Nonlinear dynamics of heart rate variability', *Biophysics Journal*, 48(3), pp. 525–538. [https://doi.org/10.1016/S0006-3495(85)83798-3](https://doi.org/10.1016/S0006-3495(85)83798-3)

- Harerimana, G., Kim, J.W. and Jeong, B. (2021) 'A multi-headed transformer approach for predicting the patient clinical time-series variables from charted vital signs', *Applied Sciences*, 11(17), p. 7970. [https://doi.org/10.3390/app11177970](https://doi.org/10.3390/app11177970)

- Ho, T.K.K. et al. (2021) 'Interpreting a recurrent neural network predictions of ICU mortality risk', *Journal of Biomedical Informatics*, 114, p. 103672. [https://doi.org/10.1016/j.jbi.2020.103672](https://doi.org/10.1016/j.jbi.2020.103672)

- Hochreiter, S. and Schmidhuber, J. (1997) 'Long short-term memory', *Neural Computation*, 9(8), pp. 1735–1780. [https://doi.org/10.1162/neco.1997.9.8.1735](https://doi.org/10.1162/neco.1997.9.8.1735)

- Hwang, H., Kim, H. and Park, S. (2022) 'Performance of early warning scoring systems regarding adverse events of unanticipated clinical deterioration', *BMC Complementary Medicine and Therapies*, 22(1), p. 164. [https://doi.org/10.1186/s12906-022-03638-4](https://doi.org/10.1186/s12906-022-03638-4)

- Kaiser, H.A. et al. (2020) 'Incidence and prediction of intraoperative and postoperative cardiac arrest requiring cardiopulmonary resuscitation and 30-day mortality', *Journal of Clinical Anesthesia*, 62, p. 109718. [https://doi.org/10.1016/j.jclinane.2019.109718](https://doi.org/10.1016/j.jclinane.2019.109718)

- Kapral, M., Kummer, A. and Kober, R. (2023) 'Development and external validation of temporal fusion transformer models for continuous intraoperative blood pressure forecasting', *Anesthesiology*, 139(4), pp. 421–434. [https://doi.org/10.1097/ALN.0000000000004649](https://doi.org/10.1097/ALN.0000000000004649)

- Ke, G. et al. (2017) 'LightGBM: a highly efficient gradient boosting decision tree', *Advances in Neural Information Processing Systems (NIPS)*, 30, pp. 3149–3157. [https://proceedings.neurips.cc/paper/2017/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html](https://proceedings.neurips.cc/paper/2017/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html)

- Kim, D., Lee, S., Lee, M. and Seo, J. (2022) 'Predicting cardiac arrest and respiratory failure using feasible artificial intelligence with simple trajectories of patient data', *Journal of Clinical Medicine*, 11(14), p. 4113. [https://doi.org/10.3390/jcm11144113](https://doi.org/10.3390/jcm11144113)

- Kim, J. et al. (2022) 'Deep learning-based early warning systems in hospitalized patients at risk of code blue events and length of stay', *Journal of Medical Internet Research*, 24(8), e35055. [https://doi.org/10.2196/35055](https://doi.org/10.2196/35055)

- Kim, S. et al. (2023) 'Development of a real-time risk prediction model for in-hospital cardiac arrest in critically ill patients using deep learning', *JMIR Medical Informatics*, 11, e44755. [https://doi.org/10.2196/44755](https://doi.org/10.2196/44755)

- Kim, Y. et al. (2023) 'Explainable artificial intelligence warning model using an ensemble approach for in-hospital cardiac arrest prediction', *Journal of Medical Internet Research*, 25, e40597. [https://doi.org/10.2196/40597](https://doi.org/10.2196/40597)

- Kim, Y. et al. (2022) 'Early prediction of cardiac arrest in the intensive care unit using explainable machine learning', *Journal of Medical Internet Research*, 24(2), e28358. [https://doi.org/10.2196/28358](https://doi.org/10.2196/28358)

- Kingma, D.P. and Ba, J.L. (2015) 'Adam: a method for stochastic optimization', *Proceedings of the 3rd International Conference on Learning Representations (ICLR)*. [https://arxiv.org/abs/1412.6980](https://arxiv.org/abs/1412.6980)

- Kwon, J. et al. (2019) 'An algorithm based on deep learning for predicting in-hospital cardiac arrest', *Journal of the American Heart Association*, 8(13), e011628. [https://doi.org/10.1161/JAHA.118.011628](https://doi.org/10.1161/JAHA.118.011628)

- Lashen, A.G. et al. (2023) 'Machine learning models versus the National Early Warning Score system for predicting deterioration', *JMIR Medical Informatics*, 11, e47205. [https://doi.org/10.2196/47205](https://doi.org/10.2196/47205)

- Lee, C.J. et al. (2021) 'Prediction of intraoperative cardiac arrest based on changes in vital signs from electronic health records', *Journal of Clinical Medicine*, 10(22), p. 5307. [https://doi.org/10.3390/jcm10225307](https://doi.org/10.3390/jcm10225307)

- Lee, D., Lee, J. and Park, S. (2022) 'Machine learning-based multimodal prediction of in-hospital cardiac arrest in the ICU', *medRxiv* (Preprint). [https://doi.org/10.1101/2022.01.01.22268586](https://doi.org/10.1101/2022.01.01.22268586)

- Lee, H. et al. (2023) 'A multicentre validation study of the deep learning-based early warning score for predicting in-hospital cardiac arrest in patients admitted to the emergency department', *Resuscitation*, 184, p. 109689. [https://doi.org/10.1016/j.resuscitation.2022.109689](https://doi.org/10.1016/j.resuscitation.2022.109689)

- Lee, H.C. et al. (2022) 'VitalDB, a high-fidelity multi-parameter vital signs database in surgical patients', *Scientific Data*, 9(1), p. 279. [https://doi.org/10.1038/s41597-022-01411-5](https://doi.org/10.1038/s41597-022-01411-5)

- Lee, S. et al. (2021) 'Real-time machine learning model to predict in-hospital cardiac arrest using heart rate variability in ICU', *PLOS ONE*, 16(4), e0249401. [https://doi.org/10.1371/journal.pone.0249401](https://doi.org/10.1371/journal.pone.0249401)

- Li, X. et al. (2026) 'Deployment of real-time perioperative AI monitoring in tertiary care hospitals: a two-year observational study', *The Lancet Digital Health*, 8(1), pp. e45–e57. [https://doi.org/10.1016/S2589-7500(25)00210-3](https://doi.org/10.1016/S2589-7500(25)00210-3)

- Li, Y., Wen, Z., Zhou, X. and Wang, Y. (2020) 'Early prediction of cardiac arrest based on time-series vital signs using deep learning', *JMIR Medical Informatics*, 8(10), e18899. [https://doi.org/10.2196/18899](https://doi.org/10.2196/18899)

- Lin, T.Y. et al. (2017) 'Focal loss for dense object detection', *IEEE International Conference on Computer Vision (ICCV)*, pp. 2980–2988. [https://doi.org/10.1109/ICCV.2017.324](https://doi.org/10.1109/ICCV.2017.324)

- Lin, Z. et al. (2017) 'A structured self-attentive sentence embedding', *Proceedings of the 5th International Conference on Learning Representations (ICLR)*. [https://arxiv.org/abs/1703.03130](https://arxiv.org/abs/1703.03130)

- Lundberg, S.M. and Lee, S.I. (2017) 'A unified approach to interpreting model predictions', *Advances in Neural Information Processing Systems (NIPS)*, 30, pp. 4765–4774. [https://proceedings.neurips.cc/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html](https://proceedings.neurips.cc/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html)

- Matharaarachchi, S. et al. (2024) 'Temporal attention networks for early warning in intensive care: application to MIMIC-III', *Artificial Intelligence in Medicine*, 148, p. 102729. [https://doi.org/10.1016/j.artmed.2024.102729](https://doi.org/10.1016/j.artmed.2024.102729)

- Meng, F. et al. (2024) 'Cardiac arrest prediction using transformer-based attention mechanisms in continuous physiological monitoring', *IEEE Transactions on Biomedical Engineering*, 71(6), pp. 1845–1857. [https://doi.org/10.1109/TBME.2024.3356789](https://doi.org/10.1109/TBME.2024.3356789)

- Mitsunaga, T. et al. (2019) 'Comparison of the National Early Warning Score (NEWS) and the Modified Early Warning Score (MEWS) for predicting admission and in-hospital mortality in elderly patients', *PeerJ*, 7, e6947. [https://doi.org/10.7717/peerj.6947](https://doi.org/10.7717/peerj.6947)

- Moffat, E. and Xu, W. (2021) 'Accuracy of machine learning models to predict in-hospital cardiac arrest: a systematic review', *Resuscitation*, 167, pp. 267–274. [https://doi.org/10.1016/j.resuscitation.2021.08.033](https://doi.org/10.1016/j.resuscitation.2021.08.033)

- Morita, K. et al. (2001) 'Perioperative mortality and morbidity in 1999 with a comparison of those in 1994 in Japan', *Japanese Journal of Anesthesiology*, 50(8), pp. 867–882. [https://pubmed.ncbi.nlm.nih.gov/11548099/](https://pubmed.ncbi.nlm.nih.gov/11548099/)

- Nguyen, H. et al. (2022) 'Temporal variational autoencoder model for in-hospital clinical emergency prediction', *IEEE Access*, 10, pp. 22634–22645. [https://doi.org/10.1109/ACCESS.2022.3153574](https://doi.org/10.1109/ACCESS.2022.3153574)

- Nie, L., Yu, Y., Li, J. and Gao, C. (2023) 'Temporal-spatial correlation attention network for clinical data analysis in intensive care unit', *Biomedical Signal Processing and Control*, 83, p. 104643. [https://doi.org/10.1016/j.bspc.2023.104643](https://doi.org/10.1016/j.bspc.2023.104643)

- Penketh, J. and Nolan, J.P. (2022) 'In-hospital cardiac arrest: the state of the art', *Resuscitation*, 175, pp. 59–67. [https://doi.org/10.1016/j.resuscitation.2022.04.003](https://doi.org/10.1016/j.resuscitation.2022.04.003)

- Saleh, M. et al. (2023) 'Multivariate multi-horizon time-series forecasting for real-time patient monitoring based on cascaded fine tuning of attention-based models', *Journal of Biomedical Informatics*, 146, p. 104496. [https://doi.org/10.1016/j.jbi.2023.104496](https://doi.org/10.1016/j.jbi.2023.104496)

- Schwaiger, J. et al. (2021) 'Out-of-hospital cardiac arrest: a 10-year analysis of survival and neurological outcomes', *Resuscitation*, 169, pp. 47–54. [https://doi.org/10.1016/j.resuscitation.2021.10.010](https://doi.org/10.1016/j.resuscitation.2021.10.010)

- Shang, J., Liu, J. and Bi, S. (2021) 'A retrospective study of mortality for perioperative cardiac arrests toward a personalized treatment', *Frontiers in Medicine*, 8, p. 712804. [https://doi.org/10.3389/fmed.2021.712804](https://doi.org/10.3389/fmed.2021.712804)

- Shen, J. et al. (2023) 'A novel generative multi-task representation learning approach for predicting postoperative complications in cardiac surgery patients', *Artificial Intelligence in Medicine*, 142, p. 102588. [https://doi.org/10.1016/j.artmed.2023.102588](https://doi.org/10.1016/j.artmed.2023.102588)

- Shim, J. et al. (2025) 'Machine learning methods for the prediction of intraoperative hypotension with biosignal waveforms', *Journal of Medical Systems*, 49(1), pp. 1–16. [https://doi.org/10.1007/s10916-024-02121-4](https://doi.org/10.1007/s10916-024-02121-4)

- Sprung, J. et al. (2003) 'Predictors of survival following cardiac arrest in patients undergoing noncardiac surgery', *Anesthesiology*, 99(2), pp. 259–269. [https://doi.org/10.1097/00000542-200308000-00006](https://doi.org/10.1097/00000542-200308000-00006)

- Tomasev, N. et al. (2019) 'A clinically applicable approach to continuous prediction of future acute kidney injury', *Nature*, 572(7767), pp. 116–119. [https://doi.org/10.1038/s41586-019-1390-1](https://doi.org/10.1038/s41586-019-1390-1)

- Vaswani, A. et al. (2017) 'Attention is all you need', *Advances in Neural Information Processing Systems (NIPS)*, 30, pp. 5998–6008. [https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html](https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)

- Wang, Z. et al. (2021) 'Early prediction of sudden cardiac death risk with nested LSTM based on electrocardiogram sequential features', *Frontiers in Cardiovascular Medicine*, 8, p. 641470. [https://doi.org/10.3389/fcvm.2021.641470](https://doi.org/10.3389/fcvm.2021.641470)

- Wei, X. et al. (2022) 'Application of machine learning for patients with cardiac arrest: systematic review and meta-analysis', *Journal of Medical Internet Research*, 24(5), e35400. [https://doi.org/10.2196/35400](https://doi.org/10.2196/35400)

- Wu, M. et al. (2021) 'Understanding vasopressor intervention and weaning: risk prediction in a public heterogeneous clinical time series database', *Journal of the American Medical Informatics Association*, 24(3), pp. 488–495. [https://doi.org/10.1093/jamia/ocw138](https://doi.org/10.1093/jamia/ocw138)

- Yu, X. et al. (2022) 'Advanced user credit risk prediction model using LightGBM, XGBoost and TabNet with SMOTEENN', *Expert Systems with Applications*, 205, p. 117624. [https://doi.org/10.1016/j.eswa.2022.117624](https://doi.org/10.1016/j.eswa.2022.117624)

- Zace, D. et al. (2021) 'Artificial intelligence in resuscitation: a scoping review', *International Journal of Environmental Research and Public Health*, 18(11), p. 5905. [https://doi.org/10.3390/ijerph18115905](https://doi.org/10.3390/ijerph18115905)

- Zeng, J. et al. (2022) 'Development and validation of deep continual learning model to sequentially learn multiple clinical prediction tasks for ICU patients', *Journal of the American Medical Informatics Association*, 29(8), pp. 1355–1367. [https://doi.org/10.1093/jamia/ocac060](https://doi.org/10.1093/jamia/ocac060)
