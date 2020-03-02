class No():
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo


class pdse ():
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
###########################

    def incereInicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.prim = No(valor, self.prim)
        self.quant += 1

    def removeInicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
        self.quant -= 1

    def show(self):
        aux = self.prim
        while aux != None:
            print(aux.info, end=' ')
            aux = aux.prox
        print()

    def estahVazia(self):
        return self.quant == 0

    def getPrim(self):
        return self.prim.info

    def dividiCompara(self):
        l = pdse()
        aux = self
        while aux.getPrim() != 'c':
            l.incereInicio(aux.getPrim())
            aux.removeInicio()
        aux.removeInicio()

        while aux.estahVazia() != True:
            if aux.getPrim() != l.getPrim():
                return "Não atende ao padrão!!"
            aux.removeInicio()
            l.removeInicio()
        return "Atende ao Critério!"
