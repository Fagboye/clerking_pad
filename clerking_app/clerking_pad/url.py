from django.urls import path, repath 

from .views import *


urlpatterns = [
    path('im-clerking/', IM_Clerking_View.as_view(), name='im_clerking_create'),
    path('surgery-clerking/', Surgery_Clerking_View.as_view(), name='surgery_clerking_create'),
    path('clerkings/', Clerking_View_List.as_view(), name='clerking_list'),
    path('clerking/<int:id>/', Clerking_View.as_view(), name='clerking_detail')
]