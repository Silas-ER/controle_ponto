import streamlit as st
import pandas as pd
from services.crud import read_registers

pontos = read_registers()

df_pontos = pd.DataFrame(pontos)

# Formatação das horas
df_pontos['Hora_Entrada1'] = pd.to_datetime(df_pontos['entrada1'], format='%H:%M:%S')
df_pontos['Hora_Saida1'] = pd.to_datetime(df_pontos['saida1'], format='%H:%M:%S')
df_pontos['Hora_Entrada2'] = pd.to_datetime(df_pontos['entrada2'], format='%H:%M:%S')
df_pontos['Hora_Saida2'] = pd.to_datetime(df_pontos['saida2'], format='%H:%M:%S')

# Calculo das horas trabalhadas
df_pontos['Horas_trabalhadas'] = (
           df_pontos['Hora_Saida1'] - df_pontos['Hora_Entrada1']
        ) + (
           df_pontos['Hora_Saida2'] - df_pontos['Hora_Entrada2']
        )

df_pontos['Total_Trabalhado'] = df_pontos['Horas_trabalhadas'].groupby(df_pontos['funcionario']).transform('sum')

col1, col2, col3, col4 = st.columns(4)

with col1: st.markdown('##### Funcionário')
with col2: st.markdown('##### Setor')
with col3: st.markdown('##### Horas Trabalhadas')
with col4: st.markdown('##### Horas Noturnas')

for _, index in df_pontos.iterrows():
    with col1: st.write(index['funcionario'])
    with col2: st.write(index['setor'])
    with col3: st.write(index['Total_Trabalhado'])
    #with col4: st.write(index['horas_noturnas'])
    st.write('---')