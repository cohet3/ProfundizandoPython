# Decoradores
# un Decorador es una funcion que recibe una funcion y regresa otra
# lo utiliozaremos para extender funcionalidad
#1. funcion decorador (a)
#2. funcion a decorar (b)
#3. funcion decorada (c)
def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c(*args,**kwargs):
        print('antes de ejecutar la funcion_decorada_c')       # funcion_a_decorar_b()
        resultado = funcion_a_decorar_b(*args,**kwargs)
        print('Despues de ejecutar la función_decorada_c')
        return resultado
    return funcion_decorada_c
# @funcion_decorador_a
'''def mostrar_mensaje():
    print(f'hola desde funcion mostrar_mensaje')

mostrar_mensaje()
@funcion_decorador_a
def imprimir():
    print('Hola desde función imprimir')
imprimir()'''
@funcion_decorador_a
def sumar(a, b):
    return a+b
resultado = sumar(5,6)
print(f'Resultado de la suma:  {resultado}')