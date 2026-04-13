# Paper 4: Kim et al. 2024 (Explainable ML for CA)

> 🔵 SUPPORTING PAPER— Explainable machine learning model for cardiac arrest prediction using SHAP-based feature attribution

---

## Metadata

| Field | Details |
|---|---|
| Title | Early Cardiac Arrest Prediction Using Explainable Machine Learning |
| Authors | Kim et al. |
| Journal | Not specified |
| Year | 2024 |
| Volume | N/A |
| DOI | N/A |
| Link | N/A |
| Read Date | Feb 2026 |
| Category | 🔵 SUPPORTING PAPER |
| Thesis Relevance | Critical — Provides explainability framework (SHAP) directly relevant for validating attention in TAN |

---

## 1. Problem Addressed

- Cardiac arrest (CA) prediction models often lack **interpretability**  
- Clinicians require **explainable predictions** for trust and adoption  
- Existing models:
  - Focus on performance but not **feature attribution**  
  - Do not provide **clinical insight into decision-making**  
- Need for models that combine:
  - High predictive performance  
  - **Transparent and explainable outputs**  

---

## 2. Dataset Used

| Field | Details |
|---|---|
| Dataset | Hospital EHR dataset (same as Paper 4) |
| Setting | ICU / Hospital |
| Population | Not specified |
| Time period | Not specified |
| Task | Cardiac arrest prediction |
| Class imbalance | Not specified |

Optional:
- Feature types (vital signs, clinical variables)

---

## 3. Methodology

### Model: Explainable Machine Learning (ML)

- Machine learning model (e.g., gradient boosting / tree-based)

- Architecture overview:
  - Feature extraction from EHR  
  - ML classifier (tree-based)  
  - SHAP-based explainability layer  

- Key components:
  - **SHAP (Shapley Additive Explanations)** for feature attribution  
  - Global and local interpretability  
  - Identification of **important physiological predictors**  

- Input features:
  - Vital signs and clinical variables  

- Prediction window:
  - Not explicitly specified  

- Training strategy:
  - Standard supervised learning  

### Baselines (if applicable)

- Compared with non-explainable ML models  

---

## 4. Results

| Model | AUROC | Other Metrics |
|---|---|---|
| Explainable ML model | N/A | Improved interpretability with competitive performance |

### Key Findings

- Provides **clinically interpretable predictions using SHAP**  
- Identifies **key features contributing to cardiac arrest risk**  
- Maintains **competitive predictive performance**  
- Enhances **trust and usability in clinical settings**  

---

## 5. Limitations

- Performance metrics (AUROC) not clearly emphasized  
- Relies on **post-hoc explainability (SHAP)** rather than intrinsic interpretability  
- No deep learning or temporal modeling  
- No external validation  
- Limited temporal dynamics modeling  

---

## 6. Relevance to This Thesis

| Aspect | Paper | This Thesis |
|---|---|---|
| Model | Explainable ML (SHAP-based) | TAN (Attention-based deep learning) |
| Data | EHR clinical data | VitalDB high-resolution signals |
| Setting | ICU / Hospital | Intraoperative OR |
| Task | Cardiac arrest prediction | Cardiac arrest prediction |

### Key Contributions to Thesis

- Provides **explainability framework (SHAP)** for validating model decisions  
- Demonstrates importance of **interpretable predictions in healthcare AI**  
- Supports use of **attention mechanisms as interpretable components**  
- Can be used to **validate TAN attention weights against SHAP importance**  

### Research Gap Addressed

- No **deep learning or temporal sequence modeling**  
- Uses **post-hoc explainability**, not integrated into model  
- No use of **high-resolution waveform data**  
- Limited ability to capture **long-term temporal dependencies**  

---

## 7. Position in Literature

| Paper | Model | Setting | Contribution |
|---|---|---|---|
| Soudan et al. 2022 | Random Forest | Hospital | Traditional ML baseline |
| Lee et al. 2022 | LGBM | ICU | HRV-based ML model |
| Kim et al. 2024 | Explainable ML | ICU | SHAP-based interpretability |
| Li et al. 2026 | TrGRU | ICU | State-of-the-art CA prediction |

---

## 8. Citation (APA)

Kim, et al. (2024). Early cardiac arrest prediction using explainable machine learning.

---

## 9. Summary (For Thesis Writing)

Kim et al. (2024) proposed an explainable machine learning model for cardiac arrest prediction using SHAP-based feature attribution, enabling clinically interpretable predictions. While the model improves transparency, it lacks temporal modeling and deep learning capabilities, supporting the use of attention-based architectures in this thesis to achieve both performance and interpretability.

---

*Notes by: Sachu Mon Puthenpuraickpal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
