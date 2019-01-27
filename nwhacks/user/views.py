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

def get_user(request, goal_id):
    retval = {}
    return retval

def put_user(request, goal_id):
    retval = {}
    return retval

def handle_new_user(request):
    retval = {}
    return JsonResponse(retval, status=retval["status"])