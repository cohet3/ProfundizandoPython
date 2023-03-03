# Leer archivo json
# JSON= JavaScript Object Notation
import json

# LEER ARCHIVO JSON

from urllib.request import Request, urlopen

# URL DE CONSULTA

URL = Request('http://globalmentoring.com.mx/api/personas.json')

# SE AGREGA UN HEADER DE LECTURA EN HTML A LA CADENA URL QUE SE CREÓ

URL.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0')

# SE HACE LA CONEXIÓN YA CON EL HEADER

respuesta = urlopen(URL)

print(respuesta)

# SE LEE EL CUERPO DE LA RESPUESTA

cuerpo_respuesta = respuesta.read()

print(cuerpo_respuesta)

# Procesamos la respuesta
json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
print(json_respuesta)
# Imprimir sólo los nombres de las personas
# JSON se convierte a listas y diccionarios en python
for persona in json_respuesta['personas']:
    print(f'Persona: {persona["nombre"]} {persona["edad"]}')
# Accedemos a las variables independientes
print(f'Total de personas: {json_respuesta["total"]}')
print(f'Mensaje: {json_respuesta["mensaje"]}')
