import matplotlib.pyplot as plt
import pandas as pd
import joblib

# Load trained model
model = joblib.load("phishing_model.pkl")  # Make sure this file exists in your project folder

# Load dataset (same dataset used for training)
df = pd.read_csv("phishing_dataset.csv")

# Drop non-feature columns
X = df.drop(columns=["url", "status"])  # These are not used in training

# Get feature importance from the model
feature_importance = pd.Series(model.feature_importances_, index=X.columns)

# Sort and plot feature importance
feature_importance.sort_values(ascending=False).plot(kind='bar', figsize=(12, 6))

plt.title("Feature Importance in Phishing Detection")
plt.xlabel("Features")
plt.ylabel("Importance Score")
plt.show()
