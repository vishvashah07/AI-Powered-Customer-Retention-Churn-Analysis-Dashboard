import pickle
import numpy as np

# Load trained model
model = pickle.load(open("../models/churn_model.pkl", "rb"))

# Example customer data
sample_data = np.array([[12,70,800]])

prediction = model.predict(sample_data)

if prediction[0] == 1:
    print("Customer will churn")
else:
    print("Customer will stay")