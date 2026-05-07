import csv
from core.graph import Grafo

COLUNAS_PESO = ["peso", "distancia_km", "distancia", "km", "custo"]

class FileReader:
    def __init__(self, pasta_data: str = "data"):
        # pasta_data aponta para a pasta data/ do projeto
        self.pasta = pasta_data

    def _caminho(self, arquivo: str) -> str:
        return f"{self.pasta}/{arquivo}"

    def carregar_cidades(self, grafo: Grafo) -> dict[str, str]:
        nomes = {}
        with open(self._caminho("cidades.csv"), "r", encoding="utf-8") as f:
            for linha in csv.DictReader(f):
                grafo.adicionar_no(linha["id"])
                nomes[linha["id"]] = linha["nome"]
        return nomes

    def carregar_rotas(self, grafo: Grafo):
        with open(self._caminho("rotas.csv"), "r", encoding="utf-8") as f:
            leitor = csv.DictReader(f)
            # detecta automaticamente o nome da coluna de peso
            coluna = next((c for c in COLUNAS_PESO if c in leitor.fieldnames), None)
            if not coluna:
                raise ValueError(f"Coluna de peso não encontrada. Disponíveis: {leitor.fieldnames}")
            for linha in leitor:
                grafo.adicionar_aresta(linha["origem"], linha["destino"], int(linha[coluna]))

    def carregar_entregas(self, arquivo: str = "entregas.csv") -> list[dict]:
        with open(self._caminho(arquivo), "r", encoding="utf-8") as f:
            return list(csv.DictReader(f))