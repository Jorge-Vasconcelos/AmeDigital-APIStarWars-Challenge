from flask import Flask
from flask_restful import Api
from resources.planet import Planets, Planet, SWApi

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DataBase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def cria_banco():
    DataBase.create_all()


api.add_resource(Planets, '/planets')
api.add_resource(Planet, '/planet/<string:planet_id>')
api.add_resource(SWApi, '/planets/api')

if __name__ == '__main__':
    from sql_alchemy import DataBase

    DataBase.init_app(app)
    app.run(debug=True)

""""
-	Adicionar um planeta (com nome, clima e terreno) xxx
-	Listar planetas do banco de dados xxx
-	Listar planetas da API do Star Wars
-	Buscar por nome no banco de dados xxx
-	Buscar por ID no banco de dados xxx
-	Remover planeta xx
"""
