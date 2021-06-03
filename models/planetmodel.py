from sql_alchemy import DataBase


class PlanetModel(DataBase.Model):
    __tablename__ = 'planets'

    planet_id = DataBase.Column(DataBase.String, primary_key=True)
    name = DataBase.Column(DataBase.String(50))
    climate = DataBase.Column(DataBase.String(50))
    terrain = DataBase.Column(DataBase.String(50))

    def __init__(self, planet_id, name, climate, terrain):
        self.planet_id = planet_id
        self.name = name
        self.climate = climate
        self.terrain = terrain

    def json(self):
        return {
            'planet_id': self.planet_id,
            'name': self.name,
            'climate': self.climate,
            'terrain': self.terrain
        }

    @classmethod
    def find_id(cls, planet_id):
        planet = cls.query.filter_by(planet_id=planet_id).first()
        if planet:
            return planet
        return False

    @classmethod
    def find_name(cls, planet_id):
        planet = cls.query.filter_by(name=planet_id).first()
        if planet:
            return planet
        return False

    def save(self):
        DataBase.session.add(self)
        DataBase.session.commit()

    def update(self, name, climate, terrain):
        self.name = name
        self.climate = climate
        self.terrain = terrain

    def delete(self):
        DataBase.session.delete(self)
        DataBase.session.commit()
