#            TIPO ABSTRATO DE DADOS - TAD
#CONJUNTO DE VALORES E CONJUNTO DE OPERAÇÕES SOBRE ESTES VALORES

# LDSEC  - LISTA Dinamica Simplesmente Encadeada CIRCULAR

class No():
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo
########################################################
class Ldsec():
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
########################################################
    def inserirInicio(self,valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.prim = No(valor, self.prim)
        self.quant+=1
#####################
    def removerInicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.proximo
        self.quant-=1
########################################################        
    def inserirFim(self,valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.ult.prox = self.ult = No(valor, None)
        self.quant+=1
#####################
    def removerFim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            aux= self.prim
            while aux.prox != self.ult:
                aux = aux.prox
            self.ult = aux
            aux.prox = None
        self.quant-=1
########################################################
    def show(self):
        aux = self.prim
        while aux !=None:
            print(aux.info)
            aux = aux.prox
########################################################
    def vazia(self):
        if self.quant == 0: return True
        else: return False
########################################################
    def remover(self, valor):
        if self.ult.info == valor:
            self.removerFim()
        elif self.prim.info == valor:
            self.removerInicio()
        else:
            ant = aux = self.prim
            while aux.info!=valor and aux!=None:
                ant = aux
                aux = aux.prox
            if aux!=None:
                ant.prox = aux.prox
                self.quant-=1
########################################################
    def inserirAposDet(self, v1, v2):
        if self.quant == 0:
            print("lista esta vazia!")
            return False
        else:
            aux = self.prim
            while aux!=None:
                if aux.info==v2:
                    aux.prox = No(v1, aux.prox)
                aux = aux.prox
        self.quant+=1
        return True
############################
    def inserirAntesDet(self, valor1, valor2):
        if self.prim.info == valor2:
            self.prim = No(valor1, self.prim)
        else:
            ant = aux = self.prim
            while aux.info!=valor2 and aux!=None:
                ant = aux
                aux = aux.prox
            if aux.info==valor2:
                ant.prox = No(valor1, aux)
                self.quant+=1