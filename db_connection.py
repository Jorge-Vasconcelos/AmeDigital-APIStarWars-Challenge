import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='starwars',
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
    def consult(cls, sql):
        with conecta() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchall()
