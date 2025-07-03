# workflow/router.py

import joblib
import pandas as pd

# Load pre-trained model and encoder
model = joblib.load("decision_engine/complexity_model.pkl")
type_encoder = joblib.load("decision_engine/claim_type_encoder.pkl")

def predict_complexity(claim_dict):
    """Predict complexity level (High/Low) for a given claim"""
    
    # Safely encode claim_type
    claim_type = claim_dict.get("claim_type", "auto")
    try:
        claim_type_encoded = type_encoder.transform([claim_type])[0]
    except Exception:
        claim_type_encoded = 0  # Fallback for unknown types

    # Create feature vector for prediction
    input_data = {
        "claim_amount": claim_dict.get("claim_amount", 0),
        "num_documents": claim_dict.get("num_documents", 0),
        "missing_documents": claim_dict.get("missing_documents", 0),
        "incident_description_length": claim_dict.get("incident_description_length", 0),
        "prior_claims": claim_dict.get("prior_claims", 0),
        "customer_age": claim_dict.get("customer_age", 0),
        "flag_fraud_risk": claim_dict.get("flag_fraud_risk", 0),
        "submission_delay_days": claim_dict.get("submission_delay_days", 0),
        "claim_type_encoded": claim_type_encoded
    }

    features = pd.DataFrame([input_data])
    prediction = model.predict(features)[0]
    return prediction
