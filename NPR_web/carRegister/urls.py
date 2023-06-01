from django.contrib import admin
from .views import index, save_point, last_point, actions_history, MyModelDetailView, video_feed, video_feed2, \
    export_records, add_white, white_list, white_list_delete, add_white_1c, get_white_list_1c, delete_1c, get_actions_history_1c
from django.urls import path, include


urlpatterns = [
    path('', index),
    path('save_point/', save_point),
    path('last_point/', last_point),
    path('actions-history/', actions_history),
    path('carRegister/<int:pk>/', MyModelDetailView.as_view(), name='actions_detail'),
    path('video_feed', video_feed, name='video_feed'),
    path('video_feed2', video_feed2, name='video_feed2'),
    path('export_records/', export_records, name='export_records'),
    path('white_list/', white_list, name='white_list'),
    path('white_list/add_white', add_white, name='add_white'),
    path('white_list/delete/<int:pk>/', white_list_delete, name='white_list_delete'),
    path('white_list/add_white_1c', add_white_1c, name="add_white_1c"),
    path('white_list/get_white_list_1c', get_white_list_1c, name="get_white_list_1c"),
    path('white_list/delete_1c', delete_1c, name="delete_1c"),
    path('white_list/get_actions_history_1c', get_actions_history_1c, name='get_actions_history_1c')
]
