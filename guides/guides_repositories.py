from DB_CP.sessionmanager import SessionManager
from .models import Guides

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

    def findGuideById(self, id):
        return self.session.query(Guides).filter(Guides.id == id).first()

    def getAllGuides(self):
        return self.session.query(Guides).all()