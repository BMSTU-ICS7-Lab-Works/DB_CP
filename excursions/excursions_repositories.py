from DB_CP.sessionmanager import SessionManager
from .models import Sights, Excursions, SightsExcursions, Guides


class SightsRepository:
    def __init__(self, role):
        self.role = role
        session_manager = SessionManager()
        session_manager.setRole(role)
        self.session = session_manager.getSession()

    def __del__(self):
        self.session.close()

    def findSightByName(self, name):
        return self.session.query(Sights).filter(Sights.name == name).first()

    def addSight(self, sight):
        self.session.add(sight)
        self.session.commit()


class ExcursionsRepository:
    def __init__(self, role):
        self.role = role
        session_manager = SessionManager()
        session_manager.setRole(role)
        self.session = session_manager.getSession()

    def __del__(self):
        self.session.close()

    def findExcursionByName(self, name):
        return self.session.query(Excursions).filter(Excursions.name == name).first()

    def addExcursion(self, excursion):
        self.session.add(excursion)
        self.session.commit()


class GuidesRepository:
    def __init__(self, role):
        self.role = role
        session_manager = SessionManager()
        session_manager.setRole(role)
        self.session = session_manager.getSession()

    def __del__(self):
        self.session.close()

    def findGuideByFIO(self, name, surname, patronymic):
        return self.session.query(Guides).filter(Guides.first_name == name).filter(Guides.last_name == surname)\
            .filter(Guides.patronymic == patronymic).first()

    def addGuide(self, guide):
        self.session.add(guide)
        self.session.commit()