# -*- coding: utf-8 -*-
import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pandas as pd
import pickle

# Set Streamlit config
st.set_page_config(page_title="📉 Customer Churn Predictor", page_icon="📉", layout="centered")

# Load trained model
model = tf.keras.models.load_model('customer_churn_model.h5')

# Load encoders and scaler
with open('label_encoder_gender.pkl', 'rb') as file:
    label_encoder_gender = pickle.load(file)

with open('ohe_geo.pkl', 'rb') as file:
    onehot_encoder_geo = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Sidebar
with st.sidebar:
    st.image("https://avatars.githubusercontent.com/u/107360623?v=4", caption="Tajamul Khan", width=120)
    st.markdown("## 📘 About")
    st.markdown("""
    **App Name:** Customer Churn Predictor  
    **Author:** Tajamul Khan  
    **Model:** Deep Learning (Keras Sequential)  
    **Connect:** [LinkedIn](https://www.linkedin.com/in/tajamulkhann/)
    """)

# Header
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>📉 Customer Churn Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Predict whether a customer is likely to churn based on their profile.</p>", unsafe_allow_html=True)
st.markdown("---")

# User input form
col1, col2 = st.columns(2)

with col1:
    geography = st.selectbox('🌍 Geography', onehot_encoder_geo.categories_[0])
    gender = st.selectbox('🧑 Gender', label_encoder_gender.classes_)
    age = st.slider('🎂 Age', 18, 92)
    balance = st.number_input('💰 Balance')
    credit_score = st.number_input('📊 Credit Score')

with col2:
    estimated_salary = st.number_input('📈 Estimated Salary')
    tenure = st.slider('📅 Tenure (Years)', 0, 10)
    num_of_products = st.slider('🛒 Number of Products', 1, 4)
    has_cr_card = st.selectbox('💳 Has Credit Card', [0, 1])
    is_active_member = st.selectbox('✅ Is Active Member', [0, 1])

# Predict button
if st.button("🔍 Predict Churn"):
    try:
        # Prepare input
        input_data = pd.DataFrame({
            'CreditScore': [credit_score],
            'Gender': [label_encoder_gender.transform([gender])[0]],
            'Age': [age],
            'Tenure': [tenure],
            'Balance': [balance],
            'NumOfProducts': [num_of_products],
            'HasCrCard': [has_cr_card],
            'IsActiveMember': [is_active_member],
            'EstimatedSalary': [estimated_salary]
        })

        # One-hot encode Geography
        geo_encoded = onehot_encoder_geo.transform([[geography]]).toarray()
        geo_encoded_df = pd.DataFrame(geo_encoded, columns=onehot_encoder_geo.get_feature_names_out(['Geography']))

        # Final input
        input_data = pd.concat([input_data.reset_index(drop=True), geo_encoded_df], axis=1)
        input_data_scaled = scaler.transform(input_data)

        # Prediction
        prediction = model.predict(input_data_scaled)[0][0]
        st.success(f"📉 Churn Probability: {prediction:.2f}")

        if prediction > 0.5:
            st.error("🚨 The customer is **likely to churn.**")
        else:
            st.success("✅ The customer is **not likely to churn.**")

    except Exception as e:
        st.error(f"❌ Error: {e}")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; font-size: 12px;'>
    © 2025 <b>Tajamul Khan</b> | Built with ❤️ using Streamlit  
    <a href='https://www.linkedin.com/in/tajamulkhann/' target='_blank'>🔗 LinkedIn</a>
</div>
""", unsafe_allow_html=True)
