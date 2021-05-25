from .models import Guides
from .guides_repositories import GuidesRepository

def addGuide(first_name, last_name, patronymic, qualification, biography, experience):
    guideRep = GuidesRepository(2)
    guideRep.addGuide(Guides(first_name, last_name, patronymic, qualification, biography, experience))

def getGuidebyFIO(name, surname, patronymic):
    guidesRep = GuidesRepository(2)
    return guidesRep.findGuideByFIO(name, surname, patronymic)

def getGuideById(id):
    guideRep = GuidesRepository(2)
    return guideRep.findGuideById(id)

def getAllGuides():
    guidesRep = GuidesRepository(2)
    return guidesRep.getAllGuides()
