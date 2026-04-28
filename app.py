import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model/model.pkl")
columns = joblib.load("model/columns.pkl")

st.title("Failure Load Predictor")

# Inputs
steel_fibre = st.slider("Steel Fibre %", 0.0, 3.0, 1.0)
age_days = st.selectbox("Age (Days)", [7, 14, 28, 56, 90])
curing = st.selectbox("Curing Method", [
    "Ambient Curing",
    "Heat Curing",
    "Steam Curing",
    "Water Curing"
])

# For Water_Cement_Ratio
cement = st.number_input("Cement (kg/m³)", 100.0, 1200.0, 800.0)
water = st.number_input("Water (kg/m³)", 50.0, 400.0, 160.0)

if st.button("Predict"):
    water_cement_ratio = water / (cement + 1e-6)

    data = pd.DataFrame({
        "Steel_Fibre_%": [steel_fibre],
        "Water_Cement_Ratio": [water_cement_ratio],
        "Age_Days": [age_days],
        "Curing_Method": [curing]
    })

    # One-hot encode
    data = pd.get_dummies(data)

    # Align to training columns
    data = data.reindex(columns=columns, fill_value=0)

    prediction = model.predict(data)[0]
    st.success(f"Predicted Failure Load: {prediction:.2f} kN")
