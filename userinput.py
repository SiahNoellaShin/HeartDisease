import streamlit as st

def get_user_input():
  heart_rate = st.number_input("What is your heart rate?")
  age = st.number_input("What is your age?")
  cholesterol = st.number_input("What is your chlosterol rate?")
  exercise_pain = st.number_input("What is your exercise pain?")
  blood_pressure = st.number_input("what is your blood pressure?")


  # YOUR CODE HERE (Ask users to enter features!)
  # YOUR CODE HERE (Ask users to enter features!)
  input_features = [[heart_rate, blood_pressure, cholesterol, exercise_pain, blood_pressure]] # put your features in here!
  return input_features
