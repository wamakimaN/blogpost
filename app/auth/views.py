from flask import render_template
from flask_wtf import FlaskForm
from .form import LoginForm
from . import auth

@auth.route('/login',methods = ['GET','POST'])
def login():

    form = LoginForm()

    return render_template('auth/login.html', form = form)