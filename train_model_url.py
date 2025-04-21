import pandas as pd
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Load cleaned dataset
df = pd.read_csv("cleaned_dataset.csv")

# Separate features and target
X = df.drop(columns=["status"])
y = df["status"].map({"legitimate": 0, "phishing": 1})  # Convert labels to 0 and 1

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Train a Random Forest model
model = RandomForestClassifier(n_estimators=200, max_depth=20, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2%}")

# Compute confusion matrix
cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()
print("\nConfusion Matrix:")
print(cm)
print(f"\nLegitimate URLs (Safe) - Correctly classified: {tn}, Misclassified: {fp}")
print(f"Phishing URLs - Correctly classified: {tp}, Misclassified: {fn}")

# Save model & features
joblib.dump(model, "phishing_model.pkl")
joblib.dump(list(X.columns), "feature_names.pkl")
print("\n✅ Model and feature names saved successfully!")
