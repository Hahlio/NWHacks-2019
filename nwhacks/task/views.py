from django.http import JsonResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import is_valid_id, Task
from datetime import date
import json

# Create your views here.

def handle_existing_task(request, task_id):
    retval = {}
    print("****************")
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
    print("WASSUP")
    task = Task.objects.get(pk=task_id)
    return JsonResponse(task.inJson())


def put_task(task_id, json_args):
    task = modify_task(task_id, json_args)
    retval = {
        "id": task.id
    }
    return JsonResponse(retval)

def modify_task(task_id, json_args):
    task = Task.objects.get(pk=task_id)
    args_dict = json.loads(json_args)
    task.description = args_dict["task"]
    done = args_dict["done"]
    deadline_string = args_dict["deadline"].split('-')
    year = deadline_string[2]
    year_int = int(year)
    month = deadline_string[1]
    month_int = int(month)
    day = deadline_string[0]
    day_int = int(day)
    deadline_date = date(year_int, month_int, day_int)
    task.deadline = deadline_date
    task.save()
    return task

