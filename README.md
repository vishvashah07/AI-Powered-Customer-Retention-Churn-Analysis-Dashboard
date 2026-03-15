AI-Powered Customer Retention & Churn Analysis DashboardAn end-to-end AI analytics solution designed to analyze telecom customer behavior, predict churn probability, and generate automated business strategies using Generative AI.🚀 Project OverviewCustomer churn is a critical challenge in the telecom industry, directly impacting recurring revenue. This project addresses this by combining Machine Learning, Interactive Data Visualization, and Generative AI to provide a 360-degree view of customer retention.Key Objectives:Identify high-risk customers before they leave.Understand the underlying drivers behind customer attrition.Provide actionable, AI-driven retention strategies.🏗️ System ArchitectureCode snippetgraph TD
    User((User)) --> Dashboard[Streamlit Dashboard]
    Dashboard --> Viz[Data Visualization]
    Dashboard --> ML[ML Prediction Model]
    ML --> Prob[Churn Probability]
    Viz --> AI[AI Insight Engine]
    AI --> Gemini[Gemini API]
    Gemini --> Recs[Business Recommendations]
Project WorkflowData Ingestion: Loading the Telecom Customer dataset.Preprocessing: Data cleaning and Feature Engineering.Modeling: Training a Classification Model (e.g., Random Forest) to predict churn.Deployment: Integrating the saved model (.pkl) into a Streamlit interface.AI Integration: Utilizing the Gemini API to interpret data trends and suggest improvements.📊 Dataset & FeaturesThe system utilizes telecom customer data covering demographics, account information, and service usage.FeatureDescriptionTenureNumber of months the customer has stayed with the companyMonthlyChargesThe amount charged to the customer monthlyTotalChargesThe total amount charged to the customerContractThe contract term (Month-to-month, One year, Two year)Churn (Target)Whether the customer stayed or left (Yes/No)✨ Key Features1. Customer Analytics DashboardInteractive visualizations powered by Plotly/Seaborn to explore:Churn distribution across different contract types.Correlation between Monthly Charges and Retention.Tenure-based cohorts.2. ML Churn PredictionA dedicated interface where users can input customer parameters to receive an instant churn probability score.Input: Tenure, Contract Type, Charges, etc.Output: Predictive classification (Likely to Churn / Likely to Stay).3. AI-Generated Business InsightsIntegrated with the Gemini API to transform raw data into narrative insights.Identifies hidden patterns in high-risk segments.Suggests specific retention maneuvers (e.g., "Transition month-to-month users to annual plans").📁 Project StructurePlaintextcustomer-churn-project
│
├── app.py                # Main Streamlit application
├── data/
│   └── telco_churn.csv   # Raw dataset
├── models/
│   └── churn_model.pkl   # Trained Machine Learning model
├── .env                  # API Key configuration (ignored by git)
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
🛠️ Installation & Setup1. Clone the RepositoryBashgit clone https://github.com/vishvashah07/customer-churn-project.git
cd customer-churn-project
2. Install DependenciesBashpip install -r requirements.txt
3. Configure Gemini APIObtain an API key from Google AI Studio.Create a .env file in the root directory:PlaintextGEMINI_API_KEY=your_api_key_here
4. Run the ApplicationBashstreamlit run app.py
🔮 Future RoadmapCloud Deployment: Hosting the dashboard on AWS or Streamlit Cloud.Real-time API: Creating a FastAPI endpoint for external model consumption.Deep Learning: Implementing Neural Networks for improved accuracy on larger datasets.Automated Retraining: Setting up a pipeline to update the model as new data arrives.Author: Vishva ShahFocus: Information Technology & Data Science
