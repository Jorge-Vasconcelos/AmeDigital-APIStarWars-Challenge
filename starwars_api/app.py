from flask import Flask
from flask_restful import Api

from starwars_api.models.db_connection import create_database
from routes.index import Index
from routes.swapi import Swapi
from routes.planets import Planets
from routes.planet import Planet

app = Flask(__name__)
api = Api(app)

api.add_resource(Index, '/')
api.add_resource(Swapi, '/swapi')
api.add_resource(Planets, '/planets')
api.add_resource(Planet, '/api/planet', '/api/planet/<string:id_planet>')

if __name__ == '__main__':
    create_database()
    app.run(debug=False, host='0.0.0.0', port=5000)
