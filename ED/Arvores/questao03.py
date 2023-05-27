class ArvoreBinaria():
    def __init__(self, dado, esq = None, dir = None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

def verificaSimetria(raiz):
    if(not raiz):
        return True
    else:
        return VerificaFilhos(raiz.esq, raiz.dir)

def VerificaFilhos(esquerda, direita):
    if(not esquerda and not direita):
        return True

    if(esquerda and direita):
        if(esquerda.dado != direita.dado):
            return False    

    if(not esquerda or not direita):
        return False

    return VerificaFilhos(esquerda.esq, direita.dir) and VerificaFilhos(esquerda.dir, direita.esq)

raiz = ArvoreBinaria(1, ArvoreBinaria(0, ArvoreBinaria(1), ArvoreBinaria(0)), ArvoreBinaria(0, ArvoreBinaria(0), ArvoreBinaria(1)))
print(verificaSimetria(raiz))

raiz = ArvoreBinaria(1, ArvoreBinaria(0, ArvoreBinaria(0), ArvoreBinaria(1)), ArvoreBinaria(0, ArvoreBinaria(0), ArvoreBinaria(1)))
print(verificaSimetria(raiz))

raiz = ArvoreBinaria(0, ArvoreBinaria(1, ArvoreBinaria(1, None, None), ArvoreBinaria(0, None, None)), ArvoreBinaria(1, ArvoreBinaria(1, None, None), ArvoreBinaria(0, None, None)))
print(verificaSimetria(raiz))