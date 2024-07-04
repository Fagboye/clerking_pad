from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('register/', CreateUserView.as_view()),
    path('login/', LoginView.as_view()),
]