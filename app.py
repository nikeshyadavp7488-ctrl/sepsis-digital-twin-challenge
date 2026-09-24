import streamlit as st
import numpy as np
import pickle

st.set_page_config(page_title="Digital Twin Sepsis Predictor", layout="wide")

st.title("🩺 Patient Digital Twin: Early Sepsis & Organ Stress Monitor")
st.markdown("Real-time predictive simulation using Wearables & EHR data.")

# Load Model
@st.cache_resource
def load_model():
    try:
        with open('sepsis_model.pkl', 'rb') as f:
            return pickle.load(f)
    except:
        return None

model = load_model()

# Sidebar Vitals
st.sidebar.header("⚙️ Patient Vitals Input")
hr = st.sidebar.slider("Heart Rate (BPM)", 50, 160, 85)
temp = st.sidebar.slider("Temperature (°C)", 35.0, 41.0, 37.0)
spo2 = st.sidebar.slider("SpO2 (%)", 80, 100, 98)
wbc = st.sidebar.slider("WBC Count (x10^3/uL)", 2.0, 30.0, 7.5)
lactate = st.sidebar.slider("Lactate (mmol/L)", 0.5, 10.0, 1.2)
creatinine = st.sidebar.slider("Creatinine (mg/dL)", 0.5, 5.0, 0.9)

# Predict Risk
if model:
    input_data = [[hr, temp, spo2, wbc, lactate, creatinine]]
    prob = model.predict_proba(input_data)[0][1] * 100
else:
    # Heuristic fallback if model file isn't present
    prob = min(100, max(0, (hr - 80)*0.5 + (temp - 37)*20 + (100 - spo2)*2 + lactate*10))

# Visual Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Sepsis Onset Risk", f"{prob:.1f}%")

with col2:
    kidney_stress = min(100, int(creatinine * 25))
    st.metric("Kidney Stress Index", f"{kidney_stress}%")

with col3:
    resp_stress = min(100, int((100 - spo2) * 5))
    st.metric("Respiratory Stress Index", f"{resp_stress}%")

# Status Banner
if prob > 60:
    st.error("🚨 HIGH RISK ALERT: High probability of Sepsis in next 6-8 hours! Immediate ICU consultation advised.")
elif prob > 35:
    st.warning("⚠️ MODERATE RISK: Patient showing early inflammatory response. Monitor vitals closely.")
else:
    st.success("✅ LOW RISK: Patient parameters are within normal recovery range.")
