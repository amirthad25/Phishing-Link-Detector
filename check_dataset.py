import pandas as pd

# Load dataset
df = pd.read_csv("phishing_dataset.csv")  # Update filename if needed

# Check label distribution
print("\n🔍 Checking dataset balance:\n")
print(df['status'].value_counts())
