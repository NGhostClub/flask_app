from flask_app import app



def run_web():
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
	#app.run()


if __name__ == '__main__':
	run_web()
