from django.db import models
from django.db.models import Q

class User(models.Model):
    username = models.CharField(default="user", max_length=100)
    password = models.CharField(default="1234", max_length=100)
    
    deviceID = models.TextField(default = "abc123abc")

    ical = models.TextField()

    def in_json(self):
        retval = {}
        retval["Name"] = self.username

        tasks = []
        q_set = Tasks.objects.all().filter(Q(user__exact=self))
        for t in q_set:
            tasks.append(t.id)
        retval["tasks"] = tasks

        goals = []
        q_set = Goals.objects.all().filter(Q(user__exact=self))
        for g in q_set:
            goals.append(g.id)
        retval["Goal"] = goals

        return retval

    def get_ical(self):
        return self.ical
    
    def edit_ical(self, args):
        json_obj = json.loads(args)
        self.ical = json_obj["ical"]
        self.save()
    
    # TODO Fix the implementation
    def edit_user(self, args):
        json_obj = json.loads(args)
        if "name" in json_obj:
            self.name = json_obj["name"]
        if "tasks" in json_obj:
            self.name = json_obj["name"]
        if "name" in json_obj:
            self.name = json_obj["name"]
        if "name" in json_obj:
            self.name = json_obj["name"]

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