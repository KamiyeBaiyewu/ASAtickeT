import requests
from bs4 import BeautifulSoup

def spider(max_pages):
    page = 1
    while page < max_pages:
        url = 'insert your url here' + str(page)
        source_code = requests.get(url)
        text_fmt = source_code.text
        soup = BeautifulSoup(text_fmt)
        for link in soup.findAll('a', {'class':'item-name'}):
            href = link.get(href)
            print(href)
            page += 1


def single_item_data(item_url):
    source_code = requests.get(item_url)
    text_fmt = source_code.text
    soup = BeautifulSoup(text_fmt)
    for item_name in soup.findAll('div',{'class': 'item-name'}):
        print(item_name.string)
    for link in soup.findAll('a'):
        href = "insert url here" + link.get('href')
        print(href)
spider(2)