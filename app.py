import streamlit as st
import pandas as pd
import joblib

model = joblib.load('traffic_model.pkl')

st.title("Traffic Congestion Predictor")

temp = st.number_input("Temperature",200.0,350.0,280.0)
rain = st.number_input("Rainfall",0.0,50.0,0.0)
snow = st.number_input("Snowfall",0.0,50.0,0.0)
clouds = st.slider("Cloud Coverage",0,100,50)
hour = st.slider("Hour",0,23,12)
day = st.slider("Day of Week",0,6,3)
month = st.slider("Month",1,12,6)

input_df = pd.DataFrame([[temp,rain,snow,clouds,hour,day,month]],
columns=['temp','rain_1h','snow_1h','clouds_all','hour','day','month'])

if st.button("Predict Congestion"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Congestion Level: {prediction}")