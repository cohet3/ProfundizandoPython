# Ejemplo de herencia siple
class ListaSimple:
    def __init__(self, elementos):
        self._elementos = list(elementos)
    def agregar(self, elemento):
        self._elementos.append(elemento)
    def __getitem__(self, indice):
        return self._elementos[indice]
    def ordenar(self):
        self._elementos.sort()
    def __len__(self):
        return len(self._elementos)
    def __repr__(self):
        return f'{self.__class__.__name__}({self._elementos!r})'

lista_simple = ListaSimple([5,3,6,8])
print(lista_simple)

class ListaOrdenada(ListaSimple):
    def __init__(self, elementos=[]):
        super().__init__(elementos)
        #Ordenamos siempre los elementos una vez inicializados
        self.ordenar()
    def agregar(self, elemento):
        super().agregar(elemento)
        # Ordenamos el nuevo elemento
        self.ordenar()
    # Esta lista solo acepta numeros
class ListaEnteros(ListaSimple):
    def __init__(self, elementos=[]):
        for elemento in elementos:
            self._validar(elemento)
            #Una vez validados los elementos, los agregamos a la poadre
            super().__init__(elementos)
    def _validar(selfself,elemento):
        #Validamos si el elemento es de tipo entero
        if not isinstance(elemento, int):
            raise ValueError(f'No es un valor entero: {elemento}')
    # Sobreescribimos el método agregar de la clase padre
    def agregar(self, elemento):
        self._validar(elemento)
        # Una vez validado lo agregamos a la lista
        super().agregar(elemento)
# Lista de Enteros Ordenada ---HERENCIA MULTIPLE----
class ListaEnterosOrdenada(ListaEnteros, ListaOrdenada):
    pass
# Lista simple
lista_simple = ListaSimple([5, 3, 6, 8])
print(lista_simple)
# Lista ordenada
lista_ordenada = ListaOrdenada([4,3,6,9,10,-1])
print(lista_ordenada)
lista_ordenada.agregar(-12)
print(lista_ordenada)
print(len(lista_ordenada))
# Lista de enteros
lista_enteros = ListaEnteros([-2,1,2,3])
print(lista_enteros)
# Lista enteros ordenada
lista_enteros_ordenada = ListaEnterosOrdenada([4,5,-1,10,14,-4])
print(lista_enteros_ordenada)
lista_enteros_ordenada.agregar(-20)
print(lista_enteros_ordenada)
# Saber las clases padre y su orden
print(ListaEnterosOrdenada.__bases__)
# MRO (Method Resolution Order)
print(ListaEnterosOrdenada.__mro__)
# isinstance regresa verdadero o falso
print('Es entero?', isinstance(10, int))
print('Es cadena?', isinstance('hola', str))
print('Es lista de ent ord?', isinstance(lista_enteros_ordenada, ListaEnterosOrdenada))
print('Es lista ent?', isinstance(lista_enteros_ordenada, ListaEnteros))
print('Es una lista ordenada', isinstance(lista_enteros_ordenada, ListaOrdenada))
print('Es lista simple?', isinstance(lista_enteros_ordenada, ListaSimple))
print('Es object', isinstance(lista_enteros_ordenada, object))
print('Es de varios tipos?', isinstance(lista_enteros_ordenada, (ListaEnteros,ListaSimple)))