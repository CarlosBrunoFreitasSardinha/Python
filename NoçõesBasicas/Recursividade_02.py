def fat(n):
    if n==0 or n ==1: return 1
    else: return n*fat(n-1)
def mult(x, y):
    if y==0 or x ==0: return 0
    elif x ==1: return y
    else: return valor + mult(x-1, y)
def exp(x, y):
    if x == 0 and y==0: return "indeterminado!"
    elif y == 0: return 1
    elif y == 1: return x
    else: return x * exp(x , y-1)
def fibonacci(quant):
    if quant==0 or quant==1: return 1
    elif quant == 2: return 2
    elif quant == 3: return 3
    elif quant == 4: return 5
    elif quant == 5: return 8
    elif quant == 6: return 13
    elif quant == 7: return 21
    elif quant == 8: return 34
    elif quant == 9: return 55
    elif quant == 10: return 89
    elif quant == 11: return 144
    elif quant == 12: return 233
    elif quant == 13: return 377
    elif quant == 14: return 610
    elif quant == 15: return 987
    elif quant == 16: return 1597
    elif quant == 17: return 2584
    elif quant == 18: return 4181
    elif quant == 19: return 6765
    elif quant == 20: return 10946
    else: return fibonacci(quant-1)+ fibonacci(quant-2)
valor = 5
x=2
y=50
print()
print(valor, " Valor: ", fat(valor))
print(x, " multiplicado por ", y, " = ", mult(x,y))
print(x, " elevado ", y, " = ", exp(x,y))
print(" fibonacci ", y, " = ", fibonacci(y))