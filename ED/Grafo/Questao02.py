from queue import PriorityQueue

class Vertice:
    def __init__(self, nome):
        self.dado = nome
        self.vizinhos = {}

    def setDistance(self, valor):
        self.vizinhos[self.dado] = valor

    def AddConexoesVertice(self, nome, distancia=0):
        self.vizinhos[nome] = distancia

    def RetornaDadoVertice(self):
        return self.dado
    
    def RetornaVizinhoVertice(self):
        lista = []
        for i in self.vizinhos.keys():
            lista.append(i.dado)
        return lista

class Graph():
    def __init__(self):
        self.ListaVertice = {}
        self.QuantidadeVertices = 0

    def AddVertice(self,nome):
        self.QuantidadeVertices = self.QuantidadeVertices + 1
        self.ListaVertice[nome] = Vertice(nome)
        return Vertice(nome)

    def AddConexoes(self, origem, destino, distancia = 0):
        if origem not in self.ListaVertice:
            self.AddVertice(origem)
        if destino not in self.ListaVertice:
            self.AddVertice(destino)

        self.ListaVertice[origem].AddConexoesVertice(self.ListaVertice[destino], distancia)

    def RetornaVizinhoVerticeGrafo(self, origem):
        return self.ListaVertice[origem].RetornaVizinhoVertice()


def dijkstra(aGraph,start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                    + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance( newDist )
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert,newDist)

#Inicio do problema
MeuGrafo = Graph()
QuantVert = int(input())

while(QuantVert):
    QuantVert -= 1
    EleEVizinhos = list(map(int, input().split()))

    MeuGrafo.AddVertice(EleEVizinhos[0])

    for i in EleEVizinhos[2:]:
        MeuGrafo.AddConexoes(EleEVizinhos[0], i)

eu, mussum = map(int, input().split())

if(len(MeuGrafo.RetornaVizinhoVerticeGrafo(eu)) == 0 or len(MeuGrafo.RetornaVizinhoVerticeGrafo(eu)) == 0):
    print('Forevis alonis...')
else:
    
    
    '''for i in MeuGrafo.ListaVertice:
        print(MeuGrafo.RetornaVizinhoVerticeGrafo(i))'''