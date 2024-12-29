from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import joblib



df = pd.read_csv("ENB2012_data.csv")
# Define features (X) and target variables (y1, y2)
X = df[['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8']]
y1 = df['Y1']
y2 = df['Y2']

# Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y1_train, y1_test = train_test_split(X, y1, test_size=0.2, random_state=42)
_, _, y2_train, y2_test = train_test_split(X, y2, test_size=0.2, random_state=42)

# Create RandomForest models for Y1 and Y2
model_y1 = RandomForestRegressor(n_estimators=100, random_state=42)
model_y2 = RandomForestRegressor(n_estimators=100, random_state=42)

# Train models
model_y1.fit(X_train, y1_train)
joblib.dump(model_y1, 'y1_rfr_model.joblib')

model_y2.fit(X_train, y2_train)
joblib.dump(model_y2, 'y2_rfr_model.joblib')


# Make predictions
y1_pred = model_y1.predict(X_test)
y2_pred = model_y2.predict(X_test)

# Evaluate models
mse_y1 = mean_squared_error(y1_test, y1_pred)
r2_y1 = r2_score(y1_test, y1_pred)

mse_y2 = mean_squared_error(y2_test, y2_pred)
r2_y2 = r2_score(y2_test, y2_pred)

mse_y1, r2_y1, mse_y2, r2_y2

print("RandomForest Regression Model Evaluation Results")
print("--------------------------------------------------")
print("Heating Load (Y1):")
print("Mean Squared Error (MSE):", mse_y1)
print("R² Score:", r2_y1)
print("")
print("Cooling Load (Y2):")
print("Mean Squared Error (MSE):", mse_y2)
print("R² Score:", r2_y2)
