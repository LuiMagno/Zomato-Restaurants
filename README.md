# Zomato Restaurants
A Análise da API Zomato é uma das mais úteis para os amantes da comida que desejam experimentar as melhores cozinhas de todas as partes do mundo que se encaixem no seu orçamento. Nesta análise avançada, vamos tratar dos dados da Zomato em várias frentes para que se entenda de forma detalhada como vários restaurantes se comportam nas mais diversas métricas, como qualidade, confiabilidade e etc.

# Business Problems
O novo CEO da empresa foi recentemente contratado e busca obter uma compreensão mais profunda do negócio para tomar decisões estratégicas acertadas e ampliar ainda mais os esforços em prol do sucesso do programa. Para atingir esse objetivo, é necessário realizar uma análise abrangente dos dados da empresa e criar painéis de controle que reflitam essas análises. Isso permitirá mapear a base de restaurantes cadastrados e obter uma visão clara sobre o desenvolvimento do negócio, utilizando as informações a seguir:
 
:mag_right: **Visão Geral**
1. Número de Restaurantes registrados e a localização deles
2. Número de países e cidades cadastradas
3. Número de avaliações feitas na plataforma
4. Número de tipos de culinárias
5. Mapa Múndi interativo:
     Nome do Restaurante,
     Valor médio de prato para 2 pessoas,
     Nota média de avaliação.

:earth_americas: **Visão Países**
1. Quantidade de Restaurantes registrados por país
2. Quantidade de Cidades registradas por país
3. Quantidade de Avaliações por país
4. Média de preço de prato para 2 pessoas por país

:convenience_store: **Visão Cidades**
1. Cidade de cada país com mais restaurantes cadastrados
2. Top 10 cidades com restaurantes com média de avaliação maior que 4
3. Top 10 cidades com restaurantes com média de avaliação menor que 2.5
4. Top 10 cidades com mais restaurantes com tipos de culinária distintos

🍽️ **Visão Culinária**
1. Melhores restaurantes dos principais tipos culinários
2. Top X restaurantes (filtros interativos de número e tipos de culinárias)
3. Top 10 melhores e Top 10 piores tipos de culinária

O desafio consiste em responder a essas perguntas e transformar seus resultados em painéis de controle que possibilitem uma compreensão rápida do progresso do negócio. Os dados da empresa podem ser obtidos a partir do link do Kaggle abaixo (arquivo zomato.csv): https://www.kaggle.com/datasets/akashram/zomato-restaurants-autoupdated-dataset?resource=download&select=zomato.csv

# Premissas assumidas para análise dos dados
1. O modelo de negócios assumido é um Marketplace;
2. O banco de dados não contém informações de data, portanto, as análises não incluem a dimensão temporal;
3. As perspectivas analíticas adotadas foram: país, cidade e gastronomia.

# Estratégias de Solução
As análises foram iniciadas a partir da resolução das perguntas propostas pelo CEO, segmentadas pelas visões de país, cidade e gastronomia;
Em termos de ferramentas, as seguintes foram utilizadas:
1. Jupyter Notebook - Análise preliminar e rascunho do script final;
2. Bibliotecas de manipulação de dados - Pandas e Numpy;
3. Bibliotecas de visualização de dados - Matplotlib, Plotly, Folium;
4. Jupyter Lab - Script Python definitivo;
5. Streamlit e Streamlit Cloud - Visualização do painel de controle e sua produção.

# Principais Insight de Dados
1. A Índia possui, muito provavelmente por causa da população, a maior quantidade de restaurantes cadastrados, assim dominando a quantidade de restaurantes com maior e menor nota.
2. O Brasil, mesmo tendo bem menos restaurantes que a Índia e os EUA, se destaca pela má avaliação de muitos dos seus restaurantes.
3. Os restaurantes que se classificam como comida do tipo 'Japonesa' são os mais bem avaliados, representando perto de 1/4 das melhores culinárias.

# Conclusão
O propósito do projeto era desenvolver uma representação visual dos dados que possibilitasse o acompanhamento das características centrais do negócio e sua distribuição geográfica.

A plataforma Zomato Restaurants tem uma presença global marcante, com uma forte influência na Ásia e América do Norte. Ela oferece uma grande diversidade gastronômica, sendo que os pratos do Norte da Índia são a espinha dorsal de seu cardápio.

# Próximos Passos
1. Melhorar a visualização de resultados, ampliando o leque de ferramentas que as bibliotecas de gráficos fornecem;
2. Melhorar a formatação de dados para que avaliações e comparações entre restaurantes e países seja mais justa e precisa
3. Analise os possíveis custos e vantagens de ampliar ou reduzir a diversidade gastronômica, levando em consideração os preços dos pratos e as avaliações dos restaurantes.

# Chegue o Resultado do projeto abaixo:
https://ftc-zomato-restaurants-luimagno-r3bejr9w2wbdge5azysb3g.streamlit.app
