import os


class Config:

    SECRET_KEY = os.environ['SECRET_KEY']

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CHARSET = 'utf8mb4'

    EMPTY_DB = 'empty'
    API_DB = 'api'
    SPIDER_DB = 'spider'

    API_USR = os.environ['API_MYSQL_USER']
    API_PWD = os.environ['API_MYSQL_PASSWORD']

    MYSQL_HOST = os.environ['MYSQL_HOST']
    MYSQL_PORT = os.environ['MYSQL_PORT']

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{API_USR}:{API_PWD}@{MYSQL_HOST}:{MYSQL_PORT}/{EMPTY_DB}?charset={CHARSET}'

     SQLALCHEMY_BINDS = {
        API_DB: f'mysql+pymysql://{API_USR}:{API_PWD}@{MYSQL_HOST}:{MYSQL_PORT}/{API_DB}?charset={CHARSET}',
    }

    # api redis
    API_REDIS_HOST = os.environ['API_REDIS_HOST']
    API_REDIS_PASSWORD = os.environ.get('API_REDIS_PASSWORD')

    # redis port
    REDIS_PORT = os.environ['REDIS_PORT']

    SYSTEM_NAME = 'spending_tracker'
    ENVIRONMENT = os.environ.get('ENVIRONMENT')
