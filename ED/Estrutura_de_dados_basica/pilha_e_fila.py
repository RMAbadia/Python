#PILHA (STACK): É uma coleção ordenada de itens onde a inserção de novos itens e a remção de intens ocorre na mesma extremidade (topo)

#implementação 
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
     
minha_pilha = Stack()     #Cria uma pilha
minha_pilha.isEmpty()     #Verifica se a pilha está vazia (True ou False)
minha_pilha.push(15)      #Insere um novo item '15' na pilha
minha_pilha.pop()         #Remove e retorna o item que está no topo da pilha
minha_pilha.peek()        #Retorna o item que está no topo da pilha
minha_pilha.size()        #Retorna o número de itens na pilha

# FILA (QUEUE): É uma coleção ordenada de itens em que a inserção de novos itens que acontece em uma extremidade (fim) e a remoção no outro extremo (inicio)

#implementação 
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
minha_fila = Queue()        #Cria uma fila
minha_fila.isEmpty()        #Verifica se a fila está vazia (True ou False)
minha_fila.enqueue()        #Insere um novo item '14' no fim da fila
minha_fila.dequeue()        #Remove e retorna o item do inicio da fila
minha_fila.size()           #Retorna o número de inten na pilha