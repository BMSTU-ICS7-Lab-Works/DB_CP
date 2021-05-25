from .models import Excursions, Schedule
from guides.guides_repositories import GuidesRepository
from .excursions_repositories import ExcursionsRepository, SightsExcursionsRepository, ScheduleRepository, SelectedExcursionsRepository

from sights.BL import getSightbyId


def addExcursion(name, description, guide_name, guide_surname, guide_patronymic, price):
    guideRep = GuidesRepository(2)
    guide = guideRep.findGuideByFIO(guide_name, guide_surname, guide_patronymic)
    excursionRep = ExcursionsRepository(2)
    excursionRep.addExcursion(Excursions(name, description, guide.id, price))

def addSchedule(excursion_id, date, time):
    scheduleRep = ScheduleRepository(2)
    scheduleRep.addSchedule(Schedule(excursion_id, date, time))

def addSelectedExcursionsRel(userId, scheduleId, date):
    selectedRep = SelectedExcursionsRepository(2)
    selectedRep.addRel(userId, scheduleId, date)

def addSightExcursionRel(sight_id, exc_id):
    SightsExcursionsRep = SightsExcursionsRepository(2)
    SightsExcursionsRep.addRel(sight_id, exc_id)

def getExcursionByName(name):
    excursionsRep = ExcursionsRepository(2)
    return excursionsRep.findExcursionByName(name)


def getScheduleByExcursion(excursion_name):
    excursion = getExcursionByName(excursion_name)
    ScheduleRep = ScheduleRepository(2)
    return ScheduleRep.findScheduleByExcursion(excursion)

def getAllExcursions():
    excursionRep = ExcursionsRepository(2)
    return excursionRep.findAllExcursions()

def getSightsbyExcursion(excursion):
    SERep = SightsExcursionsRepository(2)
    res = SERep.getSightsbyExcursion(excursion)

    fres = []
    for el in res:
        for id in el:
            fres.append(getSightbyId(id))
    return fres




def filltime():
    res = {}
    for i in range(0, 24):
        if i < 10:
            res['0' + str(i) +':00'] = '0' + str(i) +':00'
            res['0' + str(i) + ':30'] = '0' + str(i) +':30'
        else:
            res[str(i) +':00'] = str(i) +':00'
            res[str(i) +':30'] = str(i) +':30'
    return res.items()
