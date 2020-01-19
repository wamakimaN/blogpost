from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from . import main
from flask_login import login_required

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    return render_template('index.html')