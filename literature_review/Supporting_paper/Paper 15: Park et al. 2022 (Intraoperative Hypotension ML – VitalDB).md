# Paper 15: Park et al. 2022 (Intraoperative Hypotension ML – VitalDB)

> 🔵 SUPPORTING PAPER — Machine learning pipeline for intraoperative hypotension prediction using VitalDB with emphasis on preprocessing and feature engineering

---

## Metadata

| Field | Details |
|---|---|
| Title | Machine Learning Approach for Prediction of Intraoperative Hypotension Using VitalDB |
| Authors | Park et al. |
| Journal | Not specified |
| Year | 2022 |
| Volume | N/A |
| DOI | N/A |
| Link | N/A |
| Read Date | Feb 2026 |
| Category | 🔵 |
| Thesis Relevance | High — Directly uses VitalDB and provides preprocessing + feature engineering pipeline relevant for this thesis |

---

## 1. Problem Addressed

- Intraoperative hypotension (IOH) is a major risk factor for postoperative complications  
- Lack of standardized **ML pipelines for IOH prediction using VitalDB data**  
- Existing approaches suffer from:
  - inconsistent preprocessing  
  - poor feature engineering strategies  
  - limited reproducibility  

- Need for a structured ML pipeline using **real intraoperative data**

---

## 2. Dataset Used

| Field | Details |
|---|---|
| Dataset | :contentReference[oaicite:0]{index=0} |
| Setting | Operating Room (Intraoperative) |
| Population | Surgical patients (VitalDB cohort) |
| Time period | Not specified |
| Task | Intraoperative hypotension prediction |
| Class imbalance | Present (hypotension events relatively rare) |

Optional:
- Features derived from arterial pressure, heart rate, and other physiological waveforms  

---

## 3. Methodology

### Model: Traditional ML Pipeline

- Machine learning-based approach with strong emphasis on **data preprocessing**

- Pipeline steps:
  - Signal cleaning and artifact removal  
  - Normalization of physiological signals  
  - Sliding window segmentation  
  - Feature extraction  

- Key feature engineering:
  - Mean arterial pressure trends  
  - Heart rate variability features  
  - Statistical descriptors (mean, SD, min, max)  
  - Temporal trend features  

- Models used:
  - Traditional ML classifiers (exact model not specified in summary; typically RF / LGBM / SVM in similar studies)

- Prediction window:
  - Short-term intraoperative prediction (window not explicitly defined)

---

## 4. Results

| Model | AUROC | Other Metrics |
|---|---|---|
| Best ML model | N/A | Improved prediction performance over baseline rules |

### Key Findings

- Feature engineering significantly improves ML performance  
- VitalDB is a **robust dataset for intraoperative ML modeling**  
- Structured preprocessing pipeline is critical for reproducibility  
- Statistical + temporal features outperform raw signal usage  

---

## 5. Limitations

- No deep learning or end-to-end temporal modeling  
- Limited or unspecified model benchmarking details  
- No external validation beyond VitalDB  
- Performance metrics (AUROC) not clearly standardized  
- Heavy reliance on manual feature engineering  

---

## 6. Relevance to This Thesis

| Aspect | Paper | This Thesis |
|---|---|---|
| Dataset | :contentReference[oaicite:1]{index=1} | VitalDB |
| Task | Intraoperative hypotension | Cardiac arrest prediction |
| Approach | Feature engineering + ML | End-to-end deep learning (TAN) |
| Focus | Preprocessing pipeline | Temporal attention modeling |

### Key Contributions to Thesis

- Provides a **structured preprocessing pipeline for VitalDB data**  
- Confirms importance of **feature engineering for physiological signals**  
- Demonstrates feasibility of ML on intraoperative waveform data  
- Supports justification for moving from:
  - manual feature engineering → **end-to-end deep learning (TAN)**  
- Helps validate **VitalDB as a reliable intraoperative dataset**

### Research Gap Addressed

- No deep learning or attention-based modeling  
- No automatic feature learning (manual engineering only)  
- Limited generalisation beyond VitalDB  
- No long-horizon temporal modeling  
- No interpretability framework beyond feature importance  

---

## 7. Position in Literature

| Paper | Model | Setting | Contribution |
|---|---|---|---|
| Park et al. 2022 | ML pipeline | OR | Feature engineering + preprocessing for VitalDB |
| Lee et al. 2022 | LGBM | ICU | HRV-based ML baseline |
| FAST-PACE 2020 | LSTM | ICU | Temporal deep learning baseline |
| Li et al. 2026 | TrGRU | ICU | SOTA CA prediction |

---

## 8. Citation (APA)

Park, et al. (2022). Machine learning approach for prediction of intraoperative hypotension using VitalDB.

---

## 9. Summary (For Thesis Writing)

Park et al. (2022) proposed a machine learning pipeline for intraoperative hypotension prediction using VitalDB, emphasizing preprocessing and feature engineering of physiological signals. While the study demonstrates the importance of structured data preparation, it lacks deep learning and temporal modeling, highlighting the need for end-to-end attention-based approaches such as the TAN developed in this thesis.

---

*Notes by: Sachu Mon Puthenpuraickkal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
