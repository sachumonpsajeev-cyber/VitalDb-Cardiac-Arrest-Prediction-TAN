# ╔══════════════════════════════════════════════════════════════════════╗
# ║  SHAP Analysis — LightGBM Cardiac Arrest Prediction                 ║
# ║  Author: Sachu Mon P. Sajeev · MSc Data Science & AI · TSI 2026    ║
# ║                                                                      ║
# ║  SAFE TO RUN — This script:                                         ║
# ║    ✓ Does NOT modify any existing files                             ║
# ║    ✓ Does NOT touch your dashboard or training code                 ║
# ║    ✓ Trains its own LightGBM model from your CSV data               ║
# ║    ✓ Saves all outputs to a new folder: shap_outputs/               ║
# ║                                                                      ║
# ║  Run: python shap_analysis.py                                        ║
# ╚══════════════════════════════════════════════════════════════════════╝

import os
import warnings
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # No display needed — saves files directly
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

warnings.filterwarnings('ignore')

# ── Step 1: Install check ──────────────────────────────────────────────
# If you get ImportError, run in terminal:
#   pip install shap lightgbm scikit-learn matplotlib pandas
try:
    import shap
    import lightgbm as lgb
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import roc_auc_score, classification_report
    print("✓ All libraries imported successfully")
except ImportError as e:
    print(f"✗ Missing library: {e}")
    print("  Run: pip install shap lightgbm scikit-learn matplotlib pandas")
    exit(1)

# ── Step 2: Paths ──────────────────────────────────────────────────────
# This script sits in your project folder alongside the CSV files.
# Change SCRIPT_DIR if you move this file somewhere else.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, 'shap_outputs')
os.makedirs(OUTPUT_DIR, exist_ok=True)
print(f"✓ Output folder ready: {OUTPUT_DIR}")

# ── Step 3: Load your 60-min window data ──────────────────────────────
# Using combined_60min.csv — this is the window your thesis focuses on
# (AUROC 0.8917 for LightGBM at 60-min window)
DATA_FILE = os.path.join(SCRIPT_DIR, 'combined_60min.csv')

if not os.path.exists(DATA_FILE):
    print(f"✗ File not found: {DATA_FILE}")
    print("  Make sure this script is in the same folder as your CSV files.")
    exit(1)

df = pd.read_csv(DATA_FILE)
print(f"✓ Loaded {DATA_FILE}")
print(f"  Rows: {len(df)} | Columns: {len(df.columns)}")
print(f"  CA cases (label=1): {df['label'].sum()} | Non-CA (label=0): {(df['label']==0).sum()}")

# ── Step 4: Prepare features ───────────────────────────────────────────
# Drop non-feature columns — same columns your training code excludes
DROP_COLS = ['caseid', 'label', 'window_min']
FEATURE_COLS = [c for c in df.columns if c not in DROP_COLS]

X = df[FEATURE_COLS].copy()
y = df['label'].copy()

# Handle any NaN values
X = X.fillna(X.median())

print(f"✓ Features: {len(FEATURE_COLS)}")
print(f"  Feature list: {FEATURE_COLS[:6]}... (36 total)")

# ── Step 5: Train/test split ───────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y   # Keep class balance same in both splits
)
print(f"✓ Split — Train: {len(X_train)} | Test: {len(X_test)}")

# ── Step 6: Train LightGBM ─────────────────────────────────────────────
# These are the same hyperparameters from your thesis (60-min window model)
print("\nTraining LightGBM model...")

# Class imbalance ratio for scale_pos_weight
n_neg = (y_train == 0).sum()
n_pos = (y_train == 1).sum()
scale = n_neg / n_pos if n_pos > 0 else 1.0
print(f"  Class ratio (neg/pos): {scale:.2f} → used as scale_pos_weight")

model = lgb.LGBMClassifier(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=6,
    num_leaves=31,
    min_child_samples=20,
    subsample=0.8,
    colsample_bytree=0.8,
    scale_pos_weight=scale,
    random_state=42,
    verbose=-1
)

