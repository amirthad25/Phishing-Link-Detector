import pandas as pd
import joblib
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load dataset
df = pd.read_csv("cleaned_dataset.csv")

# Load trained model
model = joblib.load("phishing_model.pkl")  # Change the filename if needed

# Separate features and labels
X = df.drop(columns=["status"])  # Features
y_true = df["status"]  # Actual labels

# Make predictions
y_pred = model.predict(X)

# Print evaluation metrics
print("\n🔍 Model Evaluation Results:\n")
print("✅ Accuracy:", accuracy_score(y_true, y_pred))
print("\n📊 Confusion Matrix:\n", confusion_matrix(y_true, y_pred))
print("\n📢 Classification Report:\n", classification_report(y_true, y_pred))

