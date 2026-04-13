import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import lightgbm as lgb
import shap
import os

# --- CONFIGURATION ---
# List all the windows you want to analyze
WINDOWS = ["30min", "60min", "120min", "240min"]
BASE_FILENAME = "combined_{}.csv" # This will look for combined_30min.csv, etc.
OUTPUT_ROOT = "thesis_results"

if not os.path.exists(OUTPUT_ROOT):
    os.makedirs(OUTPUT_ROOT)

def run_analysis_for_window(window_name):
    print(f"\n{'='*20}")
    print(f" PROCESSING WINDOW: {window_name} ")
    print(f"{'='*20}")
    
    file_path = BASE_FILENAME.format(window_name)
    window_dir = os.path.join(OUTPUT_ROOT, window_name)
    
    if not os.path.exists(window_dir):
        os.makedirs(window_dir)

    try:
        # 1. Load Data
        df = pd.read_csv(file_path)
        print(f"✓ Loaded {file_path} ({len(df)} rows)")

        # 2. Prepare Data
        X = df.drop(columns=['label']) 
        y = df['label']
        
        # Chronological Split (standard for medical time-series)
        train_idx = int(len(df) * 0.8)
        X_train, X_test = X.iloc[:train_idx], X.iloc[train_idx:]
        y_train, y_test = y.iloc[:train_idx], y.iloc[train_idx:]

        # 3. Train Model with Imbalance Handling
        pos_count = sum(y_train == 1)
        neg_count = sum(y_train == 0)
        scale_weight = neg_count / pos_count if pos_count > 0 else 1
        
        model = lgb.LGBMClassifier(
            scale_pos_weight=scale_weight, 
            random_state=42,
            verbosity=-1
        )
        model.fit(X_train, y_train)
        print(f"✓ Model Trained (Scale Weight: {scale_weight:.2f})")

        # 4. SHAP Interpretability
        print("✓ Computing SHAP values...")
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(X_test)

        # Handle LightGBM SHAP output format (list vs ndarray)
        if isinstance(shap_values, list):
            shap_vals_to_plot = shap_values[1] # Class 1 (Cardiac Arrest)
        else:
            shap_vals_to_plot = shap_values

        # 5. Save Plots
        plt.figure(figsize=(10, 6))
        shap.summary_plot(shap_vals_to_plot, X_test, show=False)
        plt.title(f"Impact on Cardiac Arrest - {window_name}")
        plt.tight_layout()
        plt.savefig(os.path.join(window_dir, f"shap_summary_{window_name}.png"))
        plt.close()

        print(f"✓ Results saved to {window_dir}")

    except FileNotFoundError:
        print(f"× Error: {file_path} not found. Skipping...")
    except Exception as e:
        print(f"× An error occurred for {window_name}: {e}")

# --- EXECUTION ---
if __name__ == "__main__":
    for window in WINDOWS:
        run_analysis_for_window(window)
        
    print("\n" + "="*40)
    print("ALL WINDOW PREDICTIONS COMPLETE")
    print(f"Check the '{OUTPUT_ROOT}' folder for your thesis figures.")
    print("="*40)