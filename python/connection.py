from mysql.connector import connect, Error

class Connection:

    def __init__(self, host: str, user: str, password: str, db: str):
        self._host = host
        self._user = user
        self._password = password
        self._db = db
        self.connection = None

    def connect(self):
        try:
            self.connection = connect(
                                        host = self._host,
                                        user = self._user,
                                        password = self._password,
                                        database = self._db,
                                    )
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
            VALUES ( %s, %s, %s, %s, %s)
            """
            with self.connection.cursor() as cursor:
                cursor.executemany(insert_books_query, books)
                self.connection.commit()
                
        except Error as e:
            print(e)

    def insert_chapters(self, chapters):
        try:
            insert_chapters_query = """
            INSERT INTO chapters
            (chapter_id, book_id, title, content)
            VALUES ( %d, %d, %s, %s)
            """
            with self.connection.cursor() as cursor:
                cursor.executemany(insert_chapters_query, chapters)
                self.connection.commit()
                
        except Error as e:
            print(e)

    def get_unloaded_book(self):
        select_book_query = "SELECT * FROM books WHERE loaded = 0 LIMIT 1"
        with self.connection.cursor() as cursor:
            cursor.execute(select_books_query)
            result = cursor.fetchone()
            return result

    def set_book_loaded(self, book_id: int):
        update_book_qurey = f'UPDATE books SET loaded = 1 WHERE id = {book_id}'
        with self.connection.cursor() as cursor:
            cursor.execute(update_book_qurey)
            connection.commit()
            print(cursor.rowcount, "record(s) affected")

    def close(self):
        self.connection.close()

