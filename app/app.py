import streamlit as st

from predict_aqi import predict_aqi

st.title('Air Quality Index Predictor')
st.write('This is a machine learning application to help predict Air Quality Index levels')

# FORM
st.header('Fill in the form below')
st.write('Enter the weather conditions.')

temperature = st.number_input(label='Enter temperature in celsius:', min_value=10.0, max_value=100.0, value=20.0)

pressure = st.number_input(label='Enter pressure:', min_value=500.0, max_value=1500.0, value=1000.0)

humidity = st.number_input(label='Enter humidity:', min_value=10.0, max_value=150.0, value=20.0)

wind = st.number_input(label='Enter wind speed:', min_value=1.0, max_value=20.0, value=1.0)

if st.button(label='Predict AQI'):
    aqi = predict_aqi(temperature, pressure, humidity, wind)
    
    st.success(f'Air Quality Index is: {aqi[0]:.2f}')
