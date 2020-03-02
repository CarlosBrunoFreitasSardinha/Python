#            TIPO ABSTRATO DE DADOS - TAD
#CONJUNTO DE VALORES E CONJUNTO DE OPERAÇÕES SOBRE ESTES VALORES

# LDDE  - LISTA Dinamica Duplamente Encadeada

class No():
    def __init__(self, anterior, valor, proximo):
        self.ant = anterior
        self.info = valor
        self.prox = proximo
class Ldde():
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    def inserirInicio(self,valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.prim.ant = self.prim = No(None, valor, self.prim)
        self.quant+=1
    def inserirFim(self,valor):
        if self.quant == 0:
            self.prim = self.ult = No(None,valor, None)
        else:
            self.ult.prox = self.ult = No(self.ult,valor, None)
        self.quant+=1
    def show(self):
        if self.quant==0: print('\tLista Vazia!')
        aux = self.prim
        while aux !=None:
            print(aux.info)
            aux = aux.prox
    def showReverso(self):
        aux = self.ult
        while aux !=None:
            print(aux.info)
            aux = aux.ant
    def removerInicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
            self.prim.ant = None
        self.quant-=1
    def removerFim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.ult = self.ult.ant
            self.ult.prox = None
        self.quant-=1
    def vazia(self):
        if self.quant == 0: return True
        else: return False
 
    def removerExtremos(self, valor):
        i=0
        if not self.vazia():
            if self.ult.info == valor:
                self.removerFim()
                i+=1
            elif self.prim.info == valor:
                self.removerInicio()
                i+=1
        if i!=0:return self.removerExtremos(valor)+i
        else:return i
    def remover(self, valor):
        i = self.removerExtremos(valor)
        if not self.vazia():
            ant = aux = self.prim
            while aux.prox != None:
                ant = aux
                aux = aux.prox
                if aux.info==valor:
                    ant.prox = aux.prox
                    i+=1
                    self.quant-=1
        return i
   