# Ambientacion inicial

## crear ambiente virtual
py -m venv venv

## crear alias del ambiente
alias entorno=venv/Scripts/activate

## ejecutar e iniciar ambiente
entorno

## instalar librerias y dependencias del proyecto scrapy dentro del entorno
pip install wheel
pip install scrapy
pip install autopep8

## inicializar proyecto scrapy
scrapy startproject tutorial

## probar archivo quotes_spider.py, genera la salida en resultados.html
cd tutorial/tutorial/spider
scrapy crawl quotes

==========================================
==========================================

## iniciar la consola de scrapy
scrapy shell "https://quotes.toscrape.com/"

## realizar consultas
response.xpath('//h1/a/text()').get()
response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
request.encoding
request.method
response.status
response.headers
response.body

=========================================
=========================================

# Proyecto de Scrapping a la pagina (https://quotes.toscrape.com/)

## Instalar ambiente y dependencias
mkdir quote_scrapper
cd quote_scrapper
py -m venv venv/Scripts/activate
alias entorno=venv/Scripts/activate
entorno
scrapy startproject quote_scrapper

cd quote_scrapper
- pipelines.py: permite modificar los datos desde que entran al spider (scripts que extraen información) hasta el final.
- middlewares.py: trabaja con un concepto denominado señales: controla eventos que suceden entre los requests y la captura de información.
- items.py: transforma los datos que se reciben del requests.
- _ init _.py: define que todos los archivos en la carpeta son un módulo de python.
- Folder spiders: en donde se crearan los scripts.
- settings.py: archivo con configuraciones del uso de Scrapy.
- Directorio spiders: son nuestros scripts de consultas

## ejecutar prueba metodo version parse_consola
cd quote_scrapper/quote_scrapper
scrapy crawl quotes

## ejecutar metodo parse_yeld
scrapy crawl quotes -o quotes.json

## ejecutar con parametros
scrapy crawl quotes -a top=3


==========================================
==========================================

# Proyecto Agencia de Inteligencia (https://www.cia.gov/)

## crear proyecto
scrapy startproject intelligence_agency

## analizando la pagina
scrapy shell "https://www.cia.gov/readingroom/historical-collections"
response.xpath('//a[starts-with(@href, "collection") and (parent::h3|parent::h2)]/@href').getall()

## ejecutar
cd intelligence_agency/intelligence_agency/spiders
scrapy crawl cia

## desplegar un proyecto scrapy de manera publica
https://www.zyte.com/scrapy-cloud/
scrapy cloud
start new project
seguir las instrucciones de login y subir el proyecto



