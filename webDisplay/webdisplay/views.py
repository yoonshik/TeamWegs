from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'webDisplay'}

@view_config(route_name='motion_detected', renderer='templates/mytemplate.pt')
def motion_detected_view(request):
    return {'project':'webDisplay'}
