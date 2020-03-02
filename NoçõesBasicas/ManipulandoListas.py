# Manipulado listas. 
# A expressão listaVazia =[] é igual a expressão listaVazia = list().
listaVazia = []
print("Lista: ", listaVazia)
print("Tipo da variável: ", type(listaVazia))

listaInteiros = [7, 49, 343, 2401]
print("Lista de inteiros: ", listaInteiros)

listaDeTiposDiferentes = ["Carlos", "Bruno", 1993, [6, 1.33]]
print("Lista de elementos com tipos diferentes: ", listaDeTiposDiferentes)

print()
#acessando valores internos da lista
# Sintaxe da função range().
condicaoInicial = 0
CondicaoFinal = 7
IncrementoOuDecremento = 1

# Convertendo um intervalo em uma lista.
print(list(range(condicaoInicial, CondicaoFinal, IncrementoOuDecremento)))

print()
# Ordenando listas.
listaTeste = [7, 25, 2, 3, 30, 7, 80, 100, -1, 15]
print("Lista não ordenada: ", listaTeste)
print()
# Ordenada em Default crescente
listaTeste.sort()
print("Lista ordenada: ", listaTeste)
print()
# Ordenada Decrescente
listaTeste.sort(reverse=True)
print("Lista ordenada em ordem decrescente: ", listaTeste)
print()

# Ordenando a listas sem alterar a mesma.
listaTeste = [7, 25, 2, 3, 30, 7, 80, 100, -1, 15]

lista_ordenada = sorted(listaTeste)
print("Lista ordenada: ", lista_ordenada)
print()

print("A lista original permanece inalterada: ", listaTeste)
print()