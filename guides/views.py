from django.http import HttpResponse
from django.shortcuts import render, redirect

from .BL import *
from .forms import createGuideForm


def detail(request, guide_fio):
    guide_fio = guide_fio.split(' ')
    name = guide_fio[0]
    surname = guide_fio[1]
    patronymic = guide_fio[2]
    guide = getGuidebyFIO(name, surname, patronymic, request.session['role'])
    return render(request, '../templates/guides/guide_page.html',
                          {'guide': guide})


def createGuide(request):

    if request.method == "POST":
        form = createGuideForm(request.POST)
        if form.is_valid():
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            patronymic = request.POST.get("patronymic")
            qualification = request.POST.get("qualification")
            biography = request.POST.get("biography")
            experience = request.POST.get("experience")

            addGuide(first_name, last_name, patronymic, qualification, biography, experience, request.session['role'])
            return redirect('/success')
    else:
        if request.session['role'] > 2:
            form = createGuideForm()
        else:
            return redirect('/home')
    return render(request, '../templates/guides/create_guide.html', {'form': form})
