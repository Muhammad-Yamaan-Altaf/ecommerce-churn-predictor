import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load cleaned data
df = pd.read_csv('data/processed/ecommerce_churn_cleaned.csv')

if 'Customer_ID' in df.columns:
    df = df.drop('Customer_ID', axis=1)

X = df.drop('churned', axis=1)
y = df['churned']

obj_cols = X.select_dtypes(include=['object']).columns

encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
X[obj_cols] = encoder.fit_transform(X[obj_cols])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=250, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Model Accuracy on Test Data: {acc * 100:.2f}%")

# Save the model, encoder, and columns for future use
with open('src/model.pkl', 'wb') as f:
    pickle.dump(model, f)
    
with open('src/encoder.pkl', 'wb') as f:
    pickle.dump(encoder, f)
    
with open('src/columns.pkl', 'wb') as f:
    pickle.dump(list(X.columns), f)
    
with open('src/cat_columns.pkl', 'wb') as f:
    pickle.dump(list(obj_cols), f)
