import streamlit as st
from services.crud import read_funcionarios
from datetime import datetime
from services.crud import get_setor_name, get_contrato_name, get_funcionario_id
from services.crud import create_register_atraso

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
    
# Extrair dados dos funcionários
funcionarios = read_funcionarios()
nomes_funcionarios = [nome for _, nome, *_ in funcionarios]

# Inicializar session_state para setor e contrato
if 'setor_selecionado' not in st.session_state: st.session_state['setor_selecionado'] = ""
if 'contrato_selecionado' not in st.session_state: st.session_state['contrato_selecionado'] = ""
    
# Função para atualizar setor e contrato com base no funcionário selecionado
def atualizar_dados_funcionario():
    funcionarios_del = st.session_state["funcionario_selecionado"]
    if funcionarios_del:
        funcionario = next((f for f in funcionarios if f[1] == funcionarios_del), None)
        if funcionario:
            id_setor = funcionario[4]
            id_contrato = funcionario[3]
            st.session_state['setor_selecionado'] = get_setor_name(id_setor)
            st.session_state['contrato_selecionado'] = get_contrato_name(id_contrato)
            st.session_state['id_funcionario'] = funcionario[0]  # Guardar o ID para deletar depois

# Formulário para deletar funcionário
st.write("### Registrar Atraso")
    
with st.container():
    col1, col2, col3 = st.columns([1.4, 0.8, 0.8])

    # Campo para selecionar o funcionário
    with col1: st.selectbox('Nome do funcionário:', nomes_funcionarios, key="funcionario_selecionado", on_change=atualizar_dados_funcionario)

    # Exibir setor e contrato atualizados
    with col2: st.text_input('Setor:', st.session_state['setor_selecionado'], disabled=True)
    with col3: st.text_input('Contrato:', st.session_state['contrato_selecionado'], disabled=True)
    
    col1, col2, col3 = st.columns([0.6, 0.6, 1.8])
    
    # Campos para data, hora e motivo do atraso
    with col1: data = st.text_input('Data do atraso:', key="data_atraso", placeholder="DD/MM/YYYY")
    if data: data = validar_data(data)
    with col2: hora = st.text_input('Hora do atraso:', key="hora_atraso", placeholder="HH:MM")
    if hora: hora = validar_hora(hora)
    with col3: motivo = st.text_input('Motivo do atraso:', key="motivo_atraso")                    
    

            
    # Botão para registrar atraso
    if st.button("Cadastrar"):
        # Converter hora para string, caso tenha sido validada com sucesso
        hora_str = hora.strftime('%H:%M') if hora else None
        
        try:
            create_register_atraso(data, hora_str, st.session_state['id_funcionario'], motivo)
            st.success("Atraso registrado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao cadastrar atraso: {e}")