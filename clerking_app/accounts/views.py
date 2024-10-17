import random
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# internal imports 
from .models import User, User_Profile
from .serializers import User_Profile_Serializer, UserSerializer


# create the workflow for the creation of a user and userprofile it should return jwt 
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()

            # Create User_Profile
            profile_data = {
                'user': user.id,
                'first_name': request.data.get('first_name'),
                'last_name': request.data.get('last_name'),
                'school': request.data.get('school'),
                'gender': request.data.get('gender'),
            }
            profile_serializer = User_Profile_Serializer(data=profile_data)
            profile_serializer.is_valid(raise_exception=True)
            profile_serializer.save()

            refresh = RefreshToken.for_user(user)

            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "profile": profile_serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# login view
class LoginView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            try:
                user_profile = User_Profile.objects.get(user=user)
                profile_serializer = User_Profile_Serializer(user_profile)
                return Response({
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "user_profile": profile_serializer.data
                }, status=status.HTTP_200_OK)
            except User_Profile.DoesNotExist:
                return Response({"error": "User profile not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)