from django.contrib import admin
from .views import index, save_point, last_point, actions_history, MyModelDetailView
from django.urls import path, include


urlpatterns = [
    path('', index),
    path('save_point/', save_point),
    path('last_point/', last_point),
    path('actions-history/', actions_history),
    path('carRegister/<int:pk>/', MyModelDetailView.as_view(), name='actions_detail'),
]
