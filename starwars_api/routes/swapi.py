import requests
from flask_restful import Resource


class Swapi(Resource):
    def get(self):
        r = requests.get('https://swapi.dev/api/planets/')
        data = r.json()
        return data, 200
