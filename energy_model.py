import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load data
df = pd.read_csv("ENB2012_data.csv")
X = df[['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8']].values
y1 = df['Y1'].values
y2 = df['Y2'].values

# Split data
X_train, X_test, y1_train, y1_test = train_test_split(X, y1, test_size=0.2, random_state=42)
_, _, y2_train, y2_test = train_test_split(X, y2, test_size=0.2, random_state=42)

# Utility Functions
def bootstrap_data(X, y):
    """Generate a bootstrap sample of the dataset."""
    n_samples = X.shape[0]
    indices = np.random.choice(n_samples, n_samples, replace=True)
    return X[indices], y[indices]

def split_dataset(X, y, feature_idx, threshold):
    """Split dataset into left and right based on threshold."""
    left_idx = X[:, feature_idx] <= threshold
    right_idx = X[:, feature_idx] > threshold
    return X[left_idx], y[left_idx], X[right_idx], y[right_idx]

def calculate_mse(y):
    """Calculate Mean Squared Error for a given target array."""
    if len(y) == 0:
        return 0
    mean_y = np.mean(y)
    return np.mean((y - mean_y) ** 2)

def best_split(X, y):
    """Find the best split for the dataset."""
    n_features = X.shape[1]
    best_mse = float('inf')
    best_feature = None
    best_threshold = None

    for feature_idx in range(n_features):
        thresholds = np.unique(X[:, feature_idx])
        for threshold in thresholds:
            _, y_left, _, y_right = split_dataset(X, y, feature_idx, threshold)
            mse_left = calculate_mse(y_left)
            mse_right = calculate_mse(y_right)
            mse_split = (len(y_left) * mse_left + len(y_right) * mse_right) / len(y)

            if mse_split < best_mse:
                best_mse = mse_split
                best_feature = feature_idx
                best_threshold = threshold

    return best_feature, best_threshold

class DecisionTreeRegressor:
    """A simple decision tree regressor."""
    def __init__(self, max_depth=5, min_samples_split=10):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.tree = None

    def fit(self, X, y):
        self.tree = self._grow_tree(X, y)

    def _grow_tree(self, X, y, depth=0):
        if depth < self.max_depth and len(y) >= self.min_samples_split:
            feature_idx, threshold = best_split(X, y)
            if feature_idx is not None:
                left_X, left_y, right_X, right_y = split_dataset(X, y, feature_idx, threshold)
                return {
                    'feature_idx': feature_idx,
                    'threshold': threshold,
                    'left': self._grow_tree(left_X, left_y, depth + 1),
                    'right': self._grow_tree(right_X, right_y, depth + 1),
                }
        return np.mean(y)

    def predict_row(self, row, tree):
        if isinstance(tree, dict):
            if row[tree['feature_idx']] <= tree['threshold']:
                return self.predict_row(row, tree['left'])
            else:
                return self.predict_row(row, tree['right'])
        return tree

    def predict(self, X):
        return np.array([self.predict_row(row, self.tree) for row in X])

class RandomForestRegressor:
    """A simple random forest regressor."""
    def __init__(self, n_estimators=10, max_depth=5, min_samples_split=10):
        self.n_estimators = n_estimators
        self.trees = [
            DecisionTreeRegressor(max_depth=max_depth, min_samples_split=min_samples_split)
            for _ in range(n_estimators)
        ]

    def fit(self, X, y):
        self.bootstraps = [bootstrap_data(X, y) for _ in range(self.n_estimators)]
        for tree, (X_bootstrap, y_bootstrap) in zip(self.trees, self.bootstraps):
            tree.fit(X_bootstrap, y_bootstrap)

    def predict(self, X):
        predictions = np.array([tree.predict(X) for tree in self.trees])
        return np.mean(predictions, axis=0)

# Train Random Forest for Y1
rf_y1 = RandomForestRegressor(n_estimators=50, max_depth=10)
rf_y1.fit(X_train, y1_train)

# Train Random Forest for Y2
rf_y2 = RandomForestRegressor(n_estimators=50, max_depth=10)
rf_y2.fit(X_train, y2_train)

# Predictions
y1_pred = rf_y1.predict(X_test)
y2_pred = rf_y2.predict(X_test)

# Evaluate
mse_y1 = mean_squared_error(y1_test, y1_pred)
r2_y1 = r2_score(y1_test, y1_pred)

mse_y2 = mean_squared_error(y2_test, y2_pred)
r2_y2 = r2_score(y2_test, y2_pred)

print("\nCustom Random Forest Regressor Evaluation Results")
print("-----------------------------------------------")
print("Heating Load (Y1):")
print("Mean Squared Error (MSE):", mse_y1)
print("R² Score:", r2_y1)
print("")
print("Cooling Load (Y2):")
print("Mean Squared Error (MSE):", mse_y2)
print("R² Score:", r2_y2)
