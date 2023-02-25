# Profundizando en diccionarios

# Los dic guardan un orden (a diferencia de un set)
dic={'Nombre': 'Juan','Apellido':'Perez','Edad':28}
print(dic)
# # Los diccionarios son mutables pero las llaves deben ser inmutables
# dic = {[1,2]:'Valor1'}
# dic = {(1,2):'Valor1'}
print(dic)
# Se agrega una llave si no se encuentra
dic['Departamento'] = 'Sistemas'
print(dic)

# No hay valores duplicados en las llaves de un diccionario (si ya existe se reemplaza)
dic['Nombre'] = 'Juan carlos'
print(dic)

# Recuperar un valor indicando una llave
print(dic['Nombre'])
# Si no encuentra la llave lanza una excepcion
# print(dic['nombre'])
# Método get recupera una llave, y si no existe No lanza excepción
#además podemos regresar un valor en caso de que no exista la llave
print(dic.get('Nombre', 'No se encontrço la llave'))
print(dic)

#  setdefault si modifica el diccionario, adeás se puede agregar un valor por default
nombre = dic.setdefault('Nombres', 'Valor por default')
print(nombre)
print(dic)


# IMprimir con pprint
from pprint import pprint as pp
# help(pp)
print(pp(dic, sort_dicts=False))