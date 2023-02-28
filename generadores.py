# Generadores permite regresar valores poco a poco (you)
# Es una función especial, retorna una secuencia de valores
# suspende la ejecución de la función tield(producir) (no se usa return)

def generador():
    yield 1
    print('se reanuda la ejecucion')
    yield 2
    print('se reanuda la ejecucion')
    yield 3

# Consumimos el generador a demanda
gen = generador()
# Con cada llamada consumimos un valor
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))
# si tratamos de consumir más valores de los que produce el generador lanza un error de StopIteration
# consumiendo los valores del generador con un ciclo for
gen = generador()
for valor in generador():
    print(f'Número generado: {valor}')