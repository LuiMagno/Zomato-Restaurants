# ==============================
# Bibliotecas
# ==============================
import pandas as pd
import streamlit as st
from PIL import Image
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

# ==============================
# Configs
# ==============================
st.set_page_config(
    page_title='Home',
    page_icon='🎯',
    layout='wide'
)
# Importando Dataset
df_root = pd.read_csv('dataset/clean_zomato.csv')

# Fazendo cópia do dataframe lido
df = df_root.copy()
df.head()
print(df.head())


# ==============================
# Sidebar 
# ==============================
st.sidebar.image('comunidade.png', width=50)
st.sidebar.markdown('### Fome Zero')
st.sidebar.markdown("""___""")

st.sidebar.markdown('# Filtros')
paises = df['country_name'].unique()

# Filtros
paises = list (df['country_name'].unique())
country_opitions = st.sidebar.multiselect(
    'Escolha os países que deseja visualizar os restaurantes:', paises, default = paises)

linhas = df['country_name'].isin(country_opitions)
df = df.loc[linhas, :]

st.sidebar.markdown ('###### Powered by Comunidade DS')
st.sidebar.markdown ('###### Data Analyst: Lui Magno') 

# ==============================
# Visão Geral
# ==============================
st.header('Fome Zero!')
st.subheader('O Melhor lugar para encontrar seu mais novo restaurante favorito!')

st.subheader('Temos as seguintes marcas dentro da nossa plataforma:')

# Linha 1 -  informações gerais
with st.container():
        df_aux = df_root.copy()
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            # Quantos restaurantes únicos estão registrados
            restaurantes_unicos = df_aux['restaurant_id'].nunique()
            col1.metric(label='Restaurantes Cadastrados', value=restaurantes_unicos)
        with col2:
            paises_unicos = df_aux['country_name'].nunique()
            col2.metric(label='Países Cadastrados', value=paises_unicos)
        with col3:
            cidades_unicas = df_aux['city'].nunique()
            col3.metric('Cidades Cadastradas', cidades_unicas)
        with col4:
            soma_avaliacoes = df_aux['votes'].sum()
            col4.metric(label='Avaliações feitas na plataforma', value=soma_avaliacoes)
        with col5:
            tipos_culinaria = df_aux['cuisines'].nunique()
            col5.metric(label='Tipos de Culinárias Oferecidas', value=tipos_culinaria)

# Linha 2 - Mapa Mundi 
with st.container():
    datamap = df[['restaurant_name', 'longitude', 'latitude', 'cuisines', 'average_cost_for_two', 'currency', 'aggregate_rating', 'rating_color']].reset_index(drop = True)
    
    # Criando mapa com folium
    map = folium.Map(zoom_start = 20)
    cluster = MarkerCluster().add_to(map)
    
    icon = 'fa-cutlery'
    
    for index, location_info in datamap.iterrows():
        folium.Marker([location_info['latitude'],       
                       location_info['longitude']],
                       icon = folium.Icon(color=location_info['rating_color'], icon=icon, prefix='fa'),
                       popup = folium.Popup(f"""<h6> <b> {location_info['restaurant_name']} </b> </h6> <br>
                                            Cozinha: {location_info['cuisines']} <br>
                                            Preço médio para dois: {location_info['average_cost_for_two']} ({location_info['currency']}) <br>
                                            Avaliação: {location_info['aggregate_rating']} / 5.0 <br> """,
                                            max_width= len(f"{location_info['restaurant_name']}")*20)).add_to(cluster)

    # Exibindo o mapa
    folium_static(map, width = 1024, height = 600)  
# ---------------------------------------------------------------------
