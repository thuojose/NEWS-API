import urllib.request,json

# Getting api key
api_key = None
# Getting source url
source_url= None
# Getting source url
cat_url= None

def configure_request(app):
    global api_key, source_url, cat_url
    api_key = app.config['NEWS_API_KEY']
    source_url= app.config['NEWS_API_SOURCE_URL']
    cat_url=app.config['CAT_API_URL']
