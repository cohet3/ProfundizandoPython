# boll contine los valores True y False
# Tipos númericos, False para 0 , True para los demas valores

valor = 0
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')
valor = 15
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

#Tipo str, False para '', True demás valores
valor = ''
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')
valor = 'hola'
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

#Tipo colecciones, False para colecciones vacioas, True para todas las demas colecciones
# Lista
valor = []
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')
valor = [2,3,4]
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')
#Tupla
valor = ()
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')
valor = (2,3,4)
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')
#Diccionario
valor = {}
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')
valor = {'nombre': 'Juan', 'apellido': 'Perez'}
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')
if bool((1,2)):
    print('regreso verdadero')
else:
    print('regreso falso')
variable=1
if variable:
    print('regreso verdadero')
else:
     print('regreso falso')

while variable:
    print('ejecucuin ciclo while')
    break
else:
    print('regreso falso')