import streamlit as st
import pandas as pd
from services.crud import read_atrasos, read_ausencias
from services.crud import get_contrato_name, get_funcionario_name, get_setor_name

from services.limpeza_dados import atrasos_por_data, ausencias_por_data
from services.producao import get_producao
#######################################################################################################################################

# Título
st.title('Resumo do Dia')

col1, col2 = st.columns([1, 1])

# Filtro Data
with col1: data = st.date_input('Data:', pd.to_datetime('today').date())

# Dados filtrados
atrasados = atrasos_por_data(data)
ausentes = ausencias_por_data(data)

if data:
    with st.container():
        col1, col2 = st.columns([1, 1])
        
        # Funcionarios
        with col1: 
            st.write("Avulsos do dia")

        with col2:
            pass
        
    with st.container():
        with col1:
            st.write("Atrasos") 
            st.write("Ausências")