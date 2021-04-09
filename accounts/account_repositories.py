from DB_CP.session_manager import Session_Manager
from .models import Users


class UsersRepository:
    def __init__(self, role):
        self.role = role
        session_manager = Session_Manager()
        session_manager.setRole(role)
        self.session = session_manager.getSession()

    def __del__(self):
        self.session.close()

    def findUserByName(self, username):
        return self.session.query(Users).filter(Users.nickname == username).first()

    def addUser(self, User):
        self.session.add(User)
        self.session.commit()
