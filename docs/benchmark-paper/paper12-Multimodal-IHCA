# Paper 12: Lee et al. 2024 (RF+LSTM+SVM — Multimodal IHCA)

> 🟡 **BENCHMARK PAPER** — Multimodal stacked ensemble RF+LSTM+SVM for in-hospital cardiac arrest prediction — AUROC 0.91 at 1 hour before CA — MIMIC-IV + eICU external validation

---

## Metadata
| Field | Details |
|---|---|
| **Title** | Prediction of In-Hospital Cardiac Arrest in the Intensive Care Unit: Machine Learning–Based Multimodal Approach |
| **Authors** | Hsin-Ying Lee, Po-Chih Kuo, Frank Qian, Chien-Hung Li, Jiun-Ruey Hu, Wan-Ting Hsu, Hong-Jie Jhou, Po-Huang Chen, Cho-Hao Lee, Chin-Hua Su, Po-Chun Liao, I-Ju Wu, Chien-Chang Lee |
| **Institution** | National Taiwan University, National Tsing Hua University, Boston Medical Center, Yale School of Medicine, Harvard T.H. Chan School of Public Health |
| **Journal** | JMIR Medical Informatics |
| **Year** | 2024 |
| **Volume** | Volume 12, Article e49142 |
| **DOI** | 10.2196/49142 |
| **Full Text** | https://medinform.jmir.org/2024/1/e49142 |
| **PMC** | https://pmc.ncbi.nlm.nih.gov/articles/PMC11287234/ |
| **PubMed** | https://pubmed.ncbi.nlm.nih.gov/39051152/ |
| **Citation** | Lee HY, Kuo PC, Qian F, et al. Prediction of in-hospital cardiac arrest in the intensive care unit: machine learning–based multimodal approach. *JMIR Med Inform*. 2024;12:e49142. doi:10.2196/49142 |
| **Read Date** | Feb 24, 2026 |
| **Category** | 🟡 Benchmark Paper |
| **Thesis Relevance** | ⭐⭐⭐⭐⭐ High — directly predicts IHCA using same vital signs (HR, SpO2, BP), AUROC 0.91 at 1hr before CA is your new highest benchmark target, multimodal RF+LSTM comparable to TAN |

---

## 1. Problem They Solved
- Early identification of impending in-hospital cardiac arrest (IHCA) improves clinical outcomes but is elusive for clinicians
- Existing models used either **static baseline features** (demographics, comorbidities) OR **temporal vital signs** — never combined both effectively
- No validated multimodal model combined structured EHR data with time-series vital signs for IHCA prediction
- High false alarm rates and poor generalisability limited clinical adoption of existing models

---

## 2. Dataset Used
| Field | Details |
|---|---|
| **Primary Dataset** | MIMIC-IV — 23,909 patients |
| **IHCA cases (MIMIC-IV)** | 452 patients |
| **Control (MIMIC-IV)** | 23,457 patients |
| **External Validation 1** | eICU-CRD — 10,049 patients (85 IHCA) |
| **External Validation 2** | National Taiwan University Hospital |
| **Setting** | ICU — critically ill patients |
| **Prediction horizon** | Up to 13 hours before CA event |
| **Features** | Patient demographics, comorbidities, presenting illness (RF) + vital signs time series (LSTM) |

---

## 3. Methodology

### Three-Stage Stacked Ensemble Architecture:

**Stage 1 — Random Forest (RF)**
- Input: Baseline features — patient demographics, presenting illness, comorbidities
- Output: Probability score from static patient profile
- AUROC: 0.80 (standalone)

**Stage 2 — LSTM**
- Input: Vital signs time series — HR, SpO2, BP, RR, Temperature
- Output: Temporal probability score from vital sign trajectory
- AUROC: standalone lower than stacked model

**Stage 3 — SVM Stacking**
- Input: RF + LSTM probability scores combined
- Output: Final IHCA prediction
- AUROC: **0.91** at 1 hour before CA (highest)
- AUROC
