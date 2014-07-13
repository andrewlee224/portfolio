from pyramid.view import view_config, notfound_view_config
from pyramid.httpexceptions import HTTPNotFound

@view_config(route_name='projects', renderer='templates/mainprojects.jinja2')
def index(request):
    return {'project': 'Portfolio'}
    
@view_config(route_name='root', renderer='templates/root.jinja2')
def root(request):
    return {}

@view_config(route_name='about', renderer='templates/about.jinja2')
def about(request):
    return {}

@view_config(route_name='this', renderer='templates/this.jinja2')
def this(request):
    return {}

@view_config(route_name='contact', renderer='templates/contact.jinja2')
def contact(request):
    return {}

@view_config(route_name='rnapairs', renderer='templates/rnapairs.jinja2')
def rnapairs(request):
    return {}

@view_config(route_name='usgviewer', renderer='templates/usgviewer.jinja2')
def usgviewer(request):
    return {}

@view_config(route_name='signalmonitor', renderer='templates/signalmonitor.jinja2')
def signalmonitor(request):
    return {}

@view_config(route_name='drugscheduler', renderer='templates/drugscheduler.jinja2')
def drugscheduler(request):
    return {}

@notfound_view_config(append_slash=True)
def notFound(request):
    return HTTPNotFound("404 Error. Sorry, page not found.")
