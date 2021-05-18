from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import createExcursionForm, createSightForm, createGuideForm
from .BL import *


def startpage(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def createExcursion(request):
    guides = getAllGuides()
    if request.session['role'] > 1:
        form = createExcursionForm(guides=guides)
    else:
        return redirect('/home')
    if request.method == "POST":
        excursion_name = request.POST.get("name")
        description = request.POST.get("description")
        guide_num = request.POST['guides']
        guide = guides[int(guide_num)]
        name = guide.first_name
        surname = guide.last_name
        patronymic = guide.patronymic
        price = request.POST.get("price")
        addExcursion(excursion_name, description, name, surname, patronymic, price)
        return HttpResponse("Harosh")
    else:
        return render(request, '../templates/excursions/create_excursion.html',
                      {'form': form, 'guides': guides})



def createSight(request):

    if request.method == "POST":
        form = createSightForm(request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            build_date = request.POST.get("build_date")
            type = request.POST.get("type")
            author = request.POST.get("author")
            description = request.POST.get("description")

            addSight(name, build_date, type, author, description)
            #vot tut eshe nado podumat s perehodami
            return HttpResponse('URA URA')
    else:
        if request.session['role'] > 1:
            form = createSightForm()
        else:
            return redirect('/home')
    return render(request, '../templates/excursions/create_sight.html', {'form': form})

def createGuide(request):

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        patronymic = request.POST.get("patronymic")
        qualification = request.POST.get("qualification")
        biography = request.POST.get("biography")
        experience = request.POST.get("experience")

        addGuide(first_name, last_name, patronymic, qualification, biography, experience)
        return HttpResponse("Harosh")
    else:
        if request.session['role'] > 1:
            form = createGuideForm()
        else:
            return redirect('/home')
    return render(request, '../templates/excursions/create_guide.html', {'form': form})


def watch_excursions(request):
    excursions = getAllExcursions()
    for el in excursions:
        guide = getGuideById(el.guide)
        el.guide = guide.first_name + " " + guide.last_name + " " + guide.patronymic
    if request.method == "GET":
        return render(request, '../templates/excursions/watch_excursions.html', {'excursions': excursions})
    else:
        print(request.POST)
        return render(request, '../templates/excursions/watch_excursions.html', {'excursions': excursions})
