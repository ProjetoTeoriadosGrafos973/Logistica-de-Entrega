import pytest
from src.core.graph           import Grafo
from src.algorithms.algoritmo import dijkstra, reconstruir_caminho

@pytest.fixture
def grafo_simples():
    g = Grafo()
    g.adicionar_aresta("A", "B", 10)
    g.adicionar_aresta("B", "C", 5)
    g.adicionar_aresta("A", "C", 20)  # rota direta mais longa
    return g

def test_dijkstra_caminho_mais_curto(grafo_simples):
    dist, prev = dijkstra(grafo_simples, "A")
    # A→B→C = 15, mais curto que A→C = 20
    assert dist["C"] == 15

def test_reconstruir_caminho(grafo_simples):
    _, prev = dijkstra(grafo_simples, "A")
    caminho = reconstruir_caminho(prev, "A", "C")
    assert caminho == ["A", "B", "C"]