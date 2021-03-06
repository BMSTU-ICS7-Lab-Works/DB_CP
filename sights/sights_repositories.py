from DB_CP.sessionmanager import SessionManager
from excursions.models import Sights


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

    def findSightById(self, id):
        return self.session.query(Sights).filter(Sights.id == id).first()

    def findAllSights(self):
        return self.session.query(Sights).all()

    def addSight(self, sight):
        print(self.session)
        self.session.add(sight)
        self.session.commit()
