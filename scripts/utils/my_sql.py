import pymysql as MySQLdb

from scripts.constants import app_configuration


class MysqlClient(object):

    def __init__(self):
        self.db_name = app_configuration.sql_password
        self.passwd = app_configuration.sql_password
        self.user = app_configuration.sql_username
        self.host = app_configuration.sqldb_host

    def connect(self):
        self.db = MySQLdb.connect(host=self.host, user=self.user, password=self.passwd, database=self.db_name)
        self.db.autocommit(True)
        self.cur = self.db.cursor()
        return self.cur

    def execute(self, query):
        cursor = self.connect()
        cursor.execute(query)
        result = cursor.fetchall()
        self.close_connection()
        return result

    def execute_many(self, query, _list):
        cursor = self.connect()
        cursor.executemany(query, _list)
        result = cursor.fetchall()
        self.close_connection()
        return result

    def execute_insert(self, query):
        cursor = self.connect()
        cursor.execute(query)
        return cursor.lastrowid

    def close_connection(self):
        self.cur.close()
        self.db.close()
