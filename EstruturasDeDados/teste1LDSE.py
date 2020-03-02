#            TIPO ABSTRATO DE DADOS - TAD
#CONJUNTO DE VALORES E CONJUNTO DE OPERAÇÕES SOBRE ESTES VALORES

# LDSE  - LISTA DINAMICA SIMPESMENTE ENCADEADA

import Ldse

l = Ldse.Ldse()

l.inserirInicio('A')
l.inserirInicio('B')
l.inserirFim('Z')
print('****************')
l.show()
l.removerFim()


print('******lista**********')
l.show()
print('******apos**********')
l.inserirAposDet('C','B')
l.show()
print('********antes********')
l.inserirAntesDet('C','B')
l.show()
print('********remove C********')
l.remover('C')
l.show()
print('********INSERIR FIM********')
l.inserirFim('Z')
l.show()