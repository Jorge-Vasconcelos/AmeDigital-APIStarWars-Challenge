import pymysql.cursors
from contextlib import contextmanager


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
    @classmethod
    def execute(cls, sql, args):
        with conecta() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(sql, args)
                conexao.commit()

    @classmethod
    def consult(cls, sql, args=None):
        with conecta() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(sql, args)
                return cursor.fetchall()
