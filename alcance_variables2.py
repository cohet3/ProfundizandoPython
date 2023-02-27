# Más de funciones anidadas y alcance de varaibles

def funcion_externa():
    variable_local_externa ='Variable local externa'

    def funcion_anidada():
        variable_local_anidada= 'variable local anidada'
        nonlocal variable_local_externa
        variable_local_externa = 'Nuevo valor variable local externa'
    funcion_anidada()
    print(f'Valor varialbe local externa : {variable_local_externa}')
    # print(f'Valor variable local anidada: {variable_local_anidada}')
    # No es posible acceder a ua variable local más interna
funcion_externa()