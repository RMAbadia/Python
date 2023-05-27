def maior_entre_extremidades(lista, resposta, soma, executadas = {}):
    if(len(lista) < 3):
        return max(lista)

    else:

        if(soma):
            soma = False

            esquerda = str(lista[1:])
            direita = str(lista[:-1])
            meio = str(lista[1:-1])

            if(esquerda in executadas and direita in executadas and meio in executadas):
                variavel1 = max(executadas[esquerda], executadas[meio])
                variavel2 = max(executadas[meio], executadas[direita])

            else:
                variavel1 = max(maior_entre_extremidades(lista[1:], resposta, soma), maior_entre_extremidades(lista[1:-1], resposta, soma))
                variavel2 = max(maior_entre_extremidades(lista[1:-1], resposta, soma), maior_entre_extremidades(lista[:-1], resposta, soma))

            resultado_da_rodada = max(variavel1 + lista[0], variavel2 + lista[-1])
            executadas[str(lista)] = resultado_da_rodada
            
            return resultado_da_rodada
            
        else:
            soma = True

            valor1 = maior_entre_extremidades(lista[1:], resposta, soma)
            valor2 = maior_entre_extremidades(lista[:-2], resposta, soma)

            return max(valor1, valor2)

resposta = 0
indices = int(input())
valores_indices = list(map(int, input().split()))
print(maior_entre_extremidades(valores_indices, resposta, True))