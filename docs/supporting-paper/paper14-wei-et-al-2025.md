# Paper 14: Wei et al. 2025 (Systematic Review & Meta-Analysis)

> 🟢 **SUPPORTING PAPER** — Comprehensive systematic review of ML for CA prediction + meta-analysis pooled C-index + most important features validated across 93 studies + evidence-based justification for this thesis approach

---

## Metadata
| Field | Details |
|---|---|
| **Title** | Application of Machine Learning for Patients With Cardiac Arrest: Systematic Review and Meta-Analysis |
| **Authors** | Shengfeng Wei, Xiangjian Guo, Shilin He, Chunhua Zhang, Zhizhuan Chen, Jianmei Chen, Yanmei Huang, Fan Zhang, Qiangqiang Liu |
| **Journal** | Journal of Medical Internet Research (JMIR) |
| **Year** | 2025 |
| **DOI** | 10.2196/67871 |
| **Link** | https://www.jmir.org/2025/1/e67871 |
| **PMC Link** | https://pmc.ncbi.nlm.nih.gov/articles/PMC11933771/ |
| **PubMed** | https://pubmed.ncbi.nlm.nih.gov/40063076/ |
| **Citation** | Wei, S., Guo, X., He, S., Zhang, C., Chen, Z., Chen, J., Huang, Y., Zhang, F., & Liu, Q. (2025). Application of machine learning for patients with cardiac arrest: Systematic review and meta-analysis. *Journal of Medical Internet Research, 27*, e67871. |
| **Read Date** | Feb 25, 2026 |
| **Category** | 🟢 Supporting Paper |
| **Thesis Relevance** | ⭐⭐⭐⭐⭐ Very High — Most comprehensive ML + CA systematic review available (93 studies, 5.7M patients) + pooled AUROC benchmark + top feature validation directly supports this thesis feature selection |

---

## 1. Problem They Solved
- No systematic evidence existed to confirm whether ML models truly outperform traditional CA scoring tools (MEWS, NEWS, CART) across diverse settings
- Individual ML studies on CA prediction were inconsistent — different datasets, features, settings, and metrics made comparisons impossible
- No pooled meta-analysis existed for ML performance in CA occurrence prediction, neurological prognosis, mortality, and ROSC
- Clinical researchers lacked evidence-based guidance on which ML models and features to prioritise for CA prediction tools
- Need for a rigorous PRISMA-compliant synthesis of all available ML evidence for CA across both IHCA and OHCA settings

---

## 2. Study Design
| Field | Details |
|---|---|
| **Study Type** | Systematic Review + Meta-Analysis |
| **Databases Searched** | PubMed, Embase, Cochrane Library, Web of Science |
| **Search Period** | Database inception → May 17, 2024 |
| **Total Studies Included** | 93 studies |
| **Total Patients** | 5,729,721 (in-hospital + out-of-hospital) |
| **PROSPERO Registration** | CRD42024518949 |
| **Risk of Bias Tool** | PROBAST (Prediction Model Risk of Bias Assessment Tool) |
| **Outcomes Assessed** | CA occurrence, good neurological prognosis (CPC 1-2), mortality, ROSC |

---

## 3. Methodology
- Systematic search across 4 major databases following PRISMA guidelines
- Included: case-control, cohort, nested case-control, case-cohort, cross-sectional studies
- Extracted and weighted modelling variables from all 93 studies
- Separate analysis for:
  - **CA occurrence prediction** (28 studies)
  - **CPC 1-2 prognosis prediction** — IHCA (10 studies) + OHCA (32 studies)
- Meta-analysis performed on both **imbalanced** and **balanced** validation datasets
- Pooled C-index, sensitivity, and specificity calculated with 95% CI
- Subgroup analyses conducted for IHCA vs OHCA populations

---

## 4. Results

### Meta-Analysis — CA Occurrence Prediction
| Dataset Type | Pooled C-Index | Sensitivity | Specificity |
|---|---|---|---|
| Imbalanced validation | 0.90 (95% CI 0.87–0.93) | 0.83 (95% CI 0.79–0.87) | 0.93 (95% CI 0.88–0.96) |
| Balanced validation | 0.88 (95% CI 0.86–0.90) | 0.72 (95% CI 0.49–0.95) | 0.79 (95% CI 0.68–0.91) |

