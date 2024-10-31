import streamlit as st
import datetime
import pandas as pd

#definições de pagina
st.set_page_config(
    page_title="Controle de Ponto", 
    page_icon=":mantelpiece_clock:", 
    layout="wide", 
)

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
