from dataclasses import dataclass
from typing import ClassVar

@dataclass(eq=True, frozen=True)
class Domicilio:
    calle: str
    numero: int = 0
@dataclass(eq=True, frozen=True)
class Persona:
    nombre: str
    apellido: str
    contador_personas: ClassVar[int]= 0
    domicilio: Domicilio
    def __post_init__(self):
        if not self.nombre:
            raise ValueError(f'Valor nombre vacio: {self.nombre}')

domicilio1= Domicilio('SAturno', 15)
persona1 = Persona('juanito', 'alimaña', domicilio1)
print(f'{persona1!r}')
# Variable de clase
print(f'Variable de clase: {Persona.contador_personas}')
# variables de instancia
print(f' Variable de instancia: {persona1.__dict__}')
# Variable con valores vacíos
persona_vacia = Persona('karla','',None)
print(f'Persona vacia: {persona_vacia}')
# Revisar igualdad entre objetos ( __eq__)
persona2 = Persona('juanito','alimaña', domicilio1)
print(f'Objetos iguales?:{persona1==persona2} ')
# Agregar esta clase a una colección
coleccion = {persona1, persona2}
print(coleccion)
# coleccion[0].nombre = 'Juanki'
