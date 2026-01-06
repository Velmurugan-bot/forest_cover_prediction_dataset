[8:22 pm, 5/1/2026] ChatGPT: import streamlit as st
import pandas as pd
import joblib

model = joblib.load('model.pkl')

st.title("🌲 Forest Cover Type Prediction")

elevation = st.number_input("Elevation", 0, 4000, step=1)
aspect = st.number_input("Aspect", 0, 360, step=1)
slope = st.number_input("Slope", 0, 90, step=1)
hd_hydrology = st.number_input("Horizontal Distance to Hydrology", step=1)
vd_hydrology = st.number_input("Vertical Distance to Hydrology", step=1)
hd_roadways = st.number_input("Horizontal Distance to Roadways", step=1)
hillshade_9am = st.number_input("Hillshade 9am", 0, 255,…
[8:22 pm, 5/1/2026] ChatGPT: Soil Type (One-hot encoded: 0 to 39)
soil_type = st.selectbox("Soil Type (0–39)", list(range(40)))
soil_encoded = [0] * 40
soil_encoded[soil_type] = 1

features = [
    elevation, aspect, slope, hd_hydrology, vd_hydrology, hd_roadways,
    hillshade_9am, hillshade_noon, hillshade_3pm, hd_fire_points
] + wilderness_map[wilderness] + soil_encoded

if st.button("Predict Cover Type"):
    pred = model.predict([features])[0]
    st.success(f"Predicted Cover Type: {pred}")
