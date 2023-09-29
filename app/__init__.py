from os import getenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api #para interfaz de swagger
from app.config import environment
FLASK_ENV=getenv('FLASK_ENV')
ENVIRONMENT = environment[FLASK_ENV]

app = Flask(__name__)
app.config.from_object(ENVIRONMENT)
api = Api(
  app,
  title='Boilerplate Flask',
  version='0.1',
  description='EndPoints flask',
  doc='/swagger-ui'
  ) #para interfaz de swagger
db = SQLAlchemy(app)
migrate = Migrate(app,db)