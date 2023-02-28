# Expresión generadora ( es un generador anónimo)

multiplicacion = (valor*valor for valor in range(4))

print(type(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
# print(next(multiplicacion))

# también se puede parar una expresión generadora a una función (sin paréntesis)
suma = sum(valor*valor for valor in range(4))
print(f' Resultado suma:{suma}')

# También podemos utilizar una lista o cualquier otro iterador
lista = ['Juan','Perez']
generador =(valor for valor in lista)
print(next(generador))
print(next(generador))

# Crear un str a partir de un generador y este generador es creado a partir de una lista
lista = ['Karla', 'Gomez', 22]
contador = 0
def incrementar():
    global contador
    contador += 1
    return contador
# La primera parte es el yield y la segunda es el for, entre parentesis
generador = (f'{incrementar}. {nombre}' for nombre in lista)
lista = list(generador)
print(lista)
cadena= ','.join(lista)
print(f' Cadena generada: {cadena}')