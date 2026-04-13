# Paper 13: Chen et al. 2022 (Systematic Review on CA Prediction)

> 🔵 SUPPORTING PAPER — Systematic review and meta-analysis of machine learning approaches for cardiac arrest prediction, focusing on model performance trends and research gaps

---

## Metadata

| Field | Details |
|---|---|
| Title | Machine Learning for Cardiac Arrest Prediction: A Systematic Review and Meta-Analysis |
| Authors | Chen et al. |
| Journal | Not specified |
| Year | 2022 |
| Volume | N/A |
| DOI | N/A |
| Link | N/A |
| Read Date | Feb 2026 |
| Category | 🔵 |
| Thesis Relevance | High — Provides global benchmarking trends, identifies methodological gaps, and validates direction of deep learning and temporal models |

---

## 1. Problem Addressed

- Rapid growth of machine learning models for cardiac arrest (CA) prediction created **fragmented research landscape**  
- Lack of unified comparison across:
  - Model types (ML vs DL)  
  - Datasets  
  - Feature sets  
  - Evaluation metrics  
- Unclear **state-of-the-art performance ceiling** and methodological limitations  
- Need for **systematic synthesis of CA prediction literature**

---

## 2. Dataset Used

| Field | Details |
|---|---|
| Dataset | Aggregated from multiple studies |
| Setting | ICU, Hospital, EHR, mixed clinical environments |
| Population | Varies across studies |
| Time period | Varies across studies |
| Task | Cardiac arrest prediction |
| Class imbalance | Common issue across reviewed studies |

Optional:
- Includes studies using MIMIC, eICU, hospital EHRs, and waveform datasets

---

## 3. Methodology

### Study Type: Systematic Review + Meta-Analysis

- Reviewed published studies on CA prediction using ML/DL  
- Categorized models into:
  - Traditional ML (RF, SVM, LGBM)  
  - Deep learning (LSTM, GRU, CNN, Transformers)  

- Evaluated:
  - Dataset types  
  - Feature engineering approaches  
  - Prediction horizons  
  - Model performance metrics  

- Synthesized performance trends across studies  

---

## 4. Results

| Category | Findings |
|---|---|
| Best performing models | Deep learning models (LSTM/Transformer variants) |
| Typical AUROC range | ~0.80 to 0.95 across studies |
| Strongest predictors | Vital signs (HR, BP, SpO₂), temporal trends |
| Best performing trend | Hybrid temporal models outperform static ML |

### Key Findings

- Deep learning models consistently outperform traditional ML  
- Temporal modeling significantly improves predictive performance  
- Feature engineering remains important in many high-performing ML models  
- External validation is rare across CA prediction studies  
- Interpretability is underexplored in most high-performing models  

---

## 5. Limitations

- Heterogeneity across datasets limits direct comparability  
- Publication bias may affect reported performance  
- Lack of standardized evaluation protocols  
- Many included studies lack external validation  
- Limited focus on real-time deployment feasibility  

---

## 6. Relevance to This Thesis

| Aspect | Paper | This Thesis |
|---|---|---|
| Scope | Global CA prediction literature | Single high-resolution dataset (VitalDB) |
| Model types | ML + DL review | TAN (attention-based DL) |
| Focus | Benchmarking + gaps | Model development + evaluation |

### Key Contributions to Thesis

- Confirms **deep learning > traditional ML trend** in CA prediction  
- Highlights importance of **temporal modeling (LSTM/Transformer dominance)**  
- Identifies major gap: **lack of interpretability in high-performing models**  
- Supports need for **external validation and real-world datasets (VitalDB relevance)**  
- Justifies transition from ML → attention-based architectures in this thesis  

### Research Gap Addressed

- No unified standard for CA prediction evaluation  
- Limited interpretability in state-of-the-art models  
- Lack of perioperative (OR) dataset focus  
- Insufficient use of high-resolution waveform data  
- Poor external validation practices across literature  

---

## 7. Position in Literature

| Paper | Type | Contribution |
|---|---|---|
| Soudan et al. 2022 | ML study | Traditional baseline |
| FAST-PACE 2020 | LSTM model | Temporal DL baseline |
| Li et al. 2026 | TrGRU | SOTA performance benchmark |
| Chen et al. 2022 | Systematic review | Global synthesis + gap identification |

---

## 8. Citation (APA)

Chen, et al. (2022). Machine learning for cardiac arrest prediction: A systematic review and meta-analysis.

---

## 9. Summary (For Thesis Writing)

Chen et al. (2022) systematically reviewed machine learning approaches for cardiac arrest prediction and demonstrated that deep learning models consistently outperform traditional methods, particularly those incorporating temporal modeling. The study highlights key limitations in the field, including poor interpretability and lack of external validation, thereby motivating the development of attention-based models such as the TAN proposed in this thesis.

---

*Notes by: Sachu Mon Puthenpuraickpal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
