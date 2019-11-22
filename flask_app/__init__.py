from flask import Flask
import os, yaml


__version__ = '1.0'


app = Flask(__name__)

#print(os.path.isfile('config/config.yaml'))

with open('config/config.yaml', 'r') as f:
	yaml_config = yaml.safe_load(f)

#print(yaml_config)


def hello():
	print ('Hello from flask_app',yaml_config['SECRET']);


def run_web():
	app.run(host=yaml_config['HOST'], debug=yaml_config['DEBUG'])


if __name__ == '__main__':
	run_web()
