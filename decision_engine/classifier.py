# decision_engine/classifier.py

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
import os

def train_model(csv_path, save_path="decision_engine/complexity_model.pkl"):
    df = pd.read_csv(csv_path)

    # Drop rows where target (label) is missing
    df = df.dropna(subset=["complexity"])

    # Encode categorical feature: claim_type
    le_type = LabelEncoder()
    df['claim_type_encoded'] = le_type.fit_transform(df['claim_type'].astype(str))

    # Feature set
    features = [
        "claim_amount", "num_documents", "missing_documents",
        "incident_description_length", "prior_claims", "customer_age",
        "flag_fraud_risk", "submission_delay_days", "claim_type_encoded"
    ]

    X = df[features]
    y = df["complexity"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train Decision Tree
    model = DecisionTreeClassifier(max_depth=3, random_state=42)
    model.fit(X_train, y_train)

    # Save model and encoder
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    joblib.dump(model, save_path)
    joblib.dump(le_type, "decision_engine/claim_type_encoder.pkl")

    print(f"\n✅ Model trained and saved to {save_path}")
    print(f"📊 Training Accuracy: {model.score(X_train, y_train):.2f}")
    print(f"📊 Testing Accuracy: {model.score(X_test, y_test):.2f}")
