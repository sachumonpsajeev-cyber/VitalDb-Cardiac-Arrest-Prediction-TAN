# Paper 15: Shim et al. 2025 (GBM + CNN-RNN — Intraoperative Hypotension, VitalDB)

> 🟢 **SUPPORTING PAPER** — GBM and hybrid CNN-RNN for intraoperative hypotension prediction using VitalDB — AUROC 0.94 for both models — exact same 6,388-patient cohort as this thesis

---

## Metadata

| Field | Details |
|---|---|
| **Title** | Machine Learning Methods for the Prediction of Intraoperative Hypotension with Biosignal Waveforms |
| **Authors** | Jae-Geum Shim, Wonhyuck Yoon, Sang Jun Lee, Se-Hyun Chang, So-Ra Jung, Jun Young Chung |
| **Institution** | Kangbuk Samsung Hospital, Sungkyunkwan University; OUaR LaB Inc.; MISO Info Tech Co.; The Catholic University of Korea; Konan Technology Inc.; Kyung Hee University |
| **Journal** | Medicina (MDPI) |
| **Year** | 2025 |
| **Volume** | Volume 61(11), Article 2039 |
| **DOI** | 10.3390/medicina61112039 |
| **Full Text** | https://www.mdpi.com/1648-9144/61/11/2039 |
| **PDF** | https://www.mdpi.com/1648-9144/61/11/2039/pdf |
| **Citation** | Shim JG, Yoon W, Lee SJ, Chang SH, Jung SR, Chung JY. Machine learning methods for the prediction of intraoperative hypotension with biosignal waveforms. *Medicina*. 2025;61(11):2039. doi:10.3390/medicina61112039 |
| **Read Date** | Feb 25, 2026 |
| **Category** | 🟢 Supporting Paper |
| **Thesis Relevance** | ⭐⭐⭐⭐⭐ Critical — only 2025 peer-reviewed paper using exact same VitalDB 6,388-patient cohort in perioperative OR setting; validates 100 Hz preprocessing, ABP + ETCO2 signal selection, and multi-modal superiority; GBM parity with CNN-RNN motivates TAN+LGBM ensemble; paper explicitly calls for real-time OR dashboard — directly motivates thesis Phase 2.5 |

---

## 1. Problem They Solved

- Intraoperative hypotension (IOH) is a major cause of postoperative myocardial infarction, acute kidney injury, and mortality
- Existing IOH prediction models relied on a **single waveform only** (arterial pressure) — the commercial HPI system uses only ABP and is highly sensitive to poor arterial line quality
- No prior study had combined **multiple biosignal waveforms with preoperative clinical information** for IOH prediction in the OR
- No study had directly compared ML (GBM) vs DL (CNN-RNN) using the same multimodal inputs on the same OR dataset
- Real-time OR prediction tools were limited — clinicians lacked a validated multi-signal early warning system for hypotension

---

## 2. Dataset Used

| Field | Details |
|---|---|
| **Dataset** | VitalDB — **exact same 6,388-patient cohort as this thesis** |
| **Institution** | Seoul National University Hospital, Seoul, South Korea |
| **Period** | June 2016 – August 2017 |
| **Starting pool** | 6,388 patients (non-cardiac surgery, 10 operating rooms) |
| **After age + transplant exclusion** | 6,088 patients |
| **After waveform availability** | 3,278 patients (all 4 waveforms present) |
| **Final sample** | 2,611 patients (after removing missing clinical covariates) |
| **Train split** | 2,088 patients — 16,920 segments |
| **Test split** | 523 patients — 4,175 segments |
| **Outcome** | IOH — MAP ≤ 65 mmHg sustained for > 1 minute |
| **Prediction window** | 5 minutes before hypotensive event |
| **Input window** | 30 seconds of 4 waveforms at 100 Hz |
| **Setting** | Perioperative — Operating Room (non-cardiac surgery) |
| **Waveform signals** | ABP, ECG (lead II), PPG, ETCO2 (capnography) |
| **Clinical covariates** | Age, sex, BMI, ASA status, emergency surgery, hypertension, WBC, Hb, BUN, Cr, Albumin, Na, K |
| **Data source** | Publicly available — https://vitaldb.net |

