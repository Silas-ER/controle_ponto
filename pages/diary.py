import streamlit as st
import pandas as pd
from services.crud import read_registers
from services.crud import get_contrato_name, get_funcionario_name, get_setor_name

geral = read_registers()

df_geral = pd.DataFrame(geral)

###################################################################################################################################

# Formatação da data
df_geral['Dia'] = pd.to_datetime(df_geral['data'])
df_geral['Dia'] = df_geral['Dia'].dt.strftime('%d/%m/%Y')

# Formatação das horas
df_geral['Hora_Entrada1'] = pd.to_datetime(df_geral['entrada1'], format='%H:%M:%S')
df_geral['Hora_Saida1'] = pd.to_datetime(df_geral['saida1'], format='%H:%M:%S')
df_geral['Hora_Entrada2'] = pd.to_datetime(df_geral['entrada2'], format='%H:%M:%S')
df_geral['Hora_Saida2'] = pd.to_datetime(df_geral['saida2'], format='%H:%M:%S')

# Calculo das horas trabalhadas
df_geral['Horas_trabalhadas'] = (
           df_geral['Hora_Saida1'] - df_geral['Hora_Entrada1']
        ) + (
           df_geral['Hora_Saida2'] - df_geral['Hora_Entrada2']
        )

# Simplificação das horas para exibição
df_geral['Hora_Entrada1'] = df_geral['Hora_Entrada1'].dt.strftime('%H:%M')
df_geral['Hora_Saida1'] = df_geral['Hora_Saida1'].dt.strftime('%H:%M')
df_geral['Hora_Entrada2'] = df_geral['Hora_Entrada2'].dt.strftime('%H:%M')
df_geral['Hora_Saida2'] = df_geral['Hora_Saida2'].dt.strftime('%H:%M')
df_geral['Horas_trabalhadas'] = df_geral['Horas_trabalhadas'].apply(lambda x: f"{int(x.total_seconds() // 3600)}:{int((x.total_seconds() % 3600) // 60):02d}")

###################################################################################################################################

# Título
st.title('Diário de Ponto')
st.write('---')

# Filtro de data
col1, col2 = st.columns(2)
with col1: data_filtro_inicial = st.date_input('Selecione uma data inicial:', pd.to_datetime('today'), key='data_inicial')
with col2: data_filtro_fina = st.date_input('Selecione uma data final:', pd.to_datetime('today'), key='data_final')
st.write('---')

# Apresentação de dados
for index, row in df_geral.iterrows():
    
    funcionario = get_funcionario_name(row['funcionario']) # Pegar nome do funcionario
    contrato = get_contrato_name(row['funcionario']) # Pegar contrato do funcionario
    setor = get_setor_name(row['setor']) # Pegar setor do funcionario
    
    st.markdown(f"""
                <div>
                    <h3>{funcionario} - {setor}</h3>  
                    <p>
                        {row['Dia']} - Entrada 1: {row['Hora_Entrada1']} - Saída 1: {row['Hora_Saida1']} - 
                        Entrada 2: {row['Hora_Entrada2']} - Saída 2: {row['Hora_Saida2']} - Horas Trabalhadas: {row['Horas_trabalhadas']} 
                        - Observação: {row['observacao']} - <button>Excluir Registro</button>
                    </p>
                    
                </div>
                """, unsafe_allow_html=True)
    st.write('---')
