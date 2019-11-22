from flask_app import app
from flask_app import yaml_config as config


def run_web():
    app.run(host=config['HOST'], debug=config['DEBUG'])
	#app.run()


if __name__ == '__main__':
	run_web()