### Meta-Analysis — Good Neurological Prognosis (CPC 1-2)
| Dataset Type | Pooled C-Index | Sensitivity | Specificity |
|---|---|---|---|
| Validation dataset | 0.86 (95% CI 0.85–0.87) | 0.72 | — |

### Top Modelling Variables — CA Occurrence (28 studies)
| Feature | Studies Using It | Weight |
|---|---|---|
| Respiratory Rate | 22/28 | 79% |
| Blood Pressure | 20/28 | 71% |
| Age | 19/28 | 68% |
| Temperature | 19/28 | 68% |
| Oxygen Saturation (SpO2) | 15/28 | 54% |
| Airway status | 9/28 | 32% |

### Top Modelling Variables — CPC 1-2 IHCA (10 studies)
| Feature | Weight |
|---|---|
| Rhythm (shockable/non-shockable) | 80% |
| Age | 70% |
| Medication use | 60% |
| Gender | 50% |
| GCS | 50% |

### Top Modelling Variables — CPC 1-2 OHCA (32 studies)
| Feature | Weight |
|---|---|
| Age | 78% |
| Rhythm (shockable/non-shockable) | 75% |
| Medication use | 56% |
| ROSC | 44% |
| Gender | 38% |

---

## 5. Limitations
- **No perioperative / OR setting** — all 93 studies focused on ICU, ward, or out-of-hospital CA; intraoperative prediction not covered — directly highlights thesis novelty
- **Heterogeneity across studies** — different datasets, feature sets, and ML methods limit direct comparisons
- **Lab data dominance** — many reviewed models relied on lab results not available in real-time intraoperative monitoring
- **No VitalDB-based studies** — none of the 93 studies used VitalDB or OR haemodynamic monitoring data
- **Imbalance handling inconsistent** — methods for handling class imbalance varied significantly across studies
- **External validation lacking** — several studies had no independent external validation

---

## 6. Relevance to This Thesis

### Direct Connections
| Aspect | Wei et al. 2025 | This Thesis |
|---|---|---|
| Study type | Systematic review — 93 ML studies | Primary ML study |
| Setting covered | ICU + OHCA only | Perioperative OR 🆕 |
| Dataset | 5,729,721 patients across 93 studies | VitalDB — 6,388 surgical cases |
| Pooled AUROC (CA prediction) | 0.90 (imbalanced) / 0.88 (balanced) | Target > 0.91 |
| Top features used | BP, SpO2, RR, Age, Temp | HR, SpO2, ETCO2, ART_MBP, ART_SBP, ART_DBP |
| Model types reviewed | RF, LSTM, LR, XGBoost, SVM, DL | TAN + LGBM Ensemble |
| Imbalance handling | Inconsistent across studies | SMOTE-ENN |

### Key Takeaways for Thesis
1. **Pooled AUROC 0.90 is the gold standard benchmark** — your target of >0.91 is directly justified as exceeding the best pooled evidence across 93 studies
2. **Blood pressure + SpO2 are the top validated features** — ART_MBP, ART_SBP, ART_DBP, SpO2 in your feature set are all evidence-backed by this meta-analysis
3. **No perioperative study exists in 93 papers** — this is your strongest novelty argument for Chapter 1 and Chapter 2; your OR setting is completely unexplored
4. **No VitalDB study found** — further confirms your dataset choice is novel and not duplicated by any existing work
5. **Balanced vs imbalanced performance gap** — pooled C-index drops from 0.90 → 0.88 with balanced datasets; justifies your SMOTE-ENN approach to handle class imbalance properly
6. **ML consistently outperforms MEWS/NEWS/CART** — supports thesis argument that traditional scoring tools are insufficient for perioperative CA prediction
7. **Most recent comprehensive review (2025)** — citing this paper positions your thesis within the absolute state of the art

---

## 7. Citation (APA)
Wei, S., Guo, X., He, S., Zhang, C., Chen, Z., Chen, J., Huang, Y., Zhang, F., & Liu, Q. (2025). Application of machine learning for patients with cardiac arrest: Systematic review and meta-analysis. *Journal of Medical Internet Research, 27*, e67871. https://doi.org/10.2196/67871

---

*Notes by: Sachu Mon Puthenpuraickkal Sajeev | TSI University | Master Thesis: Cardiac Arrest Prediction using VitalDB + TAN*
