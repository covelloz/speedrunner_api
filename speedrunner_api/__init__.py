from flask import Flask
from speedrunner_api.blueprint import api

__version__ = '0.1'
__author__ = 'Michael Covello'
__created__ = '04/27/2019'

app = Flask(__name__)
app.register_blueprint(api)


def run_app(config):
    app.run(debug=True, host=config.host, port=config.port)
