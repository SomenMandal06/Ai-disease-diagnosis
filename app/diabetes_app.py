import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model
with open('models/diabetes_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="AI Diabetes Diagnosis", page_icon="🧬", layout="centered")

st.title("🧬 AI-Based Diabetes Diagnosis")
st.markdown("This tool predicts the likelihood of a person having **Diabetes** using a Machine Learning model trained on medical data.")

st.sidebar.header("📝 Enter Patient Details")

# Sidebar input fields
pregnancies = st.sidebar.number_input("Pregnancies", 0, 20, step=1)
glucose = st.sidebar.number_input("Glucose", 0, 200)
blood_pressure = st.sidebar.number_input("Blood Pressure", 0, 150)
skin_thickness = st.sidebar.number_input("Skin Thickness", 0, 100)
insulin = st.sidebar.number_input("Insulin", 0, 900)
bmi = st.sidebar.number_input("BMI", 0.0, 70.0, format="%.1f")
diabetes_pedigree = st.sidebar.number_input("Diabetes Pedigree Function", 0.0, 3.0, format="%.3f")
age = st.sidebar.number_input("Age", 1, 120, step=1)

if st.sidebar.button("🧠 Predict"):
    input_data = pd.DataFrame([{
    'Pregnancies': pregnancies,
    'Glucose': glucose,
    'BloodPressure': blood_pressure,
    'SkinThickness': skin_thickness,
    'Insulin': insulin,
    'BMI': bmi,
    'DiabetesPedigreeFunction': diabetes_pedigree,
    'Age': age
}])
    prediction = model.predict(input_data)

    st.subheader("🔍 Prediction Result")
    if prediction[0] == 1:
        st.error("⚠️ The person is likely **Diabetic**.")
    else:
        st.success("✅ The person is likely **Not Diabetic**.")
