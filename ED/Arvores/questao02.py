class ArvoreBinaria():
    def __init__(self, dado, esq = None, dir = None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

def constituiArvoreBinariaDeBusca(raiz):
    if not raiz:
        return True
    else:
        esquerda = raiz.esq
        direita = raiz.dir

        if(esquerda and direita):
            if(esquerda.dado > raiz.dado or direita.dado < raiz.dado):
                return False
        elif(esquerda or direita):
            if(esquerda):
                if(esquerda.dado > raiz.dado):
                    return False
                else:
                    constituiArvoreBinariaDeBusca(esquerda)
            else:
                if(direita.dado < raiz.dado):
                    return False
                else:
                    constituiArvoreBinariaDeBusca(direita)

        return constituiArvoreBinariaDeBusca(direita) and constituiArvoreBinariaDeBusca(esquerda)
