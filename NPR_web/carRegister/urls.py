from django.contrib import admin
from .views import index, save_point, last_point
from django.urls import path, include


urlpatterns = [
    path('', index),
    path('save_point/', save_point),
    path('last_point/', last_point)
]