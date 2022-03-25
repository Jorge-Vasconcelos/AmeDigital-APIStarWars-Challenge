from flask import jsonify, make_response
from flask_restful import Resource, reqparse

from starwars_api.models.db_connection import DataBase


class Planets(Resource):
    params = reqparse.RequestParser()
    params.add_argument('name', type=str)
    params.add_argument('climate', type=str)
    params.add_argument('terrain', type=str)

    def get(self):
        # Query Params
        dados = Planets.params.parse_args()
        name = dados['name']
        climate = dados['climate']
        terrain = dados['terrain']

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
        return make_response(jsonify(json_list), 200)
