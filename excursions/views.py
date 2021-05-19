from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import createExcursionForm
from .BL import *
from guides.BL import *


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
        return redirect('/success')
    else:
        return render(request, '../templates/excursions/create_excursion.html',
                      {'form': form, 'guides': guides})


def watch_excursions(request):
    excursions = getAllExcursions()
    sights = []
    for el in excursions:
        guide = getGuideById(el.guide)
        el.guide = guide.first_name + " " + guide.last_name + " " + guide.patronymic
        sights.append(getSightsbyExcursion(el))
    if request.method == "GET":
        return render(request, '../templates/excursions/watch_excursions.html', {'excursions': excursions, 'sights': sights})
    else:
        print(request.POST)
        return render(request, '../templates/excursions/watch_excursions.html', {'excursions': excursions, 'sights': sights})
