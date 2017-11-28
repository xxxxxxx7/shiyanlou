#!/usr/bin/env python3
import os, json
from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/shiyanlou.db'
app.config['TEMPLATES_AUTO_RELOAD'] = True
db = SQLAlchemy(app)


class Category(db.Model):
	__tablename__ = 'Category'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))

	def __init__(self, id, name):
		self.id = id
		self.name = name
	def __repr__(self):
		return '<Category %r>' % self.id


class File(db.Model):
	__tablename__ = 'file'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80))
	created_time = db.Column(db.DateTime)
	category_id = db.Column(db.Integer, db.ForeignKey(Category.id))
	content = db.Column(db.Text)

	def __init__(self, id, tile, created_time, category_id, content):
		self.id = id
		self.title = name
		self.created_time = created_time
		self.category_id = category_id
		self.content = content
	def __repr__(self):
		return '<File %r>' % self.id







@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404


@app.route('/')
def index():
	path = '/home/shiyanlou/files/'
	for list in os.walk(path):
		listdir = list[2]

	helloshiyanlou_course = {}
	with open ('/home/shiyanlou/files/helloshiyanlou.json') as test:
		helloshiyanlou_course = json.loads(test.read())

	helloworld_course = {}
	with open ('/home/shiyanlou/files/helloworld.json') as test:
		helloworld_course = json.loads(test.read())		
	return render_template('index.html',filelist=listdir, shiyanloutitle=helloshiyanlou_course, worldtitle=helloworld_course)


		

@app.route('/files/<filename>')
def file(filename):	


	thefile = filename + '.json'
	checkfile = os.path.join('/home/shiyanlou/files/',thefile)
	if os.path.exists(checkfile):

		if filename == 'helloshiyanlou':

			helloshiyanlou_course = {}
			with open ('/home/shiyanlou/files/helloshiyanlou.json') as test:
				helloshiyanlou_course = json.loads(test.read())
			
			return render_template('file.html', outputname=helloshiyanlou_course)

		elif filename == 'helloworld':

			helloworld_course = {}
			with open ('/home/shiyanlou/files/helloworld.json') as test:
				helloworld_course = json.loads(test.read())
			
			return render_template('file.html', outputname=helloworld_course)

	else:
		return render_template('404.html'), 404
		

	 
	







if __name__ == '__main__':
	app.run()
