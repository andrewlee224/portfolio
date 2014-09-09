from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('root', '/')
    config.add_route('projects', '/projects/')
    config.add_route('about', '/about/')
    config.add_route('this', '/about/this/')
    config.add_route('contact', '/about/contact/')

    # Projects subpages
    config.add_route('rnapairs', '/projects/rna-pairs/')
    config.add_route('signalmonitor', '/projects/signal-monitor/')
    config.add_route('drugscheduler', '/projects/drug-scheduler/')
    config.add_route('usgviewer', '/projects/usg-viewer/')
    config.add_route('distsemaphore', '/projects/distributed-semaphore/')

    config.scan()
    return config.make_wsgi_app()
