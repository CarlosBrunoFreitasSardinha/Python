#            TIPO ABSTRATO DE DADOS - TAD
#CONJUNTO DE VALORES E CONJUNTO DE OPERAÇÕES SOBRE ESTES VALORES

# LDDE  - LISTA Dinamica Duplamente CIRCULAR

import LddC

l = LddC.Lddc()

l.inserirInicio('F')
l.inserirInicio('E')
l.inserirInicio('D')
l.inserirInicio('C')
l.inserirInicio('A')
l.inserirFim('G')

print("\n\n\tLista Inicial \n")
l.showReverso()
print("\t ==================== Lista COM B DPS A====================\n")
print(l.inserirAposDet('B','A'))
l.show()
print("\t ==================== Lista B DPS G====================\n")
print(l.inserirAposDet('B','G'))
l.show()
print("\t ==================== Lista B DPS B====================\n")
print(l.inserirAposDet('B','B'))
l.show()
