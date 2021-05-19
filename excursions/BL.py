from .models import Excursions, SightsExcursions
from guides.guides_repositories import GuidesRepository
from .excursions_repositories import ExcursionsRepository, SightsExcursionsRepository

from sights.BL import getSightbyId


def addExcursion(name, description, guide_name, guide_surname, guide_patronymic, price):
    guideRep = GuidesRepository(2)
    guide = guideRep.findGuideByFIO(guide_name, guide_surname, guide_patronymic)
    excursionRep = ExcursionsRepository(2)
    excursionRep.addExcursion(Excursions(name, description, guide.id, price))


def getAllExcursions():
    excursionRep = ExcursionsRepository(2)
    return excursionRep.getAllExcursions()

def getSightsbyExcursion(excursion):
    SERep = SightsExcursionsRepository(2)
    res = SERep.getSightsbyExcursion(excursion)

    fres = []
    for el in res:
        for id in el:
            fres.append(getSightbyId(id))
    return fres



