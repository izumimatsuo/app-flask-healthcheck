import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    DEBUG = True
    TESTING = True

config = BaseConfig()

api = Flask(__name__, instance_relative_config=True)
api.config.from_object(config)
api.config.from_pyfile('config.py', silent=True)

db = SQLAlchemy()
db.init_app(api)
