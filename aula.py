import streamlit as st
import pandas as pd

from sqlalchemy import create_engine


# Recebe os parâmetros via GET enquanto sem criptografia mandando direto (usar bearertok)
params = st.experimental_get_query_params()
# Obtém o valor do parâmetro 'variavel' da URL
senha = params.get('senha', ['SEM_DADOS'])[0]


#criando conexão com o banco de dados
conn = create_engine(f"postgresql://revisao_data:{senha}@revisao_data.postgresql.dbaas.com.br:5432/revisao_data")

#montando a tela 
st.write("Escolha uma das abas")

#consultando o banco de dados (conhecimento de SQL)
sql_query =  pd.read_sql_query (f"SELECT * FROM moodle_marcio2.fato_join;", con=conn)

df = pd.DataFrame(sql_query, columns = ['titulo', 'nome_completo', 'coh_frazier', 'coh_brunet', 'data_entrega'])



def gepeto():
   st.write("oi")

tab1, tab2, tab3 = st.tabs(["Entendendo meus dados" , "ChatGPT", "Gerador de gráfico", ])

with tab1:
   st.dataframe(df)

with tab2:
    gepeto()

with tab3: 
    import pygwalker as pyg
    from pygwalker.api.streamlit import StreamlitRenderer, init_streamlit_comm
    # Establish communication between pygwalker and streamlit
    init_streamlit_comm()

    @st.cache_resource
    def get_pyg_renderer() -> "StreamlitRenderer":
        # When you need to publish your app to the public, you should set the debug parameter to False to prevent other users from writing to your chart configuration file.
        return StreamlitRenderer(df, spec="./gw_config.json", debug=False)
 
    renderer = get_pyg_renderer()
 
    # Render your data exploration interface. Developers can use it to build charts by drag and drop.
    renderer.render_explore()