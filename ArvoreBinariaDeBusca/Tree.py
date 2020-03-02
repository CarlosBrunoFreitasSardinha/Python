
class No:
    def __init__(self, valor):
        self.info = valor
        self.esq = None
        self.dir = None
    def insere(self, valor):
        if valor <= self.info:
            if self.esq == None:
                self.esq = No(valor)
                return 1
            else:
                return 1 + self.esq.insere(valor)
        else:
            if self.dir == None:
                self.dir = No(valor)
                return 1
            else:
                return 1 + self.dir.insere(valor)
    def buscar(self, valor):
        if valor == self.info:
            return 1
        elif valor < self.info:
            if self.esq == None:
                return 0
            else:
                aux = self.esq.buscar(valor)
                if aux == 0:
                    return 0
                else:
                    return aux+1
        else:
            if self.dir == None:
                return 0
            else:
                aux = self.dir.buscar(valor)
                if aux == 0:
                    return 0
                else:
                    return aux+1
    def inOrdem(self):
        if self.esq != None:
            self.esq.inOrdem()
        print(self.info, end=' ')
        if self.dir != None:
            self.dir.inOrdem()
    def soma(self):
        total = self.info
        if self.esq != None:
            total += self.esq.soma()
        if self.dir != None:
            total += self.dir.soma()
        return total
    def somaFolhas(self):
        total = 0
        if self.esq == None and self.dir == None:
            total = self.info
        if self.esq != None:
            total += self.esq.somaFolhas()
        if self.dir != None:
            total += self.dir.somaFolhas()
        return total
    def printFolhas(self, a):
        if self.esq != None:
            self.esq.printFolhas(a)
        if self.esq == None and self.dir == None:
            a.append(self.info)
        if self.dir != None:
            self.dir.printFolhas(a)
        return a
    def printCaminho(self, valor):
        if valor == self.info:
            print(' -> ' + str(self.info), end=' ')
        elif valor < self.info:
            if self.esq == None:
                return 0
            else:
                print(' -> ' + str(self.info), end=' ')
                self.esq.printCaminho(valor)
        else:
            if self.dir == None:
                return 0
            else:
                print(' -> ' + str(self.info), end=' ')
                aux = self.dir.printCaminho(valor)

    def max(a, b):
        if a > b:
            return a
        return b

    def altura(self):
        hesq = hdir = 0
        if self.esq != None:
            hesq = self.esq.altura()
        if self.dir!= None:
            hdir = self.dir.altura()
        return 1 + max(hesq, hdir)


class Tree:
    def __init__(self):
        self.raiz = None
    def insere(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
            return 1
        else:
            return self.raiz.insere(valor) + 1
    def buscar(self, valor):
        if self.raiz == None:
            return 1
        else:
            return self.raiz.buscar(valor)
    def inOrdem(self):
        self.raiz.inOrdem()
    def soma(self):
        if self.raiz != None:
            return self.raiz.soma()
    def somaFolhas(self):
        if self.raiz != None:
            return self.raiz.somaFolhas()
    def printFolhas(self):
        a = []
        if self.raiz != None:
            return self.raiz.printFolhas(a)

    def printCaminho(self, valor):
        if self.raiz == None:
            return "Arvore Vazia"
        else:
            return self.raiz.printCaminho(valor)

    def altura(self):
        if self.raiz != None:
            return self.raiz.altura()
        else:
            return 0