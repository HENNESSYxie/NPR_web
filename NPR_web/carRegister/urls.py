from django.contrib import admin
from .views import index
from django.urls import path, include


urlpatterns = [
    path('', index)
]