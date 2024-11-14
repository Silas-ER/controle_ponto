import streamlit as st
import pandas as pd
from services.crud import read_registers
from services.crud import get_contrato_name, get_funcionario_name, get_setor_name

from services.producao import get_producao
#######################################################################################################################################

# Título
st.title('Resumo do Dia')

col1, col2 = st.columns([1, 1])

# Filtro Data
with col1: data = st.date_input('Data:', pd.to_datetime('today').date())

