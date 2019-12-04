from flask import Flask
import os, yaml
from flask_sqlalchemy import SQLAlchemy
import psycopg2


__version__ = '1.0.1'


app = Flask(__name__)


#config init
config_file = 'config/config.yaml'

class Config(object):
	if (os.path.isfile(config_file)):
		with open(config_file, 'r') as f:
			yaml_config = yaml.safe_load(f)
	else:
		yaml_config = {}
	HOST = os.environ.get('FLASK_HOST') or yaml_config.get('FLASK_HOST', '0.0.0.0')
	PORT = os.environ.get('FLASK_PORT') or yaml_config.get('FLASK_PORT', '5000')
	DEBUG = os.environ.get('DEBUG') or yaml_config.get('DEBUG', False)
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or yaml_config.get('SQLALCHEMY_DATABASE_URI', 'postgresql://flask_app_user:123@localhost/flask_app')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = yaml_config.get('SECRET', 'default_secret')

app.config.from_object(Config)
###

db = SQLAlchemy(app)


from flask_app import models, routes
from flask_app.database import db_session, init_db


init_db()


def hello():
	print ('Hello from flask_app', app.config['SECRET_KEY']);


def run_web():
	app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])


if __name__ == '__main__':
	run_web()
