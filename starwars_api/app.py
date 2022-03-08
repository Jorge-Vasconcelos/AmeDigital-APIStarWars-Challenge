from flask import Flask

app = Flask(__name__)

from routes import *

app.run(debug=False, host='0.0.0.0', port=5000)
