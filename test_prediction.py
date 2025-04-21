import joblib
import pandas as pd

# Load trained model and feature names
model = joblib.load("phishing_model.pkl")
feature_names = joblib.load("feature_names.pkl")

# Create a test phishing-like feature set
phishing_features = pd.DataFrame([{feature: 0 for feature in feature_names}])  # Default all values to 0

# Manually set suspicious values
phishing_features["length_url"] = 200  # Long URL
phishing_features["nb_dots"] = 5  # Too many dots
phishing_features["nb_at"] = 1  # '@' in URL is suspicious
phishing_features["nb_qm"] = 1  # '?' in URL
phishing_features["nb_slash"] = 10  # Too many slashes
phishing_features["https_token"] = 0  # No HTTPS is risky
phishing_features["shortening_service"] = 1  # URL shorteners are risky

# Print feature values before prediction
print("\n🛠 Features Sent to Model:")
print(phishing_features)

# Predict using the model
prediction = model.predict(phishing_features)

# Print the result
print("\n🔍 Model Prediction:", "Phishing" if prediction[0] == 1 else "Safe")
