#            TIPO ABSTRATO DE DADOS - TAD
#CONJUNTO DE VALORES E CONJUNTO DE OPERAÇÕES SOBRE ESTES VALORES

# LDSE  - LISTA Dinamica Simplesmente Encadeada

import Ldse

l = Ldse.Ldse()

l.inserirInicio('F')
l.inserirInicio('E')
l.inserirInicio('D')
l.inserirInicio('C')
l.inserirInicio('A')
l.inserirFim('G')

print("\n\n\tLista Inicial \n")
l.show()
v = int(input('\n informe a posicao: '))
print(l.verifica(v))
