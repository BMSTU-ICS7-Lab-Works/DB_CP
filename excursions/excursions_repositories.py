from DB_CP.session_manager import Session_Manager
from .models import Sights, Excursions, SightsExcursions


class SightsRepository:
    def __init__(self, role):
        self.role = role
        session_manager = Session_Manager()
        session_manager.setRole(role)
        self.session = session_manager.getSession()

    def __del__(self):
        self.session.close()

    def findSightByName(self, name):
        return self.session.query(Sights).filter(Sights.name == name).first()

    def addSight(self, Sight):
        self.session.add(Sight)
        self.session.commit()
