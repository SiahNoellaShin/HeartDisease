import streamlit as st

def get_user_input():
  blood_pressure = st.number_input("what is your heart rate?")
  heart_rate = st.number_input("What is your blood pressure?")
  age = st.number_input("What is your age?")
  cholesterol_rate = st.number_input("What is your cholesterol rate?")
  exercise_pain = st.number_input("What is your exercise pain?")

  input_features = [[blood_pressure, heart_rate, age, cholesterol_rate, exercise_pain]]
  return input_features
