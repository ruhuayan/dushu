from os import getenv
from dotenv import load_dotenv
from mysql.connector import connect, Error

load_dotenv()
BASE_URL = getenv('BASE_URL')
class Database:

    def __init__(self):
        self.config = {
                        'host' : getenv('DB_HOST'), 
                        'user' : getenv('DB_USER'),
                        'password' : getenv('DB_PASSWORD'), 
                        'database' : getenv('DB')
                    }
        self.connection = None

    def connect(self):
        try:
            self.connection = connect(**self.config)
        except Error as e:
            print(e)
    
    def insert_books(self, books):
        
        if not self.connection:
            print('No Connection')
            return
        if not self.connection.is_connected():
            print('Not Connected to MySQL database')
            return
        try:
            insert_books_query = """
            INSERT INTO books
            (title, href, author, category, alphabet)
            VALUES (%s, %s, %s, %s, %s)
            """
            with self.connection.cursor() as cursor:
                cursor.executemany(insert_books_query, books)
                self.connection.commit()
                return cursor.lastrowid   
        except Error as e:
            print(e)

    def insert_series(self, series):
        try:
            insert_series_query = """
            INSERT INTO series
            (book_id, serie_title, href)
            VALUES (%s, %s, %s)
            """
            with self.connection.cursor() as cursor:
                cursor.executemany(insert_series_query, series)
                self.connection.commit()
                
        except Error as e:
            print(e)

    def set_serie_loaded(self, id, book_id: int, title: str):
        update_book_qurey = 'UPDATE series SET serie_id = %s WHERE book_id = %s AND serie_title = %s'
        with self.connection.cursor() as cursor:
            cursor.execute(update_book_qurey, (id, book_id, title))
            self.connection.commit()
            print(cursor.rowcount, "book affected")

    def insert_chapters(self, chapters):
        try:
            insert_chapters_query = """
            INSERT INTO chapters
            (chapter_id, book_id, title, content)
            VALUES ( %s, %s, %s, %s)
            """
            with self.connection.cursor() as cursor:
                cursor.executemany(insert_chapters_query, chapters)
                self.connection.commit()
                print(cursor.rowcount, "chapter(s) affected")
        except Error as e:
            print(e)

    def get_unloaded_book(self):
        select_book_query = "SELECT * FROM books WHERE loaded = 0 LIMIT 1"
        with self.connection.cursor() as cursor:
            cursor.execute(select_book_query)
            result = cursor.fetchone()
            return result

    def set_book_loaded(self, book_id: int, desc: str):
        update_book_qurey = 'UPDATE books SET loaded = 1, description = %s WHERE id = %s'
        with self.connection.cursor() as cursor:
            cursor.execute(update_book_qurey, (desc, book_id))
            self.connection.commit()
            print(cursor.rowcount, "book affected")

    def close(self):
        self.connection.close()

