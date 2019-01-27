from django.shortcuts import render
from django.http import JsonResponse

from .models import Goal

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
        retval = get_goal(request, goal_id)
    elif request.method == 'PUT':
        retval = put_goal(request, goal_id)
    else:
        retval["status"] = 400
        retval["user_message"] = "Method not defined"
    return JsonResponse(retval, status=retval["status"])

def get_goal(request, goal_id):
    retval = {}
    retval = get_goal_obj(goal_id)
    if(goal_obj["exist"]):
        retval["status"] = 200
        return goal_obj
    else:
        retval["status"] = 404
        retval["user_message"] = "User is not found"
    return retval

def put_goal(request, goal_id):
    retval = {}
    json_args = request.body.decode("utf-8")
    try:
        temp_obj = Goal.objects.get(pk=goal_id)
        temp_obj.edit(json_args)
        retval["status"] = 200
    except ObjectDoesNotExist:
        retval["status"] = 404
    return retval
