comando = input()
letra = ''
numero = ''

for i in range(len(comando)):
    if comando[i].isdigit() == False:
        letra = letra + comando[i]
    elif comando[i].isdigit() == True: