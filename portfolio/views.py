from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/index.jinja2')
def my_view(request):
    return {'project': 'Portfolio'}
    
@view_config(route_name='about', renderer='templates/about.jinja2')
def about(request):
    return {}
