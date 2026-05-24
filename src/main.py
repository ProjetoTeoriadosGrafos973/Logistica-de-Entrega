import streamlit as st
import folium                              
from streamlit_folium import st_folium
import pandas as pd
from ios.api_osrm import buscar_rota_osrm
from core.graph import Grafo
from algorithms.algoritmoDijkstra import dijkstra, reconstruir_caminho
from ios.file_reader import FileReader

st.set_page_config(page_title="Logística de Entregas", layout="wide")
st.title("Sistema de Logística de Entregas")

@st.cache_resource
def carregar_sistema():
    grafo  = Grafo()
    reader = FileReader("data")
    nomes  = reader.carregar_cidades(grafo) 
    reader.carregar_rotas(grafo)
    return grafo, nomes, reader

grafo, nomes, reader = carregar_sistema()

@st.cache_data
def carregar_coords():
    df = pd.read_csv("data/cidades.csv")
    return {row["id"]: (row["lat"], row["lon"]) for _, row in df.iterrows()}
                                           
coords = carregar_coords()

with st.sidebar:
    st.header("Rede cadastrada")
    st.subheader("Cidades")
    st.dataframe(pd.read_csv("data/cidades.csv"), hide_index=True, use_container_width=True)
    st.subheader("Rotas")
    st.dataframe(pd.read_csv("data/rotas.csv"), hide_index=True, use_container_width=True)

col1, col2 = st.columns(2)

ids    = list(nomes.keys())
opcoes = [f"{id_} — {nome}" for id_, nome in nomes.items()]

with col1:
    st.subheader("Calcular rota")
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
                st.success("Rota encontrada!")
                st.session_state["caminho"] = caminho
                st.session_state["dist_grafo"] = dist[destino_id]
                pontos = [coords[id_] for id_ in caminho]

                with st.spinner('Buscando rota por estradas...'):
                    rota_osrm = buscar_rota_osrm(pontos)
                st.session_state["osrm"] = rota_osrm
with col2:
    st.subheader("Mapa da rota")            
    caminho_atual = st.session_state.get("caminho")
    osrm = st.session_state.get("osrm")

    if caminho_atual:
        nomes_rota = [nomes.get(c, c) for c in caminho_atual]
        m1, m2, m3 = st.columns(3)
        m1.metric("Distância (grafo)", f"{st.session_state.get('dist_grafo', "-")} km")
        m2.metric("Distância real", f"{osrm['distancia']} km" if osrm else "-")
        if osrm:
            h = int(osrm["duracao"] // 60)
            m = int(osrm["duracao"] % 60)
            tempo = f"{h}h {m:02d}min" if h > 0 else f"{m} min"
        else:
            tempo = "-"
        m3.metric("Tempo estimado", tempo)
        st.markdown("**Rota:** " + "→ ".join(f"`{n}`" for n in nomes_rota))

    mapa = folium.Map(location=[-15,-50], zoom_start=5, tiles="CartoDB positron")
    if caminho_atual:
        for i, id_ in enumerate(caminho_atual):
            lat, lon = coords[id_]
            cor = "green" if i==0 else "red" if i==len(caminho_atual)-1 else "orange"
            folium.Marker([lat,lon], tooltip=nomes.get(id_, id_), icon=folium.Icon(color=cor)).add_to(mapa)

        pontos = [coords[id_] for id_ in caminho_atual]


        if osrm:
            h = int(osrm["duracao"] // 60)
            m = int(osrm["duracao"] % 60)
            folium.PolyLine(
                osrm["geometry"], color="#262424", weight=4, tooltip=f"{osrm['distancia']} km | {h}h {m:02d}min").add_to(mapa)
            mapa.fit_bounds(osrm["geometry"])
        else:
            folium.PolyLine(pontos, color="#95A5A6", weight=3, dash_array="8", tooltip="Linha reta - OSRM indisponível").add_to(mapa)
            mapa.fit_bounds(pontos)
    st_folium(mapa, use_container_width=True, height=420)
    osrm = st.session_state.get("osrm")
    if osrm and osrm.get("rodovias"):
        st.subheader(" Rodovias utilizadas")
        st.markdown(" · ".join(f"`{r}`" for r in osrm["rodovias"]))
    
    
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

st.divider()
st.subheader("Importar entregas do CSV")
arquivo = st.file_uploader("Envie entregas.csv", type="csv")

if arquivo:
    df = pd.read_csv(arquivo)
    st.dataframe(df, hide_index=True)

    if st.button("Processar entregas", type="primary"):
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
        if resultados:
            st.dataframe(
                pd.DataFrame(resultados),
                hide_index=True,
                use_container_width=True
            )
            st.success(f"{len(resultados)} entrega(s) processada(s)!")

if __name__ == "__main__":
    sistema = SistemaLogistica()
    sistema.processar_entregas()
    for e in sistema.entregas:
        nomes = [sistema.nomes.get(c, c) for c in e["caminho"]]
        print(f"#{e['id']} | {' → '.join(nomes)} | {e['distancia_total']} km")

