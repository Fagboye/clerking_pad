# importin the required libraries, models and serializers
from datetime import datetime
from rest_framework.serializers import ModelSerializer
from .models import User_Profile, User, School  
from django.conf import settings

# creatiing the serializer for th user model 
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'roles']


# creating the serializer for the user profile model
class User_Profile_Serializer(ModelSerializer):
    class Meta:
        model = User_Profile
        fields = '__all__'


# creating the serializer for the school model 
class School_Serializer(ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'