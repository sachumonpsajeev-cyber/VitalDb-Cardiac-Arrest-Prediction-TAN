import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import lightgbm as lgb
import shap
import os
import streamlit as st

# =================================================================
# SECTION 1: RESEARCH ENGINE (Multi-Window Analysis Logic)
# =================================================================

def run_research_pipeline():
    """Trains models for 30, 60, 120, and 240 minute windows and saves SHAP plots."""
    WINDOWS = ["30min", "60min", "120min", "240min"]
    OUTPUT_ROOT = "thesis_results"
    
    if not os.path.exists(OUTPUT_ROOT):
        os.makedirs(OUTPUT_ROOT)

    for window in WINDOWS:
        file_name = f"combined_{window}.csv"
        if not os.path.exists(file_name):
            print(f"Skipping {file_name}: File not found.")
            continue
            
        # 1. Load and Split
        df = pd.read_csv(file_name)
        X = df.drop(columns=['label'])
        y = df['label']
        
        # 2. Train LightGBM
        # Handle imbalance automatically using the ratio of classes
        ratio = (y == 0).sum() / (y == 1).sum()
        model = lgb.LGBMClassifier(scale_pos_weight=ratio, random_state=42, verbosity=-1)
        model.fit(X, y)
        
        # 3. Generate SHAP
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(X)
        target_shap = shap_values[1] if isinstance(shap_values, list) else shap_values
        
        # 4. Save Plot to disk
        plt.figure()
        shap.summary_plot(target_shap, X, show=False)
        plt.title(f"SHAP Analysis: {window}")
        plt.savefig(f"{OUTPUT_ROOT}/summary_{window}.png")
        plt.close()
        print(f"✓ Analysis for {window} complete.")

# =================================================================
# SECTION 2: DASHBOARD INTERFACE (Streamlit Code)
# =================================================================

def run_streamlit_dashboard():
    """This section contains all the code for your visual dashboard."""
    st.title("Cardiac Arrest Prediction Dashboard")
    st.sidebar.header("Settings")
    
    window_choice = st.sidebar.selectbox("Select Prediction Window", ["30min", "60min", "120min", "240min"])
    
    file_path = f"combined_{window_choice}.csv"
    
    if os.path.exists(file_path):
        data = pd.read_csv(file_path)
        st.write(f"### Current Dataset: {window_choice}")
        st.write(data.head())
        
        # Show analysis results if they exist
        img_path = f"thesis_results/summary_{window_choice}.png"
        if os.path.exists(img_path):
            st.image(img_path, caption=f"SHAP Importance for {window_choice}")
        else:
            st.warning("Please run the Analysis Engine first to generate plots.")
    else:
        st.error(f"Dataset {file_path} not found in directory.")

# =================================================================
# SECTION 3: EXECUTION LOGIC
# =================================================================

if __name__ == "__main__":
    # If you run this normally (python file.py), it runs the analysis
    # If you run it via streamlit (streamlit run file.py), it shows the dashboard
    
    # Check if we are inside a streamlit process
    try:
        from streamlit.runtime.scriptrunner import get_script_run_ctx
        if get_script_run_ctx():
            run_streamlit_dashboard()
        else:
            print("No Streamlit context found. Running Research Analysis...")
            run_research_pipeline()
    except ImportError:
        run_research_pipeline()