import streamlit as st
import pandas as pd
import joblib

model = joblib.load('Classification.pkl')

st.title('Water Potability Predictor')
st.write('Enter the water quality values to check if the water is safe to drink.')

ph = st.number_input('pH', 0.0, 14.0, 7.0)
hardness = st.number_input('Hardness', 0.0, 500.0, 200.0)
solids = st.number_input('Solids', 0.0, 70000.0, 20000.0)
chloramines = st.number_input('Chloramines', 0.0, 15.0, 7.0)
sulfate = st.number_input('Sulfate', 0.0, 500.0, 330.0)
conductivity = st.number_input('Conductivity', 0.0, 1000.0, 420.0)
organic_carbon = st.number_input('Organic_carbon', 0.0, 40.0, 14.0)
trihalomethanes = st.number_input('Trihalomethanes', 0.0, 150.0, 66.0)
turbidity = st.number_input('Turbidity', 0.0, 10.0, 4.0)

if st.button('Predict'):
    row = pd.DataFrame([{
        'ph': ph,
        'Hardness': hardness,
        'Solids': solids,
        'Chloramines': chloramines,
        'Sulfate': sulfate,
        'Conductivity': conductivity,
        'Organic_carbon': organic_carbon,
        'Trihalomethanes': trihalomethanes,
        'Turbidity': turbidity,
    }])
    result = model.predict(row)[0]
    if result == 1:
        st.success('Water is potable (safe to drink).')
    else:
        st.error('Water is NOT potable.')
