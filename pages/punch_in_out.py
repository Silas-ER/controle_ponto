import streamlit as st

setor = []
tipo_contrato = []

with st.form("ponto"):
    st.write("### Registrar Ponto")
    
    with st.container():
        col1, col2, col3 = st.columns([1,1,1])

        with col1: 
            date = st.text_input('Data (DD/MM/YYYY):', key='data_input')
            nome_funcionario = st.text_input('Nome do funcionário:')
        with col2: 
            selected_setor = st.selectbox('Setor:', setor)
            hora_entrada = st.text_input('Entrada (HH:MM):', key='hora_entrada_input')
        with col3: 
            tipo_funcionario = st.selectbox('Tipo de funcionário:', tipo_contrato)
            hora_saida = st.text_input('Saida (HH:MM):', key='hora_saida_input')
            
    observacao = st.text_input('Observação:')
    if st.form_submit_button("Registrar"):
        st.success("Ponto registrado com sucesso!")