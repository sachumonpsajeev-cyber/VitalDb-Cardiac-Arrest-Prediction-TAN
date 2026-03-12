
## Paper 2: Kwon et al. 2018 - Deep Learning for In-Hospital Cardiac Arrest Prediction

**Citation:** Kwon, J., Lee, Y., Lee, Y., Lee, S., & Park, J. (2018). An Algorithm 
Based on Deep Learning for Predicting In-Hospital Cardiac Arrest. Journal of the 
American Heart Association, 7(13), e008678. https://doi.org/10.1161/JAHA.118.008678
**Link:** https://www.ahajournals.org/doi/10.1161/JAHA.118.008678
**Date Read:** 19 Feb 2026
> 🔴 **BASE PAPER** — Primary benchmark, AUROC 0.850 target to beat



### 1. Problem They Solved
- Traditional early warning systems (like MEWS) had low sensitivity and high false alarm rates
- They treated each vital sign independently, ignoring relationships between signals
- No deep learning approach existed for in-hospital cardiac arrest (IHCA) prediction

### 2. Dataset Used
- 52,131 patients from 2 hospitals in South Korea
- June 2010 to July 2017 (retrospective cohort study)
- Train: June 2010 - January 2017
- Test: February 2017 - July 2017
- ~1,233 cardiac arrest cases (only 2.3% of patients = severe class imbalance)

### 3. Methodology
- Model: Recurrent Neural Network (RNN) called DEWS (Deep learning Early Warning System)
- Input: Only 4 vital signs — Systolic BP, Heart Rate, Respiratory Rate, Temperature
- Prediction window: 0.5 to 24 hours before cardiac arrest event
- Compared against: MEWS, Random Forest, Logistic Regression

### 4. Results
| Model | AUROC | AUPRC |
|---|---|---|
| DEWS (Deep Learning) | 0.850 | 0.044 |
| Random Forest | 0.780 | 0.014 |
| Logistic Regression | 0.613 | 0.007 |
| MEWS (traditional) | 0.603 | 0.003 |

- Deep learning significantly outperformed all traditional methods
- Reduced false alarms while maintaining high sensitivity

### 5. Limitations
- Only 4 vital signs used — no ECG waveform, no SpO2, no lab values
- Single race — Korean patients only (same as VitalDB)
- Severe class imbalance — only 2.3% positive cases
- Black box model — not interpretable for clinical staff
- General ward vitals measured manually (3x/day) — very low resolution

### 6. Relevance to MY Project
- This is the KEY baseline paper my thesis builds on
- Benchmark to beat: AUROC > 0.850
- MY improvement over Kwon: richer features (ECG, SpO2 continuous) + TAN architecture
- Class imbalance lesson: expect ~2-3% positive rate in VitalDB — plan SMOTE or class weights
- Prediction window to replicate: 0.5 to 24 hours before event



*Notes by: Sachu Mon Puthenpuraickkal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
