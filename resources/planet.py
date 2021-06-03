from flask_restful import Resource, reqparse
from models.planetmodel import PlanetModel
import requests


class SWApi(Resource):
    def get(self):
        r = requests.get('https://swapi.dev/api/planets/')
        data = r.json()
        return data


class Planets(Resource):
    def get(self):
        return {'Planets': [planet.json() for planet in PlanetModel.query.all()]}  # SELECT * FROM Planets


class Planet(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('name', type=str, required=True, help="The field 'nome' cannot be left blank.")
    atributos.add_argument('climate')
    atributos.add_argument('terrain')

    def get(self, planet_id):
        try:
            # forçando a dar o ValueError se não conseguir transformar em int
            int(planet_id)
            planet = PlanetModel.find_id(planet_id)
            if planet:
                return planet.json()
            return {'message': 'planet not found.'}, 404
        except ValueError:
            planet = PlanetModel.find_name(planet_id)
            if planet:
                return planet.json()
            return {'message': 'planet not found.'}, 404

    def post(self, planet_id):
        if PlanetModel.find_id(planet_id):
            return {f"message": f"planet id '{planet_id}' already exists."}, 400  # Bad Request

        dados = Planet.atributos.parse_args()
        planet = PlanetModel(planet_id, **dados)
        try:
            planet.save()
        except:
            return {"message": "An error ocurred trying to create planet."}, 500  # Internal Server Error
        return planet.json(), 201

    def put(self, planet_id):
        dados = Planet.atributos.parse_args()
        planet = PlanetModel(planet_id, **dados)

        planet_encontrado = PlanetModel.find_id(planet_id)
        if planet_encontrado:
            planet_encontrado.update(**dados)
            planet_encontrado.save()
            return planet_encontrado.json(), 200
        planet.save()
        return planet.json(), 201

    def delete(self, planet_id):
        planet = PlanetModel.find_id(planet_id)
        if planet:
            planet.delete()
            return {'message': 'planet deleted.'}
        return {'message': 'planet not found.'}, 404
