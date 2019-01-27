import json
from django.db import models
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from task.models import Task
from goal.models import Goal
from datetime import date

class User(models.Model):
    username = models.CharField(default="user", max_length=100)
    password = models.CharField(default="1234", max_length=100)
    
    deviceID = models.TextField(default = "abc123abc")

    ical = models.TextField()

    def in_json(self):
        print("HLLOE" + self.username)
        retval = {}
        retval["Name"] = self.username

        tasks = []
        q_set = Task.objects.all().filter(Q(user__exact=self))
        for t in q_set:
            tasks.append(t.id)
        retval["tasks"] = tasks

        goals = []
        q_set = Goal.objects.all().filter(Q(user__exact=self))
        for g in q_set:
            goals.append(g.id)
        retval["Goal"] = goals

        print("retval is " + retval.__str__())

        return retval

    def get_ical(self):
        return self.ical
    
    def edit_ical(self, args):
        json_obj = json.loads(args)
        self.ical = json_obj["ical"]
        self.save()

def user_exists(user_id):
    retval = {}
    try:
        temp_obj = User.objects.get(pk=user_id)
        return True
    except ObjectDoesNotExist:
        return False

def create_user(body):
    user = User(username=body["username"])
    user.save()
    return user.id

def create_task_with_goal(args, goal_id):
    print("ran2")
    arg_dict = json.loads(args)
    deadline_string = arg_dict["deadline"]
    deadline_list = deadline_string.split('-')
    day = int(deadline[0])
    month = int(deadline[1])
    year = int(deadline[2])
    task = Task(description=arg_dict["task"],\
                deadline=date(year, month, day),\
                done=arg_dict["done"],\
                goal=Goal.objects.get(pk=goal_id),\
                user=None)
    task.user = None
    task.save()
    return task.inJson()

def create_task_without_goal(args, user_id):
    print("Ran")
    print(args)
    arg_dict = json.loads(args)
    deadline_string = arg_dict["deadline"]
    deadline_list = deadline_string.split('-')
    day = int(deadline_list[0])
    month = int(deadline_list[1])
    year = int(deadline_list[2])
    task = Task(description=arg_dict["task"],\
                deadline=date(year, month, day),\
                done=arg_dict["done"],\
                goal=None,\
                user=User.objects.get(pk=user_id))
    task.goal = None
    task.save()
    return task.inJson()
