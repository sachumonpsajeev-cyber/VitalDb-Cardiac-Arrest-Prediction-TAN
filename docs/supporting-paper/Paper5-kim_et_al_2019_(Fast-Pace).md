# Paper 5: Kim et al. 2019 (FAST-PACE)

>  🟢**SUPPORTING PAPER** — LSTM baseline for CA prediction + 1-6hr prediction window reference + feature minimalism strategy

---

## Metadata
| Field | Details |
|---|---|
| **Title** | Predicting Cardiac Arrest and Respiratory Failure Using Feasible Artificial Intelligence with Simple Trajectories of Patient Data |
| **Authors** | Jeongmin Kim, Myunghun Chae, Hyuk-Jae Chang, Young-Ah Kim, Eunjeong Park |
| **Journal** | Journal of Clinical Medicine |
| **Year** | 2019 |
| **DOI** | 10.3390/jcm8091336 |
| **Link** | https://pmc.ncbi.nlm.nih.gov/articles/PMC6780058/ |
| **Citation** | Kim, J., Chae, M., Chang, H.J., Kim, Y.A., & Park, E. (2019). Predicting cardiac arrest and respiratory failure using feasible artificial intelligence with simple trajectories of patient data. *Journal of Clinical Medicine, 8*(9), 1336. |
| **Read Date** | Feb 21, 2026 |
| **Category** |  🟢Supporting Paper |
| **Thesis Relevance** | ⭐⭐⭐⭐⭐ High — LSTM for CA specifically + short prediction window + minimal feature set closest to VitalDB context |

---

## 1. Problem They Solved
- Existing CA prediction models relied heavily on lab results — not feasible in wards, emergency transport, or out-of-hospital settings
- Score-based systems (MEWS, NEWS) had low sensitivity and high false alarm rates
- No model existed that could predict CA using only basic vital signs without lab data
- Need for a clinically feasible real-time AI model using minimal, readily available features

---

## 2. Dataset Used
| Field | Details |
|---|---|
| **Total Patients** | 29,181 ICU patients |
| **Hospitals** | Two hospitals (one surgical ICU + one mixed ICU) |
| **Total ICU Beds** | 67 |
| **CA Cases** | 242 patients |
| **Respiratory Failure Cases** | 1,231 patients |
| **Setting** | ICU — surgical and mixed |
| **Data Source** | EMR — periodic vital signs |

---

## 3. Methodology
- Used only **9 features** — no lab data required:
  - Pulse rate (HR)
  - Systolic Blood Pressure (SBP)
  - Diastolic Blood Pressure (DBP)
  - Respiratory Rate (RR)
  - SpO2
  - Body Temperature
  - Recent surgical history (within 1 week)
  - Treatment history (pharmacological or oxygen)
  - Current health status (ASA classification)
- Built **LSTM (Long Short-Term Memory)** model on time-series vital sign trajectories
- Prediction time windows tested: **1hr, 2hr, 4hr, and 6hr** before event
- Compared against MEWS and NEWS scoring systems
- Xavier initialization for weights
- Cutoff value: 0.5 for LSTM model, 5 for MEWS and NEWS

---

## 4. Results
| Time Window | FAST-PACE AUROC | MEWS AUROC | NEWS AUROC |
|---|---|---|---|
| 1 hour | 0.896 | 0.746 | 0.759 |
| 6 hours | 0.886 | — | — |

- Average sensitivity of FAST-PACE: 0.844 (vs MEWS 0.400, NEWS 0.695)
- Net reclassification improvement over MEWS: 0.507 for CA prediction
- Net reclassification improvement over NEWS: 0.412 for CA prediction
- Outperformed MEWS and NEWS across all prediction windows
- All p-values statistically significant (McNemar test p < 0.001)

---

## 5. Limitations
- ICU setting only — not validated in perioperative OR environment
- Only 9 features — potentially limits model performance (noted by other researchers)
- Single country (South Korea) — generalizability uncertain
- RR and Body Temperature included — both excluded in this thesis due to missing data in VitalDB
- Lab data excluded by design — may miss important clinical signals

---

## 6. Relevance to This Thesis

### Direct Connections
| Aspect | FAST-PACE 2019 | This Thesis |
|---|---|---|
| Dataset | 29,181 ICU patients, 2 hospitals | VitalDB — 6,388 surgical cases, 70 CA |
| Prediction window | 1hr, 2hr, 4hr, 6hr | TBD — CA-10, supervisor discussion |
| Model | LSTM | TAN (Temporal Attention Network) |
| Features | 9 basic vital signs | HR, SpO2, ETCO2, ART_MBP, ART_SBP, ART_DBP |
| Imbalance handling | Not specified | SMOTE planned |
| Lab data | Excluded by design | Not available in VitalDB anyway |
| Setting | ICU (surgical + mixed) | Perioperative OR |

### Key Takeaways for Thesis
1. **1-6hr prediction window is clinically validated** — strongest argument for shorter window in CA-10 discussion with supervisor
2. **LSTM is the established deep learning baseline** for CA prediction — TAN should be compared against LSTM
3. **Minimal feature set works** — 9 features achieved AUROC 0.896, supports your 6-feature VitalDB approach
4. **No lab data needed** — validates your VitalDB feature set which also has no lab data
5. **Perioperative setting still unexplored** — FAST-PACE used surgical ICU patients, not intraoperative — your VitalDB OR setting is a novel contribution
6. **AUROC 0.896 at 1hr window** — this is your new benchmark to beat alongside Kwon et al. 0.850

---

## 7. Citation (APA)
Kim, J., Chae, M., Chang, H. J., Kim, Y. A., & Park, E. (2019). Predicting cardiac arrest and respiratory failure using feasible artificial intelligence with simple trajectories of patient data. *Journal of Clinical Medicine, 8*(9), 1336. https://doi.org/10.3390/jcm8091336

---

*Notes by: Sachu Mon Puthenpuraickkal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
