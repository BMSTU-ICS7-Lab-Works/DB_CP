from DB_CP.sessionmanager import SessionManager
from .models import Excursions, SightsExcursions


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

    def getAllExcursions(self):
        return self.session.query(Excursions).all()

class SightsExcursionsRepository:
    def __init__(self, role):
        self.role = role
        session_manager = SessionManager()
        session_manager.setRole(role)
        self.session = session_manager.getSession()

    def __del__(self):
        self.session.close()

    # def addGuide(self, guide):
    #     self.session.add(guide)
    #     self.session.commit()
    #
    # def findGuideById(self, id):
    #     return self.session.query(Guides).filter(Guides.id == id).first()

    def getSightsbyExcursion(self, excursion):
        return self.session.query(SightsExcursions).filter_by(excursionsId = excursion.id).with_entities(SightsExcursions.c.sightsId).all()