#Correndo na pista II
tempos = int(input())
tempos = (input().split())
b = 0
for i in range(len(tempos)):
    for c in tempos:
        if int(c) > int(b):
            b = c
listaresultado = []
for j in tempos:
    valor = int(b) - int(j)
    listaresultado.append(valor)

final = ''
for k in listaresultado:
    final += str(k) + ' '
print(final)

#Estatísticas I
'''valores = []
valores = input().split()
digitos = len(valores)
inteiros = 0
#def. media
for i in valores:
    b = int(i)
    inteiros += b
media = inteiros / len(valores)
#def. variancia
somavariancia = 0
for i in valores:
    v = int(i)
    calc1 = (v - media)**2
    somavariancia += calc1
variancia = somavariancia / len(valores)
print(f'{variancia:.1f}')
#def. desviopadrao
desviopadrao = variancia**(1/2)
print(f'{desviopadrao:.1f}')'''

#sozinho
'''numerodemeas = int(input())
pares = []
pares = input().split()
solo = []
for i in pares:
    for c in pares:
        b = pares.count(c)
        if b % 2 != 0:
            solo.append(c)
    break

if solo == []:
    print('tudo certo')
else:
    for g in solo:
        print(f'{g} sozinho')'''

#jogo da velha

'''def imprimeJogo(matriz):
    jogo = f'{matriz[0][0]}{matriz[0][1]}{matriz[0][2]}\n{matriz[1][0]}{matriz[1][1]}{matriz[1][2]}\n{matriz[2][0]}{matriz[2][1]}{matriz[2][2]}'
    print(jogo)

def atualizaMatriz(matriz,lin,col,tipo):
    if lin == 0 and col == 0:
        matriz[0][0] = tipo
    if lin == 0 and col == 1:
        matriz[0][1] = tipo
    if lin == 0 and col == 2:
        matriz[0][2] = tipo
    if lin == 1 and col == 0:
        matriz[1][0] = tipo
    if lin == 1 and col == 1:
        matriz[1][1] = tipo
    if lin == 1 and col == 2:
        matriz[1][2] = tipo
    if lin == 2 and col == 0:
        matriz[2][0] = tipo
    if lin == 2 and col == 1:
        matriz[2][1] = tipo
    if lin == 2 and col == 2:
        matriz[2][2] = tipo
    return matriz
#teste jogo da velha
matriz = [[' - ', ' - ', ' - '],
          [' O ', ' O ', ' X '],
          [' - ', ' - ', ' X ']]
imprimeJogo(atualizaMatriz(matriz, lin=0, col=0, tipo=' O '))'''

#sala de espera
'''linhas, colunas = input().split()
linha = []
vezes = 0
b = ''
g = ''
for i in range(int(linhas)):
    linha += input().split()
    for c in linha:
        if c == '0':
            '''

#bob e seus datagramas
'''valores = []
valores = input().split()
b = 0
menor = 0
for c in valores:
    if int(c) < b:
        menor += 1
        b == int(c)
print(menor)'''

#Equipe titular
'''total = int(input())
jogadores = []
jogadores = input().split()
reserva = []
jogadoresinteiros = []

for i in jogadores:
    jogadoresinteiros.append(int(i))
jogadores = sorted(jogadoresinteiros)

casas = total - 11
if casas > 0:
    for i in range(0, casas):
        h = jogadores[i]
        if h in jogadores:
            reserva.append(h)
    for cont in reserva:
        if cont in jogadores:
            jogadores.remove(cont)

    if len(reserva) > 11:
        remover = len(reserva) - 11
        for t in range(0, remover):
            u = reserva[t]
            if u in reserva:
                reserva.remove(u)

print(sum(jogadores) - (sum(reserva)))
'''

#bob e seus datagramas
'''soma = 0
numeros = []
numeros = input().split()
for i in range(0, len(numeros)):
    for cont in range(i + 1, len(numeros)):
        if int(numeros[cont]) < int(numeros[i]):
            soma += 1
        else:
            soma += 0
print(soma)
'''
print('ricardo lindo demais po')




