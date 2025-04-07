# app/heart_utils.py
import pandas as pd
import joblib

model = joblib.load('models/heart_model.pkl')

def predict_heart_disease(age, sex, cp, chol, fbs, ecg, max_hr, angina):
    input_df = pd.DataFrame([{
        'Age': age,
        'Sex': 1 if sex == 'Male' else 0,
        'ChestPainType': cp,
        'Cholesterol': chol,
        'FastingBS': fbs,
        'RestingECG': ecg,
        'MaxHR': max_hr,
        'ExerciseAngina': angina
    }])
    result = model.predict(input_df)[0]
    return "Heart Disease Detected" if result == 1 else "No Heart Disease"
