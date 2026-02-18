# Literature Review

---

## Paper 1: VitalDB Dataset (Lee et al. 2022)
**Link:** https://www.nature.com/articles/s41597-022-01411-5
**Date Read:** 18 Feb 2026

### 1. Problem They Solved
No large scale high resolution biosignal dataset existed for 
machine learning research on surgical patients.

### 2. Dataset Used
- 6,388 surgery cases from Seoul National University Hospital
- Collected August 2016 to June 2017
- 196 monitoring parameters per patient
- 486,451 total data tracks

### 3. Methodology
- Used Vital Recorder software to collect data
- Connected to 10 operating rooms simultaneously
- Time synchronized data from all devices

### 4. Results
- Successfully created open public dataset
- Average 2.8 million data points per patient
- Numeric data every 1-7 seconds
- Waveform data at 62.5-500 Hz

### 5. Limitations
- Single hospital in Seoul South Korea
- Single race - Asian patients only
- Surgical patients only not general ICU
- Real world noise not cleaned

### 6. Relevance to MY Project
- Primary dataset for cardiac arrest prediction
- No direct cardiac arrest label - will use mortality outcome
- Key features: HR, Blood Pressure, SpO2, ECG
- Must handle missing data and noise in preprocessing
- Label Strategy: Start with in-hospital mortality (exists in clinical_information.csv), 
  then attempt to derive cardiac arrest label from HR/BP collapse patterns as advanced step

---

## Paper 2: Kwon Cardiac Arrest Prediction (2018)
**Link:** https://www.ahajournals.org/doi/10.1161/JAHA.118.008678
**Date Read:** 19 Feb 2026

### 1. Problem They Solved

### 2. Dataset Used

### 3. Methodology

### 4. Results

### 5. Limitations

### 6. Relevance to MY Project

---

## Paper 3: Meyer ICU Complications (2018)
**Link:** https://www.thelancet.com/journals/lanres/article/PIIS2213-2600(18)30300-X
**Date Read:** 19 Feb 2026

### 1. Problem They Solved

### 2. Dataset Used

### 3. Methodology

### 4. Results

### 5. Limitations

### 6. Relevance to MY Project
