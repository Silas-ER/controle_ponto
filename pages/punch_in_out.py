import streamlit as st
from services.crud import read_funcionarios, read_contrato, read_departments
from datetime import datetime

def get_setor_id(setores, selected_setor):
    return next((id for id, nome in setores if nome == selected_setor), None)

def get_contrato_id(contratos, tipo_funcionario):
    return next((id for id, nome in contratos if nome == tipo_funcionario), None)

def get_funcionarios_ativos(funcionarios, id_contrato, id_setor):
    return [nome for id, nome, contrato, departamento in funcionarios if contrato == id_contrato and departamento == id_setor]

def validar_data(data_str):
    try:
        return datetime.strptime(data_str, '%d/%m/%Y')
    except ValueError:
        st.error("Data inválida. Use o formato DD/MM/YYYY.")
        return None

def validar_hora(hora_str):
    try:
        return datetime.strptime(hora_str, '%H:%M').time()
    except ValueError:
        st.error("Hora inválida. Use o formato HH:MM.")
        return None

with st.form("ponto"):
    st.write("### Registrar Ponto")
    
    with st.container():
        col1, col2, col3 = st.columns([1, 1, 1])
        
        # Manipulação de dados de setores e contratos
        setores = read_departments()
        contratos = read_contrato()
        
        nomes_setores = [nome for id, nome in setores]
        nomes_contratos = [nome for id, nome in contratos]
        
        # Manipulação de dados de funcionários
        funcionarios = read_funcionarios()
        
        # Campos de seleção
        with col1:
            selected_setor = st.selectbox('Setor:', nomes_setores)
            data_input = st.text_input('Data (DD/MM/YYYY):')
            data_valida = validar_data(data_input)
        
        with col2:
            tipo_funcionario = st.selectbox('Tipo de funcionário:', nomes_contratos)
            hora_entrada_input = st.text_input('Entrada (HH:MM):')
            hora_entrada_valida = validar_hora(hora_entrada_input)
        
        with col3:
            # Obtenção dos IDs do setor e contrato
            id_setor = get_setor_id(setores, selected_setor)
            id_contrato = get_contrato_id(contratos, tipo_funcionario)
            
            # Filtragem de funcionários ativos
            if id_setor is not None and id_contrato is not None:
                funcionarios_ativos = get_funcionarios_ativos(funcionarios, id_contrato, id_setor)
            else:
                funcionarios_ativos = [nome for id, nome, _, _ in funcionarios]  # Todos os funcionários
            
            nome_funcionario = st.selectbox('Nome do funcionário:', funcionarios_ativos)
            hora_saida_input = st.text_input('Saída (HH:MM):')
            hora_saida_valida = validar_hora(hora_saida_input)
    
    observacao = st.text_input('Observação:')
    
    # Botão para registrar o ponto, somente se todas as entradas forem válidas
    if st.form_submit_button("Registrar"):
        if data_valida and hora_entrada_valida and hora_saida_valida:
            # Aqui você pode adicionar a lógica para registrar o ponto
            st.success("Ponto registrado com sucesso!")
        else:
            st.error("Por favor, corrija os campos com erro.")
