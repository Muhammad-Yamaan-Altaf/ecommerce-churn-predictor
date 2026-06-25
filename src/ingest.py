import os
import pandas as pd

print("Data Ingestion & Validation System Start...")

features_path = 'data/raw/ecommerce_customer_features.csv'
targets_path = 'data/raw/ecommerce_customer_targets.csv'

if os.path.exists(features_path) and os.path.exists(targets_path):
    print("Success: Raw datasets found in 'data/raw/'.")
    
    features_df = pd.read_csv(features_path)
    targets_df = pd.read_csv(targets_path)
    
    print(f"Features Total Rows: {len(features_df):,}")
    print(f"Targets Total Rows: {len(targets_df):,}") 

    if 'Customer_ID' in features_df.columns and 'Customer_ID' in targets_df.columns:
        print("Validation Passed: 'Customer_ID' exists in both files for merging.")
    else:
        print("Critical Error: 'Customer_ID' is missing from one or both files!")
        
else:
    print("Error: Datasets missing!")
    print("Please ensure both CSV files are placed inside the 'data/raw/' folder.")