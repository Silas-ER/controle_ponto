import streamlit as st
import datetime, yaml
import pandas as pd
import streamlit_authenticator as stauth
from yaml.loader import SafeLoader

#definições de pagina
st.set_page_config(
    page_title="Controle de Ponto", 
    page_icon=":mantelpiece_clock:", 
    initial_sidebar_state="collapsed",
    layout="centered"
)

with open("config.yaml", "r") as f:
    config = yaml.load(f, Loader=SafeLoader)
    
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)

# tentar executar o processo de login
try:
    authenticator.login()
except Exception as e:
    st.error(e)

# condições de login e carregamento de páginas
if st.session_state["authentication_status"] is True:
    col1, col2 = st.columns(2)
    with col1: st.write(f'Logado como *{st.session_state["name"]}*')
    with col2: authenticator.logout()
    
    st.divider()

    #páginas do app
    ponto = st.Page("pages/ponto_avulso.py", title="Registrar Ponto Avulso", icon="⌛", default=True)
    atrasos = st.Page("pages/atraso.py", title="Registrar Atraso")
    ausencia = st.Page("pages/ausencia.py", title="Registrar Ausência")
    
    diary = st.Page("pages/diary.py", title="Resumo Diário e Mensal", icon="📆")
    delete_register = st.Page("pages/delete_register.py", title="Excluir Registro", icon="🗑️")
    
    
    
    register_func = st.Page("pages/register_func.py", title="Cadastrar/Excluir Funcionários", icon="📓")
    register_dept = st.Page("pages/register_dept.py", title="Cadastrar/Excluir Departamentos", icon="📒")
    
    metrics =  st.Page("pages/metrics.py", title="Métricas de funcionários", icon="📊")
    
    #navegação
    pg = st.navigation(
        {
            "Ponto": [ponto, atrasos, ausencia],
            "Cadastros e Exclusões": [register_func, register_dept],
            "Métricas:": [metrics],
        }
    )
    
    pg.run()
    

elif st.session_state["authentication_status"] is False:
    st.error('Usuário ou senha incorretos')
elif st.session_state["authentication_status"] is None:
    st.warning('Faça login para acessar o sistema')
    





