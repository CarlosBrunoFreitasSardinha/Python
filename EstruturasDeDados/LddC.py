#            TIPO ABSTRATO DE DADOS - TAD
#CONJUNTO DE VALORES E CONJUNTO DE OPERAÇÕES SOBRE ESTES VALORES

# LDDE  - LISTA Dinamica Duplamente CIRCULAR

class No():
    def __init__(self, anterior, valor, proximo):
        self.ant = anterior
        self.info = valor
        self.prox = proximo
class Lddc():
    def __init__(self):
        self.prim = None
        self.quant = 0
    def ultimoValor(self):
        ant = self.prim
        while ant.prox!=self.prim:
            ant = ant.prox
        return ant
    def inserirInicio(self,valor):
        if self.quant == 0:
            self.prim = No(None, valor, None)
        elif self.quant==1:
            self.prim.ant = self.prim.prox = self.prim =  No(self.prim, valor, self.prim)
        else:
            aux = self.ultimoValor()
            self.prim.ant = aux.prox = self.prim = No(aux, valor, self.prim)
        self.quant+=1
    def inserirFim(self,valor):
        if self.quant == 0:
            self.prim = No(None,valor, None)
        elif self.quant==1:
            self.prim.ant = self.prim.prox =  No(self.prim, valor, self.prim)
        else:
            aux = self.ultimoValor()
            aux.prox = No(aux,valor, self.prim)
        self.quant+=1
    def show(self):
        if self.quant==0: print('\tLista Vazia!')
        aux = self.prim
        while aux.prox !=self.prim:
            print(aux.info)
            aux = aux.prox
        print(aux.info)
    def showReverso(self):
        if self.quant==0: print('\tLista Vazia!')
        aux = self.ultimoValor()
        while aux !=self.prim:
            print(aux.info)
            aux = aux.ant
        print(aux.info)
    def estahVazia(self):
        if self.quant == 0: return True
        else: return False
   
    def inserirAposDet(self, alter, valor):
        i = 0
        if not self.estahVazia():
            ant = aux = self.prim
            while aux != self.prim:
                ant = aux
                aux = aux.prox
                print(ant.info,'---')
                if ant.info==valor:
                    ant.prox = No(ant, alter, ant.prox)
                    ant = ant.prox
                    self.quant+=1
                    i+=1
            if ant.info==valor:
                ant.prox = No(ant, alter, ant.prox)
                self.quant+=1
                i+=1
        return i
   