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
    page_icon="🎲"
) 
st.sidebar.image(Image.open('tomato.png' ), width=120)

# ==============================
# Layout no Streamlit
# ==============================
st.header(":red[ZOMATO RESTAURANTS!]")
st.subheader(
    ':red[Um projeto de Análise de Dados.]', divider='red')

st.markdown('Aqui você vai encontrar uma análise detalhada sobre os dados da companhia Zomato Restaurants, que tem vários restaurantes pelo mundo, e junto com eles, muita informação.')

st.markdown(
    """
    Esse dashboard analítico foi feito com informações de vários restaurantes pelo mundo.
    ### Como utilizar este :red[**dashboard**]?
    - Os dados fornecidos apresentam diversas informações, com números focados em qualidade, localidade e disponibilidade.
        - Localidade: pontos geográficos localizados num mapa múndi, com repletas informações sobre cada estabelecimento.
        - Qualidade: filtros estão disponíveis para que se tenha uma experiência personalizada, dividindo por país e notas.
        - Disponibilidade: existem diversas infos sobre entregas online, reservas, notas e preços.
    - Os indicadores foram limpos e organizados para fornecer informações precisas e enxutas.
    - No menu ao lado esquerdo você pode navegar sobre todas as informações que foram estabelecidas depois do processo de :red[**Análise Descritiva e Estatística de Dados**].
    
    ### :red[Alguma dúvida? Fale comigo!]
    - LinkedIn: https://www.linkedin.com/in/lui-magno/
    - Github: https://github.com/LuiMagno
""")