vertices, arestas, direcionamento = input().split()
MatrizAdjacente = []

for i in range(int(vertices)):
    MatrizAdjacente.append([0]*int(vertices))

while int(arestas):
    arestas = int(arestas) - 1
    origem, destino, peso = map(int, input().split())

    MatrizAdjacente[origem-1][destino-1] = peso

    if direcionamento == "N":
        MatrizAdjacente[destino-1][origem-1] = peso

for i in range(int(vertices)):
    for j in range(int(vertices)):
        print('%4d'%(MatrizAdjacente[i][j]), end='')

    print()