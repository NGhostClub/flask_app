from flask_app import db
from sqlalchemy import Column, Integer, String, JSON
from flask_app.database import Base
import json


class TableLog(Base):
	__tablename__ = 'table__log'
	id = Column(Integer, primary_key=True)
	data = Column(JSON)

	def __init__(self, data=None):
		self.data = data


	def __repr__(self):
		return '<data %r>' % (self.data)
