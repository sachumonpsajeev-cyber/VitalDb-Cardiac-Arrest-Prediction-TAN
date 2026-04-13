# Paper 11: Kapral et al. 2024 (TFT-VitalDB)

> 🟡 BENCHMARK PAPER — Temporal Fusion Transformer for intraoperative blood pressure forecasting with external validation on VitalDB

---

## Metadata

| Field | Details |
|---|---|
| Title | Development and External Validation of Temporal Fusion Transformer Models for Continuous Intraoperative Blood Pressure Forecasting |
| Authors | Lorenz Kapral, Christoph Dibiasi, Natasa Jeremic, Stefan Bartos, Sybille Behrens, Aylin Bilir, Clemens Heitzinger, Oliver Kimberger |
| Journal | eClinicalMedicine |
| Year | 2024 |
| Volume | 75 |
| DOI | 10.1016/j.eclinm.2024.102797 |
| Link | https://www.thelancet.com/journals/eclinm/article/PIIS2589-5370(24)00376-6/fulltext |
| Read Date | Feb 24, 2026 |
| Category | 🟡 |
| Thesis Relevance | Critical — Uses VitalDB for external validation and transformer-based temporal modeling directly comparable to TAN |

---

## 1. Problem Addressed

- Intraoperative hypotension (IOH) is associated with increased postoperative morbidity  
- Existing models:
  - Focus on **single-point prediction**, not temporal trajectories  
  - Often rely on **high-resolution waveform data** not widely available  
- Lack of models that:
  - Predict **multi-step blood pressure evolution**  
  - Provide **interpretable temporal insights**  
- Need for clinically deployable models using **low-resolution data**

---

## 2. Dataset Used

| Field | Details |
|---|---|
| Dataset | Vienna General Hospital (primary) + VitalDB (external) |
| Setting | Operating Room (Intraoperative) |
| Population | 73,009 patients (primary), 6,388 patients (VitalDB) |
| Time period | 2017–2020 |
| Task | Continuous BP forecasting + hypotension classification |
| Class imbalance | Present (hypotension relatively rare) |

Optional:
- Feature types (vitals, demographics, ventilation, medication)

---

## 3. Methodology

### Model: Temporal Fusion Transformer (TFT)

- Transformer-based architecture for **multi-horizon time-series forecasting**
- Predicts **blood pressure trajectory up to 7 minutes ahead**
- Outputs **28-step MAP sequence (15-second intervals)**

- Key components:
  - Gated residual networks (feature selection)
  - Temporal attention mechanism
  - Static + time-varying feature integration

- Input features:
  - Vital signs
  - Demographics
  - Ventilation and medication data

- Prediction window:
  - 7 minutes ahead

### Baselines (if applicable)

- Compared with prior single-point MAP prediction models (e.g., Lee et al.)

---

## 4. Results

| Model | AUROC | Other Metrics |
|---|---|---|
| TFT (Internal) | N/A | **MAE: 4 mmHg** |
| TFT (External VitalDB) | N/A | **MAE: 7 mmHg** |

### Key Findings

- Achieves **clinically acceptable prediction error (4–7 mmHg)**  
- Outperforms prior single-value BP prediction models  
- Successfully generalises to external **VitalDB dataset**  
- Enables **multi-step trajectory prediction** instead of single-point estimation  

---

## 5. Limitations

- Focuses on **hypotension prediction**, not cardiac arrest  
- **AUROC not primary metric**, limiting direct comparison with classification models  
- Uses **low-resolution data (15s)** despite availability of higher resolution signals  
- Not trained on VitalDB — only externally validated  
- Limited feature set (excludes SpO₂, ETCO₂)  
- Short prediction horizon (7 minutes)

---

## 6. Relevance to This Thesis

| Aspect | Paper | This Thesis |
|---|---|---|
| Model | TFT (Transformer-based) | TAN (Temporal Attention Network) |
| Data | VitalDB (external validation) | VitalDB (primary dataset) |
| Setting | Intraoperative OR | Intraoperative OR |
| Task | Hypotension prediction | Cardiac arrest prediction |

### Key Contributions to Thesis

- Demonstrates effectiveness of **transformer-based temporal models** in intraoperative data  
- Validates **VitalDB as a generalisable dataset across institutions**  
- Shows **attention mechanisms improve interpretability**, supporting TAN design  
- Provides a **real-world OR benchmark** for comparison  

### Research Gap Addressed

- Does not address **cardiac arrest prediction**  
- Limited to **short-term forecasting (7 min)**  
- Uses **low-resolution signals only**  
- Focuses on **regression task**, not event prediction  

---

## 7. Position in Literature

| Paper | Model | Setting | Contribution |
|---|---|---|---|
| Kwon et al. 2018 | RNN | ICU | Early cardiac arrest prediction |
| FAST-PACE 2019 | LSTM | ICU | High-performance deep learning model |
| Lee et al. 2023 | LGBM | ICU | Tabular baseline |
| Kapral et al. 2024 | TFT | OR | Transformer-based BP forecasting with external validation |

---

## 8. Citation (APA)

Kapral, L., Dibiasi, C., Jeremic, N., Bartos, S., Behrens, S., Bilir, A., Heitzinger, C., & Kimberger, O. (2024). Development and external validation of temporal fusion transformer models for continuous intraoperative blood pressure forecasting. *eClinicalMedicine, 75*, 102797. https://doi.org/10.1016/j.eclinm.2024.102797

---

## 9. Summary (For Thesis Writing)

Kapral et al. (2024) developed a Temporal Fusion Transformer for multi-step intraoperative blood pressure forecasting, achieving accurate predictions and demonstrating strong generalisability through external validation on VitalDB. Although focused on hypotension and short-term prediction, the study highlights the effectiveness of transformer-based temporal models in perioperative settings, supporting the use of attention-based architectures in this thesis.

---

*Notes by: Sachu Mon Puthenpuraickpal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
