
from algorithms.algoritmoDijkstra import dijkstra, reconstruir_caminho
from core.graph import Grafo
from ios.file_reader   import FileReader

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