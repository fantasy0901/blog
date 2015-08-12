from app import app
from flask import render_template,flash,redirect
from .forms import LoginForm

@app.route('/login',methods = ['GET','POST'])
#@app.route('/index')
def login():
	form = LoginForm()
	return render_template('login.html',title='Sign In',form=form)
	#user = { 'nickname': 'Fantasy'}
	#posts = [ 
	#     {
	#	'author': {'nickname':'John'},
	#	'body': 'Beautiful day in Portland!'
        #    },
        #     {
	#	'author': {'nickname':'Susan'},
	#	'body': 'The Avergers movie was so cool!'
        #     }
	#]
	#return render_template("index.html",title='Home',user = user,posts = posts)

