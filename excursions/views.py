from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import createExcursionForm, createSightForm
from .BL import *

def startpage(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def createExcursion(request):
    if request.method == "POST":
        2
    else:
        if request.session['role'] != 0:
            form = createExcursionForm()
        else:
            return redirect('/home')
    return render(request, '../templates/excursions/create_excursion.html', {'form': form})



def createSight(request):

    if request.method == "POST":
        name = request.POST.get("name")
        build_date = request.POST.get("build_date")
        type = request.POST.get("type")
        author = request.POST.get("author")
        description = request.POST.get("description")

        addSight(name, build_date, type, author, description)
        return HttpResponse("Harosh")
    else:
        if request.session['role'] != 0:
            form = createSightForm()
        else:
            return redirect('/home')
    return render(request, '../templates/excursions/create_sight.html', {'form': form})