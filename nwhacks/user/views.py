from django.shortcuts import render

from django.http import JsonResponse

from .models import User

# TODO
def handle_new_user(request):
    retval = {}
    return JsonResponse(retval, status=retval["status"])

def handle_user(request, user_id):
    retval = {}
    if request.method == 'GET':
        retval = get_user_request(request, user_id)
    elif request.method == 'PUT':
        retval = put_user_request(request, user_id)
    else:
        retval["status"] = 400
        retval["user_message"] = "Method not defined"
    return JsonResponse(retval, status=retval["status"])

def handle_user_ical(request, user_id):
    retval = {}
    if request.method == 'GET':
        retval = get_ical_request(request, user_id)
    elif request.method == 'POST':
        retval = post_ical_request(request, user_id) 
    else:
        retval["status"] = 400
        retval["user_message"] = "Method not defined"
    return JsonResponse(retval, status=retval["status"])

def handle_user_task(request, user_id):
    retval = {}
    if request.method == 'POST':
        retval = post_user_task_request(request, user_id) 
    else:
        retval["status"] = 400
        retval["user_message"] = "Method not defined"
    return JsonResponse(retval, status=retval["status"])

def handle_user_goal_task(request, user_id, goal_id):
    retval = {}
    if request.method == 'POST':
        retval = post_user_goal_task_request(request, user_id, goal_id) 
    else:
        retval["status"] = 400
        retval["user_message"] = "Method not defined"
    return JsonResponse(retval, status=retval["status"])

# TODO
def get_user_request(request, user_id):
    retval = {}
    return retval

# TODO
def put_user_request(request, user_id):
    retval = {}
    return retval

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

# TODO
def post_user_task_request(request, user_id):
    retval = {}
    return retval

# TODO
def post_user_goal_task_request(request, user_id, goal_id)
    retval = {}
    return retval