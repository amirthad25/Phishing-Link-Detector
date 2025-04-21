import joblib
import pandas as pd
import streamlit as st
import numpy as np
import validators  # New: Validate URLs

# Load trained model and feature names
model = joblib.load("phishing_model.pkl")
feature_names = joblib.load("feature_names.pkl")

# Function to extract features dynamically
def extract_features(url):
    features_dict = {
        "length_url": len(url),
        "length_hostname": len(url.split('/')[2]) if '/' in url else len(url),
        "ip": 1 if any(c.isdigit() for c in url) else 0,
        "nb_dots": url.count('.'),
        "nb_hyphens": url.count('-'),
        "nb_at": url.count('@'),
        "nb_qm": url.count('?'),
        "nb_and": url.count('&'),
        "nb_or": url.count('|'),
        "nb_eq": url.count('='),
        "nb_underscore": url.count('_'),
        "nb_tilde": url.count('~'),
        "nb_percent": url.count('%'),
        "nb_slash": url.count('/'),
        "nb_star": url.count('*'),
        "nb_colon": url.count(':'),
        "nb_comma": url.count(','),
        "nb_semicolumn": url.count(';'),
        "nb_dollar": url.count('$'),
        "nb_space": url.count(' '),
        "nb_www": int("www" in url),
        "nb_com": int(".com" in url),
        "nb_dslash": url.count('//'),
        "http_in_path": int("http" in url.split("/")[-1]),
        "https_token": int("https" in url),
        "ratio_digits_url": sum(c.isdigit() for c in url) / len(url) if len(url) > 0 else 0,
        "ratio_digits_host": (
            sum(c.isdigit() for c in url.split('/')[2]) / len(url.split('/')[2])
            if '/' in url and len(url.split('/')[2]) > 0
            else 0
        ),
        "punycode": int("xn--" in url),
        "port": int(":" in url),
        "tld_in_path": int(any(tld in url for tld in [".com", ".net", ".org", ".info"])),
        "tld_in_subdomain": int(
            '/' in url and any(tld in url.split('/')[2] for tld in [".com", ".net", ".org", ".info"])
        ),
        "abnormal_subdomain": int(url.count('.') > 2),
        "nb_subdomains": url.count('.'),
        "prefix_suffix": int("-" in url),
        "random_domain": int('/' in url and len(url.split('/')[2]) > 10),
        "shortening_service": int(any(service in url for service in ["bit.ly", "tinyurl", "short.ly"])),
        "phish_hints": int(any(hint in url.lower() for hint in ["login", "bank", "secure", "verify"])),
        "suspecious_tld": int(url.endswith((".tk", ".cn", ".cc", ".ru", ".pw"))),
    }

    # Ensure all expected features are present
    feature_vector = {feature: features_dict.get(feature, 0) for feature in feature_names}

    # Convert to DataFrame
    df_features = pd.DataFrame([feature_vector])

    # Ensure order matches training data
    df_features = df_features[feature_names]  

    return df_features

# Function to predict phishing
def predict_url(url):
    try:
        features = extract_features(url)
        prediction = model.predict(features)
        return "Phishing" if prediction[0] == 1 else "Safe"
    except Exception as e:
        return f"Error: {e}"  # Handle errors gracefully

# Streamlit UI
st.title("🔍 Phishing URL Detector")
st.write("Enter a URL to check if it's safe or a phishing attempt.")

# Input field for URL
url_input = st.text_input("🔗 Enter URL:", "")

# Predict button
if st.button("Check URL"):
    if not url_input:
        st.warning("⚠️ Please enter a URL.")
    elif not validators.url(url_input):  # Validate URL
        st.warning("🚫 Invalid URL! Please enter a proper URL format.")
    else:
        result = predict_url(url_input)
        if result == "Phishing":
            st.error("🚨 Warning: This URL seems to be phishing! Be safe.")
        elif result == "Safe":
            st.success("✅ This URL appears to be safe.")
        else:
            st.warning(f"⚠️ Unexpected Error: {result}")  # Display errors if any
