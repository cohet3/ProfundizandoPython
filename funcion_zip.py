# print(dir(__builtins__))
# help(zip)

numeros = (1,2,3)
letras = ['a','b','c','d']
identificadores = 321, 322, 324, 325
conjunto = {6,4,0,9,8,15,10}
mezcla = zip(numeros,letras, identificadores, conjunto)

# print(mezcla)
print(list(mezcla))
# print(tuple(zip(numeros, letras)))
# print(type(mezcla))

#iterar en paralelo
for numero,  letra, identificador, aleatorio in zip(numeros,letras,identificadores,conjunto):
    print(f'Número: {numero}, Letra: {letra}, Id: {identificador}, Aleatorio: {aleatorio}')

nueva_lista = []
for numero,  letra, identificador, aleatorio in zip(numeros,letras,identificadores,conjunto):
    nueva_lista.append(f'{numero}-{letra}-{identificador}-{aleatorio}')
print(nueva_lista)

# unzip
mezcla = [(1,'a'), (2,'b'),(3,'c')]
numeros , letras =zip(*mezcla)
print(f'Nuemeros {numeros}, Letras {letras}')

# ordenamiento usando zip
letras = ['c', 'd', 'a', 'e', 'b']
numeros =[3,2,4,1,0]
mezcla = zip(letras,numeros)
# sin orden
print(tuple(mezcla))
# ordenar por letra (primer iterable)
print(sorted(zip(letras,numeros)))
print(sorted(zip(numeros,letras)))

# Crear un diccionario con zip y dos iterables
llaves = ['Nombre', 'Apellido', 'Edad']
valores= ['juanito', 'Perla', 18]
diccionario = dict(zip(llaves, valores))
print(diccionario)

# Actualizar un elemento de un diccionario
llave = ['Edad']
nueva_edad = [26]
diccionario.update(zip(llave,nueva_edad))
print(diccionario)