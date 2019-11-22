from setuptools import setup, find_packages
from os.path import join, dirname
import flask_app

setup(
	name='flask_app',
	version=flask_app.__version__,
	packages=find_packages(),
	entry_points={
		'console_scripts':
			[
			'app_hello = flask_app:hello',
			'serve = flask_app:run_web',
			]
	},
	install_requires=[
		'Flask==1.1.1'
	]
)
