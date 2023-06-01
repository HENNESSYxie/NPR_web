import pytz
import datetime
import cv2
import json
from openpyxl import Workbook
from django.http import JsonResponse, StreamingHttpResponse
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.views.decorators import gzip
from .models import Point, CarRegister, WhiteList
from .forms import WhiteListForm


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
        point = Point.objects.create(x=x, y=y, camera=camera, x_relative=x_relative,
                                     date=datetime.datetime.now(pytz.timezone("Asia/Yekaterinburg")))
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
    objects = {}
    if request.method == 'POST':
        number = request.POST.get('number')
        order = request.POST.get('order')
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        type_of_action = request.POST.get('type_of_action')
        if number:
            number = WhiteList.objects.filter(car_number=number.upper().strip())
            cars = CarRegister.objects.filter(employee__in=number).filter(type_of_action=type_of_action)
        else:
            cars = CarRegister.objects.filter(type_of_action=type_of_action)

        if order == "desc":
            objects["objects"] = cars.order_by('-date')
        else:
            objects["objects"] = cars.order_by('date')

        if date_from:
            objects["objects"] = cars.filter(date__gte=date_from)
        if date_to:
            objects["objects"] = cars.filter(date__lte=date_to)
    else:
        objects["objects"] = CarRegister.objects.all()
    return render(request, 'carRegister/actions-history.html', objects)


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


@login_required(login_url='/account/login')
def export_records(request):
    number = request.GET.get('number')
    order = request.GET.get('order')
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    type_of_action = request.GET.get('type_of_action')
    if number:
        number = WhiteList.objects.filter(car_number=number.upper().strip())
        cars = CarRegister.objects.filter(employee__in=number).filter(type_of_action=type_of_action)
    else:
        cars = CarRegister.objects.filter(type_of_action=type_of_action)
    if order == "desc":
        objects = cars.order_by('-date')
    else:
        objects = cars.order_by('date')

    if date_from:
        objects = objects.filter(date__gte=date_from)
    if date_to:
        objects = objects.filter(date__lte=date_to)
    queryset = objects
    wb = Workbook()
    ws = wb.active
    ws.append(['№', 'Номер автомобиля', 'Марка', 'Модель', "Год выпуска", "Дата", "Тип действия"])

    for i, obj in enumerate(queryset):
        row = [i + 1, obj.employee.car_number, obj.employee.car_mark, obj.employee.car_model, obj.employee.car_year,
               obj.date.strftime('%Y-%m-%d %H:%M:%S'), obj.type_of_action]
        ws.append(row)

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="exported_data.xlsx"'
    wb.save(response)
    return response


@login_required(login_url='/account/login')
def add_white(request):
    error = ''
    if request.method == "POST":
        form = WhiteListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/white_list')
        else:
            error = 'Форма была неверной'

    form = WhiteListForm()
    data = {'form': form,
            'error': error}
    return render(request, 'carRegister/add_white.html', data)


def add_white_1c(request):
    number = request.GET['number']
    name = request.GET['name']
    if WhiteList.objects.filter(car_number=number).exists():
        return HttpResponse("Сотрудник с таким номером присутсвует в базе")
    elif number and name:
        white = WhiteList(car_number=number, name=name)
        white.save()
        return HttpResponse("Данные записаны успешно")
    return HttpResponse("Неверные входные данные")

def get_white_list_1c(request):
    white_list = serializers.serialize('json', WhiteList.objects.all())
    return HttpResponse(white_list, content_type='application/json')


def white_list(request):
    white_list_objs = WhiteList.objects.all()
    return render(request, 'carRegister/white_list.html', {'objects': white_list_objs})

def delete_1c(request):
    number = request.GET['number']
    obj = WhiteList.objects.filter(car_number=number)
    obj.delete()
    return HttpResponse("OK")

def get_actions_history_1c(request):
    actions = CarRegister.objects.all()
    if 'name' in request.GET:
        number = WhiteList.objects.filter(name=request.GET['name'])
        actions = actions.filter(employee__in=number)
    if "date_from" in request.GET:
        actions = actions.filter(date__gte=request.GET['date_from'])
    if "date_to" in request.GET:
        actions = actions.filter(date__lte=request.GET['date_to'])

    result = []
    for act in actions:
        tmp = {'name': act.employee.name, 'number': act.employee.car_number, 'date': str(act.date),
               'type_of_action': act.type_of_action}
        result.append(tmp)
    res = json.dumps(result)
    return HttpResponse(res, content_type='application/json')


@login_required(login_url='/account/login')
def white_list_delete(request, pk):
    obj = WhiteList.objects.filter(id=pk)
    obj.delete()
    return redirect('/white_list')

