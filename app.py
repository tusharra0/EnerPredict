import os
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Construct absolute paths for models
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_Y1_PATH = os.path.join(BASE_DIR, 'models', 'y1_rfr_model.joblib')
MODEL_Y2_PATH = os.path.join(BASE_DIR, 'models', 'y2_rfr_model.joblib')

# Load trained models (.joblib format)
model_y1 = joblib.load(MODEL_Y1_PATH)
model_y2 = joblib.load(MODEL_Y2_PATH)

@app.route('/')
def home():
    return "Welcome to the Energy Efficiency Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        required_features = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8']
        if not all(feature in data for feature in required_features):
            return jsonify({"error": "Missing one or more required features."}), 400
        
        features = np.array([[
            float(data['X1']),
            float(data['X2']),
            float(data['X3']),
            float(data['X4']),
            float(data['X5']),
            float(data['X6']),
            float(data['X7']),
            float(data['X8'])
        ]])
        
        heating_load = model_y1.predict(features)[0]
        cooling_load = model_y2.predict(features)[0]
        
        return jsonify({
            "Heating Load (Y1)": round(heating_load, 2),
            "Cooling Load (Y2)": round(cooling_load, 2)
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
