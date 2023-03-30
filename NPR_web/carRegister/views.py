import datetime
import cv2
from django.http import JsonResponse, StreamingHttpResponse
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators import gzip
from .models import Point, CarRegister
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


@login_required(login_url='/account/login')
def actions_history(request):
    car_register = CarRegister.objects.all()
    return render(request, 'carRegister/actions-history.html', {'objects': car_register})


class MyModelDetailView(LoginRequiredMixin, DetailView):
    login_url = '/account/login'
    model = CarRegister
    template_name = 'carRegister/actions-detail.html'
    context_object_name = 'item'


@login_required(login_url='/account/login')
@gzip.gzip_page
def video_feed(request):
    cap = cv2.VideoCapture(0)

    def video_stream():
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            _, buffer = cv2.imencode('.jpg', cv2.flip(cv2.resize(frame, (800, 600)), 1))

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
    return StreamingHttpResponse(video_stream(), content_type='multipart/x-mixed-replace; boundary=frame')


@login_required(login_url='/account/login')
@gzip.gzip_page
def video_feed2(request):
    cap = cv2.VideoCapture(0)

    def video_stream():
        while True:
            ret, frame = cap.read()

            if not ret:
                break

            _, buffer = cv2.imencode('.jpg', cv2.flip(cv2.resize(frame, (800, 600)), 1))

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
    return StreamingHttpResponse(video_stream(), content_type='multipart/x-mixed-replace; boundary=frame')

