# Paper 5: Cho et al. 2020 (FAST-PACE)

> 🟡 BENCHMARK PAPER — LSTM-based model using simple vital sign trajectories for early cardiac arrest prediction

---

## Metadata

| Field | Details |
|---|---|
| Title | Prediction of cardiac arrest using simple vital sign trajectories (FAST-PACE) |
| Authors | Cho et al. |
| Journal | Not specified |
| Year | 2020 |
| Volume | N/A |
| DOI | N/A |
| Link | N/A |
| Read Date | Feb 2026 |
| Category | 🟡 BENCHMARK PAPER |
| Thesis Relevance | High — Strong LSTM baseline with AUROC 0.896, widely cited benchmark for CA prediction |

---

## 1. Problem Addressed

- Early prediction of cardiac arrest (CA) remains challenging in clinical settings  
- Existing models:
  - Use **complex feature engineering**  
  - Require **large numbers of variables**  
- Need for a model that:
  - Uses **simple, routinely available vital signs**  
  - Captures **temporal trends effectively**  
  - Enables **early prediction (1–6 hours before event)**  

---

## 2. Dataset Used

| Field | Details |
|---|---|
| Dataset | Hospital EHR dataset (not specified) |
| Setting | ICU |
| Population | Not specified |
| Time period | Not specified |
| Task | Cardiac arrest prediction |
| Class imbalance | Not specified |

Optional:
- Feature types (vital sign trajectories)

---

## 3. Methodology

### Model: LSTM (FAST-PACE)

- Long Short-Term Memory (LSTM) network for **time-series modeling**

- Architecture overview:
  - Input: sequential vital sign trajectories  
  - LSTM layers for temporal dependency learning  
  - Fully connected output layer  

- Key components:
  - Models **temporal evolution of vital signs**  
  - Uses **simple trajectory inputs (no complex feature engineering)**  

- Input features:
  - Vital signs (time-series)

- Prediction window:
  - **1–6 hours before cardiac arrest**

### Baselines (if applicable)

- Compared with traditional early warning scores and simpler models  

---

## 4. Results

| Model | AUROC | Other Metrics |
|---|---|---|
| FAST-PACE (LSTM) | **0.896** | N/A |

### Key Findings

- Achieves **high AUROC (0.896)** for early CA prediction  
- Demonstrates effectiveness of **simple vital sign trajectories**  
- Shows that **temporal modeling (LSTM) outperforms static approaches**  
- Effective across **multiple prediction horizons (1–6 hours)**  

---

## 5. Limitations

- Limited to **LSTM architecture** — no attention mechanisms  
- Dataset details not fully specified  
- No **external validation dataset**  
- Uses only **low-dimensional vital signs**  
- Limited interpretability  

---

## 6. Relevance to This Thesis

| Aspect | Paper | This Thesis |
|---|---|---|
| Model | LSTM | TAN (Attention-based) |
| Data | EHR vital signs | VitalDB high-resolution signals |
| Setting | ICU | Intraoperative OR |
| Task | Cardiac arrest prediction | Cardiac arrest prediction |

### Key Contributions to Thesis

- Provides strong **deep learning baseline (AUROC 0.896)**  
- Demonstrates importance of **temporal modeling for CA prediction**  
- Validates use of **simple vital sign trajectories**  
- Establishes benchmark to **compare attention-based improvements**  

### Research Gap Addressed

- No **attention mechanism** for temporal importance  
- Limited to **LSTM (sequential modeling only)**  
- No use of **high-resolution waveform data**  
- No **interpretability framework**  
- No **perioperative dataset validation**  

---

## 7. Position in Literature

| Paper | Model | Setting | Contribution |
|---|---|---|---|
| Soudan et al. 2022 | Random Forest | Hospital | Traditional ML baseline |
| Cho et al. 2020 | LSTM | ICU | Strong temporal deep learning baseline |
| Li et al. 2026 | TrGRU | ICU | State-of-the-art CA prediction |
| Kapral et al. 2024 | TFT | OR | Transformer-based intraoperative prediction |

---

## 8. Citation (APA)

Cho, et al. (2020). Prediction of cardiac arrest using simple vital sign trajectories (FAST-PACE).

---

## 9. Summary (For Thesis Writing)

Cho et al. (2020) introduced FAST-PACE, an LSTM-based model for early cardiac arrest prediction using simple vital sign trajectories, achieving strong performance with an AUROC of 0.896. The study highlights the effectiveness of temporal modeling in clinical time-series data, while motivating the need for attention-based architectures to further improve performance and interpretability.

---

*Notes by: Sachu Mon Puthenpuraickpal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
