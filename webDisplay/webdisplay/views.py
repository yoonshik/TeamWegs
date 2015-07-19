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
@view_config(route_name='check_camera', renderer='templates/mytemplate.pt')
def admin_check_motion(request):
    #TODO: authenticate administrator using SQL class
    #TODO: check SQL server for motion event within time frame
    #return {'authorization':true, 'motion_detected':true}
    return {'project':'webDisplay'}

#POST Handler for admin clicking "YES" on GUI
@view_config(route_name='alert_users', renderer='json')
def admin_check_motion(request):
    print(request)
    #TODO: authenticate administrator, send alert to users (e-mail?, pushbullet?, other APIs?)
    return {'authorization':true, 'motion_detected':true}
