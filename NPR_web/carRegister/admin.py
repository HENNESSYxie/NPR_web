from django.contrib import admin
from .models import Point, CarRegister, Employee

# Register your models here.
admin.site.register(Point)
admin.site.register(Employee)
admin.site.register(CarRegister)
