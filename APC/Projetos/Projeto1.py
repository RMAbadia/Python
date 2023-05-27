def tarefa1(x):
    a = ''
    b = ''
    for cont in range(0, int(x)):
        objeto1 = input()
        objeto2 = input()
        x1, y1, x2, y2 = input().split()
        info = f'{objeto1},{objeto2},{x1},{y1},{x2},{y2}'
        a = f'{a}\n{info}'
        b = a
    return b

def tarefa2(x):
    ob1 = 0; ob2 = 0; ob3 = 0; ob4 = 0; ob5 = 0; ob6 = 0; ob7 = 0; ob8 = 0; ob9 = 0
    ob10 = 0; ob11 = 0; ob12 = 0; ob13 = 0; ob14 = 0; ob15 = 0; ob16 = 0; ob17 = 0; ob18 = 0; ob19 = 0
    ob20 = 0; ob21 = 0; ob22 = 0; ob23 = 0; ob24 = 0; ob25 = 0; ob26 = 0; ob27 = 0; ob28 = 0; ob29 = 0; ob30 = 0
    for cont in range(0, int(x)):
        input()
        objeto1 = input()
        objeto2 = input()
        x1, y1, x2, y2 = input().split()
        if objeto2 == 'black-bison':
            ob1 +=1
        if objeto2 == 'elephant':
            ob2 += 1
        if objeto2 == 'white-horse':
            ob3 +=1
        if objeto2 == 'brown-horse':
            ob4 +=1
        if objeto2 == 'scarlet-ibis':
            ob5 +=1
        if objeto2 == 'black-ibis':
            ob6 +=1
        if objeto2 == 'white-ibis':
            ob7 +=1
        if objeto2 == 'blue-sky':
            ob8 +=1
        if objeto2 == 'overcast-sky':
            ob9 +=1
        if objeto2 == 'cloudy-sky':
            ob10 +=1
        if objeto2 == 'dusthaze-sky':
            ob11 +=1
        if objeto2 == 'rocky-mountain':
            ob12 +=1
        if objeto2 == 'snowy-mountain':
            ob13 +=1
        if objeto2 == 'birdseye-building':
            ob14 +=1
        if objeto2 == 'perspective-building':
            ob15 +=1
        if objeto2 == 'front-building':
            ob16 +=1
        if objeto2 == 'red-flower':
            ob17 += 1
        if objeto2 == 'purple-flower':
            ob18 +=1
        if objeto2 == 'pink-flower':
            ob19 +=1
        if objeto2 == 'sand':
            ob20 +=1
        if objeto2 == 'tree':
            ob21 +=1
        if objeto2 == 'green-field':
            ob22 +=1
        if objeto2 == 'snowy-field':
            ob23 +=1
        if objeto2 == 'yellow-field':
            ob24 +=1
        if objeto2 == 'road':
            ob25 +=1
        if objeto2 == 'tower':
            ob26 +=1
        if objeto2 == 'blue-ocean':
            ob27 +=1
        if objeto2 == 'green-cliff':
            ob28 +=1
        if objeto2 == 'black-cliff':
            ob29 +=1
        if objeto2 == 'waterfall':
            ob30 +=1
    return f'black-bison: {(ob1/int(x))*100:.1f}\nelephant: {(ob2/int(x))*100:.1f}\nwhite-horse: {(ob3/int(x))*100:.1f}\nbrown-horse: {(ob4/int(x))*100:.1f}\nscarlet-ibis: {(ob5/int(x))*100:.1f}\nblack-ibis: {(ob6/int(x))*100:.1f}\nwhite-ibis: {(ob7/int(x))*100:.1f}\nblue-sky: {(ob8/int(x))*100:.1f}\novercast-sky: {(ob9/int(x))*100:.1f}\ncloudy-sky: {(ob10/int(x))*100:.1f}\ndusthaze-sky: {(ob11/int(x))*100:.1f}\nrocky-mountain: {(ob12/int(x))*100:.1f}\nsnowy-mountain: {(ob13/int(x))*100:.1f}\nbirdseye-building: {(ob14/int(x))*100:.1f}\nperspective-building: {(ob15/int(x))*100:.1f}\nfront-building: {(ob16/int(x))*100:.1f}\nred-flower: {(ob17/int(x))*100:.1f}\npurple-flower: {(ob18/int(x))*100:.1f}\npink-flower: {(ob19/int(x))*100:.1f}\nsand: {(ob20/int(x))*100:.1f}\ntree: {(ob21/int(x))*100:.1f}\ngreen-field: {(ob22/int(x))*100:.1f}\nsnowy-field: {(ob23/int(x))*100:.1f}\nyellow-field: {(ob24/int(x))*100:.1f}\nroad: {(ob25/int(x))*100:.1f}\ntower: {(ob26/int(x))*100:.1f}\nblue-ocean: {(ob27/int(x))*100:.1f}\ngreen-cliff: {(ob28/int(x))*100:.1f}\nblack-cliff: {(ob29/int(x))*100:.1f}\nwaterfall: {(ob30/int(x))*100:.1f}'

def tarefa3(x):
    valoresx1 = 0
    valoresy1 = 0
    valoresx2 = 0
    valoresy2 = 0
    for cont in range(0, int(x)):
        input()
        objeto1 = input()
        objeto2 = input()
        x1, y1, x2, y2 = input().split()
        valoresx1 += int(x1)
        valoresy1 += int(y1)
        valoresx2 += int(x2)
        valoresy2 += int(y2)
    mediax = (valoresx1 + valoresx2) / (int(linhas)*2)
    mediay = (valoresy1 + valoresy2) / (int(linhas)*2)
    mediaAX = (valoresx2 - valoresx1) / int(linhas)
    mediaAY = (valoresy2 - valoresy1) / int(linhas)
    return f'{float(mediax):.0f} {float(mediay):.0f} {float(mediaAX):.0f} {float(mediaAY):.0f}'


tarefa, linhas = input().split()

if int(tarefa) == 1:
    print(tarefa1(linhas))

if int(tarefa) == 2:
    print(tarefa2(int(linhas)))

if int(tarefa) == 3:
    print(tarefa3(linhas))

if int(tarefa) == 5:
    arquivo = []
    av = []
    cp = []
    casorep = []
    printnada = []
    for cont in range(0, int(linhas)):
        print()
        objeto1 = input()
        objeto2 = input()
        x1, y1, x2, y2 = input().split()
        a = objeto1
        if objeto2 == 'green-field' or objeto2 == 'yellow-field' or objeto2 == 'snowy-field':
            if objeto1 not in cp:
                cp.append(objeto1)
                arquivo.append(objeto1)
        if objeto1 == a and objeto2 == 'tree' and objeto2 != 'green-field' and objeto2 != 'yellow-field' and objeto2 != 'snowy-field':
            if objeto1 not in av:
                av.append(objeto1)
                arquivo.append(objeto1)
        else:
            arquivo.append(objeto1)

    for c in arquivo:
        if c not in casorep:
            casorep.append(c)

    for c in casorep:
        if c in av:
            if c not in cp:
                print(c)
                printnada.append(c)
    if len(printnada) == 0:
        print('nada')









