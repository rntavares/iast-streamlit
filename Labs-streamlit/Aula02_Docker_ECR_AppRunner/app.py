import streamlit as st

st.title("Minha App ML")
st.caption("Lab AWS — imagem publicada no Amazon ECR e servida pelo AWS App Runner")

st.write(
    "Substitua este conteúdo pela sua aplicação real "
    "(por exemplo, a app de predição da Aula 01)."
)

nome = st.text_input("Seu nome")
if nome:
    st.success(f"Olá, {nome} — containerizado e rodando na nuvem!")
