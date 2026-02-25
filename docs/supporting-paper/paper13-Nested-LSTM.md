# Paper 13: Wang et al. 2024 (Nested LSTM)

> 🟢 **SUPPORTING PAPER** — Nested LSTM architecture reference for temporal sequence modelling + ECG-based SCD prediction + deep learning baseline for comparison

---

## Metadata
| Field | Details |
|---|---|
| **Title** | Early Prediction of Sudden Cardiac Death Risk with Nested LSTM Based on Electrocardiogram Sequential Features |
| **Authors** | Ke Wang, Kai Zhang, Banteng Liu, Wei Chen, Meng Han |
| **Journal** | BMC Medical Informatics and Decision Making |
| **Year** | 2024 |
| **DOI** | 10.1186/s12911-024-02493-4 |
| **Link** | https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-024-02493-4 |
| **PMC Link** | https://pmc.ncbi.nlm.nih.gov/articles/PMC11005267/ |
| **Citation** | Wang, K., Zhang, K., Liu, B., Chen, W., & Han, M. (2024). Early prediction of sudden cardiac death risk with Nested LSTM based on electrocardiogram sequential features. *BMC Medical Informatics and Decision Making, 24*, 94. |
| **Read Date** | Feb 25, 2026 |
| **Category** | 🟢 Supporting Paper |
| **Thesis Relevance** | ⭐⭐⭐⭐ High — Introduces Nested LSTM architecture directly relevant to TAN design + SCD prediction using time-series signals + strong benchmark comparison against LSTM, Bi-LSTM, ESN, SVM |

---

## 1. Problem They Solved
- Traditional LSTM stores memories unrelated to the current time step, leading to weak robustness and low prediction accuracy in complex nonlinear tasks
- ECG signals are weak, highly nonlinear, non-stationary, and noisy — making standard prediction models unreliable
- Existing SCD detection methods relied on classification of abnormal vs normal ECG — struggling with dynamic, time-evolving patterns
- No method existed that could accurately predict ECG signal trends ahead of SCD onset using a nested temporal memory structure
- Need for a model that could capture intricate temporal dependencies in ECG signals for early SCD risk prediction

---

## 2. Dataset Used
| Field | Details |
|---|---|
| **Database** | Sudden Cardiac Death Holter Database — PhysioNet |
| **Link** | https://physionet.org/content/sddb/1.0.0/ |
| **Total Patients** | 20 groups of actual cardiac arrest patients |
| **Signal Type** | ECG (2-channel Holter recordings) |
| **Prediction Window** | 20 seconds (16 sec before + 4 sec after SCD event) |
| **Training Samples** | 4,901 input-output sample pairs per subject |
| **Setting** | Out-of-hospital / Holter monitoring |
| **Data Source** | Publicly available — PhysioNet |

---

## 3. Methodology

### Preprocessing Pipeline
- **Wavelet Denoising** — DB6 wavelet, 7-layer decomposition, unbiased likelihood estimation for threshold selection
  - Removes: baseline drift (<5Hz), power frequency interference (50/60Hz), myoelectric noise (5–2000Hz), motion artifacts (3–14Hz)
- **Normalization** — Z-score standardization to prevent training divergence
- **Phase Space Reconstruction** — Reconstructs temporal training set using time delay (tau) and embedding dimension (m)
  - Input: 99 sampling points → Output: 100th sampling point
  - Total: 4,901 input-output pairs generated per subject

### Nested LSTM Architecture
- Replaces standard LSTM memory cells with an **inner LSTM unit**
- Two-level structure: **Inner LSTM** (memory selection & forgetting) + **Outer LSTM** (sequence processing)
- Inner LSTM gates input and hidden states of the outer LSTM:
  - `h̄(t-1) = ft · c(t-1)` — inner hidden state
  - `x̄t = it · c̃t` — inner input state
- Both inner and outer LSTM use standard 4-gate system: forget gate, input gate, candidate memory cell, output gate
- Training: Error backpropagation with MSE loss function
- Training time per subject: 43–58 seconds

### Comparison Models
| Model | Type |
|---|---|
| SVM | Classical classification |
| ESN (Echo State Network) | Recurrent — simple feedback |
| LSTM | Standard recurrent |
| Bi-LSTM | Bidirectional recurrent |
| **Nested LSTM** | **Proposed — nested recurrent** |

---

## 4. Results

