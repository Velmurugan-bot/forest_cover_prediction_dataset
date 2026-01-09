import streamlit as st
import pandas as pd
import joblib

model = joblib.load('model.pkl')

st.title("🌲 Forest Cover Type Prediction")

features=joblib.load('feature_names.pkl')
elevation = st.number_input("Elevation", 0, 4000, step=1)
aspect = st.number_input("Aspect", 0, 360, step=1)
slope = st.number_input("Slope", 0, 90, step=1)
hd_hydrology = st.number_input("Horizontal Distance to Hydrology", step=1)
vd_hydrology = st.number_input("Vertical Distance to Hydrology", step=1)
hd_roadways = st.number_input("Horizontal Distance to Roadways", step=1)
hillshade_9am = st.number_input("Hillshade 9am", 0, 255, step=1)
hillshade_noon = st.number_input("Hillshade Noon", 0, 255, step=1)
hillshade_3pm = st.number_input("Hillshade 3pm", 0, 255, step=1)
hd_fire_points = st.number_input("Horizontal Distance to Fire Points", step=1)

soil_type = st.selectbox("Soil Type (0–39)", list(range(40)))
soil_encoded = [0] * 40
soil_encoded[soil_type] = 1
wilderness = st.selectbox("Wilderness Area", ["Wilderness Area 1", "Wilderness Area 2", "Wilderness Area 3", "Wilderness Area 4"])
wilderness_map = {
    "Wilderness Area 1": [1, 0, 0, 0],
    "Wilderness Area 2": [0, 1, 0, 0],
    "Wilderness Area 3": [0, 0, 1, 0],
    "Wilderness Area 4": [0, 0, 0, 1]
}

if st.button("Predict Cover Type"):
    pred = model.predict([features])[0]
    st.success(f"Predicted Cover Type: {pred}")
