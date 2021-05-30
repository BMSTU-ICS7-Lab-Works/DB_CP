import datetime

from DB_CP.sessionmanager import SessionManager
from .models import Excursions, SightsExcursions, Schedule, SelectedExcursions


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

    def findAllExcursions(self):
        return self.session.query(Excursions).all()


class SightsExcursionsRepository:
    def __init__(self, role):
        self.role = role
        session_manager = SessionManager()
        session_manager.setRole(role)
        self.session = session_manager.getSession()

    def __del__(self):
        self.session.close()

    def addRel(self, sightId, excId):
        insertion = SightsExcursions.insert().values(sightsId=sightId, excursionsId=excId)
        self.session.execute(insertion)
        self.session.commit()
    #
    # def findGuideById(self, id):
    #     return self.session.query(Guides).filter(Guides.id == id).first()

    def getSightsbyExcursion(self, excursion):
        return self.session.query(SightsExcursions).filter_by(excursionsId = excursion.id).with_entities(SightsExcursions.c.sightsId).all()


class SelectedExcursionsRepository:
    def __init__(self, role):
        self.role = role
        session_manager = SessionManager()
        session_manager.setRole(role)
        self.session = session_manager.getSession()

    def __del__(self):
        self.session.close()

    def addRel(self, userId, scheduleId, date):
        insertion = SelectedExcursions.insert().values(userId=userId, scheduleId=scheduleId, date=date)
        self.session.execute(insertion)
        self.session.commit()
    #
    # def findGuideById(self, id):
    #     return self.session.query(Guides).filter(Guides.id == id).first()

    # def getSightsbyExcursion(self, excursion):
    #     return self.session.query(SightsExcursions).filter_by(excursionsId = excursion.id).with_entities(SightsExcursions.c.sightsId).all()


class ScheduleRepository:
    def __init__(self, role):
        self.role = role
        session_manager = SessionManager()
        session_manager.setRole(role)
        self.session = session_manager.getSession()

    def __del__(self):
        self.session.close()

    def addSchedule(self, schedule):
        self.session.add(schedule)
        self.session.commit()

    def findScheduleByExcursion(self, excursion):
        return self.session.query(Schedule).filter_by(excursion=excursion.id).all()

    def deletePastExcursions(self):
        self.session.query(SelectedExcursions).filter(SelectedExcursions.c.date < datetime.datetime.today().date()).delete()
        self.session.commit()
    #
    # def findGuideById(self, id):
    #     return self.session.query(Guides).filter(Guides.id == id).first()

    # def getSightsbyExcursion(self, excursion):
    #     return self.session.query(SightsExcursions).filter_by(excursionsId = excursion.id).with_entities(SightsExcursions.c.sightsId).all()