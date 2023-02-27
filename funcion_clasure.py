
# Un closure es una función que define a otra , y ademas la regresa.
#la función anidada puede acceder a las variables locales definidas en la función principal o externa

# Función principal
# def operacion(a,b):
#     #1.definimos una funcion interna o anidada
#     def sumar():
#         return a+b
#     #2.Retornar la funcion
#     return sumar
# Función principal
def operacion(a,b):
    #1. Definimos una función lambda interna o anidada y la retorna en la misma linea de codigo
    return lambda: a+b

mi_funcionh_closure = operacion(5,2)
print(f'Resultado de la función closure: {mi_funcionh_closure}')
# Llamar la función regresada al vuelo
print(f'Resultado de la función closure al vuelo: {operacion(2,3)()}')