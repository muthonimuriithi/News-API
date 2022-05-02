from flask import Flask
from .config import DevConfig

loise = Flask(__name__,instance_relative_config=True)
loise .config.from_object(DevConfig)
loise.config.from_pyfile('config.py')

from app import views
