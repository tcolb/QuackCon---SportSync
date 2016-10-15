from flask import render_template, request
import sqlite3
from FlaskApp import app
from FlaskApp import models as dbHandle

@app.route('/', methods=['POST','GET'])
def index():
	if request.method == 'POST':
		play = request.form['play']
		detail = request.form['detail']
		dbHandle.insert_play(play, detail)

		return render_template('te.html',)
	else:
		return render_template('base.html',)