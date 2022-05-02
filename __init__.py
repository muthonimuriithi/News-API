from flask import Flask
from .config import DevConfig

loise = Flask(__name__)
loise .config.from_object(DevConfig)

from app import views
