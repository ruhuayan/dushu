import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from ebook import Chapter, Ebook
from connection import Database, BASE_URL
import re

class Download:

    def __init__(self):
        pass
        # self.db = Database()

    def start(self):
        if not self.db.connection:
            self.db.connect()

        while True:
            book = self.db.get_unloaded_book()
            if not book:
                print('No unloaded book found')
                return

            desc = self._download(book)

            # insert chpaters
            chapter_records = list(book)
            self.db.insert_chapters(chapter_records)

            self.db.set_book_loaded(book['id'])

    def _download(self, book) -> str:
        page_url = urljoin(BASE_URL, book['href'])
        print(page_url)
        page = requests.get(page_url)
        soup = BeautifulSoup(page.content, 'html.parser', from_encoding="gb18030")

        # get book description
        desc_td = soup.find('td', class_='Readme')
        description = desc_td.get_text()

        links = soup.find('td', class_='content').find_all('a')
        ebook = Ebook(book['id'], book['title'], book['author'])

        for link in links:
            print(link)

            chapter_name = link.get_text()
            page = requests.get(urljoin(BASE_URL, link['href']))
            soup = BeautifulSoup(page.content, 'html.parser', from_encoding="gb18030")

            # create chapter header
            chapter = Chapter(chapter_name)

            chapter_content = self.get_content(soup)

            chapter.set_content(chapter_content)
            ebook.add_chapter(chapter)

        ebook.save()
        return description

    def get_content(self, soup: BeautifulSoup) -> BeautifulSoup:
        c = BeautifulSoup()
        section = soup.find('td', class_='content')
        
        # change section tag name
        for attribute in ["class", "colspan"]:
            del section[attribute]
        section.name = 'div'

        #remove span & font
        for span in section.find_all('span'):
            span.replace_with("%s" % span.text)

        for font in section.find_all('font'):
            font.replace_with("%s" % font.text)

        #remove attributes
        for tag in section.findAll(True):
            for attribute in ["class", "id", "style"]:
                del tag[attribute]

        c.append(section)
        return c

download = Download()
book = {"id": 3, "title": "沉船", "href": "/waiguomingzhu/chenchuan/", "category": "waiguomingzhu", "author": "泰戈尔", "alphabet": "C"}
desc = download._download(book)
print(desc)

