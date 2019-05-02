import logging
from flask import Flask
from speedrunner_api.config import config
from speedrunner_api.blueprint import api


__version__ = '0.1'
__author__ = 'Michael Covello'

logging.basicConfig(
    filename=config.log_name,
    format='%(name)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/speedrunner')


def run_app(config):
    app.run(debug=True, host=config.host, port=config.port)
