import math

# Documento para consulta em caso de dúvidas!

primeiro = 1
segundo = 2
flutuante = 15.2
dicionario = {'ricardo':'yasmin'}
verdade = True

# 1) ENTRADA/SAÍDA:
print("ENTRADA/SAIDA\n")

print("Olá Mundo")                                                #imprime 'olá mundo' no terminal
print(primeiro)                                                   #imprime a variável 'primeiro'
'''primeiro = input()'''                                          #aguarda a entrada do usuário, essa entrada será considerada uma string
'''primeiro = input("Digite um valor")'''                         #aguarda a entrada do usuário após imprimir a mensagem
print("Ricardo","Mendes")                                         #imprime a mensagem com um espaço entre 'Ricardo' e 'Mendes'
print("Ricardo","Mendes", sep='FODA')                             #imprime a mensagem porém com 'FODA' na separação das strings
print("Ricardo","Mendes", end='FODA')                             #imprime a mensagem porém adicona 'FODA' ao final
print("Ricardo tem", primeiro, "como valor")                      #maneira de misturar variaveis com a frase
print("Ricardo depois do %d vem o %d" %(primeiro,segundo))        #string de formatação usa-se (%i e %d -> int, %u -> int sem sinal, %f -> ponto flutuante, %c -> caractere, %s -> string, % -> caractere
print("Ricardo %20d"%(primeiro))                                  #coloca o valor em um campo de 20 caracteres
print("Ricardo %-20d"%(primeiro))                                 #coloca o valor em um campo de 20 caracteres centralizado a esquerda
print("Ricardo %+20d"%(primeiro))                                 #coloca o valor em um campo de 20 caracteres centralizado a direita
print("Ricardo %020d"%(primeiro))                                 #coloca o valor em um campo de 20 caracteres preenchido com '0' a esquerda
print("Ricardo %20.2f"%(flutuante))                               #coloca o valor em um campo de 20 caracteres, com 2 caracteres a direita do ponto decimal
print("Ricardo %(ricardo)s"%(dicionario))                         #coloca o valor da chave de um dicionario
print(f"Ricardo tem int {primeiro} e float {flutuante}")          #Outra maneira de usar o print                                                        

print()

# 2) OPERADORES
print("OPERADORES\n")

