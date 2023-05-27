#GRAFOS - Grafos é uma estrutura mais geral que árvores, podemos imagina-lo como as rodovias dos mapas,
# vôos de companhias aéreas, o percurso que uma informação percorre via internet e outras coisas.

    # - Vértice(Nó): parte fundamental do grafo no qual pode ter um nome("chave"). Pode também ter informações adicionais("Carga útil")
    # - Aresta(Arco): conecta dois vértices para mostrar que existe relação entr eles, pode ser unidirecionais ou bidirecionais. Se as arestas são todas direcionais dizemos que o grafo é direcionado ou um dígrafo.
    # - Peso: as arestas podem ser ponderadas, assim informa que existe um custo para ir de um vértice ao outro
    # - Caminho: sequência de grafos conectados por arestas
    # - Ciclo: grafo direcionado é um caminho que começa e termina no mesmo vértice. Um grafo sem ciclo é chamado de "grafo acíclico" e um grafo direcionado sem ciclos é chamado de "grafo acíclico direcionado (DAG)"

#   Assim: Um Grafo pode ser representado por:
#       
#       G = (V, E)
#
#           V - conjunto de vertices
#           E - conjunto de arestas (cada aresta é uma tupla (v, w) onde w,v pertence a V)
#           Terceiro - Terceiro componente seria para representar um peso       

#CLASSE VERTICE

class Vertice:
    def __init__(self, nome):
        self.origem = nome
        self.conexoes = {}

    def AddVizinho(self, nome,distancia=0):
        self.conexoes[nome] = distancia

    def __str__(self):
        return str(self.origem) + ' conexoes: ' + str([x.origem for x in self.conexoes])

    def MostrarConexoes(self):
        return self.conexoes.keys()

    def MostrarOrigem(self):
        return self.origem

    def MostrarDistancia(self,nome):
        return self.conexoes[nome]

#CLASSE GRAFOS

class Graph:
    def __init__(self):
        self.ListaVertice = {}
        self.numVertices = 0

    def AddVertice(self,nome):
        self.numVertices = self.numVertices + 1
        NovoVertice = Vertice(nome)
        self.ListaVertice[nome] = NovoVertice
        return NovoVertice

    def RetornaVertice(self,n):
        if n in self.ListaVertice:
            return self.ListaVertice[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.ListaVertice

    def addEdge(self,f,t,weight=0):
        if f not in self.ListaVertice:
            nv = self.AddVertice(f)
        if t not in self.ListaVertice:
            nv = self.AddVertice(t)
        self.ListaVertice[f].AddVizinho(self.ListaVertice[t], weight)

    def MostrarVertices(self):
        return self.ListaVertice.keys()

    def __iter__(self):
        return iter(self.ListaVertice.values())