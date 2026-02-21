# Paper Notes: Kim et al. 2024

> 🟡 **SUPPORTING PAPER** — Informs prediction window, baseline model choice, and imbalance handling strategy

---

## Metadata
| Field | Details |
|---|---|
| **Title** | Early Prediction of Cardiac Arrest in the Intensive Care Unit Using Explainable Machine Learning: Retrospective Study |
| **Authors** | Yun Kwan Kim, Won-Doo Seo, Sun Jung Lee, Ja Hyung Koo, Gyung Chul Kim, Hee Seok Song, Minji Lee |
| **Journal** | Journal of Medical Internet Research (JMIR) |
| **Year** | 2024 |
| **DOI** | 10.2196/62890 |
| **Link** | https://pmc.ncbi.nlm.nih.gov/articles/PMC11445627/ |
| **Citation** | Kim, Y.K., Seo, W.D., Lee, S.J. et al. Early prediction of cardiac arrest in the intensive care unit using explainable machine learning: Retrospective study. *J Med Internet Res* 26, e62890 (2024). |
| **Read Date** | Feb 21, 2026 |
| **Category** | 🟡 Supporting Paper |
| **Thesis Relevance** | ⭐⭐⭐⭐⭐ High — LGBM baseline + 24hr prediction window reference + imbalance handling strategy |

---

## 1. Problem They Solved
- Existing CA prediction models lacked generalization across different ICU subtypes (cardiac ICU vs general ICU vs surgical ICU behave differently)
- Models were black-box — clinicians could not interpret or trust predictions for real-time clinical decisions
- Validation was not patient-independent — most studies used representative event sampling, not leave-one-patient-out evaluation
- At least one abnormal sign occurs in 59.4% of patients within 1–4 hours before CA onset
- Early identification improves survival by approximately 29% within the first hour

---

## 2. Dataset Used
| Field | Details |
|---|---|
| **Primary DB** | MIMIC-IV (Medical Information Mart for Intensive Care IV) |
| **External Validation DB** | eICU-Collaborative Research Database (eICU-CRD) |
| **Study Type** | Retrospective |
| **Setting** | ICU — multiple subtypes (general, cardiac, surgical) |
| **Note** | NOT perioperative — differs from VitalDB context in this thesis |

---

## 3. Methodology
- Used **12-hour sliding window** to extract features capturing unique CA precursor patterns
- Extracted **3 types of features** per patient:
  - Raw vital signs — standard ICU monitoring signals
  - Multiresolution statistical features — mean, std, min, max over multiple time resolutions within the 12hr window
  - Gini index features — signal variability and irregularity measure
- Built **TabNet** model (tabular neural network with attention mechanism) as core architecture
- Applied **cost-sensitive learning** to handle class imbalance — assigns higher misclassification penalty to minority CA class
- Validated using **10-fold leave-one-patient-out cross-validation**
- Performed **cross-dataset validation**: trained on MIMIC-IV → tested on eICU-CRD and vice versa
- Evaluated across different ICU subtypes within each database

---

## 4. Results
- Proposed TabNet framework outperformed ALL baseline models including NEWS, SOFA, SAPS-II, LR, KNN, MLP, LGBM, RNN, and RETAIN
- Achieved superior performance across different cohort populations (MIMIC vs eICU)
- Strong cross-dataset generalization confirmed
- Decision mask from TabNet provided interpretable feature importance per individual prediction
- Global interpretation revealed clear statistical differences between CA and non-CA groups

---

## 5. Limitations
- ICU setting only — not validated in perioperative or operating room environment
- Single country datasets (US-based MIMIC and eICU) — geographic limitation
- Real-time clinical deployment not yet tested
- Heterogeneity across patient populations remains an open challenge

---

## 6. Relevance to This Thesis

### Direct Connections
| Aspect | Kim et al. 2024 | This Thesis |
|---|---|---|
| Dataset | MIMIC-IV + eICU | VitalDB (perioperative OR) |
| Prediction window | 24hr (12hr feature window) | TBD — CA-10, likely 0.5–6hr |
| Model | TabNet ensemble | TAN (Temporal Attention Network) |
| Imbalance handling | Cost-sensitive learning | SMOTE (primary) + cost-sensitive as comparison |
| Features | Vital signs + statistical multiresolution | HR, SpO2, ETCO2, ART_MBP, ART_SBP, ART_DBP |
| Interpretability | TabNet decision mask | Attention weights in TAN |
| Validation | Leave-one-patient-out | TBD |

### Key Takeaways for Thesis
1. **24-hour prediction window is the established clinical standard** — directly informs CA-10 decision
2. **Multiresolution statistical features** outperform raw vitals alone — consider adding mean, std, min, max over multiple windows in CA-14 preprocessing
3. **Cost-sensitive learning** is a valid alternative to SMOTE — worth comparing both in experiments and mentioning in methodology
4. **LGBM must be a baseline model** in thesis experiments — confirmed as standard benchmark by this paper
5. **Perioperative setting (VitalDB)** is NOT covered by this paper — this is a research gap and direct contribution angle for this thesis

---

## 7. Citation (APA)
Kim, Y. K., Seo, W. D., Lee, S. J., Koo, J. H., Kim, G. C., Song, H. S., & Lee, M. (2024). Early prediction of cardiac arrest in the intensive care unit using explainable machine learning: Retrospective study. *Journal of Medical Internet Research, 26*, e62890. https://doi.org/10.2196/62890

---

*Notes by: Sachu Mon Puthenpuraickkal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
