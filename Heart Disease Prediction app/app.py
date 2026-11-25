import streamlit as  st
import pandas as pd
import joblib




st.set_page_config(page_title="Heart Risk Checker", page_icon="❤️", layout="centered")

st.markdown("""
<style>

/* Hide default Streamlit menu/footer */
#MainMenu, footer, header {visibility: hidden;}

/* Dark modern background */
.stApp {
    background: radial-gradient(circle at 15% 0%, #1e2a4a 0%, #0b1020 55%, #070a14 100%);
    color: #e2e8f0;
}

/* Main content as a glass card */
.block-container {
    max-width: 760px;
    margin-top: 2rem;
    padding: 2.5rem 2.5rem 3rem 2.5rem;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 24px;
    backdrop-filter: blur(12px);
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.45);
}

/* Title style */
h1 {
    text-align: center;
    font-weight: 800;
    background: linear-gradient(90deg, #5eead4, #818cf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Subtitle and labels */
.stMarkdown p {
    color: #94a3b8;
    text-align: center;
}
label, label p {
    color: #cbd5e1 !important;
    font-weight: 600 !important;
    text-align: left !important;
}

/* Predict button */
div.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #5eead4, #818cf8);
    color: #0b1020;
    border: none;
    border-radius: 12px;
    padding: 0.7rem;
    font-size: 1.1rem;
    font-weight: 700;
    transition: 0.3s;
}
div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(129, 140, 248, 0.4);
    color: #0b1020;
}

/* Slider handle */
div[role="slider"] {
    background-color: #5eead4 !important;
    box-shadow: 0 0 10px rgba(94, 234, 212, 0.6);
}

/* Slider ki value (number) ka color */
div[data-testid="stSliderThumbValue"] {
    color: #5eead4 !important;
}

/* Selectbox and number input */
div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {
    background-color: rgba(255, 255, 255, 0.06) !important;
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 10px;
}

/* Result boxes (error / success) */
div[data-testid="stAlert"] {
    border-radius: 14px;
    border: 1px solid rgba(255, 255, 255, 0.12);
}
</style>
""", unsafe_allow_html=True)

model = joblib.load( "KNN_heart.pkl")
scaler = joblib.load( "scaler.pkl")
expected_columns = joblib.load( "columns.pkl")

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
