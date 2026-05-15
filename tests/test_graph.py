import pytest
from src.core.graph import Grafo

def test_adicionar_no():
    g = Grafo()
    g.adicionar_no("SP")
    assert "SP" in g.adjacencia

def test_aresta_bidirecional():
    g = Grafo()
    g.adicionar_aresta("SP", "RJ", 440)
    print("Arestas:",any(e.destino == "SP" for e in g.adjacencia["RJ"]) )
    assert any(e.destino == "RJ" for e in g.adjacencia["SP"])
    assert any(e.destino == "SP" for e in g.adjacencia["RJ"])