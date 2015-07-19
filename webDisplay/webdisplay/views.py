from pyramid.view import view_config

#Main GET handler, serves static content
@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'webDisplay'}

#POST Handler for motion detection
@view_config(route_name='motion_detected', renderer='templates/mytemplate.pt')
def motion_detected_view(request):
    return {'project':'webDisplay'}

#POST Handler for admin status check
@view_config(route_name='check_camera', renderer='json')
def motion_detected_view(request):
    #Check that this is the correct format
    if request.method != 'POST':
        return ""
    print(request.json_body)
    return {'authenticated':True, 'motion':False}

#POST Handler for admin clicking "YES" on GUI
@view_config(route_name='alert_users', renderer='json')
def admin_check_motion(request):
    print(request)
    #TODO: authenticate administrator, send alert to users (e-mail?, pushbullet?, other APIs?)
    return {'authorization':true, 'motion_detected':true}
