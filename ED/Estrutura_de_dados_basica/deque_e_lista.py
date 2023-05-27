#FILA DE DUAS EXTREMIDADES (DEQUE): Fila de duas extremidades tendo uma coleção ordenada de itens, esse intens podem ser inseridos e removidos tanto no fim quanto no inicio, tendo a capacidade de pilha e fila em uma lista

#Implementação

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

minha_deque = Deque()                #Cria um deque
minha_deque.addFront(5)              #Adiciona um item '5' no inicio da equipe
minha_deque.addRear(4)               #Adiciona um item '4' no fim da equipe
minha_deque.removeFront()            #Remove o item do inicio da fila
minha_deque.removeRear()             #Remove o item do fim da fila
minha_deque.isEmpty()                #Verifica se o Deque está vazio (True ou False)
minha_deque.size()                   #Retorna o número de itens no deque

# LISTA (LIST): Coleção de itens em que cada item tem uma posição relativa em relação aos outros(lista desordenada)

'''Comandos gerais:
        List()             - Cria uma lista
        add(item)          - Adiciona um item a lista
        remove(item)       - Remove um item da lista
        search(item)       - Procura item na lista (True ou false)
        isEmpty()          - Verifica se a lista está vazia (True ou false)
        size()             - Retorna o numero de intes da lista
        append(item)       - Adiciona um item no final da lista
        index(item)        - Retorna a posição do item na lista 
        insert(pos, item)  - Adiciona um novo item à lista na posição 'pos'
        pop()              - Remove e retorna o último item da lista
        pop(pos)           - Remove e retorna o item na posição pos '''
    
# IMPLEMENTAÇÃO LISTA DESORDENADA : Listas ligadas
    #Para sua implementação usamos o bloco básico de contrução da implementação de lista ligada que é o nó(Node) - (pense como números aleatorios, porém tendo a head (cabeça) e tendo o end)
    #  temp --> data|next --> None     None denota o fato de que não há próximo nó

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
    
#Classe UnordenedList - matem uma referência ao primeiro nó

class UnorderedList:

    def __init__(self):
        self.head = None
    
    def __str__(self):
        tmp = self.head
        lstr = ''
        while tmp != None:
            lstr += str(tmp.data) + ' '
            tmp = tmp.getNext()
            
        return lstr
    
    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)                      #Cria um novo nó e adiciona item
        temp.setNext(self.head)                #Muda a referência do novo nó para se referir ao antigo primeiro nó da lista
        self.head = temp                       #Define a cabeça da lista

    def size(self):                            #Processo de varredura
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):                    #Processo de varredura
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):                    #Proceso de varredura
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


minha_lista = UnorderedList()       #Cria uma lista desordenada  
minha_lista.add(10)                 #Adiciona item a lista
minha_lista.add(11) 
minha_lista.add(12)
minha_lista.add(13)
minha_lista.add(14)
minha_lista.isEmpty()               #Verifica se a lista está vazia (True ou False)
minha_lista.size()                  #Retorna a quantidade de itens na lista
minha_lista.search(1)               #Verifica se o item está na lista (True ou False)
minha_lista.remove(10)              #Remove um item da lista

#IMPLEMENTAÇÃO LISTA ORDENADA: Se trata de uma coleção de intens onde cada item detém uma posição relativa que é baseada em algumas caracteristicas subjacentes aos itens

#Classe OrderedList - Posições relativas dos itens são baseadas em algumas caracteristicas

class OrderedList:
    def __init__(self):
        self.head = None

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)   