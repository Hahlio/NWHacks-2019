from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(default="John Doe", max_length=100)
    username = models.CharField(default="user", max_length=100)
    password = models.CharField(default="1234", max_length=100)
    
    deviceID = models.TextField(default = "abc123abc")
    
    tasks = models.ManyToManyField(Task)
    goals = models.ManyToManyField(Goal)

    ical = models.TextField()

    def in_json(self):
        retval = {}
        retval["name"] = self.name
        retval["username"] = self.username

        tasks = []

        for t in self.tasks.all():
            tasks.append(t.id)

        retval["task"] = tasks

        goals = []

        for g in self.goals.all():
            goals.append(g.id)

        retval["goals"] = goals

        return retval

    def get_ical(self):
        return self.ical
    
    def edit_ical(self, args):
        json_obj = json.loads(args)
        self.ical = json_obj["ical"]
    
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