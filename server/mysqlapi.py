import mysql.connector

class MySQLAPI():
    def __init__(self, host, database, user, password):
        self._connection = mysql.connector.connect(host=host,
            database=database,
            user=user,
            password=password
        )
        self._cursor = self._connection.cursor(dictionary=True)

    def insert(self, table, fields, values):
        cmd_sql = f"INSERT INTO {table} ({','.join([str(s) for s in fields])}) VALUES ({','.join(['%s' for s in fields])})"
        self._cursor.execute(cmd_sql, values)
        self._connection.commit()
        return self._cursor.lastrowid

    def select(self, table, fields, filter = '1'):
        # TODO prevent SQL injection by using %s
        cmd_sql = f"SELECT {fields} FROM {table} WHERE {filter}"
        self._cursor.execute(cmd_sql)
        return self._cursor.fetchall()

    def delete(self, table, filter):
        # TODO prevent SQL injection by using %s
        cmd_sql = f"DELETE FROM {table} WHERE {filter}"
        self._cursor.execute(cmd_sql)
        self._connection.commit()

    def update(self):
        pass
