from django.db import models
from django.contrib.auth.models import AbstractUser
# I want to extend django's user model to contain some additional fields 


class User(AbstractUser):
    role = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username


class User_Profile(models.Model):
    Gender_selection = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    school = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=Gender_selection, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


