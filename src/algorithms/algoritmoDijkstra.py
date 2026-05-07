import heapq
from core import edge


def dijkstra(grafo: Grafo, origem: str):
    # Inicialização
    distancias = {no: float('inf') for no in grafo.nos()}
    anteriores = {no: None for no in grafo.nos()}
    distancias[origem] = 0
    heap = [(0, origem)]

    while heap:
        distancia_atual, no_atual = heapq.heappop(heap)
        if distancia_atual > distancias[no_atual]:
            continue

        for aresta in grafo.adjacencia[no_atual]:
            nova_dist = distancias[no_atual] + aresta.peso
            if nova_dist < distancias[aresta.destino]:
                distancias[aresta.destino] = nova_dist
                anteriores[aresta.destino] = no_atual
                heapq.heappush(heap, (nova_dist, aresta.destino))

    return distancias, anteriores

def reconstruir_caminho(anteriores, origem, destino):
    caminho, no = [], destino
    while no:
        caminho.append(no)
        no = anteriores[no]
    caminho.reverse()
    return caminho if caminho and caminho[0] == origem else []