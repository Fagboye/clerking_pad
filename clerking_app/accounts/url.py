from django.urls import path, re_path

from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView
)

urlpatterns = [
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', CreateUserView.as_view(), name='user_registration'),
    path('api/login/', LoginView.as_view(), name='user_login')
]