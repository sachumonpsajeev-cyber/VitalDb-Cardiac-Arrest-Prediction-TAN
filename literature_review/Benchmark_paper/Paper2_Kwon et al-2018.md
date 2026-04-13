# Paper 2: Kwon et al. 2018 (DEWS — Deep Learning Early Warning System)

> 🟡 BENCHMARK PAPER — Early deep learning model for in-hospital cardiac arrest prediction (AUROC 0.850 baseline)

---

## Metadata

| Field | Details |
|---|---|
| Title | An Algorithm Based on Deep Learning for Predicting In-Hospital Cardiac Arrest |
| Authors | Kwon J, Lee Y, Lee Y, Lee S, Park J |
| Journal | Journal of the American Heart Association |
| Year | 2018 |
| Volume | 7(13), e008678 |
| DOI | 10.1161/JAHA.118.008678 |
| Link | https://www.ahajournals.org/doi/10.1161/JAHA.118.008678 |
| Read Date | Feb 19, 2026 |
| Category | 🟡 Benchmark Paper |
| Thesis Relevance | High — primary baseline for IHCA prediction; AUROC target ≥ 0.850 |

---

## 1. Problem Addressed

- Traditional early warning systems (e.g., MEWS):
  - Low sensitivity  
  - High false alarm rates  
- Vital signs treated independently, ignoring interdependencies  
- Limited ability to detect early deterioration before cardiac arrest  
- Lack of deep learning approaches for IHCA prediction at the time  

---

## 2. Dataset Used

| Field | Details |
|---|---|
| Population | 52,131 patients |
| Setting | General wards (2 hospitals, South Korea) |
| Study period | June 2010 – July 2017 |
| Train split | June 2010 – Jan 2017 |
| Test split | Feb 2017 – July 2017 |
| Cardiac arrest cases | ~1,233 (≈2.3%) |
| Class imbalance | Severe (rare event prediction) |

---

## 3. Methodology

### Model: DEWS (Deep Learning Early Warning System)

- **Architecture:** Recurrent Neural Network (RNN)  
- **Input features (4 vital signs):**
  - Systolic Blood Pressure  
  - Heart Rate  
  - Respiratory Rate  
  - Body Temperature  

- **Prediction window:**  
  - 0.5 to 24 hours before cardiac arrest  

---

### Baseline Comparisons

- Modified Early Warning Score (MEWS)  
- Random Forest  
- Logistic Regression  

---

## 4. Results

| Model | AUROC | AUPRC |
|---|---|---|
| DEWS (RNN) | **0.850** | 0.044 |
| Random Forest | 0.780 | 0.014 |
| Logistic Regression | 0.613 | 0.007 |
| MEWS | 0.603 | 0.003 |

### Key Findings

- Deep learning significantly outperformed traditional models  
- Improved sensitivity while reducing false alarms  
- Demonstrated feasibility of RNN-based early warning systems  

---

## 5. Limitations

- Limited feature set (only 4 vital signs)  
- No high-resolution data (manual measurements ~3 times/day)  
- No waveform data (e.g., ECG, SpO2)  
- Severe class imbalance (~2.3% positive cases)  
- Limited interpretability (black-box model)  
- Single-country dataset (Korean population)  

---

## 6. Relevance to This Thesis

| Aspect | Kwon et al. 2018 | This Thesis |
|---|---|---|
| Model | RNN (DEWS) | TAN (Attention-based) |
| Features | 4 vital signs | Multimodal vital signals |
| Data resolution | Low-frequency (manual) | High-frequency (VitalDB) |
| Setting | General ward | Operating Room |
| Task | IHCA prediction | Intraoperative cardiac arrest |

---

### Key Contributions to Thesis

- Establishes **baseline benchmark** for cardiac arrest prediction  
- Provides target performance: **AUROC ≥ 0.850**  
- Highlights importance of:
  - Temporal modeling (via RNN)  
  - Early prediction window (0.5–24 hours)  

---

### Improvements Over Kwon et al.

- Use of **high-resolution intraoperative data (VitalDB)**  
- Inclusion of richer signals:
  - SpO2  
  - Arterial blood pressure (continuous)  
  - ETCO2  
- Advanced architecture:
  - Temporal Attention Network (TAN) vs RNN  
- Improved interpretability via attention mechanisms  

---

### Practical Insights

- Expect **class imbalance (~2–3%)** → requires:
  - SMOTE or class weighting  
- Similar prediction window can be adapted:
  - 30–240 minutes (intraoperative setting)  

---

## 7. Position in Literature

| Paper | Model | Setting | Contribution |
|---|---|---|---|
| Kwon et al. 2018 | RNN (DEWS) | Ward | First DL-based IHCA prediction |
| Lee et al. 2024 | RF + LSTM + SVM | ICU | Multimodal IHCA benchmark |
| TSCAN (2024) | Attention | ICU | Temporal-spatial modeling |
| This Thesis | TAN | OR | Intraoperative CA prediction |

---

## 8. Citation (APA)

Kwon, J., Lee, Y., Lee, Y., Lee, S., & Park, J. (2018). *An algorithm based on deep learning for predicting in-hospital cardiac arrest*. Journal of the American Heart Association, 7(13), e008678. https://doi.org/10.1161/JAHA.118.008678

---

## 9. Summary (For Thesis Writing)

> Kwon et al. (2018) introduced one of the first deep learning-based approaches for predicting in-hospital cardiac arrest using an RNN model (DEWS). The model significantly outperformed traditional early warning systems, achieving an AUROC of 0.850. Despite limitations in data resolution and feature richness, this work establishes a key baseline for cardiac arrest prediction, which the proposed TAN model aims to surpass using high-resolution intraoperative data and attention-based learning.

---

*Notes by: Sachu Mon Puthenpuraickpal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
