from flask import jsonify, make_response
from flask_restful import Resource
import requests


class Swapi(Resource):
    def get(self):
        planet_list = []
        next_request = 'https://swapi.dev/api/planets/'
        while next_request:
            response = requests.get(next_request).json()
            next_request = response['next']
            for planet in response['results']:
                planet_dict = {
                    'name': planet['name'],
                    'qtd_films': len(planet['films'])
                }
                planet_list.append(planet_dict)

        return make_response(jsonify(planet_list), 200)
