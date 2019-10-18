from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('list_tasks/', list_tasks, name='list_tasks'),
]
