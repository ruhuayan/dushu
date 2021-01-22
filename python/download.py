import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from typing import List
from ebook import Chapter, Ebook
from dotenv import load_dotenv
from connection import Connection

class Download:

    def __init__(self, base_url):
        self.base_url = base_url
        self.db = Connection(os.getenv('DB_HOST'), os.getenv('DB_USER'), os.getenv('DB_PASSWORD'), os.getenv('DB'))

    def start(self):
        while true:
            book = self.get_book()
            self._download(book)

            self.db.set_book_loaded(book['id'])

    def get_book(self):
        # get unloaded book from db
        pass

    def save_chapters(self, chapters):
        pass

    def _download(self, book):
        page_url = urljoin(self.base_url, book['href'])
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

        # to do - save chapter

        ebook.save()

    def get_content(soup):
        c = BeautifulSoup()
        section = soup.find('td', class_='content')
        # remove <font></font> or <span></span>

        c.append(section)
            
        return c

