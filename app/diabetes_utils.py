# app/diabetes_utils.py
import pandas as pd
import joblib

model = joblib.load('models/diabetes_model.pkl')

def predict_diabetes(pregnancies, glucose, bp, skin_thickness, insulin, bmi, dpf, age):
    input_df = pd.DataFrame([{
        'Pregnancies': pregnancies,
        'Glucose': glucose,
        'BloodPressure': bp,
        'SkinThickness': skin_thickness,
        'Insulin': insulin,
        'BMI': bmi,
        'DiabetesPedigreeFunction': dpf,
        'Age': age
    }])
    result = model.predict(input_df)[0]
    return "Diabetes Detected" if result == 1 else "No Diabetes"
