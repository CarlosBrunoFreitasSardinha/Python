def leArquivo(arquivo):
    arq = open(arquivo, 'r')
    conteudo = arq.read()
    arq.close
    return conteudo
def DestroiArq(arquivo):
    arq = open(arquivo,'w')
    arq.write('')
    arq.close
    return True
def separaLinhas(conteudo):
    conteudo=conteudo.split('\n')
    return conteudo
def separaDados(linha):
    #linha=linha.replace('\'','')
    return linha.split(',')
def escreveArquivo(nome,linha):
    arq = open(nome,'a')
    arq.write(linha+"\n")
    arq.close
    return True
#######################################################
def calculaarea(nomearq):
    conteudo = leArquivo(nomearq)
    lista = separaLinhas(conteudo)
    DestroiArq(nomearq)
    for i in lista:
        if lista=='':
            break
        linha = separaDados(i)
        if(linha[0]=='triangulo'):
            linha.append(triangulo(linha[1],linha[2]))
            escreveArquivo(nomearq, ','.join(linha))
        elif(linha[0]=='retangulo'):
            linha.append(retangulo(linha[1],linha[2]))
            escreveArquivo(nomearq, ','.join(linha))
        elif(linha[0]=='quadrado'):
            linha.append(quadrado(linha[1]))
            escreveArquivo(nomearq, ','.join(linha))
        elif(linha[0]=='circulo'):
            linha.append(circulo(linha[1]))
            escreveArquivo(nomearq, ','.join(linha))
    return
#######################################################
def triangulo(x,y):
    return str(round(((int(x)*int(y))/2),1))
def retangulo(x,y):
    return str(round(int(x)*int(y),1))
def quadrado(x):
    return str(round(int(x)*int(x),1))
def circulo(x):
    return str(round(((int(x)^2)*3.14),1))
#######################################################
def printMaiores(nomearq):
    conteudo = leArquivo(nomearq)
    lista = separaLinhas(conteudo)
    t = r = q = c = 0.0
    for i in lista:
        if lista=='':
            break
        linha = separaDados(i)
        if(linha[0]=='triangulo' and float(linha[3])>t): t = float(linha[3])
        elif(linha[0]=='retangulo' and float(linha[3])>r): r = float(linha[3])
        elif(linha[0]=='quadrado' and float(linha[2])>q): q = float(linha[2])
        elif(linha[0]=='circulo' and float(linha[2])>c): c = float(linha[2])
        
    print("O maior triangulo tem: ",t," de area.")
    print("O maior quadrado tem: ",r," de area.")
    print("O maior retangulo tem: ",q," de area.")
    print("O maior circulo tem: ",c," de area.")
    return
#######################################################
def ordena(nomearq):
    conteudo = leArquivo(nomearq)
    lista = separaLinhas(conteudo)
    DestroiArq(nomearq)
    lista=sorted(lista)
    t = []
    r = []
    q = []
    c = []
    for i in lista:
        if lista=='':
            break
        linha = separaDados(i)
        if(linha[0]=='triangulo'): t.append(i)
        elif(linha[0]=='retangulo'): r.append(i)
        elif(linha[0]=='quadrado'): q.append(i)
        elif(linha[0]=='circulo'): c.append(i)
    
    for i in r:
       q.append(i)
    for i in t:
        q.append(i)
    for i in c:
        q.append(i)
    for i in q:
        escreveArquivo(nomearq, i)
    return True


#nome = input("Informe o nome do arquivo: ")
nome = "dados.txt"

calculaarea(nome)
ordena(nome)
printMaiores(nome)
