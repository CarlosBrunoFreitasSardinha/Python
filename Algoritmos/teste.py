def learquivo(arquivo):
    arq = open(arquivo, 'r')
    conteudo = arq.read()
    arq.close
    return conteudo
def splitclean(conteudo):
    conteudo = conteudo.split('\n')
    return conteudo
def splitponto(linha):
    return linha.split(',')
def calculainfo1(lista):
    op1 = round(float(lista[1])/1048576,2)
    op2 = round(op1/op1)
    return [lista[0],lista[1],op1,op2]
def espacoparcial(lista):
    x=0
    for i in range(len(lista)):
        x += lista[i][2]
    return x

    
def criarelatorio(arquivo, lista):
    arq = open(arquivo, 'w')
    arq.write("# \t-Usuario \t-Espaco utilizado \t-% do uso\n\n")
    arq.close
    ep = espacoparcial(lista)
    a1=round(ep*1.23,5)
    a2=round(a1/1024,1)
    a3=round(ep/1024,1)
    a4=round(ep/len(lista),2)
    
    for i in range(len(lista)):
        lista[i][3] = round(((lista[i][2]/ep)*100),2)
    aux = []   
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i][3] <lista[j][3]:
                aux= lista[i]
                lista[i] = lista[j]
                lista[j] = aux
        string = str(i+1)+"\t-"+lista[i][0]+"\t-"+str(lista[i][2])+" MB\t-"+str(lista[i][3])+"%\n"
        arq = open(arquivo, 'a')
        arq.write(string)
        arq.close
    
    arq = open(arquivo, 'a')
    arq.write("\n\nTotal do Disco inteiro:"+str(a1)+"MB("+(str(a2))+"GB)")
    arq.write("\nTotal utilizado pelos usuarios:"+str(ep)+"MB("+(str(a3))+"GB)")
    arq.write("\nTotal media utilizada:"+str(a4))
    arq.close
   
    return True
