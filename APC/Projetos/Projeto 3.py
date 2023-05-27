arquivo = open("vectors.txt", "r")
vetores = []


tarefa,chamadas,K = input().split()
listanomes = []

for cont in range(0, int(chamadas)):
    nomedoarquivo = input() + ' '
    listanomes.append(nomedoarquivo)

b = ''
lista = []
for linha in arquivo:
    for cont in listanomes:
        if cont in linha:
            for c in linha:
                if c == f'\n':
                    lista.append(b)
                    b = ''
                    c = ''
                elif c != ' ':
                    b += c
                else:
                    if '.' in b:
                        t = float(b)
                        lista.append(t)
                        b = ''

                    else:
                        lista.append(b)
                        b = ''
            if lista not in vetores:
                vetores.append(lista)
                lista = []

if int(tarefa) == 1:
    u = 0
    medoid = {}
    posicao = {}
    valoresmd = []
    resposta = []
    for d in vetores:
        posicao[d[0]] = d[1:27]
    for n, v in posicao.items():
        for n1, v1 in posicao.items():
            for pos in range(26):
                p = abs(float(v[pos]) - float(v1[pos]))
                u += p
        medoid[n] = u
        u = 0

    for item, lt in medoid.items():
        valoresmd.append(lt)
    valoresmd.sort()
    for fim, vl in medoid.items():
        if vl == valoresmd[0]:
            print(fim)

if int(tarefa) == 2:
    medoidprincipal = {}
    principal = ''
    medoid = {}
    posicao = {}
    valoresmd = []
    resposta = []
    u = 0

    for d in vetores:
        posicao[d[0]] = d[1:27]
    for n, v in posicao.items():
        for n1, v1 in posicao.items():
            for pos in range(26):
                p = abs(float(v[pos]) - float(v1[pos]))
                u += p
        medoid[n] = u
        u = 0
    for item, lt in medoid.items():
        valoresmd.append(lt)
    valoresmd.sort()
    for fim, vl in medoid.items():
        if vl == valoresmd[0]:
            principal = fim
    for j, n in posicao.items():
        if j == principal:
            medoidprincipal[j] = n

    K = int(K) - 1
    while int(K) != 0:
        ptotal = 0
        gtotal = 0
        ganho = 0
        ganhoprincipal = 0
        for d in vetores:
            posicao[d[0]] = d[1:27]
        del posicao[principal]

        for mp, vp in medoidprincipal.items():
            for n, v in posicao.items():
                for n1, v1 in posicao.items():
                    if n != n1:
                        for pos in range(26):
                            p = abs(float(v[pos]) - float(v1[pos]))
                            g = abs(float(vp[pos]) - float(v1[pos]))
                            if g > p:
                                ganho += abs(g - p)
                print(f'{n}  {ganho}')
                gtotal = 0
                ptotal = 0
                ganho = 0

        K = int(K) - 1


