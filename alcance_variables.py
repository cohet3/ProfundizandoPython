# Alcance de Variables (scope)

var_global= 'Variable global'
def imprimir():
    # Acceder a una variable global
    global var_global
    print(f'Variable global desde función :{var_global}')
    #definicion de variable local
    var_local= 'Variables local'
    print(f'Variable local desde función: {var_local}')
    def funcion_anidada():
        print(f'Variable local desde función anidada: {var_local}')
    funcion_anidada()
    var_global = 'Nuevo Valor'
imprimir()
print(f'Variable global desde función :{var_global}')
# print(f'Variable local desde función: {var_local}')
# No es popsible acceder a variables localas fuera del bloque donde se definieron
