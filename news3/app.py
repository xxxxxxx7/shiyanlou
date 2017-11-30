#!/usr/bin/env python3
from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from pymongo import MongoClient


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/shiyanlou'
app.config['TEMPLATES_AUTO_RELOAD'] = True
db = SQLAlchemy(app)
mongo = MongoClient('127.0.0.1',27017).shiyanlou

class Category(db.Model):
	__tablename__ = 'Category'
	id = db.Column(db.Integer, primary_key=True ) 
	name = db.Column(db.String(80))
	files = db.relationship('File')

	def __init__(self, name):	
		self.name = name
	def __repr__(self):
		return '<Category %r>' % self.id


class File(db.Model):
	__tablename__ = 'file'

	id = db.Column(db.Integer, primary_key=True ) 
	title = db.Column(db.String(80), unique=True)
	created_time = db.Column(db.DateTime)
	category_id = db.Column(db.Integer, db.ForeignKey(Category.id))
	category = db.relationship('Category', uselist=False)
	content = db.Column(db.Text)

	def __init__(self, title, created_time, category, content):	
		self.title = title
		self.created_time = created_time
		self.category = category
		self.content = content

	def add_tag(self,tag_name):
		file_item = mongo.files.find_one({'file_id': self.id})
		if file_item:
			tags = file_item['tags']
			if tag_name not in tags:
				tags.append(tag_name)
			mongo.files.update_one({'file_id': self.id},{'$set': {'tags': tags}})
		else:
			tags = [tag_name]
			mongo.files.insert_one({'file_id': self.id, 'tags': tags})
		return tags

	def remove_tag(self, tag_name):
		file_item = mongo.files.find_one({'file_id': self.id})
		if file_item:
			tags = file_item['tags']
			try:
				new_tags = tags.remove(tag_name)

			except ValueError:
				return tags
			mongo.files.update_one({'file_id': self.id},{'$set': {'tags': new_tags}})
			return new_tags
		return []

	@property
	def tags(self):
		file_item = mongo.files.find_one({'file_id': self.id})
		if file_item:
			print(file_item)
			return file_item['tags']
		else:
			return []



@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404


@app.route('/')
def index():
	
	return render_template('index.html', filelist=File.query.all())
		

@app.route('/files/<file_id>')
def file(file_id):	

	file_item = File.query.get_or_404(file_id)
	return render_template('file.html', file_item=file_item)