# Paper 7: Li, Lv & Wang 2026 — TrGRU: Early Prediction of Cardiac Arrest Using Deep Learning on Time-Series Vital Signs

**Citation:** Li, Y., Lv, L., & Wang, X. (2026). Early Prediction of Cardiac Arrest Based on Time-Series Vital Signs Using Deep Learning: Retrospective Study. *JMIR Formative Research*, 10, e78484. https://doi.org/10.2196/78484 **Link:** https://formative.jmir.org/2026/1/e78484 **Date Read:** 22 Feb 2026

> 🟡 **BENCHMARK PAPER** — Current SOTA deep learning model for cardiac arrest prediction — primary performance target to beat

---

## 1. Problem They Solved

- Existing CA prediction models suffered from low sensitivity and high false alarm rates
- No hybrid Transformer-GRU architecture had been applied specifically to cardiac arrest prediction
- Models lacked real-time prediction capability and cross-dataset generalisation
- Most models required large numbers of variables not commonly available in all hospital settings

---

## 2. Dataset Used

- **Primary:** MIMIC-III waveform database — 4,063 patients (2,027 CA group, 2,036 non-CA group)
- **External validation:** eICU-CRD — multicenter, 200,000+ ICU admissions across 208 US hospitals
- **Split:** 70% training / 10% validation / 20% test
- **Features:** 6 vital signs — HR, respiratory rate, systolic BP, diastolic BP, mean arterial pressure, SpO₂
- **Prediction window:** 2-hour input → predict CA within next 1 hour at 5-minute intervals

---

## 3. Methodology

- **Model:** TrGRU — hybrid Transformer + Gated Recurrent Unit
- **Architecture:** 3 stacked Transformer encoder layers → 2 GRU layers → Global Average Pooling → Fully Connected output
- Statistical features constructed using 2-hour sliding window (mean, median, min, max, SD per feature)
- Class imbalance handled via oversampling (positive) and undersampling (negative)
- **Cross-dataset generalisation:** Meta-learning approach — pretrained on MIMIC-III, rapidly adapted to eICU-CRD with small number of samples
- **Baselines compared:** Logistic Regression, XGBoost, LGBM, Random Forest

---

## 4. Results

| Metric | TrGRU (MIMIC-III) | eICU-CRD (External) |
|---|---|---|
| Accuracy | **0.904** | — |
| Sensitivity | **0.859** | 0.813 |
| Specificity | **0.933** | — |
| AUROC | **0.957** | 0.920 |
| AUPRC | **0.949** | 0.848 |
| False Alarm Rate | **0.067** | — |

- Sensitivity at 30 min before CA: **90.6%**
- Sensitivity at 20 min before CA: **92.6%**
- Sensitivity at 10 min before CA: **94.8%**
- Statistical features outperformed raw features alone across all metrics

---

## 5. Limitations

- Only 6 features used — does not exploit high-resolution waveform data
- Validated on MIMIC-III and eICU only — not tested on VitalDB perioperative data
- Surgical/perioperative patient population not represented
- Deep learning "black box" — no attention interpretability or feature attribution analysis
- Disease heterogeneity between CA patients not addressed — may limit generalisation across disease subtypes

---

## 6. Relevance to My Project

- **Primary SOTA benchmark** — AUROC 0.957 is the current performance ceiling I am targeting on VitalDB
- **Architecture comparison** — TrGRU uses stacked Transformer encoders; my TAN uses temporal-spatial dual-branch attention — direct architectural contrast available
- **Gap I fill** — TrGRU uses only 6 features from MIMIC-III; I exploit VitalDB's high-resolution waveform data (ECG at 500Hz, 196 parameters)
- **Gap I fill** — No interpretability in TrGRU; my TAN attention maps provide clinically meaningful feature attribution
- **Gap I fill** — Perioperative surgical patients entirely absent from TrGRU — VitalDB fills this population gap
- **Gap I fill** — TrGRU not validated on VitalDB; my thesis provides the first application of this class of model to perioperative cardiac arrest prediction
- **Cite in:** Related Work (current SOTA), Methodology (architectural comparison), Results (benchmark target), Discussion (interpretability gap)

---

*Notes by: Sachu Mon Puthenpuraickkal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
