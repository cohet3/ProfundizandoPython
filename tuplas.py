# Profundizando en tuplas

#Declarar variables
a,b = 'hola', 'Adios'
print(a,b)
# swap(intercambio)
a,b = b,a
print(a,b)

# Regresar múltiples valores en una función
def minmax(elementos):
    return min(elementos), max(elementos)
min, max = minmax([1,2,3,4,5])

print(f'valor min: {min}, valor de max: {max}')

# Regresa la suma de una tupla
resultado = sum((1,2,3,4,5))
print(f'Resultado {resultado}')
def sumar(*args):
    return sum(args)
resultado = sumar(5,6,7,8,9)
print(f'Resultado : {resultado}')