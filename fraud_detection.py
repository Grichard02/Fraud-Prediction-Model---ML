import streamlit as st
import pandas as pd 
import joblib

model = joblib.load("fraud_detection_pipeline.pkl")

st.title("Aplicación de predicción para detectar fraude")

st.markdown("Por favor ingresar los detalles de transacción y usar el botón para predecir")

st.divider()

transaction_type = st.selectbox("Transaction Type",["PAYMENT","TRANSFER","CASH_OUT","DEBIT"])
amount = st.number_input("Amount", min_value=0.0, value=10.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value= 0.0, value=100.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=90.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest,
    }])


    prediction = model.predict(input_data)[0]

    st.subheader(f"Predicción: '{int(prediction)}'")

    if prediction == 1:
        st.error("Esta transacción puede ser un fraude")
    else:
        st.success("Esta transacción parece que no es un fraude")
