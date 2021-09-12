from flask import app, render_template
from app import app
from . import main
from ..request import get_source


#our views
@main.route('/')
def index():
    '''
    Root function returning index/home page with data
    '''
    source= get_source()
    return render_template('index.html',source=source)