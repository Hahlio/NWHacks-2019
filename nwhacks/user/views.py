from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from task.models import create_task
from django.core.exceptions import ObjectDoesNotExist

def handle_new_user(request):
    retval = {}
    user_id = create_user(json.loads(request.body.decode("utf-8")))
    retval["ID"] = user_id
    retval["status"] = 200
    return JsonResponse(retval, status=retval["status"])

def handle_username(request, username):
    retval = {}
    try:
        temp = User.Objects.get(username=username)
        retval["userID"] = temp.id
        retval["status"] = 200
    except ObjectDoesNotExist:
        retval["status"] = 404
        retval["user_message"] = "User not found"
    return JsonResponse(retval, status=retval["status"])

def handle_user(request, user_id):
    retval = {}
    if request.method == 'GET':
        retval = get_user_request(request, user_id)
    elif request.method == 'PUT':
        retval = put_user_request(request, user_id)
    else:
        retval["status"] = 405
        retval["user_message"] = "Method not defined"
    return JsonResponse(retval, status=retval["status"])

def handle_user_ical(request, user_id):
    retval = {}
    if request.method == 'GET':
        retval = get_ical_request(request, user_id)
    elif request.method == 'POST':
        retval = post_ical_request(request, user_id) 
    else:
        retval["status"] = 405
        retval["user_message"] = "Method not defined"
    return JsonResponse(retval, status=retval["status"])

def handle_user_task(request, user_id):
    retval = {}
    if request.method == 'POST':
        retval = post_user_task_request(request, user_id) 
    else:
        retval["status"] = 405
        retval["user_message"] = "Method not defined"
    return JsonResponse(retval, status=retval["status"])

def handle_user_goal_task(request, user_id, goal_id):
    retval = {}
    if request.method == 'POST':
        retval = post_user_goal_task_request(request, user_id, goal_id) 
    else:
        retval["status"] = 405
        retval["user_message"] = "Method not defined"
    return JsonResponse(retval, status=retval["status"])

def get_user_request(request, user_id):
    retval = {}
    if user_exists(user_id):
        User.objects.get(pk=user_id).in_json()
    else:
        retval["status"] = 404
        retval["user_message"] = "User does not exist"
    return retval

# TODO implement the model function
def put_user_request(request, user_id):
    retval = {}
    if user_exists(user_id):
        user_obj = User.objects.get(pk=user_id)
        body = request.body.decode("utf-8")
        # use user_obj to edit the values based on the body
        retval = {
            "status": 200
        }
    else:
        retval = {
            "status": 404,
            "user_message": "User does not exist"
        }
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

# TODO finish up the task generation
def post_user_task_request(request, user_id):
    # Create the task
    # Associate task with user
    retval = {
        "status": 200,
    }
    return retval

# TODO finish up the task generation
def post_user_goal_task_request(request, user_id, goal_id):
    retval = {}
    try:
        goal_obj = Goal.objects.get(pk=goal_id)
        # Create the task
        # Associate task with user
        # Associate task with goal
        # Return the status
    except ObjectDoesNotExist:
        retval = {
            "status": 404,
            "user_message": "goal cannot be found"
        }
    
    return retval