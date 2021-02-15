import pathlib
import shutil
import os
import subprocess
from jinja2 import Environment, FileSystemLoader
from typing import Optional, List, Tuple
from weasyprint import HTML

class Chapter:
    index = 0
    def __init__(self, title: str):
        Chapter.index = Chapter.index + 1
        self.id = f'chapter_{Chapter.index}'
        self.db_id = Chapter.index
        self.title = title

    def set_content(self, content):
        self.content = content

class Ebook:

    def __init__(self, id: int, title: str, author = '无名氏'):
        self.id = id
        self.title = title
        self.output_path = f'ebooks/{title}'
        self.author = author
        self.file_name = f'{title}.html'
        self._templates_env = Environment(loader=FileSystemLoader(
            str(pathlib.Path(__file__).parent / 'templates/')))
        
        self.chapters = list()

        self.has_series = False
        self.series = list()
        # chapter start from 1 in every ebook
        Chapter.index = 0

    def _render_file(self, template_name: str, context: dict, filename: str):
        template = self._templates_env.get_template(template_name)
        with open(os.path.join(self.output_path, filename), mode="w", encoding='utf-8') as f:
            f.write(template.render(**context))

    def setTitle(self, title: str):
        self.title = title

    def setAuthor(self, author: str):
        self.author = author

    def getBookPath(self):
        return os.path.join(self.output_path, self.file_name)

    def getChapters(self) -> List:
        return [dict(title = chapter.title, id = chapter.id) for chapter in self.chapters]

    def add_chapter(self, chapter: Chapter): 
        self.chapters.append(chapter)

    def add_series(self, serie: Tuple): 
        self.series.append(serie)

    def save_cover(self) -> None:
        if self.cover_path:
            cover_path = self.cover_path
            shutil.copy(cover_path, str(self.output_path))
        else:
            cover = pathlib.Path(__file__).parent / 'templates/cover.jpg'
            shutil.copy(str(cover), str(self.output_path))

    def create_folder(self):
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

    ''' Create main ebook html file '''
    def _render_main(self) -> str:
        html = f'{self.title}.html'
        self._render_file(
            'template.html',
            {
                'title': self.title,
                'chapters': self.chapters
            },
            html
        )
        return html

    def _render_toc_ncx(self):
        ncx = 'toc.ncx'
        self._render_file(
            'toc.xml',
            {
                'chapters': self.chapters,
                'title': self.title,
                'author': self.author,
                'file_name': self.file_name
            },
            ncx
        )
        return ncx

    def _render_toc_html(self):
        toc = 'toc.html'
        self._render_file(toc, {'chapters': self.chapters, 'file_name': self.file_name}, toc)
        return toc

    def _render_opf(self) -> str:
        opf_file = f'{self.title}.opf'
        self._render_file(
            'opf.xml',
            {
                'file_name': self.file_name,
                'title': self.title,
                'author': self.author
            },
            opf_file
        )
        return opf_file

    ''' convert html to pdf '''
    def _render_pdf(self, html: str)->None:
        input_file = os.path.join(self.output_path, html)
        output_file = os.path.join(self.output_path, f'{self.title}.pdf')

        # make sure chinese font is installed in system
        HTML(filename=input_file, encoding='UTF-8').write_pdf(output_file)


    def save(self) -> None:
        self.create_folder()
        html = self._render_main()
        self._render_toc_ncx()
        self._render_toc_html()
        opf_file = self._render_opf()
        #self.save_cover()

        self._render_pdf(html)
        rc = subprocess.call([
            'ebook-convert', os.path.join(self.output_path, opf_file), os.path.join(self.output_path, f'{self.title}.mobi') 
        ])
        if rc != 0:
            raise Exception('ebook-convert failed')

    def __iter__(self):
        for chapter in self.chapters:
            chapter_record = (chapter.db_id, self.id, chapter.title, str(chapter.content))
            yield chapter_record