### Average Performance (All 20 Subjects)
| Model | Avg RMSE (mV) | Avg MAE (mV) |
|---|---|---|
| SVM | 0.1802 | 0.0841 |
| ESN | 0.1192 | 0.0436 |
| LSTM | 0.0882 | 0.0128 |
| Bi-LSTM | 0.0854 | 0.0141 |
| **Nested LSTM** | **0.0701** | **0.0095** |

### Improvement Over Baselines (RMSE)
| vs Model | RMSE Reduction |
|---|---|
| vs SVM | 61.1% |
| vs ESN | 41.2% |
| vs LSTM | 20.5% |
| vs Bi-LSTM | 17.9% |

### Improvement Over Baselines (MAE)
| vs Model | MAE Reduction |
|---|---|
| vs SVM | 88.7% |
| vs ESN | 78.2% |
| vs LSTM | 25.8% |
| vs Bi-LSTM | 32.6% |

- Nested LSTM consistently achieved lowest RMSE and MAE across all 20 subjects
- Wavelet denoising improved SNR from negative values (e.g. -22.13 dB) to positive (e.g. 10.82 dB) — significant noise removal confirmed

---

## 5. Limitations
- **ECG-only input** — no haemodynamic features (HR, SpO2, BP) used; not applicable to VitalDB feature set directly
- **Very small dataset** — only 20 patients; results may not generalise to larger or more diverse populations
- **Short prediction window** — 20-second window around SCD event; not a multi-minute pre-event prediction window like this thesis
- **Out-of-hospital / Holter setting** — not validated in perioperative OR environment
- **Signal prediction task (regression)** — predicts next ECG waveform point, not a binary CA risk classification like this thesis
- **No class imbalance handling** — dataset is event-focused with no non-CA control group comparison
- **Single modality** — ECG only; cannot be directly replicated with VitalDB haemodynamic signals

---

## 6. Relevance to This Thesis

### Direct Connections
| Aspect | Wang et al. 2024 (Nested LSTM) | This Thesis |
|---|---|---|
| Dataset | 20 SCD Holter ECG patients — PhysioNet | VitalDB — 6,388 surgical cases, 70 CA |
| Signal Type | ECG (waveform) | Haemodynamic (HR, SpO2, ETCO2, ART_MBP, ART_SBP, ART_DBP) |
| Task | ECG signal trend prediction (regression) | CA risk classification (binary) |
| Model | Nested LSTM | TAN (Temporal Attention Network) |
| Prediction Window | 20 seconds (pre/post SCD) | 30 / 60 / 120 / 240 min before CA |
| Metric | RMSE, MAE | AUROC, Sensitivity, Specificity |
| Setting | Out-of-hospital Holter | Perioperative OR |
| Imbalance Handling | Not applicable | SMOTE-ENN planned |

### Key Takeaways for Thesis
1. **Nested LSTM outperforms standard LSTM by 20.5% RMSE** — architectural justification for using more advanced temporal architectures (like TAN) over plain LSTM
2. **Inner memory cell concept** — the Nested LSTM's inner LSTM replacing memory cells is conceptually related to TAN's attention-gated temporal memory; useful for methodology chapter comparison
3. **Wavelet denoising pipeline** — their 7-layer DB6 wavelet approach is a validated preprocessing reference for noisy physiological signals; relevant if VitalDB signals require denoising
4. **ECG vs haemodynamic signals** — this paper confirms deep learning temporal models work well on physiological time series; supports using TAN on haemodynamic features
5. **LSTM is insufficient alone** — Nested LSTM beats LSTM; supports thesis argument that TAN (with attention) will outperform standard LSTM baseline
6. **Small dataset limitation** — 20 patients vs VitalDB's 6,388 cases; thesis has significantly larger dataset — a clear novelty and strength to highlight in Chapter 2
7. **Regression vs Classification** — this paper predicts ECG waveform trends; thesis does binary CA classification — different task but same temporal modelling domain

---

## 7. Citation (APA)
Wang, K., Zhang, K., Liu, B., Chen, W., & Han, M. (2024). Early prediction of sudden cardiac death risk with Nested LSTM based on electrocardiogram sequential features. *BMC Medical Informatics and Decision Making, 24*, 94. https://doi.org/10.1186/s12911-024-02493-4

---

*Notes by: Sachu Mon Puthenpuraickpal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
