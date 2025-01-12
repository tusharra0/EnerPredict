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
The prediction models used in this project are based on **Random Forest Regressor**. This is a method that combines multiple decision trees to make better predictions. By using many trees, the Random Forest can handle more complex patterns in the data and avoid overfitting, which happens when a model works well on training data but poorly on new data. Two separate models were trained:
- **Heating Load (Y1):** Predicts how much energy is needed to heat a building.
- **Cooling Load (Y2):** Predicts how much energy is needed to cool a building.

Additionally, **a Decision Tree Regressor and Random Forest Regressor were built from scratch** to better understand how these models work.

#### How the Decision Tree Regressor Was Built
The Decision Tree Regressor splits data into smaller groups based on a feature (like Surface Area or Roof Area) and a threshold value. To decide where to split, the algorithm calculates the Mean Squared Error (MSE) for each possible threshold. It chooses the split that reduces MSE the most. The tree continues splitting until it reaches a maximum depth or there isn’t enough data to split further.

#### How the Random Forest Regressor Was Built
The Random Forest Regressor combines multiple Decision Trees. Each tree is trained on a random sample of the data (called bootstrapping), which helps the model generalize better. During training, each tree uses a random subset of the features to decide the best splits. This randomness ensures that the trees are different from each other. When making predictions, the Random Forest averages the predictions of all the trees to give the final result. This averaging helps reduce errors and improve accuracy.

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

The dataset contains 768 samples, and each sample represents a unique combination of these parameters. Random Forest was selected because it can handle complex relationships between features, reduce overfitting, and deliver reliable predictions with minimal fine-tuning. The models were evaluated using metrics like Mean Squared Error (MSE) and R² Score to measure performance.

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
