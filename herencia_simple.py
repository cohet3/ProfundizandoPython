# Ejemplo de herencia simple
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