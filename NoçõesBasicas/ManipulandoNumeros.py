print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 ** 3)
print(3 ** 2)

print('#####################1#########################')
quociente = 7 // 3  # divisão inteira
print(quociente)
resto = 7 % 3
print(resto)
print('######################2########################')
print(3.14, int(3.14))
print(3.9999, int(3.9999))       # Isto não arredonda para o inteiro mais próximo de zero
print(3.0,int(3.0))
print(-3.999,int(-3.999))        # Observe que o resultado está mais próximo de zero
print('######################3########################')
print("2345",int("2345"))        # examina uma string para produzir um int
print(17,int(17))                # int também funciona sobre inteiros

print(int("23"))
print('#######################4#######################')
print(float("123.45"))
print(type(float("123.45")))
print('#######################5#######################')
print(str(17))
print(str(123.45))
print(type(str(123.45)))