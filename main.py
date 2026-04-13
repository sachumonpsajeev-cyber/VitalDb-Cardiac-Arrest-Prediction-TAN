# main.py - The Master Script

import check_patients
import shap_analysis
# import share_dashboard  # Un-comment to run the dashboard logic

def run_full_pipeline():
    print("--- Phase 1: Checking Patient Data ---")
    # Assuming check_patients has a function called main() or similar
    check_patients.run_validation() 

    print("--- Phase 2: Running SHAP Analysis ---")
    # Access logic from your shap_analysis.py file
    shap_analysis.generate_plots()

    print("--- Phase 3: Launching Dashboard ---")
    # Logic to trigger your dashboard
    
if __name__ == "__main__":
    run_full_pipeline()