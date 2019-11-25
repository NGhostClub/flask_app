from flask import Flask, request, url_for
from flask_app import app
from flask_app.database import db_session
from flask_app.models import TableLog
from flask_app import db
import time, json
from sqlalchemy import func


@app.route('/')
def index():
	data_count = db.session.execute(db.session.query(func.count(TableLog.id))).scalar()
	if data_count == 0:
		data = ">> <br> >> There is no records in database table  yet :( <br>"
	else:
		data = db.session.query(TableLog).order_by(TableLog.id.desc()).first().data
	return render_template('index.html', title='Index Page', data=str(data))


@app.route('/dbtest')
def dbtest():
	data = 'some test data + time.time() = ' + str(time.time())
	new_data = TableLog(data)
	db.session.add(new_data)
	try:
		db.session.commit()
		return render_template('post.html', title='Post TEST DATA - Success', data=data)
	except:
		db.session.rollback()
		data = 'Some Error happen... Rollback commit'
		return render_template('post.html', title='Post TEST DATA - Failure', data=data)
		raise


@app.route('/post_json')
def post_json():
	data = 'JSON DATA POST NOT YET WORKING'
	return render_template('post.html', title='Post JSON Page', data=data)


@app.route('/post', methods=['GET', 'POST'])
def json_test():
	if request.is_json:
		content = request.get_json()
		data = content
		db.session.add(TableLog(data))
	else:
		data = {'error':'no valid json', 'is_json': False}
		data = json.dumps(data)
		db.session.add(TableLog(data))
	db.session.commit()
	return render_template('json.html', data = data)
	return 'Data added!'
