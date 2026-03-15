import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier

# Load dataset
df = pd.read_csv("data/telco_churn.csv")

# Clean data
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df.fillna(0, inplace=True)

# Convert target
df["Churn"] = df["Churn"].map({"Yes":1,"No":0})

# Use only 3 features
X = df[["tenure","MonthlyCharges","TotalCharges"]]
y = df["Churn"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train model
model = XGBClassifier(eval_metric="logloss")

model.fit(X_train, y_train)

# Accuracy
pred = model.predict(X_test)
acc = accuracy_score(y_test, pred)

print("Model Accuracy:", acc)

# Save model
model_data = {
    "model": model,
    "scaler": scaler,
    "features": ["tenure","MonthlyCharges","TotalCharges"]
}

pickle.dump(model_data, open("models/churn_model.pkl","wb"))

print("Model saved successfully")
print("Model Type:", type(model))