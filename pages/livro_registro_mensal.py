import streamlit as st
import pandas as pd
from services.crud import read_registers, read_atrasos, read_ausencias
from services.crud import get_contrato_name, get_funcionario_name, get_setor_name

from services.producao import get_producao
#######################################################################################################################################

# Título
st.title('Resumo do Mês:')

meses = {
    "Janeiro": 1, "Fevereiro": 2, "Março": 3, "Abril": 4, "Maio": 5, "Junho": 6,
    "Julho": 7, "Agosto": 8, "Setembro": 9, "Outubro": 10, "Novembro": 11, "Dezembro": 12
}

anos = [2024, 2025, 2026, 2027]

col1, col2 = st.columns([1, 1])

# Filtro Data
with col1: data = st.selectbox('Mês:', meses.keys())
with col2: ano = st.selectbox('Ano:', anos)

# Ler dos dados gerais
df_atrasos = read_atrasos()
df_ausencias = read_ausencias()
df_pontos = read_registers()

# Manipulação dos dados

# Convertendo colunas para datetime
if not df_atrasos.empty: df_atrasos['data'] = pd.to_datetime(df_atrasos['data'], errors='coerce')
if not df_ausencias.empty: df_ausencias['data'] = pd.to_datetime(df_ausencias['data'], errors='coerce')
if not df_pontos.empty: df_pontos['data'] = pd.to_datetime(df_pontos['data'], errors='coerce')

# Filtro de mês
mes = meses[data]

df_ausencias = df_ausencias[df_ausencias['data'].dt.month == mes]
df_atrasos = df_atrasos[df_atrasos['data'].dt.month == mes]

if df_ausencias.empty:
    st.expander('Nenhuma Ausência Registrada', expanded=False)
else:
    with st.expander('Ausências Registradas', expanded=False):
        st.dataframe(df_ausencias)
    
if df_atrasos.empty:
    st.expander('Nenhum Atraso Registrado', expanded=False)        
else:
    with st.expander('Atrasos Registrados', expanded=False):
        st.dataframe(df_atrasos)



 