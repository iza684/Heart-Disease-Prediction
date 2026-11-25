import streamlit as  st
import pandas as pd
import joblib



st.set_page_config(page_title="Heart Risk Checker", page_icon="❤️", layout="centered")

st.markdown("""
<style>

/* Hide default Streamlit menu/footer */
#MainMenu, footer, header {visibility: hidden;}

/* Ice blue page with soft circles and a faint heartbeat line */
.stApp {
    background-color: #EAF2FB;
    background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 900' preserveAspectRatio='xMidYMid slice'><circle cx='1360' cy='60' r='260' fill='%23DCE9F7'/><circle cx='60' cy='860' r='300' fill='%23D5E4F5'/><g fill='%23C6DBF1'><circle cx='170' cy='150' r='28'/><circle cx='235' cy='195' r='18'/><circle cx='120' cy='225' r='12'/><circle cx='1280' cy='740' r='28'/><circle cx='1220' cy='790' r='18'/><circle cx='1330' cy='815' r='12'/></g><polyline points='0,450 300,450 350,400 400,500 450,360 500,460 540,450 1440,450' fill='none' stroke='%23B3CDE8' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/></svg>");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: #1B2B40;
}

/* Main content as a light card */
.block-container {
    max-width: 780px;
    margin-top: 2rem;
    margin-bottom: 2rem;
    padding: 0 2rem 2.5rem 2rem !important;
    background: #F8FBFF;
    border: 1px solid #C3D3E6;
    border-radius: 20px;
    overflow: hidden;
}

/* Title as dark navy banner */
h1 {
    background: #12335E;
    color: #EAF2FB !important;
    text-align: center;
    font-weight: 700;
    margin: 0 -2rem 0.5rem -2rem;
    padding: 2rem 1rem 1.2rem 1rem !important;
}

/* Subtitle */
.stMarkdown p {
    color: #2563A8;
    text-align: center;
    font-weight: 500;
}

/* Labels */
label, label p {
    color: #1B2B40 !important;
    font-weight: 600 !important;
}

/* Predict button */
div.stButton > button {
    width: 100%;
    background: #12335E;
    color: #EAF2FB;
    border: none;
    border-radius: 10px;
    padding: 0.7rem;
    font-size: 1.1rem;
    font-weight: 600;
    transition: 0.3s;
}
div.stButton > button:hover {
    background: #2563A8;
    color: #EAF2FB;
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(18, 51, 94, 0.3);
}

/* Slider handle */
div[role="slider"] {
    background-color: #12335E !important;
    box-shadow: 0 0 0 4px rgba(37, 99, 168, 0.2);
}

/* Slider ki value (number) ka color */
div[data-testid="stSliderThumbValue"] {
    color: #12335E !important;
    font-weight: 700;
}

/* Selectbox and number input */
div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {
    background-color: #EAF2FB !important;
    border: 1px solid #9DB6D3;
    border-radius: 8px;
    color: #1B2B40;
}

/* Dropdown menu */
div[data-baseweb="popover"] ul {
    background-color: #F8FBFF !important;
}

/* Result boxes (error / success) */
div[data-testid="stAlert"] {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

model = joblib.load( "KNN_heart.pkl")
scaler = joblib.load( "scaler.pkl")
expected_columns = joblib.load( "columns.pkl")

st.title("Heart Disease ")
st.markdown("Provide the following Details")

age = st.slider("Age",18,100,40)

# Selections in two columns
col1, col2 = st.columns(2)

with col1:
    sex = st.selectbox("Sex",['M','F'])
    resting_bp = st.number_input("Resting Blood Pressure (mm Hg)",80,200,120)
    fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL",[0,1])
    exercise_angina = st.selectbox("Exercise-Induced Angina ",["Y","N"])

with col2:
    chest_pain = st.selectbox("Chest pain type",["ATA","NAP","TA","ASY"])
    cholesterol = st.number_input("Cholesterol(mg/dL)",100,600,200)
    resting_ecg = st.selectbox("Resting ECG" , ["Normal","ST","LVH"])
    st_slope = st.selectbox("ST Slope ",["UP","Flat","Down"])

# Sliders in two columns
col3, col4 = st.columns(2)

with col3:
    max_hr = st.slider("Max Heart Rate" ,60,220,150)

with col4:
    oldpeak = st.slider("Oldpeak (ST Depression) ",0.0,6.0,1.0)

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
