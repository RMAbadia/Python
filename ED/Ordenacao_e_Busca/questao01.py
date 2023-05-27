def verifica(string1, string2):
    resposta1 = sorted(list(string1))
    resposta2 = sorted(list(string2))
    imprevisto = ''
    estudar = ''

    for i in resposta1:
        if i in resposta2:
            resposta2.remove(i)
        else:
            if i not in estudar:
                estudar += i
    
    for i in resposta2:
        imprevisto += i

    return estudar, imprevisto

casos = int(input())

while casos:
    conteudo = input()
    linha1 = input()
    linha2 = input()
    linha3 = input()
    
    concatena = linha1+linha2+linha3

    testou1, testou2 = verifica(conteudo, concatena)

    if(testou2 != ''):
        print('You died!')
    elif(len(testou1) != 0):
        print(f'Bora ralar: {testou1}')
    else:
        print('It\'s in the box!')
    
    casos-=1