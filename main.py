import streamlit as st
import requests

st.set_page_config(page_title = "Medical Cost Prediction")

API_URL = "http://127.0.0.1:8000/predict"


def predict_cost(payload):
    response = requests.post(API_URL, json = payload)
    return response.json()


st.title("Medical Cost Prediction")
st.write("Fill in your details below to estimate your annual medical insurance cost.")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Personal Info")
    age = st.number_input("Age", min_value = 1, max_value = 120, value = 30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    bmi = st.number_input("BMI", min_value = 10.0, max_value = 60.0, value = 25.0, step = 0.1)
    smoker = st.selectbox("Smoker", ["Yes", "No"])
    city_type = st.selectbox("City Type", ["Urban", "Semi-Urban", "Rural"])
    physical_activity_level = st.selectbox("Physical Activity Level", ["Low", "Medium", "High"])

with col2:
    st.subheader("Health Conditions")
    diabetes = st.checkbox("Diabetes")
    hypertension = st.checkbox("Hypertension")
    heart_disease = st.checkbox("Heart Disease")
    asthma = st.checkbox("Asthma")
    daily_steps = st.number_input("Daily Steps", min_value = 0, max_value = 30000, value = 5000)
    sleep_hours = st.number_input("Sleep Hours", min_value = 0.0, max_value = 24.0, value = 7.0, step = 0.5)
    stress_level = st.slider("Stress Level", min_value = 1, max_value = 10, value = 5)

with col3:
    st.subheader("Medical & Insurance")
    doctor_visits_per_year = st.number_input("Doctor Visits Per Year", min_value = 0, max_value = 50, value = 2)
    hospital_admissions = st.number_input("Hospital Admissions", min_value = 0, max_value = 20, value = 0)
    medication_count = st.number_input("Medication Count", min_value = 0, max_value = 50, value = 0)
    insurance_type = st.selectbox("Insurance Type", ["Private", "Government"])
    insurance_coverage_pct = st.slider("Insurance Coverage %", min_value = 0, max_value = 100, value = 50)
    previous_year_cost = st.number_input("Previous Year Cost ($)", min_value = 0.0, value = 5000.0, step = 100.0)

st.divider()

if st.button("Predict", use_container_width=True):
    payload = {
        "age": age,
        "gender": gender,
        "bmi": bmi,
        "smoker": smoker,
        "diabetes": int(diabetes),
        "hypertension": int(hypertension),
        "heart_disease": int(heart_disease),
        "asthma": int(asthma),
        "physical_activity_level": physical_activity_level,
        "daily_steps": daily_steps,
        "sleep_hours": sleep_hours,
        "stress_level": stress_level,
        "doctor_visits_per_year": doctor_visits_per_year,
        "hospital_admissions": hospital_admissions,
        "medication_count": medication_count,
        "insurance_type": insurance_type,
        "insurance_coverage_pct": insurance_coverage_pct,
        "city_type": city_type,
        "previous_year_cost": previous_year_cost
    }

    try:
        result = predict_cost(payload)
        if result["status"] == "success":
            cost = result["predicted_cost"]
            st.success(f"Estimated Annual Medical Cost: **${cost:,.2f}**")
    except Exception as e:
        st.error("Error: ", e)

