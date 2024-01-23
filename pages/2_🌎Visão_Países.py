# ==============================
# Bibliotecas
# ==============================
import pandas as pd
import streamlit as st
from PIL import Image
import plotly.express       as px
import plotly.graph_objects as go
from matplotlib             import pyplot as plt
# ==============================
# Configs
# ==============================
st.set_page_config(
    page_title='Visão Países',
    page_icon=':earth_americas:',
    layout='wide'
)

# Importando Dataset
df_root = pd.read_csv('dataset/clean_zomato.csv')

# Fazendo cópia do dataframe lido
df = df_root.copy()
df.head()
print(df.head())
# ==============================
# Funções
# ==============================
def bar_chart(data, x, y, color, title, textauto):
    plt.figure(figsize = (20,15))
    fig = px.bar(data, x = x, y = y, color=color, text_auto=textauto, title = title, template='seaborn')
    return fig

def treemap_graph(data, path, value, color):
    
    fig = px.treemap(data, path=[path], values=value, color = color, color_continuous_scale = 'RdBu',
           template ='plotly_white')
    fig.data[0].texttemplate = "<b>%{label}</b><br>Qt. Culinárias: %{value}<br>"
    
    return fig
    
# ==============================
# Sidebar 
# ==============================
st.sidebar.image('tomato.png', width=50)
st.sidebar.markdown('### :red[ZOMATO RESTAURANTS!]')
st.sidebar.markdown("""___""")

st.sidebar.markdown('#### Filtros')
paises = df['country_name'].unique()

# Filtros
paises = list (df['country_name'].unique())
country_opitions = st.sidebar.multiselect(
    'Escolha os países que deseja visualizar os restaurante:', paises, default=['Brazil', 'India', 'United States of America', 'England', 'South Africa'])

linhas = df['country_name'].isin(country_opitions)
df = df.loc[linhas, :]

st.sidebar.markdown("""___""")

st.sidebar.markdown ('###### Powered by Comunidade DS')
st.sidebar.markdown ('###### Data Analyst: Lui Magno')  

# ==============================
# Visão Países
# ==============================
st.header('🌎 :red[Visão Países]')


with st.container():
    # Restaurantes por país
    df_aux = (df.loc[:, ['country_name', 'restaurant_id']].groupby('country_name')
                                                         .nunique()
                                                         .sort_values(by='restaurant_id',ascending = False )
                                                         .reset_index())
    df_aux.columns = ['País', 'Num. Restaurantes']
    df_aux_mundi = df_aux.copy()
    fig = bar_chart(df_aux, 'País', 'Num. Restaurantes', 'País', 'Quantidade de Restaurantes registrados por país', True)
    st.plotly_chart(fig, use_container_width = True, theme='streamlit')
    
with st.container():
    # Cidade por país
    df_aux = (df.loc[:, ['country_name', 'city']].groupby('country_name')
                                                .nunique()
                                                .sort_values(by='city',ascending = False)
                                                .reset_index())
    df_aux.columns = ['País', 'Num. Cidades']
    
    fig = bar_chart(df_aux, 'País', 'Num. Cidades', 'País', 'Quantidade de Cidades registradas por país', True)
    st.plotly_chart(fig, use_container_width = True, theme='streamlit')
    
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        # Média de avaliações feitas por país
        df_aux = (df.loc[:, ['country_name', 'votes']].groupby('country_name')
                                                     .sum()
                                                     .sort_values(by='votes', ascending = False)
                                                     .reset_index())
        df_aux.columns = ['Países', 'Quantidade de Avaliações']
        df_aux = df_aux.head(7)
        fig = bar_chart(df_aux, 'Países', 'Quantidade de Avaliações', 'Países', 'Quantidade de avaliações por país', False)
        st.plotly_chart(fig, use_container_width = True, theme='streamlit')
        
    with col2:
        # Média de preço de prato por duas pessoas por país
        df_aux = (df.loc[:, ['country_name', 'average_cost_for_two']].groupby('country_name')
                                                                    .mean()
                                                                    .sort_values(by='average_cost_for_two', ascending = False)
                                                                    .reset_index())
        df_aux.columns = ['Países', 'Prato para 2 pessoas']
        df_aux = df_aux.head(7)
        
        fig = bar_chart(df_aux, 'Países', 'Prato para 2 pessoas', 'Países', 'Média de preço de prato para duas pessoas por país', True)
        st.plotly_chart(fig, use_container_width = True, theme='streamlit')
        

with st.container():
    # Coluna Experimental - Treemapgraph
    st.markdown('#### Diversidade Gastronômica: ')
    st.markdown('###### Quantidade de culinárias únicas por país - Treemap Graph')

    contagem = df_root[['country_name','cuisines']].groupby('country_name').nunique().sort_values('cuisines', ascending = False).reset_index()
    contagem.columns=['País','Culinárias']

    fig = treemap_graph(contagem, path='País', value='Culinárias', color='Culinárias')
    st.plotly_chart(fig, use_container_width = True, theme='streamlit')
    
    

with st.container():
    fig = px.scatter_geo(df_aux_mundi, locations="País", color="País", hover_name="País", size="Num. Restaurantes", projection="natural earth")
    
    
    
    df = px.data.gapminder()
    fig = px.scatter_geo(df, locations="iso_alpha", color="continent", hover_name="country", size="pop",
               animation_frame="year", projection="natural earth")
    st.plotly_chart(fig, use_container_width = True, theme='streamlit')