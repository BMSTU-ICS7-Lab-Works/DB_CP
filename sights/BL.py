from .models import Sights
from .sights_repositories import SightsRepository

def addSight(name, build_date, type, author, description):
    sightRep = SightsRepository(2)
    sightRep.addSight(Sights(name, build_date, type, author, description))

def getSightbyId(id):
    sightRep = SightsRepository(2)
    return sightRep.findSightById(id)

def getSightbyName(name):
    sightRep = SightsRepository(2)
    return sightRep.findSightByName(name)

def getAllSights():
    sightRep = SightsRepository(2)
    return sightRep.findAllSights()

