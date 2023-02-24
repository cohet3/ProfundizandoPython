# # Leer contenido online
#
# from urllib.request import urlopen
# with urlopen('http://globalmentoring.com.mx/recursos/GlobalMentoring.txt') as mensaje:
#     # contenido= mensaje.read()
#     contenido= mensaje.read().decode('utf-8')
#     print(contenido)
# #
# # with open('nuevo_archivo.txt', 'w', encoding='utf-8') as archivo:
# #     pass
# #count metodo para contar
# print('numero de veces de la palabra Universidadd: ', contenido.count('Universidad'))
# #upper()lower() operador in
# print(' Existe python?: ','python'.lower() in contenido.lower())
#
# #startswith- inicia con?
# print(contenido.startswith('En globalMentoring.com.mx'))
#
# # endswith - termina con?
# mensaje= 'Hola Mundo'
# print(mensaje.lower().islower())
# print(mensaje.upper().isupper())

# Alinear cadenas
#center - Centrar un str
titulo='Sitio web de GlobalMentoring.com.mx'
# print(len(titulo))
# print(titulo.center(50,'*'))
# print(len(titulo.center(50, '*')))
print(titulo.center(len(titulo)+10,'-'))
#ljust - alinea a la izquierda
print(titulo.ljust(50,'*'))
print(titulo.ljust(len(titulo)+10,'-'))
#rjust - a la derecha
print(titulo.rjust(50,'*'))
print(titulo.rjust(len(titulo)+22,'/'))

# Reemplazar contenmido en un str
contenido = 'Hola mundo'
print(contenido.replace(' ','-'))

# Eliminar caracterres al inicio y final de una str -strip
titulo= ' *** GoboDaniel.com *** '
print(f'cadena original',titulo, len(titulo))
titulo = titulo.strip()
print(f'cadena modificada',titulo, len(titulo))
titulo= '***GoboDaniel.com***'.strip('*')
print(titulo)
titulo= '***GoboDaniel.com***'.lstrip('*')
print(titulo)
titulo= '***GoboDaniel.com***'.rstrip('*')
print(titulo)

titulo=' *** GlobalMentoring.com.mx *** '.strip().strip('*').strip()
print(titulo)
