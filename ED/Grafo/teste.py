import sys
from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight=0):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D

inicia = 0
QuantVert = int(input())

while(QuantVert):
    QuantVert -= 1
    EleEVizinhos = list(map(int, input().split()))

    if inicia == 0:
        inicia += 1
        MeuGrafo = Graph(EleEVizinhos[0])
        for i in EleEVizinhos[2:]:
            MeuGrafo.add_edge(EleEVizinhos[0], i)
    else:   
        for i in EleEVizinhos[2:]:
            print(EleEVizinhos[0])
            MeuGrafo.add_edge(EleEVizinhos[0], i)

eu, mussum = map(int, input().split())

resultado = dijkstra(MeuGrafo, eu)