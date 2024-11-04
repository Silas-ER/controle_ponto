import streamlit as st
from services.crud import create_department, read_departments, delete_department

with st.form("cadastrar_departamento"):
    st.write("### Cadastrar departamento")
    
    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1: 
            setor = st.text_input('Nome do departamento:')
        with col2: pass
        with col3: pass

    if st.form_submit_button("Cadastrar"):
        try:
            create_department(setor)
            st.success("Departamento cadastrado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao cadastrar departamento: {e}") 
   
            
with st.form("deletar_departamento"):
    st.write("### Deletar departamento")
    
    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1: 
            setores = read_departments()
            
            # Criar o dropdown, exibindo apenas os nomes
            opcoes_setores = [nome for _, nome in setores]
            departamento_selecionado = st.selectbox("Setor:", opcoes_setores)      
               
        with col2: pass
        with col3: pass    
                
        # Ao clicar em "Deletar", obter a tupla completa e passar para a função de exclusão
        if st.form_submit_button("Deletar"):
            try:
                # Encontrar a tupla completa com base no nome selecionado
                tupla_selecionada = next(t for t in setores if t[1] == departamento_selecionado)
                id_departamento, nome_departamento = tupla_selecionada
                delete_department(id_departamento) 
                st.success("Departamento deletado com sucesso!")
            except Exception as e:
                st.error(f"Erro ao deletar departamento: {e}")