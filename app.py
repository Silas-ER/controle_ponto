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

def load_page():
    #páginas do app
    in_out = st.Page("pages/punch_in_out.py", title="Registrar Ponto", icon="⌛", default=True)
    diary = st.Page("pages/diary.py", title="Resumo Diário e Mensal", icon="📆")
    register_func = st.Page("pages/register.py", title="Cadastrar novo funcionário", icon="📖")
    #register_dept = st.Page("pages/register_dept.py", title="Cadastrar novo setor", icon="📖")
    #delete_func = st.Page("pages/delete.py", title="Excluir funcionário", icon="🗑️")
    #delete_dept = st.Page("pages/delete_dept.py", title="Excluir setor", icon="🗑️")
    metrics =  st.Page("pages/metrics.py", title="Métricas de funcionários", icon="📊")
    #api_consult = st.Page("pages/api_consult.py", title="Consultar Embarcações", icon="🔍")

    #navegação
    pg = st.navigation(
        {
            "Ponto": [in_out, diary],
            "Cadastros e Exclusões": [register_func],
            "Métricas:": [metrics],
        }
    )
    
    pg.run()
    
with open("config.yaml", "r") as f:
    config = yaml.load(f, Loader=SafeLoader)
    
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)

authenticator.login()

if st.session_state["authentication_status"]:
    load_page()
    st.divider()
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.write(f'Logado como *{st.session_state["name"]}*')
    with col2: 
        authenticator.logout()
elif st.session_state["authentication_status"] is False:
    st.error('Usuário ou senha incorretos')
elif st.session_state["authentication_status"] is None:
    st.warning('Faça login para acessar o sistema')
    





