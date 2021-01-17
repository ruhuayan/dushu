import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from typing import List
import json
from ebook import Chapter, Ebook

class Download:

    def __init__(self, url):
        self.url = url
        self.books = self.get_books()

    def start(self, index = None):
        book = self.get_book(index)
        self._download(book)

        while book['id'] <= len(self.books):
            self.start(book['id'] - 1)

    def _download(self, book):
        page_url = urljoin(self.ulr, book['href'])
        page = requests.get(page_url)
        soup = BeautifulSoup(page.content, 'html.parser', from_encoding="gb18030")

        # get book description
        desc_td = soup.find('td', class_='Readme')
        book['description'] = desc_td.get_text()

        links = soup.find('td', class_='content').find_all('a')
        ebook = Ebook(title, book['author'])

        for link in links:
            print(link)

            chapter_name = link.get_text()
            page = requests.get(urllib.parse.urljoin(BASE_URL, link['href']))
            soup = BeautifulSoup(page.content, 'html.parser', from_encoding="gb18030")

            # create chapter header
            chapter = Chapter(chapter_name)

            chapter_content = get_content(soup)

            chapter.set_content(chapter_content)
            ebook.add_chapter(chapter)

        ebook.save()
        book['loaded'] = True
        self.save_books()

    def get_books(self):
        with open('books.txt', 'r', encoding='utf8') as f:
            books = json.load(f)
            return books
    
    def get_book(self, index = None):
        if index:
            return self.books[index]

        for book in self.books:
            if not book['loaded']:
                return book

    def save_books():
        with open('books.txt', 'w', encoding='utf8') as f:
            json.dump(self.books, f, ensure_ascii=False)


    def get_content(soup):
        c = BeautifulSoup()
        section = soup.find('td', class_='content')
        # remove <font></font> or <span></span>

        c.append(section)
            
        return c

