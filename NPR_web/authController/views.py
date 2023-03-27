from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_p(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return render(request, 'carRegister/index.html')
        else:
            return render(request, 'authController/login.html', {'error': 'Неверный логин/пароль!'})
    return render(request, 'authController/login.html', {'error': ''})


@login_required(login_url='/account/login')
def logout_p(request):
    logout(request)
    return redirect('/')
