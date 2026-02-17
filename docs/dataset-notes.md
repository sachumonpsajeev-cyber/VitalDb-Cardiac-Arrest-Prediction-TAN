# Dataset Notes

## VitalDB Dataset
**Source:** https://physionet.org/content/vitaldb/1.0.0/
**Access Date:** 

### Dataset Structure
- Total Cases: 6,388
- Total Parameters: 196
- Total Data Tracks: 486,451

### Key Parameters for Cardiac Arrest Prediction
- Solar8000/HR - Heart Rate
- Solar8000/ART_MBP - Mean Blood Pressure
- Solar8000/SpO2 - Oxygen Saturation
- Solar8000/ETCO2 - End Tidal CO2
- BIS/BIS - Brain Activity Index

### Data Access Method
```python
pip install vitaldb
import vitaldb
cases = pd.read_csv('https://api.vitaldb.net/cases')
```

### Preprocessing Notes
- Data contains real world noise
- Missing values exist
- Needs normalization before ML
