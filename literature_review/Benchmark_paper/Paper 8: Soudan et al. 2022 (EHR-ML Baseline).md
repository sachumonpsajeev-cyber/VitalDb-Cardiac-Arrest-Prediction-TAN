# Paper 8: Soudan et al. 2022 (EHR-ML Baseline)

> 🟡 BENCHMARK PAPER — Traditional machine learning comparison for cardiac arrest prediction using EHR vital signs

---

## Metadata

| Field | Details |
|---|---|
| Title | Attempting cardiac arrest prediction using artificial intelligence on vital signs from Electronic Health Records |
| Authors | B. Soudan, F.F. Dandachi, A. Bou Nassif |
| Journal | Smart Health |
| Year | 2022 |
| Volume | 26 |
| DOI | 10.1016/j.smhl.2022.100352 |
| Link | https://www.sciencedirect.com/science/article/abs/pii/S2352648322000290 |
| Read Date | 21 Feb 2026 |
| Category | 🟡 BENCHMARK PAPER |
| Thesis Relevance | Medium — Provides traditional ML baseline and validates importance of vital signs for CA prediction |

---

## 1. Problem Addressed

- Lack of systematic comparison of AI models for cardiac arrest (CA) prediction using EHR vital signs  
- Clinical need for **early warning systems** prior to cardiac arrest  
- Uncertainty regarding:
  - Optimal **model choice**  
  - Most informative **vital signs**  
  - Best **prediction time window**  

---

## 2. Dataset Used

| Field | Details |
|---|---|
| Dataset | Hospital Electronic Health Records (EHR) |
| Setting | Hospital (general ward/ICU not specified) |
| Population | Not specified |
| Time period | Not specified |
| Task | Cardiac arrest prediction |
| Class imbalance | Not specified |

Optional:
- Feature types (routine vital signs)

---

## 3. Methodology

### Model: Traditional Machine Learning Models

- Compared **six AI algorithms**:
  - Random Forest  
  - Logistic Regression  
  - Support Vector Machine (SVM)  
  - Decision Tree  
  - K-Nearest Neighbors (KNN)  
  - Neural Network  

- Approach:
  - Evaluated multiple **time windows (1–12 hours before event)**  
  - Tested different **vital sign combinations**  
  - Identified optimal **model + feature + time window**  

- Input features:
  - Routine EHR vital signs  

- Prediction window:
  - 1–12 hours prior to cardiac arrest  

### Baselines (if applicable)

- Internal comparison among six ML models  

---

## 4. Results

| Model | AUROC | Other Metrics |
|---|---|---|
| Random Forest (best) | N/A | **Accuracy: >80%** |

### Key Findings

- **Random Forest** achieved the best performance (>80% accuracy)  
- Optimal prediction window: **last 60 minutes before event**  
- Shorter windows significantly improve performance:
  - ~**+10% accuracy gain** compared to longer windows  
- Confirms **recent vital sign trends are most predictive**  

---

## 5. Limitations

- Limited to **traditional ML models** — no deep learning approaches  
- Uses only **EHR vital signs** — no high-resolution waveform data  
- No **external validation dataset**  
- Reports **accuracy only** — AUROC not provided  
- Limited dataset detail (population, imbalance not specified)  

---

## 6. Relevance to This Thesis

| Aspect | Paper | This Thesis |
|---|---|---|
| Model | Traditional ML (Random Forest best) | TAN (Deep learning, attention-based) |
| Data | EHR vital signs | VitalDB high-resolution signals |
| Setting | Hospital (unspecified) | Intraoperative OR |
| Task | Cardiac arrest prediction | Cardiac arrest prediction |

### Key Contributions to Thesis

- Establishes that **vital signs alone contain sufficient predictive signal**  
- Identifies **60-minute window as highly predictive**, supporting temporal modeling design  
- Provides **baseline ML benchmark** for comparison with deep learning models  
- Demonstrates transition from **traditional ML → deep learning approaches**  

### Research Gap Addressed

- Does not use **deep learning or temporal attention mechanisms**  
- No use of **high-resolution waveform data (VitalDB advantage)**  
- Lacks **interpretability and temporal modeling depth**  
- No **external validation**  
- Limited evaluation metrics (no AUROC/AUPRC)  

---

## 7. Position in Literature

| Paper | Model | Setting | Contribution |
|---|---|---|---|
| Soudan et al. 2022 | Random Forest | Hospital | Traditional ML baseline for CA prediction |
| Kwon et al. 2018 | RNN | ICU | Early deep learning CA model |
| FAST-PACE 2019 | LSTM | ICU | Improved deep learning performance |
| Li et al. 2026 | TrGRU | ICU | State-of-the-art CA prediction |

---

## 8. Citation (APA)

Soudan, B., Dandachi, F. F., & Bou Nassif, A. (2022). Attempting cardiac arrest prediction using artificial intelligence on vital signs from electronic health records. *Smart Health, 26*, 100352. https://doi.org/10.1016/j.smhl.2022.100352

---

## 9. Summary (For Thesis Writing)

Soudan et al. (2022) conducted a comparative study of traditional machine learning models for cardiac arrest prediction using EHR vital signs, identifying Random Forest as the best-performing model and highlighting the importance of short-term temporal windows. While effective, the study is limited by the absence of deep learning methods and advanced temporal modeling, motivating the need for attention-based architectures in this thesis.

---

*Notes by: Sachu Mon Puthenpuraickpal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
