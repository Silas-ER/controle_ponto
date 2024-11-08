import streamlit as st
from services.crud import read_funcionarios, read_contratos, read_setors
from datetime import datetime
from services.crud import get_setor_name, get_contrato_name, get_contrato_id, get_setor_id, get_funcionario_id
from services.crud import create_register

# Funções para validar data e hora
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
    
# Função para atualizar setor e contrato com base no funcionário selecionado
def atualizar_dados_funcionario():
    funcionarios_selecionado = st.session_state["funcionario_selecionado"]
    if funcionarios_selecionado:
        funcionario = next((f for f in funcionarios if f[1] == funcionarios_selecionado), None)
        if funcionario:
            id_setor = funcionario[3]
            id_contrato = funcionario[2]
            st.session_state['setor_selecionado'] = get_setor_name(id_setor)
            st.session_state['contrato_selecionado'] = get_contrato_name(id_contrato)

# Carregar dados iniciais de setores, contratos e funcionários
setores = read_setors()
contratos = read_contratos()
funcionarios = read_funcionarios()
nome_funcionarios = [nome for id, nome, *_ in funcionarios]

# Inicializar session_state para setor e contrato selecionados
if 'setor_selecionado' not in st.session_state: st.session_state['setor_selecionado'] = ""
if 'contrato_selecionado' not in st.session_state: st.session_state['contrato_selecionado'] = ""

# Layout para registrar atraso
st.write("### Registrar Atraso")

with st.container():
    col1, col2, col3, col4 = st.columns([1.6,0.8,0.8,0.8])

    # Campos para selecionar o funcionário e data
    with col1: st.selectbox('Nome do funcionário:', nome_funcionarios, key="funcionario_selecionado", on_change=atualizar_dados_funcionario)
    with col2: st.text_input('Setor:', st.session_state['setor_selecionado'], disabled=True)    
    with col3: st.text_input('Contrato:', st.session_state['contrato_selecionado'], disabled=True)  
    with col4:
        data_input = st.text_input('Data (DD/MM/YYYY):')
        if data_input: data_valida = validar_data(data_input)  
          
    # Alteração do tamanho das colunas
    col1, col2 = st.columns([0.5,1.5])        
    with col1: st.text_input('Hora de chegada (HH:MM):')    
    with col2: observacao = st.text_input('Justificativa:')

# Botão para registrar o ponto, somente se todas as entradas forem válidas
if st.button("Registrar"):
   pass