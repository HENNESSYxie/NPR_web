import datetime

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import Point
import pytz


@login_required(login_url='/account/login')
def index(request):
    return render(request, 'carRegister/index.html')


@login_required(login_url='/account/login')
def save_point(request):
    if request.method == "POST":
        x = request.POST.get("x")
        y = request.POST.get("y")
        camera = request.POST.get("camera")
        x_relative = request.POST.get('x_relative')
        point = Point.objects.create(x=x, y=y, camera=camera, x_relative=x_relative, date=datetime.datetime.now(pytz.timezone("Asia/Yekaterinburg")))
        point.save()
        return HttpResponse('OK')


@login_required(login_url='/account/login')
def last_point(request):
    camera = request.GET.get('camera', None)
    if camera is not None:
        point = Point.objects.filter(camera=int(camera)).order_by('-id').first()
        if point is not None:
            response_data = {'x': point.x, 'y': point.y}
            return JsonResponse(response_data)
    return JsonResponse({'error': 'Invalid request'})