model.fit(
    X_train, y_train,
    eval_set=[(X_test, y_test)],
    callbacks=[lgb.early_stopping(50, verbose=False),
               lgb.log_evaluation(period=-1)]
)

# Evaluate
y_prob = model.predict_proba(X_test)[:, 1]
auroc  = roc_auc_score(y_test, y_prob)
print(f"✓ Model trained | AUROC on test set: {auroc:.4f}")
print("  (Your thesis reports 0.8917 — minor variation due to random seed is normal)")

# ── Step 7: SHAP Analysis ──────────────────────────────────────────────
print("\nRunning SHAP analysis (this may take 30–60 seconds)...")

# TreeExplainer is the correct explainer for LightGBM — fast and exact
explainer   = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

# LightGBM binary returns list [class0, class1] — we want class 1 (CA=positive)
if isinstance(shap_values, list):
    sv = shap_values[1]  # SHAP values for CA class (label=1)
else:
    sv = shap_values

print(f"✓ SHAP values computed | Shape: {sv.shape}")

# ── Step 8: Plot 1 — Summary Bar Plot (Mean |SHAP|) ────────────────────
# This is the most important plot for your thesis.
# Shows which features drive predictions the most on average.
print("\nGenerating plots...")

plt.style.use('dark_background')
FIG_BG   = '#0d1220'
CARD_BG  = '#070a10'
ACCENT   = '#89b4fa'
GREEN    = '#a6e3a1'
ORANGE   = '#fab387'
RED      = '#f38ba8'
TEXT     = '#cdd6f4'
MUTED    = '#3d4f6e'

# Friendly feature name mapping for thesis figures
SIGNAL_MAP = {
    'HR':         'Heart Rate',
    'PLETH_SPO2': 'SpO₂',
    'ETCO2':      'EtCO₂',
    'ART_MBP':    'Mean BP',
    'ART_SBP':    'Systolic BP',
    'ART_DBP':    'Diastolic BP',
}
STAT_MAP = {
    '_mean':  'Mean',
    '_std':   'Std Dev',
    '_min':   'Min',
    '_max':   'Max',
    '_range': 'Range',
    '_slope': 'Slope',
}

def friendly_name(col):
    """Convert HR_mean → Heart Rate — Mean for thesis figures."""
    for sig_key, sig_label in SIGNAL_MAP.items():
        if col.startswith(sig_key):
            remainder = col[len(sig_key):]
            stat_label = STAT_MAP.get(remainder, remainder)
            return f"{sig_label} — {stat_label}"
    return col

feature_names_friendly = [friendly_name(c) for c in FEATURE_COLS]

# ── Plot 1: Mean absolute SHAP bar chart ──────────────────────────────
mean_abs_shap = np.abs(sv).mean(axis=0)
sorted_idx    = np.argsort(mean_abs_shap)[::-1]
top_n         = 15  # Top 15 features for clean thesis figure

top_idx    = sorted_idx[:top_n]
top_names  = [feature_names_friendly[i] for i in top_idx]
top_vals   = mean_abs_shap[top_idx]

# Assign colours by signal group
sig_colours = {
    'Heart Rate':   '#f38ba8',
    'SpO₂':        '#a6e3a1',
    'EtCO₂':       '#fab387',
    'Mean BP':      '#89b4fa',
    'Systolic BP':  '#cba6f7',
    'Diastolic BP': '#89dceb',
}

bar_colours = []
for name in top_names:
    matched = ACCENT
    for sig_label, colour in sig_colours.items():
        if sig_label in name:
            matched = colour
            break
    bar_colours.append(matched)

fig1, ax1 = plt.subplots(figsize=(10, 7), facecolor=FIG_BG)
ax1.set_facecolor(FIG_BG)

bars = ax1.barh(range(top_n), top_vals[::-1], color=bar_colours[::-1],
                height=0.65, edgecolor='none')

# Value labels on bars
for bar, val in zip(bars, top_vals[::-1]):
    ax1.text(bar.get_width() + 0.0005, bar.get_y() + bar.get_height()/2,
             f'{val:.4f}', va='center', ha='left',
             color=TEXT, fontsize=9, fontfamily='monospace')

