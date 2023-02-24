# Profundizar en set
# Un set es una colección de elementos únicos y es mutable
# Los elementos de un set deben ser inmutables
# conjunto = {[1,2],[3,4]}
conjunto = {'Juan', True, 18.0}
print(conjunto)
# set vacio
# conjunto = {} genera un dict vacío
# print(type(conjunto))
# set vacio correcto
conjunto = set()
print(conjunto)
print(type(conjunto))
conjunto.add('Juanitoo')
print(conjunto)
# Contiene valores únicos
conjunto.add('Juanitoo')
print(conjunto)
# Crear un set a partir de un iterable
conjunto = set([4,5,7,8,4])
print(conjunto)
# Podemos agregar más elementos on incluso otro set
conjunto2 = {100,200,300,400}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20,30,40,40])
print(conjunto)
# Copiar un set ( copia poco profunda, solo copia las referencias)
conjunto_copia = conjunto.copy()
print(conjunto_copia)
# Verificar la igualdad
print(f' Es igual en contenido?:{conjunto == conjunto_copia}')
print(f' Es la misma referencia?:{conjunto is conjunto_copia}')


# Operaciones de conjuntos con set
# personas con distintas características

# union= se unen todos los elementos de ambos sets
pelo_negro = {'Juan', 'Karla', 'Pedro', 'Maria'}
pelo_rubio = {'Lorenzo', 'Laura', 'Marco'}
ojos_cafe = {'Karla','Laura'}
menores_30={'Juan', 'Karla','Maria'}
# Todos con ojos_cafe y pelo rubio (Union) ( no se repiten los elementos)
print(ojos_cafe.union(pelo_rubio))
#  union Invertir el orden con el mismo resultado (conmutativa)
print(pelo_rubio.union(ojos_cafe))
# intersection se unen solo los elementos que esten en comun (conmutativa). Solo las personas con ojos cafe y pelo rubio
print(ojos_cafe.intersection(pelo_rubio))
# difference solo regresa los q sean distintos de un solo conjunto los q son iguales los excluye.
# Pelo negro sin ojos cage(no es conmutativa)
print(pelo_negro.difference(ojos_cafe))
# Symmetric Difference se recuperan los q esten en a o b sin q se repitan.
#Pelo negro y ojos cafe, pero no ambos (conmutativa)
print(pelo_negro.symmetric_difference(ojos_cafe))
# Preguntar si un set esta contenido en otro (subset)
# revisamos si los elementos del primer set estan contenidos en el segundo set
print(menores_30.issubset(pelo_negro))
# Preguntar si un set contiene a otro set(superset)
#revisar si los elementos del primer set estan contenidos en el segundo set
print(pelo_negro.issuperset(ojos_cafe))
# Preguntar si los de pelo negro no tienen pelo rubio
print(pelo_negro.isdisjoint(pelo_rubio))