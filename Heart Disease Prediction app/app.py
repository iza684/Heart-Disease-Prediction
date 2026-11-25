import streamlit as  st
import pandas as pd
import joblib




st.set_page_config(page_title="Heart Risk Checker", page_icon="❤️", layout="centered")

st.markdown("""
<style>

/* Hide default Streamlit menu/footer */
#MainMenu, footer, header {visibility: hidden;}

/* Cream page background */
.stApp {
    background: #F4EFDF;
    color: #2B2B22;
}

/* Main content as a light card */
.block-container {
    max-width: 760px;
    margin-top: 1.5rem;
    padding: 0 2rem 2.5rem 2rem;
    background: #FFFBF0;
    border: 1px solid #D8D2B8;
    border-radius: 20px;
    overflow: hidden;
}

/* Title as dark green banner */
h1 {
    background: #1F3D2B;
    color: #F4EFDF !important;
    text-align: center;
    font-weight: 700;
    margin: 0 -2rem 0.5rem -2rem;
    padding: 2rem 1rem 1.2rem 1rem !important;
}

/* Subtitle */
.stMarkdown p {
    color: #3F6B4F;
    text-align: center;
    font-weight: 500;
}

/* Labels */
label, label p {
    color: #2B2B22 !important;
    font-weight: 600 !important;
}

/* Predict button */
div.stButton > button {
    width: 100%;
    background: #1F3D2B;
    color: #F4EFDF;
    border: none;
    border-radius: 10px;
    padding: 0.7rem;
    font-size: 1.1rem;
    font-weight: 600;
    transition: 0.3s;
}
div.stButton > button:hover {
    background: #2F6B45;
    color: #F4EFDF;
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(31, 61, 43, 0.3);
}

/* Slider handle */
div[role="slider"] {
    background-color: #1F3D2B !important;
    box-shadow: 0 0 0 4px rgba(47, 107, 69, 0.2);
}

/* Slider ki value (number) ka color */
div[data-testid="stSliderThumbValue"] {
    color: #1F3D2B !important;
    font-weight: 700;
}

/* Selectbox and number input */
div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {
    background-color: #F4EFDF !important;
    border: 1px solid #B9B394;
    border-radius: 8px;
    color: #2B2B22;
}

/* Dropdown menu */
div[data-baseweb="popover"] ul {
    background-color: #FFFBF0 !important;
}

/* Result boxes (error / success) */
div[data-testid="stAlert"] {
    border-radius: 12px;
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
