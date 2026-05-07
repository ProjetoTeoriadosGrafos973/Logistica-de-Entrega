class Edge:
    def __init__(self, origem: str, destino: str, peso: int):
        self.origem  = origem
        self.destino = destino
        self.peso    = peso

    def __repr__(self):
        return f"Edge({self.origem} → {self.destino}, {self.peso} km)"