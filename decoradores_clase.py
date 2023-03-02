# Decoradores de clase
#permiten trasformar de manera programática nuestra clase
#Es similar a los decoradores de funciones( es metapropgramacion)
import inspect


def decorador_repr(cls):
    print('Se ejecuta el decorador')
    print(f'Recibimos el objeto de la clase: {cls.__name__}')
    # Revisamos los atributos de la clase con método vars
    atributos= vars(cls)
    #iteramos cada atributo
    # for nombre, atributo in atributos.items():
    #     print(nombre, atributo)
    # Revisamos si se ha sobreescrito el método __init__
    if '__init__' not in atributos:
        raise TypeError(f'{cls.__name__} no ha sobreescrito el init')
    firma_init = inspect.signature(cls.__init__)
    print(f' Firma del metodo init: {firma_init}')
    # Recuperamos los parámetros, excepto el primero que es self
    parametros_init = list(firma_init.parameters)[1:]
    print(f'Parametros init: {parametros_init}')
    # Revisamos si cada parámetro tiene un método property asociado
    for parametro in parametros_init:
        # property es un valor de tipo built-in para preguntar si se esta utilizando el decorador property
        es_metedo_property=isinstance(atributos.get(parametro), property)
        if not es_metedo_property:
            raise TypeError(f'No existe ujn método property para el parametro indicado')
    #crear el método repr dinámicamente
    def metodo_repr(self):
        #Obtenemos el nombre de la clase
        nombre_clase = self.__class__.__name__
        print(f'Nombre clase: {nombre_clase}')
        # Obtenemos los nombres de las propiedades y sus valores dinámicamente
        #Expresion Generadora, crear nombre_atr = valor_atr
        generador_arg = (f'{nombre}={getattr(self, nombre)!r}' for nombre in parametros_init)
        # Lista del generador
        lista_arg = list(generador_arg)
        print(lista_arg)
        # Creamos la cadena a partir de la lista de argumentos
        argumentos = ' , '.join(lista_arg)
        print(f'Argumentos del método repr: {argumentos}')
        # Creamos la forma del método __repr__, sin su nombre, solo la firma
        resultado_metodo_repr= f'{nombre_clase}({argumentos})'
        print(f'Resultado método repr: {resultado_metodo_repr}')
        return resultado_metodo_repr

    # Agregar dinámicamente el método repr a nuestra clase
    setattr(cls,'__repr__', metodo_repr)
    return cls

@decorador_repr
class Persona:
    def __init__(self, nombre, apellido, edad):
        print('2.Se ejecuta el inicializador')
        self._nombre= nombre
        self._apellido= apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre
    @property
    def apellido(self):
        return self._apellido

    @property
    def edad(self):
        return self._edad
    # def __repr__(self):
    #     return  f'Persona(nombre={self._nombre, apellido={self._apellido}'

persona1 = Persona('Juan', 'alimaña',22)

print(persona1)
persona2 = Persona('Karlita', 'alimaña',25)
print(persona2)
#Tiene los métodos de propiedad nombre, apellido, repr
print(dir(Persona))
# Tiene el método repr sobreescrito
codigo_repr = inspect.getsource(persona1.__repr__)
print(codigo_repr)