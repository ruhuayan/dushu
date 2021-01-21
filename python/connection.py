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
    
    def insert_books(self, records):
        
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
                cursor.executemany(insert_books_query, records)
                self.connection.commit()
                
        except Error as e:
            print(e)

    def get_unloaded_books(self):
        select_books_query = "SELECT * FROM books WHERE loaded = 0"
        with self.connection.cursor() as cursor:
            cursor.execute(select_books_query)
            result = cursor.fetchall()
            return result

    def close(self):
        self.connection.close()

