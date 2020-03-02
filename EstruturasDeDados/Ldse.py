#            TIPO ABSTRATO DE DADOS - TAD
#CONJUNTO DE VALORES E CONJUNTO DE OPERAÇÕES SOBRE ESTES VALORES

# LDSE  - LISTA Dinamica Simplesmente Encadeada

class No():
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo
class Ldse():
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    def verifica(self, posicao):
        if self.quant > posicao and posicao >=0:
            i=0
            aux = self.prim
            while i!=posicao:
                aux=aux.prox
                i+=1
            return "\n Valor Contido na posicao: %s \n"%aux.info
        return ''
    def inserirInicio(self,valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.prim = No(valor, self.prim)
        self.quant+=1
    def removerInicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
        self.quant-=1
    def inserirFim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.ult.prox = self.ult = No(valor, None)
        self.quant+=1
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
    def show(self):
        if self.quant==0: print('\tLista Vazia!')
        i=0
        aux = self.prim
        while aux !=None:
            print(i,' - ',aux.info)
            aux = aux.prox
            i+=1
    def vazia(self):
        if self.quant == 0: return True
        else: return False
 
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