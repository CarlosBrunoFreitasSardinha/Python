
test = 'This is just a simple string.' 

x =len(test)
print(x)#29
print(test)#imprime a string normalmente
print(test[::-1])#imprime a string ao contrario
test = test.replace('simple', 'short')
print(test)#'This is just a short string.'
print(test.count('r'))
#Podemos também achar em que posição está certa levra ou palavra.
print(test.find('r'))#18
print(test[18])

print(test.split())#['This', 'is', 'just', 'a', 'short', 'string.']
#Podemos escolher o ponto a ser separado.
print(test.split('a'))#['This is just ', ' short string.']

#Para juntar nossa string separada, podemos usar o método join.
print( ' some '.join(test.split('a')))#'This is just  some  short string.'

#Podemos brincar com a caixa das letras (maiúsculo ou minúsculo). Vamos deixar tudo maiúsculo.
print(test.upper())#'THIS IS JUST A SHORT STRING.'

#Agora vamos deixar tudo minúsculo.
print(test.lower())#'this is just a short string.'

#Vamos deixar apenas a primeira letra maiúscula de uma string minúscula.
print(test.lower().capitalize())#'This is just a short string.'

#Podemos usar o método title, que deixa as letras de cada palavra da string maiúscula.
print(test.title())#'This Is Just A Short String.'

#Uma troca também é possível.O que for maiúsculo vira minúsculo e vice-versa.
print(test.swapcase())#'tHIS IS JUST A SHORT STRING.'

#Podemos rodar alguns testes numa string como ver se a string dada é totalmente maiúscula.

if 'UPPER'.isupper(): print('UPPER','is upper')
print('Is Upper:','UpPEr'.isupper())


#Do mesmo modo, podemos checar se a string dada é minúscula.
print('lower'.islower())
print('Lower'.islower())

#Checando se ela é um title, no caso, todas as palavras com a primeira letra maiúscula.
print('This Is A Title'.istitle())
print('This is A title'.istitle())

#Podemos checar se a string é alfa-numérica, ou seja, contém apenas letras e números, sem caracteres especiais.
print('aa44'.isalnum())
print('a$44'.isalnum())

#É possível checar se uma string contém apenas letras.
print('letters'.isalpha())
print('letters4'.isalpha())

#Agora checando se ela contém apenas números.
print('306090'.isdigit())
print('30-60-90 Triangle'.isdigit())

#Podemos checar se uma string contém apenas espacos.
print('   '.isspace())
print(''.isspace())

#Vamos adicionar espacos no lado direito de uma string.
print('A string.'.ljust(15))#'A string.      '

#Para adicionar espacos do lado esquerdo, o método rjust é usado.
print('A string.'.rjust(15))#'      A string.'
#O método center é usado para centralizar uma string dentro de espacos.
print('A string.'.center(15))#'   A string.   '

#Podemos separar os espacos de ambos os lados de uma string.
print('String.'.rjust(15).strip())#'String.'
print('String.'.ljust(15).rstrip())#'String.'