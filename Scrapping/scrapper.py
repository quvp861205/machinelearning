import requests
import lxml.html as html
import os 
import datetime

HOME = 'https://www.larepublica.co/'
XPATH_LINK = '//a[@class="globoeconomiaSect"]/@href'
XPATH_TITLE = '//h2/span/text()'
XPATH_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_CONTENT = '//div[@class="html-content"]/p[not(@class)]/text()'

def parse_home():
    try:
        response = requests.get(HOME)
        if response.status_code==200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            noticias = parsed.xpath(XPATH_LINK)
            print(noticias)

            today = datetime.date.today().strftime('%Y%m%d')
            if not os.path.isdir(today):
                os.mkdir(today)

            for link in noticias:
                parse_noticia(link, today)
                pass
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def parse_noticia(link, today):
    
    try:
        response = requests.get(link)
        if response.status_code==200:
            noticia = response.content.decode('utf-8')
            
            parsed = html.fromstring(noticia)
           
            try:

                title = parsed.xpath(XPATH_TITLE)[0]
                title = title.replace('\"','')
                print(title)

                
                summary = parsed.xpath(XPATH_SUMMARY)[0]
                body = parsed.xpath(XPATH_CONTENT)

                
            except IndexError:
                return

            with open(f'{today}/{title}.txt', 'a', encoding='utf-8') as f:
                f.write(title.upper())
                f.write('\n\n')
                f.write(summary)
                f.write('\n\n')
                for p in body:
                    f.write(p)
                    f.write('\n')

            #print(noticias)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def run():
    parse_home()

if __name__=='__main__':
    run()