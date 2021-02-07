import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from ebook import Chapter, Ebook
from connection import Database, BASE_URL
import re
import logging

class Download:

    def __init__(self):
        self.db = Database()
        logging.basicConfig(filename='download.log', format='%(name)s - %(levelname)s - %(message)s')

    def start(self):
        if not self.db.connection:
            self.db.connect()

        while True:
            book = self.db.get_unloaded_book()
            if not book:
                print('No unloaded book found')
                return
            try:
                desc, ebook = self._download(book)

                if ebook.has_series:
                    # insert series
                    self.db.insert_series(ebook.series)
                else: 
                    # insert chpaters
                    chapter_records = list(ebook)

                    self.db.insert_chapters(chapter_records)

                self.db.set_book_loaded(book[0], desc)
            except:
                logging.error(f'{book[1]} (id: {book[0]}) download failed')

    def _download(self, book) -> str:
        page_url = urljoin(BASE_URL, book[2])
        print(page_url)
        page = requests.get(page_url)
        soup = BeautifulSoup(page.content, 'html.parser', from_encoding="gb18030")

        # get book description
        desc_td = soup.find('td', class_='Readme')
        description = desc_td.get_text()
        
        ebook = Ebook(book[0], book[1], book[3])
        Chapter.index = 0

        try:
            content_td = soup.find('td', class_='content')
            # in series page, no table used
            links = content_td.find('table').find_all('a') if content_td.find('table') else content_td.find_all('a')
        except:
            links = soup.find_all('a', class_='m002')
            ebook.has_series = True
            ebook.series = [(book[0], link['title'], link['href']) for link in links]
            return str(description), ebook

        # chapters gt 300
        if len(links) > 300:
            links = links[0:300]
            logging.warning(f'{book[1]} (id: {book[0]}) has {len(links)} chapters')
        # links = links[0:300] if len(links) > 300 else links
        print(f'{len(links)} chapters')

        for link in links:
            print(link)

            chapter_name = link.get_text()

            if '.html' not in link['href'] and '.htm' not in link['href']:
                ebook.has_series = True
                serie = (book[0], chapter_name, link['href'])
                ebook.add_series(serie)
                continue

            # htm page use 001.htm
            chapter_url = urljoin(BASE_URL, link['href']) if '.html' in link['href'] else urljoin(page_url, link['href'].replace('mydoc', ''))
            page = requests.get(chapter_url)
            soup = BeautifulSoup(page.content, 'html.parser', from_encoding="gb18030")

            # create chapter header
            chapter = Chapter(chapter_name)

            try:
                chapter_content = self.get_content(soup)
            except:
                chapter_content = ''
                logging.error(f'{book[1]} (id: {book[0]}) is missing Chapter {chapter_name}')

            chapter.set_content(chapter_content)
            ebook.add_chapter(chapter)

        if ebook.has_series:
            return str(description), ebook
        else:
            ebook.save()
            return str(description), ebook

    def get_content(self, soup: BeautifulSoup) -> BeautifulSoup:
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

        return section

download = Download()
download.start()

