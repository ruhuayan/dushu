import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from ebook import Chapter, Ebook
from connection import Database, BASE_URL
import re
import logging
import math

class Download:

    def __init__(self):
        self.db = Database()
        logging.basicConfig(filename='download.log', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

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

                    # divide big book into multiple volumns
                    if ebook.per_serie > 0:
                        for i in range(len(ebook.series)):
                            serie = ebook.series[i]
                            new_book = (serie[1], book[2], book[3], book[4], book[5])

                            insert_id = self.db.insert_books([new_book])
                            print(insert_id)
                            start = i * ebook.per_serie
                            end = (i + 1) * ebook.per_serie

                            _, ebook_series= self._download([insert_id, *new_book], start, end)
                            records = list(ebook_series)
                            self.db.insert_chapters(records)
                            self.db.set_serie_loaded(insert_id, serie[0], serie[1])
                            self.db.set_book_loaded(insert_id, desc)
                else: 
                    # insert chpaters
                    chapter_records = list(ebook)

                    self.db.insert_chapters(chapter_records)

                self.db.set_book_loaded(book[0], desc)
            except Exception as e:
                logging.error(f'{book[1]} (id: {book[0]}) download failed', exc_info=True)

    def _download(self, book, start = None, end = None) -> str:
        page_url = urljoin(BASE_URL, book[2])
        print(page_url)
        page = requests.get(page_url)
        soup = BeautifulSoup(page.content, 'html.parser', from_encoding="gb18030")

        # get book description
        desc_td = soup.find('td', class_='Readme')
        description = desc_td.get_text() if desc_td else ''
        
        ebook = Ebook(book[0], book[1], book[3])
        #Chapter.index = 0

        try:
            content_td = soup.find('td', class_='content')
            # in series page, no table used
            links = content_td.find('table').find_all('a') if content_td.find('table') else content_td.find_all('a')
        except:
            links = soup.find_all('a', class_='m002')
            ebook.has_series = True
            ebook.series = [(book[0], link['title'], link['href']) for link in links]
            return str(description), ebook
        
        if start is not None and end is not None:
            links = links[start:end]
            print(f'chapter - {start} to chapter - {end}')

        elif len(links) > 250: # chapters gt 250
            total = len(links)
            per_serie = 200
            nums_series = total // per_serie
            if nums_series == 1:
                nums_series = 2
                per_serie = total // nums_series
            else:
                nums_left = total % per_serie
                per_serie += math.ceil(nums_left / nums_series)

            ebook.has_series = True
            ebook.per_serie = per_serie

            for i in range(nums_series):
                serie = (book[0], f'{book[1]}-{i+1}', book[2])
                ebook.add_series(serie)

            return str(description), ebook
            # links = links[0:300] if len(links) > 300 else links
            print(f'{total} chapters')

        for link in links:

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
            print(f'{chapter.db_id} - {chapter_name}')
            try:
                chapter_content = self.get_content(soup)
            except:
                chapter_content = ''
                logging.error(f'{book[1]} (id: {book[0]}) is missing Chapter {chapter_name}')

            chapter.set_content(chapter_content)
            ebook.add_chapter(chapter)

        if not ebook.has_series:
            try:
                ebook.save()
            except Exception as e:
                logging.error(f'{book[1]} (id: {book[0]}) raised exception', exc_info=True)

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