---

## 3. Methodology

### Two-Model Comparison Architecture:

**Model 1 — Gradient Boosting Machine (GBM)**
- Input: Handcrafted features from 30 s waveform segments + clinical covariates
- Feature engineering: Each signal (ABP, ECG, PPG, ETCO2) divided into **10 non-overlapping 3 s sub-windows** → mean value extracted per sub-window
- Total features: 4 signals × 10 sub-windows = 40 temporal features + clinical/lab covariates
- Sequential ensemble of weak learners → progressively stronger classifier
- AUROC: **0.94 (0.93–0.95)**

**Model 2 — Hybrid CNN-RNN**
- Input: Raw 4-channel waveforms (30 s × 100 Hz) + clinical covariates
- **Stage 1 — 1D CNN:** extracts spatial feature maps from each raw waveform channel
- **Stage 2 — GRU:** learns temporal dependencies across the 30 s sequence
- **Stage 3 — FNN:** fully connected binary classifier (IOH / no IOH)
- Clinical covariates fed in alongside waveform branch
- AUROC: **0.94 (0.93–0.95)**

### Comparison Models
| Model | Type | AUROC |
|---|---|---|
| Logistic Regression | Classical baseline | < 0.94 |
| HPI (commercial) | ABP-only ML | 0.92 |
| GBM | Proposed ML | **0.94** |
| Hybrid CNN-RNN | Proposed DL | **0.94** |

### Class Balancing
- 1–2 non-hypotensive segments extracted per patient to balance classes at segment level
- No SMOTE used — contrast with thesis SMOTE-ENN required for 90:1 CA imbalance

### Preprocessing
- All 4 waveforms resampled from 500 Hz → **100 Hz** — same preprocessing rate as this thesis
- Artifact removal: cardiac cycles outside physiological range excluded; MAP <20 or >200 mmHg excluded
- Peak detection via SciPy for identifying cardiac cycles in ABP waveform

---

## 4. Results

### Model Performance — 5 min before IOH event

| Metric | GBM | Hybrid CNN-RNN | p-value |
|---|---|---|---|
| **AUROC (95% CI)** | **0.94 (0.93–0.95)** | **0.94 (0.93–0.95)** | <0.001 DeLong |
| **Accuracy (95% CI)** | 0.88 (0.86–0.89) | 0.88 (0.87–0.89) | 0.591 McNemar |
| **Sensitivity (95% CI)** | **0.83 (0.81–0.85)** | 0.80 (0.78–0.82) | <0.001 |
| **Specificity (95% CI)** | 0.90 (0.89–0.92) | **0.93 (0.92–0.94)** | <0.001 |
| **PPV (95% CI)** | 0.84 (0.83–0.86) | 0.88 (0.86–0.89) | <0.001 |
| **NPV (95% CI)** | 0.89 (0.88–0.91) | 0.88 (0.87–0.89) | 0.003 |

### Key Observations
- Both models achieve identical AUROC 0.94 — no significant difference in overall discrimination
- **GBM: higher sensitivity (0.83)** → fewer missed hypotensive events — better for safety-critical OR use
- **CNN-RNN: higher specificity (0.93)** → fewer false alarms — better for clinical workflow
- Both outperform HPI commercial system (AUROC 0.92) and logistic regression baselines
- Multi-modal (4 waveforms + clinical info) outperforms single ABP-only approaches
- GBM equals CNN-RNN — well-engineered ML matches deep learning on this dataset

### Patient Demographics (2,611 patients)

| Characteristic | Total | Train | Test |
|---|---|---|---|
| Age (years) | 59.8 ± 14.0 | 59.7 ± 14.0 | 60.0 ± 14.3 |
| Male | 55.6% | 55.8% | 54.5% |
| BMI (kg/m²) | 23.1 ± 3.5 | 23.1 ± 3.5 | 23.3 ± 3.6 |
| ASA II | 64.6% | 64.8% | 63.7% |
| Emergency surgery | 11.0% | 11.1% | 10.9% |
| Hypertension | 32.8% | 33.5% | 30.0% |

