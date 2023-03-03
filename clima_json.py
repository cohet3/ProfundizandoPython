# Leer archivo json
# JSON= JavaScript Object Notation
import json

# LEER ARCHIVO JSON

from urllib.request import Request, urlopen

# URL DE CONSULTA

URL = Request('http://globalmentoring.com.mx/api/clima.json')

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
# Imprimir
# Ejercicio 1 . Acceder a la descripción clima
# descripcion_clima = json_respuesta.get('clima')[0].get('description')
descripcion_clima = json_respuesta['clima'][0]['descripcion']
print(f'Descripción clima: {descripcion_clima}')
# Ejercicio 2. Mostrar la temperatura mínima y máxima
temp_min = json_respuesta.get('principal').get('temp_min')
print(f'Temperatura mínima: {temp_min}')
temp_max = json_respuesta.get('principal').get('temp_max')
print(f'Temperatura maxima: {temp_max}')
# for clima in json_respuesta['principal']:
#     print(f'Persona: {clima["description"]}')
# # Accedemos a las variables independientes
# print(f'Clima: {json_respuesta["description"]}')
# for principal in json_respuesta['clima']:
#     print(f'Temperatura principal: {principal["temp_min"]} {principal["temp_max"]}')

