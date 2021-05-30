from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import LoginForm, RegistrateForm
from .BL import *


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            request.session['role'] = get_role(username)
            request.session['username'] = username
            return redirect('/success')
    else:
        form = LoginForm()
    return render(request, '../templates/registration/login.html', {'form': form})


def logout(request):
    request.session['role'] = 0
    request.session['username'] = ''
    return redirect('/success')


def registration(request):
    if request.method == 'POST':
        form = RegistrateForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            addUser(username, password, request.session['role'])
            request.session['username'] = username
            request.session['role'] = 1
            return redirect('/success')
    else:
        form = RegistrateForm()
        return render(request, '../templates/registration/registration.html', {'form': form})


def setUserRole(request):
    if request.method == 'POST':
        if request.POST.get('newrole') == 'Зарегистрированный пользователь':
            updateUserRole(request.POST.get('username'), 1, request.session['role'])
        elif request.POST.get('newrole') == 'Гид':
            updateUserRole(request.POST.get('username'), 2, request.session['role'])
        else:
            updateUserRole(request.POST.get('username'), 3, request.session['role'])
        #updateUserRole(request.POST.get('role'))
    return redirect('home')


def UserRoles(request):
    if request.method == 'GET':
        users = getAllUsers(request.session['role'])
        print(users)
        role1 = Roles(1, 'Зарегистрированный пользователь')
        role2 = Roles(2, 'Гид')
        role3 = Roles(3, 'Админ')
        roles = [role1, role2, role3]
        print(roles)
        return render(request, '../templates/updateRole.html', {'users': users, 'roles': roles})
    else:
        return redirect('home')