# app/multi_disease_app.py
import streamlit as st
from app.diabetes_utils import predict_diabetes
from app.heart_utils import predict_heart_disease

st.set_page_config(page_title="Multi-Disease AI Health App", layout="wide")
st.title("🧠 AI Health Assistant")
st.markdown("Predict multiple diseases using machine learning")

tab1, tab2 = st.tabs(["🩸 Diabetes Prediction", "🫀 Heart Disease Prediction"])

# ====================== Diabetes Tab ======================
with tab1:
    st.subheader("Diabetes Predictor")
    col1, col2 = st.columns(2)

    with col1:
        pregnancies = st.number_input("Pregnancies", 0, 20, 1)
        glucose = st.number_input("Glucose", 50, 200, 120)
        bp = st.number_input("Blood Pressure", 40, 140, 70)
        skin = st.number_input("Skin Thickness", 0, 100, 20)
    with col2:
        insulin = st.number_input("Insulin", 0, 900, 80)
        bmi = st.number_input("BMI", 10.0, 60.0, 25.0)
        dpf = st.number_input("Diabetes Pedigree Function", 0.0, 2.5, 0.5)
        age = st.number_input("Age", 10, 100, 30)

    if st.button("Predict Diabetes"):
        result = predict_diabetes(pregnancies, glucose, bp, skin, insulin, bmi, dpf, age)
        st.success(result)

# ====================== Heart Tab ======================
with tab2:
    st.subheader("Heart Disease Predictor")
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 18, 100, 45)
        sex = st.selectbox("Sex", ['Male', 'Female'])
        cp = st.selectbox("Chest Pain Type", ['ATA', 'NAP', 'ASY', 'TA'])
        chol = st.slider("Cholesterol", 100, 500, 200)

    with col2:
        fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", [0, 1])
        ecg = st.selectbox("Resting ECG", ['Normal', 'ST', 'LVH'])
        max_hr = st.slider("Max Heart Rate", 60, 220, 150)
        angina = st.radio("Exercise Induced Angina", ['Y', 'N'])

    if st.button("Predict Heart Disease"):
        result = predict_heart_disease(age, sex, cp, chol, fbs, ecg, max_hr, angina)
        st.success(result)
