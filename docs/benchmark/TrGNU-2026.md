# Paper 7: TrGRU (Li et al., 2026)

## Citation
Li Y, Lv L, Wang X. Early Prediction of Cardiac Arrest Based on 
Time-Series Vital Signs Using Deep Learning: Retrospective Study. 
JMIR Form Res. 2026;10:e78484. doi:10.2196/78484

## Category
🟡 BENCHMARK PAPER — Primary architecture and performance benchmark
   for this thesis. Closest prior work to TAN on intraoperative
   CA prediction using vital sign time-series.

## Problem & Objective
Most CA prediction models rely on complex multi-variable EMR data.
This study proposes TrGRU — a hybrid Transformer + GRU deep learning 
model — to predict CA within the next 1 hour using only 2 hours of 
vital sign time-series data, with meta-learning for cross-dataset 
generalisation.

## Dataset
- Primary: MIMIC-III waveform database
- Patients: 4,063 (after inclusion/exclusion)
- Note: Multiple CA events per patient treated as independent samples
  to increase CA event sample size
- Features: 6 vital signs
  (HR, SpO2, ABPSys, ABPDias, ABPMean, RR — same domain as VitalDB)
- External validation: eICU-CRD dataset
- Class imbalance: present (rare CA events)

## Method / Model
- Architecture: TrGRU hybrid
  - 3 stacked Transformer encoder layers (self-attention)
  - 2 GRU layers (sequential memory)
  - Global average pooling → fully connected output layer
- Input window: 2 hours of vital signs
- Prediction horizon: CA within next 1 hour
- Feature engineering: sliding window statistical features
  (mean, min, max, SD) on top of raw vitals
- Normalisation: min-max scaling to [0,1]
- Pipeline: 6-step development process
  (data prep → feature engineering → model build → train → validate → evaluate)
- Meta-learning used to enhance cross-dataset generalisation

## Key Results
### Internal (MIMIC-III):
- Accuracy:    0.904
- Sensitivity: 0.859  (>90% for events within 1h window)
- AUROC:       0.957
- AUPRC:       0.949

### External (eICU-CRD):
- Sensitivity: 0.813
- AUROC:       0.920
- AUPRC:       0.848

### vs Prior Work:
- Outperforms all models reported in comparison table
- Benchmarks include LGBM, LSTM, RNN, TabNet-based approaches

## Feature Insights
- Vital sign trends diverge between CA and non-CA groups
  starting ~hours before event
- ABPSys, ABPDias, ABPMean show most pronounced pre-arrest decline
- SpO2 also shows measurable drop in CA group

## Limitations
1. Black-box nature of deep learning — limited clinical interpretability
2. Patient heterogeneity across disease types not addressed
3. Single-centre development (MIMIC-III); needs broader validation
4. ICU setting only — not validated in intraoperative/OR environment

## Relevance to This Thesis ⭐⭐⭐⭐⭐ (HIGHEST)
- PRIMARY BENCHMARK PAPER for architecture comparison
- TrGRU (Transformer + GRU) is the closest prior architecture
  to the TAN (Temporal Attention Network) used in this thesis
- Same 6-feature vital sign domain as VitalDB feature set
- Their 2h input → 1h prediction mirrors our 30-60 min window range
- KEY DIFFERENTIATOR: TrGRU validated on ICU (MIMIC-III/eICU);
  this thesis applies attention-based architecture to INTRAOPERATIVE
  setting (VitalDB) — a gap TrGRU explicitly does not address
- Their limitation #4 (no OR setting) = our thesis contribution
- Meta-learning generalisation approach worth referencing in
  future work section
- AUROC 0.957 sets the performance ceiling to compare against
- Interpretability gap they flag = motivation for TAN's attention
  weights as a transparency mechanism

*Notes by: Sachu Mon Puthenpuraickkal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
