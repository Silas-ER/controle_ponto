import streamlit as st

col1, col2 = st.columns(2)

with col2: genero = st.selectbox("Gênero:", opcoes_genero)