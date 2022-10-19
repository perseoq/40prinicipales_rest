import os 

class Configure(object):
    SECRET_KEY = os.urandom(24)

class RestApiConfig(Configure):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('MYSQL_NEWREST')
    SQLALCHEMY_TRACK_MODIFICATIONS = False