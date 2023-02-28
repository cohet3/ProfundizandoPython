# Simulación de sobrecarga de constructores en python
# esto nos permite agregar otras formas de crear objetos
class Persona:
    def __init__(self, nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    @classmethod
    def crear_persona_vacia(cls):
        return cls(None, None)
    @classmethod
    def crear_persona_con_valores(cls,nombre,apellido):
        return cls(nombre, apellido)
    def __str__(self):
        return f'Nombre: {self.nombre}, apellido: {self.apellido}'

persona1 = Persona('JUanito', 'Alimaña')
print(persona1)
persona_vacio = Persona.crear_persona_vacia()
print(persona_vacio)
persona_con_valores = Persona.crear_persona_con_valores('Karla','Gomez')
print(persona_con_valores)