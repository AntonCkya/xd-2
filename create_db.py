"""
Скрипт для создания базы данных
Запустить однажды и забыть
"""
from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

con = None
con = connect(user='postgres', host = 'localhost', password='XD_120403_1000$')

dbname = "cinema"

con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = con.cursor()
cur.execute('CREATE DATABASE ' + dbname)
cur.close()
con.close()
