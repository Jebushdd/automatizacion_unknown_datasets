# Importamos las librerías
from bs4 import BeautifulSoup
import requests
import re
import webbrowser

# Proceso de web scraping
url_unknown_datasets = 'https://linktr.ee/unknow.datasets'
r = requests.get(url_unknown_datasets)
contenido = r.text
soup = BeautifulSoup(contenido,'lxml')
clase_html = 'sc-hKgILt sc-eggNIi cxwgnw lbgaqu'
titulos = soup.find_all('p', attrs={'class':clase_html})

#Link al perfil de Cafecito
buscar_cafecito = re.compile(r'.*cafecito.*')
atributos_cafecito = {'href':buscar_cafecito}
elemento_html = soup.find('a', attrs=atributos_cafecito)
link_cafecito = elemento_html['href']

#Diccionario de datasets a exportar
diccionario = {}
for dataset in titulos:
    elemento_html = soup.find('p', string=dataset.text)
    buscar_excel = re.compile(r'.*docs\.google\.com.*')
    atributos_excel = {'href':buscar_excel}
    try:
        link_dataset = elemento_html.find_parent('a',attrs=atributos_excel)['href']
        nombre_dataset = dataset.text.strip()
        diccionario[nombre_dataset] = link_dataset
        print(f'Dataset encontrado: {nombre_dataset}')
    except TypeError:
        link_fallido = elemento_html.find_parent('a')['href']
        print(f'{link_fallido} no es un dataset')
        continue

#Exportacion de archivos
for dataset in list(diccionario.keys()):
    dataset_id = diccionario[dataset].split('/d/')[1].split('/edit')[0]
    link_descarga = f'https://docs.google.com/spreadsheets/d/{dataset_id}/export?format=xlsx'
    response = requests.get(link_descarga)
    if response.status_code == 200:
        xlsx_data = response.content
        nombre_salida = dataset.strip('.xlsx')
        with open(f'{nombre_salida}.xlsx', 'wb') as archivo:
            archivo.write(xlsx_data)
        print(f'{nombre_salida} exportado correctamente')

#Agradecer con un cafecito
webbrowser.open(link_cafecito,autoraise=True)
