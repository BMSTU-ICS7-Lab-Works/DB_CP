import simplejson as simplejson
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import createExcursionForm, scheduleSelectForm, timeSelectForm
from json import dumps

from .BL import *
from guides.BL import *
from sights.BL import getAllSights, addSight, getSightbyName
from accounts.password import getUser
import datetime


def startpage(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def addBasisToExcursion(request):
    guides = getAllGuides()
    if request.session['role'] > 1:
        form = createExcursionForm(guides=guides)
    else:
        return redirect('/home')

    if request.method == "POST":
        excursion_name = request.POST.get("name")
        description = request.POST.get("description")
        guide_num = request.POST['guides']
        guide = guides[int(guide_num) - 1]
        name = guide.first_name
        surname = guide.last_name
        patronymic = guide.patronymic
        price = request.POST.get("price")
        addExcursion(excursion_name, description, name, surname, patronymic, price)
        return redirect('addSightToExcursion', excursion_name=excursion_name)
    else:
        return render(request, '../templates/excursions/create_excursion_basis.html',
                      {'form': form, 'guides': guides})


def addSightToExcursion(request, excursion_name):
    if request.session['role'] < 1:
        return redirect('/home')

    if request.method == "POST":
        for el in request.POST:
            if el != 'csrfmiddlewaretoken':
                sight = request.POST.getlist(el)
                sight_name = sight[0]
                # sight_date = sight[1]
                # sight_date = sight_date.split(' ')
                # sight_date[1] = sight_date[1][:-1].zfill(2)
                # sight_date = ' '.join(sight_date)
                # sight_date = datetime.datetime.strptime(sight_date, "%b. %d %Y").date()

                exc = getExcursionByName(excursion_name)
                sight = getSightbyName(sight_name)
                print(sight.id)
                print(exc.id)
                addSightExcursionRel(int(sight.id), int(exc.id))

        return redirect('addScheduleToExcursion', excursion_name=excursion_name)
        #return redirect('/home')
    else:
        if getExcursionByName(name=excursion_name):
            sights = getAllSights()
            return render(request, '../templates/excursions/add_sights_excursions.html',
                          {'sights': sights, 'excursion_name': excursion_name})
        else:
            return redirect('home')



def addScheduleToExcursion(request, excursion_name):
    if request.session['role'] < 1:
        return redirect('/home')

    if request.method == "POST":
        print(request.POST)
        exc = getExcursionByName(excursion_name)
        for el in request.POST:
            if el != 'csrfmiddlewaretoken':
                times = request.POST.getlist(el)
                print(el)

                for time in times:
                    addSchedule(exc.id, el, time)

        return redirect('success')
    else:
        if getExcursionByName(name=excursion_name):
            form = scheduleSelectForm()
            return render(request, '../templates/excursions/add_schedule_excursions.html',
                          {'form': form, 'excursion_name': excursion_name})
        else:
            return redirect('home')

def watch_excursions(request):
    excursions = getAllExcursions()
    sights = []
    schedule = []
    for el in excursions:
        guide = getGuideById(el.guide)
        #time = getTimeByExcId(el.id)
        el.guide = guide.first_name + " " + guide.last_name + " " + guide.patronymic
        sights.append(getSightsbyExcursion(el))
        schedule.append(getScheduleByExcursion(el.name))
    #timeform = timeSelectForm(time=time)
    if request.method == "GET":
        return render(request, '../templates/excursions/watch_excursions.html',
                      {'excursions': excursions, 'sights': sights, 'schedule': schedule})
    else:
        i = 1
        for el in request.POST:
            if el != 'csrfmiddlewaretoken':
                req = request.POST.getlist(el)
                if i % 2:
                    sched = getScheduleByExcursion(req[0])
                    day, time = req[1].split(' ')
                    for s in sched:
                        if s.day == day and s.time == time:
                            sched_id = s.id
                            break
                else:
                    user = getUser(request.session['username'])
                    sched_date = req
                    sched_date[0] = sched_date[0].zfill(2)
                    sched_date = ' '.join(sched_date)
                    sched_date = datetime.datetime.strptime(sched_date, "%d %b %Y").date()
                    print(sched_date)
                    addSelectedExcursionsRel(user.id, sched_id, sched_date)
                i += 1
        return redirect('success')

def chooseSchedule(request, excursion_name):
    schedule = getScheduleByExcursion(excursion_name)
    return render(request, '../templates/excursions/choose_schedule.html', {'schedule':schedule})
