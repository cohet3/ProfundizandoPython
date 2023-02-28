# Ejemplo atributos públicos, protegidos, privados

class MiClase:
    def __init__(self, publico, protegido, privado):
        self.publico = publico
        self._protegido = protegido
        self.__privado= privado

objeto = MiClase('Valor público','valor protegido', 'valor privado')
# Acceso al atributo público
print(objeto.publico)
# Modificar el valor público
objeto.publico = 'Nuevo valor público'
print(objeto.publico)
# Acceso al valor protegido
# Solo dentro de la misma clase o clases hijas
print(objeto._protegido)
# modificar atributo protegido
objeto._protegido = 'Nuevo valor protegido'
print(objeto._protegido)

# Acceder al atributo privado
# print(objeto.__privado)
# Pero, convierte: objeto._clase__atributo_privado
print(objeto._MiClase__privado)
# recordemos que para ello debemos usar decoradores @property y @setter.nombre_propiedad
objeto._MiClase__privado = 'Nuevo valor privado'
print(objeto._MiClase__privado)