print(2+3)     #soma
print(2*2)     #multiplicacao
print(6/3)     #divisao
print(7%3)     #resto da divisao
print(7//3)    #divisao inteira
print(2**10)   #exponencial
print((2+2)*2) #atribui ordem na operacao
primeiro < segundo  #menor que
primeiro > segundo  #maior que
primeiro <= segundo #menor ou igual a
primeiro >= segundo #maior ou igual a  
primeiro == segundo #igual a
primeiro != segundo #diferente
primeiro += segundo #soma e atribui
primeiro -= segundo #subtrai e atribui
primeiro *= segundo #multiplica e atribui
primeiro /= segundo #divide e atribui
primeiro %= segundo #resto da divisao e atribui

print()

# 3) TIPOS DE DADOS

int   #valor inteiro 
float #valores flutuante (0.5145)
bool  #True ou Falso (1 ou 0)

# 4) OPERADORES LOGICOS
print("OPERADORES LOGICOS\n")

primeiro and segundo #e logico
primeiro or segundo  #ou logico
print(not verdade)   #nao logico

print()

# 5) LISTAS (Listas são mutáveis)
print("LISTAS \n")

minha_lista = [4, 4, 5, 5]       #Cria uma lista com o elemento "3" fazendo parte da posição 0
print(minha_lista[0])            #indexação (Acessa o elemento da sequência)
minha_lista[0] = 5               #Altera o valor de 3 --> 5
print(minha_lista + minha_lista) #concatenação (combina duas sequencias)
print(minha_lista*5)             #repetição (concatena um certo numero de vezes)
print(5 in minha_lista)          #petinência (informa se o intem pertence a sequência)
print(len(minha_lista))          #comprimento (numero de itens da sequência)
print(minha_lista[0:3])          #fatiamento (extrai parte de uma sequência)

print()

minha_lista.append(5)            #adiciona um novo intem ao final da lista
minha_lista.insert(1, 0)         #adiciona o imtem "0" na posição "1"
minha_lista.pop()                #remove e retorna o último item da lista
minha_lista.pop(0)               #remove e retorna o i-esimo(primeiro no caso) item da lista
minha_lista.sort()               #modifica a lista para ficar ordenada
minha_lista.reverse()            #inverte a ordem dos items da lista
del minha_lista[2]               #exclui o terceiro item da lista
minha_lista.index(5)             #retorna a primeira posição do item (no caso do valor "5")
minha_lista.count(5)             #retorna o número de ocorrência do item (no caso do valor "5")
minha_lista.remove(5)            #remove a primeira ocorreência do item (no caso do valor "5")

# 7) RANGE
print("RANGE\n")

a = range(10)          #produz um objeto de intervalo (representa uma sequência de valores)
a = range(5, 10)       #sequência de valores de 5 à 10 (5 -> 9)
list(a)                #possivel ver o valor do objeto de intervalo como uma lista
a = range(0,10,2)      #produz um objeto de intervalo, porém pulando de dois em dois
a = range(10, 0, -1)   #produz um objeto de intervalo, porém decrementa 1 unidade
print(list(a))

# 8) STRING (são coleções de zeros ou mais letras, números e símbolos, string são imutáveis)
print("STRING\n")

meunome = "Riciarido"       #implementa string a uma variável
meunome[0]                  #retorna o caractere da casa 1
meunome*2                   #repete a string "2" vezes
meunome.center(100)         #centraliza a string com um campo "100"
meunome.count('i')          #retonar o número de ocorrências do item "i"
meunome.ljust(100)          #justifica à esquerda com um campo "100"
meunome.rjust(100)          #justifica à direita com um campo "100"
meunome.lower()             #retorna à string em minúsculo
meunome.upper()             #retorna à string em maiúsculo
meunome.find('o')           #retorna o índice do item
meunome.split('i')          #cria uma lista dividindo a string nos caracteres indicados "i"

# 9) TUPLAS (Semelhantes as listas por possuir sequência de dados heterogêneos, porém é imutalvel igual as strings)
print("TUPLAS\n")

tupla = (True, 15, 'ricardo')
print(len(tupla))
print(tupla)
print(tupla[2])
print(tupla*5)

# 10) CONJUNTO (coleção não ordenada de zero ou mais objetos de dados imutáveis, não perimite duplicatas, é heterogêneo)
print("CONJUNTO\n")

conjunto1 = {15, True, 'ricardo', 15.2}     #cria um conjunto
15 in conjunto1                             #verifica se "15" pertence ao conjunto
len(conjunto1)                              #numero de elementos do conjunto
conjunto2 = {15, False, 'ricardo', 15.3}
conjunto1 | conjunto2                       #retorna um novo conjunto com os elementos dos dois conjuntos anexados
conjunto1 & conjunto2                       #retorna um novo conjunto com os elementos em comum entre os dois conjuntos
conjunto2 - conjunto1                       #retorna um novo conjunto com os elementos do primeiro conjunto (conjunto2) que não estão no segundo conjunto (conjunto1)
conjunto1 <= conjunto2                      #retorna se todos os elementos do primeiro conjunto (conjunto1) estão no segundo conjunto (conjunto2)
conjunto1.union(conjunto2)                  #retorna um novo conjunto com os elementos dos dois conjuntos
conjunto1.intersection(conjunto2)           #retorna um novo conjunto com os elementos em comum entre os dois conjuntos
conjunto1.difference(conjunto2)             #retorna a diferença entre os dois conjuntos
conjunto1.issubset(conjunto2)               #retorna se todos os elemento do conjunto está no outro
conjunto1.add(5)                            #adiciona o item ao conjunto
conjunto1.pop()                             #remove um item arbitrário do conjunto
conjunto1.clear()                           #Limpa o conjunto

# 11) DICIONÁRIO (Coleção de pares associados de itens, cada par consiste em uma chave e um valor)
print("DICIONARIO\n")

dicionario = {'ricardo': 'yasmin', 'arthur':'lara', 'marcola':'matheus'}   #cria um dicionário
dicionario['marcola'] = 'guizada'                                          #altera o valor da chave "marcola"
dicionario['ricardo']                                                      #retorna o valor associado a chave 'ricardo'
'ricardo' in dicionario                                                    #retorna true ou false se a chave estiver no dicionário
del dicionario ['ricardo']                                                 #remove a chave do dicionario
dicionario.keys()                                                          #retorna as chaves em um objeto dict_keys()
dicionario.values()                                                        #retorna os valores em um objeto dict_values()
dicionario.items()                                                         #retorna os pares chave-valor em um objeto dict_items()
dicionario.get('arthur')                                                   #retorna o valor associado a chave, se não 'none'
dicionario.get('arthur', False)                                            #retorna o valor associado a chave, se não 'False'

# 12) RECURSIVIDADE
print("RECURSIVIDADE\n")

condicao = int(8)               #Enquanto for True (diferente de zero), será executado o escopo do 'while'
while condicao:
    print(condicao, end='')
    condicao -=1

print()

for indice in 'ricardo':        #A variavel 'indice' irá percorrer os valores de range (0 até 7)
    print(indice, end='')       #Aconteceria o mesmo se fosse string, lista e etc
print("\n")

minha_lista = []                #tres formas de envolver 'lista' com o 'for'

for indice in range(1, 11):
    minha_lista.append(indice+indice)
print(minha_lista)

minha_lista = [indice+indice for indice in range(1, 11)]
print(minha_lista)

minha_lista = [indice+indice for indice in range (1, 11) if indice%2 != 0]
print(minha_lista)

# 13) CONDICIONAIS
print("CONDICIONAIS\n")

mensao = int(90)                # "if" atribui a primeira condição
if mensao < 50:                 # "elif" atribui mais condições antes de chegar no else
    print("Tirou MI")           # "else" não atribui nem uma condição, mas só é acessado quando nenhumas das condições anteriores foram atendidas
elif mensao < 70:
    print("Tirou MM")
elif mensao < 90:
    print("Tirou MS")
else:
    print("Tirou SS")

# 14) ERROS
print("ERROS\n")                                                  #Erro de sitaxe é quando tem-se erro na estrutura do código por exempo a falta do ':' ao final das condicionais ou das recursividade

'''valor = input('Digite o valor para calcular a raiz: ')'''      #Erro de semantico ou de lógica é quando o programa é executado mas retorna o valo errado                                 
'''
try:
    print(math.sqrt(valor))
except:
    print("Nao aceitamos valor negativo")
    print("Irei converter seu valor para calcular")
    print(math.sqrt(abs(float(valor))))'''

# 15) DECLARAÇÃO DE FUNÇÕES
print("DECLARACAO DE FUNCOES")

def teste(x, y, z):                                                     #definição de função requer o nome da função, o parametro passado entre "()" e o scopo.
    return x + y + z                                                    #a função ao lado pega como parametro os valores 'x, y e z' e retorna a soma deles

print(teste(10,10,10))
print(teste(teste(10, 10, 10), teste(10, 10, 10), teste(10, 10, 10)))   #chama a função passando como parametro a propria função

# 16) DEFINIÇÃO DE CLASSES
print("DECLARACAO DE CLASSES")                          #Entra-se na ideia de programação orientada a objeto           

class fracao:                                                           #Fornece a estrutura para que então seja definido os metodos

    def __init__(self, num, den):                                       #primeiro método é o contrutor, ele define a maneira como os objetos de dados são criados. O método contrutor é chamado de '__init__"
                                                                        #'self' é um parametro que sempre será usado como referência ao proprio objeto, nunca receberá um valor de parametro real na chamada
        self.numerador = num                                            #define o 'fracao' objeto para ter um interno objeto de dado chamado 'den' e 'num'
        self.denominador = den
    
    def __str__(self):                                                  #Transforma os dados internos em uma string
        return str(self.numerador) + "/" + str(self.denominador)        #A partir daqui pode-se implementar diversos metodos afim de facilitar o codigo, como soma, subtracao, multiplicacao e etc entre fracoes

minha_fracao = fracao(8, 10)                                            #IMPORTANTE: herança é a capacidade de uma classe está relacionada a outra classe. Essas classes geralmente são chamadas de 'subclasses' ou 'superclasses'
minha_fracao.___str__() 