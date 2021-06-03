from flask import Flask
from flask_restful import Api
from resources.planet import Planets, Planet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DataBase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def cria_banco():
    DataBase.create_all()


api.add_resource(Planets, '/planets')
api.add_resource(Planet, '/planet/<string:planet_id>')

if __name__ == '__main__':
    from sql_alchemy import DataBase

    DataBase.init_app(app)
    app.run(debug=True)
