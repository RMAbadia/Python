tarefa, chamadas = input().split()

if int(tarefa) == 1:
    nomedosarquivos = []
    objetos = []
    vezes = 0
    respostafinal = ''
    listadeobjetos = ['bison', 'elephant', 'horse', 'ibis', 'sky', 'mountain', 'building', 'flower', 'sand', 'tree',
                      'field', 'road', 'tower', 'ocean', 'cliff', 'waterfall']

    for cont in range(0, int(chamadas)):
        input()
        nomedoarquivo = input()
        objeto = input().split('-')
        coordenadas = input().split()

        if nomedoarquivo not in nomedosarquivos:
            if len(nomedosarquivos) > 0 and len(objetos) > 0:
                resposta = f'{nomedosarquivos[0]}'
                for co in listadeobjetos:
                    if co in objetos:
                        resposta += f' {1}'
                    else:
                        resposta += f' {0}'
                if resposta not in respostafinal:
                    respostafinal += f'{resposta}\n'
            nomedosarquivos = []
            objetos = []
            nomedosarquivos.append(nomedoarquivo)

        if objeto not in objetos:
            if len(objeto) > 1:
                objetos.append(objeto[1])
            if len(objeto) == 1:
                objetos.append(objeto[0])

        if vezes == 0 or nomedoarquivo in nomedosarquivos:
            if nomedoarquivo not in nomedosarquivos:
                nomedosarquivos.append(nomedoarquivo)
            vezes += 1

    if len(nomedosarquivos) > 0 and len(objetos) > 0:
        resposta = f'{nomedosarquivos[0]}'
        for cont in listadeobjetos:
            if cont in objetos:
                resposta += f' {1}'
            else:
                resposta += f' {0}'
        if resposta not in respostafinal:
            respostafinal += f'{resposta}'
    print(respostafinal)


if int(tarefa) == 2:
    nomedosarquivos = []
    listaarea = []
    listacentrox = []
    listacentroy = []
    listalargurax = []
    listalarguray = []
    vezes = 0
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    resposta = ''

    for cont in range(0, int(chamadas)):
        input()
        nomedoarquivo = input()
        objeto = input().split('-')
        coordenadas = input().split()

        if vezes == 0:
            nomedosarquivos.append(nomedoarquivo)
            vezes += 1

        if nomedoarquivo in nomedosarquivos:
            x1.append(int(coordenadas[0]))
            y1.append(int(coordenadas[1]))
            x2.append(int(coordenadas[2]))
            y2.append(int(coordenadas[3]))

            centrox = (int(coordenadas[2]) + int(coordenadas[0])) / 2
            listacentrox.append(centrox)
            centroy = (int(coordenadas[3]) + int(coordenadas[1])) / 2
            listacentroy.append(centroy)

            largurax = int(coordenadas[2]) - int(coordenadas[0])
            listalargurax.append(largurax)
            larguray = int(coordenadas[3]) - int(coordenadas[1])
            listalarguray.append(larguray)

            area = largurax * larguray
            listaarea.append(area)

        if nomedoarquivo not in nomedosarquivos:
            s2 = ((((sum(x2) - sum(x1)) / 2) + sum(x1)) / len(x1)) / 128
            s3 = ((((sum(y2) - sum(y1)) / 2) + sum(y1)) / len(y1)) / 128
            s4 = (sum(listalargurax)/len(listalargurax))/128
            s5 = (sum(listalarguray)/len(listalarguray))/128
            s6 = (sum(listaarea)/len(listaarea)) / (128**2)
            import statistics
            s7 = (statistics.pstdev(listacentrox)) / 32
            s8 = (statistics.pstdev(listacentroy)) / 32
            s9 = (statistics.pstdev(listalargurax)) / 32
            s10 = (statistics.pstdev(listalarguray)) / 32
            resposta += f'{nomedosarquivos[0]} {len(x1)/2} {s2:.1f} {s3:.1f} {s4:.1f} {s5:.1f} {s6:.1f} {s7:.1f} ' \
                        f'{s8:.1f} {s9:.1f} {s10:.1f}\n'
            x1 = []
            y1 = []
            x2 = []
            y2 = []
            x1.append(int(coordenadas[0]))
            y1.append(int(coordenadas[1]))
            x2.append(int(coordenadas[2]))
            y2.append(int(coordenadas[3]))

            listalargurax = []
            listalarguray = []
            listacentrox = []
            listacentroy = []
            nomedosarquivos = []
            listaarea = []
            nomedosarquivos.append(nomedoarquivo)

            centrox = (int(coordenadas[2]) + int(coordenadas[0])) / 2
            listacentrox.append(centrox)
            centroy = (int(coordenadas[3]) + int(coordenadas[1])) / 2
            listacentroy.append(centroy)

            largurax = int(coordenadas[2]) - int(coordenadas[0])
            listalargurax.append(largurax)
            larguray = int(coordenadas[3]) - int(coordenadas[1])
            listalarguray.append(larguray)

            area = largurax * larguray
            listaarea.append(area)

    s2 = ((((sum(x2) - sum(x1)) / 2) + sum(x1)) / len(x1)) / 128
    s3 = ((((sum(y2) - sum(y1)) / 2) + sum(y1)) / len(y1)) / 128
    s4 = (sum(listalargurax) / len(listalargurax)) / 128
    s5 = (sum(listalarguray) / len(listalarguray)) / 128
    s6 = (sum(listaarea)/len(listaarea)) / (128**2)

    import statistics
    s7 = (statistics.pstdev(listacentrox))/32
    s8 = (statistics.pstdev(listacentroy))/32
    s9 = (statistics.pstdev(listalargurax))/32
    s10 = (statistics.pstdev(listalarguray))/32
    resposta += f'{nomedosarquivos[0]} {len(x1)/2} {s2:.1f} {s3:.1f} {s4:.1f} {s5:.1f} {s6:.1f} {s7:.1f} {s8:.1f} ' \
                f'{s9:.1f} {s10:.1f}'
    print(resposta)

