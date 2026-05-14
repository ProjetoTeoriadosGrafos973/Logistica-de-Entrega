import streamlit as st
import pandas as pd
from core.graph import Grafo
from algorithms.algoritmoDijkstra import dijkstra, reconstruir_caminho
from ios.file_reader import FileReader

st.set_page_config(page_title="Logística de Entregas", page_icon="📦", layout="wide")
st.title("📦 Sistema de Logística de Entregas")

@st.cache_resource
def carregar_sistema():
    grafo  = Grafo()
    reader = FileReader("data")
    nomes  = reader.carregar_cidades(grafo)
    reader.carregar_rotas(grafo)
    return grafo, nomes, reader

grafo, nomes, reader = carregar_sistema()

# Sidebar
with st.sidebar:
    st.header("🗺️ Rede cadastrada")
    st.subheader("Cidades")
    st.dataframe(pd.read_csv("data/cidades.csv"), hide_index=True, use_container_width=True)
    st.subheader("Rotas")
    st.dataframe(pd.read_csv("data/rotas.csv"), hide_index=True, use_container_width=True)

# Conteúdo principal
col1, col2 = st.columns(2)

ids    = list(nomes.keys())
opcoes = [f"{id_} — {nome}" for id_, nome in nomes.items()]

with col1:
    st.subheader("🔍 Calcular rota")
    origem_sel  = st.selectbox("Origem",  opcoes, index=0)
    destino_sel = st.selectbox("Destino", opcoes, index=len(opcoes)-1)

    if st.button("Calcular", type="primary", use_container_width=True):
        origem_id  = origem_sel.split(" — ")[0]
        destino_id = destino_sel.split(" — ")[0]

        if origem_id == destino_id:
            st.warning("Origem e destino iguais.")
        else:
            dist, prev = dijkstra(grafo, origem_id)
            caminho    = reconstruir_caminho(prev, origem_id, destino_id)

            if not caminho:
                st.error("Sem rota disponível.")
            else:
                nomes_caminho = [nomes.get(c, c) for c in caminho]
                st.success("Rota encontrada!")
                m1, m2 = st.columns(2)
                m1.metric("Distância", f"{dist[destino_id]} km")
                m2.metric("Paradas",   len(caminho) - 2)
                st.markdown("**Rota:** " + " → ".join(f"`{n}`" for n in nomes_caminho))

with col2:
    st.subheader("📂 Importar entregas")
    arquivo = st.file_uploader("Envie entregas.csv", type="csv")
    if arquivo:
        df = pd.read_csv(arquivo)
        st.dataframe(df, hide_index=True)
        if st.button("Processar", type="primary"):
            resultados = []
            for _, linha in df.iterrows():
                dist, prev = dijkstra(grafo, linha["origem"])
                caminho    = reconstruir_caminho(prev, linha["origem"], linha["destino"])
                if caminho:
                    nomes_c = [nomes.get(c, c) for c in caminho]
                    resultados.append({
                        "Pacote":    linha["pacote_id"],
                        "Rota":      " → ".join(nomes_c),
                        "Distância": f"{dist[linha['destino']]} km",
                        "Paradas":   len(caminho) - 2,
                    })
            st.dataframe(pd.DataFrame(resultados), hide_index=True, use_container_width=True)

class SistemaLogistica:
    def __init__(self, pasta_data: str = "data"):
        self.grafo    = Grafo()
        self.reader   = FileReader(pasta_data)
        self.nomes    = self.reader.carregar_cidades(self.grafo)
        self.reader.carregar_rotas(self.grafo)
        self.entregas = []

    def calcular_rota(self, origem: str, destino: str) -> dict | None:
        dist, prev = dijkstra(self.grafo, origem)
        caminho    = reconstruir_caminho(prev, origem, destino)
        if not caminho:
            return None
        return {"caminho": caminho, "distancia_total": dist[destino], "paradas": len(caminho) - 2}

    def processar_entregas(self, arquivo: str = "entregas.csv"):
        for linha in self.reader.carregar_entregas(arquivo):
            resultado = self.calcular_rota(linha["origem"], linha["destino"])
            if resultado:
                self.entregas.append({"id": linha["pacote_id"], **resultado})

if __name__ == "__main__":
    sistema = SistemaLogistica()
    sistema.processar_entregas()
    for e in sistema.entregas:
        nomes = [sistema.nomes.get(c, c) for c in e["caminho"]]
        print(f"#{e['id']} | {' → '.join(nomes)} | {e['distancia_total']} km")