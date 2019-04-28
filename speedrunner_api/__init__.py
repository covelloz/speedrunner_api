from flask import Flask
from speedrunner_api.blueprint import api

__version__ = '0.1'
__author__ = 'Michael Covello'
__created__ = '04/27/2019'


def run_app(config):
    app = Flask(__name__)
    app.register_blueprint(api)
    app.run(debug=True, host=config.host, port=config.port)
