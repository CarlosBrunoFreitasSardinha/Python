#            TIPO ABSTRATO DE DADOS - TAD
#CONJUNTO DE VALORES E CONJUNTO DE OPERAÇÕES SOBRE ESTES VALORES

# LES  - LISTA ESTATISTICA SEQUENCIAL

import Les

l= Les.Les()

l.inserirInicio('D')
l.inserirInicio('N')
l.inserirInicio('A')
l.inserirInicio('M')
l.inserirInicio('A')
l.inserirFim('A')

print("\n\n\tLista Inicial\n")
l.show()
v = input('\n informe o caracter a ser removido: ')
print("\n Quantidade de Valores Removidos: %d \n"% l.remover(v))
print("\tLista Resultante\n")
l.show()