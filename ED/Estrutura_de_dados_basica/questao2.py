class Queue:
    def __init__(self):
        self.items = []

    def __str__(self, indice):
        return str(self.items[indice])

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
lista_de_atividades = input().split()
executadas = int(input())
atividades = Queue()

if(executadas >= len(lista_de_atividades)//2):
    print("Tamanho da fila: 0")

else:
    for n in range(1, 11):
        for i in range(1, len(lista_de_atividades), 2):
            if(n == int(lista_de_atividades[i])):
                atividades.enqueue(lista_de_atividades[i-1])
                atividades.enqueue(n)

    while(executadas):
        atividades.dequeue()
        atividades.dequeue()
        executadas -= 1
        
    print(f"Tamanho da fila: {atividades.size()//2}")

    while(atividades.size()):
        print(f"Atividade: {atividades.dequeue()}, Prioridade: #{atividades.dequeue()}")