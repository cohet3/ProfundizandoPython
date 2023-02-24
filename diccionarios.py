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
#