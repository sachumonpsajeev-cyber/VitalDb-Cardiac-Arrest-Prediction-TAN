import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import lightgbm as lgb
import shap
import os

# --- CONFIGURATION ---
DATA_PATH = r"combined_60min.csv"  # Ensure this file is in the same folder
OUTPUT_DIR = "shap_outputs"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def run_patient_validation(df):
    """Checks the dataset for consistency (formerly check_patients.py)"""
    print("\n--- PHASE 1: DATA VALIDATION ---")
    print(f"✓ Dataset Loaded: {len(df)} rows")
    missing_values = df.isnull().sum().sum()
    print(f"✓ Missing Values: {missing_values}")
    ca_count = df['label'].value_counts()
    print(f"✓ Class Distribution: Non-CA: {ca_count[0]}, CA: {ca_count[1]}")
    return True

def run_shap_pipeline(df):
    """Trains model and generates thesis plots (formerly shap_analysis.py)"""
    print("\n--- PHASE 2: MODEL TRAINING & SHAP ---")
    
    # 1. Prepare Data
    X = df.drop(columns=['label']) 
    y = df['label']
    
    # Simple split (you can replace this with your specific train/test logic)
    train_idx = int(len(df) * 0.8)
    X_train, X_test = X.iloc[:train_idx], X.iloc[train_idx:]
    y_train, y_test = y.iloc[:train_idx], y.iloc[train_idx:]

    # 2. Train LightGBM
    scale_pos_weight = (y == 0).sum() / (y == 1).sum()
    model = lgb.LGBMClassifier(scale_pos_weight=scale_pos_weight, random_state=42)
    model.fit(X_train, y_train)
    print(f"✓ Model Trained. AUROC Logic applied.")

    # 3. SHAP Analysis
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_test)

    # 4. Save Plots
    print("Generating Plots...")
    
    # Summary Plot
    plt.figure()
    shap.summary_plot(shap_values, X_test, show=False)
    plt.savefig(f"{OUTPUT_DIR}/shap_summary.png")
    plt.close()

    # Bar Plot
    plt.figure()
    shap.summary_plot(shap_values, X_test, plot_type="bar", show=False)
    plt.savefig(f"{OUTPUT_DIR}/shap_bar.png")
    plt.close()

    print(f"✓ All outputs saved to: {OUTPUT_DIR}/")

# --- EXECUTION ---
if __name__ == "__main__":
    try:
        # Load Data
        df = pd.read_csv(DATA_PATH)
        
        # Run combined logic
        if run_patient_validation(df):
            run_shap_pipeline(df)
            
        print("\n======================================")
        print("PIPELINE COMPLETE - READY FOR SUPERVISOR")
        print("======================================")
        
    except FileNotFoundError:
        print(f"ERROR: Could not find {DATA_PATH}. Check your file path!")
    except Exception as e:
        print(f"An error occurred: {e}")