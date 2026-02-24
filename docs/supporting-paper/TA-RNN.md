# Paper 8: Al Olaimat & Bozdag 2024 (TA-RNN)

> 🟢 **SUPPORTING PAPER** — Time-aware RNN with dual attention for irregular EHR data — architectural foundation for TAN model

---

## Metadata
| Field | Details |
|---|---|
| **Title** | TA-RNN: An Attention-Based Time-Aware Recurrent Neural Network Architecture for Electronic Health Records |
| **Authors** | Mohammad Al Olaimat, Serdar Bozdag (for the Alzheimer's Disease Neuroimaging Initiative) |
| **Journal** | Bioinformatics (Oxford Academic) |
| **Year** | 2024 |
| **Volume** | Volume 40, Supplement 1, Pages i169–i179 |
| **DOI** | 10.1093/bioinformatics/btae264 |
| **arXiv** | https://arxiv.org/abs/2401.14694 |
| **PDF** | https://arxiv.org/pdf/2401.14694 |
| **PMC** | https://pmc.ncbi.nlm.nih.gov/articles/PMC11211851/ |
| **GitHub** | https://github.com/bozdaglab/TA-RNN |
| **Citation** | Al Olaimat M, Bozdag S; Alzheimer's Disease Neuroimaging Initiative. TA-RNN: an attention-based time-aware recurrent neural network architecture for electronic health records. *Bioinformatics*. 2024;40(Suppl 1):i169–i179. doi:10.1093/bioinformatics/btae264 |
| **Read Date** | Feb 24, 2026 |
| **Category** | 🟢 Supporting Paper |
| **Thesis Relevance** | ⭐⭐⭐⭐⭐ High — direct architectural inspiration for TAN model, solves same irregular time interval problem present in VitalDB intraoperative data |

---

## 1. Problem They Solved
- Standard RNN/LSTM models assume **regular time intervals** between data points — not true in real EHR data
- Clinical visits are **irregular** — fixed time step models fail to capture temporal dynamics accurately
- Most deep learning models for EHR are **not interpretable** — no way to understand which features drive predictions
- No existing architecture addressed both irregularity and interpretability together in a single unified framework

---

## 2. Dataset Used
| Field | Details |
|---|---|
| **Primary Dataset** | ADNI — Alzheimer's Disease Neuroimaging Initiative |
| **Secondary Dataset** | NACC — National Alzheimer's Coordinating Center |
| **Validation Dataset** | MIMIC-III — ICU mortality prediction |
| **Task** | MCI to Alzheimer's Disease conversion prediction |
| **Features** | 19 clinical and cognitive features per visit (CDRSB, MMSE, RAVLT.learning, FAQ, neuroimaging, demographics) |
| **Visits** | Up to 6 longitudinal visits per patient |
| **Note** | Architecture is dataset-agnostic — validated on both AD and ICU mortality tasks |

---

## 3. Methodology
- Proposed two architectures:
  - **TA-RNN** — predicts clinical outcome at the **next visit**
  - **TA-RNN-AE** (Autoencoder variant) — predicts outcomes **multiple visits ahead**
- Three-component architecture:
  1. **Time Embedding Layer** — encodes elapsed time Δt between visits as embeddings, directly fed into RNN to modulate hidden state updates
  2. **Attention-Based RNN** — dual-level attention mechanism:
     - *Visit-level attention*: assigns weights (0–1, sum = 1) across all visits — model learns which visits matter most
     - *Feature-level attention*: generates 19 attention weights per visit — one per clinical feature — identifies most influential features per prediction
  3. **Prediction Layer** — Multi-Layer Perceptron (MLP) trained on patient embedding + demographic data for final binary classification
- Statistical validation: t-test for significance between TA-RNN and baselines; F2 score and sensitivity used as primary metrics (not AUROC)

---

## 4. Results
| Metric | Value |
|---|---|
| **Primary Metric** | F2 Score + Sensitivity (not AUROC — AD conversion task) |
| **Performance** | Outperformed all baseline and SOTA methods in almost all experimental setups |
| **Datasets** | Superior on ADNI, NACC (AD conversion) and MIMIC-III (ICU mortality) |
| **AUROC** | Not reported as primary metric for this paper |
| **Most Important Features** | CDRSB, MMSE, RAVLT.learning, FAQ — consistent with clinical literature |
| **Visit-Level Finding** | Model prioritises **5th and 6th (final) visits** — most recent data carries highest predictive weight |

---

## 5. Limitations
- Validated on **Alzheimer's disease** dataset — not cardiac arrest or perioperative data
- Feature set (cognitive + neuroimaging) differs entirely from VitalDB vital signs — requires adaptation
- No AUROC reported — cannot directly compare to Kwon (0.850), FAST-PACE (0.896), HRV-LGBM (0.881) benchmarks
- Irregular visit intervals in ADNI are months apart — VitalDB irregularity is at seconds/minutes scale — different temporal granularity
- Single institution training — ADNI is multisite but controlled, less noisy than OR environment

---

## 6. Relevance to This Thesis

### Direct Connections
| Aspect | Al Olaimat & Bozdag 2024 (TA-RNN) | This Thesis |
|---|---|---|
| Problem | Irregular time intervals in EHR visits | Irregular vital sign sampling in VitalDB OR data |
| Architecture | Time-aware RNN + dual attention | TAN — Temporal Attention Network |
| Time handling | Time embedding layer (Δt between visits) | Sliding window with temporal encoding |
| Interpretability | Visit-level + feature-level attention weights | Feature importance for HR, SpO2, ETCO2, ART_MBP |
| Dataset | ADNI (AD), MIMIC-III (ICU mortality) | VitalDB (perioperative CA prediction) |
| Output | Binary: AD conversion yes/no | Binary: Cardiac arrest yes/no |
| Code available | Yes — github.com/bozdaglab/TA-RNN | To be developed |

### Key Takeaways for Thesis
1. **Time embedding is the key innovation** — directly applicable to VitalDB where vital signs are recorded at irregular intervals during surgery
2. **Dual attention = interpretability** — visit-level → window-level attention, feature-level → vital sign importance for CA prediction
3. **Recent data carries more weight** — model found final visits most predictive, directly supports shorter prediction windows for CA (30–60 min)
4. **Architecture generalises to ICU** — MIMIC-III mortality validation confirms applicability to critical care settings
5. **Open source code available** — TA-RNN GitHub can be used as starting codebase and adapted for TAN development
6. **Methodological justification** — citing TA-RNN directly justifies your time-aware + attention design choices in thesis Chapter 3

---

## 7. Benchmarks Summary (Updated)
| Paper | Model | AUROC | Window | Setting |
|---|---|---|---|---|
| Kwon et al. 2018 (DEWS) | RNN | 0.850 | 8hr | ICU |
| FAST-PACE 2019 | LSTM | 0.896 | 1–6hr | ICU |
| Lee et al. 2023 (HRV-LGBM) | LGBM | 0.881 | 0.5–24hr | ICU |
| TA-RNN 2024 | TA-RNN | N/A (F2) | Per visit | EHR/ICU |

> Your TAN model target: **AUROC > 0.896** to beat best existing benchmark

---

## 8. Citation (APA)
Al Olaimat, M., & Bozdag, S. (2024). TA-RNN: An attention-based time-aware recurrent neural network architecture for electronic health records. *Bioinformatics, 40*(Supplement 1), i169–i179. https://doi.org/10.1093/bioinformatics/btae264

---

*Notes by: Sachu Mon Puthenpuraickpal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
