# Logística de Entregas

O Sistema de Logística de Entregas é uma aplicação web desenvolvida em Python com Streamlit, voltada para pequenas e médias empresas que precisam otimizar rotas de distribuição. A solução modela a rede de entregas com grafo ponderado e aplica o algoritmo de Dijkstra para encontrar o caminho de menor custo entre dois pontos
Nosso projeto tem como objetivo
Para rodar o projeto, é necessário segui o passo a passo: 

# fazer um clone do repositório

git clone https://github.com/ProjetoTeoriadosGrafos973/Logistica-de-Entrega.git

# instalar dependências

pip install -r requirements.txt

# rodar a interface web

cd Logística-de-Entrega

streamlit run src/main.py

# rodar os testes

pytest tests/
