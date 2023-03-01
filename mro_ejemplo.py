class Clase1:
    def __init__(self):
        print('Clase1.__init__')

    def metodo(self):
        print('Metodo clase1')
class Clase2(Clase1):
    def __init__(self):
        print('Clase2.__init__')
        super().__init__()

    def metodo(self):
        print('Metodo clase2')
        super().metodo()
class Clase3(Clase1):
    def __init__(self):
        print('Clase3.__init__')
        super().__init__()

    def metodo(self):
        print('Metodo clase3')
        super().metodo()
class Clase4(Clase2, Clase3):
    pass
    def metodo(self):
        print('Metodo clase4')
        super().metodo()

class Clase5:
    def __init__(self):
        print('Clase1.__init__')

    def metodo(self):
        print('Metodo clase1')

# Creamos objeto clase4
clase4 = Clase4()
# __bases__
print(Clase4.__bases__)
# mro
print(Clase4.__mro__)
# cual metodo es el que se ejecuta
clase4.metodo()