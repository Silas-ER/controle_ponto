import streamlit as st
from services.crud import create_department

with st.form("ponto"):
    st.write("### Cadastrar departamento")
    
    with st.container():
        col1, col2, col3 = st.columns([1,1,1])

        with col1: 
            setor = st.text_input('Nome do departamento:')
        with col2: 
            pass
        with col3: 
            pass

    if st.form_submit_button("Cadastrar"):
        try:
            create_department(setor)
            st.success("Departamento cadastrado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao cadastrar departamento: {e}") 