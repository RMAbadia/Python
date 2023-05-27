# Recursão: é um método para resolver problemas que envolve quebrar o problema em subproblemas até atingir um problema simples o bastante, que possa ser resolvido trivialmente. Em geral a recursão envolve uma função que chama ela mesma. A recursão nos permite escrever soluções elegantes para problemas que podem ser, de outra forma, muito difíceis de programar.
    # Três leis:
        # 1 - Um algoritmo recursivo deve possuir um caso base (base case).
        # 2 - Um algoritmo recursivo deve modificar o seu estado e se aproximar do caso base.
        # 3 - Um algoritmo recursivo deve chamar a si mesmo, recursivamente.

    # Sempre implementar o código da função recursiva pelo teste do caso base

def fatorial(n):
    if(n == 0):
        return 1
    else:
        return n * fatorial(n-1)

def soma(numeros):
   if len(numeros) == 1:
        return numeros[0]
   else:
        return numeros[0] + soma(numeros[1:])

print(fatorial(10))
print(soma([1, 2, 3, 4]))