import pandas as pd
import joblib

# Load model & features
model = joblib.load("phishing_model.pkl")  # Adjust filename if different
features = joblib.load("feature_names.pkl")

# Check feature values for Microsoft.com
test_data = pd.DataFrame([[200, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
                        columns=features)

# Get prediction probability
phishing_probability = model.predict_proba(test_data)[0][1]

print(f"\n🔍 Phishing Probability for Microsoft.com: {phishing_probability:.4f}")

# Identify top suspicious features
feature_importance = model.feature_importances_
important_features = sorted(zip(features, feature_importance), key=lambda x: x[1], reverse=True)

print("\n🚨 Top Features Contributing to Phishing Prediction:")
for feature, importance in important_features[:10]:  # Show top 10
    print(f"{feature}: {importance:.4f}")
