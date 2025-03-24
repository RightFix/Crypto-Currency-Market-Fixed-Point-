import time
from pybit.unified_trading import HTTP 
from pybit.exceptions import FailedRequestError
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name='home', renderer='template/home.pt')
def home_view(request):
  
    return {'page_title': 'home'}

@view_config(route_name='fp', renderer='template/fp.pt')
def about_view(request):
    
    return {'page_title': 'fp'}

@view_config(route_name='about', renderer='template/about.pt')
def contact_view(request):
  
    return {'page_title': 'about'}

if __name__ == '__main__':
    with Configurator() as config:
        config.include('pyramid_chameleon')  # Enable Chameleon templating
        config.add_route('home', '/')
        config.add_route('fp', '/fp')
        config.add_route('about', '/about')
        config.scan() # Scan for view configurations

        config.add_static_view('static', path='static') # Serve static files

        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    print("Server started on http://0.0.0.0:6543")
    server.serve_forever()