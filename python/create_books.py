import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
from dotenv import load_dotenv
import re
from connection import Connection

load_dotenv()
BASE_URL = os.getenv('BASE_URL')
book_url = urljoin(BASE_URL, 'book')
page = requests.get(BASE_URL)
soup = BeautifulSoup(page.content, 'html.parser', from_encoding="gb18030")
lb = soup.find('td', class_='ydsylb')

alphetics = lb.find_all('td', class_='sylbbt')
book_lists = lb.find_all('td', class_='ydsylb')

def create_books():
    books = []
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

            # (title, href, author, category, alphabet, description)
            book = (title, href, author, category, alphabet)
            books.append(book)
    
    conn = Connection(os.getenv('DB_HOST'), os.getenv('DB_USER'), os.getenv('DB_PASSWORD'), os.getenv('DB'))
    conn.connect()
    conn.insert_books(books)
    conn.close()

if __name__ == '__main__': 
    create_books()