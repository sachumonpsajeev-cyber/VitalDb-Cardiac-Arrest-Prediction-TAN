# Paper 7: Soudan et al. 2022 — Cardiac Arrest Prediction Using AI on EHR Vital Signs

**Citation:** Soudan, B., Dandachi, F.F., & Bou Nassif, A. (2022). Attempting cardiac arrest prediction using artificial intelligence on vital signs from Electronic Health Records. *Smart Health*, 26, 100352. https://doi.org/10.1016/j.smhl.2022.100352 **Link:** https://www.sciencedirect.com/science/article/abs/pii/S2352648322000290 **Date Read:** 21 Feb 2026

> 🟡 **BENCHMARK PAPER** — Traditional ML baseline for cardiac arrest prediction using vital signs

---

## 1. Problem They Solved

- No systematic comparison existed of AI algorithms for cardiac arrest prediction using routine EHR vital signs
- Clinical teams lacked advance warning tools that could predict cardiac arrest before occurrence
- Unclear which vital signs, which models, and which time windows produced the most accurate prediction

---

## 2. Dataset Used

- **Source:** Hospital Electronic Health Records (EHR)
- **Data type:** Routinely recorded vital signs
- **Time windows tested:** 1 to 12 hours prior to event

---

## 3. Methodology

- Compared **six AI algorithms:** Random Forest, and five others (logistic regression, SVM, decision tree, KNN, neural network)
- Tested multiple vital sign combinations and time windows systematically
- Goal: identify optimal model + feature + window combination for CA prediction

---

## 4. Results

| Finding | Detail |
|---|---|
| Best model | **Random Forest — >80% accuracy** |
| Best time window | **Immediately preceding 60 minutes** |
| Accuracy gain | +10% improvement using last 60 min vs longer windows |

---

## 5. Limitations

- Traditional ML only — no deep learning or attention mechanisms
- EHR vital signs only — no high-resolution waveform data
- No external dataset validation
- Accuracy metric used — AUROC not reported, limiting direct comparison

---

## 6. Relevance to My Project

- Establishes that **vital signs alone** are sufficient signal for cardiac arrest prediction
- Confirms **60-minute time window** as clinically meaningful prediction horizon — informs my sliding window design
- Random Forest baseline provides a **traditional ML benchmark** to compare against my deep learning TAN model
- Demonstrates the field's progression from simple ML toward the deep learning approach I am implementing
- **Cite in:** Related Work (traditional ML approaches), Discussion (comparison with non-attention models)

---

*Notes by: Sachu Mon Puthenpuraickkal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
