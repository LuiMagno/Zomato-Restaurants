# ==============================
# Bibliotecas
# ==============================
import pandas as pd
import streamlit as st
from PIL import Image
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
import plotly.express       as px
import plotly.graph_objects as go
from matplotlib             import pyplot as plt
# ==============================
# Configs
# ==============================
st.set_page_config(
    page_title='Visão Cidades',
    page_icon=':cityscape:',
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

    
# ==============================
# Sidebar 
# ==============================
st.sidebar.image('comunidade.png', width=50)
st.sidebar.markdown('### Fome Zero')
st.sidebar.markdown("""___""")

st.sidebar.markdown('#### Filtros')
paises = df['country_name'].unique()

# Filtros
paises = list (df['country_name'].unique())
country_opitions = st.sidebar.multiselect(
    'Escolha os países que deseja visualizar os restaurantes:', paises, default = paises)

linhas = df['country_name'].isin(country_opitions)
df = df.loc[linhas, :]

st.sidebar.markdown("""___""")

st.sidebar.markdown('#### Feito por Lui Magno') 

# ==============================
# Visão Cidades
# ==============================

st.header('🏙️ Visão Cidades')

with st.container():
    # Top 10 cidades com mais restaurantes na base de dados
    df_aux = (df.loc[:, ['country_name','city', 'restaurant_id']].groupby(['country_name', 'city'])
                                                                .nunique()
                                                                .sort_values(by='restaurant_id', ascending = False)
                                                                .reset_index())

    paises = list (df['country_name'].unique())
    df_final = pd.DataFrame()
    
    for pais in paises:
        df_aux1 = df_aux.loc[df_aux['country_name'] == pais, :].head(1)
        df_final = pd.concat([df_final, df_aux1], ignore_index= True)
 
    df_final.columns = ['Pais', 'Cidade', 'Restaurantes']
    df_final = df_final.sort_values('Restaurantes', ascending=False).reset_index(drop= True)
    fig = bar_chart(df_final, 'Cidade', 'Restaurantes', 'Pais', 'Cidade de cada país com mais restaurantes cadastrados', True)
    st.plotly_chart(fig, use_container_width = True, theme='streamlit')
    
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        # Top 10 Cidades com Restaurantes com média de avaliação maior que 4
        df_aux = (df.loc[df['aggregate_rating'] > 4, ['country_name','city', 'restaurant_id']].groupby(['country_name', 'city'])
                                                                                              .nunique().sort_values(by='restaurant_id', ascending = False)
                                                                                              .reset_index()
                                                                                              .head(10))
        df_aux.columns = ['País', 'Cidade', 'Restaurantes']
        fig = bar_chart(df_aux, 'Cidade', 'Restaurantes', 'País', 'Top 10 Cidades com Restaurantes com média de avaliação maior que 4', True)
        st.plotly_chart(fig, use_container_width = True, theme='streamlit')
        
    with col2:
        # Top 10 Cidades com Restaurantes com média de avaliação menor que 2.5
        df_aux = (df.loc[df['aggregate_rating'] < 2.5, ['country_name','city', 'restaurant_id']].groupby(['country_name', 'city'])
                                                                                              .nunique().sort_values(by='restaurant_id', ascending = False)
                                                                                              .reset_index()
                                                                                              .head(10))
        df_aux.columns = ['País', 'Cidade', 'Restaurantes']
        fig = bar_chart(df_aux, 'Cidade', 'Restaurantes', 'País', 'Top 10 Cidades com Restaurantes com média de avaliação menor que 2.5', True)
        st.plotly_chart(fig, use_container_width = True, theme='streamlit')

with st.container():
    # Top 10 cidades com mais restaurantes com tipos de culinária distintos
    df_aux = (df.loc[:, ['country_name', 'city', 'cuisines']].groupby(['country_name','city'])
                                                            .nunique()
                                                            .sort_values(by='cuisines', ascending = False)
                                                            .reset_index()
                                                            .head(10))
    df_aux.columns = ['País', 'Cidade', 'Restaurantes']
    fig = bar_chart(df_aux, 'Cidade', 'Restaurantes', 'País', 'Top 10 cidades com mais restaurantes com tipos de culinária distintos', True)
    st.plotly_chart(fig, use_container_width = True, theme='streamlit')