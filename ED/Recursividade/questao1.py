def fib(valor, dicionario):
    
    if(valor in dicionario):
        dicionario[valor] += 1
    elif(valor not in dicionario):
        dicionario[valor] = 1

    if(valor <= 1):
        return valor
    else:
        return (fib(valor-2, dicionario) + fib(valor-1, dicionario ))

entrada = int(input())
chamadas = {}
mostra = 0

print(f'fibonacci({entrada}) = {fib(entrada, chamadas)}.')

for i in range(0, entrada+1):
    if(i in chamadas):
        print(f'{chamadas[i]} chamada(s) a fibonacci({i}).')
    else:
        print(f'0 chamada(s) a fibonacci({i}).')