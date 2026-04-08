import os

import streamlit as st
import numpy as np
import pickle

@st.cache_resource
def load_model():
    model_path = os.path.join('model', 'house_price_model.pkl')
    with open(model_path, 'rb') as f:
        return pickle.load(f)

model = load_model()
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #333;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">🏠 House Price Prediction</p>', unsafe_allow_html=True)
st.sidebar.header("🏡 Input Features")
quality = st.sidebar.slider("Quality (1-10)", 1, 10, 5)
living_area = st.sidebar.number_input("Living Area (sq ft)", min_value=0)
garage_cars = st.sidebar.number_input("Garage Cars", min_value=0)
basement_area = st.sidebar.number_input("Basement Area", min_value=0)
full_bathrooms = st.sidebar.number_input("Full Bathrooms", min_value=0)
bedrooms = st.sidebar.number_input("Bedrooms", min_value=0)
lot_area = st.sidebar.number_input("Lot Area", min_value=0)
age = st.sidebar.number_input("Age", min_value=0)

predict_button = st.sidebar.button("🚀 Predict Price")
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📋 House Summary")

    st.write(f"Quality: {quality}")
    st.write(f"Living Area: {living_area}")
    st.write(f"Garage Cars: {garage_cars}")
    st.write(f"Basement Area: {basement_area}")
    st.write(f"Bathrooms: {full_bathrooms}")
    st.write(f"Bedrooms: {bedrooms}")
    st.write(f"Lot Area: {lot_area}")
    st.write(f"Age: {age}")

    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("💰 Prediction Result")

    if predict_button:
        try:
            data = np.array([[ 
                quality,
                living_area,
                garage_cars,
                basement_area,
                full_bathrooms,
                bedrooms,
                lot_area,
                age
            ]])

            prediction = model.predict(data)

            st.success(f"💵 Predicted Price: {prediction[0]:,.0f}")

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.info("👈 Enter data from sidebar and click Predict")

    st.markdown('</div>', unsafe_allow_html=True)