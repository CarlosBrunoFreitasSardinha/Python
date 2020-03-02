#            TIPO ABSTRATO DE DADOS - TAD
#CONJUNTO DE VALORES E CONJUNTO DE OPERAÇÕES SOBRE ESTES VALORES

# LES  - LISTA ESTATISTICA SEQUENCIAL

class Les():
    def __init__(self):
        self.vet = [None, None, None, None, None, None]
        self.quant = 0
    def inserirFim(self, valor):
        self.vet[self.quant] = valor
        self.quant += 1
    def inserirInicio(self, valor):
        i = self.quant+1
        while i!=0:
            self.vet[i] = self.vet[i-1]
            i-=1
        self.vet[i] = valor
        self.quant += 1
    def remover(self, valor):
        qt = i = 0
        while i<self.quant:
            if self.vet[i]==valor:
                j=i
                while j+1<self.quant:
                    self.vet[j] = self.vet[j+1]
                    j+=1
                qt += 1
                self.vet[self.quant-qt] = None
            i+=1
        self.quant -= qt
        return qt
    def show(self):
        if self.quant==0: print('\tLista Vazia!')
        i=0
        while i<self.quant:
            print(self.vet[i], end=' ')
            i+=1
        print('',end='\n')
