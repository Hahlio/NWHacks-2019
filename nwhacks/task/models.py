from django.db import models
import json
from django.core.exceptions import ObjectDoesNotExist
from datetime import date

# Create your models here.

class Task(models.Model):
    description = models.CharField(default="", max_length=100)
    deadline = models.DateField()
    done = models.BooleanField(default=False)

    def inJson(self):
        task_dict = {
            "task_id": self.id,
            "description": self.description,
            "deadline" : self.deadline.__str__(),
            "done" : self.done
        }
        return task_dict


def create_task(args):
    arg_dict = json.loads(args)
    deadline_string = arg_dict["deadline"]
    deadline_list = deadline_string.split('-')
    day = int(deadline[0])
    month = int(deadline[1])
    year = int(deadline[2])
    task = Task(description=arg_dict["description"],\
                deadline=date(day, month, year),\
                done=arg_dict["done"])
    task.save()
    return task.inJson()

    
def update_task(args, task_id):
    task = Task.objects.get(pk=task_id)
    arg_dict = json.loads(args)
    deadline_string = arg_dict["deadline"]
    deadline_list = deadline_string.split('-')
    day = int(deadline[0])
    month = int(deadline[1])
    year = int(deadline[2])
    task.description = arg_dict["description"]
    task.deadline = date(day, month, year)
    task.done = arg_dict["done"]
    task.save()
    return task.inJson()


def is_valid_id(task_id):
    try:
        Task.objects.get(pk=task_id)
        return True
    except ObjectDoesNotExist:
        return False