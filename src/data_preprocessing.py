import pandas as pd

def load_and_preprocess_data(filepath):

    df = pd.read_csv(filepath)

    # Remove customer ID
    if "customerID" in df.columns:
        df.drop("customerID", axis=1, inplace=True)

    # Convert TotalCharges to numeric
    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Fill missing values
    df.fillna(df.mean(numeric_only=True), inplace=True)

    # Convert target variable
    df["Churn"] = df["Churn"].map({"Yes":1, "No":0})

    # Convert categorical features
    df = pd.get_dummies(df, drop_first=True)

    return df