---

## 5. Limitations

- Only 2,611 of 6,388 patients used — 59% excluded due to missing covariates or waveforms
- No external validation — single-centre only; authors explicitly flag this as a limitation
- IOH outcome only — cannot generalise findings to cardiac arrest prediction
- 5-minute prediction window only — no multi-horizon analysis (30/60/120/240 min)
- No explainability — no SHAP or feature importance analysis performed
- Requires invasive arterial line — limits applicability in non-invasive monitoring settings
- No class imbalance discussion — IOH is relatively frequent vs CA (1.10%); SMOTE-ENN not evaluated

---

## 6. Relevance to This Thesis

### Direct Connections

| Aspect | Shim et al. 2025 (P15) | This Thesis |
|---|---|---|
| **Dataset** | VitalDB — 6,388 patients ✅ SAME | VitalDB — 6,388 patients |
| **Setting** | Perioperative OR ✅ SAME | Perioperative OR |
| **Institution** | SNUH, Seoul ✅ SAME | SNUH, Seoul |
| **Period** | Jun 2016 – Aug 2017 ✅ SAME | Jun 2016 – Aug 2017 |
| **Waveform rate** | 100 Hz ✅ SAME | 100 Hz |
| **Outcome** | IOH (MAP ≤ 65 mmHg) ❌ DIFFERENT | Cardiac Arrest (CA) |
| **Signal overlap** | ABP + ETCO2 + PPG (→SpO2) | ART_MBP/SBP/DBP + ETCO2 + SpO2 + HR |
| **Prediction window** | 5 min before event | 30 / 60 / 120 / 240 min before event |
| **Input window** | 30 s segment | 30 min sliding window |
| **ML model** | GBM | LGBM |
| **DL model** | CNN-RNN (1D CNN + GRU) | TAN (Tabular Attentive Network) |
| **Ensemble** | No — two separate models | Yes — TAN + LGBM ensemble |
| **Imbalance handling** | Segment-based sampling | SMOTE-ENN |
| **Explainability** | None | SHAP + feature importance |
| **External validation** | None — single-centre only | Hold-out test set (VitalDB) |
| **AUROC** | 0.94 (both models) | Target > 0.91 |

> ⚠️ **NOT a direct benchmark** — different outcome (IOH vs CA), different prediction window, different class imbalance severity. Cite as supporting evidence only.

### Key Takeaways for Thesis

1. **Strongest VitalDB citation** — only 2025 peer-reviewed paper using exact same 6,388-patient cohort in perioperative OR setting — directly validates thesis dataset choice
2. **Validates 100 Hz preprocessing** — confirms thesis resampling decision is consistent with published work on this exact dataset
3. **Signal selection validated** — ABP + ETCO2 confirmed as strongest intraoperative predictive signals; both present in thesis as ART_MBP/SBP/DBP and ETCO2
4. **Multi-modal superiority confirmed** — combining waveforms outperforms single-signal models → supports thesis use of all 6 haemodynamic features rather than reducing to fewer
5. **GBM = CNN-RNN parity** — motivates thesis TAN+LGBM ensemble as best of both approaches; proves ML and DL are complementary not competing
6. **IOH → CA relationship** — haemodynamic instability is a direct precursor to intraoperative CA; same signals predict both adverse events at different severity thresholds; strengthens clinical argument for feature set
7. **Dashboard motivation** — paper explicitly calls for "a web or mobile application for real-time use in OR" — directly motivates thesis Phase 2.5 clinical dashboard (Streamlit + FastAPI)
8. **Gap confirmation** — no external validation, no SHAP, no CA prediction — thesis addresses all three gaps as novel contributions

---

## 7. Citation (APA)

Shim, J.-G., Yoon, W., Lee, S. J., Chang, S.-H., Jung, S.-R., & Chung, J. Y. (2025). Machine learning methods for the prediction of intraoperative hypotension with biosignal waveforms. *Medicina, 61*(11), 2039. https://doi.org/10.3390/medicina61112039

---

*Notes by: Sachu Mon Puthenpuraickpal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
