from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
    return render(request, '../templates/home.html')