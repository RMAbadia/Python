# BUSCA: processo algorítmico de encontrar um item específico numa coleção de intens e retorna valor booleano

lista = [10, 12, 13, 15]
10 in lista
3 in lista

#Busca Sequencial desordenada

def busca_sequencial(lista, item):
    for e in lista:
        if e == item:
            return True
        
    return False

#Melhor caso: encontra-se o item na primeira posição
#Pior caso: não encontra ou encontra-se o item na última posição
#Medio caso: encontra-se o item na metade da lista

#Busca sequencial ordenada

def BuscaSequencialOrdenada(lista, item):
    pos = 0
    encontrou = False
    para = False

    while pos < len(lista) and not encontrou and not para:
        if lista[pos] == item:
            encontrou = True
        else:
            if lista[pos] > item:
                para = True
            else:
                pos += 1
        return encontrou

#Busca Binária: nessa busca tem-se uma lista ordenada, na qual comparamos o item do meio e analisa-se se é igual ao item, caso seja menor ou maior elima-se metade da lista

def BuscaBinaria(lista, item):
    primeiro = 0
    ultimo = len(lista)-1
    encontro = False

    while primeiro<=ultimo and not encontro:
        meio = (primeiro+ultimo)/2
        if lista[meio] == item:
            encontro = True
        else:
            if item < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1

    return encontro

'por recursão'

def busca_binaria(lista, item):
    if not lista:
        return False

    meio = len(lista) // 2
    if lista[meio] == item:
        return True
    elif lista[meio] < item:
        #vamos examinar o segmento direito da lista
        return busca_binaria(lista[meio + 1:], item)
    else:
        #vamos examinar o segmento esquerdo da lista
        return busca_binaria(lista[:meio], item)

#Hashing (tabela de dispersão): é uma coleção de itens que são armazenados de maneira a serem encontrados com facilidade mais tarde

#ORDENAÇÃO: processo de coloca elemento de uma coleção em uma determinada ordem

#Bubble Sort: realiza multiplas passagem por uma lista, compara itens adjacentes e troca aqueles que estão fora de ordem

def bubbleSort(lista):
    for passnum in range(len(lista)-1,0,-1):
        for i in range(passnum):
            if lista[i]>lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp

#Short Bubble

def shortBubbleSort(lista):
    exchanges = True
    passnum = len(lista)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if lista[i]>lista[i+1]:
               exchanges = True
               temp = lista[i]
               lista[i] = lista[i+1]
               lista[i+1] = temp
       passnum = passnum-1

#Ordenação Por Seleção: realiza apenas uma troca a cada passagem pela lista

def selectionSort(lista):
   for fillslot in range(len(lista)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if lista[location]>lista[positionOfMax]:
               positionOfMax = location

       temp = lista[fillslot]
       lista[fillslot] = lista[positionOfMax]
       lista[positionOfMax] = temp
    
#Ordenação por Inserção:

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue