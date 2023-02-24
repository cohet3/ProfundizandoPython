# * desempaquetar
numeros = [1,2,3]
print(numeros)
print(*numeros)
print(*numeros, sep=' - ')
# desempaquetando al momento de pasar un parámetro a una función
def sumar (a,b,c):
    print(f'Resultado suma: {a + b + c}')
sumar(*numeros)

# Extraer algunas partes de un lista
mi_lista = [1,2,3,4,5,6]
a,b,*c,d = mi_lista
print(a,b,c,d)

#Unir lista
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 =[lista1, lista2]
print(f'Lista de listas: {lista3}')
lista3 = [*lista2,*lista1,*lista2]
print(f'Unir listas: {lista3}')
# para UNIR diccionarios **
dic1= {'A':1, 'B':2, 'C':3}
dic2= {'d':3, 'f':4, 'g':5}
dic3={**dic2, **dic1}
print(f'f Unir diccionarios: {dic3}')
# Construir una lista a partir de un str
lista = [*'Hola MUndo']
print(lista)
print(*lista, sep='')