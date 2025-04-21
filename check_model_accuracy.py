import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report

# Load trained model and test data
model = joblib.load("phishing_model.pkl")
X_test = joblib.load("X_test.pkl")  # Your test features
y_test = joblib.load("y_test.pkl")  # Your test labels

# Make predictions
y_pred = model.predict(X_test)

# Print accuracy and classification report
print("\n🎯 Model Accuracy:", accuracy_score(y_test, y_pred))
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))
