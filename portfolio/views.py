from pyramid.view import view_config, notfound_view_config
from pyramid.httpexceptions import HTTPNotFound

@view_config(route_name='projects', renderer='templates/projects.jinja2')
def index(request):
    return {'project': 'Portfolio'}
    
@view_config(route_name='about', renderer='templates/about.jinja2')
def about(request):
    return {}

@view_config(route_name='rnapairs', renderer='templates/rnapairs.jinja2')
def rnapairs(request):
    return {}

@notfound_view_config(append_slash=True)
def notFound(request):
    return HTTPNotFound("404 Error. Sorry, page not found.")
