import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
from dotenv import load_dotenv
import json
import re

load_dotenv()
BASE_URL = os.getenv('BASE_URL')
book_url = urljoin(BASE_URL, 'book')
page = requests.get(BASE_URL)
soup = BeautifulSoup(page.content, 'html.parser', from_encoding="gb18030")
lb = soup.find('td', class_='ydsylb')

alphetics = lb.find_all('td', class_='sylbbt')
book_lists = lb.find_all('td', class_='ydsylb')

def create_json():
    data = []
    count = 1
    for index, alph in enumerate(alphetics):
        al_link = alph.find('a', class_='a3')
        alphabet = al_link['title']
        print(alphabet)

        book_links = book_lists[index].find_all('a')

        for link in book_links:
            # book title
            title = link['title']
            title = title[title.find('《')+1:title.find('》')]

            # book href
            href = link['href']
            if not re.search(r'\/(.*?)\/',href):
                continue
            category = re.search(r'\/(.*?)\/',href).group(1)

            #book author
            names = link.get_text().split()
            author = names[1] if len(names) > 1 else ''

            book = {'id': count; 'title': title, 'href': href, 'category': category, 'author': author, 'alphabet': alphabet, 'loaded': False}
            count += 1
            print(book)
            data.append(book)
            
    print(len(data))
    with open('books.txt', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False) 

if __name__ == '__main__': 
    create_json()