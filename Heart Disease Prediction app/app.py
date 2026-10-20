import streamlit as  st
import pandas as pd
import joblib



st.set_page_config(page_title="Heart Risk Checker", page_icon="❤️", layout="centered")

st.markdown("""
<style>

.stApp {
    background: linear-gradient(#009FDE, #8F57C7, #FA0000);
    color: #e2e8f0;
}

/* Title style */
h1 {
    text-align: center;
    color: #f43f5e;
    font-weight: 800;
}

/* Predict button */
div.stButton > button {
    width: 100%;
    background: linear-gradient(#163FF5, #163FF5,#163FF5);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.7rem;
    font-size: 1.1rem;
    font-weight: 600;
    transition: 0.3s;
}
div.stButton > button:hover {
    transform: scale(1.03);
    box-shadow: 0 0 20px rgba(244, 63, 94, 0.5);
}
div[role="slider"] {
    background-color: #22d3ee !important;
    box-shadow: 0 0 10px rgba(34, 211, 238, 0.6);
}

/* Slider ki value (number) ka color */
div[data-testid="stSliderThumbValue"] {
    color: #22d3ee !important;
}

/* Selectbox transparent */
div[data-baseweb="select"] > div {
    background-color: transparent !important;
    border: 1px solid rgba(255, 255, 255, 0.25);
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

from pathlib import Path

BASE_DIR = Path(__file__).parent

model = joblib.load(BASE_DIR / "KNN_heart.pkl")
scaler = joblib.load(BASE_DIR / "scaler.pkl")
expected_columns = joblib.load(BASE_DIR / "columns.pkl")

st.title("Heart Disease ")
st.markdown("Provide the following Details")

age = st.slider("Age",18,100,40)

sex =st.selectbox("Sex",['M','F'])

chest_pain = st.selectbox("Chest pain type",["ATA","NAP","TA","ASY"])
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)",80,200,120)
cholesterol =st.number_input("Cholesterol(mg/dL)",100,600,200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL",[0,1])
resting_ecg =st.selectbox("Resting ECG" , ["Normal","ST","LVH"])
max_hr = st.slider("Max Heart Rate" ,60,220,150)
exercise_angina = st.selectbox("Exercise-Induced Angina ",["Y","N"])
oldpeak = st.slider("Oldpeak (ST Depression) ",0.0,6.0,1.0)
st_slope = st.selectbox("ST Slope ",["UP","Flat","Down"])

# When Predict is clicked
if st.button("Predict"):

    # Create a raw input dictionary
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    # Create input dataframe
    input_df = pd.DataFrame([raw_input])

    # Fill in missing columns with 0s
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns
    input_df = input_df[expected_columns]

    # Scale the input
    scaled_input = scaler.transform(input_df)

    # Make prediction
    prediction = model.predict(scaled_input)[0]

    # Show result
    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")
