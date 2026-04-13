# 🟡 BENCHMARK PAPERS — Performance Comparison Standards

This folder contains **state-of-the-art and baseline models** used to evaluate the performance of the proposed TAN model.

---

## 📌 Purpose of Benchmark Papers

Benchmark papers define:

- Performance ceilings (AUROC, AUPRC, F1)
- Baseline ML and DL models
- Comparison standards for cardiac arrest prediction

---

## 📊 Evaluation Role

These papers answer:

> “How good is the proposed model compared to existing methods?”

They provide:
- AUROC benchmarks
- Dataset comparisons
- Model performance hierarchy

---

## 📚 Included Papers

| ID | Paper | Model | AUROC | Role |
|---|---|---|---|---|
| 2 | Kwon et al., 2018 | RNN | 0.850 | Early DL baseline |
| 5 | FAST-PACE (Cho et al., 2020) | LSTM | 0.896 | Temporal DL baseline |
| 6 | Lee et al., 2022 | LGBM | 0.881 | HRV-based ML baseline |
| 7 | Li et al., 2026 | TrGRU | 0.920 | Current SOTA |
| 8 | Chae et al., 2021 | Hybrid DL | 0.840 | Weak DL baseline |
| 12 | Lee et al., 2024 | Multimodal ML | 0.910 | Ensemble benchmark |
| 13 | Han et al., 2020 | Nested LSTM | 0.890 | Advanced RNN variant |

---

## 🧠 Performance Hierarchy
Weak ML (0.84–0.88)
↓
Strong ML (0.88–0.89)
↓
LSTM-based DL (0.89–0.90)
↓
Transformer / Hybrid DL (0.91–0.92)
↓
SOTA (0.920 – TrGRU)

---

## 🎯 Thesis Target

Your TAN model must aim to:

- Beat **0.896 (FAST-PACE LSTM)**
- Beat **0.910 (Multimodal ML)**
- Compete with **0.920 (TrGRU SOTA)**

---

## 📌 Key Insight

Benchmark papers define:

- “How hard the problem is”
- “Where SOTA currently stands”
- “What your model must exceed”

---

