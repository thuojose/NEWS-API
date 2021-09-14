from flask import app, render_template,request,redirect,url_for
from . import main
from ..request import get_query, get_source,article_source,get_category,get_headlines


#our views
@main.route('/')
def index():
    '''
    Root function returning index/home page with data
    '''
    source= get_source()
    headlines = get_headlines()

    search_article = request.args.get('article_search')
    
    if search_article:
        return redirect(url_for('main.search',article_name = search_article))
    else:
        return render_template('index.html',sources=source,headlines=headlines)
        

@main.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the various article details page and its data
    '''
    # title= 'Articles'
    articles = article_source(id)
    return render_template('article.html',articles= articles,id=id )

@main.route('/categories/<cat_name>')
def category(cat_name):
    '''
    function to return the categories.html page and its content
    '''
    category = get_category(cat_name)
    title = f'{cat_name}'
    cat = cat_name

    return render_template('categories.html',title = title,category = category, cat= cat_name)

@main.route('/search/<article_name>')
def search(article_name):
    whole_article_name = article_name.split(" ")
    article_name_format = "+".join(whole_article_name)
    search_results = get_query(article_name_format)
    return render_template('search.html',source = search_results)
