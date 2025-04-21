import pandas as pd
import joblib

# Load dataset
df = pd.read_csv("phishing_dataset.csv")  # Change to your actual dataset file

# Load expected feature names
expected_features = joblib.load("feature_names.pkl")

# Ensure 'status' is included
expected_features.append("status")  

# Find extra columns
extra_columns = [col for col in df.columns if col not in expected_features]
if extra_columns:
    print("\n❌ Extra columns found in dataset:", extra_columns)
    print("⚠️ Removing extra columns...\n")
    df = df[expected_features]  # Keep only required columns

# Save the cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)
print("✅ Fixed dataset saved as 'cleaned_dataset.csv'")
