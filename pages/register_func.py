import streamlit as st
from services.crud import create_funcionario, delete_funcionario, read_departments, read_contrato, read_funcionarios
from services.crud import get_department_name, get_contrato_name

with st.form("cadastrar_funcionario"):
    st.write("### Cadastrar Funcionário")
    
    with st.container():
        col1, col2, col3 = st.columns(3)

        setores = read_departments()
        contratos = read_contrato()
        
        # Extrair nomes dos setores e tipos de contrato
        opcoes_setores = [nome for _, nome in setores]
        opcoes_contrato = [nome for _, nome in contratos]   
        
        # Colunas de formulário
        with col1: funcionario = st.text_input('Nome do funcionário:')
        with col2: setor = st.selectbox("Setor:", opcoes_setores)
        with col3: contrato = st.selectbox("Contrato:", opcoes_contrato)

    # Submissão do formulário
    if st.form_submit_button("Cadastrar"):
        try:
            # Encontrar o setor e contrato selecionados
            setor_selecionado = next((t for t in setores if t[1] == setor), None)
            contrato_selecionado = next((t for t in contratos if t[1] == contrato), None)

            if setor_selecionado and contrato_selecionado:
                id_setor, nome_departamento = setor_selecionado
                id_contrato, nome_contrato = contrato_selecionado
                
                create_funcionario(funcionario, id_setor, id_contrato)
                st.success("Funcionário cadastrado com sucesso!")
            else:
                st.error("Erro: setor ou contrato não encontrado.")
        except Exception as e:
            st.error(f"Erro ao cadastrar funcionário: {e}")
           
    
########################################################################################################################          
           
           
with st.form("deletar_funcionario"):
    st.write("### Deletar Funcionário")
    
    with st.container():
        col1, col2, col3 = st.columns(3)

        # Extrair nomes e informações dos funcionários
        funcionarios = read_funcionarios()
        nomes_funcionarios = [nome for _, nome, *_ in funcionarios]
        
        # Coluna para selecionar o funcionário
        with col1:
            funcionarios_del = st.selectbox('Nome do funcionário:', nomes_funcionarios)

        if funcionarios_del:
            # Encontrar o funcionário selecionado e capturar setor e contrato
            funcionario_selecionado = next((f for f in funcionarios if f[1] == funcionarios_del), None)
            if funcionario_selecionado:
                id_setor = funcionario_selecionado[3]  # Assumindo que o id_setor está na posição 2
                id_contrato = funcionario_selecionado[2]  # Assumindo que o id_contrato está na posição 3
                id_funcionario = funcionario_selecionado[0]
                
                setor_selecionado = get_department_name(id_setor)
                contrato_selecionado = get_contrato_name(id_contrato)

                with col2:
                    setor_funcionarios = st.text_input('Setor:', setor_selecionado, disabled=True)
                with col3:
                    contrato_funcionarios = st.text_input('Contrato:', contrato_selecionado, disabled=True)
                    
    if st.form_submit_button("Deletar"):
        try:
            delete_funcionario(id_funcionario)
            st.success("Funcionário deletado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao deletar funcionário: {e}")
           