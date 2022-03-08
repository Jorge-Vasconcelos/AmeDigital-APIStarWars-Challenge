from app import app
from flask import request, jsonify
from db_connection import DataBase
import requests


@app.route('/', methods=['GET'])
def index():
    return 'I am alive'


@app.route('/swapi', methods=['GET'])
def read_planet_swapi():
    r = requests.get('https://swapi.dev/api/planets/')
    data = r.json()
    return data, 200


@app.route('/api/planets', methods=['GET'])
def read_planet_all():
    # Query Params
    name = request.args.get('name')
    climate = request.args.get('climate')
    terrain = request.args.get('terrain')

    # Query Creation
    arguments = []
    add_and = False
    first = True

    sql = 'SELECT * FROM planets '

    # --------NAME--------
    if name:
        if first:
            sql = sql + 'WHERE '
            first = False

        sql = sql + 'name = %s '
        arguments.append(name)
        add_and = True

    # --------CLIMATE--------
    if climate:
        if first:
            sql = sql + 'WHERE '
            first = False
        else:
            add_and = True

        if add_and:
            sql = sql + 'AND '
            add_and = True
        sql = sql + 'climate = %s '
        arguments.append(climate)

    # --------TERRAIN--------
    if terrain:
        if first:
            sql = sql + 'WHERE '
            first = False
        else:
            add_and = True

        if add_and:
            sql = sql + 'AND '
            add_and = True
        sql = sql + 'terrain = %s '
        arguments.append(terrain)

    # Executing Query
    query_result = DataBase.consult(sql, arguments)
    json_list = [planet for planet in query_result]
    return jsonify(json_list), 200


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
