### Paper 3: TSCAN — Temporal-Spatial Correlation Attention Network (Nie et al., 2024)
**Link:** https://arxiv.org/abs/2306.01970 | https://ieeexplore.ieee.org/document/10234629/
**Date Read:** 19 Feb 2026
> 🔴 **BASE PAPER** — Primary architecture reference for TAN model



### 1. Problem They Solved
* ICU clinical data is multivariate and temporal — conventional models struggled to capture both dimensions simultaneously
* Existing methods treated temporal and spatial (inter-feature) dimensions separately, losing cross-dimensional information
* Medical time series data is sparse and strongly correlated — standard deep learning models (LSTM, Transformer) could not handle this effectively
* No unified architecture existed that jointly modelled temporal trends AND inter-feature correlations for multi-task ICU prediction

### 2. Dataset Used
* **Dataset:** MIMIC-IV v0.4
* **Source:** Beth Israel Deaconess Medical Center, Boston, USA
* **Period:** 2008–2019
* **Size:** 76,540 ICU stays from 53,150 patients (after processing: 47,046 stays)
* **Test Set:** 15% of patients — 7,057 patients, 8,906 ICU stays
* **Mortality Rate:** ~15%
* **Features:** 155 physiological variables (5 categorical + 150 continuous) including vitals, lab tests, demographics, medication, diagnosis

### 3. Methodology
* **Model:** TSCAN — Temporal-Spatial Correlation Attention Network
* **Architecture:** Dual-branch design:
  * **Temporal Branch:** Recursive merged attention — integrates features from previous time periods into the current end-time period; handles long ICU sequences without information loss
  * **Spatial Branch:** Inter-feature attention — captures correlations between clinical variables (e.g., BP ↔ HR ↔ SpO2)
  * **Fusion-Encoder:** Fuses temporal + spatial representations to produce the final prediction feature
* **Tasks Evaluated:** Mortality prediction, Length of Stay (LOS), Physiologic Decline, Phenotype Classification
* **Baselines Compared:** LSTM, Transformer, Informer, TimesNet, and other SOTA models
* Ablation studies conducted to validate each branch's individual contribution

### 4. Results
| Task | TSCAN Result | Improvement over SOTA |
|------|--------------|-----------------------|
| In-hospital Mortality | **90.7% AUROC** | +2.0% |
| Length of Stay | **45.1%** | +2.0% |
| Physiologic Decline | Best among all baselines | ✅ |
| Phenotype Classification | Best among all baselines | ✅ |

* Ablation confirmed removing either branch degrades performance — both branches are essential
* Attention maps identified **blood protein, blood pressure, and heart rate** as the most predictive clinical indicators

### 5. Limitations
* Validated on **MIMIC-IV only** — no external dataset validation (e.g., VitalDB, eICU)
* Focuses on **mortality and LOS** — not cardiac arrest as a specific acute prediction target
* No **perioperative or surgical** patient context — general ICU population only
* No discussion of **real-time or streaming inference** — limits direct ICU deployment applicability
* Dataset limited to a **single US hospital system** — generalisability across health systems unclear

### 6. Relevance to MY Project
* **Primary architectural reference** — TSCAN's dual-branch temporal-spatial attention design is the closest existing model to the Temporal Attention Network (TAN) I am implementing
* **Dataset gap I fill** — TSCAN is not validated on VitalDB; my thesis applies a similar attention approach to VitalDB's high-resolution perioperative data
* **Task gap I fill** — TSCAN targets mortality and LOS; I extend temporal-spatial attention to **cardiac arrest prediction** — a more acute and time-critical outcome
* **Benchmark reference** — TSCAN's 90.7% AUROC on mortality provides a strong ICU prediction performance anchor for contextualising my results
* **Interpretability validation** — TSCAN proves attention-based ICU models can surface clinically meaningful features (BP, HR), supporting my TAN design choice
* **Cite in:** Methodology chapter (justifying TAN architecture), Related Work section (positioning against SOTA), and Discussion (comparing interpretability findings)

*Notes by: Sachu Mon Puthenpuraickkal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
