from django.db import models
from django.contrib.auth.models import User


# table for clerking
class Clerking(models.Model):
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    marital_status_choices = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
    ]

    religion_choices = [
        ('christian', 'Christian'),
        ('muslim', 'Muslim'),
        ('other', 'Other'),
    ]
    tribe_choices = [
        ('igbo', 'Igbo'),
        ('hausa', 'Hausa'),
        ('yoruba', 'Yoruba'),
        ('other', 'Other'),
    ]
    department_choices = [
        ('im', 'Internal Medicine'),
        ('surgery', 'Surgery')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Patient's biodata
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=gender_choices)
    occupation = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=10, choices=marital_status_choices)
    home_address = models.CharField(max_length=100)
    religion = models.CharField(max_length=10, choices=religion_choices)
    tribe = models.CharField(max_length=10, choices=tribe_choices)

    # General History 
    chief_complaint = models.TextField()
    history_of_present_illness = models.TextField()
    past_medical_history = models.TextField()
    past_surgical_history = models.TextField()
    family_history = models.TextField()
    social_history = models.TextField()

    # Examination
    general_examination = models.TextField()
    chest_examination = models.TextField(blank=True, null=True)
    cardiovascular_examination = models.TextField(blank=True, null=True)
    abdominal_examination = models.TextField(blank=True, null=True)
    neurological_examination = models.TextField(blank=True, null=True)
    musculoskeletal_examination = models.TextField(blank=True, null=True)

    # assesement
    assessment = models.TextField(blank=True, null=True)

   
