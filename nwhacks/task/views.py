from django.http import JsonResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def handle_existing_task(request, task_id):
    retval = {}
    if is_valid_id(task_id):
        if request.method == 'GET':
            return get_task(task_id)
        elif request.method == 'PUT':
            json_args = request.body.decode("utf-8")
            return put_task(task_id, json_args)
        else:
            retval = {
                "status": 405,
                "user_message": "The requested method is not allowed"
            }
    else:
        retval = {
            "status": 404,
            "user_message": "The task you requested was not found"
        }
    return JsonResponse(retval, status=retval["status"])

def get_task(task_id):
    task = Task.objects.get(pk=task_id)
    return JsonResponse(task.inJson())


def put_task(task_id, json_args):
    task = modify_task(task_id, json_args)
    retval = {
        "id": task.id
    }
    return JsonResponse(retval)
