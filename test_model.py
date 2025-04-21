import joblib
import pandas as pd

# Load trained model and feature names
model = joblib.load("phishing_model.pkl")
feature_names = joblib.load("feature_names.pkl")

# Manually define a phishing-like feature set
phishing_features = pd.DataFrame([{
    "length_url": 200,  # Long URLs are often phishing
    "nb_dots": 5,  # Too many dots
    "nb_at": 1,  # '@' in URL is suspicious
    "nb_qm": 1,  # '?' in URL
    "nb_slash": 10,  # Too many slashes
    "https_token": 0,  # No HTTPS is risky
    "shortening_service": 1,  # URL shorteners are risky
}])

# Ensure all features exist
phishing_features = phishing_features.reindex(columns=feature_names, fill_value=0)

# Predict using the model
prediction = model.predict(phishing_features)

# Print the result
print("Model Prediction:", "Phishing" if prediction[0] == 1 else "Safe")
