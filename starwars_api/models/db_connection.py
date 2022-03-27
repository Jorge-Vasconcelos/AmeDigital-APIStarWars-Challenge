import traceback
from time import sleep
import pymysql.cursors
from contextlib import contextmanager

from starwars_api.models.database import SCHEMA_DDL


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='mysql_server',
        user='root',
        password='123',
        port=3306,
        db='testedb',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        conexao.close()


class DataBase:
    @staticmethod
    def execute(sql, args=None):
        with conecta() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(sql, args)
                conexao.commit()

    @staticmethod
    def consult(sql, args=None):
        with conecta() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(sql, args)
                return cursor.fetchall()


def create_database():
    for _ in range(10):
        try:
            DataBase.execute(SCHEMA_DDL)
            break
        except:
            traceback.print_exc()
            sleep(2)
