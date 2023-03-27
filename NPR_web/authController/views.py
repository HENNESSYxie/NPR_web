from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login


def login_p(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponse('Authenticated successfully')
        else:
            return HttpResponse('Invalid login')
    return render(request, 'authController/login.html')
