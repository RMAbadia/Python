pretendentes = int(input())
lista_nomes = {}

while pretendentes:
    pretendentes -= 1 
    dados = input().split()

    lista_nomes[dados[1] + ', ' + dados[0]] = [int(dados[2]), int(dados[3])]
   
lista_nomes = sorted(lista_nomes.items(), key=lambda dados: (abs(dados[1][0]-180), dados[1][1] != 75, dados[1][1] > 75, abs(dados[1][1]-75), dados[0]))

for i in lista_nomes:
    print(i[0])