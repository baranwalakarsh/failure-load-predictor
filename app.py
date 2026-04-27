import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model + columns
model = joblib.load("model/model.pkl")
columns = joblib.load("model/columns.pkl")

st.title("Failure Load Predictor")

# INPUTS
mix_id = st.selectbox("Mix ID", ["UHPC-1", "UHPC-2", "UHPC-3", "UHPC-4", "UHPC-5"])
steel_fibre = st.slider("Steel Fibre %", 0.0, 3.0, 1.0)
age_days = st.selectbox("Age (Days)", [7, 14, 28, 56, 90])
curing = st.selectbox("Curing Method", [
    "Ambient Curing",
    "Heat Curing",
    "Steam Curing",
    "Water Curing"
])

if st.button("Predict"):

    # SAME STRUCTURE AS TRAINING
    data = pd.DataFrame({
        "Mix_ID": [mix_id],
        "Steel_Fibre_%": [steel_fibre],
        "Age_Days": [age_days],
        "Curing_Method": [curing]
    })

    # Feature engineering
    data["Fibre_Age"] = data["Steel_Fibre_%"] * data["Age_Days"]
    data["Log_Age"] = np.log1p(data["Age_Days"])

    # 🔥 IMPORTANT: encode ALL columns like training
    data = pd.get_dummies(data)

    # 🔥 FORCE SAME COLUMNS
    data = data.reindex(columns=columns, fill_value=0)

    # DEBUG (remove later)
    # st.write("Input to model:", data)

    # Predict
    prediction = model.predict(data)[0]

    st.success(f"Predicted Failure Load: {prediction:.2f} kN")

    # st.write(data)
