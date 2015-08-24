from app import app, db, lm, oid
from flask import render_template,flash,redirect,session, url_for, request, g
from .forms import LoginForm
from .models import User
from flask.ext.login import login_user, logout_user, current_user, login_required

@app.before_request
def before_request()
	g.user = current_user

@app.route('/login',methods = ['GET','POST'])
#oid.loginhandler
def login():
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		session['remember_me'] = form.remember_me.data
		return oid.try_login(form.openid.data, ask_for=['nickname','email'])
	return render_template('login.html',title='Sign In',form=form,providers = app.config['OPENID_PROVIDERS'])
	
@app.route('/')
@app.route('/index')
@login_required
def index():
	user = g.user
	#user = { 'nickname': 'Fantasy'}
	posts = [ 
	     {
		'author': {'nickname':'John'},
		'body': 'Beautiful day in Portland!'
            },
             {
		'author': {'nickname':'Susan'},
		'body': 'The Avergers movie was so cool!'
             }
	]
	return render_template("index.html",title='Home',user = user,posts = posts)

@login.after_login
def after_login(resp):
	if resp.email is None or resp.email=="":
		flash('Invalid login. Please try again.')
		return redirect(url_for('login'))
	user = User.query.filter_by(email=resp.emial).first()
	if user is None:
		nickname = resp.nickname
		if nickname is None or nickname == "":
			nickname = resp.email.split('@')[0]
		user = User(nickname=nickname, email=resp.email)
		db.session.add(user)
		db.session.commit()
	remember_me = False
	if 'remember_me' in session:
		remember_me = session['remember_Me']
		session.pop('remember_me', None)
	login_user(user, remember=remember_me)
	return redirect(request.args.get('next') or url_for('index')

@lm.user_loader
def loader_user(id):
	return User.query.get(int(id))

