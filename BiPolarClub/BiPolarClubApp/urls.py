from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getResources/', views.getResources, name='resources'),
    path('getMeeting/', views.getMeeting, name='meeting'),
    path('meetingDetails/<int:id>', views.meetingDetails, name='meetingdetails'),
]