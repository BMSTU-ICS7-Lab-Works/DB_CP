from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import LoginForm, RegistrateForm
from .password import *


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            request.session['role'] = get_role(username)
            return HttpResponse('URA URA')
    else:
        form = LoginForm()
    return render(request, '../templates/registration/login.html', {'form': form})


def logout(request):
    request.session['role'] = 0
    return redirect('/home')


def registration(request):
    if request.method == 'POST':
        form = RegistrateForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            addUser(username, password)
            request.session['role'] = 1
            return HttpResponse('URA URA')
    else:
        form = RegistrateForm()
    return render(request, '../templates/registration/registration.html', {'form': form})

