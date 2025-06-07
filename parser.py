from bs4 import BeautifulSoup
import requests
import os
import json

with open('config.json', 'r', encoding='utf-8') as config_url:
    web_url = json.load(config_url)

for url_key, url_site in web_url.items():
    website = requests.get(url_site)

    if not website.ok:
        print('Ничего не работает')
    else:
        if not os.path.isfile(f'{url_key}.html'):
            print(f'[WRITE] Название: {url_key}, Сайт: {url_site}')
            with open(f'{url_key}.html', 'w', encoding='utf-8') as site_html:
                site_html.write(website.text)
        else:
            print(f'[SUCCESS] Название: {url_key}, Сайт: {url_site}')