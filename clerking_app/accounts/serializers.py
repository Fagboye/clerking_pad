# importin the required libraries, models and serializers
from datetime import datetime
from rest_framework.serializers import ModelSerializer
from .models import User_Profile, User
from django.conf import settings

# creatiing the serializer for th user model 
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'role']
        extra_kwargs = {'password': {'write_only': True}}


# creating the serializer for the user profile model
class User_Profile_Serializer(ModelSerializer):
    class Meta:
        model = User_Profile
        fields = '__all__'