import streamlit as st
import pandas as pd
import joblib  # Assuming you're using joblib to load the model

# Load your pre-trained model
model = joblib.load('caloriburntprediction.joblib')  # Replace with your model's file path

# Define the min and max values for inverse scaling
min_calories = 1.0  # Minimum calorie value used for scaling
max_calories = 314.0  # Maximum calorie value used for scaling

def predict_calories(gender, age, duration, heart_rate, body_temp):
    input_data = pd.DataFrame({
        'Gender': [gender],  
        'Age': [age],
        'Duration': [duration],
        'Heart_Rate': [heart_rate],
        'Body_Temp': [body_temp]
    })
    # Get predicted scaled calories
    predicted_scaled_calories = model.predict(input_data)
    
    # Inverse scaling to get normal form
    predicted_calories = predicted_scaled_calories * (max_calories - min_calories) + min_calories
    return predicted_calories[0]

# Streamlit app layout
st.markdown(
    """
    <h1 style='color: #978A84;'>Welcome To GP Projects 🚀</h1>
    """, unsafe_allow_html=True
)

st.markdown(
    """
    <h3 style='font-size: 40px; color: #8C92AC;'>Calorie Prediction App</h3>
    """, unsafe_allow_html=True
)

# User inputs
gender_input = st.selectbox("Select Gender", options=["Male", "Female"])
age_input = st.number_input("Enter Age", min_value=1, max_value=120, value=23)
duration_input = st.number_input("duration of the workout  (minutes)", min_value=1, value=56)
heart_rate_input = st.number_input("Enter Heart Rate (bpm)", min_value=1, value=78)
body_temp_input = st.number_input("Enter Body Temperature (°C)", min_value=30.0, max_value=42.0, value=37.0)

# Convert gender input to numerical value
gender_numeric = 1 if gender_input == "Male" else 0

# Button to trigger prediction
if st.button("Predict Calories"):
    calories_output = predict_calories(gender_numeric, age_input, duration_input, heart_rate_input, body_temp_input)
    st.success(f"Predicted Calories: {calories_output:.2f}")
