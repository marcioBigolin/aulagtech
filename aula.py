import streamlit as st
import pandas as pd

from sqlalchemy import create_engine


# Recebe os parâmetros via GET enquanto sem criptografia mandando direto (usar bearertok)
params = st.experimental_get_query_params()
# Obtém o valor do parâmetro 'variavel' da URL
bd = params.get('banco', ['SEM_DADOS'])[0]

#criando conexão com o banco de dados
conn = create_engine(bd)


#montando a tela 
st.set_page_config(page_title="Aula de low code GtechEDU", layout="wide")
st.subheader("Explore os dados utilizando Inteligência artificial")
st.write("Escrever algo")