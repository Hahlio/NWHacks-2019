import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import User, user_exists, create_user
from user.models import create_task_with_goal, create_task_without_goal
from django.core.exceptions import ObjectDoesNotExist
from goal.views import post_goal

def handle_new_user(username):
    retval = {}
    print('INSIDE FN' , username)
    user_id = create_user({"username":username})
    retval["ID"] = user_id
    retval["status"] = 200
    return JsonResponse(retval, status=retval["status"])

def handle_username(request, username):
    if request.method == 'GET':
        retval = {}
        print(request)
        try:
            temp = User.objects.get(username=username)
            retval["userID"] = temp.id
            retval["status"] = 200
            print("inside try")
        except ObjectDoesNotExist:
            print('from here?')
            retval["status"] = 404
            retval["user_message"] = "User not found"
        return JsonResponse(retval, status=retval["status"])
    elif request.method == 'POST':
        return handle_new_user(username)

def handle_user_id(request, user_id):
    print("Ran user!!!!!!")
    retval = {}
    if request.method == 'GET':
        retval = get_user_request(request, user_id)
        print("DID GET")
        return JsonResponse(retval)
    # elif request.method == 'PUT':
    #     retval = put_user_request(request, user_id)
    else:
        retval["status"] = 405
        retval["user_message"] = "Method not defined"
        return JsonResponse(retval, status=retval["status"])

def handle_user_ical(request, user_id):
    retval = {}
    print("Ran ical")
    if request.method == 'GET':
        retval = get_ical_request(request, user_id)
    elif request.method == 'POST':
        retval = post_ical_request(request, user_id) 
    else:
        retval["status"] = 405
        retval["user_message"] = "Method not defined"
    return JsonResponse(retval, status=retval["status"])

def handle_user_task(request, user_id):
    print("hello")
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

def handle_user_goal(request, user_id):
    retval = {}
    if request.method == 'POST':
        retval = post_user_goal_request(request, user_id) 
    else:
        retval["status"] = 405
        retval["user_message"] = "Method not defined"
    return JsonResponse(retval, status=retval["status"])

def post_user_goal_request(request, user_id):
    retval = {}
    if user_exists(user_id):
        print("USER EXISTS")
        body = request.body.decode("utf-8")
        retval = post_goal(body, user_id)
        print(retval)
        return retval
    else:
        print("USER DOESNT EXISTS")
        retval["status"] = 404
        retval["user_message"] = "User does not exist"
        return retval

def get_user_request(request, user_id):
    retval = {}
    if user_exists(user_id):
        print("USER EXISTS")
        return User.objects.get(pk=user_id).in_json()
    else:
        print("USER DOESNT EXISTS")
        retval["status"] = 404
        retval["user_message"] = "User does not exist"
        return retval

# # TODO implement the model function
# def put_user_request(request, user_id):
#     retval = {}
#     if user_exists(user_id):
#         user_obj = User.objects.get(pk=user_id)
#         body = request.body.decode("utf-8")
#         # use user_obj to edit the values based on the body
#         retval = {
#             "status": 200
#         }
#     else:
#         retval = {
#             "status": 404,
#             "user_message": "User does not exist"
#         }
#     return retval

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

def post_user_task_request(request, user_id):
    # Create the task
    # Associate task with user
    body = request.body.decode("utf-8")
    task = create_task_without_goal(body, user_id)
    retval = {
        "id": task["task_id"],
        "status": 200
    }
    return retval

def post_user_goal_task_request(request, user_id, goal_id):
    # Create the task
    # Associate task with goal
    body = request.body.decode("utf-8")
    task = create_task_with_goal(body, goal_id)
    retval = {
        "id": task["task_id"],
        "status": 200
    }
    return retval
