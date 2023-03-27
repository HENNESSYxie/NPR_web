from django.urls import path, include
from .views import login_p, logout_p

urlpatterns = [
    path('login/', login_p),
    path('logout/', logout_p)
]
