# Leer contenido online

from urllib.request import urlopen
with urlopen('http://globalmentoring.com.mx/recursos/GlobalMentoring.txt') as mensaje:
    # contenido= mensaje.read()
    contenido= mensaje.read().decode('utf-8')
    print(contenido)
#
# with open('nuevo_archivo.txt', 'w', encoding='utf-8') as archivo:
#     pass
#count metodo para contar
print('numero de veces de la palabra Universidadd: ', contenido.count('Universidad'))
#upper()lower() operador in
print(' Existe python?: ','python'.lower() in contenido.lower())

#startswith- inicia con?
print(contenido.startswith('En globalMentoring.com.mx'))
# endswith - termina con?

mensaje= 'Hola Mundo'
print(mensaje.lower().islower())
print(mensaje.upper().isupper())