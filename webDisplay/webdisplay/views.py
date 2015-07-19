from pyramid.view import view_config
from sqlLink import dbLink

db_link = dbLink()
EVENT_MINUTES_WINDOW = 20

#Main GET handler, serves static content
@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'webDisplay'}

#POST Handler for motion detection
@view_config(route_name='motion_detected', renderer='json')
def motion_detected_view(request):
    print("Motion detected")
    return ""

#POST Handler for admin status check
@view_config(route_name='check_camera', renderer='json')
def motion_detected_view(request):
    #Check that this is the correct format
    if request.method != 'POST':
        return ""
    print(request.json_body)
    #TODO: check authentication status
    #Check for a motion event
    unapproved_events = db_link.get_unapproved_events(EVENT_MINUTES_WINDOW)
    motion = (len(unapproved_events) > 0)
    return {'authenticated':True, 'motion':motion}

#POST Handler for admin clicking "YES" on GUI
@view_config(route_name='alert_users', renderer='json')
def admin_check_motion(request):
    print(request)
    #TODO: authenticate administrator, send alert to users (e-mail?, pushbullet?, other APIs?)
    user_list = db_link.get_users()
    print(user_list)
    #TODO: gordon, put your thing here and call it with user_list
    return user_list
