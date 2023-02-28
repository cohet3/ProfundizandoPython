# Generador de números del 1 al 5:
def generador_numeros():
    for numero in range(1,6):
        yield numero
        print('Se reanuda la ejecución de la función')

#Utlizamos el generador
generador= generador_numeros()
print(f'Obejto generador: {generador}')
print(type(generador))
# consumimos los valores del generador
for valor in generador:
    print(f'Número porducido: {valor}')

#consumir a demanda
generador = generador_numeros()
try:
    print(f'consumimos a demanda: {next(generador)}')
    print(f'consumimos a demanda: {next(generador)}')
    print(f'consumimos a demanda: {next(generador)}')
except StopIteration as e:
    print(f'Error al consumir generador {e}')

# Otra forma de consumir un generador
generador = generador_numeros()
while True:
    try:
        valor = next(generador)
        print('Impresión valor generado: {valor}')
    except StopIteration as e:
        print('Se termino de iterar el generador')
        break