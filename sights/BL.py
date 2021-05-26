from excursions.models import Sights
from .sights_repositories import SightsRepository

def addSight(name, build_date, type, author, description, role):
    sightRep = SightsRepository(role)
    sightRep.addSight(Sights(name, build_date, type, author, description))

def getSightbyId(id, role):
    sightRep = SightsRepository(role)
    return sightRep.findSightById(id)

def getSightbyName(name, role):
    sightRep = SightsRepository(role)
    return sightRep.findSightByName(name)

def getAllSights(role):
    sightRep = SightsRepository(role)
    return sightRep.findAllSights()