if int(tarefa) == 3:
    objetos = []
    vezes = 0
    respostafinal = []
    arquivos = []
    listadeobjetos = ['bison', 'elephant', 'horse', 'ibis', 'sky', 'mountain', 'building', 'flower', 'sand', 'tree',
                      'field', 'road', 'tower', 'ocean', 'cliff', 'waterfall']
    bison = 0; elephant = 0; horse = 0; ibis = 0; sky = 0; mountain = 0; building = 0; flower = 0; sand = 0; tree = 0
    field = 0; road = 0; tower = 0; ocean = 0; cliff = 0; waterfall = 0; s2 = 0; s3 = 0; s4 = 0; s5 = 0; s6 = 0
    s7 = 0; s8 = 0; s9 = 0; s10 = 0
    listacentrox = []
    listacentroy = []
    listalargurax = []
    listalarguray = []
    listaarea = []
    x1 = []
    y1 = []
    x2 = []
    y2 = []

    for cont in range(0, int(chamadas)):
        input()
        nomedoarquivo = input()
        objeto = input().split('-')
        coordenadas = input().split()

        if vezes == 0 or nomedoarquivo in arquivos:
            if nomedoarquivo not in arquivos:
                arquivos.append(nomedoarquivo)

            vezes += 1
            x1.append(int(coordenadas[0]))
            y1.append(int(coordenadas[1]))
            x2.append(int(coordenadas[2]))
            y2.append(int(coordenadas[3]))

            centrox = (int(coordenadas[2]) + int(coordenadas[0])) / 2
            listacentrox.append(centrox)
            centroy = (int(coordenadas[3]) + int(coordenadas[1])) / 2
            listacentroy.append(centroy)

            largurax = int(coordenadas[2]) - int(coordenadas[0])
            listalargurax.append(largurax)
            larguray = int(coordenadas[3]) - int(coordenadas[1])
            listalarguray.append(larguray)

            area = largurax * larguray
            listaarea.append(area)

        if nomedoarquivo not in arquivos:
            if len(arquivos) > 0 and len(objetos) > 0:
                resposta = []
                for co in listadeobjetos:
                    if co in objetos:
                        if co == 'bison':
                            bison += 1
                        if co == 'elephant':
                            elephant += 1
                        if co == 'horse':
                            horse += 1
                        if co == 'ibis':
                            ibis += 1
                        if co == 'sky':
                            sky += 1
                        if co == 'mountain':
                            mountain += 1
                        if co == 'building':
                            building += 1
                        if co == 'flower':
                            flower += 1
                        if co == 'sand':
                            sand += 1
                        if co == 'tree':
                            tree += 1
                        if co == 'field':
                            field += 1
                        if co == 'road':
                            road += 1
                        if co == 'tower':
                            tower += 1
                        if co == 'ocean':
                            ocean += 1
                        if co == 'cliff':
                            cliff += 1
                        if co == 'waterfall':
                            waterfall += 1

                s2 += ((((sum(x2) - sum(x1)) / 2) + sum(x1)) / len(x1)) / 128
                s3 += ((((sum(y2) - sum(y1)) / 2) + sum(y1)) / len(y1)) / 128
                s4 += (sum(listalargurax) / len(listalargurax)) / 128
                s5 += (sum(listalarguray) / len(listalarguray)) / 128
                s6 += (sum(listaarea) / len(listaarea)) / (128 ** 2)
                import statistics
                s7 += (statistics.pstdev(listacentrox)) / 32
                s8 += (statistics.pstdev(listacentroy)) / 32
                s9 += (statistics.pstdev(listalargurax)) / 32
                s10 += (statistics.pstdev(listalarguray)) / 32

            x1 = []
            y1 = []
            x2 = []
            y2 = []
            x1.append(int(coordenadas[0]))
            y1.append(int(coordenadas[1]))
            x2.append(int(coordenadas[2]))
            y2.append(int(coordenadas[3]))

            listalargurax = []
            listalarguray = []
            listacentrox = []
            listacentroy = []
            nomedosarquivos = []
            listaarea = []

            centrox = (int(coordenadas[2]) + int(coordenadas[0])) / 2
            listacentrox.append(centrox)
            centroy = (int(coordenadas[3]) + int(coordenadas[1])) / 2
            listacentroy.append(centroy)

            largurax = int(coordenadas[2]) - int(coordenadas[0])
            listalargurax.append(largurax)
            larguray = int(coordenadas[3]) - int(coordenadas[1])
            listalarguray.append(larguray)

            area = largurax * larguray
            listaarea.append(area)

            objetos = []
            arquivos.append(nomedoarquivo)

        if objeto not in objetos:
            if len(objeto) > 1:
                objetos.append(objeto[1])
            if len(objeto) == 1:
                objetos.append(objeto[0])


    if len(arquivos) > 0 and len(objetos) > 0:
        for co in listadeobjetos:
            if co in objetos:
                if co == 'bison':
                    bison += 1
                if co == 'elephant':
                    elephant += 1
                if co == 'horse':
                    horse += 1
                if co == 'ibis':
                    ibis += 1
                if co == 'sky':
                    sky += 1
                if co == 'mountain':
                    mountain += 1
                if co == 'building':
                    building += 1
                if co == 'flower':
                    flower += 1
                if co == 'sand':
                    sand += 1
                if co == 'tree':
                    tree += 1
                if co == 'field':
                    field += 1
                if co == 'road':
                    road += 1
                if co == 'tower':
                    tower += 1
                if co == 'ocean':
                    ocean += 1
                if co == 'cliff':
                    cliff += 1
                if co == 'waterfall':
                    waterfall += 1
    s2 += ((((sum(x2) - sum(x1)) / 2) + sum(x1)) / len(x1)) / 128
    s3 += ((((sum(y2) - sum(y1)) / 2) + sum(y1)) / len(y1)) / 128
    s4 += (sum(listalargurax) / len(listalargurax)) / 128
    s5 += (sum(listalarguray) / len(listalarguray)) / 128
    s6 += (sum(listaarea) / len(listaarea)) / (128 ** 2)
    import statistics
    s7 += (statistics.pstdev(listacentrox)) / 32
    s8 += (statistics.pstdev(listacentroy)) / 32
    s9 += (statistics.pstdev(listalargurax)) / 32
    s10 += (statistics.pstdev(listalarguray)) / 32

    respostafinal = f'{bison/len(arquivos):.1f} {elephant/len(arquivos):.1f} {horse/len(arquivos):.1f} ' \
                    f'{ibis/len(arquivos):.1f} {sky/len(arquivos):.1f} {mountain/len(arquivos):.1f} ' \
                    f'{building/len(arquivos):.1f} {flower/len(arquivos):.1f} {sand/len(arquivos):.1f} ' \
                    f'{tree/len(arquivos):.1f} {field/len(arquivos):.1f} {road/len(arquivos):.1f} ' \
                    f'{tower/len(arquivos):.1f} {ocean/len(arquivos):.1f} {cliff/len(arquivos):.1f} ' \
                    f'{waterfall/len(arquivos):.1f} {(int(chamadas)/2)/len(arquivos):.1f} {s2/len(arquivos):.1f} ' \
                    f'{s3/len(arquivos):.1f} {s4/len(arquivos):.1f} {s5/len(arquivos):.1f} {(s6/len(arquivos)):.1f} ' \
                    f'{s7/len(arquivos):.1f} {s8/len(arquivos):.1f} {s9/len(arquivos):.1f} {s10/len(arquivos):.1f}'

    print(respostafinal)
