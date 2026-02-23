---
title: "VitalDB: A High-Fidelity Multi-Parameter Vital Signs Database in Surgical Patients"
authors: "Lee, H.C., Park, Y., Yoon, S.B. et al."
year: 2022
journal: "Scientific Data"
doi: "https://doi.org/10.1038/s41597-022-01411-5"
date_read: 2026-02-18
status: "Base Paper"
role: "Primary dataset for entire thesis"
tags: [dataset, biosignals, surgical-patients, VitalDB]
---

# Paper 1: VitalDB Dataset — Lee et al. (2022)

> 🔴 **BASE PAPER** — Primary dataset for entire thesis

**Full Citation:** Lee, H.C., Park, Y., Yoon, S.B. et al. VitalDB, a high-fidelity multi-parameter vital signs database in surgical patients. *Scientific Data* 9, 279 (2022). https://doi.org/10.1038/s41597-022-01411-5

---

## 1. Problem They Solved

No large-scale, high-resolution biosignal dataset existed for machine learning research on surgical patients, creating a significant gap in perioperative AI development.

---

## 2. Dataset Overview

| Property | Detail |
|---|---|
| Cases | 6,388 surgical patients |
| Collection period | August 2016 – June 2017 |
| Hospital | Seoul National University Hospital |
| Parameters | 196 monitoring parameters per patient |
| Total data tracks | 486,451 |
| Numeric data resolution | Every 1–7 seconds |
| Waveform resolution | 62.5–500 Hz |
| Avg. data points/patient | 2.8 million |

---

## 3. Methodology

- **Vital Recorder software** used for continuous data collection
- Connected simultaneously across **10 operating rooms**
- Time-synchronised data streams from all monitoring devices
- Dataset made publicly available via open access

---

## 4. Results

- Successfully created and published a large-scale, open, perioperative biosignal database
- Covers a wide range of monitoring modalities including ECG, arterial blood pressure, SpO₂, BIS, and cardiac output

---

## 5. Limitations

- Single-centre study (Seoul National University Hospital, South Korea)
- Predominantly Asian patient population — **limits generalisability**
- Restricted to **surgical patients only** — not general ICU
- Raw data includes real-world noise; **no preprocessing applied**

---

## 6. Relevance to My Project

- **Primary dataset** for cardiac arrest prediction model
- No direct cardiac arrest label available — initial approach will use **in-hospital mortality** from `clinical_information.csv`
- **Advanced step:** Derive cardiac arrest label from HR/BP collapse patterns
- Key features of interest: HR, Blood Pressure, SpO₂, ECG (500 Hz), BIS, Cardiac Output
- **Key challenge:** Must handle substantial missing data and signal noise during preprocessing
