import redis
from config import Config
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

app = Flask(__name__)

config = Config()
app.config.from_object(config)

db = SQLAlchemy(app)

cors = CORS(app, resources={r"/*": {"origins": "*"}})
db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)

from core.models import *

api_rs = redis.StrictRedis(
    host=config.API_REDIS_HOST,
    password=config.API_REDIS_PASSWORD,
    port=config.REDIS_PORT,
    charset=config.CHARSET,
    decode_responses=True)

from controllers.route_controllers import *

def create_app():
    return app
