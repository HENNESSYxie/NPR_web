from django.contrib import admin
from .models import Point, CarRegister, WhiteList

# Register your models here.
admin.site.register(Point)
admin.site.register(WhiteList)
admin.site.register(CarRegister)
