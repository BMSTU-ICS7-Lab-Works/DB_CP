from .models import Sights, Excursions, SightsExcursions, Guides
from .excursions_repositories import SightsRepository, ExcursionsRepository, GuidesRepository


def addSight(name, build_date, type, author, description):
    sightRep = SightsRepository(2)
    sightRep.addSight(Sights(name, build_date, type, author, description))


def addExcursion(name, description, guide_name, guide_surname, guide_patronymic, price):
    guideRep = GuidesRepository(2)
    guide = guideRep.findGuideByFIO(guide_name, guide_surname, guide_patronymic)
    excursionRep = ExcursionsRepository(2)
    excursionRep.addExcursion(Excursions(name, description, guide.id, price))


def addGuide(first_name, last_name, patronymic, qualification, biography, experience):
    guideRep = GuidesRepository(2)
    guideRep.addGuide(Guides(first_name, last_name, patronymic, qualification, biography, experience))
