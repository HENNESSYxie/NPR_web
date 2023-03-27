from django.urls import path, include
from .views import login_p

urlpatterns = [
    path('', login_p)
]
