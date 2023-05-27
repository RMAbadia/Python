'''tupla = ()
b = input().split(' ')
for c in b:
    tupla = tupla + (int(c), )
tupla_invertida = tupla[::-1]
print(tupla_invertida)'''

'''input()
valores = input().split(' ')
valoresinteiros = []
vezes = 0
for c in valores:
    valoresinteiros.append(int(c))
for g in valoresinteiros:
    b = g/2
    if b in valoresinteiros and b != float:
        h = valoresinteiros.count(int(b))
        vezes += 1 * h
print(vezes)
print(valoresinteiros)'''

'''lista = []
l1 = []
def replace(l, x):
    l1 = []
    tupla = ()
    for g in l:
        lista = []
        tupla = ()
        for cont in g:
            lista.append(cont)
        lista[-1] = x
        for i in lista:
            tupla += (int(i), )
        l1.append(tupla)
    return(l1)

l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
x = 100
resposta = replace(l, x)
print(resposta)'''

'''chamadas = input()
dicio = {}
dicio1 = {}
todos = ''
for cont in range(0, int(chamadas)):
    dicio1 = {}
    nomedoarquivo,atributo = input().split(':')
    dicio[nomedoarquivo] = atributo
    dicio1[nomedoarquivo] = atributo
    todos += f'{dicio1}\n'
print(f'{todos}{dicio}')'''

'''frase = input()
lista = []
dicio = {}
for c in frase:
    lista.append(c)

for cont in lista:
    b = lista.count(cont)
    dicio[cont] = b
print(dicio)'''

'''chamadas = input()
dicio = {}
vezes = ''
for cont in range(0, int(chamadas)):
    nomedoarquivo,atributo = input().split(' ')
    dicio[nomedoarquivo] = atributo
g = input().split(' ')

for k, v in dicio.items():
    for c in g:
        if g == k
    vezes += f'{v} '

print(vezes)'''