# Funciones Anidadas

def calculadora( a, b, operacion='sumar'):
    #1.Funcón anidada
    def sumar(a,b):
        return a+b
    def restar(a,b):
        return a -b
    #2. llamamos a la función anidada
    if operacion == 'sumar':
       print(f'Resultado de la suma: {sumar(a, b)}')
    elif operacion == 'restar':
       print(f'Resultado de la resta: {restar(a,b)}')

calculadora(5,7, operacion='restar')
calculadora(8,2)
