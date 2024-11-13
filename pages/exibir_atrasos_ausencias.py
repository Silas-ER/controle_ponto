import streamlit as st
from services.crud import read_funcionarios, read_contratos, read_setors, read_generos

# Exibir setores para filtro
setores = read_setors()

col1, col2 = st.columns(2)

with col2: genero = st.selectbox("Gênero:", opcoes_genero)