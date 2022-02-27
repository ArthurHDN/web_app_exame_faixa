import mysql.connector

class MySQLAPI():
    def __init__(self, host, database, user, password):
        self._connection = mysql.connector.connect(host=host,
            database=database,
            user=user,
            password=password
        )

    def get_connection(self):
        return self._connection
