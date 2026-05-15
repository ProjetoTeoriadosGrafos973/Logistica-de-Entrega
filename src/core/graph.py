from core.edge import Edge

class Grafo:
    def __init__(self):
        self.adjacencia: dict[str, list[Edge]] = {}

    def adicionar_no(self, no: str):
        if no not in self.adjacencia:
            self.adjacencia[no] = []

    def adicionar_aresta(self, origem: str, destino: str, peso: int):
        self.adicionar_no(origem)
        self.adicionar_no(destino)
        self.adjacencia[origem].append(Edge(origem, destino, peso))
        self.adjacencia[destino].append(Edge(destino, origem, peso))

    def nos(self) -> list[str]:
        return list(self.adjacencia.keys())