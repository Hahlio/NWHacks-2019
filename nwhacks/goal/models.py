import json

from django.db import models

from django.core.exceptions import ObjectDoesNotExist
#from Task.models import Task

# Create your models here.
class Goal(models.Model):
    goal = models.CharField(default="", max_length=256)
    #tasks = models.ManyToManyField(Task)
    done = models.BooleanField()
    deadline = models.DateField(auto_now=False, auto_now_add=False)

    def in_json(self):
        retval = {}
        retval["goal"] = self.goal
        retval["done"] = self.done
        task_number = 1
        tasks = {}

        for t in self.tasks.all():
            task_obj = {}
            task_obj["taskID"] = t.id
            tasks[str(task_number)] = task_obj
            task_number += 1

        retval["task"] = tasks

        return retval

    def edit(self, args):
        json_obj = json.loads(args)
        #for x in json_obj["task"]:
            #try:
                #temp_task = Task.objects.get(pk=x)
                

def create_goal(args):
    json_obj = json.loads(args)
    goal = Goal(goal=json_obj['goal'], done=json_obj['done'])
    goal.save()
    return goal.id

def get_goal_obj(goal_id):
    retval = {}
    try:
        temp_obj = Goal.objects.get(pk=goal_id)
        retval = temp_obj.in_json()
        retval["exist"] = True
    except ObjectDoesNotExist:
        retval["exist"] = False
    return retval
    