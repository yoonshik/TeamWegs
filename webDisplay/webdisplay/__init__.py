from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('motion_detected', '/motion_detected')
    config.add_route('check_camera', '/check_camera')
    config.add_route('alert_users', '/alert_users')
    config.scan()
    return config.make_wsgi_app()
