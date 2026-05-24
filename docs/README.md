# Logística de Entregas


## O Porque do Projeto
Muitas empresa e microempreendedores enfrentam dificuldades ao lidar com a falta de otimização de rotas, gerando um aumento nos custos operacionais, baixa eficiência, sobrecarga de mão de obra e possíveis atrasos em entregas.
Nesse contexto, o Sistema de Logística de Entregas é uma aplicação web desenvolvida em Python, que foi desenvolvida inicialmente para simular e otimizar rotas de distribuição entre centros urbanos e pontos de coleta.

O projeto foi inspirado no modelo logístico da Shopee, especialmente no uso de pontos de entrega como os Shopee Xpress, que conectam vendedores, centros de distribuição e consumidores finais. Esse tipo de estrutura é essencial para empresas de e-commerce em larga escala, pois permite descentralizar entregas e reduzir o tempo de transporte.

A aplicação busca representar esse cenário ao calcular automaticamente as melhores rotas entre o centro de distribuição e os pontos de entrega, ou entre os próprios pontos, utilizando algoritmos de grafos como o Dijkstra para encontrar o menor caminho em termos de distância.
Dessa forma, o sistema simula como grandes plataformas como a Shopee conseguem melhorar eficiência logística, reduzir custos e aumentar a velocidade de entrega por meio da otimização de rotas.

Este projeto nasceu para resolver essa dor através de:
* **Automação do cálculo de rotas usando teoria dos grafos**
* **Redução do trabalho manual de planejamento de semanas para segundos**
* **Interface focada na experiência do usuário para operação rápida**

A solução modela a rede de entregas com grafo ponderado e aplica o algoritmo de Dijkstra para encontrar o caminho de menor custo entre dois pontos. 

## Tecnologias Utilizadas

O sistema do projeto foi desenvolvido com as seguintes funcionalidade:

* **Python**: Utilizado no backend e também no frontend através de suas bibliotecas
* **Bibliotecas**:

    * **Streamlit**: Framework para criação da interface web em Python
    * **Pandas**: Leitura, manipulaçao e exibição de dados CSV em tabelas
    * **Folium**: Geração de mapas interativos baseados em Leaflet.js
    * **Streamlit-folium**: Integração do mapa Folium dentro da interface Streamlit
    * **Requests**: Requisições HTTP para  a Api OSRM
    * **Heapq**: Fila de prioridade (min-heap) usada internamente pelo Dijkstra
    * **CSV**: Leitura de arquivos CSV
    * **Pytest**: Framework de testes unitários

* **APIs**:
    * **OSRM**: Motor de roteamento open source usado para calcular rotas em mapas reais com alta performance.


---
## Para rodar o projeto, é necessário segui o passo a passo:

### Clonar o repositório

* git clone https://github.com/ProjetoTeoriadosGrafos973/Logistica-de-Entrega.git

### Instalar as dependências

* pip install -r requirements.txt

### Rodar a interface web

* cd Logística-de-Entrega

* streamlit run src/main.py

### Para rodar os testes

python -m pytest tests/test_algorithms.py

python -m pytest tests/test_graph.py


---
## Demonstração Visual

### Tela Inicial
> Essa é a tela principal do sistema, onde o usuário pode visualizar á esquerda, as Redes cadastradas, compostos pelos Pontos de Entregas Xpress da Shopee e suas cidades, além de rotas pré inseridas no sistema. Ao centro da tela se encontra os botões para selecionar a origem e o destino, além do mapa á direita.

![Dashboard do Sistema](/docs/assets/tela_inicial.png)


### Fluxo Principal
> Essa é a tela após o sistema calcular a melhor rota para aquele destino. O mapa mostra o caminho que poderá ser percorrido, indicando as rotas e rodovias, a distância em quilômetros e o tempo estimado em horas para a rota. No mapa, é possível identificar as vértices e as arestas por cores, sendo elas:
>- Vértices:
>   - Origem: cor verde 
>   - Destino: cor vermelha 
>   - Paradas: cor laranja 
>- Arestas:
>   - Rotas: cor preta 

![Dashboard do Sistema](/docs/assets/rota.png)


### Seção de Entregas
> Ao fim da tela, há uma seção dedicada à importação de arquivos CSV, para processar entregas a serem feitas.
> Essa parte é ideal para que o sistema salve essas entregas, e os usuários insira diversas rotas de forma prática.
>
>Os dados importados são utilizados para processamento e exibição das rotas otimizadas dentro da aplicação. No entanto, o sistema é uma parte escalável, perimitindo futuras melhorias, como a possibilidade de envio automático das informações de entrega por e-mail ou integração com APIs de gestão logística.

![Dashboard do Sistema](/docs/assets/entregas.png)

## Uso de Inteligência Artificial

O projeto não foi desenvolvido 100% com a IA, mas usamos das ferramentas de chats (chatGPT e Claude AI), para nos ajudarmos a superar alguns bugs do sistema e auxiliar na criação da interface visual da tela, além da chamada para a Api.