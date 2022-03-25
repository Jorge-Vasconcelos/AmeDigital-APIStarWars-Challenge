from flask import jsonify, make_response
from flask_restful import Resource, reqparse

from starwars_api.db_connection import DataBase


class Planet(Resource):
    params = reqparse.RequestParser()
    params.add_argument('name', type=str)
    params.add_argument('climate', type=str)
    params.add_argument('terrain', type=str)

    def get(self, id_planet):
        sql = 'select * from planets where id_planet= %s'
        arguments = (id_planet,)
        query_result = DataBase.consult(sql, arguments)
        if query_result == ():
            return {'message': 'planet not found'}, 404
        return make_response(jsonify(query_result), 200)
    
    def post(self, id_planet=None):
        body = Planet.params.parse_args()
        sql = 'insert into planets (name,climate,terrain)' \
              'VALUES (%s,%s,%s)'
        arguments = (body['name'], body['climate'], body['terrain'])
        DataBase.execute(sql, arguments)
        return {'message': 'planet created'}, 201
    
    def put(self, id_planet):
        sql = f'select * from planets where id_planet= %s'
        arguments = (id_planet,)
        query_result = DataBase.consult(sql, arguments)
        if query_result == ():
            return {'message': 'planet not found'}, 404
        body = Planet.params.parse_args()
        sql = 'update planets set name=%s ,climate=%s , terrain=%s ' \
              'WHERE id_planet=%s'
        arguments = (body['name'], body['climate'], body['terrain'], id_planet)
        DataBase.execute(sql, arguments)
        return {'message': 'planet updated'}, 200

    def delete(self, id_planet):
        sql = f'select * from planets where id_planet= %s'
        arguments = (id_planet,)
        query_result = DataBase.consult(sql, arguments)
        if query_result == ():
            return {'message': 'planet not found'}, 404
        sql = 'delete from planets where id_planet=%s'
        arguments = id_planet
        DataBase.execute(sql, arguments)
        return {'message': 'planet deleted'}, 200


