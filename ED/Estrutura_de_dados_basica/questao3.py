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

indices = int(input())
valores = input().split()
sub_lista = int(input())

meu_deque = Deque()
maior = 0

for i in range(0, indices):
    meu_deque.addRear(valores[i])

    if(meu_deque.size() == sub_lista):
        for g in range(0, sub_lista):
            if(int(meu_deque.items[g]) > maior):
                maior = int(meu_deque.items[g])
        
        print(maior, end='  ')
        maior = 0
        meu_deque.removeFront()
    