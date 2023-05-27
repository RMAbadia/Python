#Árvores:

    # - Os nós de uma árvore são independentes entre si
    # - Nó: são os pontos ligados pelas arestas
    # - Arestas: são as ligações(caminhos) que ligam os nós
    # - Raiz: único nó que não possui arestas de entrada
    # - Caminho: percurso saindo de um nó percorrendo arestas e chegando ao determinado nó final
    # - Filhos: nós que são filhos de um mesmo nó anterior
    # - Pai: é nó que se conecta a outros nós pelas arestas de saída
    # - Irmão: aqueles que são filhos do mesmo nó 
    # - Subárvore: conjunto de nós e arestas compostos por um pai e todos os descendentes desse pai
    # - Nó folha: um nó que não tem filhos
    # - Nível: número de arestas no caminho nó para outro
    # - Altura: é o nível máximo de qualquer nó na árvore

#Definição 01: Conjunto de nós e um conjunto de arestas que conectam pares de nós. Propriedades:

    # - Um nó da árvore é designado como o nó raiz
    # - Cada nó n, exceto o nó raiz, é conectado por uma aresta de exatamente um outro nó p, onde p é o pai de n
    # - Um caminho único percorre da raiz para cada nó
    # - Se cada nó da árvore tiver no máximo dois filhos, dizemos que a árvore é uma árvore binária

#Codiguin:

class ArvoreBinaria:
    def __init__(self, raiz):
        self.key = raiz
        self.FilhoEsquerdo = None
        self.FilhoDireito = None
    
    def InserirEsquerda(self, NovoNo):
        if self.FilhoEsquerdo == None:
            self.FilhoEsquerdo = ArvoreBinaria(NovoNo)
        else:
            temporaria = ArvoreBinaria(NovoNo)
            temporaria.FilhoEsquerdo = self.FilhoEsquerdo
            self.FilhoEsquerdo = temporaria
        
    def InserirDireita(self,NovoNo):
        if self.FilhoDireito == None:
            self.FilhoDireito = ArvoreBinaria(NovoNo)
        else:
            temporaria = ArvoreBinaria(NovoNo)
            temporaria.FilhoDireito = self.FilhoDireito
            self.FilhoDireito = temporaria

    def RetornaFilhoDireito(self):
        return self.FilhoDireito

    def RetornaFilhoEsquerdo(self):
        return self.FilhoEsquerdo

    def MudaValorRaiz(self,obj):
        self.key = obj

    def RetornaRaiz(self):
        return self.key

#Travessia:

    # - Pré-Ordem: Visita-se inicialmente o nó raiz, recursivamente fazemos uma travessia de pre-ordem da sub-árvore esquerda, seguid por uma travessia recursiva de pre-ordem da subárvore diretia.
    # - Ordem: recursivamente uma travessia em ordem na subárvore esquerda, visitamos o nó raiz e finalmente fazemos uma travessia recursiva em ordem na subarvore direita
    # - Pos-Ordem: Fazemos recursivamente um percurso de pos-ordem da subárvore esquerda e da subarvore direita seguido por uma visita ao nó raiz

def PreOrdem(arvore):
    if arvore:
        print(arvore.RetornaRaiz())
        PreOrdem(arvore.RetornaFilhoEsquerdo())
        PreOrdem(arvore.RetornaFilhoDireito())

def PosOrdem(arvore):
    if arvore != None:
        PosOrdem(arvore.RetornaFilhoEsquerdo())
        PosOrdem(arvore.RetornaFilhoDireito())
        print(arvore.RetornaRaiz())

def Ordem(arvore):
  if arvore != None:
      Ordem(arvore.RetornaFilhoEsquerdo())
      print(arvore.RetornaRaiz())
      Ordem(arvore.RetornaFilhoDireito())

MinhaArvore = ArvoreBinaria(4)
MinhaArvore.InserirEsquerda(5)
MinhaArvore.InserirDireita(6)
MinhaArvore.InserirEsquerda(7)
MinhaArvore.InserirDireita(8)
MinhaArvore.InserirDireita(9)

PreOrdem(MinhaArvore)
print()
PosOrdem(MinhaArvore)
print()
Ordem(MinhaArvore)