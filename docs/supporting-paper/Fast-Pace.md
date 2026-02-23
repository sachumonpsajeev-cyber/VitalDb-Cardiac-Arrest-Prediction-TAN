# Paper 8: Kim et al. 2019 — FAST-PACE: Predicting Cardiac Arrest and Respiratory Failure Using Feasible AI with Simple Trajectories of Patient Data

**Citation:** Kim, J., Chae, M., Chang, H.J., Kim, Y.A., & Park, E. (2019). Predicting Cardiac Arrest and Respiratory Failure Using Feasible Artificial Intelligence with Simple Trajectories of Patient Data. *Journal of Clinical Medicine*, 8(9), 1336. https://doi.org/10.3390/jcm8091336 **Link:** https://pmc.ncbi.nlm.nih.gov/articles/PMC6780058/ **Date Read:** 21 Feb 2026

> 🟢 **SUPPORTING PAPER** — LSTM baseline for CA prediction + 1–6hr prediction window reference + feature minimalism strategy

---

## 1. Problem They Solved

- Existing CA prediction models relied heavily on lab results — not feasible in wards, emergency transport, or out-of-hospital settings
- Score-based systems (MEWS, NEWS) had low sensitivity and high false alarm rates
- No model existed that could predict CA using only basic vital signs without lab data
- Need for a clinically feasible real-time AI model using minimal, readily available features

---

## 2. Dataset Used

- **Total patients:** 29,181 ICU patients
- **Hospitals:** Two hospitals — one surgical ICU + one mixed ICU (67 total ICU beds)
- **CA cases:** 242 patients
- **Respiratory failure cases:** 1,231 patients
- **Setting:** ICU — surgical and mixed
- **Data source:** EMR — periodic vital signs only

---

## 3. Methodology

- **Model:** FAST-PACE — LSTM (Long Short-Term Memory) on time-series vital sign trajectories
- **Features:** 9 only — no lab data required:
  - Pulse rate (HR), Systolic BP, Diastolic BP, Respiratory Rate, SpO₂, Body Temperature
  - Recent surgical history (within 1 week), Treatment history (pharmacological or oxygen), ASA classification
- **Prediction windows tested:** 1hr, 2hr, 4hr, and 6hr before event
- Xavier initialisation for weights; cutoff 0.5 for LSTM, 5 for MEWS/NEWS
- **Baselines compared:** MEWS and NEWS scoring systems

---

## 4. Results

| Time Window | FAST-PACE AUROC | MEWS AUROC | NEWS AUROC |
|---|---|---|---|
| 1 hour | **0.896** | 0.746 | 0.759 |
| 6 hours | **0.886** | — | — |

- Average sensitivity: **0.844** (vs MEWS 0.400, NEWS 0.695)
- Net reclassification improvement over MEWS: **0.507** for CA prediction
- Net reclassification improvement over NEWS: **0.412** for CA prediction
- Outperformed MEWS and NEWS across all prediction windows
- All results statistically significant (McNemar test p < 0.001)

---

## 5. Limitations

- ICU setting only — not validated in perioperative OR environment
- Only 9 features — potentially limits model performance
- Single country (South Korea) — generalisability uncertain
- RR and Body Temperature included — both excluded in this thesis due to missing data in VitalDB
- Lab data excluded by design — may miss important clinical signals

---

## 6. Relevance to My Project

| Aspect | FAST-PACE 2019 | This Thesis |
|---|---|---|
| Dataset | 29,181 ICU patients, 2 hospitals | VitalDB — 6,388 surgical cases |
| Prediction window | 1hr, 2hr, 4hr, 6hr | TBD — CA-10, supervisor discussion |
| Model | LSTM | TAN (Temporal Attention Network) |
| Features | 9 basic vital signs | HR, SpO₂, ETCO2, ART_MBP, ART_SBP, ART_DBP |
| Lab data | Excluded by design | Not available in VitalDB anyway |
| Setting | ICU (surgical + mixed) | Perioperative OR |

- **1–6hr prediction window is clinically validated** — strongest argument for shorter window in CA-10 discussion with supervisor
- **LSTM is the established deep learning baseline** for CA prediction — TAN should be compared against LSTM directly
- **Minimal feature set works** — 9 features achieved AUROC 0.896, supports your 6-feature VitalDB approach
- **No lab data needed** — validates your VitalDB feature set which also has no lab data
- **Perioperative setting still unexplored** — FAST-PACE used surgical ICU patients, not intraoperative — your VitalDB OR setting is a novel contribution
- **AUROC 0.896 at 1hr window** — new secondary benchmark to beat alongside Kwon et al. 0.850
- **Cite in:** Related Work (early feasible AI approaches), Methodology (feature selection + window justification), Discussion (clinical deployability + LSTM comparison)

---

*Notes by: Sachu Mon Puthenpuraickkal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
