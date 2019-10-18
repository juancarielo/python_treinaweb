from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('list/', list, name='list'),
    path('create/', create, name='create'),
    path('edit/<int:id>', edit, name='edit'),
    path('delete/<int:id>', delete, name='delete'),
]
