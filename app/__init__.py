from flask import Flask

from app.request import configure_request
from .config import config_options


def create_app(environment):
    loise = Flask(__name__, instance_relative_config=True)
    loise.config.from_object(config_options[environment])
    from app.main import main
    loise.register_blueprint(main)
    configure_request(loise)
    return loise
