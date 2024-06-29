from django.db import models
from django.contrib.auth.models import User
# I want to extend django's user model to contain some additional fields 


class School(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


