# Paper 8: Soudan et al. (2022)

## Citation
Soudan B, Dandachi FF, Bou Nassif A. Predicting In-Hospital Cardiac 
Arrest Using Vital Signs from Electronic Health Records. 
Smart Health. 2022;24:100318. doi:10.1016/j.smhl.2022.100318

## Category
🟢 SUPPORTING PAPER — Multi-algorithm comparison study establishing
   Random Forest as strong baseline and validating the 60-minute
   prediction window for vital-sign-based CA prediction.

## Problem & Objective
Addresses three specific research gaps in CA prediction:
1. Which AI algorithm produces the most accurate CA prediction
   from standard EHR vital signs?
2. How many hours of vital signs are needed for acceptable accuracy?
3. How far in advance can CA be predicted accurately?
Goal: give caregivers advance notice to intervene or prepare
immediate response before CA onset.

## Dataset
- Source: Publicly available EHR dataset with documented
  in-hospital CA occurrences (MIMIC-based)
- Features: Standard vital signs routinely recorded in EHR
  (SBP, HR, body temperature, respiratory rate — no lab data)
- Observation window tested: 1h to 12h
- Prediction horizon tested: immediate (next 60 min) and longer

## Method / Model
- Six AI algorithms compared:
  (includes Random Forest, Deep Learning/RNN-LSTM, and others)
- Input: vital sign time-series from EHR records only
- No non-standard or imaging-based features used
- Evaluation metrics: Accuracy, F1-score, AUROC

## Key Results
- Random Forest (RF) achieved best overall accuracy: >80%
- Accuracy improves by >10% when prediction uses vital sign
  data from the immediately preceding 60 minutes
- Performance improves only ~3% when observation window
  increases from 1h to 12h (diminishing returns beyond 1h)
- Key finding: shorter, more recent input windows outperform
  longer historical windows for imminent CA prediction

## Significant Contributions
1. Confirmed CA can be predicted with reasonable accuracy from
   standard EHR vital signs alone
2. RF outperforms other algorithms tested including DL approaches
3. 60-minute window identified as optimal prediction horizon
4. Increasing observation range beyond 1h yields minimal gain

## Limitations
1. Abstract-level access only — full methodology details
   (exact feature set, dataset size, class imbalance handling)
   require full paper access
2. Focuses on in-hospital ward setting — not intraoperative
3. No temporal attention or sequence modelling architecture used
4. No external validation reported

## Relevance to This Thesis ⭐⭐⭐
- Directly supports the CA-10 provisional prediction window
  decision — their finding that 60 min is the optimal horizon
  aligns with our 30/60/120/240 min multi-window strategy
- Validates vital-sign-only feature set as sufficient for
  meaningful CA prediction — supports VitalDB feature selection
- RF as best-performing algorithm establishes it as a strong
  baseline to compare against TAN in CA-15
- Key insight: diminishing returns beyond 1h input window
  informs input sequence length design (our 30-min input window)
- Differentiator: we use TAN with attention on high-frequency
  intraoperative data vs their RF on hourly EHR recordings
