import streamlit as st
import pandas as pd
import joblib

model = joblib.load('model.pkl')

st.title("🌲 Forest Cover Type Prediction")

features=joblib.load('feature_names.pkl')

if st.button("Predict Cover Type"):
    pred = model.predict([features])[0]
    st.success(f"Predicted Cover Type: {pred}")
