from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import createSightForm
from .BL import *

def createSight(request):
    if request.method == "POST":
        form = createSightForm(request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            build_date = request.POST.get("build_date")
            type = request.POST.get("type")
            author = request.POST.get("author")
            description = request.POST.get("description")

            addSight(name, build_date, type, author, description, request.session['role'])
            return redirect('/success')
    else:
        if request.session['role'] > 1:
            form = createSightForm()
        else:
            return redirect('/home')
    return render(request, '../templates/sights/create_sight.html', {'form': form})

def detail(request, sight_id):
    sight = getSightbyId(sight_id, request.session['role'])
    return render(request, '../templates/sights/sight_page.html',
                  {'sight': sight})
