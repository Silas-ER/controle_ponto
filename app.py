import streamlit as st
import datetime
import pandas as pd

#definições de pagina
st.set_page_config(
    page_title="Controle de Ponto", 
    page_icon=":mantelpiece_clock:", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

#lista de setores
setor = ['BENEFICIAMENTO', 'CAIS', 'CÂMARA FRIA', 'CARGA E DESCARGA', 'COPA', 'EMBALAGEM', 'LIMPEZA', 'QUALIDADE', 'RECEPÇÃO']

#tipos de contrato
tipo_contrato = ['CTPS', 'AVULSO']

#captura da data
today = datetime.date.today() 
formatted_date = today.strftime("%d/%m/%Y") # formatação da data

#listas de armazenamento temporario
db_func = []
db_diario = []

#exibição do formulario
with st.container():
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns([1,1.3,1,1.3,0.7,0.7,1,1])

    with col1: date = st.text_input('Data (DD/MM/YYYY):', key='data_input')
    with col2: selected_setor = st.selectbox('Setor:', setor)
    with col3: tipo_funcionario = st.selectbox('Tipo de funcionário:', tipo_contrato)
    with col4: nome_funcionario = st.text_input('Nome do funcionário:')
    with col5: hora_entrada = st.text_input('Entrada (HH:MM):', key='hora_entrada_input')
    with col6: hora_saida = st.text_input('Saida (HH:MM):', key='hora_saida_input')
    with col7: observacao = st.text_input('Observação:')
    with col8: 
        st.markdown(' ')
        st.markdown(' ')
        if st.button('Registrar ponto'):
            db_diario.append([date, selected_setor, tipo_funcionario, nome_funcionario, hora_entrada, hora_saida, observacao])
            #st.success('Ponto registrado com sucesso!')

#exibição de dados para controle   
with st.container():
    df_diario = pd.DataFrame(db_diario, columns=['date', 'selected_setor', 'tipo_funcionario', 'nome_funcionario', 'hora_entrada', 'hora_saida', 'observacao'])
    st.dataframe(df_diario)    

with st.container():
    col1, col2 = st.columns([1.6, 0.4])
    db_func = df_diario.groupby(['date', 'selected_setor']).agg('count').reset_index()

    #
    total_employees = df_diario.shape[0]
    # 
    ctps_count = df_diario[df_diario['tipo_funcionario'] == 'CTPS'].shape[0]
    temporary_count = df_diario[df_diario['tipo_funcionario'] == 'AVULSO'].shape[0]

    #exibição de metricas de controle
    with col1:                       
        st.dataframe(db_func)

    with col2:
        st.metric("Total de funcionários", total_employees)

        st.metric("Funcionários CTPS", ctps_count)

        st.metric("Funcionários temporários", temporary_count)