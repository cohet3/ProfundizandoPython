# Funciones Lambda
# son funciones anónimas, y son pequeñas ( una línea de código)
# No es posible asignar una funcion a una variable
# mi_funcion = def sumar(a, b): return a+b

# Con una funcion lambda( anónima, sin nombre y una sola línea de código
# NO se necesita agregar paréntesis para los parámetros
# No se necesita usar la palabra return, pero si debe regresar una expresión
mi_fuincion_lambda  = lambda a,b: a+b

resultado= mi_fuincion_lambda(4,6)
print(f'Resultado sumar con función lambda: {resultado}')
# Función lambda que no recibe argumentos (debemos regresar una expresión valida)
mi_fuincion_lambda= lambda: 'Función sin argumentos'
print(f'Llamar función lambeda sin argumentos: {mi_fuincion_lambda}')

# Función lambda con paramatros default
mi_fuincion_lambda= lambda  a =2, b=3: a+b
print(f'Resultado argumentos por default: {mi_fuincion_lambda}')

# Función lambda con argumentos variables *args y **kwargs
mi_fuincion_lambda = lambda *args,**kwargs: len(args)+len(kwargs)
print(f'Resultado argumentos variables:{mi_fuincion_lambda(1,2,3,a=5,b=6)}')

# Funciones lambda con argumentos, argumentos variables y valores por default
mi_fuincion_lambda = lambda a,b,c=3,*args,**kwargs: a+b+c+len(args)+len(kwargs)
print(f'Resultado función lambda: {mi_fuincion_lambda(1,2,4, 5,6,7,e=5,f=7 )}')