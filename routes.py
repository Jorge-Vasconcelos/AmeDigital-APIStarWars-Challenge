from app import app
from flask import request, jsonify
from db_connection import DataBase
import requests


@app.route('/swapi', methods=['GET'])
def read_planet_swapi():
    r = requests.get('https://swapi.dev/api/planets/')
    data = r.json()
    return data


@app.route('/api/planets', methods=['GET'])
def read_planet_all():
    sql = 'select * from planets'
    query_result = DataBase.consult(sql)
    return {'planeta': [planet for planet in query_result]}


@app.route('/api/planet/<string:id_planet>', methods=['GET'])
def read_planet_id(id_planet):
    sql = f'select * from planets where id_planet={id_planet}'
    query_result = DataBase.consult(sql)
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
    return {'message': 'planet created'}, 200


@app.route('/api/planet/<string:id_planet>', methods=['PUT'])
def update_planet(id_planet):
    sql = f'select * from planets where id_planet={id_planet}'
    query_result = DataBase.consult(sql)
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
    sql = f'select * from planets where id_planet={id_planet}'
    query_result = DataBase.consult(sql)
    if query_result == ():
        return {'message': 'planet not found'}, 404
    sql = 'delete from planets where id_planet=%s'
    arguments = id_planet
    DataBase.execute(sql, arguments)
    return {'message': 'planet deleted'}, 200
