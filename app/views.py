from app import app
from flask import render_template,flash,redirect
from .forms import LoginForm

@app.route('/login',methods = ['GET','POST'])
#@app.route('/index')
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('login requested for OpenID="' + form.openid.date + '", remember_me=' + str(form.remember_me.data))
	return render_template('login.html',title='Sign In',form=form,providers = app.config['OPENID_PROVIDERS'])
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

