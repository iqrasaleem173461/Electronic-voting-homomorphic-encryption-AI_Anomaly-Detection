import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

MODEL_PATH = "fraud_model.pkl"

def train_initial_model():
    # Simulating synthetic data for training
    # Features: [hour_of_day, login_attempts, time_since_last_action, is_new_ip]
    data = [
        [10, 1, 300, 0, 0], # Normal
        [14, 2, 600, 0, 0], # Normal
        [3, 15, 1, 1, 1],   # Fraud (middle of night, high attempts, fast, new IP)
        [2, 20, 0, 1, 1],   # Fraud
        [12, 1, 1000, 0, 0],# Normal
        [4, 8, 2, 1, 1],    # Fraud
    ]
    
    df = pd.DataFrame(data, columns=['hour', 'attempts', 'interval', 'new_ip', 'is_fraud'])
    
    X = df.drop('is_fraud', axis=1)
    y = df['is_fraud']
    
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    
    joblib.dump(model, MODEL_PATH)
    print("Initial fraud detection model trained.")

def predict_fraud(data):
    # data: {'hour': int, 'attempts': int, 'interval': int, 'new_ip': int}
    if not os.path.exists(MODEL_PATH):
        train_initial_model()
        
    model = joblib.load(MODEL_PATH)
    features = np.array([[data['hour'], data['attempts'], data['interval'], data['new_ip']]])
    
    # Get probability of fraud
    prob = model.predict_proba(features)[0][1]
    is_fraud = prob > 0.5
    
    return {
        "is_fraud": bool(is_fraud),
        "confidence": float(prob),
        "risk_score": float(prob * 100)
    }

if __name__ == "__main__":
    train_initial_model()
