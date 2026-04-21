# E1 — Proposta e Definição do Projeto

> **Disciplina:** Teoria dos Grafos  
> **Prazo:** 19 de março de 2026  
> **Peso:** 10% da nota final  

---

## Identificação do Grupo

| Campo | Preenchimento |
|-------|---------------|
| Nome do projeto | Logística de Entregas|
| Integrante 1 | Maria Beatriz Santos Carvalho — 38778131 |
| Integrante 2 | Gabrielle dos Santos Carmo — 44124937 |
| Integrante 3 | Gabriel Santos da Silva — 42565561 |
| Domínio de aplicação | Logística de entregas |

---

## 1. Contexto e Motivação

> Descreva o problema do mundo real que será abordado. Por que ele é relevante?  
> *Orientação: 2 a 3 parágrafos. Seja específico — evite generalizações.*

Ao decorrer dos anos, as vantagens da tecnologia em diversas áreas organizacionais tornaram-se evidentes. Pensando nisso, analisamos as diversas ferramentas de logísticas empresariais, e como elas são integradas ao setor de entregas.

A ferramenta que mais se assemelha a ideia deste projeto é a ERP (Enterprise Resource Planning), que  pode ser integrada a vários setores da organização, e também no setor de logístico de entregas, ela é responsável por medir os fluxos de entrega, emitir Notas Fiscais e rastrear os transportes de entregas, além dos usos dos algoritmos Dijkstra para calcular o menor caminho e do “Graph Neural Networks” para previsionar o tempo de chegada. Assim, foi viável se inspirar em uma ideia já consolidada no mercado para desenvolvermos uma ferramenta que seja acessível e com menor custo de execução.

Esse projeto discute a necessidade de inserir ferramentas tecnológicas, para a elaboração de rotas de distribuição mais eficientes e de maior custo benefício para as empresas. Através da utilização da Teoria dos Grafos, com a finalidade de diminuir a carga de trabalho manual, e potencializar os resultados que podem ser fornecidos através dos algoritmos. Os grafos utilizados nesse sistema são os Grafos Conectados e os Grafos Ponderados, eles vão auxiliar na interligação das rotas e definir os pesos de cada, e assim evitar desperdícios operacionais para a organização.

---

## 2. Objetivo Geral

> O que o sistema deve ser capaz de fazer ao final?  
> *Orientação: 1 frase clara e objetiva. Ex.: "O sistema deve calcular a rota de menor custo entre dois pontos em um mapa urbano."*

O sistema deve analisar as rotas de entrega utilizando grafos dirigidos e ponderados, além do algoritmo Dijkstra para encontrar caminhos mais rápidos e reduzir custos.

---

## 3. Objetivos Específicos

> Desmembre o objetivo geral em metas mensuráveis.  
> *Orientação: liste entre 3 e 5 itens. Cada item deve ser verificável — use verbos como "implementar", "calcular", "exibir", "carregar".*

- [Modelar a rede de entregas como um grafo dirigido e ponderado, com vértices representando o depósito e os clientes e arestas representando trechos viários com peso em distância (km).] 

- [Carregar o grafo a partir de um arquivo de entrada no formato CSV com colunas: origem, destino, peso.] 

- [Identificar através do algoritmo de Dijkstra a rota mais rápida ou mais curta entre um centro de distribuição e múltiplos clientes.] 

- [Calcular custos não apenas por distância, mas incorporando trânsito, pedágios, tipo de via e horários, atribuindo "pesos" a cada conexão.] 

- [Detectar nós críticos (pontos únicos de falha) onde atrasos podem paralisar a operação] 

---

## 4. Público-Alvo / Caso de Uso Principal

> Para quem ou em qual cenário o sistema seria utilizado?  
> *Orientação: descreva um cenário concreto de uso. Ex.: "Um entregador de aplicativo que precisa otimizar a sequência de entregas em um bairro."*

Pequenas e médias empresas, que estão começando a crescer no setor de entregas, que precisam de um aplicativo mais robusto para a otimização de suas rotas. Tendo assim um maior número de entregas por um menor custo.

---

## 5. Justificativa Técnica — Por que Grafos?

> Por que a modelagem em grafo é a abordagem mais adequada para este problema?  
> *Orientação: explique quais elementos do problema mapeiam naturalmente para vértices e arestas. Mencione se há pesos, direção, ou restrições que reforçam a escolha.*

A modelagem em grafos é a abordagem mais adequada, pois os centros de distribuições e clientes podem ser representados como os vértices e identificados como ids, as rotas como as arestas dirigidas, pensando em um ponto de partida até o trecho percorrido (u -> v), do que permite uma visualização mais clara de todas as conexões logísticas. O peso de cada aresta representa a distância em quilômetros entre dois pontos, além de especificar o cálculo de trânsitos quando houver, serão modelados com essa distância base: w(e) = distância_km × fator_trânsito, onde fator_trânsito ∈ [1,0 ; 2,5] é estimado por faixa horária." Esse modelo também pode considerar grafos dirigidos já que algumas rotas possuem restrições como sentido único da via e é possível incorporar restrições como horário de entrega etc. 


---

## 6. Tipo de Grafo

> Especifique as características do grafo que o problema requer.

| Característica | Escolha | Justificativa breve |
|----------------|---------|---------------------|
| Dirigido ou não-dirigido | DIRIGIDO | Dirigido, pois as rotas podem ter sentido único o que podem influenciar o trajeto. |
| Ponderado ou não-ponderado | PONDERADO |  Ponderado, pois cada conexão possui tempo, distância e custos e condições de locomoção.|
| Conectado / bipartido / geral | CONECTADO | Conectado, pois os pontos de entregas têm que estar interligados para garantir a realização das entregas. |
| Representação interna pretendida | lista de adjacência / matriz | LISTA DE ADJACÊNCIA |  Lista de adjacência, pois gera uma estrutura mais eficiente para representar os grafos com muitos vértices e arestas.|

---

## 7. Diagrama Conceitual

> Insira aqui ao menos uma figura que ilustre o domínio do problema.  
> *Pode ser uma imagem exportada do Draw.io, Excalidraw, foto de esboço à mão etc.*  


![Diagrama conceitual](image.png)

**Legenda:** 
    - Arestas:  Rotas ( Grafos Ponderado distância  entre cada par)
    - Peso arestas: distância em quilômetros
    - Vértices: Depósitos e clientes (cada número define a ordem de entrega)
---

## Checklist de Entrega

Antes de submeter, confirme:

- [X] Texto entre 300 e 600 palavras (seções 1 a 5)
- [X] Todos os campos da tabela de identificação preenchidos
- [x] Tipo de grafo especificado com justificativa
- [X] Diagrama presente e referenciado no texto
- [X] Arquivo nomeado como `E1_NomeGrupo_Grafos.docx` (versão Word) ou PR aberto (versão GitHub)

---

*Teoria dos Grafos — Profa. Dra. Andréa Ono Sakai*
