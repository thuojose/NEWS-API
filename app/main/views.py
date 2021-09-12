from flask import app, render_template
from app import app
from . import main

#our views
@main.route('/')
def index():
    '''
    Root function returning index/home page with data
    '''
    return render_template('index.html')