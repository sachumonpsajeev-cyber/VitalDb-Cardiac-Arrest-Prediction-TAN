# Paper 1: Lee et al. 2022 - VitalDB High-Fidelity Vital Signs Dataset

**Citation:** Lee, H.C., Park, Y., Yoon, S.B. et al. VitalDB, a high-fidelity multi-parameter vital signs database in surgical patients. *Scientific Data* 9, 279 (2022). https://doi.org/10.1038/s41597-022-01411-5 **Link:** https://www.nature.com/articles/s41597-022-01411-5 **Date Read:** 18 Feb 2026

> 🔴 **BASE PAPER** — Primary dataset for entire thesis

---

## 1. Problem They Solved

- No large-scale, high-resolution biosignal dataset existed for machine learning research on surgical patients
- Existing datasets were small, low-resolution, or not publicly available
- No standardised perioperative monitoring database for AI development

---

## 2. Dataset Used

- 6,388 surgical cases from Seoul National University Hospital
- Collected August 2016 to June 2017
- 196 monitoring parameters per patient
- 486,451 total data tracks
- Average 2.8 million data points per patient
- Numeric data recorded every 1–7 seconds
- Waveform data at 62.5–500 Hz

---

## 3. Methodology

- Used Vital Recorder software to collect continuous intraoperative data
- Connected simultaneously to 10 operating rooms
- Time-synchronised data streams from all monitoring devices
- Released as open public dataset

---

## 4. Results

- Successfully created the largest open perioperative biosignal database
- Covers ECG, arterial blood pressure, SpO₂, BIS, cardiac output, and 190+ additional parameters

---

## 5. Limitations

- Single-centre study — Seoul National University Hospital, South Korea only
- Predominantly Asian patient population — limits generalisability
- Surgical patients only — not applicable to general ICU settings
- Raw data includes real-world noise — no preprocessing applied

---

## 6. Relevance to My Project

- Primary dataset for cardiac arrest prediction model
- No direct cardiac arrest label — initial label strategy uses in-hospital mortality from `clinical_information.csv`
- Advanced step: derive cardiac arrest label from HR/BP collapse patterns
- Key features: HR, Blood Pressure, SpO₂, ECG (500 Hz), BIS, Cardiac Output
- Key challenge: substantial missing data and signal noise must be handled in preprocessing

*Notes by: Sachu Mon Puthenpuraickkal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
