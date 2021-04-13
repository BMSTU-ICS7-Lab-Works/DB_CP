from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class SessionManager():

    admin_engine = create_engine("postgresql+psycopg2://postgres:1@localhost/Excursions")
    unlogged_engine = create_engine("postgresql+psycopg2://postgres:1@localhost/Excursions")
    logged_engine = create_engine("postgresql+psycopg2://postgres:1@localhost/Excursions")

    def __init__(self):
        self.role = 0
        self.sessionmaker = sessionmaker(bind=self.unlogged_engine)
        self.session = self.sessionmaker()

    def setRole(self, role):
        if 0 <= role <= 3:
            self.role = role
        else:
            raise Exception("Wrong role")

    def getSession(self):
        if self.role == 0:
            self.sessionmaker = sessionmaker(bind=self.admin_engine)
            self.session = self.sessionmaker()
            return self.session
        elif self.role == 1:
            self.sessionmaker = sessionmaker(bind=self.unlogged_engine)
            self.session = self.sessionmaker()
            return self.session
        elif self.role == 2:
            self.sessionmaker = sessionmaker(bind=self.logged_engine)
            self.session = self.sessionmaker()
            return self.session
        else:
            raise Exception("Wrong role")

