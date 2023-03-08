from App2.views import *
from django.urls import path
app_name='Nothing'

urlpatterns=[
    path('Virat/',Virat,name='Virat'),
    path('Jaddu/',Jaddu,name='Jaddu'),
]