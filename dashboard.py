import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import os
from dotenv import load_dotenv
from google import genai



load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

st.set_page_config(page_title="Customer Dashboard", layout="wide")

st.title("Customer Retention & Leaving Analysis Dashboard")

st.write("""
This dashboard analyzes customer behaviour and helps identify customers
who might leave the telecom service.
""")

# ==========================
# Load Dataset
# ==========================

df = pd.read_csv("data/telco_churn.csv")

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df.fillna(0, inplace=True)

# ==========================
# Load Model
# ==========================

model = None
scaler = None
features = None

model_path = "models/churn_model.pkl"

if os.path.exists(model_path):

    model_data = pickle.load(open(model_path, "rb"))

    if isinstance(model_data, dict):
        model = model_data["model"]
        scaler = model_data["scaler"]
        features = model_data["features"]
    else:
        model = model_data

# ==========================
# AI SUMMARY FUNCTION
# ==========================

def generate_ai_summary(data):

    prompt = f"""
    Analyze this telecom customer dataset summary and provide insights.

    Dataset summary:
    {data}

    Provide:
    1. Main reason customers leave
    2. High-risk customer segment
    3. Suggested retention strategy
    """

    try:

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Gemini AI summary failed: {str(e)}"


# ==========================
# TABS
# ==========================

tab1, tab2, tab3 = st.tabs([
    "Customer Overview",
    "Predict if Customer Might Leave",
    "Model Insights"
])

# ===================================================
# ANALYTICS TAB
# ===================================================

with tab1:

    st.subheader("Customer Overview")

    col1, col2, col3 = st.columns(3)

    churn_rate = (df["Churn"].value_counts(normalize=True)["Yes"]) * 100

    col1.metric("Total Customers", len(df))
    col2.metric("Customers Leaving (%)", round(churn_rate,2))
    col3.metric("Avg Monthly Charges", round(df["MonthlyCharges"].mean(),2))

    st.divider()

    col4, col5 = st.columns(2)

    with col4:

        st.subheader("Customers Staying vs Leaving")

        fig, ax = plt.subplots()
        sns.countplot(x="Churn", data=df, ax=ax)
        st.pyplot(fig)

    with col5:

        st.subheader("Contract Type vs Customers Leaving")

        fig, ax = plt.subplots()
        sns.countplot(x="Contract", hue="Churn", data=df, ax=ax)
        st.pyplot(fig)

    col6, col7 = st.columns(2)

    with col6:

        st.subheader("Monthly Charges Distribution")

        fig, ax = plt.subplots()
        sns.histplot(df["MonthlyCharges"], bins=30, ax=ax)
        st.pyplot(fig)

    with col7:

        st.subheader("How Long Customers Stay Before Leaving")

        fig, ax = plt.subplots()
        sns.boxplot(x="Churn", y="tenure", data=df, ax=ax)
        st.pyplot(fig)

# ===================================================
# PREDICTION TAB
# ===================================================

with tab2:

    st.subheader("Predict if a Customer Might Leave the Service")

    if model is None:

        st.warning("Model not found. Train the model first.")

    else:

        col1, col2, col3 = st.columns(3)

        with col1:
            tenure = st.slider("Customer Tenure (months)", 0, 72, 12)

        with col2:
            monthly = st.slider("Monthly Charges", 0, 200, 70)

        with col3:
            total = st.slider("Total Charges", 0, 10000, 800)

        sample = pd.DataFrame({
            "tenure":[tenure],
            "MonthlyCharges":[monthly],
            "TotalCharges":[total]
        })

        colA, colB = st.columns(2)

        # Prediction Button
        with colA:

            if st.button("Check if Customer Might Leave"):

                if features is not None:

                    for col in features:
                        if col not in sample.columns:
                            sample[col] = 0

                    sample = sample[features]

                if scaler is not None:
                    sample = scaler.transform(sample)

                prediction = model.predict(sample)

                if hasattr(model,"predict_proba"):
                    prob = model.predict_proba(sample)[0][1]
                else:
                    prob = None

                st.subheader("Prediction Result")

                if prediction[0] == 1:
                    st.error("This customer is likely to leave the service.")
                else:
                    st.success("This customer is likely to continue using the service.")

                if prob is not None:
                    st.write("Chance that customer may leave:", round(prob*100,2), "%")

        # AI Summary Button
        with colB:

            if st.button("Generate AI Summary"):

                dataset_summary = df.describe(include="all").to_string()

                with st.spinner("Generating AI insights..."):
                    ai_output = generate_ai_summary(dataset_summary)

                st.subheader("AI Insights")

                st.write(ai_output)

# ===================================================
# MODEL INSIGHTS TAB
# ===================================================

with tab3:

    st.subheader("Feature Importance")

    if model is None:

        st.warning("Train the model first.")

    else:

        if hasattr(model,"feature_importances_") and features is not None:

            importance = model.feature_importances_

            imp_df = pd.DataFrame({
                "Feature":features,
                "Importance":importance
            })

            imp_df = imp_df.sort_values(by="Importance", ascending=False).head(10)

            fig, ax = plt.subplots()

            sns.barplot(x="Importance", y="Feature", data=imp_df, ax=ax)

            st.pyplot(fig)

        else:

            st.info("Feature importance not available.")

st.divider()

st.markdown("### Project Author")

st.markdown("""
**Vishva Shah**

Information Technology Student

GitHub: https://github.com/vishvashah07

Project: AI Powered Customer Retention & Churn Analysis Dashboard
""")