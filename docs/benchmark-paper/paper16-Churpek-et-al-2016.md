# Paper 16: Churpek et al. 2016 (eCART — ML for Cardiac Arrest Prediction)

> 🔴 **BENCH MARK PAPER** — Multicenter machine learning comparison for predicting cardiac arrest and clinical deterioration on hospital wards — establishes eCART as the gold-standard traditional ML benchmark — directly comparable to this thesis

---

## Metadata
| Field | Details |
|---|---|
| **Title** | Multicenter Comparison of Machine Learning Methods and Conventional Regression for Predicting Clinical Deterioration on the Wards |
| **Authors** | Matthew M. Churpek, Trevor C. Yuen, Christopher Winslow, David O. Meltzer, Michael W. Kattan, Dana P. Edelson |
| **Institution** | Department of Medicine, University of Chicago, Chicago, IL |
| **Journal** | Critical Care Medicine |
| **Year** | 2016 |
| **Volume** | Vol. 44, No. 2, pp. 368–374 |
| **DOI** | 10.1097/CCM.0000000000001571 |
| **PubMed** | https://pubmed.ncbi.nlm.nih.gov/26771782/ |
| **Citation** | Churpek MM, Yuen TC, Winslow C, Meltzer DO, Kattan MW, Edelson DP. Multicenter comparison of machine learning methods and conventional regression for predicting clinical deterioration on the wards. *Crit Care Med*. 2016;44(2):368–374. doi:10.1097/CCM.0000000000001571 |
| **Read Date** | Mar 4, 2026 |
| **Category** | 🔴 Benchmark Paper |
| **Thesis Relevance** | ⭐⭐⭐⭐⭐ Critical — directly predicts cardiac arrest using vital signs + EHR data, establishes eCART as the leading traditional ML baseline, used as benchmark in Section 2.2 and results comparison table |

---

## 1. Problem They Solved
- Ward patients experiencing cardiac arrest (CA), ICU transfer, or death are often not identified early enough
- Existing early warning scores (MEWS, NEWS) were rule-based and built on expert opinion — not data-driven
- No large-scale multicenter comparison of machine learning vs conventional regression existed for CA prediction
- Clinical need: accurate, real-time risk stratification of general ward patients using routinely available EHR data

---

## 2. Dataset Used
| Field | Details |
|---|---|
| **Setting** | Five US hospitals (urban tertiary, suburban teaching, community) |
| **Period** | November 2008 – January 2013 |
| **Patient Admissions** | 269,999 (from the broader eCART dataset) |
| **Cardiac Arrests** | 424 confirmed ward cardiac arrests |
| **ICU Transfers** | 13,188 |
| **Deaths** | 2,840 |
| **Features** | Vital signs, laboratory values, demographics — 33 time-varying EHR parameters |
| **Split** | First 60% for derivation, remaining 40% for validation (per hospital) |
| **Note** | General hospital wards — NOT operating room / intraoperative setting |

---

## 3. Methodology
- Compared multiple ML methods: **random forest, gradient boosting, neural networks, logistic regression** (conventional)
- Used **discrete-time survival analysis** framework to handle time-varying predictors
- Combined outcome: cardiac arrest OR ICU transfer OR death on the wards
- Used 33 EHR parameters including vital signs (HR, RR, BP, SpO2, temperature) + lab values + demographics
- Model updated in real-time as new observations arrived
- Compared all methods to MEWS as the existing clinical standard
- eCART score derived from logistic regression coefficients — continuously scored per patient

---

## 4. Results
| Model | AUROC (CA) | AUROC (Combined) | vs MEWS |
|---|---|---|---|
| **eCART (Logistic Regression)** | **0.83** | **0.77** | +0.13 AUROC improvement |
| Random Forest | Higher than LR | — | Best ML method |
| Gradient Boosting | Similar to RF | — | — |
| MEWS (Baseline) | 0.71 | 0.70 | Reference |
| NEWS | 0.76 | — | — |

