# Energy Efficiency Predictor

## Project Overview
The Energy Efficiency Predictor is a web application designed to predict heating and cooling loads for buildings using machine learning models. It leverages a user-friendly frontend and a Flask-based backend for seamless interaction and accurate predictions.

---

## Technologies Used
### Backend:
- Python
- Flask
- Scikit-learn
- Joblib

### Frontend:
- HTML5
- CSS3
- JavaScript

### Models and Dataset:
The prediction models used in this project are based on **Random Forest Regressor**, a robust ensemble learning method that combines multiple decision trees to improve predictive accuracy and control overfitting. Two separate models were trained and optimized:
- **Heating Load (Y1):** Predicts the energy required for heating a building.
- **Cooling Load (Y2):** Predicts the energy required for cooling a building.

Additionally, **a Decision Tree Regressor and Random Forest Regressor were implemented from scratch** to explore the inner workings of these models. The scratch-built versions allow for a deeper understanding of how these algorithms split data, handle bootstrapping, and aggregate results in ensemble learning methods.

Both models were trained on the **Energy Efficiency Dataset (ENB2012)**, a publicly available dataset that includes data on eight building design parameters:
- **X1:** Relative Compactness
- **X2:** Surface Area
- **X3:** Wall Area
- **X4:** Roof Area
- **X5:** Overall Height
- **X6:** Orientation
- **X7:** Glazing Area
- **X8:** Glazing Area Distribution

The target variables are:
- **Y1:** Heating Load
- **Y2:** Cooling Load

The dataset contains 768 samples, and each sample represents a unique combination of these parameters. Random Forest was selected due to its ability to handle non-linear relationships, reduce overfitting, and deliver reliable results with minimal hyperparameter tuning. The models were evaluated using metrics such as Mean Squared Error (MSE) and R² Score to ensure performance and accuracy.

---

## Folder Structure
```
project-root/
│
├── backend/
│   ├── models/
│   │   ├── y1_rfr_model.joblib
│   │   ├── y2_rfr_model.joblib
│   ├── app.py
│   ├── energy_model.py
│   ├── requirments.txt
│   ├── test_api.py
│
├── frontend/
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── styles.css
│   ├── script.js
│
└── README.md
```

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo-url.git
cd project-root
```

### 2. Set Up Backend
```bash
cd backend
pip install -r requirments.txt
```

### 3. Run Flask Backend
```bash
python app.py
```
The backend will be available at `http://127.0.0.1:5000/`

### 4. Access the Frontend
Open your browser and visit:
```
http://127.0.0.1:5000/
```

---

## Test the API
You can test the prediction API using the provided `test_api.py` script:
```bash
python test_api.py
```

Expected Output:
```
Successful
{'Heating Load (Y1)': value, 'Cooling Load (Y2)': value}
```

---

## How to Use
1. Enter values for features X1 to X8 in the input fields.
2. Click the Predict button.
3. View predicted Heating Load (Y1) and Cooling Load (Y2).

---

## Additional Features
This project also includes implementations of:
- A **Decision Tree Regressor** from scratch, demonstrating the algorithm's ability to split data based on thresholds to minimize prediction errors.
- A **Random Forest Regressor** from scratch, showcasing the ensemble learning process, including bootstrapping and aggregation of multiple decision trees for robust predictions.

These implementations were added for educational purposes to understand the inner workings of these machine learning models.

---

## Troubleshooting
- Ensure the backend is running (`python app.py`).
- Verify all dependencies are installed (`pip install -r requirments.txt`).
- Use the browser developer console (`Ctrl+Shift+I`) to check for frontend errors.

---

## Contributing
Contributions are welcome. Please open an issue first to discuss your proposed changes.

---

Thank you for using the Energy Efficiency Predictor.
