#Senha Válida
senha = input()
numeros = 0
letras = 0
pontos = 0
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if len(senha) >= 6 and len(senha) <= 32:
    pontos += 1

if senha != senha.lower() and senha != senha.upper():
    pontos += 1

for i in senha:
    if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
        numeros += 1
if numeros > 0:
    pontos += 1

for i in senha:
    for c in alfabeto:
        if i.upper() == c.upper():
            letras += 1

if letras + numeros < len(senha) or pontos < 3:
    print('Senha invalida.')

else:
    if pontos >= 3:
        print('Senha valida.')

#Batalha naval 1D
'''mapa = input()
x = '.'
vezes = 0
for i in mapa:
    if i != x:
        vezes += 1
        x = i

print(f'{int((vezes/2 + 0.5)):.0f}')'''

#Escrita com espaço
'''palavra = input()
b = ''
for i in palavra:
    if i != ' ':
        b += (f'{i} ')
    elif i == ' ':
        b += (f'')

print(f'{b}')'''

#Tamanho de uma String sem len()
'''frase = input()
simbolo = 0
for i in frase:
        simbolo += 1
print(simbolo)'''

#remover vogais americanas AOYEUI
'''palavra = input()
consoante = 'bcdfghjklmnpqrstvwxz'
escrita = ''
for i in palavra:
        for c in consoante:
                if c.upper() == i.upper():
                        escrita += f'.{c}'

print(escrita)'''

#split
'''frase = input()
alfabeto = 'abcçdefghijklmnopqrstuvwxyz'
palavra = ''
diferente = ''
for i in frase:
        for c in alfabeto:
                if i.upper() in c.upper():
                        palavra += i
                elif i.upper() not in alfabeto.upper():
                        if palavra != diferente:
                                palavra += f'\n'
                                diferente = palavra
print(palavra)
'''

#compressão de strings

'''alfabeto = 'abcçdefghijklmnopqrstuvwxyz'
numeros = '1234567890'
chamadas = int(input())
resultado = ''
calc = ''
letra = ''
numero = ''
for c in range(0, chamadas):
        frase = input()
        for i in frase:
                for c in numeros:
                        if i == c:
                                numero += i
        for i in alfabeto:
                for c in frase:
                        if c.upper() == i.upper():
                                letra = i
                        calc = int(numero) * letra
print(calc)'''


#Genoma
'''A = 0
T = 0
G = 0
C = 0
quantidadegenoma = int(input())
genoma = input()
for i in genoma:
        if i == 'A':
                A += 1
        if i == 'T':
                T += 1
        if i == 'G':
                G += 1
        if i == 'C':
                C += 1


oculto = len(genoma) - (A + T + G + C)
if A >= (quantidadegenoma / 2) or T >= (quantidadegenoma / 2) or G >= (quantidadegenoma / 2) or C >= (quantidadegenoma / 2):
        print('Feiticeiro misterioso')
elif A == T == G == C:
        print('Segredos desvendados')
elif (len(genoma) - oculto) % 4 == 0 or quantidadegenoma % 4 == 0:
        print('Segredos desvendados')
else:
        print('Feiticeiro misterioso')
'''

#apagando algo

'''nletras = int(input())
string = input()
b = ''
resposta = ''
removidos = 0
iguais = 0
if nletras == 1:
        print(string)
for i in string:
        if i > b:
                b = i
for i in string:
        if i == b:
                iguais += 1
        if iguais == nletras:
                print((nletras - 1) * b)

else:
        for c in string:
                if c != b:
                        resposta += c
                elif c == b and removidos == 0:
                        resposta += ''
                        removidos += 1
print(resposta)'''
