from flask import render_template,redirect,url_for
from flask_wtf import FlaskForm
from ..models import User
from .form import LoginForm,RegistrationForm
from . import auth
from .. import db

@auth.route('/login',methods = ['GET','POST'])
def login():

    form = LoginForm()

    return render_template('auth/login.html', form = form)

@auth.route('/signup',methods = ["GET","POST"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/signup.html',reg_form = form)