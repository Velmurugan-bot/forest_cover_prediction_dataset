import streamlit as st
import pandas as pd
import joblib

model = joblib.load('model.pkl')
prediction = model.predict(['features_names.pkl'])

st.title("🌲 Forest Cover Type Prediction")

elevation = st.number_input('Elevation' 0, 4000, step=1)
aspect = st.number_input('Aspect' 0, 360, step=1)
slope = st.number_input("Slope", 0, 90, step=1)
hd_hydrology = st.number_input('Horizontal_Distance_To_Hydrology', step=1)
vd_hydrology = st.number_input('Vertical_Distance_To_Hydrology', step=1)
hd_roadways = st.number_input('Horizontal_Distance_To_Roadways', step=1)
hillshade_9am = st.number_input('Hillshade_9am', 0, 255, step=1)
hillshade_noon = st.number_input("Hillshade_Noon", 0, 255, step=1)
hillshade_3pm = st.number_input("Hillshade_3pm", 0, 255, step=1)
hd_fire_points = st.number_input("Horizontal_Distance_to_Fire_Points", step=1)

wilderness = st.selectbox("Wilderness_Area", ["Rawah", "Neota", "Comanche Peak", "Cache la Poudre"])
wilderness_map = {
    "Rawah": [1, 0, 0, 0],
    "Neota": [0, 1, 0, 0],
    "Comanche Peak": [0, 0, 1, 0],
    "Cache la Poudre": [0, 0, 0, 1]
}

soil_type = st.selectbox("Soil_Type (0–39)", list(range(40)))
soil_encoded = [0] * 40
soil_encoded[soil_type] = 1


features = [
    elevation, aspect, slope, hd_hydrology, vd_hydrology, hd_roadways,
    hillshade_9am, hillshade_noon, hillshade_3pm, hd_fire_points
] + wilderness_map[wilderness] + soil_encoded


if st.button("Predict Cover_Type"):
    pred = model.predict([features])[0]
    st.success(f"Predicted Cover_Type: {pred}")
