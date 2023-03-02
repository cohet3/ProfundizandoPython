from bs4 import BeautifulSoup
import requests

website ='https://www.infojobs.net/ofertas-trabajo/informatica-telecomunicaciones'
result = requests.get(website)
result.text
content = result.text

soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())

box = soup.findall('a', class_="script")
targeta = box.find('div').get_text()
print(targeta)
# transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
#
# with open('ofertas.txt', 'w') as file:
#     file.write(transcript)
# print(title)
# print(transcript)
# hasta aqui funciona extrayendo el html
''' Es recomendado buscar elementos en este orden.
1. ID
2.Class Name
3.Tagname, CSSselector
4. Xpath'''