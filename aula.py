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

sql_query =  pd.read_sql_query (f"SELECT * FROM moodle_marcio2.fato_join;", con=conn)

df = pd.DataFrame(sql_query, columns = ['titulo', 'nome_completo', 'coh_frazier', 'coh_brunet', 'data_entrega'])