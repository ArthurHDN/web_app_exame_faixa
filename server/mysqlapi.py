import mysql.connector

class MySQLAPI():
    def __init__(self, host, database, user, password):
        self._connection = mysql.connector.connect(host=host,
            database=database,
            user=user,
            password=password
        )
        self._cursor = self._connection.cursor()

    def insert(self, table, fields, values):
        cmd_sql = f"INSERT INTO {table} ({','.join([str(s) for s in fields])}) VALUES ({','.join(['%s' for s in fields])})"
        self._cursor.execute(cmd_sql, values)
        self._connection.commit()

    def get_connection(self):
        return self._connection
