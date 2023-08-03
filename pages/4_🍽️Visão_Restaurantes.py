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
    page_title='Visão Restaurantes',
    page_icon=':knife_fork_plate:',
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
    if color:
        plt.figure(figsize = (20,15))
        fig = px.bar(data, x = x, y = y, color=color, text_auto=textauto, title = title, template='simple_white')
        return fig
    else:
        plt.figure(figsize = (20,15))
        fig = px.bar(data, x = x, y = y, text_auto=textauto, title = title, template='simple_white')
        return fig
    
def melhor_restaurante(tipo):  
    linhas_selecionadas = (df['cuisines'] == tipo)
    df_aux01 = (df.loc[linhas_selecionadas, ['restaurant_id', 'aggregate_rating', 'restaurant_name']].groupby(['restaurant_id', 'restaurant_name'])
                                                                                                   .mean()
                                                                                                   .sort_values(by='aggregate_rating')
                                                                                                   .reset_index())
    maior_nota = df_aux01['aggregate_rating'].max()
    print(maior_nota)
    # Selecionando os que tem nota igual a maior
    linhas_selecionadas = (df_aux01['aggregate_rating'] == maior_nota)

    # Ordenando por ID
    df_aux01 = df_aux01.loc[linhas_selecionadas, :].sort_values(by='restaurant_id')

    return df_aux01    
# ==============================
# Sidebar 
# ==============================
st.sidebar.image('comunidade.png', width=50)
st.sidebar.markdown('### Fome Zero')
st.sidebar.markdown("""___""")

st.sidebar.markdown('#### Filtros')
paises = df['country_name'].unique()

# Filtros
# Países
paises = list (df['country_name'].unique())
country_opitions = st.sidebar.multiselect(
    'Escolha os países que deseja visualizar os restaurantes:', paises, default = paises)

linhas = df['country_name'].isin(country_opitions)
df = df.loc[linhas, :]

# Número de restaurantes - Slider
num_slider = st.sidebar.slider('Selecione a quantidade de Restaurantes que deseja visualizar', value=10,
                 min_value=0,
                 max_value=50)


# Tipos de culinária
culinarias = list (df['cuisines'].unique())
culinarias_options = st.sidebar.multiselect(
    'Escolha os tipos de culinária que deseja visualizar:', culinarias, default = ['Home-made', 'BBQ', 'Japanese', 'Brazilian', 'Arabian', 'American'])

linhas = df['cuisines'].isin(culinarias_options)
df_culinaria = df.loc[linhas, :]
st.sidebar.markdown("""___""")

st.sidebar.markdown('#### Feito por Lui Magno') 

# ==============================
# Visão Restaurantes
# ==============================
st.header(':knife_fork_plate: Visão Tipos de Culinárias')
st.subheader('Melhores restaurantes dos principais tipos culinários.')


with st.container():
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        # Selecionando restaurantes com a cozinha 'Italian'
        df_aux = melhor_restaurante('Italian')
        st.metric(label='Italiana: ' + str(df_aux.iloc[0, 1]), value=df_aux.iloc[0, 2])
    
    with col2:
        # Selecionando restaurantes com a cozinha 'Brazilian'
        df_aux = melhor_restaurante('Brazilian')
        st.metric(label='Brasileira: ' + str(df_aux.iloc[0, 1]), value=df_aux.iloc[0, 2])
    
    with col3:
        # Selecionando restaurantes com a cozinha 'American'
        df_aux = melhor_restaurante('American')
        st.metric(label='Americana: ' + str(df_aux.iloc[0, 1]), value=df_aux.iloc[0, 2])
        
    with col4:
        # Selecionando restaurantes com a cozinha 'Japanese'
        df_aux = melhor_restaurante('Japanese')
        st.metric(label='Japonesa: ' + str(df_aux.iloc[0, 1]), value=df_aux.iloc[0, 2])
        
    with col5:
        # Selecionando restaurantes com a cozinha 'Indian'
        df_aux = melhor_restaurante('Indian')
        st.metric(label='Indiana: ' + str(df_aux.iloc[0, 1])  , value=df_aux.iloc[0, 2])

with st.container():
    st.header('Top '+ str(num_slider) +  ' restaurantes')
    
    df_culinaria = df_culinaria.sort_values(['aggregate_rating', 'restaurant_id'], ascending = False).head(num_slider)
    
    df_culinaria = df_culinaria.drop(['address', 'locality', 'longitude', 'latitude', 'currency', 'has_table_booking', 'has_online_delivery', 'is_delivering_now', 'price_range', 'rating_color', 'rating_text'], axis=1)
    
    st.dataframe(df_culinaria, use_container_width= True)
    

with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        # Top 10 melhores tipos de culinárias
        df_aux = df.loc[:, ['cuisines', 'aggregate_rating']].groupby('cuisines').mean().sort_values('aggregate_rating', ascending = False).reset_index().head(num_slider)
        
        df_aux.columns = ['Culinárias', 'Nota']
        
        fig = bar_chart(df_aux, 'Culinárias','Nota','','Top '+ str(num_slider) +  ' melhores tipos de culinária', True)
        st.plotly_chart(fig, use_container_width = True, theme='streamlit')
        
    with col2:
        # Top 10 piores tipos de culinárias
        df_aux = df.loc[:, ['cuisines', 'aggregate_rating']].groupby('cuisines').mean().sort_values('aggregate_rating', ascending = True).reset_index().head(num_slider)
        
        df_aux.columns = ['Culinárias', 'Nota']
        
        fig = bar_chart(df_aux, 'Culinárias','Nota','','Top '+ str(num_slider) +  ' piores tipos de culinária', True)
        st.plotly_chart(fig, use_container_width = True, theme='streamlit')
        
    