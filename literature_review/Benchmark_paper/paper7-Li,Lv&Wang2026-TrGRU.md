# Paper 7: Li et al. 2026 (TrGRU)

> 🟡 BENCHMARK PAPER — Hybrid Transformer-GRU model achieving state-of-the-art performance for cardiac arrest prediction

---

## Metadata

| Field | Details |
|---|---|
| Title | Early Prediction of Cardiac Arrest Based on Time-Series Vital Signs Using Deep Learning: Retrospective Study |
| Authors | Y. Li, L. Lv, X. Wang |
| Journal | JMIR Formative Research |
| Year | 2026 |
| Volume | 10 |
| DOI | 10.2196/78484 |
| Link | https://formative.jmir.org/2026/1/e78484 |
| Read Date | 22 Feb 2026 |
| Category | 🟡 BENCHMARK PAPER |
| Thesis Relevance | Critical — Current SOTA model with AUROC 0.957, primary benchmark target for this thesis |

---

## 1. Problem Addressed

- Existing cardiac arrest (CA) prediction models:
  - Low sensitivity and high false alarm rates  
- Lack of **hybrid Transformer + recurrent architectures** for CA prediction  
- Limited **real-time prediction capability**  
- Poor **cross-dataset generalisation**  
- Many models require **large feature sets** not available in all clinical settings  

---

## 2. Dataset Used

| Field | Details |
|---|---|
| Dataset | MIMIC-III (primary) + eICU-CRD (external) |
| Setting | ICU |
| Population | 4,063 patients (MIMIC-III), multicenter ICU (eICU) |
| Time period | Not specified |
| Task | Cardiac arrest prediction |
| Class imbalance | Balanced via sampling techniques |

Optional:
- Feature types (6 vital signs: HR, RR, SBP, DBP, MAP, SpO₂)

---

## 3. Methodology

### Model: TrGRU

- Hybrid deep learning architecture combining **Transformer + GRU**

- Architecture overview:
  - 3 Transformer encoder layers  
  - 2 GRU layers  
  - Global Average Pooling  
  - Fully connected output layer  

- Key components:
  - Transformer captures **long-range temporal dependencies**  
  - GRU captures **sequential dynamics**  

- Input features:
  - 6 vital signs  
  - Statistical features (mean, median, min, max, SD over 2-hour window)  

- Prediction window:
  - Input: 2 hours  
  - Output: Predict CA within next 1 hour (5-min intervals)

- Training strategy:
  - Oversampling (positive class)  
  - Undersampling (negative class)  
  - Meta-learning for cross-dataset adaptation  

### Baselines (if applicable)

- Logistic Regression  
- XGBoost  
- LightGBM  
- Random Forest  

---

## 4. Results

| Model | AUROC | Other Metrics |
|---|---|---|
| TrGRU (MIMIC-III) | **0.957** | Accuracy: 0.904, Sensitivity: 0.859, Specificity: 0.933, AUPRC: **0.949** |
| TrGRU (eICU External) | **0.920** | Sensitivity: 0.813, AUPRC: 0.848 |

### Key Findings

- Achieves **state-of-the-art AUROC (0.957)** for CA prediction  
- Maintains strong performance on external dataset (**AUROC 0.920**)  
- **Statistical features outperform raw signals**  
- Sensitivity improves closer to event:
  - 30 min: **90.6%**  
  - 20 min: **92.6%**  
  - 10 min: **94.8%**  

---

## 5. Limitations

- Uses only **6 vital signs** — limited feature richness  
- No use of **high-resolution waveform data**  
- Not validated on **perioperative (OR) data**  
- Limited interpretability — no attention or feature attribution analysis  
- Disease heterogeneity in CA not addressed  

---

## 6. Relevance to This Thesis

| Aspect | Paper | This Thesis |
|---|---|---|
| Model | Transformer + GRU (TrGRU) | TAN (Temporal Attention Network) |
| Data | MIMIC-III + eICU | VitalDB |
| Setting | ICU | Intraoperative OR |
| Task | Cardiac arrest prediction | Cardiac arrest prediction |

### Key Contributions to Thesis

- Establishes **current SOTA benchmark (AUROC 0.957)**  
- Demonstrates effectiveness of **hybrid Transformer-based temporal modeling**  
- Validates **cross-dataset generalisation strategy**  
- Provides strong **baseline for performance comparison**  

### Research Gap Addressed

- Limited to **low-dimensional vital sign inputs (6 features)**  
- No use of **high-resolution waveform data (VitalDB advantage)**  
- No **interpretability mechanism**  
- No **perioperative patient population**  
- Does not explore **longer prediction horizons beyond ICU setting**  

---

## 7. Position in Literature

| Paper | Model | Setting | Contribution |
|---|---|---|---|
| Kwon et al. 2018 | RNN | ICU | Early CA prediction baseline |
| FAST-PACE 2019 | LSTM | ICU | High-performance deep learning model |
| Li et al. 2026 | TrGRU | ICU | State-of-the-art CA prediction (AUROC 0.957) |
| Kapral et al. 2024 | TFT | OR | Transformer-based intraoperative prediction |

---

## 8. Citation (APA)

Li, Y., Lv, L., & Wang, X. (2026). Early prediction of cardiac arrest based on time-series vital signs using deep learning: Retrospective study. *JMIR Formative Research, 10*, e78484. https://doi.org/10.2196/78484

---

## 9. Summary (For Thesis Writing)

Li et al. (2026) proposed TrGRU, a hybrid Transformer-GRU model for early cardiac arrest prediction, achieving state-of-the-art performance with an AUROC of 0.957 on MIMIC-III and strong external validation on eICU. Despite high accuracy, the model relies on limited vital sign inputs and lacks interpretability, highlighting opportunities for improvement using high-resolution data and attention-based architectures in this thesis.

---

*Notes by: Sachu Mon Puthenpuraickpal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
