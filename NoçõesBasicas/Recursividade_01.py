'''
funções recursivas para os seguintes problemas:

    Soma dos n primeiros números inteiros positivos
    Impressão de um número natural em base binária.
    Imprimir uma string invertida
    Somar todos os números de uma lista estática sequencial
    Somar todos os números de uma lista dinâmica simplesmente encadeada
    Gerador da sequência dada por:
    F(1) = 1
    F(2) = 2
    F(n) = 2 ∗ F(n − 1) + 3 ∗ F(n − 2).
Gerador de Sequência de Ackerman:
A(m, n) = n + 1, se m = 0
A(m, n) = A(m − 1, 1), se m != 0 e n = 0
A(m, n) = A(m − 1, A(m, n − 1)), se m != 0 e n != 0.
Gerador de máximo divisor comum (mdc):
mdc(x, y) = y, se x ≥ y e x mod y = 0
mdc(x, y) = mdc(y, x), se x < y
mdc(x, y) = mdc(y, x mod y), caso contrário.'''
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
    def inserirInicio(self,valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.prim = No(valor, self.prim)
        self.quant+=1
    def show(self):
        if self.quant==0: print('\tLista Vazia!')
        i=0
        aux = self.prim
        print('[', end='')
        while aux !=None:
            print(aux.info,end='')
            if(aux.prox!=None):
                print(', ', end='')
            aux = aux.prox
            i+=1
        print(']', end='\n')
    def vazia(self):
        if self.quant == 0: return True
        else: return False

def somaN(num):
    if num==1: return 1
    return num+somaN(num-1)
def imprimeBaseBin(num):
    if num==1 or num==0: return str(num)
    return imprimeBaseBin(num-(num//2)-num%2)+str(num%2)
def invertString(num, quant):
    if quant==1: return num[quant-1]
    return num[quant-1]+invertString(num, quant-1)
def somaTudoEstatica(num, quant):
    if quant==1: return num[quant-1]
    return num[quant-1]+somaTudoEstatica(num, quant-1)
def somaTudoDinamicamente(self):
    if  self.prox == None: return self.info
    return self.info+somaTudoDinamicamente(self.prox)
def geradorSequenciaF(num):
    if num==1: return 1
    if num==2: return 2
    return 2 * geradorSequenciaF(num - 1) + 3 * geradorSequenciaF(num - 2)
def geradorSequenciaAckerman(m, n):
    if m == 0: return n + 1
    if m > 0 and n == 0: return geradorSequenciaAckerman(m-1, 1)
    if m > 0 and n > 0:return geradorSequenciaAckerman(m - 1, geradorSequenciaAckerman(m,n-1))
def geradorMDC(x, y):
    if x >= y and x%y==0: return y
    if x < y: return geradorMDC(y, x)
    if x > y: return geradorMDC(y, x % y)
    
l = Ldse()
l.inserirInicio(4)
l.inserirInicio(3)
l.inserirInicio(2)
l.inserirInicio(1)

lista1=[1,2,3,4]
var ='ETNEXO'
print("\n\n\tLista Inicial \n")
l.show()


print(somaN(3))
print(imprimeBaseBin(15))
print(invertString(var,len(var)))
print(somaTudoEstatica(lista1,len(lista1)))
print(somaTudoDinamicamente(l.prim))
print(geradorSequenciaF(4))
print(geradorSequenciaAckerman(3,4))
print(geradorMDC(64, 8))
