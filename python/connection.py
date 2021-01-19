from mysql.connector import connect, Error

class Connection:

    def __init__(self, host: str, user: str, password: str, db: str):
        self._host = host
        self._user = user
        self._password = password
        self._db = db

    def connect(self):
        try:
            with connect(
                host = self._host,
                user = self._user,
                password = self._password,
                database = self._db,
            ) as connection:
                self.connection = connection

        except Error as e:
            print(e)
    
    def exec(self, query: str):
        if not self.connection:
            raise 'no connection exists'
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
                
        except Error as e:
            print(e)

