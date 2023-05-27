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

ordem_dos_pesos = Stack()
pesos_retirados = 0
esforco_realizado = 0

peso = int(input())
while peso != 0:
    ordem_dos_pesos.push(peso)
    peso = int(input())
    
peso_desejado = int(input())

for peso_i in range(ordem_dos_pesos.size()):
    varia = ordem_dos_pesos.pop()
    if(varia == peso_desejado):
        pesos_retirados += 1
        esforco_realizado += varia
        print(f"Peso retirado: {varia}")
        break
    else:
        pesos_retirados += 1
        esforco_realizado += varia
        print(f"Peso retirado: {varia}")

print(f"Anilhas retiradas: {pesos_retirados}")
print(f"Peso total movimentado: {esforco_realizado}")