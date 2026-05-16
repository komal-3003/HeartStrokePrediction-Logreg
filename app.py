import streamlit as st
import pandas as pd
import joblib
st.set_page_config(
    page_title="Heart Stroke Prediction",
    page_icon="🫀",
    layout="wide"
)

# Remove top padding and center title
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
        }

        .main-title {
            text-align: center;
            font-size: 42px;
            font-weight: bold;
            margin-top: 20px;
            margin-bottom: 20px;
        }

        .subtext {
            text-align: center;
            font-size: 18px;
            color: gray;
            margin-bottom: 30px;
        }
            
        div.stButton > button:first-child {
        background-color: #ff4b4b;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        height: 3em;
        margin-left:100px;
        width: 40%;
        border: none;
        }

        div.stButton > button:first-child:hover {
            background-color: #e63939;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Custom centered heading
st.markdown(
    '<div class="main-title">🫀 Heart Stroke Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtext">Provide the following health details</div>',
    unsafe_allow_html=True
)

# Load files
model = joblib.load("Log_reg_heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("Columns.pkl")



# Create 3 columns
col1, col2, col3 = st.columns(3)

# Create 3 columns
col1, col2, col3 = st.columns(3)

# COLUMN 1
with col1:
    age = st.slider("Age", 18, 100, 40)

    sex = st.selectbox(
        "Sex",
        ["M", "F"]
    )

    chest_pain = st.selectbox(
        "Chest Pain Type",
        ['ATA', 'NAP', 'TA', 'ASY']
    )

    resting_bp = st.number_input(
        "Resting BP (mm Hg)",
        80, 200, 120
    )

# COLUMN 2
with col2:
    cholesterol = st.number_input(
        "Cholesterol (mg/DL)",
        100, 600, 200
    )

    fasting_bs = st.selectbox(
        "Fasting Blood Sugar > 120 mg/DL",
        [0, 1]
    )

    resting_ecg = st.selectbox(
        "Resting ECG",
        ['Normal', 'ST', 'LVH']
    )

    max_hr = st.slider(
        "Max Heart Rate",
        60, 220, 150
    )

# COLUMN 3
with col3:
    exercise_angenia = st.selectbox(
        "Exercise Induced Angina",
        ['Y', 'N']
    )

    oldpeak = st.slider(
        "Oldpeak (ST Depression)",
        0.0, 6.0, 1.0
    )

    st_slope = st.selectbox(
        "ST Slope",
        ['Up', 'Flat', 'Down']
    )

# Predict Button
# Center the Predict Button
left_space, center_btn, right_space = st.columns([1, 1, 1])

with center_btn:
    predict_btn = st.button(
        "🔍 Predict",
        use_container_width=True
    )

# Show Result Below Button
if predict_btn:

    raw_input = {
        "age": age,
        "Resting_BP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "Max_HR": max_hr,
        "Oldpeak": oldpeak,
        "RestingECG_" + resting_ecg: 1,
        "Sex_" + sex: 1,
        "ChestPainType_" + chest_pain: 1,
        "ExerciseAngenia_" + exercise_angenia: 1,
        "ST_slope_" + st_slope: 1
    }

    input_df = pd.DataFrame([raw_input])

    # Add missing columns
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    # Scale input
    scaled_input = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(scaled_input)[0]

    st.markdown("<br>", unsafe_allow_html=True)

    # Center Result
    result_left, result_center, result_right = st.columns([1, 2, 1])

    with result_center:

        if prediction == 1:
            st.error("⚠️ High Risk of Heart Disease")

        else:
            st.success("✅ Low Risk of Heart Disease")
