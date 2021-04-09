from .models import Sights, Excursions, SightsExcursions
from .excursions_repositories import SightsRepository


def addSight(name, build_date, type, author, description):
    sightRep = SightsRepository(1)
    sightRep.addSight(Sights(name, build_date, type, author, description))