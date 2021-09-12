from flask import app, render_template
from app import app
from . import main
from ..request import get_source,article_source


#our views
@main.route('/')
def index():
    '''
    Root function returning index/home page with data
    '''
    source= get_source()
    return render_template('index.html',source=source)

@main.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the various article details page and its data
    '''
    # title= 'Articles'
    articles = article_source(id)
    return render_template('article.html',articles= articles,id=id )
