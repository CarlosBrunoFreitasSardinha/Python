# Manipulado Matrizes. 


matriz = []
for i in range(0, 5, 1):
    lista = []
    for j in range(0, 5 , 1):
        lista.append([str(i+1) + "x"+ str(j+1)])
    matriz.append(lista)
# Impressão Normal
print(matriz)
# Impressão em outro formato
print("Matriz impressa de outra forma:")
for lista in matriz:
    for elemento in lista:
        print(elemento, end=' ')
    print()
