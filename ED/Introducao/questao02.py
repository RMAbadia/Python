frase = input()

caracteres = len(frase)
resto = caracteres%2
ao_contrario = frase[::-1]
desigualdade = 0

if(resto == 0):
    for i in range(0, caracteres):
        if(frase[i] != ao_contrario[i]):
            desigualdade += 1
    
    if(desigualdade == 2):
        print("POSSÍVEL")
    else:
        print("IMPOSSÍVEL")

else:
    for i in range(0, caracteres):
        if(frase[i] != ao_contrario[i]):
            desigualdade += 1

    if(desigualdade <= 2):
        print("POSSÍVEL")
    else:
        print("IMPOSSÍVEL")