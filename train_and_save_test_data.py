import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# ✅ Load dataset
try:
    df = pd.read_csv("phishing_dataset.csv")
    print("✅ Dataset loaded successfully!")
except FileNotFoundError:
    print("❌ Error: phishing_dataset.csv not found!")
    exit()

# ✅ Ensure "status" column exists
if "status" not in df.columns:
    print("❌ Error: 'status' column not found in dataset!")
    exit()

# ✅ Convert categorical labels to numeric values
label_mapping = {"legitimate": 0, "phishing": 1, "suspicious": 2}  # Adjust as needed
df["status"] = df["status"].map(label_mapping)

# ✅ Drop non-numeric columns
X = df.drop(columns=["url", "status"], errors="ignore")  # Ignore if columns are missing
y = df["status"]

# ✅ Handle any remaining missing values
X = X.fillna(0)

# ✅ Split dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Train a Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# ✅ Save model and test data
joblib.dump(model, "phishing_model.pkl")
joblib.dump(X_test, "X_test.pkl")
joblib.dump(y_test, "y_test.pkl")

print("🎉 Model retrained and test data saved successfully!")
