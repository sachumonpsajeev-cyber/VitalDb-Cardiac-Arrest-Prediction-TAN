# Paper 13: Han et al. 2020 (Nested LSTM SCD)

> 🟡 BENCHMARK PAPER — Nested LSTM architecture for sudden cardiac death risk prediction using temporal dependencies

---

## Metadata

| Field | Details |
|---|---|
| Title | Prediction of Sudden Cardiac Death Using Nested LSTM Networks |
| Authors | Han et al. |
| Journal | Not specified |
| Year | 2020 |
| Volume | N/A |
| DOI | N/A |
| Link | N/A |
| Read Date | Feb 2026 |
| Category | 🟡 |
| Thesis Relevance | High — Advanced LSTM variant (AUROC 0.890) capturing hierarchical temporal dependencies |

---

## 1. Problem Addressed

- Sudden cardiac death (SCD) prediction requires modeling **complex temporal dependencies**  
- Standard LSTM models:
  - Limited in capturing **hierarchical temporal patterns**  
  - Struggle with **long-term dependencies across multiple time scales**  
- Need for architectures that better represent **nested temporal relationships**  

---

## 2. Dataset Used

| Field | Details |
|---|---|
| Dataset | Clinical/EHR dataset (not specified) |
| Setting | Healthcare (likely ICU or cardiology cohort) |
| Population | Not specified |
| Time period | Not specified |
| Task | Sudden cardiac death prediction |
| Class imbalance | Not specified |

Optional:
- Feature types (clinical time-series data)

---

## 3. Methodology

### Model: Nested LSTM

- Extension of LSTM with **nested memory structure**

- Architecture overview:
  - Inner LSTM cells embedded within outer LSTM  
  - Hierarchical memory representation  
  - Fully connected output layer  

- Key components:
  - Captures **multi-level temporal dependencies**  
  - Inner memory handles **short-term patterns**  
  - Outer memory captures **long-term dependencies**  

- Input features:
  - Time-series clinical data  

- Prediction window:
  - Not explicitly specified  

- Training strategy:
  - Standard supervised sequence learning  

### Baselines (if applicable)

- Compared with standard LSTM and traditional models  

---

## 4. Results

| Model | AUROC | Other Metrics |
|---|---|---|
| Nested LSTM | **0.890** | N/A |

### Key Findings

- Achieves strong performance with **AUROC 0.890**  
- Outperforms standard LSTM in modeling **complex temporal dependencies**  
- Demonstrates effectiveness of **hierarchical memory structures**  
- Improves representation of **multi-scale temporal patterns**  

---

## 5. Limitations

- No attention mechanism for interpretability  
- Dataset details not clearly specified  
- No external validation  
- Limited feature diversity (not specified)  
- Focus on SCD — may differ from general cardiac arrest scenarios  

---

## 6. Relevance to This Thesis

| Aspect | Paper | This Thesis |
|---|---|---|
| Model | Nested LSTM (hierarchical RNN) | TAN (Attention-based) |
| Data | Clinical time-series | VitalDB high-resolution signals |
| Setting | Healthcare (unspecified) | Intraoperative OR |
| Task | Sudden cardiac death prediction | Cardiac arrest prediction |

### Key Contributions to Thesis

- Demonstrates importance of **capturing multi-scale temporal dependencies**  
- Provides **advanced RNN baseline (AUROC 0.890)**  
- Shows limitations of LSTM variants compared to attention models  
- Supports need for **more flexible temporal modeling (attention-based)**  

### Research Gap Addressed

- No **attention mechanism** for temporal importance  
- No use of **transformer-based architectures**  
- No **high-resolution waveform data**  
- No interpretability framework  
- Limited generalisability (no external validation)  

---

## 7. Position in Literature

| Paper | Model | Setting | Contribution |
|---|---|---|---|
| Soudan et al. 2022 | Random Forest | Hospital | Traditional ML baseline |
| Lee et al. 2022 | LGBM | ICU | HRV-based ML model |
| Han et al. 2020 | Nested LSTM | Healthcare | Hierarchical temporal modeling |
| Cho et al. 2020 | LSTM | ICU | Standard deep learning baseline |
| Li et al. 2026 | TrGRU | ICU | State-of-the-art CA prediction |

---

## 8. Citation (APA)

Han, et al. (2020). Prediction of sudden cardiac death using nested LSTM networks.

---

## 9. Summary (For Thesis Writing)

Han et al. (2020) proposed a nested LSTM architecture for sudden cardiac death prediction, achieving an AUROC of 0.890 by capturing hierarchical temporal dependencies. While improving upon standard LSTM models, the absence of attention mechanisms and interpretability highlights the need for more flexible temporal modeling approaches such as the attention-based TAN used in this thesis.

---

*Notes by: Sachu Mon Puthenpuraickpal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
