from flask import Flask, request, jsonify
import pickle
import numpy as np


app = Flask(__name__)

model = pickle.load(open("models/churn_model.pkl", "rb"))

@app.route("/")
def home():
    return "Customer Churn Prediction API"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    features = np.array(data["features"]).reshape(1, -1)

    prediction = model.predict(features)

    result = "Customer will churn" if prediction[0] == 1 else "Customer will stay"

    return jsonify({
        "prediction": result
    })

if __name__ == "__main__":
    app.run(debug=True)

    