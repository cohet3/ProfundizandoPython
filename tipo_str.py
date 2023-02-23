# PROFUNDIZANDO EN EL TIPO STR

# Concatenacion automática en python
# variable = 'Adios'
# mensaje = 'Hola' 'Mundo'+variable
# mensaje += 'Universidad' 'Python'
# print(mensaje)
# import math
# help(math)
#
# from mi_clase import MiClase
#
# # help(MiClase)
#
# print(MiClase.__doc__)
# print(MiClase.__init__.__doc__)
# print(MiClase.mi_metodo.__doc__)
# print(MiClase.mi_metodo)
# print(type(MiClase.mi_metodo()))


# help(str.capitalize)

# mensaje1= 'hola Mundo'
# mensaje2 = mensaje1.capitalize()
# print(f'{mensaje2}, id:{id(mensaje1)}')
# print(mensaje1)
# mensaje1 += 'adios'
# print(mensaje1)


# help(str.join)
#
# tupla_str= ('Hola', 'Mundo', 'joe', 'python')
# mensaje = '  '.join(tupla_str)
# print(f'mensaje: {mensaje}')
#
# lista_cursor = ['Java', 'python', 'Angular', 'Spring']
# mensaje = ', '.join(lista_cursor)
# print(f'mensaje: {mensaje}')
#
# cadena = 'HolaMundo'
# mensaje= '.'.join(cadena)
# print(f'mensaje: {mensaje}')
#
# diccionario = {'nombre': 'Juan', 'apellido': 'Perez', 'edad':'18'}
# llaves = '-'.join(diccionario.keys())
# valores = '-'.join(diccionario.values())
# print(f'llaves: {llaves}, type: {type(llaves)}')
# print(f'valores: {valores}, type: {type(valores)}')

# help(str.split)
# cursos= 'Java Python JavaScript Anguñar Spring Excel'
# lista_cursos = cursos.split()
# print(lista_cursos)
# print(type(lista_cursos))
# cursos_separados_por_coma= 'Java,Python,JavaScript,Anguñar,Spring,Excel'
# lista_cursos=cursos_separados_por_coma.split(',',2)
# print(lista_cursos)
# print(len(lista_cursos))

#dar formato a un str
# mensaje_con_formato = 'Mi nombre es %s y tengo %d años '%(nombre,edad)
# print(mensaje_con_formato)
#
# persona=('Karla', 'Gomez', 5000.00)
# mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f'
# print(mensaje_con_formato%persona)
# nombre = 'Juanito'
# edad = 2
# sueldo= 3000
# mensaje = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre, edad, sueldo)
# # print(mensaje)
# mensaje = 'Nombre{0} Edad {1} Sueldo{2:.2f}'.format(nombre, edad, sueldo)
# # print(mensaje)
# mensaje = 'Sueldo{2:.2f} Nombre{0} Edad {1} '.format(nombre, edad, sueldo)
# # print(mensaje)
# mensaje = 'Nombre {n} Edad {e} Sueldo {s:.2f}'.format(n=nombre, e=edad, s=sueldo)
# # print(mensaje)
#
# diccionario= {'nombre': 'Ivan', 'edad':35, 'sueldo': 8000.00}
# mensaje='Nombre {persona[nombre]} Edad {persona[edad]} Sueldo{persona[sueldo]}'.format(persona=diccionario)
# print(mensaje)

#Método print
# nombre = 'Juanito'
# edad = 2
# sueldo= 3000
# print(nombre, edad, sueldo, sep=', ')

# #multiplicacion str
# resultado = 5*'Hola'
# print(f'Resultado: {resultado}')
#
# # multiplicación tuplas
# resultado = 5*('hola','Mundo', 33)
# print(f'Resulltado: {resultado}')
#
# #multiplicación listas
# resultado= 10*[0]
# print(f'Resulltado: {resultado}, largo {len(resultado)}')

# caracteres de escape
# resultado = 'Hola \'Mundo'
# print(f' Resultado:{resultado}')
#
# resultado =  'Se va a eliminar el punto.\b\b'
# print(resultado)
# # Caracter \
# resultado = 'c:\\nuevo\\juan'
# print(f' Resultado:{resultado}')
# #raw string
# resultado= r'Cadena con \n salto de linea'
# print(f' Resultado: {resultado}')

# CARACTERRES UNICODE
# print('Hola\u0020mundo')
# print(f'Notacion simple:', '\u0041')
# print('Notacion extendida:','\U00000041')
# print('Notacion hexadecimal', '\x41')
#
# print('Corazon:', '\u2665')
# print('Cara sonriendo:', '\U0001f600')
# print('Python: ', '\U0001f40D')
#
# # CARACTERES ASCII
# caracter = chr(65)
# print(f'A mayuscula:{caracter}')
# caracter = chr(4578)
# print(f'simbolo @:{caracter}')

# #caracteres_en_bytes
# caracteres_en_bytes = b'Hola mundo'
# print(caracteres_en_bytes)
# mensaje= b'Universidad Python'
# print(mensaje[0])
# print(chr(mensaje[0]))
# lista_caracteres = mensaje.split()
# print(lista_caracteres)

# Convertir str a bytes
string = 'Programación con python'
print('string original:', string)
bytes = string.encode('UTF-8')
print('bytes codificado:', bytes)
#convertir de bytes a str
string2 = bytes.decode('UTF-8')
print('string decodificado:', string2)
print(string == string2)