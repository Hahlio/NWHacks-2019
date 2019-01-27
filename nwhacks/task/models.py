from django.db import models
import json
from django.core.exceptions import ObjectDoesNotExist

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
    task = Task(description=arg_dict["description"],\
                deadline=arg_dict["deadline"],\
                done=arg_dict["done"])
    task.save()
    return task.inJson()

    
def update_task(args, task_id):
    task = Task.objects.get(pk=task_id)
    arg_dict = json.loads(args)
    task.description = arg_dict["description"]
    task.deadline = arg_dict["deadline"]
    task.done = arg_dict["done"]
    task.save()
    return task.inJson()


def is_valid_id(task_id):
    try:
        Task.objects.get(pk=task_id)
        return True
    except ObjectDoesNotExist:
        return False