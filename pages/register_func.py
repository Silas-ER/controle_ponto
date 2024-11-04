import streamlit as st
from services.crud import create_funcionario, delete_funcionario, read_departments, read_contrato, read_funcionarios

with st.form("cadastrar_funcionario"):
    st.write("### Cadastrar Funcionário")
    
    with st.container():
        col1, col2, col3 = st.columns(3)

        setores = read_departments()
        tipo_contrato = read_contrato()
        
        #extrair nomes dos setores e tipos de contrato
        opcoes_setores = [nome for _, nome in setores]
        opcoes_contrato = [nome for _, nome in tipo_contrato]   
        
        #colunas de formulário
        with col1: funcionario = st.text_input('Nome do funcionário:')
        with col2: setor = st.selectbox("Setor:", opcoes_setores)
        with col3: tipo_contrato = st.selectbox("Contrato:", opcoes_contrato)

    #submissão do formulário
    if st.form_submit_button("Cadastrar"):
        try:
            id_setor = next(t[0] for t in setores if t[1] == setor)
            id_contrato = next(t[0] for t in tipo_contrato if t[1] == tipo_contrato)
            
            create_funcionario(funcionario, id_setor, id_contrato)
            
            st.success("Funcionário cadastrado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao cadastrar funcionário: {e}") 
   
"""           
with st.form("deletar_funcionario"):
    st.write("### Deletar Funcionário")
    
    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1: funcionario = st.text_input('Nome do funcionário:')
        with col2: setor = st.text_input('Setor:')
        with col3: tipo_funcionario = st.text_input('Tipo de funcionário:')

    if st.form_submit_button("Cadastrar"):
        try:
            create_department(setor)
            st.success("Departamento cadastrado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao cadastrar departamento: {e}") """ 