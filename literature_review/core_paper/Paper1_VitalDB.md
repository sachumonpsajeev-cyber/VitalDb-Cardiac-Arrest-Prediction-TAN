# Paper 1: Lee et al. 2022 (VitalDB — High-Fidelity OR Dataset)

>  CORE PAPER — VitalDB: High-resolution intraoperative vital signs database enabling perioperative machine learning

---

## Metadata

| Field | Details |
|---|---|
| Title | VitalDB, a High-Fidelity Multi-Parameter Vital Signs Database in Surgical Patients |
| Authors | Lee HC, Park Y, Yoon SB, et al. |
| Institution | Seoul National University Hospital (SNUH), South Korea |
| Journal | Scientific Data |
| Year | 2022 |
| Volume | 9, Article 279 |
| DOI | 10.1038/s41597-022-01411-5 |
| Read Date | Feb 18, 2026 |
| Category | Core Paper |
| Thesis Relevance | Critical — primary dataset for intraoperative cardiac arrest prediction |

---

## 1. Problem Addressed

- Lack of publicly available high-resolution intraoperative datasets for machine learning  
- Existing ICU datasets (e.g., MIMIC-IV):
  - Low temporal resolution (hourly data)
  - Not representative of intraoperative physiology  
- Intraoperative data is:
  - High-frequency and dynamic  
  - Device-dependent and heterogeneous  
- No standardized dataset existed for perioperative AI applications  

---

## 2. Dataset Overview

| Field | Details |
|---|---|
| Dataset Name | VitalDB |
| Institution | SNUH |
| Total cases | 6,388 surgeries |
| Time period | 2016–2017 |
| Setting | Operating Room (OR) |
| Sampling | High-frequency (up to 500 Hz) |
| Data type | Waveform + numeric time-series |

### Key Signals

- Cardiovascular: ECG, arterial BP (SBP, DBP, MBP)  
- Respiratory: ETCO2, respiratory rate  
- Oxygenation: SpO2  
- Anesthesia: BIS, anesthetic gases  
- Ventilation: Tidal volume, airway pressure  

---

## 3. Methodology (Dataset Construction)

- Real-time data acquisition from:
  - Patient monitors  
  - Anesthesia machines  
  - Infusion devices  

### Processing Steps

1. Time synchronization across devices  
2. Data cleaning (artifact and noise removal)  
3. Standardization into unified format  
4. Efficient storage for large waveform data  

---

## 4. Key Contributions

- First publicly available high-resolution intraoperative dataset  
- Enables modeling of second-level physiological dynamics  
- Provides multimodal data (waveforms + numerical signals)  
- Supports development of:
  - Real-time monitoring models  
  - Predictive models (e.g., hypotension, cardiac arrest)  

---

## 5. Limitations

- Single-center dataset (SNUH)  
- Retrospective data collection  
- Limited demographic diversity  
- Requires preprocessing (resampling, segmentation)  
- No direct labels for some clinical outcomes  

---

## 6. Relevance to This Thesis

| Aspect | VitalDB | This Thesis |
|---|---|---|
| Setting | Operating Room | Operating Room |
| Data type | High-frequency signals | Same |
| Signals used | HR, SpO2, BP, ETCO2 | Same |
| Use case | General dataset | Cardiac arrest prediction |

### Key Points

- Core dataset used in this thesis  
- Provides high temporal resolution unavailable in ICU datasets  
- Suitable for Temporal Attention Network (TAN)  
- Enables modeling of rapid intraoperative physiological changes  

---

## 7. Position in Literature

| Paper | Type | Setting | Contribution |
|---|---|---|---|
| MIMIC-III / IV | Dataset | ICU | Low-frequency EHR data |
| Lee et al. 2022 | Dataset | OR | High-frequency intraoperative data |
| Lee et al. 2024 | Model | ICU | Multimodal IHCA prediction |
| This Thesis | Model | OR | TAN-based cardiac arrest prediction |

---

## 8. Citation (APA)

Lee, H. C., Park, Y., Yoon, S. B., et al. (2022). *VitalDB, a high-fidelity multi-parameter vital signs database in surgical patients*. Scientific Data, 9, 279. https://doi.org/10.1038/s41597-022-01411-5

---

## 9. Summary (For Thesis Writing)

> VitalDB (Lee et al., 2022) is a high-resolution intraoperative dataset that enables machine learning models to capture fine-grained physiological dynamics during surgery. Unlike ICU datasets, it provides continuous waveform data, making it highly suitable for real-time perioperative prediction tasks such as intraoperative cardiac arrest.


