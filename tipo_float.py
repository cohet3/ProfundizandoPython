#profundizando tipo float
a = 3.0
# Constructor de tipo flotante recibir int y str
a = float(10)
a = float('10')
print(f'a: {a:.2f}')
#Notacion exponecial (valores positivos o negativos)
a = 3e5
a = 3e-5
print(f'a: {a:.5f}')
# Cualquier cambio que involucre un float, se promueve a float
a = 3.0 + 5
print(a)
print(type(a))