def maior_entre_extremidades(lista, executadas = {}):
    if(len(lista) < 3):
        return max(lista)

    else:

        esquerda = str(lista[2:])
        direita = str(lista [:-2])
        meio = str(lista[1:-1])

        if(esquerda in executadas and direita in executadas and meio in executadas):
            variavel1 = max(executadas[esquerda], executadas[meio])
            variavel2 = max(executadas[meio], executadas[direita])

        else:
            variavel1 = max(maior_entre_extremidades(lista[2:]), maior_entre_extremidades(lista[1:-1]))
            variavel2 = max(maior_entre_extremidades(lista[1:-1]), maior_entre_extremidades(lista[:-2]))

        resultado_da_rodadaa = max(variavel1 + lista[0], variavel2 + lista[-1])
        executadas[str(lista)] = resultado_da_rodadaa
            
        return resultado_da_rodadaa

indices = int(input())
valores_indices = list(map(int, input().split()))
print(maior_entre_extremidades(valores_indices))