import streamlit as st

def get_app_response(prediction):
  if prediction == 1:
    st.write("The model predicts you have heart disease.")
  else:
    st.write('The model predicts you do not have heart disease.')
