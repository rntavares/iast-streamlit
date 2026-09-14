import streamlit as st
import joblib
import pandas as pd


@st.cache_resource
def load_model():
    return joblib.load("modelo_churn.joblib")


model = load_model()

st.title("Previsão de Churn de Clientes")
st.caption("Lab AWS — rodando em uma instância EC2")

idade = st.slider("Idade do cliente", 18, 90, 35)
meses = st.number_input("Meses como cliente", min_value=0, value=12)
valor = st.number_input("Valor mensal (R$)", min_value=0.0, value=79.90)

if st.button("Prever"):
    entrada = pd.DataFrame(
        [[idade, meses, valor]],
        columns=["idade", "meses", "valor_mensal"],
    )
    proba = model.predict_proba(entrada)[0][1]
    st.metric("Probabilidade de churn", f"{proba:.1%}")
    if proba > 0.5:
        st.warning("Cliente em risco — sugerir ação de retenção.")
    else:
        st.success("Cliente com baixo risco de cancelamento.")
