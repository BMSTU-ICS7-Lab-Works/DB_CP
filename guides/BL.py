from excursions.models import Guides
from .guides_repositories import GuidesRepository

def addGuide(first_name, last_name, patronymic, qualification, biography, experience, role):
    guideRep = GuidesRepository(role)
    guideRep.addGuide(Guides(first_name, last_name, patronymic, qualification, biography, experience))

def getGuidebyFIO(name, surname, patronymic, role):
    guidesRep = GuidesRepository(role)
    return guidesRep.findGuideByFIO(name, surname, patronymic)

def getGuideById(id, role):
    guideRep = GuidesRepository(role)
    return guideRep.findGuideById(id)

def getAllGuides(role):
    guidesRep = GuidesRepository(role)
    return guidesRep.getAllGuides()
