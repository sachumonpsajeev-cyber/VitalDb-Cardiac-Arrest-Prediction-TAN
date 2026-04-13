# Paper 3: Nie et al. 2024 (TSCAN — Temporal-Spatial Correlation Attention Network)

> 🔴 CORE PAPER — Primary architectural reference for Temporal Attention Network (TAN)

---

## Metadata

| Field | Details |
|---|---|
| Title | Temporal-Spatial Correlation Attention Network for Clinical Data Analysis in Intensive Care Unit |
| Authors | Nie W, Yu Y, Zhang C, Song D, Zhao L, Bai Y |
| Journal | IEEE Transactions on Knowledge and Data Engineering |
| Year | 2024 |
| DOI | 10.1109/TKDE.2023.3309148 |
| Links | https://ieeexplore.ieee.org/document/10234629 \| https://arxiv.org/abs/2306.01970 |
| Read Date | Feb 19, 2026 |
| Category | 🔴 Core Paper |
| Thesis Relevance | Critical — architectural foundation for TAN (temporal + spatial attention modeling) |

---

## 1. Problem Addressed

- ICU clinical data is **multivariate and temporal**, making it difficult for traditional models to capture complex dependencies  
- Existing approaches:
  - Model temporal dynamics (e.g., LSTM) OR  
  - Model feature relationships (e.g., attention)  
  - Rarely both jointly  
- Loss of **temporal–spatial interaction information** reduces predictive performance  
- Medical time-series data is:
  - Sparse  
  - Irregular  
  - Strongly correlated across features  
- No unified architecture effectively captured both:
  - Temporal evolution  
  - Inter-feature correlations  

---

## 2. Dataset Used

| Field | Details |
|---|---|
| Dataset | MIMIC-IV v0.4 |
| Source | Beth Israel Deaconess Medical Center, Boston |
| Time period | 2008–2019 |
| Raw size | 76,540 ICU stays (53,150 patients) |
| Processed | 47,046 ICU stays |
| Test split | 15% (7,057 patients, 8,906 ICU stays) |
| Mortality rate | ~15% |
| Features | 155 variables (5 categorical + 150 continuous) |

### Feature Categories

- Vital signs  
- Laboratory measurements  
- Demographics  
- Medications  
- Diagnosis codes  

---

## 3. Methodology

### Model: TSCAN (Temporal-Spatial Correlation Attention Network)

#### Architecture Overview

- **Dual-branch attention architecture:**

1. **Temporal Branch**
   - Recursive merged attention  
   - Integrates historical time steps into current representation  
   - Captures long-range temporal dependencies  

2. **Spatial Branch**
   - Inter-feature attention mechanism  
   - Learns correlations between clinical variables (e.g., BP ↔ HR ↔ SpO₂)  

3. **Fusion Encoder**
   - Combines temporal and spatial representations  
   - Produces final prediction embedding  

---

### Tasks Evaluated

- In-hospital mortality prediction  
- Length of Stay (LOS) prediction  
- Physiologic decline prediction  
- Phenotype classification  

---

### Baselines

- LSTM  
- Transformer  
- Informer  
- TimesNet  
- Other state-of-the-art time-series models  

---

### Validation

- Extensive ablation studies:
  - Removing temporal branch → performance drop  
  - Removing spatial branch → performance drop  
- Confirms both components are essential  

---

## 4. Results

| Task | TSCAN Performance | Improvement |
|---|---|---|
| In-hospital Mortality | **0.907 AUROC** | +2.0% |
| Length of Stay | **45.1%** | +2.0% |
| Physiologic Decline | Best among baselines | ✓ |
| Phenotype Classification | Best among baselines | ✓ |

### Key Findings

- Consistently outperforms all baseline models  
- Joint temporal-spatial modeling significantly improves performance  
- Attention highlights clinically meaningful features:
  - Blood pressure  
  - Heart rate  
  - Blood-related biomarkers  

---

## 5. Limitations

- Evaluated only on MIMIC-IV (no external validation)  
- Focused on general ICU tasks (mortality, LOS), not acute events like cardiac arrest  
- No perioperative or surgical context  
- No real-time/streaming deployment discussion  
- Limited generalisability (single healthcare system)  

---

## 6. Relevance to This Thesis

| Aspect | TSCAN | This Thesis (TAN) |
|---|---|---|
| Architecture | Temporal + Spatial Attention | Temporal Attention Network |
| Setting | ICU | Operating Room (OR) |
| Data | MIMIC-IV | VitalDB |
| Task | Mortality, LOS | Cardiac arrest prediction |
| Resolution | Low-frequency EHR | High-frequency waveform data |

### Key Contributions to Thesis

- Provides **direct architectural inspiration** for TAN  
- Demonstrates effectiveness of **attention-based modeling** in clinical time-series  
- Validates importance of **feature interactions (spatial attention)**  
- Supports use of **attention for interpretability**  

### Research Gap Addressed

- TSCAN does not:
  - Use high-frequency intraoperative data  
  - Address cardiac arrest prediction  
- This thesis extends:
  - Temporal attention → perioperative setting  
  - Prediction → acute intraoperative cardiac arrest  

---

## 7. Position in Literature

| Paper | Type | Setting | Contribution |
|---|---|---|---|
| LSTM / Transformer | Model | ICU | Temporal modeling |
| TSCAN (Nie et al. 2024) | Model | ICU | Temporal + spatial attention |
| Lee et al. 2024 | Model | ICU | Multimodal IHCA prediction |
| This Thesis | Model | OR | TAN for cardiac arrest prediction |

---

## 8. Citation (APA)

Nie, W., Yu, Y., Zhang, C., Song, D., Zhao, L., & Bai, Y. (2024). *Temporal-spatial correlation attention network for clinical data analysis in intensive care unit*. IEEE Transactions on Knowledge and Data Engineering. https://doi.org/10.1109/TKDE.2023.3309148

---

## 9. Summary (For Thesis Writing)

> TSCAN (Nie et al., 2024) introduces a dual-branch attention architecture that jointly models temporal dynamics and inter-feature relationships in ICU data. It demonstrates that integrating temporal and spatial attention significantly improves predictive performance. This work forms the architectural foundation for the proposed Temporal Attention Network (TAN), which extends these concepts to high-resolution intraoperative data for cardiac arrest prediction.

---

*Notes by: Sachu Mon Puthenpuraickpal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
