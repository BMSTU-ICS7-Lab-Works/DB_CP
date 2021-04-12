from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import LoginForm, RegistrateForm
from .password import *


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if check_user_login(username, password):
            request.session['role'] = get_role(username)
            return redirect('/home')
        else:
            return HttpResponse('Durashka')
    else:
        form = LoginForm()
    return render(request, '../templates/registration/login.html', {'form': form})


def logout(request):
    request.session['role'] = 0
    return redirect('/home')


def registration(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        if find_user(username):
            return HttpResponse('takoy chel uje est paka')
        else:
            password = request.POST.get('password')
            if password == request.POST.get('repeat_password'):
                addUser(username, password)
                request.session['role'] = 1

                return redirect('/home')
            else:
                HttpResponse('tut nado AJAX shob pisalo nepralno i povtoryalo')

        return redirect('/home')
    else:
        form = RegistrateForm()
        return render(request, '../templates/registration/registration.html', {'form': form})

