# 📉 E-Commerce Customer Churn Predictor

An end-to-end Machine Learning web application designed to predict whether an e-commerce customer is at risk of churning (leaving the platform). This allows businesses to proactively target at-risk customers with retention strategies.

## 🚀 Project Overview
[cite_start]This project features a fully automated data pipeline that ingests raw customer data, merges features and targets, cleans missing values, and trains a highly accurate Random Forest Classifier[cite: 146, 152]. The prediction engine is then served through an interactive, lightning-fast Streamlit web dashboard.

### 📊 Model Performance
* [cite_start]**Algorithm:** Random Forest Classifier [cite: 25]
* [cite_start]**Accuracy:** 96.58% 
* **Features Used:** Account Age, Avg Order Value, Loyalty Status, Return Rate, Satisfaction Score, etc.

### ⚙️ Tech Stack Used:
* [cite_start]**Data Processing & EDA:** Pandas, NumPy, Matplotlib, Seaborn [cite: 18, 19, 20, 21]
* [cite_start]**Machine Learning:** Scikit-Learn [cite: 22]
* [cite_start]**Categorical Encoding:** OrdinalEncoder [cite: 138]
* **Web App / UI:** Streamlit

## 📂 Project Structure
* `data/raw/`: Contains the original Kaggle datasets (`features.csv` & `targets.csv`).
* `data/processed/`: Contains the merged and cleaned data ready for training.
* `src/ingest.py`: Data ingestion and validation script.
* `src/clean.py`: Automated merging and cleaning pipeline.
* `src/train.py`: Model training, encoding, and artifact generation script.
* `src/app.py`: The frontend Streamlit dashboard.

## 🛠️ How to Run Locally
1. Clone this repository.
2. Create a virtual environment and activate it.
3. Install the dependencies: `pip install -r requirements.txt`
4. Run the data pipeline (optional if models are already generated):
   ```bash
   python src/ingest.py
   python src/clean.py
   python src/train.py
5. Launch the Streamlit App: streamlit run src/app.py

Developed as part of a professional Data Science & Machine Learning portfolio.