ax1.set_yticks(range(top_n))
ax1.set_yticklabels(top_names[::-1], color=TEXT, fontsize=10)
ax1.set_xlabel('Mean |SHAP Value|  (impact on model output magnitude)',
               color=MUTED, fontsize=10)
ax1.set_title(
    'Feature Importance via SHAP — LightGBM (60-min Window)\n'
    'Cardiac Arrest Prediction · VitalDB Dataset · TSI 2026',
    color=TEXT, fontsize=12, fontweight='bold', pad=15
)
ax1.tick_params(colors=MUTED, labelsize=9)
ax1.spines[['top','right','left']].set_visible(False)
ax1.spines['bottom'].set_color(MUTED)
ax1.xaxis.label.set_color(MUTED)
ax1.grid(axis='x', color='#1a2035', linewidth=0.5, linestyle='--')

# Legend by signal
legend_patches = [mpatches.Patch(color=c, label=s)
                  for s, c in sig_colours.items()]
ax1.legend(handles=legend_patches, loc='lower right',
           facecolor=FIG_BG, edgecolor=MUTED,
           labelcolor=TEXT, fontsize=8, title='Vital Signal',
           title_fontsize=8)

plt.tight_layout()
out1 = os.path.join(OUTPUT_DIR, 'shap_bar_top15.png')
fig1.savefig(out1, dpi=150, bbox_inches='tight', facecolor=FIG_BG)
plt.close(fig1)
print(f"  ✓ Saved: shap_bar_top15.png")

# ── Plot 2: SHAP Beeswarm / Summary Dot Plot ──────────────────────────
# Shows direction — red dots = high feature value pushes risk UP
# This goes in your thesis as the interpretability figure

fig2, ax2 = plt.subplots(figsize=(10, 8), facecolor=FIG_BG)
ax2.set_facecolor(FIG_BG)

top15_sv   = sv[:, top_idx]          # SHAP values for top 15 features
top15_Xval = X_test.values[:, top_idx]  # Actual feature values

# Normalise feature values 0→1 for colour mapping
for i in range(top_n):
    col_vals = top15_Xval[:, i]
    col_min, col_max = col_vals.min(), col_vals.max()
    norm = (col_vals - col_min) / (col_max - col_min + 1e-9)

    # Jitter y position so dots don't overlap
    y_jitter = np.random.default_rng(i).uniform(-0.3, 0.3, len(norm))
    y_pos    = (top_n - 1 - i) + y_jitter

    scatter = ax2.scatter(
        top15_sv[:, i], y_pos,
        c=norm, cmap='RdYlBu_r',
        alpha=0.5, s=8, linewidths=0
    )

# Colour bar
cbar = plt.colorbar(scatter, ax=ax2, pad=0.01, fraction=0.02)
cbar.set_label('Feature value\n(blue=low, red=high)', color=MUTED, fontsize=9)
cbar.ax.yaxis.set_tick_params(color=MUTED, labelcolor=MUTED, labelsize=8)
cbar.outline.set_edgecolor(MUTED)

ax2.set_yticks(range(top_n))
ax2.set_yticklabels(top_names[::-1], color=TEXT, fontsize=10)
ax2.axvline(0, color=MUTED, linewidth=0.8, linestyle='--')
ax2.set_xlabel('SHAP Value  (positive = increases CA risk prediction)',
               color=MUTED, fontsize=10)
ax2.set_title(
    'SHAP Beeswarm Plot — LightGBM Feature Impact Direction\n'
    'Cardiac Arrest Prediction · VitalDB Dataset · TSI 2026',
    color=TEXT, fontsize=12, fontweight='bold', pad=15
)
ax2.tick_params(colors=MUTED, labelsize=9)
ax2.spines[['top','right']].set_visible(False)
ax2.spines[['left','bottom']].set_color(MUTED)
ax2.grid(axis='x', color='#1a2035', linewidth=0.5, linestyle='--')

