from DB_CP.sessionmanager import SessionManager
from excursions.models import Users


class UsersRepository:
    def __init__(self, role):
        self.role = role
        session_manager = SessionManager()
        session_manager.setRole(role)
        self.session = session_manager.getSession()

    def __del__(self):
        self.session.close()

    def findUserByName(self, username):
        return self.session.query(Users).filter(Users.nickname == username).first()

    def addUser(self, user):
        self.session.add(user)
        self.session.commit()

    def changeRole(self, username, roleset):
        self.session.query(Users).filter(Users.nickname == username).update({Users.role: roleset})
        self.session.commit()

    def findAllUsers(self):
        return self.session.query(Users).all()
