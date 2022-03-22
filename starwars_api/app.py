from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse

from db_connection import DataBase

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

@app.route('/api/planet/<string:id_planet>', methods=['GET'])
def read_planet_id(id_planet):
    sql = 'select * from planets where id_planet= %s'
    arguments = (id_planet,)
    query_result = DataBase.consult(sql, arguments)
    if query_result == ():
        return {'message': 'planet not found'}, 404
    return jsonify(query_result), 200


@app.route('/api/planet', methods=['POST'])
def creat_planet():
    body = request.get_json()
    sql = 'insert into planets (name,climate,terrain)' \
          'VALUES (%s,%s,%s)'
    arguments = (body['name'], body['climate'], body['terrain'])
    DataBase.execute(sql, arguments)
    return {'message': 'planet created'}, 201


@app.route('/api/planet/<string:id_planet>', methods=['PUT'])
def update_planet(id_planet):
    sql = f'select * from planets where id_planet= %s'
    arguments = (id_planet,)
    query_result = DataBase.consult(sql, arguments)
    if query_result == ():
        return {'message': 'planet not found'}, 404
    body = request.get_json()
    sql = 'update planets set name=%s ,climate=%s , terrain=%s ' \
          'WHERE id_planet=%s'
    arguments = (body['name'], body['climate'], body['terrain'], id_planet)
    DataBase.execute(sql, arguments)
    return {'message': 'planet updated'}, 200


@app.route('/api/planet/<string:id_planet>', methods=['DELETE'])
def delete_planet(id_planet):
    sql = f'select * from planets where id_planet= %s'
    arguments = (id_planet,)
    query_result = DataBase.consult(sql, arguments)
    if query_result == ():
        return {'message': 'planet not found'}, 404
    sql = 'delete from planets where id_planet=%s'
    arguments = id_planet
    DataBase.execute(sql, arguments)
    return {'message': 'planet deleted'}, 200


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
