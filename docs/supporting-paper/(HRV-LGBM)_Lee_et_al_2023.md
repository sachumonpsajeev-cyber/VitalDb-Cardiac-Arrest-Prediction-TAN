# Paper Notes: Lee et al. 2023 (HRV-LGBM)

> 🟡 **SUPPORTING PAPER** — Real-time CA prediction using HRV + LGBM, 0.5–24hr window reference, ECG feature importance

---

## Metadata
| Field | Details |
|---|---|
| **Title** | Real-time Machine Learning Model to Predict In-Hospital Cardiac Arrest Using Heart Rate Variability in ICU |
| **Authors** | Hyeonhoon Lee, Hyun-Lim Yang, Ho Geol Ryu, Chul-Woo Jung, Youn Joung Cho, Soo Bin Yoon, Hyun-Kyu Yoon, Hyung-Chul Lee |
| **Journal** | npj Digital Medicine |
| **Year** | 2023 |
| **DOI** | 10.1038/s41746-023-00960-2 |
| **Link** | https://pmc.ncbi.nlm.nih.gov/articles/PMC10665411/ |
| **GitHub** | https://github.com/HyeonhoonLee/hrvarrest |
| **Citation** | Lee, H., Yang, H.L., Ryu, H.G. et al. Real-time machine learning model to predict in-hospital cardiac arrest using heart rate variability in ICU. *npj Digital Medicine, 6*, 215 (2023). |
| **Read Date** | Feb 21, 2026 |
| **Category** | 🟡 Supporting Paper |
| **Thesis Relevance** | ⭐⭐⭐⭐⭐ High — LGBM with HRV features + 0.5–24hr prediction window + real-time framework + same hospital as VitalDB (Seoul National University Hospital) |

---

## 1. Problem They Solved
- Existing CA prediction models used static snapshots of patient data — not real-time
- Standard vital sign models ignored the rich temporal information in ECG signals
- No validated real-time model existed using HRV measures alone for ICU CA prediction
- HRV captures autonomic nervous system dysfunction which precedes cardiac events — an underutilized signal for CA prediction

---

## 2. Dataset Used
| Field | Details |
|---|---|
| **Hospital** | Seoul National University Hospital, Seoul, South Korea |
| **Setting** | ICU |
| **Signal** | ECG — continuous monitoring |
| **HRV Epoch** | 5-minute epochs |
| **Features** | 33 HRV measures (time domain, frequency domain, nonlinear) |
| **Note** | SAME hospital as VitalDB dataset — strong institutional connection |

---

## 3. Methodology
- Extracted **33 HRV measures** from 5-minute ECG epochs including:
  - Time domain: MeanNN, SDNN, RMSSD, pNN50, pNN20, IQRNN, MedianNN
  - Frequency domain: LFn (normalized low frequency)
  - Nonlinear: TINN (triangular interpolation), HTI (HRV triangular index), IALS, PAS, PIP, Porta's Index
- Used **LightGBM (LGBM)** as prediction model
- Prediction window: **0.5 to 24 hours** before CA event
- Real-time framework: model updates predictions continuously as new ECG data arrives
- Validated using robust statistical testing — DeLong's test for AUROC comparison, Kendall's tau for time-to-event association

---

## 4. Results
| Metric | Value |
|---|---|
| **AUROC** | 0.881 (95% CI: 0.875–0.887) |
| **AUPRC** | 0.104 (95% CI: 0.093–0.116) |
| **Most Important Feature** | TINN — baseline width of triangular interpolation of RR interval histogram |

- Significantly outperformed traditional clinical parameter-based model (AUROC 0.735, p < 0.001)
- Real-time prediction framework validated across 0.5–24hr windows
- HRV nonlinear measures showed strongest predictive value

---

## 5. Limitations
- ICU setting only — not validated in perioperative OR environment
- Requires continuous ECG signal — may not always be available at high quality
- HRV features require clean RR interval extraction — noise sensitive
- AUPRC of 0.104 is low — reflects severe class imbalance challenge
- Single hospital — limited geographic generalizability

---

## 6. Relevance to This Thesis

### Direct Connections
| Aspect | Lee et al. 2023 (HRV-LGBM) | This Thesis |
|---|---|---|
| Dataset | Seoul National University Hospital ICU | VitalDB — same hospital, surgical OR |
| Prediction window | 0.5–24 hours | TBD — CA-10, supervisor discussion |
| Model | LightGBM | TAN (Temporal Attention Network) |
| Features | 33 HRV measures from ECG | HR, SpO2, ETCO2, ART_MBP, ART_SBP, ART_DBP |
| Real-time | Yes — continuous updates | Sliding window approach |
| Imbalance | Not specified | SMOTE planned |
| Setting | ICU | Perioperative OR |

### Key Takeaways for Thesis
1. **Same hospital as VitalDB** — institutional context is directly comparable, strengthens your thesis argument
2. **0.5–24hr prediction window validated** — supports shorter window choice for CA-10 discussion
3. **AUROC 0.881 is your new benchmark** — alongside Kwon (0.850) and FAST-PACE (0.896)
4. **HRV features are powerful** — VitalDB has ECG at 500Hz, consider adding HRV features in CA-14 as advanced step
5. **LGBM confirmed again as strong baseline** — three papers now confirm LGBM as the standard ML benchmark
6. **Nonlinear HRV measures** (TINN, HTI) outperformed simple time-domain features — temporal attention in TAN should capture similar nonlinear patterns
7. **Perioperative OR setting** still unexplored — your thesis fills this gap directly

---

## 7. Benchmarks Summary (Updated)
| Paper | Model | AUROC | Window |
|---|---|---|---|
| Kwon et al. 2018 (DEWS) | RNN | 0.850 | 8hr |
| FAST-PACE 2019 | LSTM | 0.896 | 1–6hr |
| Lee et al. 2023 (HRV-LGBM) | LGBM | 0.881 | 0.5–24hr |

> Your TAN model target: **AUROC > 0.896** to beat best existing benchmark

---

## 8. Citation (APA)
Lee, H., Yang, H. L., Ryu, H. G., Jung, C. W., Cho, Y. J., Yoon, S. B., Yoon, H. K., & Lee, H. C. (2023). Real-time machine learning model to predict in-hospital cardiac arrest using heart rate variability in ICU. *npj Digital Medicine, 6*, 215. https://doi.org/10.1038/s41746-023-00960-2

---

*Notes by: Sachu Mon Puthenpuraickkal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
