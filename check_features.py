import joblib

# Load the feature names
features = joblib.load("feature_names.pkl")

# Print feature count and names
print(f"\n🔢 Model expects {len(features)} features.")
print("\n📝 Feature names:")
print(features)
