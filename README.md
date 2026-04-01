# AI-Powered Customer Retention & Churn Analysis Dashboard

An end-to-end AI analytics solution designed to analyze telecom customer behavior, predict churn probability, and generate automated business strategies using Generative AI.

## 🚀 Project Overview

Customer churn is a critical challenge in the telecom industry, directly impacting recurring revenue. This project addresses this by combining **Machine Learning**, **Interactive Data Visualization**, and **Generative AI** to provide a 360-degree view of customer retention.

**Key Objectives:**

* Identify high-risk customers before they leave.
* Understand the underlying drivers behind customer attrition.
* Provide actionable, AI-driven retention strategies.

---

## 🏗️ System Architecture

```mermaid
graph TD
    User((User)) --> Dashboard[Streamlit Dashboard]
    Dashboard --> Viz[Data Visualization]
    Dashboard --> ML[ML Prediction Model]
    ML --> Prob[Churn Probability]
    Viz --> AI[AI Insight Engine]
    AI --> Gemini[Gemini API]
    Gemini --> Recs[Business Recommendations]

```

### Project Workflow

1. **Data Ingestion:** Loading the Telecom Customer dataset.
2. **Preprocessing:** Data cleaning and Feature Engineering.
3. **Modeling:** Training the Classification Model XGBoost to predict churn.
4. **Deployment:** Integrating the saved model (`.pkl`) into a Streamlit interface.
5. **AI Integration:** Utilizing the Gemini API to interpret data trends and suggest improvements.

---# 🛠️ Technical Stack

This project leverages a modern data science and web stack to deliver high-performance churn predictions and AI-driven business intelligence.

---

## 🧠 Machine Learning & Data Science
| Technology | Usage |
| :--- | :--- |
| **Python 3.9+** | Primary programming language for data pipelines and modeling. |
| **XGBoost** | High-performance gradient boosting framework used for the core classification model. |
| **Scikit-Learn** | Used for data splitting, feature scaling (`StandardScaler`), and model evaluation. |
| **Pandas & NumPy** | Essential libraries for data manipulation, cleaning, and numerical operations. |
| **Matplotlib & Seaborn** | Powering the exploratory data analysis (EDA) and static visualizations. |

---

## 🤖 Generative AI & Intelligence
* **Engine:** [Google Gemini API](https://aistudio.google.com/app/apikey) (`google-generativeai`)
* **Role:** Acts as the "Insight Engine," automatically interpreting complex dataset statistics to provide human-readable retention strategies and business recommendations.

---

## 🌐 Web Frameworks & API
* **Frontend Dashboard:** [Streamlit](https://streamlit.io/) — Chosen for its ability to create interactive, data-rich user interfaces with Python.
* **Backend API:** [Flask](https://flask.palletsprojects.com/) 
* **Security:** `python-dotenv` for managing sensitive API credentials locally.

---

## ⚙️ DevOps & Tools
* **Version Control:** Git & GitHub for collaborative development and source tracking.
* **Serialization:** `Pickle` for saving the trained model and preprocessing pipeline (Scaler) to ensure consistency between training and production.


---
## 📊 Dataset & Features

The system utilizes telecom customer data covering demographics, account information, and service usage.

| Feature | Description |
| --- | --- |
| **Tenure** | Number of months the customer has stayed with the company |
| **MonthlyCharges** | The amount charged to the customer monthly |
| **TotalCharges** | The total amount charged to the customer |
| **Contract** | The contract term (Month-to-month, One year, Two year) |
| **Churn (Target)** | Whether the customer stayed or left (**Yes/No**) |

---

## ✨ Key Features

### 1. Customer Analytics Dashboard

Interactive visualizations powered by Matplotlib & Seaborn to explore:

* Churn distribution across different contract types.
* Correlation between Monthly Charges and Retention.
* Tenure-based analysis.

### 2. ML Churn Prediction

A dedicated interface where users can input customer parameters to receive an instant churn probability score.

* **Input:** Tenure, Contract Type, Charges, etc.
* **Output:** Predictive classification (Likely to Churn / Likely to Stay).

### 3. AI-Generated Business Insights

Integrated with the **Gemini API** to transform raw data into narrative insights.

* Identifies hidden patterns in high-risk segments.
* Suggests specific retention maneuvers (e.g., "Transition month-to-month users to annual plans").

---

## 📁 Project Structure

```text
customer-churn-project
│
├── data/                          # Dataset used for training and analysis
│
├── models/                        # Saved trained models
│   └── churn_model.pkl            # Trained XGBoost churn prediction model
│
├── src/                           # Core source code
│   ├── data_preprocessing.py      # Data cleaning and preprocessing
│   ├── model_training.py          # Training the XGBoost classification model
│   └── prediction.py              # Functions used for churn prediction
│
├── app.py                         # Main Streamlit dashboard entry point
├── dashboard.py                   # Dashboard layout and visualization logic
│
├── .env                           # API keys (not pushed to GitHub)
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation

```

---

## 🛠️ Installation & Setup

**1. Clone the Repository**

```bash
git clone https://github.com/vishvashah07/customer-churn-project.git
cd customer-churn-project

```

**2. Install Dependencies**

```bash
pip install -r requirements.txt

```

**3. Configure Gemini API**

* Obtain an API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
* Create a `.env` file in the root directory:
```text
GEMINI_API_KEY=your_api_key_here

```



**4. Run the Application**

```bash
streamlit run dashboard.py

```

---

## 🔮 Future Roadmap

* **Cloud Deployment:** Hosting the dashboard on AWS or Streamlit Cloud.
* **Real-time API:** Creating a FastAPI endpoint for external model consumption.
* **Deep Learning:** Implementing Neural Networks for improved accuracy on larger datasets.
* **Automated Retraining:** Setting up a pipeline to update the model as new data arrives.

---

**Author:** [Vishva Shah](https://github.com/vishvashah07)

**Focus:** Information Technology & Data Science