- Random forest and gradient boosting **outperformed conventional logistic regression**
- eCART significantly outperformed MEWS across all five hospitals and all outcomes
- NRI = 0.28 — 19% of CA patients reclassified into more appropriate risk group

---

## 5. Limitations
- **Hospital wards only** — NOT intraoperative / operating room setting — key gap this thesis addresses
- Uses 33 parameters including lab values — not all available in real-time OR monitoring
- No temporal sequence modelling — no attention mechanism
- No fixed prediction window (30/60/120/240 min) — reactive rather than proactive prediction
- Does not use ETCO2 — a key intraoperative vital sign used in this thesis
- General inpatient population — CA rate and clinical context differ from surgical OR patients

---

## 6. Relevance to This Thesis

### Direct Connections
| Aspect | Churpek et al. 2016 (eCART) | This Thesis |
|---|---|---|
| Outcome | Cardiac arrest + ICU transfer + death | Cardiac arrest only (binary) |
| Setting | General hospital wards | Intraoperative surgical OR |
| Dataset | 5-hospital EHR, 269,999 admissions | VitalDB, 6,388 patients |
| Features | 33 EHR variables (vitals + labs + demographics) | 6 intraoperative vitals only |
| Model | Logistic regression / ML comparison | TAN — Temporal Attention Network |
| Temporal modelling | Discrete-time survival (no attention) | Attention-based temporal sequence |
| Prediction window | Real-time threshold (no fixed window) | 30 / 60 / 120 / 240 min |
| AUROC (CA) | 0.83 | Target: ≥ 0.91 |
| Imbalance handling | Not explicitly addressed | SMOTE-ENN |

### Key Takeaways for Thesis
1. **Primary baseline** — eCART AUROC 0.83 is the key traditional ML benchmark to beat in results
2. **MEWS/NEWS comparison** — eCART already outperforms MEWS (0.83 vs 0.71) — your TAN must exceed both
3. **Ward vs OR gap** — entire dataset is ward-based, confirming NO intraoperative CA prediction model exists — core novelty argument
4. **Feature limitation** — 33 parameters required vs only 6 vitals in your thesis — leaner and more OR-deployable
5. **No temporal attention** — eCART uses point-in-time LR; your TAN captures temporal dynamics — architectural superiority argument
6. **Cite in Chapter 2.2** — Traditional ML approaches section + Chapter 4 results comparison table

---

## 7. Benchmarks Summary (Updated — Paper 16 Added)
| Paper | Model | AUROC (CA) | Window | Setting | Dataset |
|---|---|---|---|---|---|
| **Churpek et al. 2016** | **eCART (LR + ML)** | **0.83** | **Real-time** | **Ward** | **5-hospital EHR** |
| Kwon et al. 2018 | RNN | 0.850 | 8 hr | ICU | Custom |
| FAST-PACE 2019 | LSTM | 0.896 | 1–6 hr | ICU | Custom |
| Lee et al. 2023 | LGBM | 0.881 | 0.5–24 hr | ICU | SNUH |
| TFT 2024 (Kapral) | TFT | N/A (MAE) | 7 min | OR | VitalDB |
| Wei et al. 2025 | Meta-analysis | 0.90 (pooled) | — | Mixed | Systematic review |
| **This Thesis (TAN)** | **TAN** | **Target ≥ 0.91** | **30–240 min** | **OR** | **VitalDB** |

> **Beat order: MEWS (0.71) → eCART (0.83) → Kwon (0.85) → Lee (0.881) → FAST-PACE (0.896) → Target ≥ 0.91**

---

## 8.  Citation (APA)
Churpek, M. M., Yuen, T. C., Winslow, C., Meltzer, D. O., Kattan, M. W., & Edelson, D. P. (2016). Multicenter comparison of machine learning methods and conventional regression for predicting clinical deterioration on the wards. *Critical Care Medicine, 44*(2), 368–374. https://doi.org/10.1097/CCM.0000000000001571

---

*Notes by: Sachu Mon Puthenpuraickkal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
