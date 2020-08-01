import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///{db_path}/{db_name}'.format(**{
    'db_path': os.path.dirname(os.path.abspath(__file__)),
    'db_name': 'db.sqlite3'
})
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_ENGINE_OPTIONS = ''
DEBUG = True
TESTING = True
