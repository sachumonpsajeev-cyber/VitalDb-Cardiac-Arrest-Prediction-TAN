# Paper Notes: An et al. 2022 (TERTIAN)

> 🔴 **CORE PAPER** — Time-aware transformer + hierarchical attention network for ICU clinical prediction — direct architectural foundation for TAN model

---

## Metadata
| Field | Details |
|---|---|
| **Title** | TERTIAN: Clinical Endpoint Prediction in ICU via Time-Aware Transformer-Based Hierarchical Attention Network |
| **Authors** | Ying An, Yang Liu, Xianlai Chen, Yu Sheng |
| **Institution** | Big Data Institute & School of Computer Science, Central South University, Changsha, China |
| **Journal** | Computational Intelligence and Neuroscience (Hindawi / Wiley) |
| **Year** | 2022 |
| **DOI** | 10.1155/2022/4207940 |
| **PMC** | https://pmc.ncbi.nlm.nih.gov/articles/PMC9788893/ |
| **Free Full Text** | https://onlinelibrary.wiley.com/doi/10.1155/2022/4207940 |
| **PubMed** | https://pubmed.ncbi.nlm.nih.gov/36567811/ |
| **Citation** | An Y, Liu Y, Chen X, Sheng Y. TERTIAN: Clinical Endpoint Prediction in ICU via Time-Aware Transformer-Based Hierarchical Attention Network. *Computational Intelligence and Neuroscience*. 2022;2022:4207940. doi:10.1155/2022/4207940 |
| **Read Date** | Feb 24, 2026 |
| **Category** | 🔴 Core Paper |
| **Thesis Relevance** | ⭐⭐⭐⭐⭐ Critical — direct architectural blueprint for TAN model, solves identical problems of irregular time series + multivariate vital signs in ICU |

---

## 1. Problem They Solved
- Standard deep learning models assume **regular time intervals** between clinical measurements — not true in ICU EMR data
- Existing models fail to capture **interrelationships between different types of clinical data** (vital signs, lab tests, prescriptions)
- Traditional ICU scoring systems (APACHE, SAPS) consider only **current snapshots** — ignore temporality of patient records
- No unified framework existed for **heterogeneous multivariate irregular time series** clinical prediction

---

## 2. Dataset Used
| Field | Details |
|---|---|
| **Primary Dataset** | MIMIC-III — Medical Information Mart for Intensive Care III |
| **Secondary Dataset** | MIMIC-IV — validation and comparison |
| **Task** | ICU mortality prediction |
| **Input Window** | First 48 hours since ICU admission |
| **Data Types** | Vital signs (Xr), Laboratory tests (Xl), Prescription information (M) |
| **Setting** | ICU — critically ill patients |

---

## 3. Methodology

### Three-Component Architecture:

**Component 1 — Heterogeneous Event Representation Module**
- Separate deep learning encoders for each data type:
  - Vital signs → Time-aware Transformer
  - Lab tests → Time-aware Transformer
  - Prescriptions → Embedding layer
- Each encoder captures unique temporal patterns of its data type

**Component 2 — Hierarchical Feature Fusion Module**
- Layer-by-layer fusion of different data types
- Uses hierarchical attention to weight interactions between:
  - Clinical examinations (lab tests + vital signs)
  - Treatment data (prescriptions)
- Captures potential interactions between data types for comprehensive patient representation

**Component 3 — Mortality Prediction Module**
- Final patient embedding fed into prediction layer
- Binary classification: mortality yes/no

### Time-Aware Transformer Key Mechanism:
- Encodes **irregular time intervals** between clinical events directly into transformer attention
- Models **personalised temporal patterns** — different patients have different disease progression speeds
- Avoids information loss caused by assuming fixed time steps

---

## 4. Results
| Metric | MIMIC-III | MIMIC-IV |
|---|---|---|
| **AUROC** | Outperforms all SOTA baselines | Outperforms all SOTA baselines |
| **Comparison** | Superior to standard RNN, LSTM, Transformer, and attention baselines |
| **Ablation** | Time-aware transformer component shown critical — removing it degrades performance significantly |
| **Fusion method** | Hierarchical fusion outperforms simple concatenation and early/late fusion alternatives |

> Note: Exact AUROC values vary with hyperparameter settings — optimal vector dimension found through grid search; AUC shows inverted-U curve with increasing dimension

---

## 5. Limitations
- Validated only on **MIMIC-III and MIMIC-IV** — not perioperative or surgical data
- Task is **ICU mortality** not cardiac arrest — requires adaptation for CA prediction
- **48-hour window** from admission — longer than ideal for intraoperative CA prediction
- No external validation on non-MIMIC datasets
- Prescription data used as input — not available in VitalDB intraoperative setting

---

## 6. Relevance to This Thesis

### Direct Connections
| Aspect | TERTIAN 2022 | This Thesis |
|---|---|---|
| Core problem | Irregular time intervals in ICU vital signs | Irregular vital sign sampling in VitalDB OR |
| Architecture | Time-aware Transformer + Hierarchical Attention | TAN — Temporal Attention Network |
| Input data | Vital signs + lab tests + prescriptions | HR, SpO2, ETCO2, ART_MBP, ART_SBP, ART_DBP |
| Time handling | Time-aware transformer encoding Δt | Sliding window + temporal encoding |
| Attention | Hierarchical — feature + visit level | Feature-level attention for vital sign importance |
| Dataset | MIMIC-III / MIMIC-IV ICU | VitalDB perioperative OR |
| Output | Binary: mortality yes/no | Binary: cardiac arrest yes/no |
| Setting | ICU post-admission | Intraoperative surgical |

### Key Takeaways for Thesis
1. **TERTIAN is your TAN blueprint** — time-aware transformer + hierarchical attention = exact components of your proposed model
2. **Irregular time series is the core problem** — TERTIAN validates that standard transformers fail without time-awareness, directly justifying your TAN design
3. **Hierarchical attention = interpretability** — maps directly to feature-level attention for HR, SpO2, ETCO2, ART_MBP in your model
4. **Vital signs as primary input confirmed** — TERTIAN uses same vital sign types available in VitalDB
5. **Heterogeneous data fusion** — TERTIAN's multimodal approach can inspire future extension of your model beyond 6 vital signs
6. **ICU to OR gap** — TERTIAN validated in ICU; your thesis fills the perioperative surgical gap — a novel contribution
7. **Cite in Chapter 3 (Methodology)** — use TERTIAN as the primary architectural reference for your TAN design decisions

---

## 7. Benchmarks Summary (Updated)
| Paper | Model | AUROC | Window | Setting |
|---|---|---|---|---|
| Kwon et al. 2018 (DEWS) | RNN | 0.850 | 8hr | ICU |
| FAST-PACE 2019 | LSTM | 0.896 | 1–6hr | ICU |
| Lee et al. 2023 (HRV-LGBM) | LGBM | 0.881 | 0.5–24hr | ICU |
| TA-RNN 2024 | TA-RNN | N/A (F2) | Per visit | EHR/ICU |
| TERTIAN 2022 | Transformer+Attention | SOTA on MIMIC | 48hr | ICU |

> Your TAN model target: **AUROC > 0.896** to beat best existing benchmark

---

## 8. Citation (APA)
An, Y., Liu, Y., Chen, X., & Sheng, Y. (2022). TERTIAN: Clinical endpoint prediction in ICU via time-aware transformer-based hierarchical attention network. *Computational Intelligence and Neuroscience, 2022*, 4207940. https://doi.org/10.1155/2022/4207940

---

*Notes by: Sachu Mon Puthenpuraickpal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
