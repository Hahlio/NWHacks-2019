from django.shortcuts import render

from django.http import JsonResponse

from .models import User

# Create your views here.

def handle_goal(request, goal_id):
    """
    satisfies all the goal endpoint commands
    GET:
    PUT:
    POST:
    DELETE:
    """
    retval = {}
    if request.method == 'GET':
        retval = get_user(request, goal_id)
    elif request.method == 'PUT':
        retval = put_user(request, goal_id)
    else:
        retval["status"] = 400
        retval["user_message"] = "Method not defined"
    return JsonResponse(retval, status=retval["status"])

def get_user(request, user_id):
    retval = {}
    
    return retval

def put_user(request, user_id):
    retval = {}
    return retval

def handle_new_user(request):
    retval = {}
    return JsonResponse(retval, status=retval["status"])

def handle_user_ical(request, user_id):
    retval = {}
    if request.method == 'GET':
        retval = get_ical_request(request, user_id)
    elif request.method == 'POST':
        retval = post_ical_request(request, goal_id) 
    else:
        retval["status"] = 400
        retval["user_message"] = "Method not defined"
    return JsonResponse(retval, status=retval["status"])

def get_ical_request(request, user_id):
    retval = {}
    if user_exists(user_id):
        ical = User.objects.get(pk=user_id).get_ical()
        retval["ical"] = ical
        retval["status"] = 200
    else:
        retval = {
            "status": 404,
            "user_message": "user cannot be found"
        }
    return retval

def post_ical_request(request, user_id):
    retval = {}
    body = request.body.decode("utf-8")
    if user_exists(user_id):
        User.objects.get(pk=user_id).edit_ical(body)
        retval["status"] = 200
    else:
        retval = {
            "status": 404,
            "user_message": "user cannot be found"
        }
    return retval