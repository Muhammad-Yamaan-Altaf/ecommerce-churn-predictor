import pandas as pd

try:
    features = pd.read_csv('data/raw/ecommerce_customer_features.csv')
    targets = pd.read_csv('data/raw/ecommerce_customer_targets.csv')
    
    print(f"Features loaded: {features.shape[0]} rows")
    print(f"Targets loaded: {targets.shape[0]} rows")

    df = pd.merge(features, targets, on='Customer_ID', how='inner')
    print("Data successfully merged on 'Customer_ID'.")

    df.fillna(df.median(numeric_only=True), inplace=True)
    print("Missing numeric values filled.")

    output_path = 'data/processed/ecommerce_churn_cleaned.csv'
    df.to_csv(output_path, index=False)
    
    print(f"Data cleaning complete! File saved at: {output_path}")

except Exception as e:
    print(f"Error: {e}")