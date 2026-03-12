# Paper 11: Kapral et al. 2024 (TFT-VitalDB)

> 🟡 **BENCHMARK PAPER** — Temporal Fusion Transformer for intraoperative blood pressure prediction — uses VitalDB for external validation — same dataset as this thesis

---

## Metadata
| Field | Details |
|---|---|
| **Title** | Development and External Validation of Temporal Fusion Transformer Models for Continuous Intraoperative Blood Pressure Forecasting |
| **Authors** | Lorenz Kapral, Christoph Dibiasi, Natasa Jeremic, Stefan Bartos, Sybille Behrens, Aylin Bilir, Clemens Heitzinger, Oliver Kimberger |
| **Institution** | Medical University of Vienna, Department of Anaesthesia, Intensive Care Medicine and Pain Medicine, Vienna, Austria |
| **Journal** | eClinicalMedicine (The Lancet) |
| **Year** | 2024 |
| **Volume** | Volume 75, Article 102797 |
| **DOI** | 10.1016/j.eclinm.2024.102797 |
| **Full Text** | https://www.thelancet.com/journals/eclinm/article/PIIS2589-5370(24)00376-6/fulltext |
| **PMC** | https://pmc.ncbi.nlm.nih.gov/articles/PMC11402414/ |
| **PubMed** | https://pubmed.ncbi.nlm.nih.gov/39281101/ |
| **PDF** | https://repositorium.meduniwien.ac.at/obvumwoa/content/titleinfo/10438796/full.pdf |
| **Citation** | Kapral L, Dibiasi C, Jeremic N, et al. Development and external validation of temporal fusion transformer models for continuous intraoperative blood pressure forecasting. *eClinicalMedicine*. 2024;75:102797. doi:10.1016/j.eclinm.2024.102797 |
| **Read Date** | Feb 24, 2026 |
| **Category** | 🟡 Benchmark Paper |
| **Thesis Relevance** | ⭐⭐⭐⭐⭐ Critical — uses VitalDB (same 6,388 patients) for external validation, Temporal Fusion Transformer directly comparable to TAN architecture, intraoperative setting identical to this thesis |

---

## 1. Problem They Solved
- Intraoperative hypotension (IOH) is associated with postoperative morbidity and should be avoided during surgery
- Existing prediction models relied on **high-resolution waveform data** — often unavailable in real clinical settings
- No model could **forecast continuous blood pressure trajectories** multiple time points ahead — only single-value predictions existed
- Standard deep learning models lacked **interpretability** in the operating room context

---

## 2. Dataset Used
| Field | Details |
|---|---|
| **Primary Dataset** | General Hospital of Vienna, Austria |
| **Patients** | 73,009 patients undergoing general anaesthesia for non-cardiothoracic surgery |
| **Period** | January 1, 2017 — December 30, 2020 |
| **Resolution** | Low-resolution — sampled every 15 seconds |
| **Features** | Patient demographics, vital signs, medication, ventilation data |
| **Internal Test Set** | n = 8,113 patients |
| **External Validation** | VitalDB — 6,388 patients, Seoul National University Hospital |
| **External Test Set** | n = 5,065 patients from VitalDB |
| **Note** | VitalDB used as external validation — SAME dataset as this thesis |

---

## 3. Methodology
- Used **Temporal Fusion Transformer (TFT)** — a multi-horizon time series forecasting architecture
- Predicts **intraoperative blood pressure trajectories 7 minutes in advance**
- Predicts an entire **curve of 28 different MAP values** — not just a single point prediction
- Low-resolution input (15s sampling) — more practical than high-resolution waveform models
- Binary hypotension prediction: MAP < 65 mmHg threshold
- Evaluated on both:
  - **Continuous prediction** — MSE and MAE metrics
  - **Binary classification** — hypotension yes/no (AUROC)
- External validation on VitalDB confirms generalisability across institutions and countries

---

## 4. Results
| Metric | Internal Test Set | External (VitalDB) |
|---|---|---|
| **MAE (MAP prediction)** | 4 mmHg (0.376 SD) | 7 mmHg (0.622 SD) |
| **Task** | Continuous BP forecasting | Continuous BP forecasting |
| **Binary hypotension** | Evaluated (MAP < 65 mmHg) | Evaluated |
| **Outperforms** | Lee et al. single MAP model (MAE 7 mmHg) | — |
| **Key advantage** | Predicts 28-point trajectory vs single value | Validated on VitalDB |

---

## 5. Limitations
- Task is **hypotension prediction** not cardiac arrest — different clinical endpoint
- Primary metric is **MAE** for continuous prediction — AUROC not primary focus
- Low-resolution data (15s) — VitalDB has higher resolution available
- **Not trained on VitalDB** — only externally validated — direct comparison limited
- Does not use SpO2, ETCO2 — limited vital sign set compared to this thesis
- Perioperative setting matches but clinical question differs

---

## 6. Relevance to This Thesis

### Direct Connections
| Aspect | Kapral et al. 2024 (TFT) | This Thesis |
|---|---|---|
| Dataset | VitalDB external validation (6,388 patients) | VitalDB primary dataset (6,388 patients) |
| Setting | Intraoperative surgical OR | Intraoperative surgical OR |
| Architecture | Temporal Fusion Transformer (TFT) | TAN — Temporal Attention Network |
| Input | Vital signs + demographics | HR, SpO2, ETCO2, ART_MBP, ART_SBP, ART_DBP |
| Prediction window | 7 minutes ahead | 30–240 minute windows |
| Output | Continuous BP trajectory + binary hypotension | Binary: cardiac arrest yes/no |
| Resolution | 15 seconds | High resolution (VitalDB native) |
| Interpretability | TFT attention weights | TAN attention weights |

### Key Takeaways for Thesis
1. **VitalDB validated externally** — confirms VitalDB generalises beyond Seoul, strengthens your dataset choice argument
2. **TFT architecture** — transformer-based temporal model on intraoperative data, directly comparable to your TAN model
3. **Low-resolution data works** — 15s sampling sufficient for intraoperative prediction, supports your sliding window approach
4. **Intraoperative OR setting confirmed** — validates that deep learning works in perioperative context — your thesis builds directly on this
5. **28-point trajectory vs binary CA** — your thesis solves a harder, higher-stakes problem (CA prediction vs hypotension forecasting)
6. **Cite in Chapter 2 (Related Work)** — use as evidence that transformer-based models work on VitalDB intraoperative data

---

## 7. Benchmarks Summary (Updated)
| Paper | Model | AUROC | Window | Setting | Dataset |
|---|---|---|---|---|---|
| Kwon et al. 2018 | RNN | 0.850 | 8hr | ICU | Custom |
| FAST-PACE 2019 | LSTM | 0.896 | 1–6hr | ICU | Custom |
| Lee et al. 2023 | LGBM | 0.881 | 0.5–24hr | ICU | SNUH |
| TA-RNN 2024 | TA-RNN | N/A (F2) | Per visit | EHR | ADNI/MIMIC |
| **TFT 2024** | **TFT** | **N/A (MAE)** | **7 min** | **OR** | **VitalDB** |

> Your TAN model target: **AUROC > 0.896** to beat best existing benchmark

---

## 8. Citation (APA)
Kapral, L., Dibiasi, C., Jeremic, N., Bartos, S., Behrens, S., Bilir, A., Heitzinger, C., & Kimberger, O. (2024). Development and external validation of temporal fusion transformer models for continuous intraoperative blood pressure forecasting. *eClinicalMedicine, 75*, 102797. https://doi.org/10.1016/j.eclinm.2024.102797

---

*Notes by: Sachu Mon Puthenpuraickpal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