plt.tight_layout()
out2 = os.path.join(OUTPUT_DIR, 'shap_beeswarm_top15.png')
fig2.savefig(out2, dpi=150, bbox_inches='tight', facecolor=FIG_BG)
plt.close(fig2)
print(f"  ✓ Saved: shap_beeswarm_top15.png")

# ── Plot 3: Top 3 signal SHAP dependence plots ────────────────────────
# Shows exactly how each feature value affects risk — good for thesis discussion
top3_idx = sorted_idx[:3]

fig3, axes = plt.subplots(1, 3, figsize=(15, 5), facecolor=FIG_BG)

for ax, feat_i in zip(axes, top3_idx):
    ax.set_facecolor(FIG_BG)
    feat_name = feature_names_friendly[feat_i]
    feat_vals = X_test.values[:, feat_i]
    shap_vals = sv[:, feat_i]

    sc = ax.scatter(feat_vals, shap_vals,
                    c=shap_vals, cmap='RdYlBu_r',
                    alpha=0.5, s=10, linewidths=0)
    ax.axhline(0, color=MUTED, linewidth=0.8, linestyle='--')
    ax.set_xlabel(feat_name, color=MUTED, fontsize=9)
    ax.set_ylabel('SHAP Value', color=MUTED, fontsize=9)
    ax.set_title(feat_name, color=TEXT, fontsize=10, fontweight='bold')
    ax.tick_params(colors=MUTED, labelsize=8)
    ax.spines[['top','right']].set_visible(False)
    ax.spines[['left','bottom']].set_color(MUTED)
    ax.grid(color='#1a2035', linewidth=0.4, linestyle='--')
    plt.colorbar(sc, ax=ax).outline.set_edgecolor(MUTED)

fig3.suptitle(
    'SHAP Dependence Plots — Top 3 Predictors\n'
    'How each feature value shifts the CA risk prediction',
    color=TEXT, fontsize=11, fontweight='bold'
)
fig3.patch.set_facecolor(FIG_BG)
plt.tight_layout()
out3 = os.path.join(OUTPUT_DIR, 'shap_dependence_top3.png')
fig3.savefig(out3, dpi=150, bbox_inches='tight', facecolor=FIG_BG)
plt.close(fig3)
print(f"  ✓ Saved: shap_dependence_top3.png")

# ── Step 9: Save SHAP values as CSV for thesis appendix ───────────────
shap_df = pd.DataFrame(sv, columns=feature_names_friendly)
shap_csv = os.path.join(OUTPUT_DIR, 'shap_values_test_set.csv')
shap_df.to_csv(shap_csv, index=False)
print(f"  ✓ Saved: shap_values_test_set.csv")

# ── Step 10: Print thesis-ready summary table ──────────────────────────
print("\n" + "="*60)
print("THESIS-READY SHAP SUMMARY TABLE")
print("Copy this into your Results section (Section 4.x)")
print("="*60)
print(f"\nModel: LightGBM | Window: 60-min | AUROC: {auroc:.4f}")
print(f"SHAP explainer: TreeExplainer (exact, not approximate)")
print(f"Test set size: {len(X_test)} samples\n")
print(f"{'Rank':<5} {'Feature':<35} {'Mean |SHAP|':<14} {'Direction'}")
print("-"*70)

for rank, idx in enumerate(sorted_idx[:10], 1):
    fname  = feature_names_friendly[idx]
    mshap  = mean_abs_shap[idx]
    # Direction: positive mean SHAP = higher value → more risk
    mean_signed = sv[:, idx].mean()
    direction   = "↑ Risk" if mean_signed > 0 else "↓ Risk"
    print(f"{rank:<5} {fname:<35} {mshap:<14.4f} {direction}")

print("\n" + "="*60)
print("ALL OUTPUTS SAVED TO:", OUTPUT_DIR)
print("Files:")
print("  • shap_bar_top15.png       → Figure for thesis Results")
print("  • shap_beeswarm_top15.png  → Figure for thesis Discussion")
print("  • shap_dependence_top3.png → Figure for thesis Appendix")
print("  • shap_values_test_set.csv → Raw data for appendix")
print("="*60)
print("\n✓ SHAP analysis complete. Your existing files were not modified.")
