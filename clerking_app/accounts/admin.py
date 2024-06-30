from django.contrib import admin
from .models import User_Profile, User, School
# Register your models here.


admin.site.register(User_Profile)
admin.site.register(User)
admin.site.register(School)