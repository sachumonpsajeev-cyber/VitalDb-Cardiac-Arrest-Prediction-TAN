# Paper 9: Al Olaimat et al. 2024 (TA-RNN)

> 🔵 SUPPORTING PAPER — Time-aware attention-based RNN for handling irregularly sampled EHR time-series data

---

## Metadata

| Field | Details |
|---|---|
| Title | TA-RNN: Attention-Based Time-Aware Recurrent Neural Network for Electronic Health Records |
| Authors | Al Olaimat et al. |
| Journal | Not specified |
| Year | 2024 |
| Volume | N/A |
| DOI | N/A |
| Link | N/A |
| Read Date | Feb 2026 |
| Category | 🔵 |
| Thesis Relevance | High — Provides time-aware attention mechanism for irregular temporal data, directly relevant for temporal modeling in TAN |

---

## 1. Problem Addressed

- EHR data is **irregularly sampled** with missing and uneven time intervals  
- Standard RNNs assume **uniform time steps**, leading to information loss  
- Existing models fail to:
  - Capture **temporal gaps explicitly**  
  - Model **time-dependent feature importance**  
- Need for models that incorporate **time-awareness into attention mechanisms**  

---

## 2. Dataset Used

| Field | Details |
|---|---|
| Dataset | EHR dataset (not specified) |
| Setting | Healthcare (EHR-based) |
| Population | Not specified |
| Time period | Not specified |
| Task | Clinical event prediction (general) |
| Class imbalance | Not specified |

Optional:
- Feature types (EHR time-series data with irregular intervals)

---

## 3. Methodology

### Model: Time-Aware Attention RNN (TA-RNN)

- RNN-based architecture enhanced with **time-aware attention mechanism**

- Architecture overview:
  - Recurrent neural network backbone  
  - Time-aware attention layer  
  - Output prediction layer  

- Key components:
  - **Time decay function** to model irregular intervals  
  - **Attention weights adjusted by time gaps**  
  - Captures both:
    - Temporal sequence patterns  
    - Time interval importance  

- Input features:
  - EHR time-series data with timestamps  

- Prediction window:
  - Not explicitly specified  

### Baselines (if applicable)

- Compared with standard RNN-based models (non-time-aware)

---

## 4. Results

| Model | AUROC | Other Metrics |
|---|---|---|
| TA-RNN | N/A | Improved performance over standard RNNs |

### Key Findings

- Time-aware attention improves modeling of **irregular time intervals**  
- Outperforms standard RNNs lacking temporal awareness  
- Better captures **clinical temporal dynamics in EHR data**  

---

## 5. Limitations

- Dataset and evaluation details not clearly specified  
- No comparison with **transformer-based architectures**  
- No external validation reported  
- Limited interpretability beyond attention weights  
- Not applied specifically to cardiac arrest prediction  

---

## 6. Relevance to This Thesis

| Aspect | Paper | This Thesis |
|---|---|---|
| Model | Time-aware RNN + attention | TAN (Temporal Attention Network) |
| Data | Irregular EHR time-series | VitalDB (high-resolution time-series) |
| Setting | EHR (general clinical) | Intraoperative OR |
| Task | General prediction | Cardiac arrest prediction |

### Key Contributions to Thesis

- Introduces **time-aware attention mechanism**, relevant for temporal modeling  
- Highlights importance of **handling irregular sampling in clinical data**  
- Supports use of **attention for temporal importance weighting**  
- Provides conceptual foundation for **temporal attention design in TAN**  

### Research Gap Addressed

- Does not use **transformer or advanced attention architectures**  
- No use of **high-resolution waveform data**  
- Not validated on **cardiac arrest prediction task**  
- Does not explore **long prediction horizons**  
- Limited evaluation and benchmarking  

---

## 7. Position in Literature

| Paper | Model | Setting | Contribution |
|---|---|---|---|
| Soudan et al. 2022 | Random Forest | Hospital | Traditional ML baseline |
| Kwon et al. 2018 | RNN | ICU | Early deep learning model |
| Al Olaimat et al. 2024 | TA-RNN | EHR | Time-aware attention for irregular data |
| Li et al. 2026 | TrGRU | ICU | State-of-the-art CA prediction |

---

## 8. Citation (APA)

Al Olaimat, et al. (2024). TA-RNN: Attention-based time-aware recurrent neural network for electronic health records.

---

## 9. Summary (For Thesis Writing)

Al Olaimat et al. (2024) proposed TA-RNN, a time-aware attention-based recurrent neural network designed to handle irregularly sampled EHR data by incorporating temporal gaps into the attention mechanism. The study highlights the importance of time-aware modeling in clinical time-series, providing a conceptual foundation for attention-based temporal architectures used in this thesis.

---

*Notes by: Sachu Mon Puthenpuraickpal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
