#!/usr/bin/env python3
import os, json
from flask import Flask, render_template, abort

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

#helloshiyanlou = '/home/shiyanlou/files/helloshiyanlou.json'
#helloworld = '/home/shiyanlou/files/helloworld.json'
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
