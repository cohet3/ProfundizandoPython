# Profundizando listas
# Listas son Mutables
nombres1 = ['Juan', 'Karla', 'Pedro']
nombres2 = 'Laura Maria Gonzalo Ernesto'.split()
# Sumar listas
print(nombres1+nombres2)
# Extender una lista con otra lista
nombres1.extend(nombres2)
print(f'Extender la lista1 con la lista2: {nombres1}')
# Lista de números
numeros1 = [1,2,3,4,5,6,7,4]
#obtener el indice del primer elemento encontrado en una lista
# help(list.index)
print(f'Lista original: {numeros1}')
print(f'Indice 4: {numeros1.index(4)}')
# Invertir el orden de los elementos de una lista
numeros1.reverse()
print(f'Lista invertida: {numeros1}')
# Ordenar los elementos de una lista
numeros1.sort()
print((f'Lista ordenada: {numeros1}'))
# ordenar de manera descendente una lista
numeros1.sort(reverse=True)
print(f'Lista ordenada de manera descendente: {numeros1}')
#obtetener minimo y maximo de una lista
print(f'valor minimo: {min(numeros1)}')
print(f'valor máximo: {max(numeros1)}')

#copiar los elementos de una lista
numeros2= numeros1.copy()
# help(list.copy)
print(f'Misma referencia de memoria{numeros1 is numeros2}')
print(f'es el mismo contenido  {numeros1 == numeros2}')
# Podemos usar el constructor de la lista
numeros2 = list(numeros1)
print(f'Misma referencia de memoria{numeros1 is numeros2}')
print(f'es el mismo contenido  {numeros1 == numeros2}')
# Slicing
numeros2 = numeros1[:]
print(f'Misma referencia de memoria{numeros1 is numeros2}')
print(f'es el mismo contenido  {numeros1 == numeros2}')
# Multiplicacion listas
lista_multiplicacion = 5*[[2,5]]
print(lista_multiplicacion)
print(f'tienen la misma referencia en memoria{lista_multiplicacion[0] is  lista_multiplicacion[1]}')
print(f'es el mismo contenido  {lista_multiplicacion[1] == lista_multiplicacion[3]}')
lista_multiplicacion[2].append(10)
print(lista_multiplicacion)
# Matrices en Python (lista de listas)
matriz = [[10,20], [30,40,50],[60,70,80,90]]
print(f'matriz original{matriz}')
print(f'Renglon 0 , columna 0: {matriz[0][0]}')
print(f'Renglon 2 , columna 3: {matriz[2][3]}')
matriz[2][0]=65
print(matriz)

# Ordenar una lista de listas = [[]]
lista_listas= [[10,14,87,90,71],[4,5,6,7],[9,0,11,15,45,64,71]]
lista_listas.sort(key=len)
print(f' Ordenar lista por cantidad de elementos: {lista_listas}')
# sorted build-in
# help(sorted)
nombres1 = ['juanki','karla','Pedroo', 'djnano']
nombres1=sorted(nombres1)
print(nombres1)
# ordenar de manera desendente
nombres1=sorted(nombres1, reverse=True)
print(nombres1)
# Ordenar por la cantidad de caracteres (largo)
nombres1  = sorted(nombres1, key=len)
print(nombres1)
# build in reversed
nombres1= reversed(nombres1)
print(list(nombres1))