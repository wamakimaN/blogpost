from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from . import main
from app.models import Post,User
from flask_login import login_required

@main.route('/')
@main.route('/index')
@main.route('/index/<int:id>')
def index(id = None):
    if id:
        posts = Post.query.filter_by(id=id)
    else:
        posts = Post.query.all()
        title = 'Home'

    return render_template('index.html', posts=posts, title = title)

@main.route('/user/<uname>', methods = ['GET','POST'])
@login_required
def profile(uname):

    
    user = User.query.filter_by(username = uname).first()
    posts = Post.query.all()
    

    return render_template("profile/profile.html",posts = posts ,user = user)