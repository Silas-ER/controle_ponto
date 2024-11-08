import streamlit as st
from services.crud import create_funcionario, delete_funcionario, read_setors, read_contratos, read_funcionarios
from services.crud import get_setor_name, get_contrato_name

with st.form("cadastrar_funcionario"):
    st.write("### Cadastrar Funcionário")
    
    with st.container():
        col1, col2, col3, col4 = st.columns(3)

        setores = read_setors()
        contratos = read_contratos()
        
        # Extrair nomes dos setores e tipos de contrato
        opcoes_setores = [nome for _, nome in setores]
        opcoes_contrato = [nome for _, nome in contratos]
        opcoes_genero = ["MASCULINO", "FEMININO"]   
        
        # Colunas de formulário
        with col1: funcionario = st.text_input('Nome do funcionário:')
        with col2: genero = st.selectbox("Gênero:", opcoes_genero)
        with col3: setor = st.selectbox("Setor:", opcoes_setores)
        with col4: contrato = st.selectbox("Contrato:", opcoes_contrato)

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
st.divider()    
########################################################################################################################          
           
# Extrair dados dos funcionários
funcionarios = read_funcionarios()
nomes_funcionarios = [nome for _, nome, *_ in funcionarios]

# Inicializar session_state para setor e contrato
if 'setor_selecionado' not in st.session_state:
    st.session_state['setor_selecionado'] = ""
if 'contrato_selecionado' not in st.session_state:
    st.session_state['contrato_selecionado'] = ""
    
# Função para atualizar setor e contrato com base no funcionário selecionado
def atualizar_dados_funcionario():
    funcionarios_del = st.session_state["funcionario_selecionado"]
    if funcionarios_del:
        funcionario = next((f for f in funcionarios if f[1] == funcionarios_del), None)
        if funcionario:
            id_setor = funcionario[3]
            id_contrato = funcionario[2]
            st.session_state['setor_selecionado'] = get_setor_name(id_setor)
            st.session_state['contrato_selecionado'] = get_contrato_name(id_contrato)
            st.session_state['id_funcionario'] = funcionario[0]  # Guardar o ID para deletar depois

# Formulário para deletar funcionário
st.write("### Deletar Funcionário")
    
with st.container():
    col1, col2, col3 = st.columns(3)

    # Campo para selecionar o funcionário
    with col1:
        st.selectbox('Nome do funcionário:', nomes_funcionarios, key="funcionario_selecionado", on_change=atualizar_dados_funcionario)

    # Exibir setor e contrato atualizados
    with col2:
        st.text_input('Setor:', st.session_state['setor_selecionado'], disabled=True)
    with col3:
        st.text_input('Contrato:', st.session_state['contrato_selecionado'], disabled=True)
                    
    # Botão para deletar o funcionário
    if st.button("Deletar"):
        try:
            delete_funcionario(st.session_state['id_funcionario'])
            st.success("Funcionário deletado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao deletar funcionário: {e}")
           