import logging
from flask import Flask
from speedrunner_api.config import config
from speedrunner_api.blueprint import api


__version__ = '0.1'
__author__ = 'Michael Covello'

# configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
f_handler = logging.FileHandler(config.log_name, encoding='utf-8')
f_format = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)

# configure flask
app = Flask(__name__)
app.register_blueprint(api, url_prefix='/speedrunner')


def run_app(config):
    app.run(debug=True, host=config.host, port=config.port)
