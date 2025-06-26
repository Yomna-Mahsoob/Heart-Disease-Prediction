import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open('models/best_rf.pkl', 'rb'))

st.markdown("<h1 style='color:#4a90e2;'>Heart Disease Prediction App</h1>", unsafe_allow_html=True)

# Original inputs
age = st.number_input('Age', min_value=0, max_value=120)
sex = st.selectbox('Sex', ['Male', 'Female'])
trestbps = st.number_input('Resting Blood Pressure')
chol = st.number_input('Cholesterol')
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['Yes', 'No'])
restecg = st.selectbox('Resting ECG', ['Normal', 'ST-T Abnormality', 'Left Ventricular Hypertrophy'])
thalach = st.number_input('Max Heart Rate Achieved')
exang = st.selectbox('Exercise Induced Angina', ['Yes', 'No'])
oldpeak = st.number_input('ST Depression (Oldpeak)')
ca = st.slider('Number of Major Vessels (0–3)', 0, 3)

# One-hot style encoded features
cp = st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
slope = st.selectbox('Slope of ST Segment', ['Upsloping', 'Flat', 'Downsloping'])
thal = st.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversible Defect'])

# Encode categorical variables as one-hot manually
cp_1 = 1 if cp == 'Atypical Angina' else 0
cp_2 = 1 if cp == 'Non-anginal Pain' else 0
cp_3 = 1 if cp == 'Asymptomatic' else 0

thal_1 = 1 if thal == 'Fixed Defect' else 0
thal_2 = 1 if thal == 'Reversible Defect' else 0

slope_1 = 1 if slope == 'Flat' else 0
slope_2 = 1 if slope == 'Downsloping' else 0

# Final input list (17 features)
input_data = [
    age,
    1 if sex == 'Male' else 0,
    trestbps,
    chol,
    1 if fbs == 'Yes' else 0,
    1 if restecg == 'ST-T Abnormality' else 2 if restecg == 'Left Ventricular Hypertrophy' else 0,
    thalach,
    1 if exang == 'Yes' else 0,
    oldpeak,
    ca,
    cp_1, cp_2, cp_3,
    slope_1, slope_2,
    thal_1, thal_2
]

input_array = np.array(input_data).reshape(1, -1)

# Predict
if st.button('Predict'):
    prediction = model.predict(input_array)[0]
    if prediction == 1:
        st.markdown("<div style='color:#4a90e2; font-size:20px;'>⚠️ High risk of heart disease.</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div style='color:#4a90e2; font-size:20px;'>✅ Low risk of heart disease.</div>", unsafe_allow_html=True)
