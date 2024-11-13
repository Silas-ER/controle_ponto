import streamlit as st
import pandas as pd
from services.crud import read_registers

pontos = read_registers()

df_pontos = pd.DataFrame(pontos)

# Função para calcular as horas noturnas entre um intervalo de entrada e saída
def calcular_horas_noturnas(entrada, saida):
    inicio_periodo_noturno = entrada.replace(hour=22, minute=0, second=0)
    fim_periodo_noturno = entrada.replace(hour=5, minute=0, second=0) + pd.Timedelta(days=1)
    
    # Caso a saída ocorra no dia seguinte, ajustar o fim do período noturno
    if saida < entrada:
        saida += pd.Timedelta(days=1)

    inicio = max(entrada, inicio_periodo_noturno)
    fim = min(saida, fim_periodo_noturno)
    
    if inicio < fim:
        return (fim - inicio).total_seconds() / 3600  # horas noturnas
    return 0
 
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

# Horas noturnas 
df_pontos['Horas_Noturnas'] = (
    df_pontos.apply(lambda row: calcular_horas_noturnas(row['Hora_Entrada1'], row['Hora_Saida1']), axis=1) +
    df_pontos.apply(lambda row: calcular_horas_noturnas(row['Hora_Entrada2'], row['Hora_Saida2']), axis=1)
)

col1, col2, col3, col4 = st.columns(4)

with col1: st.markdown('##### Funcionário')
with col2: st.markdown('##### Setor')
with col3: st.markdown('##### Horas Trabalhadas')
with col4: st.markdown('##### Horas Noturnas')

for _, index in df_pontos.iterrows():
    with col1: st.write(index['funcionario'])
    with col2: st.write(index['setor'])
    with col3: st.write(index['Total_Trabalhado'])
    with col4: st.write(index['Horas_Noturnas'])
    st.write('---')