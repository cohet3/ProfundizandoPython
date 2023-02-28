# Representación de objetos (str, repr, format)
# print(dir(object))

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre= nombre
        self.apellido= apellido

    # repr, más enfocado a los desarrolladores
    def __repr__(self):
        return f'{self.__class__.__name__}(nombre:{self.nombre}, apellido:{self.apellido})'
    # str es más para el ususario final u otros sitemas
    #la implementación por default llama al método repr
    def __str__(self):
        return f'{self.__class__.__name__}: {self.nombre} {self.apellido}'
    #format su implementación por defult es str
    # Y se manda a llamar al usar f-string
    def __format__(self, format_spec):
        return f'{self.__class__.__name__} con nombre{self.nombre} y apellido {self.apellido}'
persona1= Persona(nombre='JUanito', apellido='maraña')
# repr
print(f'Mi objeto persona1: {persona1!r}')
# str (automáticamente print llama al método str
print(persona1)
#format
print(f'{persona1}')