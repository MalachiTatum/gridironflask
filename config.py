import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    DB_USER = 'postgres'
    DB_PASSWORD = ''
    DB_HOST = 'localhost'
    DB_NAME = 'gridironflaskdb'
    #SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_DATABASE_URI = "postgresql://" + DB_USER + ":" + DB_PASSWORD + "@" + DB_HOST + ":5432/" + DB_NAME

# Local Development Environment
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

# Development envs in Docker Containers
class DevDockerConfig(DevelopmentConfig):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    DB_USER = 'postgres'
    DB_PASSWORD = ''
    DB_HOST = 'db'
    DB_NAME = 'gridironflaskdb'
    #SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_DATABASE_URI = "postgresql://" + DB_USER + ":" + DB_PASSWORD + "@" + DB_HOST + ":5432/" + DB_NAME
    #DEBUG = True
    #DB_HOST = 'db'

class TestingConfig(Config):
    TESTING = True

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

#print(os.environ['DATABASE_URL'])
