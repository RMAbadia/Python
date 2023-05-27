class Arvore:

    def __init__(self, raiz = None):
        self.raiz = raiz
        self.FilhoEsquerdo = None
        self.FilhoDireito = None                

def InsereABB(Arvorezinha, valor):
    if(Arvorezinha.raiz == None):
        Arvorezinha.raiz = valor
    else:
        if(Arvorezinha.raiz > valor):
            if(Arvorezinha.FilhoEsquerdo == None):
                Arvorezinha.FilhoEsquerdo = Arvore(valor)
            else:
                InsereABB(Arvorezinha.FilhoEsquerdo, valor)
        else:
            if(Arvorezinha.FilhoDireito == None):
                Arvorezinha.FilhoDireito = Arvore(valor)
            else:
                InsereABB(Arvorezinha.FilhoDireito, valor)
        
def PreOrdem(arvore):
    if arvore:
        if(arvore.raiz != None): print(arvore.raiz, end=' ')
        PreOrdem(arvore.FilhoEsquerdo)
        PreOrdem(arvore.FilhoDireito)

def PosOrdem(arvore):
    if arvore:
        PosOrdem(arvore.FilhoEsquerdo)
        PosOrdem(arvore.FilhoDireito)
        if(arvore.raiz != None): print(arvore.raiz, end=' ')
    
def Ordem(arvore):
    if arvore:
        Ordem(arvore.FilhoEsquerdo)
        if(arvore.raiz != None): print(arvore.raiz, end=' ')
        Ordem(arvore.FilhoDireito)

entrada = 0
MinhaArvore = Arvore()

while(entrada != 'quack'):
    entrada = input()

    if(entrada == 'in'):
        Ordem(MinhaArvore)
        print()
    elif(entrada == 'pre'):
        PreOrdem(MinhaArvore)
        print()
    elif(entrada == 'pos'):
        PosOrdem(MinhaArvore)
        print()
    try:
        InsereABB(MinhaArvore, int(entrada))
    except:
        pass