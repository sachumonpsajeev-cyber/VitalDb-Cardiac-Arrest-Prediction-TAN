# Cardiac Arrest Prediction using TAN — VitalDB

## Project
Master Thesis — TSI University, Riga, Latvia  
Predicting intraoperative cardiac arrest using Temporal Attention Network (TAN) on VitalDB dataset.

## Research Goal
Multi-horizon early warning system predicting cardiac arrest at:
- 30 minutes before arrest
- 60 minutes before arrest
- 2 hours before arrest
- 4 hours before arrest

## Dataset
- Source: VitalDB (Lee et al. 2022)
- Total cases: 6,388
- CA cases: 70 (1.10%)
- Non-CA cases: 6,318 (98.90%)
- Class ratio: 90:1
- Features: HR, SpO2, ETCO2, ART_MBP, ART_SBP, ART_DBP

## Model
- Primary: Temporal Attention Network (TAN)
- Baselines: LSTM, Logistic Regression, MEWS/NEWS
- Benchmark target: AUROC > 0.881 (HRV-LGBM 2023)

## Project Structure
```
VitalDb-Cardiac-Arrest-Prediction-TAN/
├── data/        # Dataset files
├── notebooks/   # Jupyter notebooks
├── src/         # Source code
├── models/      # Trained models
├── results/     # Results and plots
└── docs/        # Documentation and paper notes
```

## Technologies
- Python, Pandas, NumPy
- Scikit-learn, TensorFlow/PyTorch
- Google Colab, VS Code

## Sprint Status
Sprint 1 — 18 Feb to 3 Mar 2026
- CA-1: Done — VitalDB paper read
- CA-2: Done — GitHub setup
- CA-3: Done — Data exploration complete
- CA-9: Done — Class imbalance confirmed
- CA-12: Done — Dev environment setup
- CA-8: In Progress — Paper reading (3/15)
- CA-10: In Progress — Prediction window defined (multi-horizon)

## Author
Sachu Mon Puthenpuraickkal Sajeev  
TSI University, Riga, Latvia  
2026