
import Tree

t = Tree.Tree()

print("INSERE")
t.insere(4)
t.insere(3)
t.insere(2)
t.insere(1)
t.insere(0)
t.insere(6)
t.insere(8)
print(t.insere(10))

print("BUSCAR 8")
print(t.buscar(8))
print("SOMA ARVORE")
print(t.soma())
print("SOMA FOLHAS")
print(t.somaFolhas())
print("IMPRIME FOLHAS")
print(t.printFolhas())
print()
print("Altura Arvore")
print(t.altura())
print()
print("IMPRIME Caminho 8")
t.printCaminho(8)
print()

t.inOrdem()