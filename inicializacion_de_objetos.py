# Orden de inicializacion de objetos
class Padre:
    def __init__(self):
        print('Inicializador Padre')

    def metodo(self):
        print('metodo padre')


class Hijo(Padre):
    # se manda a llamar el metodo __init__ de la clase padre,
    # siempre y cuando la clase no defina su propio metodo init

    # Definimos el metodo init
    def __init__(self):
        # de manera opcional podemos llamar al metodo __init de la clase padre(super)
        print('Inicializado hijo')
        super().__init__()

    # Sobreescribimos el metodo heredaddo de la clase padre
    def metodo(self):
        print('Metodo sobreescrito hijo')
        super().metodo()


# padre1=Padre()
# padre1.metodo()
hijo1 = Hijo()

hijo1.metodo()
