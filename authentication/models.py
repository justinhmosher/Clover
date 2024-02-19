from django.db import models

class Question(models.Model):
    your_primary_key = models.AutoField(primary_key=True)
    email = models.CharField(max_length = 100, default = "username")
    complete = models.BooleanField(default = False)
    numteams = models.IntegerField(default = 0)
    def __str__(self):
        return f"{self.username}"
