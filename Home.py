# ==============================
# Bibliotecas
# ==============================
import streamlit as st
from PIL import Image

# ==============================
# Configs
# ==============================
st.set_page_config(
    page_title="Home",
    page_icon="🎲",
    layout='wide'
) 
st.sidebar.image(Image.open('comunidade.png' ), width=120)

# ==============================
# Layout no Streamlit
# ==============================
st.header("Fome Zero: um projeto de análise de dados.")

st.markdown('Aqui você vai encontrar uma análise detalhada sobre os dados da companhia Fome Zero, que tem vários restaurantes pelo mundo, e junto com eles, muita informação.')

st.markdown(
    """
    Esse dashboard de crescimento foi feito com informações de vários restaurantes pelo mundo.
    ### Como utilizar este dashboard??
    - Os dados fornecidos apresentam diversas informações, com números focados em qualidade, localidade e disponibilidade.
    - Localidade: pontos geográficos localizados num mapa múndi, com repletas informações sobre cada estabelecimento.
    - Qualidade: filtros estão disponíveis para que se tenha uma experiência personalizada, dividindo por país e notas.
    - Disponibilidade: existem diversas infos sobre entregas online, reservas, notas e preços.
    - Os indicadores foram limpos e organizados para fornecer informações precisas e enxutas.
    ### Ask for Help
    - Comunidade DS
    - luimagno
""")