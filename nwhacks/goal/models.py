import json

from django.db import models

from django.core.exceptions import ObjectDoesNotExist
from task.models import Task
from django.db.models import Q

# Create your models here.
class Goal(models.Model):
    goal = models.CharField(default="", max_length=256)
    done = models.BooleanField()
    deadline = models.DateField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)

    def in_json(self):
        retval = {}
        retval["goal"] = self.goal
        retval["done"] = self.done
        retval["user_id"] = self.user.id
        task_set = Tasks.objects.filter(Q(goal__exact=self))
        tasks = [task.id for task in task_set]
        retval["tasks"] = tasks
        return retval

    def edit(self, args):
        json_obj = json.loads(args)
        self.goal = json_obj["goal"]
        self.done = json_obj["done"]
        date = json_obj["deadline"].split("-")
        self.deadline = datetime.datetime(date[2], date[1], date[0])

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
    