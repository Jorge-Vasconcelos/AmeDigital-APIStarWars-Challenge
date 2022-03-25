from flask import Flask
from flask_restful import Api

from models.database import SCHEMA_DDL
from starwars_api.models.db_connection import DataBase

from routes.index import Index
from routes.swapi import Swapi
from routes.planets import Planets
from routes.planet import Planet

app = Flask(__name__)
api = Api(app)


@app.before_first_request
def create_database():
    DataBase.execute(SCHEMA_DDL)


api.add_resource(Index, '/')
api.add_resource(Swapi, '/swapi')
api.add_resource(Planets, '/planets')
api.add_resource(Planet, '/api/planet', '/api/planet/<string:id_planet>')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
